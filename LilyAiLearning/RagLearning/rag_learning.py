"""Knowledge learning: promote well-received, evidence-backed answers into the RAG index."""
from LilyAiLearning.Models.learning_models import FeedbackRecord


def qualifies_for_promotion(fb: FeedbackRecord) -> bool:
    return fb.rating > 0 and fb.used_evidence and 40 <= len(fb.response) <= 2000 and len(fb.prompt) >= 8


def promotion_text(fb: FeedbackRecord) -> str:
    return f"Q: {fb.prompt.strip()}\n\nA: {fb.response.strip()}"
