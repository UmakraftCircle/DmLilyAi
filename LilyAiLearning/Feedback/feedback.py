from LilyAiLearning.Models.learning_models import FeedbackRecord
from LilyAiLearning.store import LearningStore


class FeedbackCollector:
    def __init__(self, store: LearningStore):
        self.store = store

    def record(self, fb: FeedbackRecord) -> int:
        return self.store.add_feedback(
            fb.user_id, 1 if fb.rating > 0 else -1, fb.prompt, fb.response, fb.comment, fb.used_evidence, fb.domains
        )

    def summary(self) -> dict:
        row = self.store.db.query_one(
            "SELECT COUNT(*) AS total, COALESCE(SUM(rating>0),0) AS up, COALESCE(SUM(rating<0),0) AS down FROM feedback"
        ) or {"total": 0, "up": 0, "down": 0}
        recent = self.store.db.query(
            "SELECT rating, prompt, response, comment, created_at FROM feedback ORDER BY id DESC LIMIT 10"
        )
        return {**row, "recent": recent}
