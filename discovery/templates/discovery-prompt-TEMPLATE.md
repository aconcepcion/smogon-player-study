# EMPO DISCOVERY — Paste everything below this line into ChatGPT 5.6 Pro (Deep Research ON)

---

# Research mission — Complete tournament game inventory: Empo (Smogon)

**Today's date: Sunday, July 12, 2026.** This is an ARCHIVAL COLLECTION task on the Smogon forums (forums.smogon.com). No analysis, no commentary on play quality — inventory only.

## Subject
**Empo** — Smogon forums user (profile: smogon.com/forums/members/288721/), #1 on Smogon's Hall of Fame. Trophy anchors to guide your search: Smogon Tour XXX, XXXIII, XXXVI · Official Smogon Tournament XVII · Smogon Masters II · Smogon Premier League X, XI (team) · World Cup of Pokémon XV, XX (team). He has played in MANY more editions than he won — inventory every season he appears in, not just trophy runs. His games are typically played under the handle "Empo" (or close variants) on the smogtours or main Showdown servers.

## Scope — which tournaments count (Tier 1: Smogon trophy singles officials)
Smogon Tour (playoffs at minimum; regular-season games where recorded) · Official Smogon Tournament · Official Ladder Tournament · Smogon Classic · Smogon Grand Slam · Smogon Masters · World Cup of Pokémon · Smogon Premier League · Smogon Champions League · Smogon Snake Draft. Exclude doubles/VGC events, unofficial invitationals, and Premier Leagues outside this list.

## What to produce

### Part A — Career map (markdown)
1. **Activity timeline:** for each year from his first Tier-1 appearance to now — which tournaments he played, approximate game volume, and results density. Identify his peak windows explicitly.
2. **Per-tournament tally:** edition · his individual record where stated in threads · how far he/his team advanced.
3. **Coverage report:** where replays are systematically available (e.g., team-tour weekly threads) vs. missing (deleted, unposted, hidden) — explicit gaps, never silence.

### Part B — Game inventory (machine-readable, THE critical deliverable)
One JSON array inside a single fenced code block. One object per GAME (bo3 sets = one row per game). Schema:

```json
[
  {
    "url": "https://replay.pokemonshowdown.com/smogtours-gen9ou-XXXXXX",
    "tournament": "Smogon Premier League",
    "edition": "XI",
    "stage": "Week 5",
    "date": "2020-02-16",
    "format": "gen8ou",
    "opponent": "OpponentHandle",
    "result": "W",
    "source_thread": "https://www.smogon.com/forums/threads/....",
    "notes": ""
  }
]
```
Field rules: `date` = thread post date if exact game date unknown (say so in notes) · `result` from thread context, `"?"` if unstated · `format` as the replay/thread states it (gen5ou, gen9ou, etc.) · `notes` for anything irregular (alt handle, game 2 of bo3, disputed link).

## Hard constraints (violations make the output unusable)
1. **NEVER construct or guess a replay URL.** Every `url` must be literally copied from a source page you opened. Replay IDs cannot be inferred — a fabricated link poisons the dataset.
2. Every row carries its `source_thread`. No source, no row.
3. A game known to exist whose replay is not posted/found → row with `"url": null` and an explanatory note. Explicit gaps beat silence and beat guesses.
4. The JSON block must parse: no prose inside it, no comments, no trailing commas.
5. Where thread pages are paginated (team-tour weeks span many pages), walk the pages — replays are usually in the week's OP or scattered in posts; both count.
6. Do not stop at recent years: his BW/ORAS/SM-era games matter equally (cross-generation coverage is a primary goal of this corpus).

## Where to look (guidance, not limits)
- Team tours (SPL/WCoP/SCL/Snake): weekly match threads post replays routinely — richest source.
- Smogon Tour: the Smogon Tour subforum; playoff threads carry replays most reliably.
- OST / OLT / Classic / Grand Slam / Masters: bracket and finals threads.
- "Replay archive" threads that some tournaments maintain.
- His forum profile's post history can surface games he posted himself.

## Success criteria
Target: the COMPLETE Tier-1 inventory — expect 60–150+ games for a player of this longevity. Completeness across eras beats polish; we curate later. End Part A with a 5-line summary: total games found · games with live replay links · games logged as replay-missing · era coverage span · biggest gap.
