#!/usr/bin/env python3
"""
Build the Umamusume support card tables from the Umamusume Wiki (umamusu.wiki).

What it does
  - Lists every card page in Category:Support Cards through the MediaWiki API.
  - Downloads each page (cached, so re-runs are fast and polite to the wiki).
  - Reads rarity, type, the max-level bonus column, unique effect, hints and events.
  - Writes, into "LilyAiGameSpace/Umamusume/Support Cards/":
        SSR.md, SR.md, R.md            stat tables, one section per type
        SSR-Details.md, SR-Details.md, R-Details.md   unique effects, hints, events
        SupportCardList.md             index
  - Any bonus name that is not in the known list becomes a NEW COLUMN automatically.

How to run (needs Python 3.9+ and internet)
    pip install requests beautifulsoup4

    # 1) quick sanity check on 5 cards, written to a scratch folder
    python tools/build_support_cards.py --limit 5 --out tools/test_out

    # 2) full run (about 600 pages, roughly 5-10 minutes at the default delay)
    python tools/build_support_cards.py

Then commit the changed files in "Support Cards/". Cards that failed are listed in
tools/failed.txt; re-run the script to retry them (finished pages come from the cache).

NOTE: this script was written without being able to test it against the live site.
The stat table parsing is the most careful part. Hints and events are best effort:
if a card's hints/events look wrong, that is where to look first.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

API = "https://umamusu.wiki/w/api.php"
UA = "DmLilyAi-support-card-builder/1.0 (personal project, github.com/UmakraftCircle/DmLilyAi)"
NS_GAME = 3002

# Known bonus columns, in display order. New ones found on the wiki are appended.
KNOWN = [
    "Friendship Bonus", "Mood Effect",
    "Speed Bonus", "Stamina Bonus", "Power Bonus", "Guts Bonus", "Wit Bonus",
    "Training Effectiveness",
    "Initial Speed", "Initial Stamina", "Initial Power", "Initial Guts", "Initial Wit",
    "Initial Friendship Gauge", "Race Bonus", "Fan Bonus",
    "Hint Levels", "Hint Frequency", "Hint Quantity Bonus", "Specialty Priority",
    "Failure Protection", "Energy Cost Reduction", "Skill Point Bonus",
    "Wit Friendship Recovery", "Event Effectiveness", "Event Recovery",
]
TYPE_ORDER = ["Speed", "Power", "Stamina", "Guts", "Wit", "Group", "Friend"]
TYPE_MAP = {"Pal": "Friend"}
RARITIES = ["SSR", "SR", "R"]

CJK = re.compile(r"[\u3000-\u30ff\u3400-\u9fff\uff00-\uffef]+")
BLOCK = ["p", "div", "li", "ul", "ol", "table", "tr", "td", "th", "h2", "h3", "h4",
         "dl", "dd", "dt", "section", "hr", "br"]
DESC_START = re.compile(
    r"(.+?)(?=(?:Increases|Amplifies|Reduces|Decreases|Raises|Boosts|Provides|Recovers|"
    r"Prevents|Lowers|Improves|Grants|Gives)\b)"
)

ROOT = Path(__file__).resolve().parent
DEFAULT_OUT = ROOT.parent / "LilyAiGameSpace" / "Umamusume" / "Support Cards"
CACHE = ROOT / ".cache_support_cards"


# ---------------------------------------------------------------- network ----
def api_get(session, **params):
    params.update(format="json", formatversion=2)
    for attempt in range(4):
        try:
            r = session.get(API, params=params, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))


def list_cards(session):
    titles, cont = [], {}
    while True:
        data = api_get(session, action="query", list="categorymembers",
                       cmtitle="Category:Support Cards", cmnamespace=NS_GAME,
                       cmlimit=500, **cont)
        titles += [m["title"] for m in data["query"]["categorymembers"]]
        if "continue" in data:
            cont = data["continue"]
        else:
            return titles


def fetch_page(session, title, delay):
    CACHE.mkdir(exist_ok=True)
    key = hashlib.md5(title.encode("utf-8")).hexdigest()[:12]
    f = CACHE / f"{key}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    data = api_get(session, action="parse", page=title, prop="text|categories",
                   disableeditsection=1, redirects=1)
    p = data["parse"]
    page = {"title": title, "html": p["text"],
            "cats": [c["category"] for c in p.get("categories", [])]}
    f.write_text(json.dumps(page, ensure_ascii=False), encoding="utf-8")
    time.sleep(delay)
    return page


# ---------------------------------------------------------------- parsing ----
def effect_name(cell):
    strings = list(cell.stripped_strings)
    if not strings:
        return None
    first = strings[0]
    for k in sorted(KNOWN, key=len, reverse=True):
        if first.startswith(k):
            return k
    m = DESC_START.match(first)
    if m:
        return m.group(1).strip()
    return first if len(first) <= 40 else None


def find_bonus_table(soup):
    for t in soup.find_all("table"):
        first_row = t.find("tr")
        if not first_row:
            continue
        head = [c.get_text(strip=True) for c in first_row.find_all(["th", "td"])]
        if any(re.fullmatch(r"Lv\d+", h) for h in head) and "Friendship Bonus" in t.get_text():
            return t, head
    return None, []


def parse_unique(soup):
    node = soup.find(string=re.compile(r"Unique Effect"))
    if not node:
        return None
    tbl = node.find_next("table")
    if not tbl:
        return None
    parts = []
    for tr in tbl.find_all("tr"):
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
        if len(cells) >= 2 and cells[1]:
            val = cells[1]
            parts.append(f"{cells[0]} {'+' if val[:1].isdigit() else ''}{val}")
    return ", ".join(parts) or None


def parse_hints(soup, stop_tables):
    hints = []
    for tbl in soup.find_all("table"):
        if tbl in stop_tables or "Friendship Bonus" in tbl.get_text():
            break
        if not tbl.find("a", href=re.compile(r"Game:Skills")):
            continue
        for tr in tbl.find_all("tr"):
            strings = list(tr.stripped_strings)
            if not strings:
                continue
            name = strings[0]
            desc = [s for s in strings[1:]
                    if s != name and not (CJK.search(s) and not re.search(r"[A-Za-z]", s))]
            hints.append((name, " ".join(desc)))
    return hints


def _collect(node, out):
    for ch in node.children:
        if isinstance(ch, NavigableString):
            t = str(ch).strip()
            if t:
                out.append(("inline", t))
        elif isinstance(ch, Tag):
            if ch.name in ("script", "style"):
                continue
            if ch.name == "hr":
                out.append(("hr", "---"))
            elif ch.name == "br":
                out.append(("break", None))
            elif ch.name in ("h3", "h4"):
                out.append(("block", "**" + ch.get_text(" ", strip=True) + "**"))
            elif ch.find(BLOCK) is not None:
                _collect(ch, out)
            elif ch.name in BLOCK:
                out.append(("block", ch.get_text(" ", strip=True)))
            else:
                t = ch.get_text(" ", strip=True)
                if t:
                    out.append(("inline", t))


def parse_events(soup):
    h = soup.find(id="Training_Events")
    if not h:
        return []
    wrap = h.parent if h.parent is not None and "mw-heading" in " ".join(h.parent.get("class", [])) else h
    items = []
    for sib in wrap.next_siblings:
        if not isinstance(sib, Tag):
            continue
        if sib.get("id") == "Episode" or sib.find(id="Episode") is not None:
            break
        _collect(sib, items)
    lines, buf = [], []
    for kind, text in items:
        if kind == "inline":
            buf.append(text)
        else:
            if buf:
                lines.append(" ".join(buf))
                buf = []
            if kind in ("block", "hr"):
                lines.append(text)
    if buf:
        lines.append(" ".join(buf))
    clean = []
    for ln in lines:
        if ln != "---":
            ln = CJK.sub("", ln)
            ln = re.sub(r"(^|\s)edit$", "", ln.strip()).strip()
            ln = re.sub(r"\s+", " ", ln)
        if ln:
            clean.append(ln)
    return clean


def parse_card(page):
    title, html, cats = page["title"], page["html"], page["cats"]
    soup = BeautifulSoup(html, "html.parser")

    m = re.search(r"Support_Rarity_(SSR|SR|R)_Pill", html)
    tm = re.match(r"Game:(SSR|SR|R) ", title)
    rarity = m.group(1) if m else (tm.group(1) if tm else "SSR")
    m = re.search(r"Support_Type_([A-Za-z]+)\.png", html)
    ctype = TYPE_MAP.get(m.group(1), m.group(1)) if m else "Unknown"
    m = re.search(r"Support_Card_(\d+)\.png", html)
    card_id = int(m.group(1)) if m else None

    m = re.match(r"^Game:(?:(?:SSR|SR|R) )?(.+?) \((.+)\)$", title)
    name = f"[{m.group(2)}] {m.group(1)}" if m else title.replace("Game:", "", 1)

    m = re.search(r"Initially released \(EN\):\s*([0-9-]+)", soup.get_text(" "))
    if m:
        released = m.group(1)
    else:
        released = "EN" if "Support_Cards_on_Global" in cats else "JP only"

    table, head = find_bonus_table(soup)
    effects = {}
    if table is not None:
        for tr in table.find_all("tr")[1:]:
            cells = tr.find_all(["td", "th"])
            if len(cells) < 2:
                continue
            en = effect_name(cells[0])
            if not en:
                continue
            val = cells[-1].get_text(" ", strip=True)
            effects[en] = val if val else "-"

    return {
        "title": title, "name": name, "rarity": rarity, "type": ctype, "id": card_id,
        "released": released, "max_level": head[-1] if head else "?",
        "effects": effects,
        "unique": parse_unique(soup),
        "hints": parse_hints(soup, [table] if table is not None else []),
        "events": parse_events(soup),
    }


# ---------------------------------------------------------------- output -----
def esc(s):
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def build_tables(cards, columns, rarity):
    mine = [c for c in cards if c["rarity"] == rarity]
    levels = Counter(c["max_level"] for c in mine)
    lvl = levels.most_common(1)[0][0] if levels else "max level"
    out = [f"# {rarity} Support Cards", "",
           f"Stat bonuses at max level ({lvl}). Values in (+N) come from the card's unique effect. "
           "\"-\" means the card has no such bonus. Hints, unique effects and events: "
           f"see [{rarity}-Details.md]({rarity}-Details.md). "
           "Source: https://umamusu.wiki/Game:List_of_Support_Cards", ""]
    header = "| Support Card Name | " + " | ".join(columns) + " | EN Release |"
    sep = "| " + " | ".join(["---"] * (len(columns) + 2)) + " |"
    types = [t for t in TYPE_ORDER if t != "Group" or rarity == "SSR"]
    types += sorted({c["type"] for c in mine} - set(types))
    for t in types:
        out += [f"## {t}", "", header, sep]
        rows = sorted([c for c in mine if c["type"] == t], key=lambda c: c["id"] or 10 ** 9)
        for c in rows:
            vals = [esc(c["effects"].get(col, "-")) for col in columns]
            out.append(f"| {esc(c['name'])} | " + " | ".join(vals) + f" | {esc(c['released'])} |")
        out.append("")
    return "\n".join(out)


def build_details(cards, rarity):
    mine = [c for c in cards if c["rarity"] == rarity]
    out = [f"# {rarity} Support Card Details", "",
           f"Unique effects, hints and training events. Stat bonuses are in [{rarity}.md]({rarity}.md). "
           "Source: umamusu.wiki card pages.", ""]
    types = [t for t in TYPE_ORDER if t != "Group" or rarity == "SSR"]
    types += sorted({c["type"] for c in mine} - set(types))
    for t in types:
        rows = sorted([c for c in mine if c["type"] == t], key=lambda c: c["id"] or 10 ** 9)
        if not rows:
            continue
        out += [f"## {t}", ""]
        for c in rows:
            out += [f"### {c['name']}", ""]
            out.append(f"**Unique Effect (Lv1+):** {c['unique'] or '-'}")
            out.append("")
            out.append("**Hints**")
            if c["hints"]:
                out += [f"- {n}: {d}" if d else f"- {n}" for n, d in c["hints"]]
            else:
                out.append("- (none found)")
            out.append("")
            out.append("**Training Events**")
            if c["events"]:
                for ln in c["events"]:
                    out.append("" if ln == "---" else (ln if ln.startswith("**") else f"- {ln}"))
            else:
                out.append("- (none found)")
            out.append("")
    return "\n".join(out)


def build_index():
    return "\n".join([
        "# Support Card List", "",
        "Support cards are split by rarity, then by type inside each file. "
        "Tables hold stat bonuses only; hints, unique effects and events are in the detail files.", "",
        "- [SSR.md](SSR.md) / [SSR-Details.md](SSR-Details.md): Speed, Power, Stamina, Guts, Wit, Group, Friend",
        "- [SR.md](SR.md) / [SR-Details.md](SR-Details.md): Speed, Power, Stamina, Guts, Wit, Friend",
        "- [R.md](R.md) / [R-Details.md](R-Details.md): Speed, Power, Stamina, Guts, Wit, Friend", "",
        "Notes:",
        "- The wiki calls the Friend type \"Pal\".",
        "- \"-\" means the card has no such bonus; (+N) values come from the card's unique effect.",
        "- Generated by tools/build_support_cards.py from https://umamusu.wiki/Game:List_of_Support_Cards",
        ""])


# ------------------------------------------------------------------ main -----
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="output folder")
    ap.add_argument("--limit", type=int, help="only process the first N cards (for testing)")
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    args = ap.parse_args()

    session = requests.Session()
    session.headers["User-Agent"] = UA

    titles = list_cards(session)
    print(f"Found {len(titles)} card pages")
    if args.limit:
        titles = titles[:args.limit]

    cards, failed = [], []
    columns = list(KNOWN)
    for i, title in enumerate(titles, 1):
        try:
            card = parse_card(fetch_page(session, title, args.delay))
            if not card["effects"]:
                raise ValueError("no bonus table found")
            for k in card["effects"]:
                if k not in columns:
                    columns.append(k)
                    print(f"  new column detected: {k}")
            cards.append(card)
        except Exception as e:
            failed.append(f"{title}\t{e}")
            print(f"  FAILED {title}: {e}", file=sys.stderr)
        if i % 25 == 0 or i == len(titles):
            print(f"{i}/{len(titles)}")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for r in RARITIES:
        (out / f"{r}.md").write_text(build_tables(cards, columns, r), encoding="utf-8")
        (out / f"{r}-Details.md").write_text(build_details(cards, r), encoding="utf-8")
    (out / "SupportCardList.md").write_text(build_index(), encoding="utf-8")
    (ROOT / "failed.txt").write_text("\n".join(failed), encoding="utf-8")
    print(f"Done: {len(cards)} cards written to {out}; {len(failed)} failed (see tools/failed.txt)")


if __name__ == "__main__":
    main()
