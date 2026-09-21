from LilyAiLearning.store import LearningStore


class WebLearning:
    """Learns which domains lead to good answers (thumbs up/down on replies that used web sources)."""

    def __init__(self, store: LearningStore):
        self.store = store

    def record_outcome(self, domains: list[str], rating: int) -> None:
        for d in set(domains):
            self.store.add_event("domain", d, float(rating), rating > 0)

    def preferred_domains(self, max_boost: float = 0.5) -> dict[str, float]:
        rows = self.store.db.query(
            "SELECT key, SUM(value) AS net, COUNT(*) AS n FROM learning_events WHERE kind='domain' GROUP BY key"
        )
        return {r["key"]: max(-max_boost, min(max_boost, 0.1 * r["net"])) for r in rows if r["n"] >= 2}
