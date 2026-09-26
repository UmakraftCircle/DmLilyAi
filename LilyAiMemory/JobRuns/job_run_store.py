"""Idempotency guard for scheduled jobs that must run at most once per UTC calendar day.

Without this, a scheduler job aligned to a fixed UTC time (e.g. 11:00) could still
fire twice for the same day if the process restarts right around that time - a
Render redeploy briefly overlapping the old and new process, or a crash-restart
loop - since the new process's in-memory scheduler has no idea what the old one
already sent. A job checks has_run() before doing anything user-visible (like
sending a DM) and calls mark_run() right after, so a second process racing the
same day's run sees it's already claimed and skips instead of sending a duplicate.
"""
from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Storage.store import MemoryStore


class JobRunStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db

    def has_run(self, job_name: str, run_date: str) -> bool:
        """run_date: a UTC calendar date as 'YYYY-MM-DD'."""
        row = self.db.query_one(
            "SELECT 1 FROM daily_job_runs WHERE job_name=? AND run_date=?", (job_name, run_date)
        )
        return row is not None

    def mark_run(self, job_name: str, run_date: str) -> None:
        self.db.execute(
            "INSERT INTO daily_job_runs(job_name, run_date, ran_at) VALUES (?,?,?) "
            "ON CONFLICT(job_name, run_date) DO NOTHING",
            (job_name, run_date, now_ts()),
        )
