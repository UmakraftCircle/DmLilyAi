"""Rank a user's saved parents for a target, using the deterministic part of the Career Start Workflow:

    scenario white skill > pink sparks (distance > track > style) > white count

The Unique Skill Gate (does the unique activate on the target track?) and compatibility are NOT judged
here. They need the Skill docs and the in-game compatibility rating, so the model and the user check them.
"""
from typing import Callable

from LilyAiGameSpace.UmamusumeCatalog import SCENARIO_SPIRIT

_PINK_POINTS = (("distance", 3.0), ("track", 2.0), ("style", 1.0))


def rank_parents(
    parents: list[dict],
    *,
    trainee_uma_id: str | None = None,
    scenario: str | None = None,
    distance: str | None = None,
    track: str | None = None,
    style: str | None = None,
) -> list[tuple[float, dict, list[str]]]:
    """Return (score, parent, reasons) sorted best first; ties keep the lower parent number first."""
    targets = {"distance": distance, "track": track, "style": style}
    want_spirit = SCENARIO_SPIRIT.get(scenario or "")
    ranked: list[tuple[float, dict, list[str]]] = []
    for p in parents:
        score, why = 0.0, []
        if want_spirit:
            mine = [s for s in p.get("scenario_white") or [] if s.get("name") == want_spirit]
            if mine:
                score += 4
                why.append(f"{want_spirit} +4")
                if any(s.get("plus") for s in mine):
                    score += 1
                    why.append("plus version +1")
            else:
                why.append(f"no {want_spirit}")
        wc = p.get("white_count")
        if wc is not None:
            pts = 3 if wc >= 60 else 2 if wc >= 40 else 1 if wc > 0 else 0
            score += pts
            why.append(f"{wc} whites +{pts}")
        for kind, base in _PINK_POINTS:
            target = targets[kind]
            if not target:
                continue
            hit = next((s for s in p.get("pink") or [] if s.get("kind") == kind and s.get("aptitude") == target), None)
            if hit:
                stars = int(hit.get("stars") or 0)
                bonus = base + 0.1 * stars
                score += bonus
                why.append(f"{kind} {target} {stars}★ +{bonus:g}")
            else:
                why.append(f"no {kind} {target} spark")
        if trainee_uma_id and p.get("uma_id") == trainee_uma_id:
            why.append("same uma as the trainee")
        ranked.append((round(score, 1), p, why))
    ranked.sort(key=lambda t: (-t[0], t[1]["parent_id"]))
    return ranked


def _spirit_text(s: dict) -> str:
    stat = f" {s['stat'].title()}" if s.get("stat") else ""
    return f"{s['name'].title()}{stat}{'+' if s.get('plus') else ''}"


def parent_line(p: dict, name_of: Callable[[str], str]) -> str:
    head = f"#{p['parent_id']} {name_of(p['uma_id'])}"
    if p.get("nickname"):
        head += f' "{p["nickname"]}"'
    bits = [head]
    if p.get("scenario"):
        bits.append(p["scenario"].title())
    if p.get("white_count") is not None:
        bits.append(f"{p['white_count']} whites")
    if p.get("scenario_white"):
        bits.append("scenario white: " + ", ".join(_spirit_text(s) for s in p["scenario_white"]))
    if p.get("pink"):
        bits.append("pink: " + ", ".join(f"{s['kind']} {s['aptitude']} {s['stars']}★" for s in p["pink"]))
    blue = p.get("blue") or {}
    if blue.get("stat"):
        bits.append(f"blue: {blue['stat'].title()} {blue.get('stars', '?')}★")
    if p.get("unique_skill"):
        bits.append(f"unique: {p['unique_skill']}")
    if p.get("key_whites"):
        bits.append("key whites: " + ", ".join(p["key_whites"]))
    gps = [g.get("name", "?") + (f" ({g['unique_skill']})" if g.get("unique_skill") else "") for g in p.get("grandparents") or []]
    if gps:
        bits.append("grandparents: " + ", ".join(gps))
    return " | ".join(bits)
