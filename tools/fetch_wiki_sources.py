#!/usr/bin/env python3
"""Stage Umamusume Wiki text for character profiles that still have blank sections.

Only three sections are considered: Overview, Background and Appearances.
A section counts as blank when its body is empty or says "Not filled in yet".
Files where all three sections already have content are skipped completely.
For the others, only the wiki sections needed by the blank ones are saved.

Nothing in LilyAiGameSpace/Umamusume/Character is ever modified. The staged text
goes to sources/wiki/<n>.md and is meant to be read and reworded by hand.
Standard library only.
"""
import argparse
import datetime
import html as htmllib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAR_DIR = os.path.join(ROOT, "LilyAiGameSpace", "Umamusume", "Character")
OUT_DIR = os.path.join(ROOT, "sources", "wiki")
LOG_PATH = os.path.join(ROOT, "debug", "wiki-fetch.log")

WIKI = "https://umamusu.wiki"
UA = "DmLilyAi-profile-generator/1.0 (+https://github.com/UmakraftCircle/DmLilyAi)"

# File names that drop punctuation the wiki page title keeps. Key: norm_name(file stem).
# The override is tried first; the file's H1 and the file name stay as fallbacks.
TITLE_OVERRIDES = {
    "curren_bouquetdor": "Curren_Bouquetd'or",
    "mr_cb": "Mr._C.B.",
}

TARGETS = ("Overview", "Background", "Appearances")
BLANK_MARK = "not filled in yet"

# Wiki section titles (matched by keyword, case-insensitive) that feed each target.
KEYWORDS = {
    "Overview": ("biography", "profile", "personality"),
    "Background": ("biography", "personality", "relationship", "trivia"),
    "Appearances": ("appearance", "song", "discography", "trivia"),
}

H2 = re.compile(r"^==(?!=)\s*(.*?)\s*==\s*$", re.M)
DISCO_TEMPLATE = re.compile(r"\{\{\s*Character[_ ]Discography", re.I)


# ---------------------------------------------------------------- blank check

def norm_name(s):
    """Normalise a file name typed by hand: 'Air Shakur', 'air_shakur.md' -> 'air_shakur'."""
    s = s.strip()
    if s.lower().endswith(".md"):
        s = s[:-3]
    return re.sub(r"[\s\-]+", "_", s).lower()


def section_body(md, name):
    """Text under '## name' up to the next '## ' heading or '---' rule, or None."""
    m = re.search(r"^##\s+%s\s*$" % re.escape(name), md, re.M)
    if not m:
        return None
    rest = md[m.end():]
    n = re.search(r"^(##\s|---\s*$)", rest, re.M)
    return rest[: n.start()] if n else rest


def blank_sections(md):
    """Return the target sections that are blank (or whose heading is missing)."""
    out = []
    for name in TARGETS:
        body = section_body(md, name)
        if body is None or not body.strip() or BLANK_MARK in body.lower():
            out.append(name)
    return out


def wiki_title(md, stem):
    """Wiki page title candidates: a known override, then the file's H1, then the file name."""
    cands = []
    over = TITLE_OVERRIDES.get(norm_name(stem))
    if over:
        cands.append(over)
    m = re.search(r"^#\s+(.+?)\s*$", md, re.M)
    if m:
        cands.append(m.group(1).replace(" ", "_"))
    cands.append(stem)
    seen, out = set(), []
    for c in cands:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


# ------------------------------------------------------------------ wikitext

def norm_title(t):
    return re.sub(r"['*]+", "", t).strip()


def split_sections(text):
    """Split wikitext into (lead, [(title, body)]) using level-2 headings only.
    Level-3+ headings stay inside their parent section."""
    ms = list(H2.finditer(text))
    lead = text[: ms[0].start()] if ms else text
    secs = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        secs.append((norm_title(m.group(1)), text[m.end():end].strip()))
    return lead, secs


def pick_sections(secs, targets):
    """Sections needed by the given targets, in page order, without duplicates."""
    words = set()
    for t in targets:
        words.update(KEYWORDS[t])
    picked = []
    for title, body in secs:
        low = title.lower()
        if any(w in low for w in words):
            picked.append((title, body))
    return picked


def clean_text(text, strip_templates=False):
    """Light cleanup so staged text is readable. Not a finished profile."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<ref[^>]*/>", "", text)
    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text, flags=re.S)
    if strip_templates:
        prev = None
        while prev != text:
            prev = text
            text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\[\[(?:File|Image):[^\]]*\]\]", "", text, flags=re.I)
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"'{2,5}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ------------------------------------------------------------ rendered HTML

def html_to_text(h):
    """Turn a rendered HTML fragment (tables, lists) into plain lines."""
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", h)
    h = re.sub(r"(?i)</tr\s*>", "\n", h)
    h = re.sub(r"(?i)</t[dh]\s*>", " | ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</div>|</h[1-6]>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = htmllib.unescape(h)
    lines = []
    for ln in h.splitlines():
        ln = re.sub(r"\s+", " ", ln).strip()
        ln = re.sub(r"(\s*\|)+$", "", ln).strip()
        if ln:
            lines.append(ln)
    return "\n".join(lines)


def extract_rendered_section(page_html, heading_id):
    """Text of the level-2 section whose heading has the given id, from parsed HTML."""
    i = page_html.find('id="%s"' % heading_id)
    if i < 0:
        return None
    seg = page_html[i:]
    k = seg.find("</h2>")  # drop the rest of the heading itself
    seg = seg[k + 5:] if k >= 0 else seg[seg.find(">") + 1:]
    j = seg.find("<h2")
    if j >= 0:
        seg = seg[:j]
    text = html_to_text(seg)
    return text or None


# ------------------------------------------------------------------- network

def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # network error, timeout, DNS
        return 0, "%s: %s" % (type(e).__name__, e)


def fetch_wikitext(title, log, _depth=0):
    """Raw wikitext for a page, or None. Tries action=raw, then the API."""
    q = urllib.parse.quote(title, safe=":_.()!,'")
    code, text = http_get("%s/w/index.php?title=%s&action=raw" % (WIKI, q))
    if code == 200 and text.strip():
        m = re.match(r"\s*#REDIRECT\s*\[\[([^\]|#]+)", text, re.I)
        if m and _depth < 2:
            return fetch_wikitext(m.group(1).strip().replace(" ", "_"), log, _depth + 1)
        return text
    log("    raw fetch of %s returned HTTP %s" % (title, code or text[:80]))
    api = (
        "%s/w/api.php?action=query&prop=revisions&rvprop=content&rvslots=main"
        "&format=json&formatversion=2&redirects=1&titles=%s" % (WIKI, q)
    )
    code, body = http_get(api)
    if code == 200:
        try:
            page = json.loads(body)["query"]["pages"][0]
            return page["revisions"][0]["slots"]["main"]["content"]
        except (KeyError, IndexError, ValueError):
            pass
    log("    api fetch of %s returned HTTP %s" % (title, code or body[:80]))
    return None


def fetch_rendered_section(title, heading_id, log):
    """Rendered text of one section (used for template-generated song tables), or None."""
    q = urllib.parse.quote(title, safe=":_.()!,'")
    url = ("%s/w/api.php?action=parse&page=%s&prop=text&format=json&formatversion=2&redirects=1"
           % (WIKI, q))
    code, body = http_get(url)
    if code != 200:
        log("    rendered fetch of %s returned HTTP %s" % (title, code or body[:80]))
        return None
    try:
        page_html = json.loads(body)["parse"]["text"]
    except (KeyError, ValueError):
        log("    rendered fetch of %s returned unexpected data" % title)
        return None
    text = extract_rendered_section(page_html, heading_id)
    if not text:
        log("    rendered page of %s has no section %r" % (title, heading_id))
    return text


# ------------------------------------------------------------------ staging

def build_staged(stem, char_rel, blanks, title, page, irl_title, irl_text, songs_text=None):
    lead, secs = split_sections(page)
    picked = pick_sections(secs, blanks)
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    out = [
        "# Wiki source: %s" % stem.replace("_", " "),
        "",
        "- Character file: %s" % char_rel,
        "- Blank sections to fill: %s" % ", ".join(blanks),
        "- Page: %s/%s (retrieved %s UTC)" % (WIKI, urllib.parse.quote(title, safe=":_.()!,'"), today),
        "- License: Umamusume Wiki text is CC BY-SA 4.0. Reword before use. Game materials are copyright Cygames, Inc.",
        "- This is staging data with links and refs stripped. It is not the finished profile.",
        "",
    ]
    if "Overview" in blanks:
        out += ["## Lead", "", clean_text(lead, strip_templates=True) or "(empty)", ""]
    for t, body in picked:
        if songs_text and DISCO_TEMPLATE.search(body):
            out += ["## %s" % t, "", "(expanded from the rendered page; columns: song | album | type)", "", songs_text, ""]
        elif DISCO_TEMPLATE.search(body):
            out += ["## %s" % t, "", "(the wiki builds this list from a template that could not be expanded; songs are missing)", ""]
        else:
            out += ["## %s" % t, "", clean_text(body), ""]
    if not picked:
        out += ["(No matching sections found on the page. Check the page by hand.)", ""]
    if "Overview" in blanks and irl_text:
        rl, rs = split_sections(irl_text)
        excerpt = clean_text(rl, strip_templates=True)
        body = "\n\n".join("### %s\n\n%s" % (t, clean_text(b)) for t, b in rs[:3])
        text = (excerpt + "\n\n" + body).strip()
        out += ["## Real-life page (excerpt)", "", "Source: %s/%s" % (WIKI, urllib.parse.quote(irl_title, safe=":_.()!,'")), "", text[:3500], ""]
    return "\n".join(out).rstrip() + "\n"


def section_sizes(text):
    """'Biography (1200), Relationships (900)' from a staged file, for the log."""
    parts = re.split(r"^## ", text, flags=re.M)[1:]
    return ", ".join("%s (%d)" % (p.split("\n", 1)[0].strip(), len(p)) for p in parts)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--limit", type=int, default=3, help="max characters to fetch (0 = all)")
    ap.add_argument("--only", default="", help="comma-separated file names, e.g. Air_Groove,Agnes_Tachyon")
    ap.add_argument("--dry-run", action="store_true", help="fetch and preview, write no staged files")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests")
    args = ap.parse_args(argv)

    lines = []

    def log(msg):
        print(msg, flush=True)
        lines.append(msg)

    only = {norm_name(s) for s in args.only.split(",") if s.strip()}
    files = sorted(f for f in os.listdir(CHAR_DIR) if f.endswith(".md"))
    log("scanned %d character file(s) in %s" % (len(files), os.path.relpath(CHAR_DIR, ROOT)))
    todo, skipped, matched = [], [], set()
    for f in files:
        stem = f[:-3]
        if only:
            if norm_name(stem) not in only:
                continue
            matched.add(norm_name(stem))
        with open(os.path.join(CHAR_DIR, f), encoding="utf-8") as fh:
            md = fh.read()
        blanks = blank_sections(md)
        if not blanks:
            skipped.append(stem)
            continue
        todo.append((stem, md, blanks))

    for name in sorted(only - matched):
        log("no character file matches --only %r (use the file name without .md, e.g. Air_Shakur)" % name)

    log("%d character file(s) with blank sections, %d skipped (all three sections already filled)"
        % (len(todo), len(skipped)))
    for s in skipped:
        log("  skipped: %s" % s)
    if args.limit > 0:
        todo = todo[: args.limit]
    if not todo:
        log("nothing to fetch")
        _write_log(lines)
        # Asking for specific files and getting none is an error, not a green run.
        return 1 if only else 0

    staged = failed = 0
    first_songs = None
    for stem, md, blanks in todo:
        log("- %s: blank = %s" % (stem, ", ".join(blanks)))
        page, used = None, None
        for title in wiki_title(md, stem):
            page = fetch_wikitext(title, log)
            time.sleep(args.delay)
            if page:
                used = title
                break
        if not page:
            log("  FAILED: no wiki page found or the wiki blocked the request")
            failed += 1
            continue
        irl_title, irl_text = "IRL:" + used, None
        if "Overview" in blanks:
            irl_text = fetch_wikitext(irl_title, log)
            time.sleep(args.delay)
            if not irl_text:
                log("  note: no real-life page found (%s)" % irl_title)
        songs_text = None
        if "Appearances" in blanks and DISCO_TEMPLATE.search(page):
            songs_text = fetch_rendered_section(used, "Song_Discography", log)
            time.sleep(args.delay)
            log("  songs: %s" % ("%d line(s) expanded" % len(songs_text.splitlines()) if songs_text
                                  else "could not be expanded, noted in the staged file"))
            if songs_text and first_songs is None:
                first_songs = (stem, songs_text)
        char_rel = "LilyAiGameSpace/Umamusume/Character/%s.md" % stem
        text = build_staged(stem, char_rel, blanks, used, page, irl_title, irl_text, songs_text)
        log("  sections: %s" % section_sizes(text))
        if args.dry_run:
            log("  wrote (dry run, not saved) sources/wiki/%s.md, %d chars" % (stem, len(text)))
        else:
            os.makedirs(OUT_DIR, exist_ok=True)
            with open(os.path.join(OUT_DIR, stem + ".md"), "w", encoding="utf-8") as fh:
                fh.write(text)
            log("  wrote sources/wiki/%s.md, %d chars" % (stem, len(text)))
        staged += 1

    log("done: %d staged, %d failed" % (staged, failed))
    if first_songs and args.dry_run:
        log("")
        log("--- expanded song list for %s (first 25 lines) ---" % first_songs[0])
        for ln in first_songs[1].splitlines()[:25]:
            log(ln)
    _write_log(lines)
    return 0 if staged else 1


def _write_log(lines):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
