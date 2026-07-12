#!/usr/bin/env python3
"""Empo quant fingerprint — Player Study Program pilot.
Metrics per playbook: leads, length profile, switch rate, hazard economy,
status/setup shares, Tera timing+context, priority, faint trajectory, comeback rate.
Computed per-game over the full corpus, split by gen (invariant filter).
"""
import json, os, re, sys
from collections import Counter, defaultdict

CORPUS = "/home/claude/empo"
SUBJECT = "empo"

PIVOT_MOVES = {"U-turn","Volt Switch","Flip Turn","Teleport","Parting Shot",
               "Chilly Reception","Shed Tail","Baton Pass"}
HAZARD_MOVES = {"Stealth Rock","Spikes","Toxic Spikes","Sticky Web"}
REMOVAL_MOVES = {"Defog","Rapid Spin","Court Change","Mortal Spin","Tidy Up"}
SETUP_MOVES = {"Swords Dance","Nasty Plot","Calm Mind","Dragon Dance","Quiver Dance",
               "Shift Gear","Bulk Up","Iron Defense","Agility","Autotomize","Rock Polish",
               "Shell Smash","Growth","Work Up","Hone Claws","Coil","Belly Drum",
               "Victory Dance","Curse"}
PRIORITY_MOVES = {"Sucker Punch","Ice Shard","Aqua Jet","Extreme Speed","Mach Punch",
                  "Bullet Punch","Shadow Sneak","Quick Attack","Vacuum Wave",
                  "Water Shuriken","Accelerock","First Impression","Grassy Glide",
                  "Jet Punch","Thunderclap","Fake Out"}
RECOVERY_MOVES = {"Recover","Roost","Soft-Boiled","Slack Off","Synthesis","Moonlight",
                  "Morning Sun","Wish","Rest","Strength Sap","Shore Up","Milk Drink"}
# Status classification (heuristic; covers standard OU status clicks gens 6-9)
STATUS_MOVES = (HAZARD_MOVES | REMOVAL_MOVES - {"Rapid Spin","Mortal Spin"} | SETUP_MOVES
    | RECOVERY_MOVES | PIVOT_MOVES - {"U-turn","Volt Switch","Flip Turn"}
    | {"Protect","Substitute","Toxic","Thunder Wave","Will-O-Wisp","Taunt","Encore",
       "Whirlwind","Roar","Haze","Leech Seed","Sleep Powder","Spore","Hypnosis","Glare",
       "Trick","Switcheroo","Heal Bell","Aromatherapy","Light Screen","Reflect",
       "Aurora Veil","Tailwind","Memento","Destiny Bond","Pain Split","Sleep Talk",
       "Refresh","Magic Coat","Imprison","Disable","Yawn","Stun Spore","Block",
       "Mean Look","Perish Song","Trick Room","Gravity","Sunny Day","Rain Dance",
       "Sandstorm","Hail","Snowscape","Detect","Spiky Shield","Baneful Bunker",
       "Thunder Cage" } - {"Thunder Cage"})

def parse_game(gid, meta):
    path = os.path.join(CORPUS, "games", f"{gid}.log")
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    players = {}
    for ln in lines:
        m = re.match(r"\|player\|(p[12])\|([^|]*)\|", ln)
        if m and m.group(2):
            players.setdefault(m.group(1), m.group(2))
    subj_side = None
    for side, name in players.items():
        if name.lower() == SUBJECT:
            subj_side = side
    g = {
        "id": gid, "players": players, "subj_side": subj_side,
        "format": meta.get("format_actual"), "gen": None,
        "tournament": meta.get("tournament"), "edition": meta.get("edition"),
        "stage": meta.get("stage"), "opponent_declared": meta.get("opponent"),
        "date": meta.get("date"), "uploadtime": meta.get("uploadtime"),
        "turns": 0, "winner": None, "result": None, "forfeit_like": False,
        "lead": None, "opp_lead": None, "team": [], "opp_team": [],
        "moves": [], "voluntary_switches": 0, "pivot_switches": 0,
        "replacement_switches": 0, "opp_voluntary_switches": 0,
        "hazard_events": [], "removal_events": [], "opp_hazard_events": [],
        "tera": None, "opp_tera": None,
        "faint_track": [],  # (turn, side)
        "status_clicks": 0, "setup_clicks": 0, "priority_clicks": 0,
        "recovery_clicks": 0, "attack_clicks": 0, "total_clicks": 0,
        "opp_total_clicks": 0, "opp_status_clicks": 0,
    }
    if subj_side is None:
        return g  # wrong-player suspect; keep minimal
    opp_side = "p2" if subj_side == "p1" else "p1"
    g["opponent_actual"] = players.get(opp_side)

    cur_turn = 0
    pending_faint = {"p1": False, "p2": False}
    pending_pivot = {"p1": False, "p2": False}
    started = False
    first_switch_seen = {"p1": False, "p2": False}
    faints = {"p1": 0, "p2": 0}

    for ln in lines:
        if ln == "|start":
            started = True; continue
        if ln.startswith("|turn|"):
            cur_turn = int(ln.split("|")[2]); continue
        if ln.startswith("|poke|"):
            parts = ln.split("|")
            side = parts[2]; species = parts[3].split(",")[0]
            (g["team"] if side == subj_side else g["opp_team"]).append(species)
            continue
        if ln.startswith("|win|"):
            g["winner"] = ln.split("|")[2]
            continue
        if ln.startswith("|faint|"):
            side = ln.split("|")[2][:2]
            faints[side] += 1
            pending_faint[side] = True
            g["faint_track"].append((cur_turn, "subj" if side == subj_side else "opp"))
            continue
        if ln.startswith("|-terastallize|"):
            parts = ln.split("|")
            side = parts[2][:2]; ttype = parts[3]
            nick = parts[2].split(": ",1)[-1]
            diff = faints[opp_side] - faints[subj_side]  # positive = subj ahead
            rec = {"turn": cur_turn, "type": ttype, "nick": nick, "faint_diff_subj": diff}
            if side == subj_side: g["tera"] = rec
            else: g["opp_tera"] = rec
            continue
        if ln.startswith("|switch|") or ln.startswith("|drag|"):
            parts = ln.split("|")
            side = parts[2][:2]
            species = parts[3].split(",")[0]
            if started and not first_switch_seen[side]:
                first_switch_seen[side] = True
                if side == subj_side: g["lead"] = species
                else: g["opp_lead"] = species
            if ln.startswith("|drag|"):
                pending_faint[side] = False; pending_pivot[side] = False
                continue
            if pending_faint[side]:
                pending_faint[side] = False
                if side == subj_side: g["replacement_switches"] += 1
            elif pending_pivot[side]:
                pending_pivot[side] = False
                if side == subj_side: g["pivot_switches"] += 1
            else:
                if not started or cur_turn == 0:  # team preview leads
                    continue
                if side == subj_side: g["voluntary_switches"] += 1
                else: g["opp_voluntary_switches"] += 1
            continue
        if ln.startswith("|move|"):
            parts = ln.split("|")
            side = parts[2][:2]
            move = parts[3]
            if side == subj_side:
                g["total_clicks"] += 1
                g["moves"].append((cur_turn, move))
                if move in PIVOT_MOVES: pending_pivot[side] = True
                if move in HAZARD_MOVES:
                    g["hazard_events"].append((cur_turn, move))
                if move in REMOVAL_MOVES:
                    g["removal_events"].append((cur_turn, move))
                if move in STATUS_MOVES: g["status_clicks"] += 1
                else: g["attack_clicks"] += 1
                if move in SETUP_MOVES: g["setup_clicks"] += 1
                if move in PRIORITY_MOVES: g["priority_clicks"] += 1
                if move in RECOVERY_MOVES: g["recovery_clicks"] += 1
            else:
                g["opp_total_clicks"] += 1
                if move in PIVOT_MOVES: pending_pivot[side] = True
                if move in HAZARD_MOVES:
                    g["opp_hazard_events"].append((cur_turn, move))
                if move in STATUS_MOVES: g["opp_status_clicks"] += 1
            continue

    g["turns"] = cur_turn
    g["faints_subj"] = faints[subj_side]
    g["faints_opp"] = faints[opp_side]
    if g["winner"]:
        won = (g["winner"].lower() == SUBJECT)
        g["result"] = "W" if won else "L"
        loser_faints = faints[opp_side] if won else faints[subj_side]
        if loser_faints < 6:
            g["forfeit_like"] = True
    # faint trajectory: max deficit and comeback
    diff = 0; max_deficit = 0; led_first = None
    for (t, who) in g["faint_track"]:
        diff += 1 if who == "opp" else -1
        if led_first is None: led_first = (who == "opp")
        max_deficit = min(max_deficit, diff)
    g["max_deficit"] = -max_deficit
    g["drew_first_blood"] = led_first
    g["final_diff"] = diff
    return g

def main():
    manifest = json.load(open(os.path.join(CORPUS, "manifest.json")))
    games, suspects = [], []
    for gid, meta in sorted(manifest.items()):
        g = parse_game(gid, meta)
        (suspects if g["subj_side"] is None else games).append(g)

    def gen_of(g): return g["format"]
    by_gen = defaultdict(list)
    for g in games: by_gen[gen_of(g)].append(g)

    out = {"n_games": len(games), "n_suspects_excluded": len(suspects),
           "suspect_ids": [s["id"] for s in suspects],
           "suspect_players": [s["players"] for s in suspects]}

    def agg(gs, label):
        n = len(gs)
        wl = Counter(g["result"] for g in gs)
        turns = sorted(g["turns"] for g in gs)
        med = turns[n//2] if n else 0
        vsw = sum(g["voluntary_switches"] for g in gs)
        psw = sum(g["pivot_switches"] for g in gs)
        tt = sum(g["turns"] for g in gs) or 1
        clicks = sum(g["total_clicks"] for g in gs) or 1
        atk = sum(g["attack_clicks"] for g in gs)
        stat = sum(g["status_clicks"] for g in gs)
        setup = sum(g["setup_clicks"] for g in gs)
        prio = sum(g["priority_clicks"] for g in gs)
        rec = sum(g["recovery_clicks"] for g in gs)
        opp_clicks = sum(g["opp_total_clicks"] for g in gs) or 1
        opp_stat = sum(g["opp_status_clicks"] for g in gs)
        opp_vsw = sum(g["opp_voluntary_switches"] for g in gs)
        leads = Counter(g["lead"] for g in gs)
        set_first = sum(1 for g in gs if g["hazard_events"] and g["opp_hazard_events"]
                        and g["hazard_events"][0][0] <= g["opp_hazard_events"][0][0])
        both_haz = sum(1 for g in gs if g["hazard_events"] and g["opp_hazard_events"])
        haz_games = sum(1 for g in gs if g["hazard_events"])
        first_haz_turns = [g["hazard_events"][0][0] for g in gs if g["hazard_events"]]
        fh_med = sorted(first_haz_turns)[len(first_haz_turns)//2] if first_haz_turns else None
        comebacks = [g for g in gs if g["result"]=="W" and g["max_deficit"]>=2]
        deficits_faced = [g for g in gs if g["max_deficit"]>=2]
        fb = [g for g in gs if g["drew_first_blood"] is not None]
        fb_drawn = sum(1 for g in fb if g["drew_first_blood"])
        fb_won = sum(1 for g in fb if g["drew_first_blood"] and g["result"]=="W")
        return {
            "label": label, "n": n, "W": wl.get("W",0), "L": wl.get("L",0),
            "unknown_result": wl.get(None,0),
            "turns_min_med_max": (turns[0] if n else 0, med, turns[-1] if n else 0),
            "turns_mean": round(sum(turns)/n,1) if n else 0,
            "voluntary_switch_per_turn": round(vsw/tt,3),
            "pivot_per_turn": round(psw/tt,3),
            "opp_voluntary_switch_per_turn": round(opp_vsw/tt,3),
            "status_share": round(stat/clicks,3),
            "attack_share": round(atk/clicks,3),
            "setup_share": round(setup/clicks,3),
            "priority_share_of_clicks": round(prio/clicks,3),
            "recovery_share": round(rec/clicks,3),
            "opp_status_share": round(opp_stat/opp_clicks,3),
            "leads_top": leads.most_common(6),
            "hazard_games_pct": round(haz_games/n,2) if n else 0,
            "set_hazards_first_pct_of_contested": round(set_first/both_haz,2) if both_haz else None,
            "median_first_hazard_turn": fh_med,
            "comeback_wins_from_2down": len(comebacks),
            "times_2down": len(deficits_faced),
            "first_blood_drawn_pct": round(fb_drawn/len(fb),2) if fb else None,
            "first_blood_conversion": round(fb_won/fb_drawn,2) if fb_drawn else None,
            "forfeit_like_endings": sum(1 for g in gs if g["forfeit_like"]),
        }

    SUBJECTS = {"soulwind","abr","bkc","tesung","mcmeghan","ojama","ciele","tricking",
                "ctc","bro fist","punny","vert","storm zone","separation","ox the fox"}
    ELIM_WORDS = ("final","semifinal","quarterfinal","tiebreak","playoff")
    for g in games:
        opp = (g.get("opponent_actual") or "").lower()
        g["vs_subject"] = opp in SUBJECTS
        stage = (g.get("stage") or "").lower()
        g["elimination"] = any(w in stage for w in ELIM_WORDS)
    out["vs_subject_games"] = [
        {"id": g["id"], "opp": g.get("opponent_actual"), "fmt": g["format"],
         "result": g["result"], "turns": g["turns"]} for g in games if g["vs_subject"]]
    out["elimination_games"] = [
        {"id": g["id"], "stage": g["stage"], "tournament": g["tournament"],
         "opp": g.get("opponent_actual"), "fmt": g["format"], "result": g["result"],
         "turns": g["turns"]} for g in games if g["elimination"]]
    out["overall"] = agg(games, "ALL")
    out["by_gen"] = {k: agg(v, k) for k, v in sorted(by_gen.items())}
    out["tera_events"] = [
        {"id": g["id"], **g["tera"]} for g in games if g.get("tera")]
    out["gen9_games"] = [
        {"id": g["id"], "result": g["result"], "turns": g["turns"],
         "opp": g.get("opponent_actual"), "tera": g.get("tera"),
         "opp_tera": g.get("opp_tera")} for g in by_gen.get("[Gen 9] OU", [])]
    # per-game table
    out["games"] = [{
        "id": g["id"], "fmt": g["format"], "date": g["date"],
        "tournament": f'{g["tournament"]} {g["edition"] or ""}'.strip(),
        "stage": g["stage"], "opp": g.get("opponent_actual"),
        "result": g["result"], "turns": g["turns"],
        "lead": g["lead"], "max_deficit": g["max_deficit"],
        "final_diff": g["final_diff"], "forfeit_like": g["forfeit_like"],
        "vs_subject": g.get("vs_subject"), "elimination": g.get("elimination"),
        "vol_sw": g["voluntary_switches"], "status_clicks": g["status_clicks"],
        "total_clicks": g["total_clicks"], "team": g["team"],
    } for g in games]
    json.dump(out, open(os.path.join(CORPUS, "fingerprint.json"), "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("n_games","n_suspects_excluded","suspect_players","overall")}, indent=1))
    print("\nBY GEN:")
    for k, v in out["by_gen"].items():
        print(json.dumps(v, indent=1))

if __name__ == "__main__":
    main()
