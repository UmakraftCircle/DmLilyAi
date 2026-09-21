import uuid
from collections import OrderedDict
from dataclasses import dataclass, field

from LilyAiLearning.Models.learning_models import FeedbackRecord
from LilyAiLearning.service import LearningService
from LilyAiRag.service import RagService


@dataclass
class ReplyRecord:
    user_id: str
    prompt: str
    response: str
    used_evidence: bool = False
    domains: list[str] = field(default_factory=list)


class ReplyLog:
    """Remembers recent replies so a later thumbs-up/down can be tied back to what was said."""

    def __init__(self, max_items: int = 500):
        self.max_items = max_items
        self._items: OrderedDict[str, ReplyRecord] = OrderedDict()

    def add(self, record: ReplyRecord) -> str:
        rid = uuid.uuid4().hex[:12]
        self._items[rid] = record
        while len(self._items) > self.max_items:
            self._items.popitem(last=False)
        return rid

    def get(self, rid: str) -> ReplyRecord | None:
        return self._items.get(rid)


class FeedbackHandler:
    def __init__(self, replies: ReplyLog, learning: LearningService, rag: RagService):
        self.replies, self.learning, self.rag = replies, learning, rag
        self._rated: set[tuple[str, str]] = set()

    def handle(self, user_id: str, reply_id: str, rating: int, comment: str = "") -> str:
        rec = self.replies.get(reply_id)
        if rec is None:
            return "That message is too old for me to learn from, but thanks!"
        if rec.user_id != user_id:
            return "That reply isn't yours to rate."
        if (user_id, reply_id) in self._rated:
            return "Thanks, I already have your feedback on that one."
        self._rated.add((user_id, reply_id))
        promoted = self.learning.on_feedback(
            FeedbackRecord(user_id, rating, rec.prompt, rec.response, comment, rec.used_evidence, rec.domains)
        )
        if promoted:
            self.rag.ingest_text("learned:qa", promoted)
        return "Thanks, glad it helped!" if rating > 0 else "Thanks, I'll try to do better."
