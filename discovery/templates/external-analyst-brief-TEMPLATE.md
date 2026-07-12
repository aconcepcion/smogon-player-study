# EXTERNAL ANALYST BRIEF — Paste into ChatGPT 5.6 Pro (code execution ON), with the repo ZIP attached

---

# Independent player profile: Empo (competitive Pokémon, Smogon tournaments)

**Standing constraint, before anything else: do NOT use web browsing or search at any point in this task — even if the capability is available to you.** Every fact must come from the attached files. This is a methodological requirement (an independence-controlled study), not a suggestion.

You are an expert analyst of competitive Pokémon (Smogon singles). Attached is a ZIP of a research repo. Your corpus is `corpus/empo/`: `manifest.json` (one record per game: tournament, date, format, opponent, result, source, validation warnings) and `games/*.log` (raw Pokémon Showdown battle logs, standard `|`-delimited protocol). Produce an evidence-grounded profile of the player **Empo** from this corpus and NOTHING else.

## Hard rules
1. **Corpus-only — no web browsing or search, period.** If you find yourself wanting to look something up (a tournament date, a player's reputation, a set's popularity), the answer is: don't — say "not determinable from corpus" instead. Prior knowledge of this player from training data gets set aside too; this profile must be derivable from the attached logs alone. Contaminating the profile with outside reputation defeats the study's design.
2. **Compute, don't estimate.** Any number (usage rates, game lengths, switch frequencies, timing distributions) must come from code you ran over the logs. Label every quantitative claim COMPUTED and every interpretive claim JUDGED.
3. **Cite everything.** Every judged claim references specific evidence: replay id + turn number(s). A claim you cannot cite gets cut.
4. **Behavior, not psychology.** Logs show decisions, not thoughts. Describe patterns and choices; never speculate about emotions or motives.
5. **Losses are first-class evidence** — how a player handles bad positions reveals more than wins. Do not build a highlight reel.
6. Respect the manifest's `warnings` field: games flagged SUSPECT get reduced weight, and say so where relevant.

## Deliverable (markdown, these sections)

1. **Corpus description** — what you were given: game count, formats/generations represented, date span, W/L split, coverage caveats you noticed.
2. **Quantitative tendencies (computed)** — at minimum: lead choices and diversity; game-length profile overall and by result; switch rate; hazard usage and timing; status/setup move shares; priority usage; Terastallization timing and context (gen9 games); comeback behavior (results after falling behind on Pokémon count). Add any metric you think is revealing.
3. **Cross-generation invariants** — patterns that hold across the different generations in the corpus. These are the crown jewels; be demanding about what qualifies.
4. **Generation-specific technique** — what he does in specific gens/metas that doesn't generalize.
5. **Style profile on six axes**, each placed on its spectrum with ≥3 cited game-events: risk pricing (variance-seeking ↔ suppressing) · tempo (initiative-forcing ↔ counter-punching) · progress mode (tactical burst ↔ grind/accumulation) · information handling (scout-patient ↔ early-committing) · preparation weight (novel teams/sets ↔ standard executor) · range (specialist ↔ universalist).
6. **Signature games (3–5)** — brief walkthroughs of the games that best exemplify the profile, including at least one loss.
7. **Open observations** — anything notable the structure above didn't ask for. This section is why you were hired; surprise us.

## Exclusions
No coaching advice, no improvement tips, no "lessons for players" — this is a scouting profile, not a lesson. No filler, no hedging boilerplate. If the corpus is too thin to support a section, say so explicitly rather than padding.

## Required final line of your output
End the profile with exactly one attestation line: `Web tools used: none` — or, if any browsing or search occurred for any reason, `Web tools used: YES — <what and why>`. This line is mandatory and its honesty matters more than the profile itself.
