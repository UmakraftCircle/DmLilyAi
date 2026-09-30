#!/usr/bin/env python3
"""Scrape the Uma Musume race list from GameTora into a text-only calendar.

Output: LilyAiGameSpace/Umamusume/Guide/RaceList/Racelist.md, one calendar table per year
(Junior / Classic / Senior), one row per half-month slot (Early Jan ... Late Dec).

Usage:
    python scrape_racelist.py            # scrape and write Racelist.md
    python scrape_racelist.py --dump     # also save rendered page to ./racelist_debug/

The page is rendered client-side, so a headless browser (Playwright) is used.
If nothing is parsed the script exits with an error and leaves Racelist.md
untouched, so a layout change on GameTora never wipes the file.
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from playwright.sync_api import sync_playwright

URL = "https://gametora.com/umamusume/races"
HERE = Path(__file__).resolve().parent            # .github/scripts
REPO_ROOT = HERE.parents[1]
OUT = REPO_ROOT / "LilyAiGameSpace/Umamusume/Guide/RaceList/Racelist.md"
DEBUG = REPO_ROOT / "racelist_debug"              # not committed

ROW_SELECTOR = "tr, [role=row], [class*=races_row]"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

YEARS = ["Junior", "Classic", "Senior"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SLOTS = [f"{half} {m}" for m in MONTHS for half in ("Early", "Late")]

TRACKS = ["Sapporo", "Hakodate", "Niigata", "Fukushima", "Nakayama", "Tokyo",
          "Chukyo", "Kyoto", "Hanshin", "Kokura", "Ooi", "Kawasaki",
          "Funabashi", "Morioka", "Longchamp"]
GRADE_ORDER = {"G1": 0, "G2": 1, "G3": 2, "OP": 3, "Pre-OP": 4, "Debut": 5, "Maiden": 5}

MONTH_PAT = "|".join(MONTHS)
# e.g. "Classic Year Late Dec" / "Classic Year, Late December"
PAIR_RE = re.compile(
    rf"\b(Junior|Classic|Senior)\b(?:\s+Year)?[\s,·\-|/]*\b(Early|Late)\s+({MONTH_PAT})[a-z]*",
    re.I,
)
YEAR_RE = re.compile(r"\b(Junior|Classic|Senior)\b", re.I)
SLOT_RE = re.compile(rf"\b(Early|Late)\s+({MONTH_PAT})[a-z]*", re.I)
GRADE_RE = re.compile(r"\b(G1|G2|G3|Pre-OP|OP|Debut|Maiden)\b")
DIST_RE = re.compile(r"\b(\d{3,4})\s*m\b")
SURFACE_RE = re.compile(r"\b(Turf|Dirt)\b", re.I)
CATEGORY_RE = re.compile(r"\b(Short|Mile|Medium|Long)\b")


def norm_slot(half: str, month: str) -> str:
    return f"{half.title()} {month[:3].title()}"


def collect_rows(page):
    """Return a list of rows, each a list of cell strings."""
    js_table = (
        "rows => rows.map(r => Array.from(r.querySelectorAll('th,td'))"
        ".map(c => c.innerText.trim()))"
    )
    rows = page.eval_on_selector_all("tr", js_table)
    rows = [r for r in rows if any(r)]
    if rows:
        return rows
    # Fallback for div-based layouts.
    js_div = "els => els.map(e => e.innerText.split('\\n').map(s => s.trim()).filter(Boolean))"
    return page.eval_on_selector_all("[role=row], [class*=races_row]", js_div)


def dump_page(page):
    DEBUG.mkdir(exist_ok=True)
    (DEBUG / "page.html").write_text(page.content(), encoding="utf-8")
    (DEBUG / "page.txt").write_text(page.inner_text("body"), encoding="utf-8")
    page.screenshot(path=str(DEBUG / "page.png"), full_page=False)


def load_rows(dump: bool):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            viewport={"width": 1400, "height": 1000},
            locale="en-US",
            user_agent=USER_AGENT,
        )
        page = context.new_page()

        # Skip images/fonts/media: faster, and less for ad scripts to hang on.
        page.route(
            "**/*",
            lambda route: route.abort()
            if route.request.resource_type in ("image", "media", "font")
            else route.continue_(),
        )

        # "networkidle" never fires here (ads/analytics keep connections open),
        # so wait for the DOM and then for the table itself.
        resp = page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        print(f"HTTP {resp.status if resp else '?'} | title={page.title()!r} | url={page.url}")
        try:
            # state="attached": a hidden first match must not cause a timeout.
            page.wait_for_selector(ROW_SELECTOR, state="attached", timeout=45000)
        except Exception:
            try:
                print("BODY START:", page.inner_text("body")[:800])
            except Exception:
                pass
            dump_page(page)
            browser.close()
            raise

        # Scroll until the row count stops growing (handles lazy/virtual lists).
        last, stable = -1, 0
        while stable < 3:
            page.mouse.wheel(0, 6000)
            page.wait_for_timeout(500)
            count = page.locator(ROW_SELECTOR).count()
            stable = stable + 1 if count == last else 0
            last = count

        rows = collect_rows(page)
        if dump or not rows:
            dump_page(page)
        browser.close()
    return rows


def parse_row(cells):
    text = " | ".join(cells)

    pairs = [(y.title(), norm_slot(h, m)) for y, h, m in PAIR_RE.findall(text)]
    if not pairs:  # year and slot in separate cells
        years = [y.title() for y in YEAR_RE.findall(text)]
        slots = [norm_slot(h, m) for h, m in SLOT_RE.findall(text)]
        if years and slots:
            pairs = [(y, s) for y in years for s in slots[:1]] if len(slots) == 1 \
                else list(zip(years, slots))
    if not pairs:
        return None

    name = None
    for cell in cells:
        first = cell.split("\n")[0].strip()
        if len(first) < 3 or not re.search(r"[A-Za-z]", first):
            continue
        if PAIR_RE.search(first) or SLOT_RE.search(first) or YEAR_RE.fullmatch(first):
            continue
        if GRADE_RE.fullmatch(first) or DIST_RE.search(first):
            continue
        name = first
        break
    if not name:
        return None

    grade = GRADE_RE.search(text)
    dist = DIST_RE.search(text)
    surface = SURFACE_RE.search(text)
    category = CATEGORY_RE.search(text)
    track = next((t for t in TRACKS if re.search(rf"\b{t}\b", text)), None)

    details = []
    if grade:
        details.append(grade.group(1))
    surf_dist = " ".join(
        x for x in [surface.group(1).title() if surface else "",
                    f"{dist.group(1)}m" if dist else ""] if x
    )
    if surf_dist:
        details.append(surf_dist)
    if category:
        details.append(category.group(1))
    if track:
        details.append(track)

    return [
        {
            "year": y, "slot": s, "name": name,
            "grade": grade.group(1) if grade else "",
            "details": " · ".join(details),
        }
        for y, s in pairs
    ]


def build(rows):
    calendar = {y: defaultdict(list) for y in YEARS}
    seen = set()
    for cells in rows:
        parsed = parse_row(cells)
        if not parsed:
            continue
        for r in parsed:
            key = (r["year"], r["slot"], r["name"], r["details"])
            if r["year"] in calendar and key not in seen:
                seen.add(key)
                calendar[r["year"]][r["slot"]].append(r)
    return calendar, len(seen)


def render(calendar) -> str:
    out = ["# Uma Musume Race Calendar", "",
           f"Source: {URL}", ""]
    for year in YEARS:
        out += [f"## {year} Year", "", "| Schedule | Races |", "|---|---|"]
        for slot in SLOTS:
            races = sorted(calendar[year].get(slot, []),
                           key=lambda r: (GRADE_ORDER.get(r["grade"], 9), r["name"]))
            cell = "<br>".join(
                f"**{r['name']}**" + (f" ({r['details']})" if r["details"] else "")
                for r in races
            ).replace("|", "\\|") or "—"
            out.append(f"| {slot} | {cell} |")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", action="store_true", help="save rendered page to ./racelist_debug/")
    args = ap.parse_args()

    rows = load_rows(args.dump)
    calendar, total = build(rows)
    if total == 0:
        print(f"No races parsed from {len(rows)} rows; see {DEBUG}/ . "
              "Racelist.md left unchanged.", file=sys.stderr)
        sys.exit(1)

    OUT.write_text(render(calendar) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({total} race entries).")


if __name__ == "__main__":
    main()
