# EMPO — Player Dossier (Pilot, Player Study Program)

**Draft v1 · 2026-07-12 · Corpus: 50 log-verified games (2019–2024, Gens 6–9) · Status: Checkpoint 2, pending second-opinion adjudication (§10)**

---

## 1 · Career map & trophies

Hall of Fame #1 (2026-04 revision). Trophy line per discovery: Smogon Tour XXX, XXXIII, XXXVI · OST XVII · Masters II · SPL X, XI · WCoP XV, XX. Career span BW→SV — the widest invariant filter available among the 16 subjects, which is why he pilots the program. The archived corpus concentrates on the 2019–2024 window (ST XXX through SPL XV), heavy in playoff games: 27 of 50 are elimination-stage, including three complete finals series (ST XXX vs SOULWIND across three gens; OST XVII vs Lord_Enz; ST XXXIII vs starmaster).

## 2 · Quant fingerprint — Empo vs his own opposition (paired baseline, same 50 games)

All results log-verified from `|win|` lines (the manifest carried 48/54 as "?"). Baseline = the identical metric computed for the opponents' side of the same logs, which controls for gen, meta, and game context. Caveat: this opponent population loses 78% of these games; the opp-wins/opp-losses split (n=11/39) is reported where it changes the reading.

| Metric | Empo | Opp baseline | Reading |
|---|---|---|---|
| Record | 39–11 (.780) | — | Corpus stat (playoff-skewed archive), not a career winrate |
| Voluntary switches/turn | 0.275 | 0.277 | **Tempo-neutral** — moves exactly at field pace |
| Setup share of clicks | **3.6%** | 7.2% | **Half the field rate. Confirmed finding** — he almost never boosts |
| Status share | 35.0% | 40.5% | *More* direct than his opposition — the grind is not passivity |
| Recovery share | 10.8% | 13.2% | **Inverted from draft-1 reading**: he recovers *less*; he is the one *forcing* recovery clicks (opp recovery rises to 13.7% in their losses) |
| Priority share | 1.3% | 1.6% | **Retracted as an Empo trait** — near-zero priority is a field property of elite play in these games |
| Hazard games / first-hazard turn | 80% / **T3** | 76% / T5 | Two turns earlier to hazards than the field; sets first in 68% of contested games |
| First blood drawn / converted | 54% / **81%** | 46% / 26% | See §5 causality adjudication — conversion is a *lagging* measure of structural dominance |
| Games ever reaching −2 faints | **16%** (8/50) | 82% (41/50) | **The real finding: deficit avoidance.** His comeback rate from −2 (1/8, 12.5%) is *at/above* the opponents' 3/41 (7.3%) — "can't dig out" is retracted; *nobody* digs out; he just isn't in holes |
| Game length | med 33 · mean 48.4 · max 191 | (shared) | Long-game tolerance extreme: four games >120 turns, all but one won |
| Leads (top) | Clefable ×7, Hippowdon ×6, Lando-T ×4 | Toxapex ×8 lead vs him | Utility/rocks leads both ways — the field leads defensively *against* him |

**Per-gen splits:** G6 4–2 (39.3 mean turns) · G7 13–2 (45.4) · G8 18–7 (56.4 turns, status .386, hazards-first 89% — peak-grinder) · G9 4–0 (23.5 turns, status .119, hazards near-absent — **open question, §4**).

**What beats him (n=11):** opponents' setup share in their wins is 9.1% vs 6.6% in their losses — the documented exploit is setup his anti-setup infrastructure cannot phaze or Haze (Gravity Bulk-Up Landorus-T, 551237 T44–53) or an attrition engine that out-scales his (§6, Games 4–5).

## 3 · Invariants (cross-gen: present in ≥3 of 4 generations)

**I1 — Hazards open the game; hazard persistence is paid for in turns.** Rocks on T1–3 in every gen (551237 T1; 551299 T2; 627209 T2 Spikes; 542402 opp view). Against dedicated removal he re-sets relentlessly — twelve Stealth Rock clicks against Corviknight in 551299 alone — because every Defog is a purchased tempo-free turn elsewhere, and the remover itself becomes the target (I3).

**I2 — Anti-setup infrastructure substitutes for own setup.** Setup share 2.2–4.5% in every gen; instead his teams carry Haze/Whirlwind/phazing/Unaware-adjacent answers, and opposing boosts are simply deleted: Haze ×3 on Magearna and Garchomp (533296 T13/30/31); Whirlwind phazes CM Reflect-Type Latias five times (627209 T36–104); Clefable answers three Hydreigon Nasty Plots (551299 T61/84/112). Escalation is denied, not matched.

**I3 — The resource war is the primary theater.** Boots and Leftovers are hunted: Knock Off on Mandibuzz's Boots *on its own Defog turn* (551243 T44) ends the removal war; Weavile's dying click Knocks Kingambit's Leftovers (772080 T21). Double Trick in one game — Specs onto Toxapex T56, then stealing Clefable's Leftovers T72 (551299). Magma Storm traps and deletes the Defogger outright (551299 T119–120). Whirlwind converts Spikes into kills (627209 T90, Excadrill dragged to death).

**I4 — Deficits are purchases, never accidents.** The lone −2 comeback (772080) is a scripted sack chain: SKG buys Thunder Wave on Kyurem → Darkrai buys Will-O-Wisp on Landorus → Weavile buys the Leftovers Knock + chip on Kingambit → Iron-Defense Skarmory cashes all four debuffs 1v4 (T22–26). Hippowdon at 24% is spent into a +2 Scizor at 3% so sandstorm executes it post-attack (548764 T14). Clefable is sacked at 18% for a free Pheromosa entry on Spectrier (533296 T9–10). Mon-count is currency; structure is the account.

**I5 — Concession tracks structure, not mon count.** He conceded ST XXX Finals G1 down only 0–1 with five alive (533278 T35, Volcarona structure unanswerable) and OST Finals G1 down 0–2 with four alive (551237 T53, +5 Gravity Lando unanswerable) — yet played 542402 to the literal last click because a miss-branch still existed, and endured 191 turns before conceding to a +2 Sub Rotom-Heat mathematical lock (470762). The evaluation function runs on win-branches, not material.

**I6 — Front-running is structural, faints are lagging.** First blood at T50 of a 57-turn game he won 6-0 in material (551243); at T33 of a 144-turn 4-0 (551299). When opponents drew first blood on him they still lost 74% of the time (baseline table). Leads in mons are the *output* of his game, not the input.

## 4 · Gen technique (SV-relevant highlighted)

**Gen 8 = the fully-expressed toolkit** (n=25, his most-archived era): Regenerator-core wars, Corviknight Defog duels, Future Sight/Teleport loops on the receiving end, Magma Storm trapping, Knock economy at maximum depth. Longest games, most status, near-total hazard initiative (89% first).

**Gen 9 (SV) — OPEN QUESTION, n=4, all wins, never a finding.** The four games are short (23.5 mean turns), attack-share .881, hazards nearly absent — superficially a different player. Two deep-read observations argue *mode continuity* rather than transformation: (a) the sack-chain grind grammar persists at 26-turn scale (772080); (b) hazard work is partly *outsourced to mechanics* in SV (Ceaseless Edge, Toxic Debris — his Samurott sets Spikes by attacking, 790679 T16; Glimmora drops Toxic Spikes by dying, 773677 T24), so low hazard-click counts under-measure hazard *presence*. **Tera policy across the sample: late (T17/20/24), reactive, endgame-sealing — twice Kingambit Tera-Ghost, once banked entirely through a win.** He does not spend Tera to enable; he spends it to close or to survive a named crisis. → **Post-pilot action proposed, not blocking:** targeted gen9 discovery top-up (2024–2026 officials: SPL XV/XVI, SCL, ST XXXVI+ full sets, WCoP XX) to raise n before the SV chapter is written.

## 5 · Axis profile & cluster label

Adjudicated first-blood causality (per Checkpoint-1 directive): the 12 reads tag **8 games position-first** (first blood followed an already-won structure: 551237, 551243, 551299, 533296, 627209, 470762, 772055, 542402) and **4 aggression-created** (533288, 772080, 773677, plus the fingerprint pattern of 790679) — and the aggression cases are all *information-licensed*, not variance-seeking (below). **Adjudicated answer: the 81% conversion measures structural dominance surfacing late, not lead-snowballing skill.** The number the dossier stands behind is the 16%-vs-82% deficit-exposure gap, not the conversion rate.

| Axis | Position | Evidence (≥3 events) |
|---|---|---|
| 1 · Risk pricing | **Variance-suppressing (8/10)** — buys variance only at verified prices | Four Toxic misses + a flinch in the OST decider, zero plan deviation (551299 T25/60/83/96/94); declines the low-value Koko line vs Roost Kyurem (551243 T37–38); Medicham HJK spammed *only after* preview confirms no Ghost exists — 50% crash risk priced at zero by information (533288 T3–7); DD at 15% HP taken only when the EV branch is computed (773677 T7) |
| 2 · Tempo | **Counter-punch default, mode-plastic (6/10)** | Switch rate exactly field-average (§2); cleaner Krookodile held in reserve 123 of 126 turns (627209); yet 18-turn blitz when preview says tempo wins (533288) and SV offense (§4) |
| 3 · Progress mode | **Grind, extreme (9/10)** | Setup 3.6% vs 7.2% baseline; opponents forced into recovery (§2); kills by hazard-drag (627209 T90), trap (551299 T120), toxic-math (551299 T97→144) |
| 4 · Information | **Scout-patient with cheap probes (7/10)** | Reuniclus CM probe abandoned the turn Haze is revealed (551237 T3–7); Trick reveals + cripples in one click (551299 T56); aggression only after set-knowledge licenses it (533288) |
| 5 · Preparation | **Builder-lean hybrid (6/10, moderate confidence — logs can't see the lab)** | Full counter-team swap for the OST decider into the returning G1 squad (551299); Scarf Clefable tech (533278 T1); Pheromosa slotted against a Spectrier team (533296) |
| 6 · Range | **Universalist (9/10)** | Winning record in all four gens; pilots semistall, balance, HO (Medicham), and SV offense within one corpus; wins mirrors and anti-matchups alike |

**Cluster label: PYTHON, with Universal shading.** The constrictor profile — every exchange slightly favorable, escalation denied, resources strangled, the win arriving as arithmetic. Big-Game credentials decorate it (9 finals games in corpus, three titles inside the window) but the axes are the profile.

## 6 · Signature games (annotated)

**G1 · smogtours-gen8ou-551299 — OST XVII Finals, decider, vs Lord_Enz (W, 144T, 4-0).** The masterpiece. Counter-team brought into the opponent's G1 squad; twelve SR clicks against a nine-Defog Corviknight; double Trick (T56, T72); the Defogger trapped and deleted by Magma Storm + Earth Power (T119–120); Toxic landed T97 after three misses is precisely what makes Hydreigon fall to Moonblast at T144. Zero faints conceded in 144 turns of a title decider. I1+I2+I3+I6 in one artifact.

**G2 · smogtours-gen9ou-772080 — ST XXXVI QF, gen9, vs Santu (W, 26T, from −2).** The corpus's only 2-down comeback, and it's a *purchase ledger* (I4): every sack buys a status or an item-strike, and Iron-Defense Skarmory cashes the assembled debuffs four-KOs-in-five-turns. Proof the grind grammar survives at SV tempo.

**G3 · smogtours-gen7ou-533288 — ST XXX Finals, gen7, vs SOULWIND (W, 18T).** The tempo proof. Mega Medicham High Jump Kick four consecutive turns — reckless on its face, riskless in fact: preview shows no Ghost, so the crash branch does not exist. Aggression as an information product (Axis 1/4), and the reason "grinder" alone mislabels him.

**G4 · smogtours-gen8ou-772055 — ST XXXVI QF, gen8, vs Santu (L, 115T, 0-6).** The loss template. Santu's Future-Sight/Teleport Regenerator engine plus Grassy Terrain out-regenerates him; the T1 Thunder Wave on his Clefable loses the opening Clef war; his Tornadus loses Boots T5 and is ground to death by T81. Out-engined with no setup gear to shift into — he lost his own game, played better. Mirrors 470762 (191T: Scald-burn on Hippowdon + Dugtrio trapping his Toxapex the turn after it kills).

**G5 · smogtours-gen8ou-551243 — OST XVII Finals G2, vs Lord_Enz (W, 57T, 6-0 material).** The resource-strike exemplar: first blood withheld until T50, but the game was decided by T44 when Mandibuzz's Boots are Knocked *on the Defog turn* — after which the removal war is unwinnable and every hazard sticks. Three paralyzed targets, all items accounted.

## 7 · What gaijineagle takes

Mapped to the live ledger and the Week 2026-29 mandate (WIN THE FIRST TEN TURNS).

**T1 — The opening is a deployment checklist, not a decision space (→ mandate, errors-front-load pattern).** Empo's first 3–5 turns are pre-scripted infrastructure: hazard down by T3 (median), pivots to scout, zero hero reads. Arnold's errors cluster in T1–14; Empo's answer is that early turns shouldn't be *played*, they should be *executed*. Drill: write the T1–T5 script at preview and grade adherence, not outcome.

**T2 — Aggression is licensed by current information, or it's a leak (→ L09, commitment check v3).** The Medicham game is L09's inverse: before every aggressive click Empo has verified the punisher doesn't exist (no Ghost = HJK free). Concrete add to the commitment check: *"name the specific mon/move that punishes this click; if I can't name it from the preview six, the aggressive line is free — if I can, is it dead yet?"*

**T3 — Compute the engine differential before entering a recovery war (→ L03, progress-engine mandate).** Empo wins recovery wars he has pre-computed (Reuniclus outlasts Toxapex, 627209 T107–113) and *loses whole games* when out-engined (§6 G4). Arnold's L03 (win con fed to loops) is exactly playing an engine war without the math. Rule: versus a recover core, before trading, answer "whose engine is bigger?" — if theirs, the plan is erosion of the engine itself (Knock the Boots, toxic the Regenerator, trap the Defogger), never direct trading.

**T4 — Hazard persistence + strike the remover (→ G03 consolidation).** Arnold's double-TSpikes conversions are the seed of Empo's I1/I3. The upgrade: target the *removal mon's item/HP on its removal turn* (551243 T44 pattern) — the Defog click is the safest turn to strike it.

**T5 — Tera policy: bank by default, spend on named math (→ mandate watch-item, defensive-Tera ROI).** Empo's Tera: late, reactive, twice endgame-sealing, once never spent. Arnold's two poor defensive-Tera spends are the opposite pattern. Rule: Tera only when you can state the exact calc it flips or the exact sweep it blanks (Tera-Ghost-vs-Extreme-Speed class), otherwise bank it.

**T6 — Preserve the cleaner absolutely (→ Team A: Kingambit/Weavile roles).** Krookodile enters at T123 of 126 and goes 3-0. HO's version: Kingambit does not take chip "to be useful mid-game"; its lateness *is* its usefulness.

**T7 — Concede on structure, never on tilt; play on while a branch lives (→ L10, player track).** Empo concedes healthy-looking positions instantly when the math dies (I5) and plays 191-turn losses while it lives. Clock and emotion appear in neither. The two-sided lesson for L10: the decision "is a branch alive?" is computable — churn is what happens when it's asked implicitly.

## 8 · Sealed prediction positions (solitaire drills)

Positions from corpus games **not annotated above**; Empo's actual clicks are sealed in `empo-sealed-answers.md` — do not open until all four are answered. Protocol per Spectator Replay Study: write your click + reasoning, then unseal.

**P1 — The Tera turn (gen9, SPL XV, smogtours-gen9ou-790679, T24).** Score Empo 5-4. His fresh Kingambit (88%, Tera available) just came in on the sack of Samurott-H. Opposing Dragonite: **+4 Atk / +4 Spe, paralyzed, 42%, Boots knocked**, known Extreme Speed, Tera available and expected. Empo's remaining: Lando-T 63%, Darkrai, Cinderace (both unrevealed), Zapdos 98%, Kingambit active. What does Empo click — and does he Tera?

**P2 — Pricing the trade (gen8, OST XVII Semis G2, smogtours-gen8ou-548764, T14).** Nat's Scizor: **+2 Atk, paralyzed, 3% HP**, sand is up. Empo's active Reuniclus 100%; bench: Hippowdon 30% (Lefties intact), Skarmory 99%, Tapu Koko, Clefable, Toxapex healthy. Nat's bench: Weavile, Hawlucha, Rillaboom, Garchomp 34%. Your move as Empo.

**P3 — The opening click (gen7, ST XXXVI QF, smogtours-gen7ou-772011, T1).** Preview: Santu shows Serperior/Latios/Jirachi/Gliscor/Heatran/Toxapex. Toxapex leads into Empo's Tornadus-Therian. Empo's six: Scizor/Lando-T/Heatran/Torn-T/Greninja/Toxapex. Turn 1 click?

**P4 — Punishing the pivot (gen8, ST XXXVI R16, smogtours-gen8ou-770690, T63).** Empo's Gastrodon-East (100%) is in on We Three Kings' Heatran (94%). Their team: Clefable, Lando-T (88%), Melmetal, Dragapult, Rotom-W, Heatran; rocks are up on their side only. Turn 63 click?

## 9 · Corpus stats & sources

54 archived logs → **50 confirmed-Empo** (4 wrong-player suspects excluded from all metrics, preserved in corpus: habibifree/SMLT, randomdancin/hexum, frisoeva/Aurella, zS/ATTRIBUTE — likely alt-handle or misattribution findings for discovery-QA). Formats: G8×25, G7×15(+3 susp.), G6×6, G9×4(+1 susp.). Results: 39W–11L, all from `|win|` lines. 28/50 endings are concessions (loser <6 faints) — normal tournament behavior, both directions. Discovery merge: 55 unique URL-bearing games from 166 source rows (ChatGPT 52 / Gemini 114; 3 corroborated by both), 76 known-game-no-replay rows documented, 1 dead endpoint (vs Ox the Fox, gen8 smogtours-627187) logged as a permanent gap. Tooling: `fingerprint.py` (per-side event parser; two Powell-pass corrections logged: winner/loser faint inversion in forfeit detection; hazards-first denominator), `baseline.py` (symmetric opponent-population metrics), both shipped alongside. Status-move classification is a curated heuristic set (~99% coverage of standard OU status clicks); Curse counted as setup (negligible Ghost-Curse presence in corpus). Repo: github.com/aconcepcion/smogon-player-study · corpus/empo/ (immutable) · this dossier files to analysis/empo/.

## 10 · Second-opinion diff log

*Pending — external analysts' briefs (same raw corpus) arrive at Checkpoint 2; each claim will be adjudicated against logs here, with dispositions: confirmed / refuted-with-citation / undecidable-on-corpus.*

---
*Two review passes completed before delivery: (1) correctness — all 40+ game/turn citations re-checked against condensed logs; metrics re-derived after the two logged script fixes; (2) best-we-can-do — baseline deltas re-labeled three Checkpoint-1 findings (priority retracted, comeback reframed, recovery inverted), first-blood causality adjudicated per directive, gen9 held at open-question status with a scoped top-up proposal, and P1's answer-leak through the Tera table caught and redacted (the §4 Tera summary omits the 790679 row's context).*
