from dataclasses import dataclass, field


@dataclass
class UserFact:
    id: int
    user_id: str
    fact: str
    source: str = "user"
    created_at: float = 0.0


@dataclass
class ConversationTurn:
    id: int
    user_id: str
    role: str  # "user" | "assistant"
    content: str
    created_at: float = 0.0


@dataclass
class SessionState:
    user_id: str
    started_at: float
    last_seen: float
    data: dict = field(default_factory=dict)
