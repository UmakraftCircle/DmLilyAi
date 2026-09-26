"""Facade for the Memory domain."""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiMemory.ConversationMemory.conversation_memory import ConversationMemory
from LilyAiMemory.DeficitState.deficit_state_store import DeficitStateStore
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.Retrieval.retriever import rank_by_overlap
from LilyAiMemory.SessionMemory.session_memory import SessionMemory
from LilyAiMemory.Storage.store import MemoryStore
from LilyAiMemory.TrainerLink.trainer_link import TrainerLinkStore
from LilyAiMemory.UserMemory.user_memory import UserMemory


class MemoryService:
    def __init__(self, db: Database):
        self.store = MemoryStore(db)
        self.user = UserMemory(self.store)
        self.conversation = ConversationMemory(self.store)
        self.session = SessionMemory()
        self.trainer_link = TrainerLinkStore(self.store)
        self.fan_gain = FanSnapshotStore(self.store)
        self.deficit_state = DeficitStateStore(self.store)

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

    def forget_user(self, user_id: str) -> None:
        self.user.clear(user_id)
        self.conversation.clear(user_id)
        self.session.end(user_id)
