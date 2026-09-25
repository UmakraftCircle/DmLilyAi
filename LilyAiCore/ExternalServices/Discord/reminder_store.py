"""SQLite-backed store for pending remind_me DMs, so a restart/redeploy before a reminder
fires doesn't lose it. See NotifierBox.resume_pending() in notifier.py, which replays these
on startup.
"""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.Helpers.clock import now_ts

SCHEMA = """
CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    message TEXT NOT NULL,
    due_at REAL NOT NULL,
    created_at REAL NOT NULL
);
"""


class ReminderStore:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def add(self, user_id: str, message: str, due_at: float) -> int:
        return self.db.execute(
            "INSERT INTO reminders(user_id,message,due_at,created_at) VALUES (?,?,?,?)",
            (user_id, message, due_at, now_ts()),
        )

    def remove(self, reminder_id: int) -> None:
        self.db.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))

    def all_pending(self) -> list[dict]:
        return self.db.query("SELECT id, user_id, message, due_at FROM reminders ORDER BY due_at")
