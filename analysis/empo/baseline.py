#!/usr/bin/env python3
"""Opponent-population baseline: parse every log symmetrically, compute the identical
metric set for Empo's side and the opponents' side, report deltas.
Also splits opponent metrics by game outcome (opp-won vs opp-lost) to expose
the winner's-profile confound."""
import json, os, re
from collections import Counter, defaultdict
from fingerprint import (PIVOT_MOVES, HAZARD_MOVES, REMOVAL_MOVES, SETUP_MOVES,
                         PRIORITY_MOVES, RECOVERY_MOVES, STATUS_MOVES, SUBJECT, CORPUS)

def parse_sides(gid):
    path = os.path.join(CORPUS, "games", f"{gid}.log")
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    players = {}
    for ln in lines:
        m = re.match(r"\|player\|(p[12])\|([^|]*)\|", ln)
        if m and m.group(2):
            players.setdefault(m.group(1), m.group(2))
    if not any(n.lower() == SUBJECT for n in players.values()):
        return None
    S = {s: {"vol_sw":0,"pivot_sw":0,"clicks":0,"status":0,"setup":0,"prio":0,
             "rec":0,"haz":[], "lead":None} for s in ("p1","p2")}
    cur_turn = 0; started = False
    pend_f = {"p1":False,"p2":False}; pend_p = {"p1":False,"p2":False}
    first_sw = {"p1":False,"p2":False}
    faints = {"p1":0,"p2":0}
    faint_track = []
    winner = None
    for ln in lines:
        if ln == "|start": started = True; continue
        if ln.startswith("|turn|"): cur_turn = int(ln.split("|")[2]); continue
        if ln.startswith("|win|"): winner = ln.split("|")[2]; continue
        if ln.startswith("|faint|"):
            side = ln.split("|")[2][:2]; faints[side]+=1; pend_f[side]=True
            faint_track.append((cur_turn, side)); continue
        if ln.startswith("|switch|") or ln.startswith("|drag|"):
            parts = ln.split("|"); side = parts[2][:2]
            if started and not first_sw[side]:
                first_sw[side]=True; S[side]["lead"]=parts[3].split(",")[0]
            if ln.startswith("|drag|"): pend_f[side]=False; pend_p[side]=False; continue
            if pend_f[side]: pend_f[side]=False
            elif pend_p[side]: pend_p[side]=False; S[side]["pivot_sw"]+=1
            elif started and cur_turn>0: S[side]["vol_sw"]+=1
            continue
        if ln.startswith("|move|"):
            parts = ln.split("|"); side = parts[2][:2]; mv = parts[3]
            d = S[side]; d["clicks"]+=1
            if mv in PIVOT_MOVES: pend_p[side]=True
            if mv in HAZARD_MOVES: d["haz"].append(cur_turn)
            if mv in STATUS_MOVES: d["status"]+=1
            if mv in SETUP_MOVES: d["setup"]+=1
            if mv in PRIORITY_MOVES: d["prio"]+=1
            if mv in RECOVERY_MOVES: d["rec"]+=1
            continue
    subj = "p1" if players.get("p1","").lower()==SUBJECT else "p2"
    opp = "p2" if subj=="p1" else "p1"
    won = winner and winner.lower()==SUBJECT
    # first blood + max deficit per side
    def traj(side):
        other = "p2" if side=="p1" else "p1"
        diff=0; maxdef=0; fb=None
        for t,who in faint_track:
            diff += 1 if who==other else -1
            if fb is None: fb = (who==other)
            maxdef = min(maxdef, diff)
        return fb, -maxdef
    fb_s, md_s = traj(subj); fb_o, md_o = traj(opp)
    return {"turns":cur_turn,"subj":S[subj],"opp":S[opp],"won":won,
            "fb_subj":fb_s,"fb_opp":fb_o,"maxdef_subj":md_s,"maxdef_opp":md_o}

def agg(rows, key):
    tt = sum(r["turns"] for r in rows) or 1
    ck = sum(r[key]["clicks"] for r in rows) or 1
    n = len(rows)
    haz_games = sum(1 for r in rows if r[key]["haz"])
    fh = sorted(r[key]["haz"][0] for r in rows if r[key]["haz"])
    return {
        "vol_sw_per_turn": round(sum(r[key]["vol_sw"] for r in rows)/tt,3),
        "pivot_per_turn": round(sum(r[key]["pivot_sw"] for r in rows)/tt,3),
        "status_share": round(sum(r[key]["status"] for r in rows)/ck,3),
        "setup_share": round(sum(r[key]["setup"] for r in rows)/ck,3),
        "priority_share": round(sum(r[key]["prio"] for r in rows)/ck,3),
        "recovery_share": round(sum(r[key]["rec"] for r in rows)/ck,3),
        "hazard_games_pct": round(haz_games/n,2),
        "median_first_hazard_turn": fh[len(fh)//2] if fh else None,
        "leads_top": Counter(r[key]["lead"] for r in rows).most_common(5),
        "n": n,
    }

def main():
    manifest = json.load(open(os.path.join(CORPUS,"manifest.json")))
    rows = []
    for gid in sorted(manifest):
        r = parse_sides(gid)
        if r: rows.append(r)
    out = {}
    out["empo"] = agg(rows, "subj")
    out["opp_all"] = agg(rows, "opp")
    out["opp_in_their_wins"]  = agg([r for r in rows if not r["won"]], "opp")
    out["opp_in_their_losses"]= agg([r for r in rows if r["won"]], "opp")
    # first blood, both populations
    fb_s = [r for r in rows if r["fb_subj"] is not None]
    s_drawn = [r for r in fb_s if r["fb_subj"]]
    o_drawn = [r for r in fb_s if r["fb_opp"]]
    out["first_blood"] = {
        "empo_drawn_pct": round(len(s_drawn)/len(fb_s),2),
        "empo_conversion": round(sum(1 for r in s_drawn if r["won"])/len(s_drawn),2),
        "opp_drawn_pct": round(len(o_drawn)/len(fb_s),2),
        "opp_conversion": round(sum(1 for r in o_drawn if not r["won"])/len(o_drawn),2),
    }
    # comeback from -2, both populations
    s2 = [r for r in rows if r["maxdef_subj"]>=2]
    o2 = [r for r in rows if r["maxdef_opp"]>=2]
    out["down2"] = {
        "empo_times": len(s2), "empo_wins": sum(1 for r in s2 if r["won"]),
        "opp_times": len(o2), "opp_wins": sum(1 for r in o2 if not r["won"]),
    }
    json.dump(out, open(os.path.join(CORPUS,"baseline.json"),"w"), indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
