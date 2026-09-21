import json

from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.Helpers.clock import now_ts

SCHEMA = """
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL, rating INTEGER NOT NULL,
    prompt TEXT, response TEXT, comment TEXT,
    used_evidence INTEGER NOT NULL DEFAULT 0, domains TEXT NOT NULL DEFAULT '[]',
    created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS learning_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL, key TEXT NOT NULL, value REAL NOT NULL DEFAULT 0, ok INTEGER NOT NULL DEFAULT 1,
    created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_events_kind ON learning_events(kind, key);
"""


class LearningStore:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def add_feedback(self, user_id, rating, prompt, response, comment, used_evidence, domains) -> int:
        return self.db.execute(
            "INSERT INTO feedback(user_id,rating,prompt,response,comment,used_evidence,domains,created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (user_id, rating, prompt, response, comment, int(used_evidence), json.dumps(domains), now_ts()),
        )

    def add_event(self, kind: str, key: str, value: float = 0.0, ok: bool = True) -> None:
        self.db.execute(
            "INSERT INTO learning_events(kind,key,value,ok,created_at) VALUES (?,?,?,?,?)",
            (kind, key, value, int(ok), now_ts()),
        )
