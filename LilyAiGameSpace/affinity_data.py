"""Umamusume affinity (compatibility) data: load, look up characters by name, build small slices.

Source: uma.moe's public `affinity.json`, generated from the game's own master tables
(succession_relation + succession_relation_member). Layout, verified against the real file:
    chars : the character ids covered (74 on Global at v1.35.2), sorted
    aff2  : n*n pair ratings,   aff2[i*n + j]            (symmetric, 0 on the diagonal)
    aff3  : n*n*n triple ratings, aff3[(i*n + j)*n + k]  (symmetric in all three, 0 if two ids repeat)
A triple value is the sum of the ratings of the groups that contain all three characters, so it is never
larger than the smallest of the three pair ratings.

Where the file is looked for, in order:
    1. $AFFINITY_DATA_PATH
    2. LilyAiGameSpace/affinity_data/affinity.json   (commit it to the repo: simplest and works offline)
    3. $LILYAI_DATA_DIR/affinity.json                (a downloaded copy)
    4. download https://uma.moe/resources/current/affinity.json.gz into $LILYAI_DATA_DIR (needs outbound access;
       uma.moe may refuse scripts, in which case do 2)
"""
from __future__ import annotations

import difflib
import gzip
import json
import os
import re
import threading
from dataclasses import dataclass, field
from pathlib import Path

from LilyAiCore.Logging.logger import get_logger

log = get_logger("gamespace.affinity")

PKG_DIR = Path(__file__).resolve().parent / "affinity_data"
DATA_URL = "https://uma.moe/resources/current/affinity.json.gz"
NAMES_FILE = "affinity_names.json"


class AffinityError(Exception):
    """A user-presentable problem (unknown character, missing data file...)."""


def _norm(s: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", str(s).casefold())


@dataclass
class AffinityData:
    chars: list[int]
    aff2: list[int]
    aff3: list[int]
    names: dict[int, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        n = len(self.chars)
        if n < 3 or len(self.aff2) != n * n or len(self.aff3) != n ** 3:
            raise AffinityError(
                f"The affinity file looks wrong: {n} characters but {len(self.aff2)} pair values and {len(self.aff3)} triple values "
                f"(expected {n * n} and {n ** 3}).")
        self.n = n
        self.index = {c: i for i, c in enumerate(self.chars)}

    # ---- lookups
    def label(self, cid: int) -> str:
        return self.names.get(cid) or str(cid)

    def pair(self, a: int, b: int) -> int:
        return self.aff2[self.index[a] * self.n + self.index[b]]

    def triple(self, a: int, b: int, c: int) -> int:
        return self.aff3[(self.index[a] * self.n + self.index[b]) * self.n + self.index[c]]

    def resolve(self, ref) -> int:
        """Character id from an id or a name (case/punctuation-insensitive, unique prefixes/fragments allowed)."""
        text = str(ref).strip()
        if not text:
            raise AffinityError("a character name is empty")
        if text.isdigit() and int(text) in self.index:
            return int(text)
        q = _norm(text)
        by_norm = {c: _norm(self.label(c)) for c in self.chars}
        for test in (lambda v: v == q, lambda v: v.startswith(q), lambda v: q in v):
            hits = [c for c, v in by_norm.items() if test(v)]
            if len(hits) == 1:
                return hits[0]
            if len(hits) > 1:
                raise AffinityError(f"{text!r} matches several characters: {', '.join(self.label(c) for c in hits[:6])}. Be more specific.")
        close = difflib.get_close_matches(text, [self.label(c) for c in self.chars], n=3, cutoff=0.5)
        hint = f" Did you mean: {', '.join(close)}?" if close else ""
        raise AffinityError(f"{text!r} isn't in the affinity data (it covers 74 characters, newer ones may be missing).{hint}")

    def subset(self, ids: list[int]) -> dict:
        """The same file format restricted to `ids`, small enough to hand to a sandbox for a single calculation."""
        ids = sorted(set(ids))
        n = len(ids)
        return {
            "chars": ids,
            "aff2": [self.pair(a, b) for a in ids for b in ids],
            "aff3": [self.triple(a, b, c) for a in ids for b in ids for c in ids],
        }

    def to_json(self) -> str:
        return json.dumps({"chars": self.chars, "aff2": self.aff2, "aff3": self.aff3}, separators=(",", ":"))


# ------------------------------------------------------------------ loading
_lock = threading.Lock()
_cached: tuple[tuple[str, float], AffinityData] | None = None


def _candidates() -> list[Path]:
    out: list[Path] = []
    if os.getenv("AFFINITY_DATA_PATH"):
        out.append(Path(os.environ["AFFINITY_DATA_PATH"]))
    out.append(PKG_DIR / "affinity.json")
    out += sorted(PKG_DIR.glob("affinity*.json")) if PKG_DIR.exists() else []
    data_dir = Path(os.getenv("LILYAI_DATA_DIR", "./data"))
    out.append(data_dir / "affinity.json")
    seen, unique = set(), []
    for p in out:
        if p.name != NAMES_FILE and p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def _read_names() -> dict[int, str]:
    path = PKG_DIR / NAMES_FILE
    try:
        return {int(k): str(v) for k, v in json.loads(path.read_text(encoding="utf-8")).items()}
    except (OSError, ValueError):
        log.warning("affinity names file missing or unreadable at %s", path)
        return {}


def _parse(raw: bytes) -> dict:
    try:
        return json.loads(raw)
    except ValueError:
        return json.loads(gzip.decompress(raw))      # a still-compressed download


def _download(dest: Path) -> None:
    try:
        import httpx
        resp = httpx.get(DATA_URL, timeout=30, follow_redirects=True, headers={"User-Agent": "LilyAi/1.0 (game docs bot)"})
        resp.raise_for_status()
        data = _parse(resp.content)
    except Exception as e:
        log.warning("affinity download failed: %s: %s", type(e).__name__, str(e)[:200])
        raise AffinityError("The affinity data isn't installed and couldn't be downloaded. Add affinity.json to LilyAiGameSpace/affinity_data/ in the repo.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    log.info("downloaded affinity data to %s", dest)


def load() -> AffinityData:
    global _cached
    with _lock:
        path = next((p for p in _candidates() if p.is_file()), None)
        if path is None:
            path = Path(os.getenv("LILYAI_DATA_DIR", "./data")) / "affinity.json"
            _download(path)
        key = (str(path), path.stat().st_mtime)
        if _cached and _cached[0] == key:
            return _cached[1]
        try:
            raw = _parse(path.read_bytes())
            data = AffinityData([int(c) for c in raw["chars"]], [int(x) for x in raw["aff2"]], [int(x) for x in raw["aff3"]], _read_names())
        except AffinityError:
            raise
        except Exception as e:
            raise AffinityError(f"Couldn't read the affinity file {path.name}: {type(e).__name__}")
        _cached = (key, data)
        return data
