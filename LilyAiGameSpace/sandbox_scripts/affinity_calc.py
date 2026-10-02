"""Affinity (compatibility) calculator. Runs INSIDE a PandaStack sandbox, never in the bot. Standard library only.

Uploaded files:
    /workspace/params.json    {"op": "total" | "best" | "partners", "main": id, ...}  (ids already resolved by the bot)
    /workspace/affinity.json  {"chars": [...], "aff2": [n*n], "aff3": [n*n*n]}  - either the whole game file or a slice of it
Prints one JSON object: {"ok": true, "text": "..."} or {"ok": false, "error": "..."}.

Formula (GameTora's own explanation of its calculator; the aff3 layout was checked against the real data):
    total = pair(main, L1) + pair(main, L2) + pair(L1, L2)
          + triple(main, L1, S11) + triple(main, L1, S12) + triple(main, L2, S21) + triple(main, L2, S22)
    + `bonus`, a number the caller supplies for G1-race wins (the community sources disagree on that rule, so it is NOT guessed).
Tiers (community sources, three agree): triangle 50 or less, circle 51-150, double circle 151 or more.
GameTora's live tool is the authority for the tiers.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARAMS = Path("/workspace/params.json")
DATA = Path("/workspace/affinity.json")
TRI_MAX, CIRCLE_MIN, DOUBLE_MIN = 50, 51, 151
SLOTS = ("legacy1", "legacy2", "sub11", "sub12", "sub21", "sub22")


class CalcError(Exception):
    pass


class Data:
    def __init__(self, raw: dict, names: dict):
        self.chars = [int(c) for c in raw["chars"]]
        self.n = len(self.chars)
        self.a2, self.a3 = raw["aff2"], raw["aff3"]
        if len(self.a2) != self.n ** 2 or len(self.a3) != self.n ** 3:
            raise CalcError("the affinity data has the wrong size")
        self.idx = {c: i for i, c in enumerate(self.chars)}
        self.names = {int(k): v for k, v in names.items()}

    def name(self, c: int) -> str:
        return self.names.get(c) or str(c)

    def need(self, c) -> int:
        c = int(c)
        if c not in self.idx:
            raise CalcError(f"{self.name(c)} isn't in the affinity data")
        return c

    def pair(self, a: int, b: int) -> int:
        return self.a2[self.idx[a] * self.n + self.idx[b]]

    def triple(self, a: int, b: int, c: int) -> int:
        return self.a3[(self.idx[a] * self.n + self.idx[b]) * self.n + self.idx[c]]


def tier(total: float) -> str:
    if total >= DOUBLE_MIN:
        return "\u25ce double circle"
    if total >= CIRCLE_MIN:
        return "\u3007 circle"
    return "\u25b3 triangle"


def tier_note(total: float) -> str:
    if total >= DOUBLE_MIN:
        return ""
    if total >= CIRCLE_MIN:
        return f" ({DOUBLE_MIN - total:g} more for double circle)"
    return f" ({CIRCLE_MIN - total:g} more for circle, {DOUBLE_MIN - total:g} for double circle)"


def op_total(d: Data, p: dict) -> str:
    main = d.need(p.get("main"))
    legacies = [(k, d.need(p[k])) for k in ("legacy1", "legacy2") if p.get(k) not in (None, "")]
    if not legacies:
        raise CalcError("give at least one legacy")
    notes: list[str] = []
    lines: list[str] = []
    total = 0
    for k, leg in legacies:
        if leg == main:
            raise CalcError("a character can't be her own legacy")
        v = d.pair(main, leg)
        total += v
        lines.append(f"- {d.name(main)} + {d.name(leg)} (legacy {k[-1]}): {v}")
    if len(legacies) == 2:
        (_, a), (_, b) = legacies
        v = d.pair(a, b)
        total += v
        lines.append(f"- {d.name(a)} + {d.name(b)} (the two legacies): {v}")
        if a == b:
            notes.append("both legacies are the same character, which scores 0 together")
    for k in ("sub11", "sub12", "sub21", "sub22"):
        if p.get(k) in (None, ""):
            continue
        parent = dict(legacies).get("legacy" + k[3])
        if parent is None:
            raise CalcError(f"{k} needs legacy{k[3]} to be set")
        sub = d.need(p[k])
        v = d.triple(main, parent, sub)
        total += v
        lines.append(f"- {d.name(main)} + {d.name(parent)} + {d.name(sub)} (sub-legacy {k[3]}-{k[4]}): {v}")
        if sub in (main, parent):
            notes.append(f"{d.name(sub)} repeats a name in her own line, which the game data scores 0")
    bonus = float(p.get("bonus") or 0)
    out = ["Base affinity from the game data:"] + lines + [f"Base total: {total}"]
    final = total + bonus
    if bonus:
        out.append(f"Plus your race bonus: {bonus:g} -> total {final:g}")
    out.append(f"Result: {final:g} = {tier(final)}{tier_note(final)}")
    if not bonus:
        out.append("Race-win bonuses (shared G1 wins) are not included; pass bonus to add them.")
    out.extend(notes)
    return "\n".join(out)


def best_two_subs(d: Data, main: int, leg: int) -> list[tuple[int, int]]:
    cands = sorted(((d.triple(main, leg, s), s) for s in d.chars if s not in (main, leg)), key=lambda t: (-t[0], t[1]))
    return cands[:2]


def op_best(d: Data, p: dict) -> str:
    main = d.need(p.get("main"))
    top = max(1, min(int(p.get("top") or 5), 10))
    pinned = d.need(p["legacy1"]) if p.get("legacy1") not in (None, "") else None
    if pinned == main:
        raise CalcError("a character can't be her own legacy")
    pool = [c for c in d.chars if c != main]
    subs = {c: best_two_subs(d, main, c) for c in pool}
    sub_sum = {c: sum(v for v, _ in subs[c]) for c in pool}
    results = []
    firsts = [pinned] if pinned else pool
    for a in firsts:
        for b in pool:
            if b == a or (pinned is None and b < a):
                continue
            base = d.pair(main, a) + d.pair(main, b) + d.pair(a, b)
            results.append((base + sub_sum[a] + sub_sum[b], base, a, b))
    results.sort(key=lambda r: (-r[0], r[2], r[3]))
    out = [f"Best theoretical setups for {d.name(main)}" + (f" with {d.name(pinned)} as a legacy" if pinned else "") +
           " (base affinity; each legacy gets its two best sub-legacies; a real build is limited to the veterans you actually have):"]
    for rank, (total, base, a, b) in enumerate(results[:top], 1):
        sa = ", ".join(f"{d.name(s)} {v}" for v, s in subs[a])
        sb = ", ".join(f"{d.name(s)} {v}" for v, s in subs[b])
        out.append(f"{rank}. {total} ({tier(total)}): {d.name(a)} + {d.name(b)} (pairs {base}); "
                   f"subs of {d.name(a)}: {sa}; subs of {d.name(b)}: {sb}")
    out.append("Add race-win bonuses on top; the tier uses the base total only here.")
    return "\n".join(out)


def op_partners(d: Data, p: dict) -> str:
    main = d.need(p.get("main"))
    top = max(1, min(int(p.get("top") or 10), 25))
    ranked = sorted(((d.pair(main, c), c) for c in d.chars if c != main), key=lambda t: (-t[0], t[1]))
    lines = [f"{i}. {d.name(c)}: {v}" for i, (v, c) in enumerate(ranked[:top], 1)]
    return f"Highest pair affinity with {d.name(main)} (out of {len(ranked)} characters):\n" + "\n".join(lines)


OPS = {"total": op_total, "best": op_best, "partners": op_partners}


def run(params: dict, raw: dict) -> dict:
    op = str(params.get("op") or "").lower()
    if op not in OPS:
        return {"ok": False, "error": f"op must be one of {', '.join(OPS)}"}
    try:
        return {"ok": True, "text": OPS[op](Data(raw, params.get("names") or {}), params)}
    except CalcError as e:
        return {"ok": False, "error": str(e)}


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        raw = json.loads(DATA.read_text(encoding="utf-8"))
        result = run(params if isinstance(params, dict) else {}, raw)
    except Exception as e:
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
