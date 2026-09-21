from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import SessionState


class SessionMemory:
    """Ephemeral per-user working state (in-process, expires after idle)."""

    def __init__(self, idle_seconds: int = 30 * 60):
        self.idle_seconds = idle_seconds
        self._sessions: dict[str, SessionState] = {}

    def touch(self, user_id: str) -> tuple[SessionState, bool]:
        """Return (session, is_new)."""
        now = now_ts()
        s = self._sessions.get(user_id)
        if s and now - s.last_seen <= self.idle_seconds:
            s.last_seen = now
            return s, False
        s = SessionState(user_id, started_at=now, last_seen=now)
        self._sessions[user_id] = s
        return s, True

    def get(self, user_id: str) -> SessionState | None:
        return self._sessions.get(user_id)

    def end(self, user_id: str) -> None:
        self._sessions.pop(user_id, None)

    def active_count(self) -> int:
        now = now_ts()
        return sum(1 for s in self._sessions.values() if now - s.last_seen <= self.idle_seconds)
