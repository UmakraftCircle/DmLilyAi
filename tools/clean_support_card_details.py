#!/usr/bin/env python3
"""Clean up the scraped Support Card *-Details.md files.

What it fixes (see README block in the workflow for the rationale):
  * removes the leaked wiki CSS line (".mw-parser-output ...") from every card
  * turns the run-on "Unique Effect" line into a readable bullet list
  * restructures "Other Events" / "Event Chain" into explicit
      Event -> Choice -> Result bullets (falls back to the raw lines, minus
      junk, when a section can't be parsed with confidence)
  * removes scrape artifacts: doubled skill names ("Restart Restart"),
    stray icon lines ("○"), and "No data yet! Add it here ." placeholders

The script is idempotent: a cleaned file gets a marker comment on line 3 and is
skipped on later runs, so it is safe to run on every push. When the scraper
regenerates a file (marker gone) the cleaner simply runs again.

Usage:
  python tools/clean_support_card_details.py            # rewrite files in place
  python tools/clean_support_card_details.py --check    # exit 1 if any file needs cleaning
  python tools/clean_support_card_details.py path/to/X-Details.md ...
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

DEFAULT_GLOB = "LilyAiGameSpace/Umamusume/Support Cards/*-Details.md"
MARKER = "<!-- cleaned: support-card-details v1 -->"

# The wiki lists every possible effect for every card and uses "-" for the ones
# a card doesn't have. Dropping those keeps the list short. Flip to False to
# keep them as "none".
DROP_EMPTY_EFFECTS = True

VERBS = "Increases|Amplifies|Decreases|Reduces|Improves|Raises|Boosts|Recovers|Restores|Lowers|Enhances"
EFFECT_SPLIT = re.compile(r",\s+(?=[A-Z][A-Za-z' /]*? (?:%s)\b)" % VERBS)
EFFECT_SEG = re.compile(
    r"^(?P<name>[A-Z][A-Za-z' /]*?) (?P<desc>(?:%s)\b.*?)\s*"
    r"(?P<val>(?:[+-]?\d+%%?|-)?(?:\s*\([+-]?\d+%%?\))?)$" % VERBS
)
UNLOCK = re.compile(r"^Effect Lv(\d+)$")

CSS_LINE = re.compile(r"^- \.mw-parser-output\b")
PLACEHOLDER = re.compile(r"^No data yet!")
JUNK_LINE = re.compile(r"^[○◎×✕]$")
STAT = re.compile(
    r"\b(Speed|Stamina|Power|Guts|Wit|Bond|Mood|Energy|Max Energy|Skill Points?|All Stats)\s*[+-]\s*\d+", re.I
)
HINT_LINE = re.compile(r"^(?P<desc>.*?)\s*Hints?(?: Level)? \+(?P<n>\d+),?\s*$", re.I)
CHAIN_STEP = re.compile(r"^\((\d+) / (\d+)\)$")


# ----------------------------------------------------------------- unique effect
def format_unique_effect(body: str) -> list[str]:
    body = body.strip()
    if body in ("-", ""):
        return ["**Unique Effect:** none"]
    segs = EFFECT_SPLIT.split(body)
    out: list[str] = []
    unlock = None
    for seg in segs:
        m = UNLOCK.match(seg.strip())
        if m:
            unlock = m.group(1)
            continue
        m = EFFECT_SEG.match(seg.strip())
        if not m:
            return ["**Unique Effect (Lv1+):** " + body]  # unknown shape: leave untouched
        val = m.group("val").strip()
        if val == "-" or val == "":
            if DROP_EMPTY_EFFECTS:
                continue
            val = "none"
        out.append(f"- {m.group('name')}: {val} — {m.group('desc')}")
    head = "**Unique Effect**" + (f" (unlocks at Lv{unlock})" if unlock else "") + ":"
    return [head] + (out or ["- none"])


# ----------------------------------------------------------------- events
def dedupe_doubled(text: str) -> str:
    """'Restart Restart' -> 'Restart'; 'Left-Handed ○ Left-Handed ○' -> 'Left-Handed ○'."""
    parts = []
    for seg in text.split(", "):
        toks = seg.split()
        n = len(toks)
        if n >= 2 and n % 2 == 0 and toks[: n // 2] == toks[n // 2 :]:
            seg = " ".join(toks[: n // 2])
        parts.append(seg)
    return ", ".join(parts)


ICON_TAIL = re.compile(r"(\s+([☆★○◎♪♡]))(?:\s+\2)+\s*$")


def tidy(text: str) -> str:
    """Collapse trailing repeated icons ('Yes! Let's Hug ☆ ☆' -> '... ☆') and doubled names."""
    text = ICON_TAIL.sub(r"\1", text.strip())
    return dedupe_doubled(text)


def is_doubled_only(line: str) -> bool:
    return dedupe_doubled(line) != line and STAT.search(line) is None


def classify(line: str) -> str:
    if PLACEHOLDER.match(line):
        return "P"
    if JUNK_LINE.match(line):
        return "J"
    if HINT_LINE.match(line):
        return "H"
    if STAT.search(line) or is_doubled_only(line):
        return "O"   # stat line, or a bare "Skill Skill" line (skill hint gained)
    return "T"


def tokenize(lines: list[str]):
    """lines are raw section lines (with '- ' prefix or '' for blank)."""
    toks = []
    for raw in lines:
        if raw.strip() == "":
            toks.append(("BLANK", ""))
            continue
        text = raw[2:] if raw.startswith("- ") else raw
        toks.append((classify(text), text.strip()))
    return toks


class ParseError(Exception):
    pass


def parse_other_events(toks):
    """Return list of events: {"title": str|None, "choices": [{"text": str|None, "results": [Result]}]}"""
    events: list[dict] = []
    cur = None
    choice = None
    blank_seen = False
    i = 0

    def is_result(k):
        return k in ("O", "P")

    def new_event(title):
        nonlocal cur, choice
        cur = {"title": title, "choices": []}
        events.append(cur)
        choice = None

    def new_choice(text):
        nonlocal choice
        choice = {"text": text, "results": []}
        cur["choices"].append(choice)

    while i < len(toks):
        kind, text = toks[i]
        if kind == "BLANK":
            blank_seen = True
            i += 1
            continue
        if kind == "J":
            i += 1
            continue
        if kind == "H":
            if not (choice and choice["results"] and choice["results"][-1]["kind"] == "O"):
                raise ParseError("orphan hint line: " + text)
            choice["results"][-1]["hints"].append(text)
            i += 1
            continue
        if is_result(kind):
            if choice is None:
                if cur is None:
                    new_event(None)
                new_choice(None)
            choice["results"].append({"kind": kind, "text": text, "hints": []})
            blank_seen = False
            i += 1
            continue
        # kind == "T": look ahead to the next significant token
        j = i + 1
        while j < len(toks) and toks[j][0] in ("J",):
            j += 1
        nxt = toks[j][0] if j < len(toks) else None
        after_result = choice is not None and bool(choice["results"])
        if after_result and blank_seen:
            # blank line after a result => another choice of the same event
            new_choice(text)
        elif after_result or cur is None:
            # directly after a result (or first line) => a new event starts
            if nxt == "T":
                new_event(text)          # title, followed by choice text
                new_choice(toks[j][1])
                i = j
            elif nxt is not None and is_result(nxt):
                new_event(text)          # title with an unlabeled result
            else:
                raise ParseError("dangling text: " + text)
        else:
            raise ParseError("unexpected text: " + text)
        blank_seen = False
        i += 1
    for ev in events:
        for ch in ev["choices"]:
            if not ch["results"]:
                raise ParseError("choice without result: %r" % ch["text"])
    return events


def render_result(res) -> list[str]:
    if res["kind"] == "P":
        return ["_no data yet_"]
    return [dedupe_doubled(res["text"])]


def render_other_events(events) -> list[str]:
    out: list[str] = []
    for ev in events:
        title = ev["title"]
        out.append(f"- **{tidy(title)}**" if title is not None else "- **(untitled event)**")
        indent = "  "
        for ch in ev["choices"]:
            res_lines = []
            for r in ch["results"]:
                res_lines += render_result(r)
            joined = " / ".join(res_lines)
            if ch["text"] is None:
                out.append(f"{indent}- {joined}")
            else:
                out.append(f"{indent}- “{tidy(ch['text'])}” → {joined}")
            for r in ch["results"]:
                for h in r["hints"]:
                    m = HINT_LINE.match(h)
                    d = m.group("desc").strip()
                    out.append(f"{indent}  - Hint +{m.group('n')}" + (f": {d}" if d else ""))
    return out


def parse_chain(toks):
    sig = [t for t in toks if t[0] not in ("BLANK", "J")]
    steps = []
    pending: list[str] = []
    cur = None
    pending_choice = None
    for idx, (kind, text) in enumerate(sig):
        m = CHAIN_STEP.match(text)
        if m:
            name = re.sub(r"\s*→+\s*$", "", pending[-1]).strip() if pending else None
            cur = {"n": int(m.group(1)), "of": int(m.group(2)), "path": name, "results": []}
            steps.append(cur)
            pending, pending_choice = [], None
            continue
        nxt = sig[idx + 1][1] if idx + 1 < len(sig) else ""
        if kind in ("T", "O") and CHAIN_STEP.match(nxt) and (kind == "T" or is_doubled_only(text)):
            pending.append(text)          # event name that precedes "(n / m)"
            continue
        if kind == "T":
            if cur is None:
                raise ParseError("chain text before first step: " + text)
            pending_choice = text         # choice text inside the step
            continue
        if cur is None:
            raise ParseError("chain line before step: " + text)
        if kind in ("O", "P"):
            cur["results"].append({"kind": kind, "text": text, "hints": [], "choice": pending_choice})
            pending_choice = None
        elif kind == "H":
            if not cur["results"]:
                raise ParseError("orphan chain hint: " + text)
            cur["results"][-1]["hints"].append(text)
    for st in steps:
        if not st["results"]:
            raise ParseError("chain step without result")
    if pending_choice:
        raise ParseError("trailing chain text: " + pending_choice)
    return steps


def render_chain(steps) -> list[str]:
    if all(r["kind"] == "P" for s in steps for r in s["results"]):
        return ["_No chain data yet._"]
    out = []
    for st in steps:
        label = f"{st['n']}/{st['of']}" + (f" — {tidy(st['path'])}" if st["path"] else "")
        if any(r.get("choice") for r in st["results"]):
            out.append(f"- **Step {label}**")
            for r in st["results"]:
                body = " / ".join(render_result(r))
                out.append(f"  - “{tidy(r['choice'])}” → {body}" if r.get("choice") else f"  - {body}")
                for h in r["hints"]:
                    m = HINT_LINE.match(h)
                    d = m.group("desc").strip()
                    out.append(f"    - Hint +{m.group('n')}" + (f": {d}" if d else ""))
        else:
            body = " / ".join(x for r in st["results"] for x in render_result(r))
            out.append(f"- **Step {label}:** {body}")
            for r in st["results"]:
                for h in r["hints"]:
                    m = HINT_LINE.match(h)
                    d = m.group("desc").strip()
                    out.append(f"  - Hint +{m.group('n')}" + (f": {d}" if d else ""))
    return out


def raw_fallback(lines: list[str]) -> list[str]:
    """Minimal cleanup when we can't parse: drop junk/placeholders, dedupe names."""
    out = []
    for raw in lines:
        text = raw[2:] if raw.startswith("- ") else raw
        if raw.strip() and (JUNK_LINE.match(text.strip()) or PLACEHOLDER.match(text.strip())):
            continue
        out.append(("- " + dedupe_doubled(text)) if raw.startswith("- ") else raw)
    while out and out[-1] == "":
        out.pop()
    return out


# ----------------------------------------------------------------- card / file
class Stats:
    def __init__(self):
        self.cards = self.css_removed = self.fallbacks = 0
        self.fallback_examples: list[str] = []


def clean_card(card: str, stats: Stats) -> str:
    lines = card.split("\n")
    title = lines[0]
    out: list[str] = []
    i = 0
    n = len(lines)
    stats.cards += 1
    while i < n:
        line = lines[i]
        if line.startswith("**Unique Effect (Lv1+):**"):
            out += format_unique_effect(line.split(":** ", 1)[1] if ":** " in line else "")
            i += 1
            continue
        if line in ("**Event Chain**", "**Other Events**"):
            j = i + 1
            while j < n and not (lines[j].startswith("**") or lines[j].startswith("### ")):
                j += 1
            body = lines[i + 1 : j]
            before = len(body)
            body = [b for b in body if not CSS_LINE.match(b)]
            stats.css_removed += before - len(body)
            while body and body[-1].strip() == "":
                body.pop()
            toks = tokenize(body)
            try:
                if line == "**Event Chain**":
                    rendered = render_chain(parse_chain(toks)) if body else []
                else:
                    rendered = render_other_events(parse_other_events(toks)) if body else []
            except ParseError as e:
                stats.fallbacks += 1
                if len(stats.fallback_examples) < 8:
                    stats.fallback_examples.append(f"{title.strip()} [{line.strip('*')}]: {e}")
                rendered = raw_fallback(body)
            out.append(line)
            out += rendered
            out.append("")
            i = j
            continue
        out.append(line)
        i += 1
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip("\n") + "\n"
    return text


def clean_file(path: Path, stats: Stats) -> bool:
    src = path.read_text(encoding="utf-8")
    if MARKER in src:
        return False
    parts = re.split(r"(?m)^(?=### )", src)
    head, cards = parts[0], parts[1:]
    # section headers (## Speed ...) trail the previous card; split them off so
    # they survive card-level cleaning
    rebuilt = []
    for c in cards:
        m = re.search(r"(?m)^## ", c)
        tail = ""
        if m:
            c, tail = c[: m.start()], c[m.start() :]
        rebuilt.append(clean_card(c.rstrip("\n"), stats) + ("\n" + tail.rstrip("\n") + "\n" if tail else ""))
    new_head = head.rstrip("\n") + "\n\n" + MARKER + "\n\n"
    new_head = re.sub(r"\n{3,}", "\n\n", new_head)
    out = new_head + "\n".join(rebuilt)
    out = re.sub(r"\n{3,}", "\n\n", out).rstrip("\n") + "\n"
    if out != src:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--check", action="store_true", help="don't write; exit 1 if any file needs cleaning")
    args = ap.parse_args(argv)
    paths = [Path(p) for p in (args.paths or sorted(glob.glob(DEFAULT_GLOB)))]
    if not paths:
        print("no files matched", file=sys.stderr)
        return 0
    changed = []
    for p in paths:
        stats = Stats()
        src = p.read_text(encoding="utf-8")
        if args.check:
            needs = MARKER not in src
            print(f"{p}: {'needs cleaning' if needs else 'clean'}")
            if needs:
                changed.append(p)
            continue
        did = clean_file(p, stats)
        print(f"{p}: {'cleaned' if did else 'unchanged'} — cards={stats.cards} css_lines_removed={stats.css_removed} "
              f"unparsed_sections={stats.fallbacks}")
        for ex in stats.fallback_examples:
            print("   fallback:", ex)
        if did:
            changed.append(p)
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
