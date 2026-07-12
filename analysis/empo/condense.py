#!/usr/bin/env python3
"""Condense a Showdown log into compact per-turn strategic notation for deep reads."""
import json, os, re, sys

CORPUS = "/home/claude/empo"

def pct(hp):
    if not hp: return "?"
    hp = hp.split(" ")[0]
    if "/" in hp:
        try:
            a,b = hp.split("/"); return f"{round(100*int(a)/int(b))}%"
        except Exception: return hp
    return hp

def condense(gid):
    lines = open(f"{CORPUS}/games/{gid}.log", encoding="utf-8", errors="replace").read().splitlines()
    out = []
    players = {}
    manifest = json.load(open(f"{CORPUS}/manifest.json"))
    meta = manifest[gid]
    teams = {"p1": [], "p2": []}
    buf = []
    def flush():
        if buf: out.append(" | ".join(buf)); buf.clear()
    for ln in lines:
        p = ln.split("|")
        if len(p) < 2: continue
        tag = p[1]
        if tag == "player" and len(p) > 3 and p[3]:
            players.setdefault(p[2], p[3])
        elif tag == "poke":
            teams[p[2]].append(p[3].split(",")[0])
        elif tag == "turn":
            flush(); out.append(f"— T{p[2]} —")
        elif tag == "start":
            side = lambda s: f"{players.get(s,s)}"
            out.append(f"PLAYERS: p1={players.get('p1')} p2={players.get('p2')}  TIER: {meta.get('format_actual')}")
            out.append(f"p1 team: {', '.join(teams['p1'])}")
            out.append(f"p2 team: {', '.join(teams['p2'])}")
            out.append(f"CTX: {meta.get('tournament')} {meta.get('edition','')} {meta.get('stage','')} vs {meta.get('opponent')} ({meta.get('date')})")
            out.append("=== BATTLE ===")
        elif tag in ("switch","drag"):
            v = "drag" if tag=="drag" else "sw"
            buf.append(f"{p[2]} {v}→ {p[3].split(',')[0]} {pct(p[4]) if len(p)>4 else ''}")
        elif tag == "move":
            buf.append(f"{p[2]}: {p[3]}")
        elif tag == "-damage":
            buf.append(f"{p[2].split(': ')[-1]}→{pct(p[3])}")
        elif tag == "-heal":
            buf.append(f"{p[2].split(': ')[-1]} heal→{pct(p[3])}")
        elif tag == "-status":
            buf.append(f"{p[2].split(': ')[-1]} {p[3].upper()}")
        elif tag == "-boost":
            buf.append(f"{p[2].split(': ')[-1]} +{p[4]} {p[3]}")
        elif tag == "-unboost":
            buf.append(f"{p[2].split(': ')[-1]} -{p[4]} {p[3]}")
        elif tag == "faint":
            buf.append(f"** FAINT {p[2]} **")
        elif tag == "-sidestart":
            buf.append(f"HAZ+ {p[2].split(': ')[-1]}: {p[3].replace('move: ','')}")
        elif tag == "-sideend":
            buf.append(f"HAZ- {p[2].split(': ')[-1]}: {p[3].replace('move: ','')}")
        elif tag == "-terastallize":
            buf.append(f"*** TERA {p[2]} → {p[3]} ***")
        elif tag == "-mega":
            buf.append(f"MEGA {p[2]}")
        elif tag == "-enditem":
            if len(p)>3 and ("Knock Off" in ln or "eaten" not in ln):
                buf.append(f"{p[2].split(': ')[-1]} loses {p[3]}")
        elif tag == "-item":
            buf.append(f"{p[2].split(': ')[-1]} item revealed: {p[3]}")
        elif tag == "-weather" and len(p)>2 and "upkeep" not in ln:
            buf.append(f"WX {p[2]}")
        elif tag == "-crit":
            buf.append(f"CRIT on {p[2].split(': ')[-1]}")
        elif tag == "-miss":
            buf.append("MISS")
        elif tag == "cant":
            buf.append(f"{p[2].split(': ')[-1]} can't ({p[3]})")
        elif tag == "win":
            flush(); out.append(f"=== WIN: {p[2]} ===")
    flush()
    return "\n".join(out)

if __name__ == "__main__":
    ids = sys.argv[1:]
    os.makedirs(f"{CORPUS}/condensed", exist_ok=True)
    for gid in ids:
        txt = condense(gid)
        open(f"{CORPUS}/condensed/{gid}.txt","w").write(txt)
        print(gid, len(txt.splitlines()), "lines,", len(txt), "chars")
