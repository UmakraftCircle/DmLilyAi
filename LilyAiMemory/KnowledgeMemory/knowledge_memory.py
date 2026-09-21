from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import KnowledgeNote
from LilyAiMemory.Storage.store import MemoryStore


class KnowledgeMemory:
    """Shared, user-independent notes LilyAi has learned (short facts, corrections)."""

    def __init__(self, store: MemoryStore):
        self.db = store.db

    def add(self, topic: str, content: str, source: str = "") -> KnowledgeNote:
        ts = now_ts()
        nid = self.db.execute(
            "INSERT INTO knowledge_notes(topic, content, source, created_at) VALUES (?,?,?,?)",
            (topic.strip(), content.strip(), source, ts),
        )
        return KnowledgeNote(nid, topic, content, source, ts)

    def all(self) -> list[KnowledgeNote]:
        return [KnowledgeNote(**r) for r in self.db.query("SELECT * FROM knowledge_notes ORDER BY id")]
