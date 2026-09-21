"""Facade for the Learning domain."""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiLearning.ContextLearning import ContextLearning
from LilyAiLearning.Feedback import FeedbackCollector
from LilyAiLearning.MemoryLearning import explicit_memory_request, extract_facts, name_from_message  # noqa: F401
from LilyAiLearning.Models import FeedbackRecord
from LilyAiLearning.RagLearning import promotion_text, qualifies_for_promotion
from LilyAiLearning.store import LearningStore
from LilyAiLearning.ToolLearning import ToolLearning
from LilyAiLearning.WebLearning import WebLearning


class LearningService:
    def __init__(self, db: Database):
        self.store = LearningStore(db)
        self.feedback = FeedbackCollector(self.store)
        self.tools = ToolLearning(self.store)
        self.web = WebLearning(self.store)
        self.context = ContextLearning(self.store)

    def on_feedback(self, fb: FeedbackRecord) -> str | None:
        """Record feedback and update domain scores. Returns text to add to the RAG index, if any."""
        self.feedback.record(fb)
        if fb.domains:
            self.web.record_outcome(fb.domains, 1 if fb.rating > 0 else -1)
        return promotion_text(fb) if qualifies_for_promotion(fb) else None

    def report(self) -> dict:
        return {
            "feedback": self.feedback.summary(),
            "tools": self.tools.stats(),
            "context": self.context.summary(),
            "preferred_domains": self.web.preferred_domains(),
        }
