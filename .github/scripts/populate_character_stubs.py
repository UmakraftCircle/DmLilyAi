#!/usr/bin/env python3
"""Populate stub Umamusume character profiles using the Special_Week.md layout.

A stub is any file in the Character folder that is under STUB_MAX_BYTES
(currently just a "# Name" heading). Files that already have content are
never touched, so the script is safe to re-run.

Source: the GameTora character page (server-rendered text). Only facts that
were actually parsed are written. Anything that could not be confirmed is
listed under "Gaps" instead of being guessed.

Game-specific short flavor text (ears, tail, family, trivia, weight line) is
not copied. If GROQ_API_KEY is set it is reworded with a free-tier Groq model;
otherwise those rows are left out and listed as gaps.

Usage:
  python populate_character_stubs.py [--limit N] [--only A,B] [--dry-run]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

CHAR_DIR = Path(os.environ.get("CHARACTER_DIR", "LilyAiGameSpace/Umamusume/Character"))
STUB_MAX_BYTES = 200
REQUEST_DELAY = 2.0
USER_AGENT = "LilyAi-profile-bot (+https://github.com/UmakraftCircle/DmLilyAi)"
GAMETORA = "https://gametora.com/umamusume/characters/"
WIKI_RAW = (
    "https://en.wikipedia.org/w/index.php"
    "?title=List_of_Umamusume:_Pretty_Derby_characters&action=raw"
)
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-20b")

# File stem -> GameTora slug, only for names where lowercase-with-hyphens is wrong.
# Example: "KS_Miracle": "k-s-miracle"
SLUG_OVERRIDES: dict[str, str] = {}

LABELS = [
    "Japanese name", "Voice actor", "Birthday", "School", "Dorm", "Height",
    "Weight", "Three sizes", "Shoe size", "Strong points", "Weak points",
    "Ears", "Tail", "Family", "Secrets", "Country of birth", "Races", "Wins",
    "Record", "Earnings", "Date of birth", "Date of death", "Profile",
    "Measurements", "Official art", "Character", "Background", "Version",
    "RL Counterpart",
]
LABEL_SET = set(LABELS)


class TextLines(HTMLParser):
    """Flatten HTML into a list of non-empty text lines."""

    SKIP = {"script", "style", "noscript", "svg"}

    def __init__(self):
        super().__init__()
        self.lines: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip:
            return
        text = " ".join(data.split())
        if text:
            self.lines.append(text)


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def field(lines: list[str], label: str) -> str | None:
    for i, line in enumerate(lines):
        if line == label and i + 1 < len(lines):
            nxt = lines[i + 1]
            return None if nxt in LABEL_SET else nxt
    return None


def secrets(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        if line.startswith("Did you know?"):
            out.append(line.removeprefix("Did you know?").strip())
    return out[:3]


def tagline(lines: list[str], display: str) -> str | None:
    if "Japanese name" not in lines:
        return None
    prev = lines[lines.index("Japanese name") - 1]
    if prev in (display, "Character versions") or len(prev) < 10:
        return None
    return prev


def reword(texts: list[str]) -> list[str] | None:
    """Paraphrase short flavor lines with Groq. Returns None if unavailable."""
    key = os.environ.get("GROQ_API_KEY")
    if not key or not texts:
        return None
    prompt = (
        "Reword each line below in your own words as a neutral, encyclopedia-style "
        "fact. Do not add any information that is not in the line. Keep each under "
        "25 words. Return ONLY a JSON array of strings, same length and order.\n\n"
        + json.dumps(texts, ensure_ascii=False)
    )
    body = json.dumps({
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(GROQ_URL, data=body, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            content = json.load(resp)["choices"][0]["message"]["content"]
        arr = json.loads(content[content.index("["): content.rindex("]") + 1])
        if len(arr) == len(texts) and all(isinstance(x, str) and x.strip() for x in arr):
            return [x.strip() for x in arr]
    except Exception as exc:  # optional step, never fatal
        print(f"  reword skipped: {exc}")
    return None


_wiki_cache: dict[str, str | None] = {}


def wiki_voice_actor(display: str) -> str | None:
    """Best-effort voice actor lookup in the Wikipedia character list."""
    if "text" not in _wiki_cache:
        try:
            _wiki_cache["text"] = fetch(WIKI_RAW)
        except Exception:
            _wiki_cache["text"] = None
    text = _wiki_cache["text"]
    if not text:
        return None
    pos = text.find(display)
    if pos < 0:
        return None
    chunk = text[pos: pos + 300]
    m = re.search(r"[Vv]oiced by\W+(?:\{\{[^|}]*\|)?([A-Z][A-Za-z.'-]+(?: [A-Z][A-Za-z.'-]+){1,3})", chunk)
    return m.group(1) if m else None


def cell(value: str | None) -> str:
    return value if value else "Not confirmed"


def render(name: str, url: str, lines: list[str], reworded: dict[str, str],
           voice: str | None, voice_from_wiki: bool) -> tuple[str, list[str]]:
    jp = field(lines, "Japanese name")
    gaps = [
        "Overview, background and personality: not filled in yet.",
        "Appearances (anime, game, other media): not filled in yet.",
        "Game data (versions, aptitudes, career objectives, stats, unique skills, support cards, images): "
        "not filled in by this script. Add them from uma.guide or GameTora.",
    ]
    if not reworded:
        gaps.insert(0, "Ears, tail, family, trivia and weight rows were left out (game text is not copied).")

    height = field(lines, "Height")
    height_cell = height if height and re.search(r"\d", height) else None
    infobox = [
        ("Name", name),
        ("Japanese name", cell(jp)),
        ("Voice actor", cell(voice)),
        ("Birthday", cell(field(lines, "Birthday"))),
        ("Height", cell(height_cell)),
        ("Three sizes", cell(field(lines, "Three sizes"))),
        ("Shoe size", cell(field(lines, "Shoe size"))),
        ("School", cell(field(lines, "School"))),
        ("Dorm", cell(field(lines, "Dorm"))),
        ("Strong point", cell(field(lines, "Strong points"))),
        ("Weak point", cell(field(lines, "Weak points"))),
    ]
    if reworded.get("weight"):
        infobox.insert(5, ("Weight", reworded["weight"]))

    out = [f"# {name}", ""]
    if jp:
        out.append(f"**Japanese name:** {jp}")
    out.append("**Series:** Umamusume: Pretty Derby (anime, game and franchise)")
    if reworded.get("tagline"):
        out.append(f"**Tagline (game):** {reworded['tagline']}")
    out += [
        "",
        "> Profile page in the style of an encyclopedia entry. Facts are gathered from the sources "
        "listed at the bottom and reworded. Values come from the sources' data at the time of the "
        "last automated update and can change with game updates.",
        "",
        "---",
        "",
        "## Infobox",
        "",
        "| Field | Details |",
        "|-------|---------|",
    ]
    out += [f"| {k} | {v} |" for k, v in infobox]

    out += ["", "## Overview", "", "Not filled in yet.", "", "## Background", "", "Not filled in yet."]

    detail_rows = [
        ("Ears", reworded.get("ears")), ("Tail", reworded.get("tail")),
        ("Family", reworded.get("family")),
    ]
    for i in range(3):
        detail_rows.append((f"Trivia {i + 1}", reworded.get(f"secret{i}")))
    detail_rows = [(k, v) for k, v in detail_rows if v]
    if detail_rows:
        out += ["", "## Profile details (game)", "", "| Detail | Description |", "|--------|-------------|"]
        out += [f"| {k} | {v} |" for k, v in detail_rows]

    rl = [
        ("Country of birth", field(lines, "Country of birth")),
        ("Date of birth", field(lines, "Date of birth")),
        ("Date of death", field(lines, "Date of death")),
        ("Races", field(lines, "Races")),
        ("Wins", field(lines, "Wins")),
        ("Record (1st-2nd-3rd-other)", field(lines, "Record")),
    ]
    earnings = field(lines, "Earnings")
    if earnings and earnings.isdigit():
        earnings = f"{int(earnings):,} JPY"
    elif earnings:
        earnings = earnings if "JPY" in earnings else f"{earnings} JPY"
    rl.append(("Earnings", earnings))
    rl = [(k, v) for k, v in rl if v]
    out += ["", "## Real-life counterpart", ""]
    if rl:
        out += [
            f"{name} is named after and based on a Japanese racehorse.", "",
            "| Field | Details |", "|-------|---------|",
        ]
        out += [f"| {k} | {v} |" for k, v in rl]
    else:
        out.append("Not confirmed from any source.")
        gaps.append("Real-life counterpart details were not found on the source page.")

    out += ["", "---", "", "## Game data: versions", "", "Not filled in yet (see Gaps).", "", "## Gaps", ""]
    out += [f"- {g}" for g in gaps]

    out += ["", "## Sources", "", "| Source | URL |", "|--------|-----|",
            f"| GameTora profile | {url} |"]
    if voice_from_wiki:
        out.append("| Wikipedia, list of characters (voice actor) | "
                   "https://en.wikipedia.org/wiki/List_of_Umamusume:_Pretty_Derby_characters |")
    out += ["", "Game materials are copyright Cygames, Inc.", ""]
    return "\n".join(out), gaps


def is_stub(path: Path) -> bool:
    return path.stat().st_size < STUB_MAX_BYTES


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--only", default="", help="comma-separated file stems, e.g. Kitasan_Black,Rice_Shower")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    only = {s.strip() for s in args.only.split(",") if s.strip()}
    stubs = sorted(p for p in CHAR_DIR.glob("*.md") if is_stub(p) and (not only or p.stem in only))
    print(f"{len(stubs)} stub(s) found; processing up to {args.limit}")

    done, skipped = [], []
    for path in stubs:
        if len(done) >= args.limit:
            break
        stem = path.stem
        display = stem.replace("_", " ")
        slug = SLUG_OVERRIDES.get(stem, stem.lower().replace("_", "-"))
        url = GAMETORA + slug
        print(f"- {stem}: {url}")
        try:
            html_text = fetch(url)
        except Exception as exc:
            skipped.append((stem, f"fetch error: {exc}"))
            continue
        finally:
            time.sleep(REQUEST_DELAY)
        if html_text is None:
            skipped.append((stem, "404 (add to SLUG_OVERRIDES)"))
            continue

        parser = TextLines()
        parser.feed(html_text)
        lines = parser.lines
        # Sanity check: must have parsed the basics or we write nothing.
        if not field(lines, "Japanese name") or not (field(lines, "Birthday") or field(lines, "Height")):
            skipped.append((stem, "page layout not recognised"))
            continue

        voice = field(lines, "Voice actor")
        from_wiki = False
        if not voice:
            voice = wiki_voice_actor(display)
            from_wiki = bool(voice)

        flavor = {
            "tagline": tagline(lines, display),
            "weight": field(lines, "Weight"),
            "ears": field(lines, "Ears"),
            "tail": field(lines, "Tail"),
            "family": field(lines, "Family"),
        }
        for i, s in enumerate(secrets(lines)):
            flavor[f"secret{i}"] = s
        flavor = {k: v for k, v in flavor.items() if v}
        keys = list(flavor)
        new = reword([flavor[k] for k in keys])
        reworded = dict(zip(keys, new)) if new else {}

        content, gaps = render(display, url, lines, reworded, voice, from_wiki)
        if args.dry_run:
            print(f"  [dry-run] would write {len(content)} bytes, {len(gaps)} gap(s)")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"  wrote {len(content)} bytes")
        done.append(stem)

    summary = [f"Populated: {len(done)}"] + [f"- {s}" for s in done]
    summary += [f"Skipped: {len(skipped)}"] + [f"- {s}: {why}" for s, why in skipped]
    text = "\n".join(summary)
    print("\n" + text)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write("## Character stub run\n\n" + text.replace("\n", "\n") + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
