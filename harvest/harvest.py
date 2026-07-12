#!/usr/bin/env python3
"""
harvest.py - Showdown replay harvester for the Player Study Program.

Consumes the discovery JSON (Part B of a discovery report), pulls each
replay's raw battle log (.log endpoint, HTML fallback) plus metadata
(.json endpoint), validates, and writes a per-player corpus:

    corpus/<player>/games/<replay-id>.log
    corpus/<player>/manifest.json      (one merged record per game)
    corpus/<player>/failures.json      (anything that needs manual follow-up)

Usage:
    python3 harvest.py links.json --out corpus/empo --subject Empo
    python3 harvest.py links.json --out corpus/empo --subject Empo --dry-run
    python3 harvest.py --self-test https://replay.pokemonshowdown.com/<id>

Idempotent: already-downloaded games are skipped (use --refresh to force).
Polite: ~2 requests/second with retries. No dependencies beyond stdlib.
"""
import argparse
import html as htmllib
import json
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

UA = {"User-Agent": "smogon-player-study-harvester/1.0 (personal research tool)"}
SLEEP = 0.6
RETRIES = 3


def http_get(url: str, timeout: int = 25) -> str:
    last_err = None
    for attempt in range(RETRIES):
        try:
            req = Request(url, headers=UA)
            with urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", "replace")
        except HTTPError as e:
            if e.code == 404:
                raise  # deleted/never-existed: no point retrying
            last_err = e
        except URLError as e:
            last_err = e
        time.sleep(1.5 * (attempt + 1))
    raise last_err


def normalize_url(url: str) -> str:
    url = url.strip().split("#")[0].split("?")[0].rstrip("/")
    url = url.replace("http://", "https://")
    return url


def replay_id(url: str) -> str:
    return url.rsplit("/", 1)[-1]


def fetch_log(base_url: str) -> tuple[str, str]:
    """Return (log_text, method). Tries the native .log endpoint, then
    falls back to extracting the battle-log-data block from the HTML page
    (needed for some legacy-era replays)."""
    try:
        text = http_get(base_url + ".log")
        if "|" in text:  # crude sanity: battle protocol lines contain pipes
            return text, "log-endpoint"
    except Exception:
        pass
    page = http_get(base_url)
    m = re.search(
        r'<script[^>]*class="battle-log-data"[^>]*>(.*?)</script>', page, re.S
    )
    if m:
        return htmllib.unescape(m.group(1)).strip(), "html-fallback"
    raise RuntimeError("no battle log found at endpoint or in page HTML")


def fetch_meta(base_url: str) -> dict:
    try:
        return json.loads(http_get(base_url + ".json"))
    except Exception:
        return {}


def players_from_log(log_text: str) -> list[str]:
    return re.findall(r"^\|player\|p[12]\|([^|\n]+)", log_text, re.M)


def validate(log_text: str, meta: dict, subject: str, declared: dict) -> list[str]:
    warnings = []
    turns = len(re.findall(r"^\|turn\|", log_text, re.M))
    if turns == 0:
        warnings.append("SUSPECT: zero turns parsed (empty or malformed log)")
    players = meta.get("players") or players_from_log(log_text)
    if subject and players:
        subj = subject.lower().replace(" ", "")
        if not any(subj in p.lower().replace(" ", "") for p in players):
            warnings.append(
                f"SUSPECT: subject '{subject}' not among players {players} "
                "(alt handle, or wrong link?)"
            )
    fmt_declared = (declared.get("format") or "").lower().replace(" ", "")
    fmt_actual = (meta.get("format") or meta.get("formatid") or "").lower().replace(" ", "")
    if fmt_declared and fmt_actual and fmt_declared not in fmt_actual and fmt_actual not in fmt_declared:
        warnings.append(f"NOTE: declared format {fmt_declared!r} vs actual {fmt_actual!r}")
    return warnings


def run_self_test(url: str) -> int:
    base = normalize_url(url)
    print(f"[self-test] {base}")
    log_text, method = fetch_log(base)
    meta = fetch_meta(base)
    turns = len(re.findall(r"^\|turn\|", log_text, re.M))
    players = meta.get("players") or players_from_log(log_text)
    print(f"  method:  {method}")
    print(f"  players: {players}")
    print(f"  format:  {meta.get('format') or meta.get('formatid') or 'unknown'}")
    print(f"  turns:   {turns}")
    print("  PASS" if turns > 0 and players else "  FAIL")
    return 0 if turns > 0 and players else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("links", nargs="?", help="discovery JSON (array of game rows)")
    ap.add_argument("--out", help="output dir, e.g. corpus/empo")
    ap.add_argument("--subject", default="", help="player name for validation")
    ap.add_argument("--dry-run", action="store_true", help="validate links file only")
    ap.add_argument("--refresh", action="store_true", help="re-download existing games")
    ap.add_argument("--self-test", metavar="URL", help="smoke-test one replay URL and exit")
    args = ap.parse_args()

    if args.self_test:
        return run_self_test(args.self_test)
    if not args.links or not args.out:
        ap.error("links file and --out are required (or use --self-test URL)")

    rows = json.loads(Path(args.links).read_text())
    if not isinstance(rows, list):
        print("ERROR: links file must be a JSON array of game rows"); return 2

    with_url = [r for r in rows if r.get("url")]
    missing = [r for r in rows if not r.get("url")]
    print(f"[load] {len(rows)} rows: {len(with_url)} with replay URLs, "
          f"{len(missing)} logged replay-missing")
    if args.dry_run:
        bad = [r for r in with_url
               if "replay.pokemonshowdown.com" not in r["url"]]
        for r in bad:
            print(f"  NON-STANDARD HOST: {r['url']}")
        print(f"[dry-run] OK — {len(with_url) - len(bad)} standard replay URLs")
        return 0

    out = Path(args.out); games_dir = out / "games"
    games_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out / "manifest.json"
    manifest = (json.loads(manifest_path.read_text())
                if manifest_path.exists() else {})
    failures, done, skipped = [], 0, 0

    for i, row in enumerate(with_url, 1):
        base = normalize_url(row["url"])
        rid = replay_id(base)
        log_path = games_dir / f"{rid}.log"
        if log_path.exists() and rid in manifest and not args.refresh:
            skipped += 1
            continue
        try:
            log_text, method = fetch_log(base)
            meta = fetch_meta(base)
            warnings = validate(log_text, meta, args.subject, row)
            log_path.write_text(log_text)
            record = dict(row)
            record.update({
                "id": rid,
                "url": base,
                "players": meta.get("players") or players_from_log(log_text),
                "format_actual": meta.get("format") or meta.get("formatid"),
                "uploadtime": meta.get("uploadtime"),
                "turns": len(re.findall(r"^\|turn\|", log_text, re.M)),
                "fetch_method": method,
                "warnings": warnings,
            })
            manifest[rid] = record
            done += 1
            flag = " !! " + "; ".join(warnings) if warnings else ""
            print(f"[{i}/{len(with_url)}] OK  {rid} ({record['turns']} turns){flag}")
        except Exception as e:
            failures.append({"row": row, "error": str(e)})
            print(f"[{i}/{len(with_url)}] FAIL {base} — {e}")
        time.sleep(SLEEP)

    manifest_path.write_text(json.dumps(manifest, indent=1))
    (out / "failures.json").write_text(json.dumps(
        {"failures": failures, "replay_missing_rows": missing}, indent=1))
    suspects = sum(1 for r in manifest.values() if r.get("warnings"))
    print(f"\n[done] fetched {done} · skipped(existing) {skipped} · "
          f"failed {len(failures)} · flagged-suspect {suspects} · "
          f"replay-missing(from discovery) {len(missing)}")
    print(f"[out]  {manifest_path} · {out/'failures.json'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
