from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import ConversationTurn
from LilyAiMemory.Storage.store import MemoryStore


class ConversationMemory:
    """Rolling transcript per user (DM channel)."""

    def __init__(self, store: MemoryStore):
        self.db = store.db

    def append(self, user_id: str, role: str, content: str) -> None:
        self.db.execute(
            "INSERT INTO conversation_turns(user_id, role, content, created_at) VALUES (?,?,?,?)",
            (user_id, role, content, now_ts()),
        )

    def recent(self, user_id: str, limit: int = 12) -> list[ConversationTurn]:
        rows = self.db.query(
            "SELECT * FROM conversation_turns WHERE user_id=? ORDER BY id DESC LIMIT ?", (user_id, limit * 2)
        )
        return [ConversationTurn(**r) for r in reversed(rows)]

    def clear(self, user_id: str) -> None:
        self.db.execute("DELETE FROM conversation_turns WHERE user_id=?", (user_id,))

    def count(self, user_id: str) -> int:
        row = self.db.query_one("SELECT COUNT(*) AS n FROM conversation_turns WHERE user_id=?", (user_id,))
        return int(row["n"]) if row else 0
