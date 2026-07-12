# EMPO — Player Dossier (FINAL, Player Study Program Pilot)

**v2 FINAL · 2026-07-12 · Corpus: 50 log-verified games (Gens 6–9) · Adjudicated against two independent second opinions (§10) · Supersedes draft v1**

---

## 1 · Career map & trophies

Hall of Fame #1 (2026-04 revision). Trophy line per discovery: Smogon Tour XXX, XXXIII, XXXVI · OST XVII · Masters II · SPL X, XI · WCoP XV, XX. Career span BW→SV — the widest invariant filter among the 16 subjects, which is why he pilots the program. The archived corpus concentrates on Smogon Tour playoff runs (26 games), SPL (15), OST (5), WCoP (3), Snake (1); 27 of 50 games are elimination-stage, including three complete finals series. **Chronology caveat (adjudicated):** manifest `date` fields are archive-thread dates, wrong in 53/54 records; the defensible span is upload-derived, 2018-09 → 2024-09 UTC. No within-corpus development arc is claimed.

## 2 · Quant fingerprint — Empo vs his own opposition (paired baseline, same 50 games)

All results log-verified from `|win|` lines (manifest carried 48/54 as "?", including one false W — 396168 is a loss). Baseline = identical metrics for the opponents' side of the same logs. Caveat: this population loses 78% of these games; the opp-wins split (n=11) is used where it changes the reading. Definitions in §9.

| Metric | Empo | Opp baseline | Reading |
|---|---|---|---|
| Record | 39–11 (.780) | — | Corpus stat (playoff-skewed; Tour 23–3 vs WCoP 1–2 is discovery bias, not a circuit split) |
| Voluntary switches/turn | 0.275 | 0.277 | **Tempo-neutral** at field pace — but rises in his losses (26.8 → 29.5/100T; both externals corroborate under their own definitions) |
| Stat-raising setup share | **3.77%** | 7.37% | **Half the field rate. Confirmed** — and asymmetric by result: 2.55% in wins vs **7.71% in losses**, concentrated in *defensive* setup (§6) |
| Status-infliction share | 4.14% (Toxic 44 · TWave 16 · Spore 4 · WoW 4) | — | Narrow definition, externally computed and verified; my broader non-attack share (35.0% vs opp 40.5%) says he is *more direct* than his opposition |
| Recovery share | 10.6% | 13.2% | He recovers *less*; he is the one *forcing* recovery clicks (opp recovery 13.7% in their losses) |
| Priority share | 1.3% | 1.6% | **Retracted as an Empo trait** — field property (one external declines the metric entirely as underivable without an external move DB; the computed value is definition-dependent either way) |
| Hazard economy | 82% of games · median first hazard **T3** · **159 selections**, 3.88/hazard-game (SR 94, Spikes 56, Web 4, TSpikes 4, Ceaseless 1) | 76% / T5 | Two turns earlier than the field, and the deeper signature is the **re-buy**: hazards recur through T66/T93/T123 in the long games. *Scoped Gens 6–8* (§4) |
| First blood drawn / converted | 54% / 81% | 46% / 26% | Lagging measure of structural dominance (§5 adjudication) |
| **Deficit gradient** | never behind: **19/19 W** · max −1: **19W–4L (82.6%)** · max −2: 1W–4L · −3/−4: 0W–3L | opp reaches −2 in 82% of games | **The central finding, now graded:** −1 is his routine operating zone and highly recoverable; −2 is the cliff; every one of his 11 losses passed through a deficit. Comeback rate from −2 (12.5%) still ≥ opponents' (7.3%) |
| Game length | med 33 · mean 48.4 · 8 games ≥81T · max 191 | (shared) | Long-game tolerance extreme; 6 of the 8 marathons are wins |
| Leads | **25 distinct in 50 games** (top: Clefable 14%) · normalized entropy 0.93, >0.91 in every gen | Toxapex ×8 leads vs him | No signature lead exists — see I2 |

## 3 · Invariants (cross-gen: ≥3 of 4 generations)

**I1 — Hazards open the game (Gens 6–8), and persistence is the signature, not speed.** Rocks/Spikes by median T3; 23 of 41 hazard games by T3. The distinctive habit (externally sharpened, verified): **re-buying** — 159 total selections, recurring through T66 (627181), T93 (627209), T123 (551299 — twelve SR clicks against a nine-Defog Corviknight), because every Defog is a purchased free turn and the remover becomes the target (I4). *Scope note (adjudicated):* as a click metric this is a Gens 6–8 invariant — Gen 9 shows two selections in four games; see §4 for the mechanics-outsourcing argument and the open question.

**I2 — The opening role is fixed; the opening piece is not.** 25 leads in 50 games, normalized entropy above 0.91 in every generation (externally computed, verified). What repeats is the *function*: immediate field control (Shuckle Web T1, 531323), pivot-scout into the revealed plan (Tapu Koko U-turn T1 out on Scizor's Swords Dance, 548764), instant status (Hydreigon TWave T1, 470762), item strike (Samurott Knock T1, 790679). The first five turns are scripted infrastructure per team, never a fixed species script.

**I3 — The resource war is the primary theater.** His two most-clicked moves are tied: **Knock Off 113 = Moonblast 113** (externally computed, verified) — item removal is co-equal with his best attack. Boots hunted on the removal mon's own removal turn (Mandibuzz, 551243 T44); Weavile's dying click Knocks Kingambit's Leftovers (772080 T21); double Trick in one game (551299 T56/T72); Magma Storm traps and deletes the Defogger (551299 T119–120); Whirlwind (23 clicks corpus-wide) converts Spikes into kills (627209 T90).

**I4 — Deficits are purchases; −1 is the operating zone, −2 is the cliff.** The gradient (§2) grades the draft-1 finding: he *routinely* trades into one-down positions and recovers them at 82.6%, because the trades are paid — SKG buys TWave, Darkrai buys WoW, Weavile buys the item-strike, Iron-Defense Skarmory cashes all three 1v4 (772080 T22–26); Swampert at 41% is spent into Landorus so the 123-turn-preserved Moxie Krookodile enters untouched for the 3-0 cleanup (627209 T123); Clefable is sacked for a free Pheromosa entry (533296 T9–10). Every loss in the corpus passed through a deficit; no never-behind game was lost.

**I5 — Concession tracks structure, not mon count.** Conceded finals games down only −1 with five alive (533278 T35) and −2 with four alive (551237 T53, +5 Gravity Lando unanswerable); played 542402 to the last click because a miss-branch lived; endured 191 turns before a mathematical lock (470762). 20 of his 39 wins carry the opponent's explicit forfeit message — the norm runs both directions at this level.

**I6 — Front-running is structural; faints lag.** First blood at T50 of a 6-0-material win (551243); at T33 of a 144-turn 4-0 (551299). Opponents who drew first blood on him still lost 74% of the time.

## 4 · Gen technique (SV-relevant highlighted)

**Gen 8 — the fully-expressed toolkit** (n=25): Regenerator wars, Corviknight duels, Magma Storm trapping, Knock economy at maximum depth; longest games (mean 56.4), highest hazard share (10.8% of moves). The **Iron Defense + Body Press Skarmory module** emerges here as a recurring late wincon (533296 T3/T21–23; 548764 T3/T15–17).

**Gen 9 (SV) — OPEN QUESTION, n=4, all wins; never a finding.** Short (23.5 mean turns), two hazard clicks total. Three continuity arguments now stand (one mine, two externally corroborated): (a) the sack-chain grind grammar persists at 26-turn scale (772080); (b) SV outsources hazards to mechanics — Ceaseless Edge Spikes by attacking (790679 T16), Toxic Debris on death (773677 T24) — so click-counts under-measure hazard presence; (c) the **Gen 8 Skarmory ID/Body Press module reappears verbatim** as the no-Tera comeback wincon (772080 T22–26), and repeated tech modules (Samurott-H lead ×2, Darkrai ×2, Kingambit Tera-Ghost tech — 773677 T20) suggest module continuity, not reinvention. **Tera policy (adjudicated trichotomy):** late (T17/20/24; ≥70% of game length), terminal-board conversion in three roles — *finisher* (Iron Valiant Steel T17 → three closing KOs, 770676), *bridge/survivor* (Kingambit Ghost at 1% leaves Landorus + rocks to close, 773677), and a third role whose event, game, and mechanism are **redacted — sealed position P1** (see `empo-sealed-answers.md`) — and once fully banked through a win against an opponent's T9 Tera (772080). → **Post-pilot action (proposed, non-blocking):** targeted gen9 discovery top-up, 2024–2026 officials.

## 5 · Axis profile & cluster label

First-blood causality (Checkpoint-1 directive, upheld through adjudication): 8 of 12 deep reads tag position-first, 4 aggression-created — and every aggression case is *information-licensed*, not variance-seeking. **Adjudicated answer: the 81% conversion measures structural dominance surfacing late.** The number this dossier stands behind is the deficit gradient, not the conversion rate. Both external profiles, computed independently, landed on materially the same axis placements — logged as convergent evidence in §10.

| Axis | Position | Evidence (≥3 events) |
|---|---|---|
| 1 · Risk pricing | **Variance-suppressing (8/10)**, buys variance only at verified prices | Four Toxic misses + a flinch in the OST decider, zero deviation (551299 T25/60/83/96/94); HJK ×4 only after preview proves no Ghost exists (533288 T3–7); DD at 15% HP on computed EV (773677 T7); external counterpoint accepted: scheduled high-variance clicks exist when structure demands (Focus Blast, Gunk Shot with T3 miss re-clicked T4, 770676) — spikes are *scheduled*, never the base plan |
| 2 · Tempo | **Counter-punch default, mode-plastic (6/10)** | Switch rate exactly field-average; cleaner held 123 of 126 turns (627209); 18-turn blitz when preview licenses it (533288); staged four-piece answer to a +4 Dragonite — Zapdos TWave, Volt Switch, Landorus pivot, timed sack (790679 T18–23; endgame redacted — P1) |
| 3 · Progress mode | **Grind, extreme (9/10) — with a defensive-setup expression under pressure** | Setup 3.77% vs 7.37% baseline; kills by hazard-drag, trap, and toxic-math (§3); *amended:* in losses setup **triples** (7.71%), but it is BU ×15 / ID ×5 — more grind, not a mode change (§6) |
| 4 · Information | **Scout-patient with cheap probes (7/10)** | CM probe abandoned on the Haze reveal (551237 T3–7); Trick reveals-and-cripples (551299 T56); Ditto as a literal set-stealing instrument (542981, lead + T48); Tera withheld to T17–24 or banked |
| 5 · Preparation | **Structure-varied executor with repeating tech modules; builder weight UNDECIDABLE-ON-CORPUS** *(amended from draft's "builder-lean" after adjudication)* | 43 distinct compositions in 50 games and a full counter-team swap for the OST decider (551299) prove *variation*; but both externals correctly object that logs cannot show authorship or novelty vs the era's standards — Scarf Clefable (533278) and Web Shuckle read as tech modules, provenance unknowable here |
| 6 · Range | **Universalist within OU singles (9/10)** | Winning record in all four gens; 86 species fielded; Web offense, fat balance, Medicham HO, SV structured offense in one corpus; unscored beyond OU (no other tier present) |

**Cluster label: PYTHON, with Universal shading.** The constrictor — every exchange slightly favorable, escalation denied (Whirlwind/Haze delete opposing boosts: Latias ×5, 627209; Magearna/Garchomp, 533296; Hydreigon ×3, 551299), resources strangled, the win arriving as arithmetic. Big-Game credentials decorate (9 finals games, three titles in-window); the axes are the profile.

## 6 · Signature games (annotated)

**G1 · 551299 — OST XVII Finals decider, vs Lord_Enz (W, 144T, 4-0).** The masterpiece: counter-team into the returning G1 squad; twelve SR clicks vs nine Defogs; double Trick; the Defogger trapped and deleted T119–120; the T97 Toxic (after three misses) is exactly what fells Hydreigon at T144. Zero faints conceded in a title decider.

**G2 · 772080 — ST XXXVI QF, gen9, vs Santu (W, 26T, from −2).** The purchase ledger (I4), and the Gen 8 Skarmory module cashing it — no Tera spent.

**G3 · 533288 — ST XXX Finals, gen7, vs SOULWIND (W, 18T).** The tempo proof: four consecutive High Jump Kicks, riskless because preview shows no Ghost. Aggression as an information product.

**G4 · The loss modes (amended after adjudication).** Two distinct templates, both verified: **(a) Out-engined** — 772055 (L, 115T): Santu's Future-Sight/Teleport Regenerator engine out-scales him; and 470762 (L, 191T): Scald-burn on Hippowdon, Dugtrio trapping his Toxapex the turn after it kills. *Correction to draft v1:* he does shift gears in these games — **15 Bulk Ups (T21–87) in 470762 and 5 Iron Defenses in 772055** — but the gear is more grind (defensive setup), and the opponent's ten Hazes (T51–88) erase it one-for-one. What is absent is an offensive mode-change; when the engine differential is against him, his losses also grow *more active* (switch rate 29.5 vs 26.8/100T; setup 7.7% vs 2.6%) — continued search through familiar control tools after their marginal value has fallen. **(b) Tempo-gift** — 473406 (L, 10T): T1 Thunder Wave into a Dragon-Dancing Dragapult that never needed to switch; Corviknight fed to Phantom Force T2–4; no hazard ever set. The counter-punch style's failure mode when the opponent's first piece *is* the win condition.

**G5 · 551243 — OST XVII Finals G2, vs Lord_Enz (W, 57T, 6-0 material).** The resource-strike exemplar: first blood withheld to T50; decided at T44 when the Defogger's Boots are Knocked on the Defog turn.

## 7 · What gaijineagle takes

Mapped to the live ledger and the WIN-THE-FIRST-TEN-TURNS mandate.

**T1 — The opening is a deployment checklist, not a decision space (→ mandate; errors-front-load).** Per-team scripts, executed by median T3 — and per I2 the *role* (field control / denial / status / item strike) is the constant while the piece varies. Drill: write the T1–T5 script at preview; grade adherence, not outcome.

**T2 — Aggression is licensed by current information, or it's a leak (→ L09, commitment check v3).** Before every aggressive click Empo has verified the punisher doesn't exist. Add to the check: *"name the mon/move that punishes this click; can't name it from the preview six → the line is free; can → is it dead yet?"*

**T3 — Compute the engine differential before entering a recovery war (→ L03).** He wins pre-computed engine wars (Reuniclus outlasts Toxapex, 627209 T107–113) and loses whole games when out-engined — note that even *he* had no in-game repair for a losing engine matchup, only more grind (§6 G4a). The fix lives at preview and in building, not at T60. Versus a recover core: answer "whose engine is bigger?" first; if theirs, the plan is erosion of the engine itself, never direct trading.

**T4 — Hazard persistence + strike the remover (→ G03).** Re-buy hazards; target the removal mon's item/HP on its removal turn (551243 T44 pattern).

**T5 — Tera: bank by default, spend on named math (→ mandate watch-item).** Empo's three roles — finisher, bridge, shield — share one gate: he can state the exact calc it flips or the exact move it blanks. Two poor defensive spends is the opposite pattern; the gate is the fix.

**T6 — Preserve the cleaner absolutely (→ Team A Kingambit/Weavile).** Krookodile enters at T123 of 126 and goes 3-0. Lateness *is* the usefulness.

**T7 — Concede on structure, never on tilt; activity under pressure must be plan-priced (→ L10, G05).** "Is a branch alive?" is computable — churn is that question asked implicitly. And the adjudicated losses-more-active finding is the warning label: under pressure even Empo's activity rises; the difference between his G05-style repair and flailing is that each extra click still buys a named resource.

## 8 · Sealed prediction positions (solitaire drills)

From corpus games **not annotated above**; answers sealed separately (`empo-sealed-answers.md`) — write your click + reasoning for all four before unsealing.

**P1 — The Tera turn (gen9, SPL XV, smogtours-gen9ou-790679, T24).** Score 5-4 Empo. His fresh Kingambit (88%, Tera available) just came in on the Samurott sack. Opposing Dragonite: **+4 Atk / +4 Spe, paralyzed, 42%, Boots knocked**, Extreme Speed known, its Tera available and expected. Empo's remaining: Lando-T 63%, Darkrai, Cinderace, Zapdos 98%, Kingambit active. What does Empo click — and does he Tera?

**P2 — Pricing the trade (gen8, OST XVII Semis G2, smogtours-gen8ou-548764, T14).** Nat's Scizor: **+2 Atk, paralyzed, 3% HP**, sand up. Empo's active Reuniclus 100%; bench Hippowdon 30%, Skarmory 99%, Tapu Koko, Clefable, Toxapex healthy. Nat's bench: Weavile, Hawlucha, Rillaboom, Garchomp 34%. Your move as Empo.

**P3 — The opening click (gen7, ST XXXVI QF, smogtours-gen7ou-772011, T1).** Preview: Santu shows Serperior/Latios/Jirachi/Gliscor/Heatran/Toxapex. Toxapex leads into Empo's Tornadus-Therian. Empo's six: Scizor/Lando-T/Heatran/Torn-T/Greninja/Toxapex. Turn 1 click?

**P4 — Punishing the pivot (gen8, ST XXXVI R16, smogtours-gen8ou-770690, T63).** Empo's Gastrodon-East (100%) in on Heatran (94%). Their team: Clefable, Lando-T (88%), Melmetal, Dragapult, Rotom-W, Heatran; rocks up on their side only. Turn 63 click?

## 9 · Corpus stats, definitions & sources

54 archived logs → **50 confirmed-Empo** (4 wrong-player suspects zero-weighted by all three analyses independently; preserved in corpus as discovery-QA findings). Formats: G8×25, G7×15, G6×6, G9×4. Results 39–11 from `|win|` lines; manifest results unusable (48/54 "?", one false W at 396168). **Chronology:** manifest dates wrong 53/54; uploadtime span 2018-09-10 → 2024-09-14 UTC is the only defensible bound. **Ending measures (both reported):** explicit opponent-forfeit message in 20/39 Empo wins; loser-under-6-faints in 28/50 games overall. **Discovery bias:** Tour 23–3 vs WCoP 1–2 reflects archive composition, not a circuit split; 76 known-game-no-replay rows and 1 dead endpoint (vs Ox the Fox, gen8) are documented gaps.

**Definitional table (adjudication forced precision):** *stat-raising setup* = boost moves incl. Tail Glow (Empo 62/1644 = 3.77%; one external adds Substitute → 4.50%); *status-infliction* = TWave/Toxic/WoW/Spore/Glare only (4.14%); my broader *non-attack share* (35.0%) additionally counts hazards, recovery, pivots-as-status, screens etc.; *switch rate* reported per-turn (0.275), per-decision (~0.29–0.31), and per-100-turns (32.5 incl. pivots) across the three analyses — all consistent. **Errata from adjudication:** draft v1's parser omitted Tail Glow (setup 3.6%→3.77%; baseline 7.2%→7.37%; finding unchanged) and §6 understated the losses' defensive-setup content (corrected).

Tooling shipped alongside: `fingerprint.py` (+2 logged Powell-pass fixes), `baseline.py`, `condense.py`, both JSONs. The externally-supplied `empo-analyst-chatgpt-game-index.csv` **validated** (0 mismatches vs the independent parser on 6 fields × 50 rows; novel columns exact on a 4-game/10-figure raw-log hand sample) and is admitted to the package as a second independent index. Repo: github.com/aconcepcion/smogon-player-study · corpus/empo/ (immutable) · analysis/empo/.

## 10 · Second-opinion diff log (adjudicated 2026-07-12)

Two briefs, same raw corpus, no web tools (attested last lines verified). Both independently: excluded the 4 suspects, derived W/L from logs, caught the 396168 false-W, and flagged gen9 n=4. Verification coverage: every cited game ID exists (12/12 spot-checked including three games outside my deep-read set); ~20 computed figures re-derived exactly; 5 narrative sequences checked against raw logs.

**CONFIRMED & FOLDED (selection):**
1. *Comeback gradient* (ChatGPT — exact match on re-derivation): never-behind 19/19 W; −1 = 19W–4L; every loss passed a deficit (Grok's framing). → §2, I4.
2. *Setup triples in losses, concentrated in defensive setup* (both; W 2.55% vs L 7.71% exact; BU ×15 in 470762 vs opp Haze ×10; ID ×5 in 772055). → §5 axis 3, §6 G4 correction.
3. *Losses become more active* (both, three independent definitions; mine 26.8→29.5/100T). → §2, §6, T7.
4. *Hazard invariant scoped Gens 6–8; re-buy > speed* (ChatGPT; 159 selections, 3.88/hazard-game, all counts exact). → I1 rescoped.
5. *Lead entropy / opening-role flexibility* (ChatGPT; 25 leads, H=4.310 bits exact, Ditto ×2 verified). → new I2.
6. *Knock Off 113 = Moonblast 113 co-top; Whirlwind 23; Toxic 44* (Grok, exact). → I3.
7. *Tera trichotomy: finisher / bridge / shield* (ChatGPT). → §4.
8. *Skarm ID/Body-Press module continuity into gen9; Samurott-H ×2, Darkrai ×2* (Grok). → §4 continuity argument (c).
9. *Chronology unreliability* (both; 53/54, uploadtime span exact). → §1, §9.
10. *473406 tempo-gift loss mode* (Grok; T1–T4 sequence verified verbatim). → §6 G4b.
11. *20/39 wins carry explicit forfeit message* (Grok, exact). → I5, §9.
12. *43 distinct teams; 86 species; usage counts* (both, exact). → §5 axes 5–6.
13. *Preparation-weight caution* (both, convergent): builder-vs-executor is unknowable from logs. → axis 5 amended from "builder-lean" to "undecidable-on-corpus," the adjudication's one axis change.

**REFUTED-WITH-CITATION:**
1. Grok, game 531323: "Volcanion **Magma Storm** → Rotom drag." Log: `|move|p1a: Volcanion|Steam Eruption|p2a: Shuckle` → drag via Shuckle's Red Card. Move name wrong; mechanism unstated; conclusion (Web-burst game) unaffected.
(ChatGPT: no refuted claims found — every checked figure and sequence reproduced.)

**UNDECIDABLE-ON-CORPUS (correctly self-marked by the analysts, upheld):** suspect-log alt-handle identity · set/team novelty vs era standards · career winrate · cross-tier range · exact game dates · ChatGPT's position that priority-share is underivable without an external move DB (logged as a methodological dissent; the metric was already retracted as an Empo trait on baseline grounds).

**Convergence note:** both externals, working independently from raw logs, placed Empo variance-suppressing / counter-punch-leaning / accumulation-primary / scout-patient / universalist-within-OU — materially identical to the coach profile. Axis placements are now triple-sourced.

---
*Adjudication throughput (pilot log): fetch+attest 1 min · CSV validation 4 min · brief reads 3 min · scripted claim verification 4 min · narrative hand-checks 2 min · fold+finalize 8 min ≈ 22 min. Two review passes completed on this final: (1) correctness — all folded figures re-derived, corrected setup shares propagated to both sides; (2) best-we-can-do — one axis honestly downgraded, both loss modes named, and the draft's one substantive error (§6 "no setup gear") corrected in the open rather than silently. Seal-integrity audit: three body citations that decoded sealed positions P1–P3 were replaced with verified substitute evidence or redacted.*
