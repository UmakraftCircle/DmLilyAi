#!/usr/bin/env python3
"""Scrape the Uma Musume race list from GameTora into a text-only calendar.

Output: LilyAiGameSpace/Umamusume/Guide/RaceList/Racelist.md, one calendar table per year
(Junior / Classic / Senior), one row per half-month slot (Early Jan ... Late Dec).

Usage:
    python scrape_racelist.py            # scrape and write Racelist.md
    python scrape_racelist.py --dump     # also save rendered page to ./racelist_debug/

The page is rendered client-side, so a headless browser (Playwright) is used.
The race list is not an HTML table, so the script parses the page's visible text:
each race is a block of lines (name / year / slot / surface / track / category /
distance) that ends with a "Details" line.
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
YEAR_LINE_RE = re.compile(r"(Junior|Classic|Senior)\b", re.I)
SLOT_RE = re.compile(rf"(Early|Late)\s+({MONTH_PAT})[a-z]*", re.I)
FOUND_RE = re.compile(r"Found\s+(\d+)\s+results\.?", re.I)
GRADE_RE = re.compile(r"(G1|G2|G3|Pre-OP|OP|Debut|Maiden)")
DIST_RE = re.compile(r"\b(\d{3,4})\s*m\b")
SURFACE_RE = re.compile(r"\b(Turf|Dirt)\b", re.I)
CATEGORY_RE = re.compile(r"\b(Short|Mile|Medium|Long)\b")


def norm_slot(half: str, month: str) -> str:
    return f"{half.title()} {month[:3].title()}"


def dump_page(page):
    DEBUG.mkdir(exist_ok=True)
    (DEBUG / "page.html").write_text(page.content(), encoding="utf-8")
    (DEBUG / "page.txt").write_text(page.inner_text("body"), encoding="utf-8")
    page.screenshot(path=str(DEBUG / "page.png"), full_page=False)


def parse_records(text):
    """Parse the page's visible text into race dicts.

    Each race is: name / year ("Junior C.") / slot ("Late Jun") / surface /
    track / category / distance, followed by a "Details" line. A block that was
    cut off by scrolling doesn't have year and slot in lines 2-3 and is skipped.
    """
    m = FOUND_RE.search(text)
    if m:
        text = text[m.end():]
    races = []
    for block in re.split(r"\n\s*Details\s*(?:\n|$)", text):
        lines = [ln.strip() for ln in block.split("\n") if ln.strip()]
        if len(lines) < 3:
            continue
        ym = YEAR_LINE_RE.match(lines[1])
        sm = SLOT_RE.fullmatch(lines[2])
        if not ym or not sm:
            continue

        name = lines[0]
        rest = lines[3:]
        rest_text = " ".join(rest)

        grade = next((ln for ln in rest if GRADE_RE.fullmatch(ln)), "")
        dist = DIST_RE.search(rest_text)
        surface = SURFACE_RE.search(rest_text)
        category = CATEGORY_RE.search(rest_text)
        track = next((t for t in TRACKS if re.search(rf"\b{t}\b", rest_text)), None)

        details = []
        if grade:
            details.append(grade)
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

        races.append({
            "year": ym.group(1).title(),
            "slot": norm_slot(sm.group(1), sm.group(2)),
            "name": name,
            "grade": grade,
            "details": " · ".join(details),
        })
    return races


def load_races(dump: bool):
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
        # so wait for the DOM and then for the "Found N results" line.
        resp = page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        print(f"HTTP {resp.status if resp else '?'} | title={page.title()!r} | url={page.url}")
        try:
            page.wait_for_function(
                "() => /Found \\d+ results/.test(document.body.innerText)",
                timeout=45000,
            )
        except Exception:
            try:
                print("BODY START:", page.inner_text("body")[:800])
            except Exception:
                pass
            dump_page(page)
            browser.close()
            raise

        # Read the visible text after every scroll step and accumulate races, so
        # lazy-loaded and virtualised lists are both covered.
        seen = {}
        expected = None
        stable = 0
        for _ in range(500):
            text = page.inner_text("body")
            if expected is None:
                fm = FOUND_RE.search(text)
                expected = int(fm.group(1)) if fm else None
            before = len(seen)
            for r in parse_records(text):
                seen[(r["year"], r["slot"], r["name"], r["details"])] = r
            stable = stable + 1 if len(seen) == before else 0
            if (expected and len(seen) >= expected) or stable >= 8:
                break
            page.mouse.wheel(0, 1500)
            page.wait_for_timeout(300)
        print(f"Collected {len(seen)} races (page says {expected}).")

        if dump or not seen:
            dump_page(page)
        browser.close()
    return list(seen.values())


def build(races):
    calendar = {y: defaultdict(list) for y in YEARS}
    total = 0
    for r in races:
        if r["year"] in calendar:
            calendar[r["year"]][r["slot"]].append(r)
            total += 1
    return calendar, total


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

    races = load_races(args.dump)
    calendar, total = build(races)
    if total == 0:
        print(f"No races parsed; see {DEBUG}/ . Racelist.md left unchanged.",
              file=sys.stderr)
        sys.exit(1)

    OUT.write_text(render(calendar) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({total} race entries).")


if __name__ == "__main__":
    main()
