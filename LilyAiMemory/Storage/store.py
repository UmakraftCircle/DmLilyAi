"""Storage adapter: the only place in LilyAiMemory that touches the database handle."""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from .schema import SCHEMA


class MemoryStore:
    def __init__(self, db: Database):
        self.db = db
        self.db.executescript(SCHEMA)
