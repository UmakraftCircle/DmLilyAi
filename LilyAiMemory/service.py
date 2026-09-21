"""Facade for the Memory domain."""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiMemory.ConversationMemory.conversation_memory import ConversationMemory
from LilyAiMemory.KnowledgeMemory.knowledge_memory import KnowledgeMemory
from LilyAiMemory.Retrieval.retriever import rank_by_overlap
from LilyAiMemory.SessionMemory.session_memory import SessionMemory
from LilyAiMemory.Storage.store import MemoryStore
from LilyAiMemory.UserMemory.user_memory import UserMemory


class MemoryService:
    def __init__(self, db: Database):
        self.store = MemoryStore(db)
        self.user = UserMemory(self.store)
        self.conversation = ConversationMemory(self.store)
        self.session = SessionMemory()
        self.knowledge = KnowledgeMemory(self.store)

    def relevant_user_facts(self, user_id: str, query: str, limit: int = 6) -> list[str]:
        """Most relevant facts for this message; falls back to the newest facts so basics aren't lost."""
        facts = [f.fact for f in self.user.list(user_id)]
        hits = rank_by_overlap(query, facts, limit=limit)
        if len(hits) < 3:
            for f in reversed(facts):
                if f not in hits:
                    hits.append(f)
                if len(hits) >= 3:
                    break
        return hits

    def relevant_notes(self, query: str, limit: int = 3) -> list[str]:
        notes = [f"{n.topic}: {n.content}" for n in self.knowledge.all()]
        return rank_by_overlap(query, notes, limit=limit, min_score=0.15)

    def forget_user(self, user_id: str) -> None:
        self.user.clear(user_id)
        self.conversation.clear(user_id)
        self.session.end(user_id)
