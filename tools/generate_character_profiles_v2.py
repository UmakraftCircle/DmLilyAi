#!/usr/bin/env python3
"""Character profile generator, v2: reads GameTora's embedded page JSON.

GameTora's pages keep stats and aptitudes in a JSON block (__NEXT_DATA__ ->
props.pageProps.itemData), not in the visible text, so v1's text parsing found
nothing. v2 takes numbers from that JSON, career objectives from the page text,
and reuses everything else (rendering, support-card tables, stub detection,
CLI options) from generate_character_profiles.py.

Usage is identical:
  python tools/generate_character_profiles_v2.py --limit 3
  python tools/generate_character_profiles_v2.py --only Air_Messiah
"""
from __future__ import annotations

import datetime
import json
import re
import sys

import generate_character_profiles as g

APT_KEYS = ["Turf", "Dirt", "Short", "Mile", "Medium", "Long", "Front", "Pace", "Late", "End"]
OBJ_HEAD = re.compile(r"^(\d+)\.\s+(.+)$")
TURN = re.compile(r"^Turn\s+(\d+)")
CLASS = re.compile(r"^(Junior|Classic|Senior)\s+Class$")
MONTH = re.compile(r"^(Early|Mid|Late)\s+[A-Za-z]+$")
RACE = re.compile(r"\d+m\b")


def next_data(raw: str) -> dict | None:
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', raw, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1)).get("props", {}).get("pageProps", {})
    except (ValueError, AttributeError):
        return None


def parse_objectives(lines: list[str]) -> list[dict]:
    """Objectives from page text. Timing arrives as separate nodes: 'Junior Class' ',' 'Late June'."""
    out: list[dict] = []
    start = next((i for i, l in enumerate(lines) if l == "Objectives"), None)
    if start is None:
        return out
    i = start + 1
    while i < len(lines):
        m = OBJ_HEAD.match(lines[i])
        if not m or int(m.group(1)) != len(out) + 1:   # only accept 1, 2, 3, ... in order
            i += 1
            continue
        o = {"n": int(m.group(1)), "text": m.group(2).strip(), "turn": None, "timing": None, "race": None}
        timing: list[str] = []
        k = i + 1
        while k < len(lines) and k < i + 9:
            ln = lines[k]
            if OBJ_HEAD.match(ln):
                break
            if TURN.match(ln):
                o["turn"] = TURN.match(ln).group(1)
            elif ln == ",":
                timing.append(",")
            elif CLASS.match(ln) or MONTH.match(ln):
                timing.append(ln)
            elif RACE.search(ln) and re.search(r"[–-]", ln):
                o["race"] = re.sub(r"\s*[–-]\s*", ", ", ln)
            else:
                break
            k += 1
        o["timing"] = re.sub(r"\s+,", ",", " ".join(timing)).strip() or None
        out.append(o)
        i = max(k, i + 1)
    return out


def parse_version_page(raw: str, vid: str, url: str, log) -> dict | None:
    pp = next_data(raw)
    item = (pp or {}).get("itemData")
    if not isinstance(item, dict) or not item.get("base_stats") or not item.get("aptitude"):
        log(f"  {vid}: page has no usable itemData JSON (keys: {sorted(item) if isinstance(item, dict) else None})")
        return None
    lines, h1, _ = g.html_to_lines(raw)
    rarity = item.get("rarity")
    groups = [{"stars": rarity, **dict(zip(g.STATS, item["base_stats"]))}]
    if item.get("four_star_stats"):
        groups.append({"stars": 4, **dict(zip(g.STATS, item["four_star_stats"]))})
    if item.get("five_star_stats"):
        groups.append({"stars": 5, **dict(zip(g.STATS, item["five_star_stats"]))})
    bonus = item.get("stat_bonus") or [0] * 5
    title = (item.get("title_en_gl") or item.get("title") or "").strip("[] ") or None
    label = re.search(r"\(([^)]+)\)\s*$", h1 or "")
    release = item.get("release_en")
    if not release and item.get("release"):
        release = f"Not released globally yet (JP release: {item['release']})"
    return {
        "title": h1,
        "epithet": title,
        "label": label.group(1) if label else None,
        "release": release,
        "stat_groups": groups,
        "bonuses": {s: (f"{v}%" if v else None) for s, v in zip(g.STATS, bonus)},
        "aptitudes": dict(zip(APT_KEYS, item["aptitude"])),
        "objectives": parse_objectives(lines),
        "vid": vid,
        "url": url,
    }


def build_profile(stem: str, slug_override: str | None, cards_by_char: dict, log) -> str | None:
    name = g.display_name(stem)
    slug = raw_profile = None
    for cand in ([slug_override] if slug_override else g.slug_candidates(stem)):
        raw_profile = g.fetch(f"{g.BASE}/{cand}")
        if raw_profile:
            slug = cand
            break
    if not raw_profile:
        log(f"  no GameTora profile page found for {stem} (tried {g.slug_candidates(stem)}); use --slug")
        return None
    lines, _h1, em = g.html_to_lines(raw_profile)
    profile = g.parse_profile(lines, em)
    cid = g.parse_character_id(raw_profile)
    if not cid:
        log(f"  no character id found in the profile page of {stem}")
        return None
    versions: list[dict] = []
    for n in range(1, 10):
        vid = f"{cid}{n:02d}"
        url = f"{g.BASE}/{vid}-{slug}"
        raw = g.fetch(url)
        if not raw:
            break
        v = parse_version_page(raw, vid, url, log)
        if v is None:
            break
        versions.append(v)
    if not versions:
        log(f"  no playable versions parsed for {stem} (character id: {cid})")
        return None
    log(f"  {len(versions)} version(s); objectives per version: {[len(v['objectives']) for v in versions]}")
    return g.render(name, slug, cid, profile, versions, cards_by_char.get(g.norm(stem), []), datetime.date.today())


g.build_profile = build_profile

if __name__ == "__main__":
    sys.exit(g.main())
