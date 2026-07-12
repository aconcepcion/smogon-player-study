#!/usr/bin/env python3
"""
merge_discovery.py - merge N discovery outputs into one harvester manifest.

Takes any number of discovery documents (raw markdown reports from deep-research
runs, or bare JSON arrays), extracts every parseable game-row array, and merges
them into a single harvest-ready manifest with:

  - deduplication by replay ID (URL rows) / by tournament+stage+opponent (null rows)
  - a "sources" list per row (which engines found it) -> corroboration signal
  - field-conflict detection (same game, different claimed result/date/etc.)
  - a merge report (counts per source, corroborated, single-source, conflicts)

Usage:
    python3 merge_discovery.py discovery/raw/empo-*.md \
        --names chatgpt gemini --out discovery/empo-links.json

Deterministic by design: no row is ever invented, repaired-by-guess, or dropped
silently. Unparseable blocks are reported, not patched.
"""
import argparse
import json
import re
import sys
from pathlib import Path

FIELDS = ["tournament", "edition", "stage", "date", "format",
          "opponent", "result", "source_thread", "notes"]


def repair_json(s: str) -> str:
    """Fix the two most common LLM JSON sins without touching content:
    smart quotes and trailing commas."""
    s = (s.replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2018", "'").replace("\u2019", "'"))
    s = re.sub(r",\s*([\]}])", r"\1", s)
    return s


def extract_arrays(text: str, label: str) -> tuple[list, list]:
    """Return (rows, problems). Unions ALL parseable arrays of game-row dicts
    (deep research sometimes splits the inventory across several blocks)."""
    candidates = re.findall(r"```(?:json)?\s*(.*?)```", text, re.S)
    stripped = text.strip()
    if stripped.startswith("["):
        candidates.append(stripped)
    rows, problems = [], []
    for idx, c in enumerate(candidates):
        c = c.strip()
        if "[" not in c:
            continue
        c = c[c.find("["): c.rfind("]") + 1]
        try:
            data = json.loads(repair_json(c))
        except Exception as e:
            if '"url"' in c or '"tournament"' in c:  # looked like data, failed
                problems.append(f"{label}: block #{idx+1} looks like game data "
                                f"but failed to parse ({e})")
            continue
        if (isinstance(data, list) and data
                and all(isinstance(r, dict) for r in data)
                and any(("url" in r or "tournament" in r) for r in data)):
            rows.extend(data)
    return rows, problems


def normalize_url(url: str) -> str:
    url = url.strip().split("#")[0].split("?")[0].rstrip("/")
    return url.replace("http://", "https://")


def rid_of(url: str) -> str:
    return normalize_url(url).rsplit("/", 1)[-1].lower()


def null_key(row: dict) -> str:
    return "|".join(str(row.get(f, "")).strip().lower()
                    for f in ("tournament", "edition", "stage", "opponent"))


def merge_into(base: dict, new: dict, src: str) -> None:
    if src not in base["sources"]:
        base["sources"].append(src)
    for f in FIELDS:
        old_v, new_v = base.get(f), new.get(f)
        old_s = str(old_v).strip() if old_v not in (None, "") else ""
        new_s = str(new_v).strip() if new_v not in (None, "") else ""
        if not old_s and new_s:
            base[f] = new_v
        elif old_s and new_s and f != "notes" and old_s.lower() != new_s.lower():
            base.setdefault("merge_conflicts", []).append(
                f"{f}: {old_s!r} vs {new_s!r} ({src})")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", nargs="+", help="discovery files (md or json)")
    ap.add_argument("--names", nargs="*", default=None,
                    help="source labels, same order as inputs (default: filenames)")
    ap.add_argument("--out", required=True, help="merged manifest path")
    args = ap.parse_args()

    names = args.names or [Path(p).stem for p in args.inputs]
    if len(names) != len(args.inputs):
        print("ERROR: --names count must match inputs"); return 2

    by_rid, null_rows, problems = {}, {}, []
    per_source = {}
    for path, label in zip(args.inputs, names):
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        rows, probs = extract_arrays(text, label)
        problems.extend(probs)
        per_source[label] = len(rows)
        if not rows:
            problems.append(f"{label}: NO parseable game rows found in {path}")
        for row in rows:
            url = row.get("url")
            if url:
                key = rid_of(url)
                if key in by_rid:
                    merge_into(by_rid[key], row, label)
                else:
                    rec = dict(row)
                    rec["url"] = normalize_url(url)
                    rec["sources"] = [label]
                    by_rid[key] = rec
            else:
                key = null_key(row)
                if key in null_rows:
                    merge_into(null_rows[key], row, label)
                else:
                    rec = dict(row); rec["url"] = None
                    rec["sources"] = [label]
                    null_rows[key] = rec

    merged = sorted(by_rid.values(),
                    key=lambda r: (str(r.get("date") or "9999"),
                                   str(r.get("tournament") or "")))
    merged += list(null_rows.values())
    Path(args.out).write_text(json.dumps(merged, indent=1, ensure_ascii=False))

    corroborated = sum(1 for r in by_rid.values() if len(r["sources"]) >= 2)
    conflicts = sum(1 for r in merged if r.get("merge_conflicts"))
    only = {n: sum(1 for r in by_rid.values() if r["sources"] == [n]) for n in names}
    report = {
        "per_source_rows": per_source,
        "unique_games_with_url": len(by_rid),
        "corroborated_by_2plus": corroborated,
        "single_source_only": only,
        "replay_missing_rows": len(null_rows),
        "rows_with_field_conflicts": conflicts,
        "parse_problems": problems,
        "output": args.out,
    }
    Path(args.out).with_name("merge-report.json").write_text(
        json.dumps(report, indent=1))
    print("=== MERGE REPORT ===")
    print(json.dumps(report, indent=1))
    print("====================")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
