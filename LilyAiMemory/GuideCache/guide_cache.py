"""Saved guides, so asking for the same guide twice doesn't spend model quota twice.

Hard rule: only a finished, successful guide is ever stored. Error messages (provider failures, the
offline-provider placeholder, "couldn't build" notices) must never be cached, because a cached error
would be served back later as if it were a guide. is_cacheable() is the single gate: put() runs it on
every write, and get() runs it on every read so a bad row (e.g. one written by an older build) is
dropped instead of served.
"""
import json
from dataclasses import dataclass, field

from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Storage.store import MemoryStore

MIN_GUIDE_CHARS = 200

# Lower-cased fragments that only ever appear in error / placeholder replies.
_ERROR_MARKERS = (
    "having trouble reaching my language model",
    "(offline mode",
    "tool error:",
    "couldn't put a good answer together",
    "couldn't finish that guide",
    "couldn't find anything in the game docs",
    "language model isn't connected",
    "something went wrong on my side",
    "traceback (most recent call last)",
)


def is_cacheable(text: str, *, ok: bool, model: str = "") -> bool:
    """True only for a successful, real guide. Everything else (errors, placeholders, stubs) is refused."""
    if not ok:
        return False
    if not text or len(text.strip()) < MIN_GUIDE_CHARS:
        return False
    if (model or "").strip().lower() == "offline":
        return False
    low = text.casefold()
    return not any(marker in low for marker in _ERROR_MARKERS)


@dataclass
class CachedGuide:
    key: str
    title: str
    question: str
    content: str
    model: str
    source_ids: list[str] = field(default_factory=list)
    docs_sig: str = ""
    created_at: float = 0.0
    uses: int = 0
    stale: bool = False  # set by the caller when the source docs changed since this was built


class GuideCacheStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db

    def get(self, key: str) -> CachedGuide | None:
        row = self.db.query_one("SELECT * FROM guide_cache WHERE cache_key=?", (key,))
        if not row:
            return None
        if not is_cacheable(row["content"], ok=True, model=row["model"]):
            self.delete(key)  # never serve something that couldn't have been stored today
            return None
        try:
            source_ids = [str(s) for s in json.loads(row["source_ids"] or "[]")]
        except ValueError:
            source_ids = []
        return CachedGuide(
            key=row["cache_key"], title=row["title"], question=row["question"], content=row["content"],
            model=row["model"], source_ids=source_ids, docs_sig=row["docs_sig"],
            created_at=row["created_at"], uses=row["uses"] or 0,
        )

    def put(self, key: str, *, title: str, question: str, content: str, model: str,
            source_ids: list[str], docs_sig: str, ok: bool) -> bool:
        """Store (or replace) a guide. Returns False, and stores nothing, if it isn't cacheable."""
        if not key or not is_cacheable(content, ok=ok, model=model):
            return False
        now = now_ts()
        self.db.execute(
            "INSERT INTO guide_cache(cache_key, title, question, content, model, source_ids, docs_sig, "
            "created_at, last_used_at, uses) VALUES (?,?,?,?,?,?,?,?,?,0) "
            "ON CONFLICT(cache_key) DO UPDATE SET title=excluded.title, question=excluded.question, "
            "content=excluded.content, model=excluded.model, source_ids=excluded.source_ids, "
            "docs_sig=excluded.docs_sig, created_at=excluded.created_at, last_used_at=excluded.created_at, uses=0",
            (key, title, question, content, model or "", json.dumps(source_ids), docs_sig, now, now),
        )
        return True

    def mark_used(self, key: str) -> None:
        self.db.execute("UPDATE guide_cache SET uses = uses + 1, last_used_at = ? WHERE cache_key = ?", (now_ts(), key))

    def delete(self, key: str) -> None:
        self.db.execute("DELETE FROM guide_cache WHERE cache_key = ?", (key,))
