"""Stable keys and name resolution for Umamusume support cards, characters and aptitudes.

Reads the same docs folder as the docs engine (LilyAiGameSpace/Umamusume):

- Support cards come from the generated tables in 'Support Cards/{SSR,SR,R}.md'. A card's id is
  '<rarity>:<type>:<slug of "[title] uma">', e.g. 'sr:speed:cozy-cute-memory-curren-chan'. The docs
  hold the game data; a user's database stores only these ids, so a patch never leaves stored data stale.
- Characters come from the file names in 'Character/' (one doc per uma): 'Oguri_Cap' -> 'Oguri Cap'.

Everything here is read-only and never raises on a missing or odd docs folder (it just finds nothing).
"""
from __future__ import annotations

import re
import threading
import unicodedata
from dataclasses import dataclass
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent / "Umamusume"
CARD_DIR = "Support Cards"
RARITIES = ("SSR", "SR", "R")
TYPE_ORDER = ("Speed", "Stamina", "Power", "Guts", "Wit", "Friend", "Group")
STATS = ("speed", "stamina", "power", "guts", "wit")

# --------------------------------------------------------------------------- text helpers


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKC", str(text)).lower()


def tokens(text: str) -> list[str]:
    return re.findall(r"\w+", _fold(text))


def compact(text: str) -> str:
    return re.sub(r"[\W_]+", "", _fold(text))


def _slug(text: str) -> str:
    return re.sub(r"[\W_]+", "-", _fold(text)).strip("-")


def _tok_match(t: str, toks: tuple[str, ...] | list[str]) -> bool:
    return any(x == t or (len(t) >= 3 and x.startswith(t)) for x in toks)


# --------------------------------------------------------------------------- data classes


@dataclass(frozen=True)
class Card:
    card_id: str
    rarity: str  # SSR / SR / R
    type: str  # Speed, Stamina, Power, Guts, Wit, Friend, Group
    title: str  # e.g. "Cozy Cute Memory ♪"
    uma: str  # e.g. "Curren Chan"
    release: str = ""  # the docs' "EN Release" column ("JP only", "EN" or a date) - informational

    @property
    def label(self) -> str:
        return f"{self.rarity} {self.type} [{self.title}] {self.uma}"

    @property
    def uma_tokens(self) -> tuple[str, ...]:
        return tuple(tokens(self.uma))

    @property
    def title_tokens(self) -> tuple[str, ...]:
        return tuple(tokens(self.title))


@dataclass(frozen=True)
class Character:
    uma_id: str  # file stem, e.g. "Oguri_Cap" (also the docs id 'Character/Oguri_Cap')
    name: str  # "Oguri Cap"

    @property
    def tokens(self) -> tuple[str, ...]:
        return tuple(tokens(self.name))

    @property
    def compact(self) -> str:
        return compact(self.name)


# --------------------------------------------------------------------------- loading

_ROW = re.compile(r"^\|\s*\[(?P<title>.*?)\]\s*(?P<uma>[^|]*?)\s*\|")


def _parse_cards(path: Path, rarity: str) -> list[Card]:
    cards: list[Card] = []
    seen: dict[str, int] = {}
    ctype = ""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return cards
    for line in lines:
        if line.startswith("## "):
            ctype = line[3:].strip()
            continue
        if not ctype or not line.startswith("|"):
            continue
        m = _ROW.match(line)
        if not m:
            continue
        title, uma = m.group("title").strip(), m.group("uma").strip()
        if not uma:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        base = f"{rarity.lower()}:{ctype.lower()}:{_slug(title + ' ' + uma)}"
        n = seen.get(base, 0) + 1
        seen[base] = n
        cards.append(Card(base if n == 1 else f"{base}-{n}", rarity, ctype, title, uma, cells[-1] if cells else ""))
    return cards


class _Catalog:
    """Lazily parsed, refreshed when the card tables or the character folder change."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._sig: tuple | None = None
        self._cards: list[Card] = []
        self._chars: list[Character] = []

    @staticmethod
    def _signature() -> tuple:
        parts: list = []
        for r in RARITIES:
            try:
                st = (DOCS_ROOT / CARD_DIR / f"{r}.md").stat()
                parts.append((st.st_mtime_ns, st.st_size))
            except OSError:
                parts.append(None)
        try:
            parts.append(sum(1 for _ in (DOCS_ROOT / "Character").glob("*.md")))
        except OSError:
            parts.append(None)
        return tuple(parts)

    def load(self) -> tuple[list[Card], list[Character]]:
        sig = self._signature()
        with self._lock:
            if sig != self._sig:
                cards: list[Card] = []
                for r in RARITIES:
                    cards.extend(_parse_cards(DOCS_ROOT / CARD_DIR / f"{r}.md", r))
                try:
                    chars = [Character(p.stem, p.stem.replace("_", " ")) for p in sorted((DOCS_ROOT / "Character").glob("*.md"))]
                except OSError:
                    chars = []
                self._cards, self._chars, self._sig = cards, chars, sig
            return self._cards, self._chars


_CATALOG = _Catalog()


def all_cards() -> list[Card]:
    return _CATALOG.load()[0]


def all_characters() -> list[Character]:
    return _CATALOG.load()[1]


def card_by_id(card_id: str) -> Card | None:
    return next((c for c in all_cards() if c.card_id == card_id), None)


def character_by_id(uma_id: str) -> Character | None:
    return next((c for c in all_characters() if c.uma_id == uma_id), None)


def uma_name(uma_id: str) -> str:
    c = character_by_id(uma_id)
    return c.name if c else uma_id.replace("_", " ")


# --------------------------------------------------------------------------- resolving names

_TYPE_WORDS = {
    "speed": "Speed", "spd": "Speed",
    "stamina": "Stamina", "stam": "Stamina", "sta": "Stamina",
    "power": "Power", "pow": "Power", "pwr": "Power",
    "guts": "Guts",
    "wit": "Wit", "wiz": "Wit",
    "friend": "Friend", "pal": "Friend",
    "group": "Group",
}


def norm_type(value: str | None) -> str | None:
    if not value:
        return None
    return _TYPE_WORDS.get(_fold(value).strip())


def _type_rank(t: str) -> int:
    return TYPE_ORDER.index(t) if t in TYPE_ORDER else len(TYPE_ORDER)


def resolve_card(text: str, rarity: str | None = None, ctype: str | None = None) -> list[Card]:
    """Cards matching free text like 'kitasan ssr speed' (best match first; empty if nothing fits).

    Rarity and type words in the text act as filters; every remaining word must appear in the
    character name or the card title. Callers must treat more than one result as ambiguous.
    """
    cards = all_cards()
    rar = rarity.upper() if rarity else None
    typ = norm_type(ctype)
    work = str(text)
    if re.search(r"(?<!\w)R(?!\w)", work):  # a standalone capital R means rarity R; lowercase 'r' is never a filter
        rar = rar or "R"
        work = re.sub(r"(?<!\w)R(?!\w)", " ", work)
    rest: list[str] = []
    for t in tokens(work):
        if t in ("ssr", "sr"):
            rar = rar or t.upper()
        elif t in _TYPE_WORDS and typ is None:
            typ = _TYPE_WORDS[t]
        else:
            rest.append(t)
    if not rest:
        return []
    scored: list[tuple[int, Card]] = []
    for c in cards:
        if (rar and c.rarity != rar) or (typ and c.type != typ):
            continue
        ut, tt = c.uma_tokens, c.title_tokens
        score = 0
        for t in rest:
            if _tok_match(t, ut):
                score += 2
            elif _tok_match(t, tt):
                score += 1
            else:
                score = -1
                break
        if score >= 0:
            scored.append((score, c))
    if not scored:  # fall back to punctuation-insensitive matching, e.g. "tm opera o" vs "T.M. Opera O"
        qc = "".join(rest)
        if len(qc) >= 4:
            scored = [(1, c) for c in cards
                      if (not rar or c.rarity == rar) and (not typ or c.type == typ) and qc in compact(c.uma)]
    scored.sort(key=lambda sc: (-sc[0], RARITIES.index(sc[1].rarity), _type_rank(sc[1].type), sc[1].label))
    return [c for _, c in scored]


def resolve_uma(text: str) -> list[Character]:
    """Characters matching free text ('oguri', 'K.S.Miracle'); an exact name wins outright."""
    chars = all_characters()
    qc = compact(text)
    if not qc:
        return []
    exact = [c for c in chars if c.compact == qc]
    if len(exact) == 1:
        return exact
    qt = tokens(text)
    hits = [c for c in chars if all(_tok_match(t, c.tokens) for t in qt)]
    if not hits and len(qc) >= 4:
        hits = [c for c in chars if qc in c.compact]
    return sorted(hits, key=lambda c: (len(c.name), c.name))


# --------------------------------------------------------------------------- limit break

_LB_NUM = (
    re.compile(r"\b(?:lb|limit\s*break)\s*[:=]?\s*([0-4])\b", re.I),
    re.compile(r"\b([0-4])\s*(?:lb|limit\s*breaks?)\b", re.I),
)
_LB_MAX = re.compile(r"\b(?:mlb|max(?:ed)?(?:\s*(?:lb|limit\s*breaks?))?|fully\s+(?:limit\s*)?broken)\b", re.I)
_LB_ZERO = re.compile(r"\b(?:unbroken|no\s*lb|zero\s*lb)\b", re.I)


def _squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" ,;:-")


def split_limit_break(text: str) -> tuple[str, int | None]:
    """('kitasan ssr speed mlb') -> ('kitasan ssr speed', 4). Returns (text, None) if no limit break is stated."""
    for pat in _LB_NUM:
        m = pat.search(text)
        if m:
            return _squash(text[:m.start()] + " " + text[m.end():]), int(m.group(1))
    for pat, value in ((_LB_MAX, 4), (_LB_ZERO, 0)):
        m = pat.search(text)
        if m:
            return _squash(text[:m.start()] + " " + text[m.end():]), value
    return _squash(text), None


def lb_label(n: int | None) -> str:
    return "?" if n is None else ("MLB" if n >= 4 else f"LB{n}")


# --------------------------------------------------------------------------- aptitudes / scenarios

_DIST = {"sprint": "sprint", "short": "sprint", "mile": "mile", "medium": "medium", "med": "medium",
         "middle": "medium", "long": "long"}
_TRACK = {"turf": "turf", "grass": "turf", "dirt": "dirt"}
_STYLE = {"front runner": "front runner", "front": "front runner", "frontrunner": "front runner",
          "pace chaser": "pace chaser", "pace": "pace chaser", "pacechaser": "pace chaser",
          "late surger": "late surger", "late": "late surger", "latesurger": "late surger",
          "end closer": "end closer", "end": "end closer", "closer": "end closer", "endcloser": "end closer"}
_SCEN = {"ura": "ura finale", "ura finale": "ura finale", "finale": "ura finale", "unity cup": "unity cup",
         "unity": "unity cup", "trackblazer": "trackblazer", "grand concert": "grand concert",
         "grand live": "grand concert"}
SCENARIO_SPIRIT = {"ura finale": "racing spirit", "unity cup": "burning spirit"}
_STAT_WORDS = {"speed": "speed", "spd": "speed", "stamina": "stamina", "stam": "stamina", "sta": "stamina",
               "power": "power", "pow": "power", "pwr": "power", "guts": "guts", "wit": "wit", "wiz": "wit",
               "wisdom": "wit"}


def norm_aptitude(kind: str, value: object) -> str | None:
    table = {"distance": _DIST, "track": _TRACK, "style": _STYLE}.get(kind)
    return table.get(" ".join(tokens(str(value)))) if table else None


def norm_scenario(value: object) -> str | None:
    key = " ".join(tokens(str(value)))
    if not key:
        return None
    return _SCEN.get(key, key)


def norm_stat(value: object) -> str | None:
    return _STAT_WORDS.get(" ".join(tokens(str(value))))


def parse_spirit(item: object) -> dict | None:
    """'Racing Spirit Speed+' / {'name': 'burning spirit', 'stat': 'power', 'plus': true} -> normalised dict."""
    if isinstance(item, dict):
        text = f"{item.get('name', '')} {item.get('stat', '') or ''}"
        plus = bool(item.get("plus")) or "+" in text
    else:
        text, plus = str(item), "+" in str(item)
    toks = tokens(text)
    if "burning" in toks or "ignited" in toks:
        name = "burning spirit"
    elif "racing" in toks:
        name = "racing spirit"
    else:
        return None
    stat = next((_STAT_WORDS[t] for t in toks if t in _STAT_WORDS), None)
    if stat is None and "mood" in toks:
        stat = "mood"
    return {"name": name, "stat": stat, "plus": plus or "plus" in toks}
