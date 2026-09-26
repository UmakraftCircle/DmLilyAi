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


@dataclass
class TrainerLink:
    """A confirmed Discord <-> uma.moe trainer ID link."""

    id: int
    discord_id: str
    trainer_id: str
    trainer_name: str | None = None
    created_at: float = 0.0


@dataclass
class FanSnapshot:
    """A trainer's fan_total at a point in time.

    Written once per day (and, on Mondays, doubles as the week's
    baseline) by LilyAiTask/DailyTask; used by LilyAiMemory.FanGain to
    compute today/weekly/monthly gain for the fan gain leaderboard.
    """

    id: int
    club: str
    trainer_id: str
    fan_total: int
    snapshot_at: float = 0.0
