"""Read-only docs engine for the Umamusume game space.

LilyAi never opens the markdown files itself. It asks this engine, which indexes
LilyAiGameSpace/Umamusume/**/*.md at startup, re-checks for changed files in the
background of normal calls, and hands back small, section-sized pieces of text so
the free-tier Groq models do not burn their context on whole documents.

Three operations are exposed (wrapped as Groq tools in LilyAiTool/GameSpaceTools):

    list_docs(category)        what exists
    search(query, category)    best-matching sections across all docs
    read(ref, section)         one doc, or one section of it

Design notes:
- Documents are addressed by id ("Character/Special_Week"), by title, or by alias
  ("Special Week", "special_week", the Japanese name). The model never passes a
  filesystem path, so it cannot read anything outside the docs folder.
- Docs are split at markdown headings; search ranks sections, not files.
- The "Images" section of a doc is hidden for now (images are out of scope), and
  markdown image syntax is reduced to its alt text.
- Standard library only.
"""

from __future__ import annotations

import difflib
import math
import re
import threading
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent / "Umamusume"

MAX_FILE_BYTES = 2_000_000
DEFAULT_READ_CHARS = 6000
MAX_READ_CHARS = 12000
SNIPPET_CHARS = 240

_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*#*\s*$")
_FENCE_RE = re.compile(r"^\s*(```|~~~)")
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_URL_RE = re.compile(r"https?://[^\s|)>\]]+")
_TOKEN_RE = re.compile(r"\w+")
_CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_JP_LINE_RE = re.compile(r"\*\*Japanese name:\*\*\s*(.+)")
_JP_ROW_RE = re.compile(r"\|\s*Japanese name\s*\|\s*([^|]+?)\s*\|")
_PAREN_RE = re.compile(r"^(.*?)\s*\((.*?)\)\s*$")

# Hidden from outlines, reads and search (images are out of scope for now).
_HIDDEN_SECTIONS = {"images"}
# Readable, but not searched (mostly URLs, which only add noise to ranking).
_UNSEARCHED_SECTIONS = {"sources"}

_STOPWORDS = frozenset(
    "a an and are as at be but by can do does for from how i in is it me my of on or "
    "the to was what when where which who why with you tell about please give".split()
)


def _norm(text: str) -> str:
    """Case/punctuation/space-insensitive key; keeps non-ASCII letters (Japanese names)."""
    return re.sub(r"[\W_]+", "", text.casefold())


def _stem(token: str) -> str:
    if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def _tokens(text: str) -> list[str]:
    return [_stem(t) for t in _TOKEN_RE.findall(text.replace("_", " ").casefold())]


def _strip_images(text: str) -> str:
    return _IMAGE_RE.sub(lambda m: m.group(1), text)


@dataclass
class Section:
    heading: str
    level: int
    path: str
    text: str
    terms: Counter = field(default_factory=Counter)
    head_terms: frozenset = frozenset()

    @property
    def key(self) -> str:
        return self.heading.casefold().strip()


@dataclass
class Doc:
    id: str
    category: str
    title: str
    aliases: list[str]
    sections: list[Section]
    sources: list[str]
    sig: tuple[int, int]
    name_terms: frozenset = frozenset()

    @property
    def chars(self) -> int:
        return sum(len(s.text) + len(s.heading) + 4 for s in self.sections)

    def visible(self) -> list[Section]:
        return [s for s in self.sections if s.key not in _HIDDEN_SECTIONS]


@dataclass
class DocInfo:
    id: str
    category: str
    title: str
    chars: int


@dataclass
class Hit:
    doc_id: str
    title: str
    section: str
    snippet: str
    score: float


@dataclass
class ReadResult:
    doc_id: str
    title: str
    section: str | None          # matched section path, None when the doc itself was read
    text: str
    truncated: bool
    outline: list[str]           # "Heading path (N chars)", for follow-up reads
    sources: list[str]
    note: str = ""


def _split_frontmatter(raw: str) -> tuple[dict[str, str], str]:
    if not raw.startswith("---"):
        return {}, raw
    lines = raw.splitlines()
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta: dict[str, str] = {}
            for line in lines[1:i]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().casefold()] = v.strip()
            return meta, "\n".join(lines[i + 1:])
    return {}, raw


def _split_list(value: str) -> list[str]:
    value = value.strip().strip("[]")
    return [p.strip().strip("'\"") for p in value.split(",") if p.strip().strip("'\"")]


def _parse_sections(body: str) -> list[Section]:
    sections: list[Section] = []
    stack: list[tuple[int, str]] = []
    cur_heading, cur_level, cur_path = "", 0, ""
    buf: list[str] = []
    in_fence = False

    def flush() -> None:
        text = "\n".join(buf).strip("\n")
        if cur_heading or text.strip():
            sections.append(Section(cur_heading or "Overview", cur_level, cur_path or "Overview", text))

    for line in body.splitlines():
        if _FENCE_RE.match(line):
            in_fence = not in_fence
        m = None if in_fence else _HEADING_RE.match(line)
        if m:
            flush()
            buf = []
            level, heading = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, heading))
            deeper = [h for lv, h in stack if lv > 1]
            cur_heading, cur_level = heading, level
            cur_path = " > ".join(deeper) if deeper else heading
        else:
            buf.append(line)
    flush()

    for s in sections:
        s.text = _strip_images(s.text)
        s.terms = Counter(_tokens(s.heading + " " + s.text))
        s.head_terms = frozenset(_tokens(s.path))
    return sections


def _aliases_for(path: Path, title: str, sections: list[Section], meta: dict[str, str]) -> list[str]:
    names: list[str] = [title]
    stem = path.stem
    parent = path.parent.name
    for base in (stem, parent if stem.casefold() == "readme" else ""):
        if base:
            spaced = base.replace("_", " ").replace("-", " ")
            names += [spaced, _CAMEL_RE.sub(" ", spaced)]
    if "aliases" in meta:
        names += _split_list(meta["aliases"])

    # Characters: "**Japanese name:** スペシャルウィーク (Supesharu Wīku)" or an infobox row.
    intro = "\n".join(s.text for s in sections[:2])
    for rx in (_JP_LINE_RE, _JP_ROW_RE):
        m = rx.search(intro)
        if m:
            raw = m.group(1).strip()
            pm = _PAREN_RE.match(raw)
            names += [pm.group(1), pm.group(2)] if pm else [raw]

    out, seen = [], set()
    for n in names:
        n = n.strip()
        if n and _norm(n) not in seen:
            seen.add(_norm(n))
            out.append(n)
    return out


class UmamusumeGameSpaceEngine:
    def __init__(self, root: Path | str | None = None, refresh_interval: float = 30.0):
        self.root = Path(root) if root else DOCS_ROOT
        self.refresh_interval = refresh_interval
        self._docs: dict[str, Doc] = {}
        self._alias_map: dict[str, list[str]] = {}
        self._df: Counter = Counter()
        self._n_sections = 0
        self._last_check = float("-inf")
        self._lock = threading.RLock()
        self.refresh(force=True)

    # ---------------------------------------------------------------- indexing
    def refresh(self, force: bool = False) -> bool:
        """Re-scan the docs folder (at most every refresh_interval seconds). True if anything changed."""
        with self._lock:
            now = time.monotonic()
            if not force and now - self._last_check < self.refresh_interval:
                return False
            self._last_check = now
            changed, seen = False, set()
            if self.root.is_dir():
                for p in sorted(self.root.rglob("*.md")):
                    rel = p.relative_to(self.root)
                    if any(part.startswith(".") for part in rel.parts):
                        continue
                    try:
                        st = p.stat()
                        if st.st_size > MAX_FILE_BYTES:
                            continue
                        doc_id = rel.with_suffix("").as_posix()
                        seen.add(doc_id)
                        sig = (st.st_mtime_ns, st.st_size)
                        old = self._docs.get(doc_id)
                        if old and old.sig == sig:
                            continue
                        self._docs[doc_id] = self._parse(p, rel, doc_id, sig)
                        changed = True
                    except OSError:
                        seen.discard(rel.with_suffix("").as_posix())
            for gone in set(self._docs) - seen:
                del self._docs[gone]
                changed = True
            if changed:
                self._rebuild()
            return changed

    def _parse(self, path: Path, rel: Path, doc_id: str, sig: tuple[int, int]) -> Doc:
        raw = path.read_text(encoding="utf-8", errors="replace")
        meta, body = _split_frontmatter(raw)
        sections = _parse_sections(body)
        h1 = next((s.heading for s in sections if s.level == 1), None)
        title = meta.get("title") or h1 or path.stem.replace("_", " ")
        sources: list[str] = []
        for s in sections:
            if s.key == "sources":
                for u in _URL_RE.findall(s.text):
                    u = u.rstrip(".,;")
                    if u not in sources:
                        sources.append(u)
        category = rel.parts[0] if len(rel.parts) > 1 else "General"
        aliases = _aliases_for(path, title, sections, meta)
        name_terms = frozenset(t for a in aliases for t in _tokens(a))
        return Doc(doc_id, category, title, aliases, sections, sources, sig, name_terms)

    def _rebuild(self) -> None:
        alias_map: dict[str, list[str]] = {}
        df: Counter = Counter()
        n = 0
        for doc in sorted(self._docs.values(), key=lambda d: d.id):
            for key in {_norm(doc.id), *(_norm(a) for a in doc.aliases)}:
                if key:
                    alias_map.setdefault(key, []).append(doc.id)
            for s in doc.visible():
                if s.key in _UNSEARCHED_SECTIONS:
                    continue
                n += 1
                df.update(s.terms.keys())
        self._alias_map, self._df, self._n_sections = alias_map, df, n

    # ----------------------------------------------------------------- lookups
    def categories(self) -> dict[str, int]:
        self.refresh()
        counts: Counter = Counter(d.category for d in self._docs.values())
        return dict(sorted(counts.items()))

    def list_docs(self, category: str | None = None) -> list[DocInfo]:
        self.refresh()
        cat = _norm(category) if category else None
        docs = [d for d in self._docs.values() if not cat or _norm(d.category) == cat]
        return [DocInfo(d.id, d.category, d.title, d.chars) for d in sorted(docs, key=lambda d: d.id)]

    def resolve(self, ref: str, category: str | None = None) -> Doc | None:
        """Find a doc by id, title, filename or alias; falls back to containment, then fuzzy match."""
        self.refresh()
        q = _norm(ref)
        if not q:
            return None
        cat = _norm(category) if category else None

        def pick(ids: list[str]) -> Doc | None:
            docs = [self._docs[i] for i in ids if i in self._docs]
            if cat:
                docs = [d for d in docs if _norm(d.category) == cat]
            return docs[0] if docs else None

        if q in self._alias_map and (d := pick(self._alias_map[q])):
            return d
        # "special week summer" -> longest known name contained in the query
        inside = sorted((k for k in self._alias_map if len(k) >= 4 and k in q), key=len, reverse=True)
        for k in inside:
            if d := pick(self._alias_map[k]):
                return d
        # "weeksp" -> unique name that starts with / contains the query
        if len(q) >= 4:
            hits = [k for k in self._alias_map if q in k]
            owners = {i for k in hits for i in self._alias_map[k]}
            if len(owners) == 1 and (d := pick(sorted(owners))):
                return d
        close = difflib.get_close_matches(q, list(self._alias_map), n=3, cutoff=0.8)
        for k in close:
            if d := pick(self._alias_map[k]):
                return d
        return None

    def suggest(self, ref: str, n: int = 5) -> list[str]:
        self.refresh()
        q = _norm(ref)
        keys = difflib.get_close_matches(q, list(self._alias_map), n=n * 2, cutoff=0.5)
        keys += [k for k in self._alias_map if q and len(q) >= 3 and q in k and k not in keys]
        out: list[str] = []
        for k in keys:
            for doc_id in self._alias_map[k]:
                if doc_id in self._docs and self._docs[doc_id].title not in out:
                    out.append(self._docs[doc_id].title)
        return out[:n]

    # -------------------------------------------------------------------- read
    def read(self, ref: str, section: str | None = None, max_chars: int = DEFAULT_READ_CHARS,
             category: str | None = None) -> ReadResult | None:
        doc = self.resolve(ref, category)
        if doc is None:
            return None
        max_chars = max(500, min(int(max_chars or DEFAULT_READ_CHARS), MAX_READ_CHARS))
        secs = doc.visible()
        outline = [f"{s.path} ({len(s.text)} chars)" for s in secs if s.level > 1 or len(secs) == 1][:40]

        def render(items: list[Section]) -> str:
            return "\n\n".join(f"{'#' * s.level} {s.heading}\n{s.text}".rstrip() for s in items)

        if section:
            idx = self._find_section(secs, section)
            if idx is None:
                return ReadResult(doc.id, doc.title, None, "", False, outline, doc.sources[:5],
                                  note=f"No section matching '{section}'. Pick one from the outline.")
            body = render(self._subtree(secs, idx))
            text, truncated = _clip(body, max_chars)
            return ReadResult(doc.id, doc.title, secs[idx].path, text, truncated, outline, doc.sources[:5])

        whole = render(secs)
        if len(whole) <= max_chars:
            return ReadResult(doc.id, doc.title, None, whole, False, outline, doc.sources[:5])
        intro = render(secs[:1])
        text, _ = _clip(intro, max_chars)
        return ReadResult(doc.id, doc.title, None, text, True, outline, doc.sources[:5],
                          note="Document is long; showing the intro only. Call again with a section from the outline.")

    @staticmethod
    def _find_section(secs: list[Section], query: str) -> int | None:
        q = _norm(query)
        if not q:
            return None
        for test in (
            lambda s: _norm(s.heading) == q or _norm(s.path) == q,
            lambda s: _norm(s.heading).startswith(q) or _norm(s.path).startswith(q),
            lambda s: q in _norm(s.path),
        ):
            for i, s in enumerate(secs):
                if test(s):
                    return i
        names = [_norm(s.heading) for s in secs]
        close = difflib.get_close_matches(q, names, n=1, cutoff=0.7)
        return names.index(close[0]) if close else None

    @staticmethod
    def _subtree(secs: list[Section], idx: int) -> list[Section]:
        out = [secs[idx]]
        for s in secs[idx + 1:]:
            if s.level <= secs[idx].level:
                break
            out.append(s)
        return out

    # ------------------------------------------------------------------ search
    def search(self, query: str, category: str | None = None, limit: int = 5) -> list[Hit]:
        self.refresh()
        terms = [t for t in dict.fromkeys(_tokens(query)) if t not in _STOPWORDS]
        if not terms:
            return []
        limit = max(1, min(int(limit or 5), 10))
        cat = _norm(category) if category else None
        n = max(self._n_sections, 1)
        idf = {t: math.log(1 + n / (1 + self._df.get(t, 0))) for t in terms}

        hits: list[Hit] = []
        for doc in self._docs.values():
            if cat and _norm(doc.category) != cat:
                continue
            name_match = [t for t in terms if t in doc.name_terms]
            doc_boost = 3.0 * sum(idf[t] for t in name_match)
            for i, s in enumerate(doc.visible()):
                if s.key in _UNSEARCHED_SECTIONS:
                    continue
                score, matched = 0.0, 0
                for t in terms:
                    tf = s.terms.get(t, 0)
                    if tf:
                        matched += 1
                        score += idf[t] * (1 + math.log(tf))
                    if t in s.head_terms:
                        score += 2.0 * idf[t]
                if score == 0 and not (i == 0 and doc_boost):
                    continue
                score *= 0.5 + 0.5 * matched / len(terms)
                score += doc_boost
                hits.append(Hit(doc.id, doc.title, s.path, _snippet(s, terms), round(score, 3)))

        hits.sort(key=lambda h: (-h.score, h.doc_id, h.section))
        return hits[:limit]


def _clip(text: str, max_chars: int) -> tuple[str, bool]:
    if len(text) <= max_chars:
        return text, False
    cut = text.rfind("\n", 0, max_chars)
    cut = cut if cut > max_chars * 0.5 else max_chars
    return text[:cut].rstrip(), True


def _snippet(section: Section, terms: list[str]) -> str:
    lines = [ln.strip() for ln in section.text.splitlines() if ln.strip() and not set(ln.strip()) <= set("|-: ")]
    best = next((ln for ln in lines if any(t in _tokens(ln) for t in terms)), lines[0] if lines else section.heading)
    return best if len(best) <= SNIPPET_CHARS else best[: SNIPPET_CHARS - 1].rstrip() + "…"


_engine: UmamusumeGameSpaceEngine | None = None
_engine_lock = threading.Lock()


def get_engine() -> UmamusumeGameSpaceEngine:
    """Process-wide engine (built on first use)."""
    global _engine
    with _engine_lock:
        if _engine is None:
            _engine = UmamusumeGameSpaceEngine()
        return _engine
