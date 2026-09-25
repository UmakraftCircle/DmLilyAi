"""Persists Discord reconnect backoff across process restarts. Without this, a Render
redeploy that lands mid-cooldown resets run_forever()'s in-memory backoff to its floor and
immediately retries - which re-triggers (or extends) a Cloudflare IP-level rate-limit block
(error 1015), rather than actually waiting it out.
"""
from LilyAiCore.ExternalServices.Database.sqlite import Database

SCHEMA = """
CREATE TABLE IF NOT EXISTS discord_reconnect_state (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    next_attempt_at REAL NOT NULL,
    backoff_s REAL NOT NULL
);
"""


class ReconnectState:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def get(self) -> tuple[float, float]:
        row = self.db.query_one("SELECT next_attempt_at, backoff_s FROM discord_reconnect_state WHERE id=1")
        return (row["next_attempt_at"], row["backoff_s"]) if row else (0.0, 0.0)

    def set(self, next_attempt_at: float, backoff_s: float) -> None:
        self.db.execute(
            "INSERT INTO discord_reconnect_state(id,next_attempt_at,backoff_s) VALUES (1,?,?) "
            "ON CONFLICT(id) DO UPDATE SET next_attempt_at=excluded.next_attempt_at, backoff_s=excluded.backoff_s",
            (next_attempt_at, backoff_s),
        )

    def clear(self) -> None:
        self.db.execute("DELETE FROM discord_reconnect_state WHERE id=1")
