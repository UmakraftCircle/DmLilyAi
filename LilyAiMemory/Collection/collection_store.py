"""What a user owns in Umamusume: support cards (with limit break), trainees (with potential) and
inheritance parents.

Only ownership and state live here. Card effects, trainee stats and skill conditions stay in the docs
(LilyAiGameSpace), referenced by stable ids from LilyAiGameSpace/UmamusumeCatalog.py, so a game patch
never leaves stored data out of date. Every row is keyed by Discord user id.
"""
import json
from typing import Any

from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Storage.store import MemoryStore

COLLECTION_SCHEMA = """
CREATE TABLE IF NOT EXISTS user_support_cards (
    user_id TEXT NOT NULL,
    card_id TEXT NOT NULL,
    limit_break INTEGER NOT NULL DEFAULT 0,
    updated_at REAL NOT NULL,
    PRIMARY KEY (user_id, card_id)
);

CREATE TABLE IF NOT EXISTS user_trainees (
    user_id TEXT NOT NULL,
    uma_id TEXT NOT NULL,
    version TEXT NOT NULL DEFAULT '',
    potential_level INTEGER,
    updated_at REAL NOT NULL,
    PRIMARY KEY (user_id, uma_id, version)
);

CREATE TABLE IF NOT EXISTS user_parents (
    user_id TEXT NOT NULL,
    parent_id INTEGER NOT NULL,
    uma_id TEXT NOT NULL,
    nickname TEXT,
    scenario TEXT,
    white_count INTEGER,
    scenario_white TEXT NOT NULL DEFAULT '[]',
    pink TEXT NOT NULL DEFAULT '[]',
    blue TEXT NOT NULL DEFAULT '{}',
    unique_skill TEXT,
    key_whites TEXT NOT NULL DEFAULT '[]',
    grandparents TEXT NOT NULL DEFAULT '[]',
    updated_at REAL NOT NULL,
    PRIMARY KEY (user_id, parent_id)
);
CREATE INDEX IF NOT EXISTS idx_user_parents_uma ON user_parents(user_id, uma_id);
"""

_PARENT_JSON = {"scenario_white": [], "pink": [], "blue": {}, "key_whites": [], "grandparents": []}
_PARENT_PLAIN = ("nickname", "scenario", "white_count", "unique_skill")
_PARENT_COLS = ("uma_id", *_PARENT_PLAIN, *_PARENT_JSON)
_SCOPES = {"cards": "user_support_cards", "trainees": "user_trainees", "parents": "user_parents"}


def _decode_parent(row: dict[str, Any]) -> dict[str, Any]:
    out = dict(row)
    for col, default in _PARENT_JSON.items():
        try:
            out[col] = json.loads(out.get(col) or "")
        except (TypeError, ValueError):
            out[col] = type(default)()
    return out


def _encode(col: str, value: Any) -> Any:
    if col in _PARENT_JSON:
        return json.dumps(value if value is not None else _PARENT_JSON[col], ensure_ascii=False)
    return value


class CollectionStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db
        self.db.executescript(COLLECTION_SCHEMA)

    # ------------------------------------------------------------------ support cards

    def get_card(self, user_id: str, card_id: str) -> int | None:
        row = self.db.query_one(
            "SELECT limit_break FROM user_support_cards WHERE user_id=? AND card_id=?", (user_id, card_id))
        return None if row is None else int(row["limit_break"])

    def set_card(self, user_id: str, card_id: str, limit_break: int) -> int | None:
        """Absolute write (never '+1'). Returns the previous limit break, or None if the card was new."""
        prev = self.get_card(user_id, card_id)
        self.db.execute(
            "INSERT INTO user_support_cards(user_id, card_id, limit_break, updated_at) VALUES (?,?,?,?) "
            "ON CONFLICT(user_id, card_id) DO UPDATE SET limit_break=excluded.limit_break, updated_at=excluded.updated_at",
            (user_id, card_id, int(limit_break), now_ts()),
        )
        return prev

    def remove_card(self, user_id: str, card_id: str) -> int | None:
        prev = self.get_card(user_id, card_id)
        if prev is not None:
            self.db.execute("DELETE FROM user_support_cards WHERE user_id=? AND card_id=?", (user_id, card_id))
        return prev

    def list_cards(self, user_id: str) -> list[dict[str, Any]]:
        return self.db.query(
            "SELECT card_id, limit_break, updated_at FROM user_support_cards WHERE user_id=? ORDER BY card_id", (user_id,))

    # ------------------------------------------------------------------ trainees

    def get_trainee(self, user_id: str, uma_id: str, version: str = "") -> dict[str, Any] | None:
        return self.db.query_one(
            "SELECT uma_id, version, potential_level, updated_at FROM user_trainees "
            "WHERE user_id=? AND uma_id=? AND version=?", (user_id, uma_id, version))

    def set_trainee(self, user_id: str, uma_id: str, version: str = "", potential: int | None = None) -> dict[str, Any] | None:
        """Create or update. A None potential keeps the stored one. Returns the previous row (or None)."""
        prev = self.get_trainee(user_id, uma_id, version)
        self.db.execute(
            "INSERT INTO user_trainees(user_id, uma_id, version, potential_level, updated_at) VALUES (?,?,?,?,?) "
            "ON CONFLICT(user_id, uma_id, version) DO UPDATE SET "
            "potential_level=COALESCE(excluded.potential_level, user_trainees.potential_level), "
            "updated_at=excluded.updated_at",
            (user_id, uma_id, version, potential, now_ts()),
        )
        return prev

    def restore_trainee(self, user_id: str, uma_id: str, version: str, row: dict[str, Any] | None) -> None:
        """Put a trainee back exactly as it was (row=None means it did not exist)."""
        if row is None:
            self.remove_trainee(user_id, uma_id, version)
            return
        self.db.execute(
            "INSERT OR REPLACE INTO user_trainees(user_id, uma_id, version, potential_level, updated_at) VALUES (?,?,?,?,?)",
            (user_id, uma_id, version, row.get("potential_level"), now_ts()),
        )

    def remove_trainee(self, user_id: str, uma_id: str, version: str = "") -> dict[str, Any] | None:
        prev = self.get_trainee(user_id, uma_id, version)
        if prev is not None:
            self.db.execute("DELETE FROM user_trainees WHERE user_id=? AND uma_id=? AND version=?",
                            (user_id, uma_id, version))
        return prev

    def list_trainees(self, user_id: str) -> list[dict[str, Any]]:
        return self.db.query(
            "SELECT uma_id, version, potential_level, updated_at FROM user_trainees "
            "WHERE user_id=? ORDER BY uma_id, version", (user_id,))

    # ------------------------------------------------------------------ inheritance parents

    def add_parent(self, user_id: str, data: dict[str, Any]) -> int:
        """Insert a parent and return its per-user number (#1, #2, ...)."""
        values = [_encode(c, data.get(c)) for c in _PARENT_COLS]
        rowid = self.db.execute(
            "INSERT INTO user_parents(user_id, parent_id, uma_id, nickname, scenario, white_count, unique_skill, "
            "scenario_white, pink, blue, key_whites, grandparents, updated_at) "
            "SELECT ?, COALESCE(MAX(parent_id), 0) + 1, ?,?,?,?,?,?,?,?,?,?,? FROM user_parents WHERE user_id=?",
            (user_id, *values, now_ts(), user_id),
        )
        row = self.db.query_one("SELECT parent_id FROM user_parents WHERE rowid=?", (rowid,))
        return int(row["parent_id"])

    def get_parent(self, user_id: str, parent_id: int) -> dict[str, Any] | None:
        row = self.db.query_one("SELECT * FROM user_parents WHERE user_id=? AND parent_id=?", (user_id, parent_id))
        return _decode_parent(row) if row else None

    def update_parent(self, user_id: str, parent_id: int, fields: dict[str, Any]) -> None:
        cols = [c for c in fields if c in _PARENT_COLS and c != "uma_id"]
        if not cols:
            return
        sets = ", ".join(f"{c}=?" for c in cols) + ", updated_at=?"
        self.db.execute(
            f"UPDATE user_parents SET {sets} WHERE user_id=? AND parent_id=?",
            (*[_encode(c, fields[c]) for c in cols], now_ts(), user_id, parent_id),
        )

    def replace_parent(self, user_id: str, row: dict[str, Any]) -> None:
        """Re-insert a parent under its old number (used to undo a delete or an edit)."""
        values = [_encode(c, row.get(c)) for c in _PARENT_COLS]
        self.db.execute(
            "INSERT OR REPLACE INTO user_parents(user_id, parent_id, uma_id, nickname, scenario, white_count, "
            "unique_skill, scenario_white, pink, blue, key_whites, grandparents, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (user_id, int(row["parent_id"]), *values, now_ts()),
        )

    def delete_parent(self, user_id: str, parent_id: int) -> dict[str, Any] | None:
        prev = self.get_parent(user_id, parent_id)
        if prev is not None:
            self.db.execute("DELETE FROM user_parents WHERE user_id=? AND parent_id=?", (user_id, parent_id))
        return prev

    def list_parents(self, user_id: str, uma_id: str | None = None) -> list[dict[str, Any]]:
        if uma_id:
            rows = self.db.query("SELECT * FROM user_parents WHERE user_id=? AND uma_id=? ORDER BY parent_id", (user_id, uma_id))
        else:
            rows = self.db.query("SELECT * FROM user_parents WHERE user_id=? ORDER BY parent_id", (user_id,))
        return [_decode_parent(r) for r in rows]

    # ------------------------------------------------------------------ whole collection

    def counts(self, user_id: str) -> dict[str, int]:
        return {
            scope: int(self.db.query_one(f"SELECT COUNT(*) AS n FROM {table} WHERE user_id=?", (user_id,))["n"])
            for scope, table in _SCOPES.items()
        }

    def last_updated(self, user_id: str) -> float | None:
        row = self.db.query_one(
            "SELECT MAX(t) AS latest FROM ("
            "SELECT MAX(updated_at) AS t FROM user_support_cards WHERE user_id=? UNION ALL "
            "SELECT MAX(updated_at) FROM user_trainees WHERE user_id=? UNION ALL "
            "SELECT MAX(updated_at) FROM user_parents WHERE user_id=?)",
            (user_id, user_id, user_id),
        )
        return row["latest"] if row and row["latest"] is not None else None

    def clear(self, user_id: str, scope: str = "all") -> dict[str, int]:
        """Delete a user's cards / trainees / parents (or all). Returns how many rows were removed per kind."""
        scopes = list(_SCOPES) if scope == "all" else [scope]
        if any(s not in _SCOPES for s in scopes):
            raise ValueError(f"unknown scope {scope!r}")
        removed = self.counts(user_id)
        for s in scopes:
            self.db.execute(f"DELETE FROM {_SCOPES[s]} WHERE user_id=?", (user_id,))
        return {s: removed[s] for s in scopes}
