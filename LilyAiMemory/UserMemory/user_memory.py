from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import UserFact
from LilyAiMemory.Storage.store import MemoryStore

MAX_FACTS_PER_USER = 200


class UserMemory:
    """Durable facts about a user ("prefers metric units", "works night shifts")."""

    def __init__(self, store: MemoryStore):
        self.db = store.db

    def add(self, user_id: str, fact: str, source: str = "user") -> UserFact | None:
        fact = " ".join(fact.split())
        if not fact:
            return None
        existing = self.db.query_one(
            "SELECT id FROM user_facts WHERE user_id=? AND lower(fact)=lower(?)", (user_id, fact)
        )
        if existing:
            return None
        ts = now_ts()
        fid = self.db.execute(
            "INSERT INTO user_facts(user_id, fact, source, created_at) VALUES (?,?,?,?)",
            (user_id, fact, source, ts),
        )
        self._trim(user_id)
        return UserFact(fid, user_id, fact, source, ts)

    def list(self, user_id: str) -> list[UserFact]:
        rows = self.db.query("SELECT * FROM user_facts WHERE user_id=? ORDER BY id", (user_id,))
        return [UserFact(**r) for r in rows]

    def remove(self, user_id: str, fact_id: int) -> bool:
        before = len(self.list(user_id))
        self.db.execute("DELETE FROM user_facts WHERE user_id=? AND id=?", (user_id, fact_id))
        return len(self.list(user_id)) < before

    def clear(self, user_id: str) -> None:
        self.db.execute("DELETE FROM user_facts WHERE user_id=?", (user_id,))

    def _trim(self, user_id: str) -> None:
        self.db.execute(
            "DELETE FROM user_facts WHERE user_id=? AND id NOT IN "
            "(SELECT id FROM user_facts WHERE user_id=? ORDER BY id DESC LIMIT ?)",
            (user_id, user_id, MAX_FACTS_PER_USER),
        )
