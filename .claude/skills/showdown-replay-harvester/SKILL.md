# SKILL: showdown-replay-harvester

Pulls Pokémon Showdown replay logs + metadata into the `smogon-player-study` corpus repo, from a discovery-report JSON manifest. The intelligence lives in `harvest.py`; this skill just runs it correctly.

## When to use
Arnold says "harvest <player>" / "run the harvester" / provides a discovery JSON for a player in the Player Study Program.

## Prerequisites
- `python3` ≥ 3.9 on PATH (stdlib only — no pip installs)
- The `smogon-player-study` repo cloned locally; `harvest.py` lives in `harvest/`
- A links manifest: the JSON array from Part B of the player's discovery report, saved as `discovery/<player>-links.json`

## Steps (follow in order)
1. **First run on this machine only — smoke test** against a known-good replay:
   `python3 harvest/harvest.py --self-test https://replay.pokemonshowdown.com/gen9ou-2647633176-8db02itenyenwb6f9e95ypc88cu7s79pw`
   Expect `PASS` with players `['KING丶3266926956今余', 'gaijineagle']` (or similar order) and 46 turns. FAIL → stop, report to the coach.
2. **Validate the manifest:**
   `python3 harvest/harvest.py discovery/<player>-links.json --out corpus/<player> --subject "<Player>" --dry-run`
   Fix any JSON parse errors (usually prose or trailing commas from the researcher — strip them, never invent rows).
3. **Harvest:**
   `python3 harvest/harvest.py discovery/<player>-links.json --out corpus/<player> --subject "<Player>"`
   Runtime ≈ 1 second per game. Idempotent; re-running only fetches what's missing.
4. **Review the summary line.** Report to Arnold: fetched / failed / flagged-suspect / replay-missing counts. Open `corpus/<player>/failures.json` and list anything needing manual follow-up (dead links, wrong-player suspects).
5. **Commit + push:**
   `git add corpus/<player> discovery/ && git commit -m "corpus: <player> harvest (<N> games)" && git push`
6. Tell Arnold the corpus is live and the coach can now read it via `raw.githubusercontent.com/<user>/smogon-player-study/main/corpus/<player>/manifest.json`.

## Rules
- NEVER hand-edit a fetched `.log`. Corpus files are immutable evidence.
- NEVER fabricate or "fix" a replay URL. Failures are reported, not repaired by guessing.
- `--refresh` only when the coach explicitly asks for a re-download.

## Troubleshooting
- 404s: replay deleted — expected for old games; it stays in failures.json as a finding.
- "subject not among players": alt handle or wrong link; flag it, don't delete it.
- Rate-limit or connection errors: the script already retries; if persistent, wait 10 minutes and re-run (idempotency resumes where it stopped).
