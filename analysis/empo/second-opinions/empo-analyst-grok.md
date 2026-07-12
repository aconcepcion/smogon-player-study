# Independent Player Profile: Empo

**Scope:** `corpus/empo/` only (manifest + 54 Showdown logs).  
**Analysis set:** 50 games where `|player|` lists **Empo** (4 SUSPECT logs excluded from behavioral metrics; noted separately).  
**Labeling:** **COMPUTED** = measured from logs/manifest by code; **JUDGED** = interpretive claim with cited turn(s).

---

## Corpus description

| Item | Value |
|------|--------|
| Manifest entries / log files | **54 / 54** (full match) |
| Empo identified as a player | **50** |
| SUSPECT (Empo not among log players) | **4** — reduced weight; **not** used for style metrics |
| Formats (all logs) | gen6ou 6 · gen7ou 18 · gen8ou 25 · gen9ou 5 |
| Formats (confirmed Empo) | gen6ou 6 · gen7ou 15 · gen8ou 25 · gen9ou 4 |
| Tournaments (confirmed) | Smogon Tour 26 · SPL 15 · OST 5 · WCoP 3 · Snake Draft 1 |
| Manifest date field span (confirmed) | 2019-10-15 → 2024-01-15 |
| Upload-time span (confirmed) | 2018-09-10 → 2024-09-14 (UTC from `uploadtime`) |
| Computed W–L (confirmed) | **39–11** (78.0% W) |
| Manifest declared results | W: 6 · `?`: 48 (logs used to resolve) |

**COMPUTED — SUSPECT IDs (Empo absent from `|player|` lines):**  
`gen7ou-2330828926-…`, `gen7ou-2383788762-…`, `smogtours-gen7ou-538821`, `smogtours-gen9ou-860383`. Players are other handles only; any “Empo alt” claim is **not determinable from corpus** beyond the warning text.

**Coverage caveats (from corpus metadata, not outside knowledge):**
1. **Selection bias:** Discovery is tournament-archive heavy; 39–11 is not a career sample. `failures.json` records **76** `replay_missing_rows` and **1** harvest failure — large unobserved set.
2. **Dates unreliable:** Many `notes` state date is archive-thread start, not game day. Prefer `uploadtime` only as upload bound, not event date.
3. **Manifest vs log result:** `smogtours-gen7ou-396168` declared `W`; log ends `|win|aim` with Empo as p2 → **L**. All W/L below are log-derived.
4. **Forfeits:** **20** of 39 wins contain an opponent “forfeited” message — positions often already decided; turn counts still valid.
5. **Gen9 thin:** only **4** confirmed games (all W, 20–26 turns). Gen6 only **6** games. Cross-gen claims require care.

---

## Quantitative tendencies (COMPUTED)

### Lead choices and diversity
- **25 unique leads / 50 games**; top share Clefable **7/50 (14%)** — no single lead dominates.
- Top leads: Clefable 7, Hippowdon 6, Landorus-Therian 4, Tapu Koko 3, Shuckle 3; then long tail (Victini, Tornadus-T, Samurott-Hisui, Rotom-Heat, Dragapult, Ditto, …).
- By format unique leads: gen6 **5/6**, gen7 **12/15**, gen8 **14/25**, gen9 **3/4**.
- **Turn-1 action (first Empo decision on turn 1):** switch **14**; Stealth Rock **6**; U-turn **5**; Sticky Web **3**; Thunder Wave **3**; Knock Off **3**; remainder status/attack one-offs.
- **Voluntary switch on turn 1:** **20/50** games.

### Game-length profile
| Slice | n | mean | median | min–max |
|-------|---|------|--------|---------|
| Overall | 50 | 48.44 | 33.0 | 9–191 |
| Wins | 39 | 46.72 | 33.0 | 9–144 |
| Losses | 11 | 54.55 | 35.0 | 10–191 |
| gen6ou | 6 | 39.33 | 21.0 | 9–140 |
| gen7ou | 15 | 45.40 | 29.0 | 15–126 |
| gen8ou | 25 | 56.44 | 41.0 | 10–191 |
| gen9ou | 4 | 23.50 | 24.0 | 20–26 |

**Buckets:** 1–15: 5 · 16–30: 19 · 31–50: 13 · 51–80: 5 · **81+: 8**.  
**≥80 turns (8):** wins at 101, 120, 126, 135, 140, 144; losses at 115, **191**.

### Switch rate
Definition: voluntary midgame switches ÷ (Empo moves + voluntary switches); forced replacements/drags excluded; lead switch excluded.

- Mean **0.310**, median **0.343** (min 0.00, max 0.439).
- Mean voluntary switches/game **15.74**; mean moves/game **32.88**.
- **Wins** switch rate mean **0.293** vs **losses 0.370** (more switching in losses).
- By gen means: gen6 **0.206**, gen7 **0.333**, gen8 **0.332**, gen9 **0.246**.

### Hazard usage and timing
- Games where Empo sets ≥1 hazard: **41/50 (82%)**.
- First hazard turn: mean **5.22**, median **3**, min **1**, max **22**.
- First hazard by turn ≤3: **23/41**; by turn ≤2: **18** games.
- Hazard move counts: Stealth Rock **94**, Spikes **56**, Sticky Web **4**, Toxic Spikes **4**, Ceaseless Edge **1**.
- Per hazard-game uses mean **3.88** (med 2, max 16) — frequent re-sets after removal.
- Removal games: **15/50** (Defog 13, Rapid Spin 7).
- Hazard rate by gen: gen6 5/6, gen7 12/15, gen8 22/25, gen9 2/4.
- Losses without Empo hazard: 4/11 (`396168`, `473406`, `542402`, `562715`).

### Status / setup / priority / related shares
Of **1644** Empo moves:

| Class | Uses | Share of moves | Games used |
|-------|------|----------------|------------|
| Pure status (TWave/Toxic/WoW/Spore) | 68 | 4.14% | 26/50 |
| Setup (CM/BU/ID/Sub/SD/NP/DD/QD/TG) | 74 | 4.50% | 26/50 |
| Priority attacks | 21 | 1.28% | 15/50 |
| Protect | 23 | 1.40% | 11/50 |
| Pivot (U-turn/Volt Switch) | 123 | **7.48%** | 30/50 |
| Recovery (Soft-Boiled/Recover/Roost/Slack Off/Wish/…) | 175 | **10.64%** | — |

Status detail: Toxic **44**, Thunder Wave **16**, Spore **4**, Will-O-Wisp **4**.  
Setup detail: Calm Mind **15**, Bulk Up **15**, Iron Defense **14**, Substitute **12**, Swords Dance **10**.  
Priority detail: Fake Out **6**, Ice Shard **4**, Quick Attack **4**, Shadow Sneak **3**.  
**Knock Off** is the co-top move with Moonblast (**113** each). Phazing: Whirlwind **23**. Body Press **30**. Seismic Toss **30**.

Early-game: pivot in turns 1–5 in **14/50** games; Knock Off in turns 1–5 in **11/50**; setup by turn ≤8 in **11/50**.

### Terastallization (gen9 only, n=4 confirmed)

| Game | Result | Turns | Empo Tera |
|------|--------|-------|-----------|
| `smogtours-gen9ou-770676` | W | 20 | Iron Valiant → **Steel**, turn **17** |
| `smogtours-gen9ou-772080` | W | 26 | **No tera** |
| `smogtours-gen9ou-773677` | W | 24 | Kingambit → **Ghost**, turn **20** (same turn as opp Tera Water Ogerpon) |
| `smogtours-gen9ou-790679` | W | 24 | Kingambit → **Ghost**, turn **24** (vs Dragonite Extreme Speed) |

**COMPUTED pattern:** when used, Tera is late (≥70% of game length); 2/3 uses are Kingambit Ghost into priority/Extreme Speed contexts; 1/4 wins never Terastallize.

### Comeback behavior (Pokémon-count deficit)
- Games Empo was behind on remaining mons at some faint: **31/50**.
- From those: **W 20 / L 11** → **64.5%** win rate while having been behind.
- Games **never** behind: **19/19 wins** (no loss without a mon-count deficit).
- Max deficit in a comeback win usually **1**; one win from deficit **2** (`smogtours-gen9ou-772080`).
- Losses include deep deficits (max_def **3–4** in `542402`, `772055`, `470762`).

### Species / structure (team preview)
- **86** unique species across confirmed games.
- Highest game appearance: Landorus-Therian **20**, Clefable **19**, Toxapex **15**, Kartana **12**, Hippowdon **11**, Skarmory **11**, Heatran **10**.
- Top co-occurrence pairs (games together): Kartana+Lando **10**; Clefable+Skarmory **10**; Clefable+Toxapex **10**; Hippowdon+Toxapex **10**.
- Mega events: **14** games; Z-move: **10** games; Dynamax: **0**.

### Mega/Z note
Gen6–7 tools appear when the format supplies them (e.g. Mega Charizard Y in `396168` t4; Z Bloom Doom Kartana in `542981` t42). Not a cross-gen constant.

---

## Cross-generation invariants

Only patterns that appear in **multiple gens** with repeated, citable mechanics:

### 1. Residual / attrition progress over pure speed-control offense
**COMPUTED:** Toxic 44, Knock Off 113, hazards in 82% of games, recovery 10.6% of moves — across gen6–9.  
**JUDGED:** Progress is frequently measured in residual chip + item removal + board hazards rather than only clean KO races.  
Evidence: Hippowdon Toxic open vs Spectrier line (`smogtours-gen8ou-533296` t1 Toxic); Clefable Moonblast + residual path without Tera (`smogtours-gen9ou-772080` t1–10); gen7 Chansey/Seismic Toss grind (`smogtours-gen7ou-542981` t13–24 Seismic Toss/Toxic).

### 2. High lead diversity with information-first turn 1
**COMPUTED:** 25 leads/50; 14 turn-1 switches; 20 voluntary t1 switches; only 14% Clefable max share.  
**JUDGED:** Opens are matchup-reactive (switch/pivot/status/rocks), not a fixed signature lead across gens.  
Evidence: Shuckle Web t1 (`smogtours-gen6ou-531323` t1 Sticky Web); Lando → Rotom t1 switch (`smogtours-gen8ou-562715` t1); Samurott Knock Off into Ogerpon switch (`smogtours-gen9ou-790679` t1).

### 3. Hazard discipline when the game lasts
**COMPUTED:** 82% set hazards; median first rocks/spikes **turn 3**; multi-set mean ~3.9 uses/hazard-game.  
**JUDGED:** Empo treats entry hazards as a default long-horizon wincon, re-establishing after spins/defogs.  
Evidence: Hippowdon SR early (`smogtours-gen8ou-470762` t6 SR, re-sets t27/t29); Lando SR midgame after trades (`smogtours-gen9ou-773677` t17 SR).

### 4. Balance cores recur (fat + glue + breaker)
**COMPUTED:** Clefable/Toxapex/Skarmory/Hippowdon/Lando dominate gen7–8 usage; recovery and phazing present.  
**JUDGED:** Default structure is balanced stall-leaning or bulky offense, not glass hyper offense as baseline (offense appears as module, not default).  
Evidence: Skarm ID/spikes/Body Press stack (`smogtours-gen8ou-533296` t2–4, t21–23; `smogtours-gen8ou-548764` t3 ID, t17 Body Press); gen9 Skarm Iron Defense → Body Press sweep (`smogtours-gen9ou-772080` t22–26).

### 5. Mon-count deficits are often playable; all observed losses went through one
**COMPUTED:** 20/31 wins after behind; 0 losses among never-behind games.  
**JUDGED:** Empo’s games frequently route through a temporary mon deficit and still stabilize — losses are those where the deficit widens or the wincon never forms.  
Evidence: deficit-2 then Skarm win (`772080` faints t8/t13 before t22–26 conversion); long gen6 Clef/Amoonguss grind win from behind (`smogtours-gen6ou-627181`, first deficit t19, win t140).

### 6. Pivot as repositioning, not only as damage
**COMPUTED:** U-turn 92 + Volt Switch 31 = 7.5% of moves; 30/50 games.  
**JUDGED:** Turns often spend a click to change the active rather than force damage.  
Evidence: Tapu Koko U-turn → Skarm on Scizor SD (`548764` t1); repeated U-turn sequencing in gen7 loss (`396168` t1, t3).

**What does *not* qualify as invariant:** Tera patterns (gen9-only, n=4); Sticky Web (gen6/rare gen8); Dynamax (absent); a single lead Pokémon.

---

## Generation-specific technique

### Gen 6 (n=6)
- **Sticky Web offense module:** Shuckle lead → Web → setup breaker.  
  - `smogtours-gen6ou-531323`: t1 Sticky Web (after Magma Storm → drag), t2 Manaphy, t3–9 Thundurus Nasty Plot into Thunderbolt/Focus Blast/HP sequence, win t9.  
  - `smogtours-gen6ou-532032`: Shuckle lead Web path, Tail Glow Manaphy t7–8, win t10.
- Azelf lead offense burst (`500244`, win t13, switch rate 0.00 — pure sequence).
- Long fat game exists (`627181`, 140 turns) — same residual identity as later gens.

### Gen 7 (n=15)
- **Megas & Z** as scheduled power spikes: Mega Charizard Y Solar Beam (`396168` t4); Z Bloom Doom Kartana (`542981` t42).
- **Ditto as information/steal tool:** Ditto lead `542981` — transforms into Alakazam line, later Ditto again t48/t63 to steal Psyshock KO.
- **Lopunny / Medicham mega offense leads** mixed with fat (Lopunny leads wins `629026`, `540413`).
- High Kartana + Magearna + Lando co-usage (gen7-specific breaker package).

### Gen 8 (n=25; densest slice)
- **Hippowdon / Clefable lead balance** (5 each) with Toxapex–Skarm–Reuniclus.
- **Iron Defense + Body Press** on Skarmory as a primary late wincon (`533296` t3/t21–23; `548764` t3/t15–17).
- **Haze on Toxapex** to erase setup (`533296` t13, t30–31) — gen8-specific counterpunch tool in-corpus.
- Extreme length battles both ways: win 144 (`551299`), loss 191 (`470762`) — passive Corvi/Pex/Hippo mirror wars.
- Short collapse when DD Dragapult gets free turns (`473406` t1 TWave into t2 Corvi while DD completes; loss t10).

### Gen 9 (n=4; all W, short)
- **Samurott-Hisui lead** (2/4) with Razor Shell / Ceaseless Edge hazard offense (`790679` t4–16; `773677` lead).
- **Kingambit Tera Ghost** twice as priority answer (`773677` t20; `790679` t24).
- **Cinderace lead aggression** into mirror/Gunk Shot (`770676` t1–4) — more early damage commitment than gen8 medians.
- One full win **without Tera** via Skarm Body Press (`772080` t22–26).
- Mean length **23.5** — compressed vs gen8 mean 56.4 (sample-size caveat).

---

## Style profile (six axes)

Each axis: spectrum position, then ≥3 cited game-events.

### 1. Risk pricing — **variance-suppressing, with scheduled spikes**
Spectrum: variance-seeking ↔ **suppressing** (leans suppress; spikes when format tools appear).

- Prefers Toxic/Knock/Rocks/recovery over accuracy-stacked offense as default (**COMPUTED** residual-heavy move table).
- Still fires high-variance clicks when the structure needs them: Focus Blast Thundurus (`531323` t6); Hydro Pump Rotom sequences in gen6 loss (`533278` t18–22); Gunk Shot Cinderace (`770676` t3–4, including miss protocol on t3 in raw log).
- Protect used sparingly (23 uses / 11 games) — not a stall-timer specialist; suppression is residual, not endless Protect.

**JUDGED:** Prices risk down via fat + residual; accepts variance on breaker turns, not as the base plan.

### 2. Tempo — **counter-punching with selective initiative**
Spectrum: initiative-forcing ↔ **counter-punching** (center-right toward counter).

- Turn-1 switches/pivots (14 switches; 5 U-turns) wait on information (`562715` t1 Lando→Rotom; `548764` t1 Koko U-turn→Skarm).
- Initiative when Web/DD/Tera windows open (`531323` Web→NP; `773677` Kyurem DD t7→Earth Power t8; `790679` Tera Ghost t24).
- Loss when initiative is *given*: Rotom TWave into Dragapult free DD (`473406` t1–4).

**JUDGED:** Default is answer-the-active; forces tempo when a prepared window (Web, setup, Tera) is live.

### 3. Progress mode — **grind / accumulation, with tactical bursts**
Spectrum: tactical burst ↔ **grind/accumulation**.

- Soft-Boiled/Moonblast wars (`627181` multi-dozen Clef turns; `542981` Seismic Toss/Toxic loop).
- Spikes + ID + Body Press accumulation (`533296` t4 Spikes → t21–23 Body Press KOs).
- Bursts exist: 9-turn Web game (`531323`); 20-turn gen9 Valiant close (`770676` t17–20).

**JUDGED:** Primary progress is layered residual and boosts; burst games are the short tail, not the center (median 33 turns, 8 games ≥80).

### 4. Information handling — **scout-patient, early-committing only on known plans**
Spectrum: **scout-patient** ↔ early-committing.

- Ditto lead steals sets (`542981` lead Ditto; midgame Ditto t48).
- Heavy t1 switch rate; Double-switch turns common (**COMPUTED** ~4.3 double-switch turns/game).
- Early commit when the plan is structural: Sticky Web t1 (`531323`); Samurott click-on-lead (`790679` t1 Knock).
- Scout failure cost: gen7 `396168` U-turn choreography into Zygarde DD×2 (`396168` t5–6) without a clean check path.

**JUDGED:** Holds commitment until roles are forced; pre-commits mainly for Web/hazard/offense scripts.

### 5. Preparation weight — **standard executor with modular specialty techs**
Spectrum: novel teams/sets ↔ **standard executor** (with modules).

- Species are recurrent OU glue/breakers (Lando, Clef, Pex, Skarm, Hippo, Heatran, Kartana) — **COMPUTED** usage table.
- Specialty modules appear repeatedly but narrowly: Shuckle Web; Ditto; Skarm ID/Body Press; gen9 Tera Ghost Gambit; Darkrai in two gen9 teams (`772080`, `790679`).
- Not determinable from corpus whether sets are “ladder standard” vs “novel” beyond log moves — **no external tier data used**.

**JUDGED:** Builds read as established OU structures plus a small set of repeating tech modules, not constant rebuild novelty.

### 6. Range — **universalist within OU singles (gen6–9)**
Spectrum: specialist ↔ **universalist**.

- Confirmed play in **four generations** of OU, five tournament types (Tour, SPL, OST, WCoP, Snake Draft).
- 86 species brought; lead diversity high.
- Not shown outside OU / not doubles — **not determinable from corpus**.

**JUDGED:** Within Smogon OU singles, range is wide across gens and team archetypes (Web offense, fat balance, bulky offense, gen9 structured offense).

---

## Signature games

### 1. `smogtours-gen6ou-531323` vs FREE XIMRAPTOR — **W, 9 turns** (Web burst)
Shuckle lead sets Sticky Web t1 (after Volcanion Magma Storm → Rotom drag). Manaphy intermediate t2, Thundurus-T Nasty Plot t4, then Thunderbolt/Focus Blast/HP clears Tornadus and Mega Metagross for the win t8–9.  
**Profile fit:** specialty module + compressed tactical burst; shows Empo is not only a long grinder.

### 2. `smogtours-gen8ou-533296` vs SOULWIND — **W, 33 turns** (balance counterpunch)
Hippowdon lead Toxic t1; Skarm Iron Defense t3 + Spikes t4; Clefable dies to Spectrier t9; Pheromosa deletes Spectrier t10; Toxapex Haze vs Magearna Stored Power t13; later Skarm ID t21 + Body Press KOs Magearna t22–23; Pheromosa Ice Beam finishes Garchomp t33 after double Haze t30–31.  
**Profile fit:** residual open, setup denial, ID/Body Press wincon, temporary mon deficit (Clefable) recovered.

### 3. `smogtours-gen9ou-772080` vs Santu — **W, 26 turns** (comeback, no Tera)
Clefable lead Moonblasts; loses Gliscor t8 and Slowking-Galar t13 (max deficit 2). Darkrai chip/WoW t15–19; Weavile SD fails vs Kingambit t20–21. **Skarmory Iron Defense t22 → Body Press** KOs Roaring Moon, Lando, Kyurem, Kingambit t23–26. Never Terastallizes.  
**Profile fit:** deficit tolerance; accumulation wincon on Skarm; Tera optional.

### 4. `smogtours-gen9ou-790679` vs 3d — **W, 24 turns** (late Tera Ghost)
Samurott-Hisui lead pressure (Knock/Razor Shell/Ceaseless Edge); Zapdos Roost/Hurricane/TWave vs Dragonite DD stack t10–21; Samurott dies to Extreme Speed t23. **Kingambit Tera Ghost t24** into Kowtow Cleave vs Tera Normal Dragonite Extreme Speed — KO and win.  
**Profile fit:** gen9-specific priority answer; Tera as endgame tool, not turn-1.

### 5. `smogtours-gen8ou-473406` vs blarghlfarghl — **L, 10 turns** (loss — tempo gift)
Rotom-Heat lead Thunder Wave t1 while Dragapult Dragon Dances; Corviknight comes in t2 into Phantom Force; U-turn to Mamoswine t4 into further DD; game collapses by t10. No Empo hazard set. Switch rate 0.38.  
**Profile fit:** shows the failure mode of the counter-punch style — status into a setup attacker that didn’t need to switch. First-class loss evidence, not a highlight.

**Honorable long grind (not expanded):** `smogtours-gen8ou-470762` **L, 191 turns** — Hippo/Pex/Corvi residual war ends with Excadrill/Corvi failing to break Rotom-Heat after mon deficit reaches 4. Demonstrates that grind length alone does not save a stalled wincon.

---

## Open observations

1. **Corpus is a victory archive with a long right tail.** Median game is moderate (33), but Empo’s distinctive fingerprint in this sample is willingness to *stay* in 100+ turn residual games and still convert (~6 such wins). Losses in that regime (`470762` 191, `772055` 115) show the same commitment without conversion — length is style, not skill guarantee.

2. **Switch rate rises in losses (0.37 vs 0.29).** Compatible with fishing for positioning when the wincon is unclear; also compatible with being forced to dance under pressure. The logs show both: reactive Corvi/Pex hopping in `470762`, and forced pivots under Blaziken Close Combat in `562715` t21–28.

3. **“Fat glue” naming Easter eggs in nicknames** (e.g. Hippowdon “dons meetup”, Skarm “Willkommen”, Clefable “THE NIGHTMARE” / “Houston”) recur across SPL/Tour logs — cosmetic, but team continuity across events is visible in species choice, not just nicks.

4. **Gen9 sample is all wins and all short** — dangerous to extrapolate. What *is* solid: Samurott-Hisui lead + Kingambit Ghost Tera appeared in multiple games; one win refused Tera entirely in favor of classic Skarm Body Press. Continuity with gen8 Skarm plans is stronger than “new gen reinvent.”

5. **Priority is not a pillar** (1.28% of moves). Closing power is more often Body Press, boosted specials, Kartana, or Tera-enabled Kowtow than classic priority chains — Ice Shard/Fake Out appear as supplements.

6. **SUSPECT contamination risk is real.** Four logs would pollute species/lead stats if included (different players entirely). Manifest notes sometimes assert alts (“Empo Aurella”, “world title”) but player tags do not say Empo — methodology correctly down-weights them to zero for this profile.

7. **Manifest result field is unusable without logs** (48/54 `?`, one false W). Any future study should treat log `|win|` as ground truth, as done here.

8. **World Cup slice is tiny and bad in-sample (1–2)** while Smogon Tour is 23–3 — almost certainly discovery bias (Tour playoff replay packs), not a true circuit split. Not determinable beyond sample composition.

---

Web tools used: none
