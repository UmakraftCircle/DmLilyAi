"""Decide what is worth remembering about a user, safely."""
import json
import re

from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider

log = get_logger("learning.memory")

_EXPLICIT = re.compile(r"^\s*(?:please\s+)?(?:remember|note|keep in mind)(?:\s+that)?[:,]?\s+(.{3,300})$", re.I | re.S)
_NAME = re.compile(r"\b(?:my name is|call me)\s+([A-Za-z][\w'\- ]{0,30})", re.I)
_SECRET = re.compile(
    r"(api[_-]?key|password|passwd|secret|token|bearer|\b\d{13,19}\b|\b\d{3}-\d{2}-\d{4}\b|sk-[A-Za-z0-9]{10,}|gsk_[A-Za-z0-9]{10,})",
    re.I,
)

EXTRACT_PROMPT = """Extract durable personal facts or preferences the USER stated about themselves in the exchange below.
Only include stable things worth remembering across weeks (name, location, job, preferences, ongoing projects, constraints).
Exclude: passwords/keys/IDs, health or financial details, opinions about other people, one-off requests, anything the assistant said.
Return JSON: {"facts": ["short third-person fact", ...]}. Use {"facts": []} if nothing qualifies. Max 3 facts."""


def is_safe_fact(fact: str) -> bool:
    return 3 <= len(fact) <= 300 and not _SECRET.search(fact)


def explicit_memory_request(text: str) -> str | None:
    """'remember that I prefer metric units' -> 'prefer metric units' (rewritten to third person)."""
    m = _EXPLICIT.match(text)
    if not m:
        return None
    fact = m.group(1).strip().rstrip(".")
    fact = re.sub(r"^(?:that\s+)?i\s+am\b", "User is", fact, flags=re.I)
    fact = re.sub(r"^(?:that\s+)?i(?:'m)\b", "User is", fact, flags=re.I)
    fact = re.sub(r"^(?:that\s+)?i\s+", "User ", fact, flags=re.I)
    fact = re.sub(r"\bmy\b", "their", fact, flags=re.I)
    return fact if is_safe_fact(fact) else None


def name_from_message(text: str) -> str | None:
    m = _NAME.search(text)
    if not m:
        return None
    name = re.split(r"[.,!?]| and | but ", m.group(1).strip(), maxsplit=1)[0].strip()
    return f"User's name is {name}" if name and is_safe_fact(name) else None


async def extract_facts(provider: LLMProvider, user_message: str, reply: str, model: str | None = None) -> list[str]:
    if len(user_message) < 25:
        return []
    try:
        resp = await provider.chat(
            [
                {"role": "system", "content": EXTRACT_PROMPT},
                {"role": "user", "content": f"USER: {user_message}\nASSISTANT: {reply[:600]}"},
            ],
            model=model,
            temperature=0.0,
            max_tokens=200,
            json_mode=True,
        )
        facts = json.loads(resp.content).get("facts", [])
    except Exception as e:  # learning must never break chat
        log.info("fact extraction skipped: %s", e)
        return []
    return [f.strip() for f in facts if isinstance(f, str) and is_safe_fact(f.strip())][:3]
