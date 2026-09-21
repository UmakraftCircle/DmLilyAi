from LilyAiLearning.store import LearningStore


class ToolLearning:
    def __init__(self, store: LearningStore):
        self.store = store

    def record(self, tool: str, ok: bool, duration_ms: float) -> None:
        self.store.add_event("tool", tool, duration_ms, ok)

    def stats(self) -> list[dict]:
        return self.store.db.query(
            "SELECT key AS tool, COUNT(*) AS calls, SUM(ok=0) AS failures, ROUND(AVG(value),1) AS avg_ms "
            "FROM learning_events WHERE kind='tool' GROUP BY key ORDER BY calls DESC"
        )
