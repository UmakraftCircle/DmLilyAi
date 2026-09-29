#!/usr/bin/env python3
"""Generate Character/<Name>.md profiles for characters that are still one-line stubs.

Data sources (all fetched at run time, so this needs network access - it is meant
to run in GitHub Actions, not in an offline sandbox):
  * GameTora character pages  -> infobox, profile details, aptitudes, career
                                 objectives, per-version stats / growth bonuses
  * this repo's Support Cards/{SSR,SR,R}.md tables -> "Related support cards"

Output follows the layout of Special_Week.md / Vodka.md, minus the sections that
need a human (overview, background, real-life horse, appearances, unique skills).
Those are listed in the file's "Gaps" section so nobody mistakes the page for finished.

Safety rules:
  * a file is only written if it is a stub (a single "# Name" line) or already
    carries the generated marker below. Hand-written profiles are never touched.
  * a character that cannot be fetched/parsed is skipped and left as it was.

Usage:
  python tools/generate_character_profiles.py --limit 8
  python tools/generate_character_profiles.py --only Vodka,Air_Groove --refresh
  python tools/generate_character_profiles.py --slug KS_Miracle=ks-miracle
"""
from __future__ import annotations

import argparse
import datetime
import html.parser
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

CHAR_DIR = Path("LilyAiGameSpace/Umamusume/Character")
SUPPORT_DIR = Path("LilyAiGameSpace/Umamusume/Support Cards")
BASE = "https://gametora.com/umamusume/characters"
MARKER = "<!-- generated: character-profile v1 -->"
UA = "DmLilyAi-profile-generator/1.0 (+https://github.com/UmakraftCircle/DmLilyAi)"
DELAY = 0.7  # seconds between requests, be polite to the site

STATS = ["Speed", "Stamina", "Power", "Guts", "Wit"]
APT_KEYS = ["Turf", "Dirt", "Short", "Mile", "Medium", "Long", "Front", "Pace", "Late", "End"]
STRATEGY_NAME = {"Front": "Front Runner", "Pace": "Pace Chaser", "Late": "Late Surger", "End": "End Closer"}
RANK_ORDER = "SABCDEFG"
KNOWN_LABELS = {
    "Japanese name", "Voice actor", "Release date", "Birthday", "Height", "Weight", "Three sizes",
    "Shoe size", "School", "Dorm", "Strong points", "Weak points", "Ears", "Tail", "Family",
    "Base stats", "Stat bonuses", "Aptitude", "Objectives", "Measurements", "Profile",
    "Surface", "Distance", "Strategy",
} | set(STATS) | set(APT_KEYS)
KEY_BONUSES = ["Friendship Bonus", "Mood Effect", "Training Effectiveness", "Initial Friendship Gauge", "Specialty Priority"]


# ------------------------------------------------------------------ fetching
def fetch(url: str, retries: int = 3) -> str | None:
    """Return page text, or None for 404 / persistent failure."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
            with urllib.request.urlopen(req, timeout=25) as r:
                data = r.read().decode("utf-8", "replace")
            time.sleep(DELAY)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                time.sleep(DELAY)
                return None
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 * (attempt + 1))
                continue
            return None
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(3 * (attempt + 1))
    return None


class _TextExtractor(html.parser.HTMLParser):
    """HTML -> list of text lines (one per text node) plus h1 and first <em>/<i> text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.h1: str | None = None
        self.em: str | None = None
        self._skip = 0
        self._in_h1 = False
        self._in_em = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._skip += 1
        elif tag == "h1":
            self._in_h1 = True
        elif tag in ("em", "i"):
            self._in_em += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self._skip = max(0, self._skip - 1)
        elif tag == "h1":
            self._in_h1 = False
        elif tag in ("em", "i"):
            self._in_em = max(0, self._in_em - 1)

    def handle_data(self, data):
        if self._skip:
            return
        t = re.sub(r"\s+", " ", data).strip()
        if not t:
            return
        self.lines.append(t)
        if self._in_h1 and self.h1 is None:
            self.h1 = t
        if self._in_em and self.em is None:
            self.em = t


def html_to_lines(html_text: str):
    p = _TextExtractor()
    p.feed(html_text)
    return p.lines, p.h1, p.em


# ------------------------------------------------------------------ parsing
def _label_value(lines: list[str], label: str, start: int = 0):
    for i in range(start, len(lines) - 1):
        if lines[i] == label:
            nxt = lines[i + 1]
            if nxt in KNOWN_LABELS:
                return None, i
            return nxt, i
    return None, -1


def _clean(v: str | None) -> str | None:
    if v is None:
        return None
    v = v.strip()
    return None if v in ("", "???", "-", "cm") else v


def parse_profile(lines: list[str], em: str | None = None) -> dict:
    out: dict = {}
    for key, label in [
        ("jp", "Japanese name"), ("va", "Voice actor"), ("birthday", "Birthday"), ("school", "School"),
        ("dorm", "Dorm"), ("height", "Height"), ("weight", "Weight"), ("sizes", "Three sizes"),
        ("shoe", "Shoe size"), ("strong", "Strong points"), ("weak", "Weak points"),
        ("ears", "Ears"), ("tail", "Tail"), ("family", "Family"),
    ]:
        v, _ = _label_value(lines, label)
        out[key] = _clean(v)
    out["tagline"] = em
    # in-game introduction sits between the Dorm value and "Measurements"
    _, di = _label_value(lines, "Dorm")
    if di >= 0 and "Measurements" in lines[di:]:
        mi = lines.index("Measurements", di)
        intro = " ".join(lines[di + 2: mi]).strip()
        out["intro"] = intro or None
    else:
        out["intro"] = None
    trivia = []
    for i, ln in enumerate(lines):
        if ln.startswith("Did you know?"):
            rest = ln[len("Did you know?"):].strip()
            if not rest and i + 1 < len(lines) and not lines[i + 1].startswith("Did you know?"):
                rest = lines[i + 1]
            if rest and rest not in trivia:
                trivia.append(rest)
    out["trivia"] = trivia[:4]
    return out


def _stars(line: str) -> int:
    return line.count("⭐") + line.count("★")


def parse_version(lines: list[str], h1: str | None) -> dict:
    lines = _merge_turn_lines(lines)
    v: dict = {"title": h1}
    m = next((re.match(r"^\[(.+)\]$", l) for l in lines if re.match(r"^\[(.+)\]$", l) and "Character versions" not in l), None)
    v["epithet"] = m.group(1) if m else None
    m2 = re.search(r"\(([^)]+)\)\s*$", h1 or "")
    v["label"] = m2.group(1) if m2 else None
    rd, _ = _label_value(lines, "Release date")
    v["release"] = _clean(rd)
    # base stats: groups of five Speed..Wit values; a repeated label starts a new group
    _, bi = _label_value(lines, "Base stats")
    _, si = _label_value(lines, "Stat bonuses")
    groups: list[dict] = []
    if bi >= 0:
        end = si if si > bi else len(lines)
        cur: dict = {}
        stars = None
        for j in range(bi + 1, end):
            ln = lines[j]
            if _stars(ln) and ln.replace("⭐", "").replace("★", "").strip() == "":
                if cur:
                    groups.append(cur)
                    cur = {}
                stars = _stars(ln)
                cur = {"stars": stars}
            elif ln in STATS and j + 1 < len(lines) and re.fullmatch(r"\d+", lines[j + 1]):
                if ln in cur:
                    groups.append(cur)
                    cur = {}
                cur[ln] = int(lines[j + 1])
        if cur:
            groups.append(cur)
    v["stat_groups"] = [g for g in groups if any(k in g for k in STATS)]
    bonuses: dict = {}
    if si >= 0:
        for j in range(si + 1, len(lines) - 1):
            if lines[j] == "Aptitude":
                break
            if lines[j] in STATS:
                val = lines[j + 1]
                bonuses[lines[j]] = val if re.fullmatch(r"\d+%?", val) else None
    v["bonuses"] = bonuses
    _, ai = _label_value(lines, "Aptitude")
    apt: dict = {}
    if ai >= 0:
        for j in range(ai + 1, len(lines) - 1):
            if lines[j] == "Objectives":
                break
            if lines[j] in APT_KEYS and re.fullmatch(r"[A-G]", lines[j + 1]):
                apt[lines[j]] = lines[j + 1]
    v["aptitudes"] = apt
    v["objectives"] = _parse_objectives(lines)
    return v


def _merge_turn_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i] == "Turn" and i + 1 < len(lines) and re.fullmatch(r"\d+", lines[i + 1]):
            out.append(f"Turn {lines[i + 1]}")
            i += 2
        else:
            out.append(lines[i])
            i += 1
    return out


def _parse_objectives(lines: list[str]) -> list[dict]:
    objs: list[dict] = []
    start = next((i for i, l in enumerate(lines) if l == "Objectives"), None)
    if start is None:
        return objs
    i = start + 1
    while i < len(lines):
        m = re.match(r"^\*{0,2}(\d+)\.\s+(.+?)\*{0,2}$", lines[i])
        if m:
            o = {"n": int(m.group(1)), "text": m.group(2).strip(), "turn": None, "timing": None, "race": None}
            for k in range(i + 1, min(i + 6, len(lines))):
                ln = lines[k]
                if re.match(r"^\*{0,2}\d+\.\s+", ln):
                    break
                mt = re.match(r"^Turn\s+(\d+)", ln)
                if mt:
                    o["turn"] = mt.group(1)
                elif re.search(r"Class,", ln) and not o["timing"]:
                    o["timing"] = ln
                elif re.search(r"\d+m", ln) and not o["race"]:
                    o["race"] = re.sub(r"\s*[–-]\s*", ", ", ln)
            objs.append(o)
        i += 1
    return objs


def parse_character_id(raw_html: str) -> str | None:
    m = re.search(r"(?:chr_icon_|/profile/|chara_stand_)(\d{4})", raw_html)
    return m.group(1) if m else None


# ------------------------------------------------------------------ support cards
def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def load_support_cards(support_dir: Path = SUPPORT_DIR) -> dict[str, list[dict]]:
    by_char: dict[str, list[dict]] = {}
    for rarity in ("SSR", "SR", "R"):
        path = support_dir / f"{rarity}.md"
        if not path.exists():
            continue
        section = header = None
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                section, header = line[3:].strip(), None
            elif line.startswith("| Support Card Name"):
                header = [c.strip() for c in line.strip().strip("|").split("|")]
            elif header and line.startswith("|") and not line.startswith("| ---"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) != len(header):
                    continue
                m = re.match(r"^\[(.*?)\]\s*(.+)$", cells[0])
                if not m:
                    continue
                row = dict(zip(header, cells))
                by_char.setdefault(norm(m.group(2)), []).append({
                    "card": m.group(1), "rarity": rarity, "type": section,
                    "release": row.get("EN Release", ""), "row": row,
                })
    return by_char


# ------------------------------------------------------------------ rendering
def _best(ranks: dict, keys: list[str]) -> list[str]:
    have = [k for k in keys if k in ranks]
    if not have:
        return []
    top = min(RANK_ORDER.index(ranks[k]) for k in have)
    return [k for k in have if RANK_ORDER.index(ranks[k]) == top]


def best_fits(apt: dict) -> str | None:
    surf = _best(apt, ["Turf", "Dirt"])
    dist = _best(apt, ["Short", "Mile", "Medium", "Long"])
    strat = _best(apt, ["Front", "Pace", "Late", "End"])
    if not (surf and dist and strat):
        return None
    s = " or ".join(x.lower() for x in surf)
    d = " and ".join(dist)
    st = " or ".join(STRATEGY_NAME[x] for x in strat)
    return f"Best fits: {d} {s}, as a {st}."


def _growth(bonuses: dict) -> str:
    parts = [f"{k} {v}" for k, v in bonuses.items() if v]
    return ", ".join(parts) or "None listed"


def _nl(v) -> str:
    return v if v else "Not listed"


def _apt_table(apt: dict) -> list[str]:
    rows = ["| Category | Type | Rank |", "|----------|------|------|"]
    layout = [("Surface", ["Turf", "Dirt"]), ("Distance", ["Short", "Mile", "Medium", "Long"]),
              ("Strategy", ["Front", "Pace", "Late", "End"])]
    for cat, keys in layout:
        for k in keys:
            if k in apt:
                rows.append(f"| {cat} | {STRATEGY_NAME.get(k, k)} | {apt[k]} |")
    return rows


def _obj_table(objs: list[dict]) -> list[str]:
    rows = ["| # | Objective | Turn | Timing | Race |", "|---|-----------|------|--------|------|"]
    for o in objs:
        rows.append(f"| {o['n']} | {o['text']} | {o['turn'] or '-'} | {o['timing'] or '-'} | {o['race'] or '-'} |")
    return rows


def _stat_rows(v: dict) -> list[str]:
    rows = ["| Stats | Speed | Stamina | Power | Guts | Wit |", "|-------|-------|---------|-------|------|-----|"]
    for idx, g in enumerate(v["stat_groups"]):
        label = f"{g['stars']} star" if g.get("stars") else ("Base" if idx == 0 else "Max")
        rows.append(f"| {label} | " + " | ".join(str(g.get(s, "-")) for s in STATS) + " |")
    return rows


def _five_star(v: dict) -> dict:
    groups = v["stat_groups"]
    if not groups:
        return {}
    return next((g for g in groups if g.get("stars") == 5), groups[-1])


def support_table(cards: list[dict]) -> list[str]:
    rows = ["| Card | Rarity | Type | EN release | Key bonuses (max level) |", "|------|--------|------|------------|-------------------------|"]
    for c in cards:
        bits = [f"{k} {c['row'][k]}" for k in KEY_BONUSES if c["row"].get(k, "-") not in ("-", "")]
        rows.append(f"| [{c['card']}] | {c['rarity']} | {c['type']} | {c['release'] or '-'} | {', '.join(bits) or '-'} |")
    return rows


def render(name: str, slug: str, cid: str | None, profile: dict, versions: list[dict], cards: list[dict],
           today: datetime.date) -> str:
    p = profile
    L: list[str] = [f"# {name}", "", MARKER, ""]
    if p.get("jp"):
        L.append(f"**Japanese name:** {p['jp']}")
    L.append("**Series:** Umamusume: Pretty Derby (anime, game and franchise)")
    if p.get("tagline"):
        L.append(f"**Tagline (game):** \"{p['tagline'].strip('*')}\"")
    L += ["", f"> Auto-generated profile (not yet hand-reviewed). Values come from GameTora and this repo's support card "
              f"tables as of {today.isoformat()} and can change with game updates. Sections that need a human are listed under Gaps.",
          "", "---", "", "## Infobox", "", "| Field | Details |", "|-------|---------|",
          f"| Name | {name} |", f"| Japanese name | {_nl(p.get('jp'))} |", f"| Voice actor | {_nl(p.get('va'))} |",
          f"| Birthday | {_nl(p.get('birthday'))} |", f"| Height | {_nl(p.get('height'))} |",
          f"| Weight | {_nl(p.get('weight'))} |", f"| Three sizes | {_nl(p.get('sizes'))} |",
          f"| Shoe size | {_nl(p.get('shoe'))} |", f"| School | {_nl(p.get('school'))} |",
          f"| Dorm | {_nl(p.get('dorm'))} |", f"| Strong point | {_nl(p.get('strong'))} |",
          f"| Weak point | {_nl(p.get('weak'))} |"]
    names = [v["epithet"] for v in versions if v.get("epithet")]
    L.append(f"| Game versions | {len(versions)}" + (f" ({', '.join(names)})" if names else "") + " |")
    if p.get("intro"):
        L += ["", "## Introduction (game)", "", f"\"{p['intro']}\""]
    prof_rows = [("Ears", p.get("ears")), ("Tail", p.get("tail")), ("Family", p.get("family"))]
    prof_rows += [(f"Trivia {i}", t) for i, t in enumerate(p.get("trivia", []), 1)]
    prof_rows = [(k, v) for k, v in prof_rows if v]
    if prof_rows:
        L += ["", "## Profile details (game)", "", "| Detail | Description |", "|--------|-------------|"]
        L += [f"| {k} | {v} |" for k, v in prof_rows]
    L += ["", "---", "", "## Game data: versions", ""]
    n = len(versions)
    L += [f"{name} has {n} playable version{'s' if n != 1 else ''} in the game.", "",
          "| Version | uma.guide page | GameTora page |", "|---------|----------------|---------------|"]
    for v in versions:
        label = v.get("epithet") or v.get("title") or "Version"
        L.append(f"| {label}{' (' + v['label'] + ')' if v.get('label') else ''} | https://uma.guide/characters/{v['vid']} | {v['url']} |")
    apts = [v["aptitudes"] for v in versions if v["aptitudes"]]
    objs = [v["objectives"] for v in versions if v["objectives"]]
    shared_apt = bool(apts) and all(a == apts[0] for a in apts) and len(apts) == len(versions)
    shared_obj = bool(objs) and all(o == objs[0] for o in objs) and len(objs) == len(versions)
    L.append("")
    if shared_apt:
        L += ["### Shared aptitudes (all versions)", ""] + _apt_table(apts[0])
        bf = best_fits(apts[0])
        if bf:
            L += ["", bf]
        L.append("")
    if shared_obj:
        L += ["### Shared career objectives (all versions)", ""] + _obj_table(objs[0]) + [""]
    for i, v in enumerate(versions, 1):
        head = f"### Version {i}: {v.get('title') or name}" + (f" [{v['epithet']}]" if v.get("epithet") else "")
        L += [head, "", "| Field | Details |", "|-------|---------|", f"| Release date (Global) | {_nl(v.get('release'))} |"]
        if v["stat_groups"] and v["stat_groups"][0].get("stars"):
            L.append(f"| Rarity | {v['stat_groups'][0]['stars']} star (base) |")
        L += [f"| Stat growth bonuses | {_growth(v['bonuses'])} |", ""]
        if v["stat_groups"]:
            L += _stat_rows(v) + [""]
        if not shared_apt and v["aptitudes"]:
            L += ["**Aptitudes**", ""] + _apt_table(v["aptitudes"])
            bf = best_fits(v["aptitudes"])
            L += (["", bf] if bf else []) + [""]
        if not shared_obj and v["objectives"]:
            L += ["**Career objectives**", ""] + _obj_table(v["objectives"]) + [""]
    if len(versions) > 1:
        L += ["### Version comparison", "",
              "| Version | Release | Speed (5 star) | Stamina (5 star) | Power (5 star) | Guts (5 star) | Wit (5 star) | Growth bonuses |",
              "|---------|---------|----------------|------------------|----------------|---------------|--------------|----------------|"]
        for v in versions:
            g = _five_star(v)
            label = v.get("epithet") or v.get("title")
            L.append(f"| {label} | {_nl(v.get('release'))} | " + " | ".join(str(g.get(s, '-')) for s in STATS) + f" | {_growth(v['bonuses'])} |")
        L.append("")
    L += ["---", ""]
    if cards:
        L += ["## Related support cards", "", "Generated from this repo's support card tables. Values in (+N) come from the card's unique effect.", ""]
        L += support_table(cards) + [""]
    L += ["## Gaps", "",
          "Not filled in by the generator (these are not on the pages it reads): overview and background, real-life horse "
          "counterpart, appearances, unique skills, build notes, event lists and obtain methods. Add them by hand or in a "
          "follow-up research pass, then delete the generated marker line under the title so this file is no longer regenerated.",
          "", "## Sources", "", "| Source | URL |", "|--------|-----|", f"| GameTora profile | {BASE}/{slug} |"]
    for v in versions:
        L.append(f"| GameTora, {v.get('epithet') or v.get('title')} | {v['url']} |")
    L += ["| This repo, support card tables | LilyAiGameSpace/Umamusume/Support Cards |", "",
          "Game materials are copyright Cygames, Inc.", ""]
    if cid:
        L += ["## Images", "", "Each image is kept as its original URL.", "", "| Description | URL |", "|-------------|-----|"]
        for v in versions:
            L.append(f"| {v.get('epithet') or v.get('title')} standing art (GameTora) | https://gametora.com/images/umamusume/characters/chara_stand_{cid}_{v['vid']}.png |")
        L += [f"| Profile art | https://media.gametora.com/umamusume/characters/profile/{cid}.png |",
              f"| Character icon | https://gametora.com/images/umamusume/characters/icons/chr_icon_{cid}.png |", ""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(L)).rstrip("\n") + "\n"


# ------------------------------------------------------------------ orchestration
def display_name(stem: str) -> str:
    special = {"KS_Miracle": "K.S. Miracle", "TM_Opera_O": "T.M. Opera O", "Mr_CB": "Mr. C.B."}
    return special.get(stem, stem.replace("_", " "))


def slug_candidates(stem: str) -> list[str]:
    parts = stem.lower().split("_")
    cands = ["-".join(parts), "".join(parts)]
    if any(len(p) <= 2 for p in parts):
        cands.append("-".join(re.sub(r"(?<=.)(?=.)", "-", p) if len(p) <= 2 else p for p in parts))
    return list(dict.fromkeys(cands))


def is_stub(text: str) -> bool:
    body = [l for l in text.splitlines() if l.strip()]
    return len(body) <= 1 and (not body or body[0].startswith("# "))


def build_profile(stem: str, slug_override: str | None, cards_by_char: dict, log) -> str | None:
    name = display_name(stem)
    slug = raw_profile = None
    for cand in ([slug_override] if slug_override else slug_candidates(stem)):
        raw_profile = fetch(f"{BASE}/{cand}")
        if raw_profile:
            slug = cand
            break
    if not raw_profile:
        log(f"  no GameTora profile page found for {stem} (tried {slug_candidates(stem)}); use --slug")
        return None
    lines, _h1, em = html_to_lines(raw_profile)
    profile = parse_profile(lines, em)
    cid = parse_character_id(raw_profile)
    versions: list[dict] = []
    if cid:
        for n in range(1, 10):
            vid = f"{cid}{n:02d}"
            url = f"{BASE}/{vid}-{slug}"
            raw = fetch(url)
            if not raw:
                break
            vl, vh1, _ = html_to_lines(raw)
            v = parse_version(vl, vh1)
            v.update(vid=vid, url=url)
            if not v["stat_groups"] and not v["aptitudes"]:
                log(f"  {vid}: page fetched but no stats/aptitudes parsed - layout may have changed")
                break
            versions.append(v)
    if not versions:
        log(f"  no playable versions parsed for {stem} (character id: {cid})")
        return None
    return render(name, slug, cid, profile, versions, cards_by_char.get(norm(stem), []), datetime.date.today())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=0, help="max characters to process (0 = all)")
    ap.add_argument("--only", default="", help="comma-separated names/file stems, e.g. Vodka,Air_Groove")
    ap.add_argument("--refresh", action="store_true", help="also regenerate files that carry the generated marker")
    ap.add_argument("--slug", action="append", default=[], help="Stem=gametora-slug override (repeatable)")
    ap.add_argument("--char-dir", default=str(CHAR_DIR))
    args = ap.parse_args(argv)
    overrides = dict(s.split("=", 1) for s in args.slug)
    only = {norm(x) for x in args.only.split(",") if x.strip()}
    files = sorted(Path(args.char_dir).glob("*.md"))
    targets = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        eligible = is_stub(text) or (args.refresh and MARKER in text)
        if only:
            if norm(f.stem) in only and (eligible or MARKER in text):
                targets.append(f)
        elif eligible:
            targets.append(f)
    if args.limit:
        targets = targets[: args.limit]
    print(f"{len(targets)} profile(s) to generate")
    cards = load_support_cards()
    ok = failed = 0
    for f in targets:
        print(f"- {f.stem}")
        out = build_profile(f.stem, overrides.get(f.stem), cards, print)
        if out:
            f.write_text(out, encoding="utf-8")
            ok += 1
            print(f"  wrote {len(out)} bytes")
        else:
            failed += 1
    print(f"done: {ok} written, {failed} skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
