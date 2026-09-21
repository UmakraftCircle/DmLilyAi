from LilyAiLearning.store import LearningStore


class ContextLearning:
    def __init__(self, store: LearningStore):
        self.store = store

    def record(self, token_estimate: int, dropped_history: int) -> None:
        self.store.add_event("context_tokens", "prompt", float(token_estimate))
        if dropped_history:
            self.store.add_event("context_dropped", "history", float(dropped_history))

    def summary(self) -> dict:
        t = self.store.db.query_one(
            "SELECT COUNT(*) AS n, ROUND(AVG(value),0) AS avg_tokens, MAX(value) AS max_tokens "
            "FROM learning_events WHERE kind='context_tokens'"
        ) or {}
        d = self.store.db.query_one(
            "SELECT COUNT(*) AS trims FROM learning_events WHERE kind='context_dropped'"
        ) or {}
        return {**t, **d}
