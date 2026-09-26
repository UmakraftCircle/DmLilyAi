"""Fan gain leaderboard data: total / today / weekly / monthly per trainee.

Reads FanSnapshot rows written once per day by LilyAiTask/DailyTask (the
same job that runs Deficit.py) to compute gain since three boundaries:
today's 00:00, this week's Monday 00:00, and this month's 1st 00:00.

Monthly gain here is computed independently of LilyAiTask/MonthlyTask/
quota.py's carry-forward tracking - reconcile the two before shipping so
the fan gain embed and the quota DM never disagree for the same trainer.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import FanSnapshot
from LilyAiMemory.Storage.store import MemoryStore


class FanSnapshotStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db

    def record(self, club: str, trainer_id: str, fan_total: int) -> FanSnapshot:
        """Write today's snapshot for a trainer. Called once per day per
        trainer by the daily task, right after the uma.moe scrape."""
        ts = now_ts()
        sid = self.db.execute(
            "INSERT INTO fan_snapshots(club, trainer_id, fan_total, snapshot_at) VALUES (?,?,?,?)",
            (club, trainer_id, fan_total, ts),
        )
        return FanSnapshot(sid, club, trainer_id, fan_total, ts)

    def latest(self, club: str) -> dict[str, FanSnapshot]:
        """Most recent snapshot per trainer_id in this club."""
        rows = self.db.query(
            """
            SELECT fs.* FROM fan_snapshots fs
            JOIN (
                SELECT trainer_id, MAX(snapshot_at) AS max_ts
                FROM fan_snapshots WHERE club=?
                GROUP BY trainer_id
            ) latest ON fs.trainer_id = latest.trainer_id AND fs.snapshot_at = latest.max_ts
            WHERE fs.club=?
            """,
            (club, club),
        )
        return {r["trainer_id"]: FanSnapshot(**r) for r in rows}

    def at_or_before(self, club: str, cutoff: datetime) -> dict[str, FanSnapshot]:
        """For each trainer_id, their last snapshot at or before cutoff.
        Trainers with nothing that far back are simply absent from the
        result - the caller treats their gain as 0."""
        rows = self.db.query(
            """
            SELECT fs.* FROM fan_snapshots fs
            JOIN (
                SELECT trainer_id, MAX(snapshot_at) AS max_ts
                FROM fan_snapshots WHERE club=? AND snapshot_at<=?
                GROUP BY trainer_id
            ) base ON fs.trainer_id = base.trainer_id AND fs.snapshot_at = base.max_ts
            WHERE fs.club=?
            """,
            (club, cutoff.timestamp(), club),
        )
        return {r["trainer_id"]: FanSnapshot(**r) for r in rows}


@dataclass
class FanGainRow:
    trainer_id: str
    trainer_name: str
    club: str
    total: int
    today: int
    weekly: int
    monthly: int


def _boundaries(now: datetime) -> tuple[datetime, datetime, datetime]:
    """Return (today_start, week_start_monday, month_start), all UTC midnight."""
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = today_start - timedelta(days=now.weekday())  # Monday = 0
    month_start = today_start.replace(day=1)
    return today_start, week_start, month_start


def get_fan_gain_rows(
    club: str,
    roster: dict[str, str],
    store: FanSnapshotStore,
    now: datetime | None = None,
) -> list[FanGainRow]:
    """roster: trainer_id -> display name, e.g. from TrainerLinkStore.all_linked()."""
    now = now or datetime.utcnow()
    today_start, week_start, month_start = _boundaries(now)

    latest = store.latest(club)
    today_base = store.at_or_before(club, today_start)
    week_base = store.at_or_before(club, week_start)
    month_base = store.at_or_before(club, month_start)

    rows: list[FanGainRow] = []
    for trainer_id, snap in latest.items():
        total = snap.fan_total

        def gain_since(base_map: dict[str, FanSnapshot]) -> int:
            base = base_map.get(trainer_id)
            return total - base.fan_total if base else 0

        rows.append(
            FanGainRow(
                trainer_id=trainer_id,
                trainer_name=roster.get(trainer_id, "Unknown"),
                club=club,
                total=total,
                today=gain_since(today_base),
                weekly=gain_since(week_base),
                monthly=gain_since(month_base),
            )
        )

    rows.sort(key=lambda r: r.weekly, reverse=True)
    return rows
