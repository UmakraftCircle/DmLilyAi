"""Persisted state for the daily fan quota's DeficitTracker.

Without this, a trainer's carry (deficit still owed / surplus banked toward
future days) only lived in an in-memory dict on the running process - any
restart or Render redeploy silently reset it back to zero, understating (or
erasing) what a trainer actually still owed for the month. See
LilyAiTask/DailyTask/DeficitTask/Deficit.py for the DeficitTracker itself and
snapshot_job.py for where this gets read/written each day.
"""
from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import DeficitState
from LilyAiMemory.Storage.store import MemoryStore


class DeficitStateStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db

    def get(self, club: str, trainer_id: str) -> DeficitState | None:
        row = self.db.query_one(
            "SELECT * FROM deficit_tracker_state WHERE club=? AND trainer_id=?", (club, trainer_id)
        )
        return DeficitState(**row) if row else None

    def set(self, club: str, trainer_id: str, carry: int, total_gained: int) -> DeficitState:
        ts = now_ts()
        self.db.execute(
            "INSERT INTO deficit_tracker_state(club,trainer_id,carry,total_gained,updated_at) "
            "VALUES (?,?,?,?,?) ON CONFLICT(club,trainer_id) DO UPDATE SET "
            "carry=excluded.carry, total_gained=excluded.total_gained, updated_at=excluded.updated_at",
            (club, trainer_id, carry, total_gained, ts),
        )
        return DeficitState(club, trainer_id, carry, total_gained, ts)

    def reset(self, club: str, trainer_id: str) -> DeficitState:
        """Zero out carry/total_gained - called on the 1st of the month, the same
        boundary run_daily_fan_gain already re-baselines the monthly gain figure at."""
        return self.set(club, trainer_id, 0, 0)
