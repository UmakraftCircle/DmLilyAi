"""SQLite-backed last-seen state for tracked uma.moe circles, so the polling job can diff
rank/points/member fan totals and only alert on real changes instead of every poll.

Also doubles as the "former member" record: a row stays here (with its last-known fan total
and `updated_at`) even after the member drops out of a circle's live roster, because the poll
job only touches rows for members it currently sees. /api/leaderboard diffs this table against
the live member list to find who left.
"""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.Helpers.clock import now_ts

SCHEMA = """
CREATE TABLE IF NOT EXISTS umamoe_circle_state (
    circle_id INTEGER PRIMARY KEY,
    name TEXT,
    monthly_rank INTEGER,
    monthly_point INTEGER,
    member_count INTEGER,
    updated_at REAL
);

CREATE TABLE IF NOT EXISTS umamoe_member_state (
    circle_id INTEGER NOT NULL,
    viewer_id INTEGER NOT NULL,
    trainer_name TEXT,
    total_fans INTEGER,
    updated_at REAL,
    PRIMARY KEY (circle_id, viewer_id)
);
"""


class UmamoeStore:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def get_circle_state(self, circle_id: int) -> dict | None:
        return self.db.query_one("SELECT * FROM umamoe_circle_state WHERE circle_id=?", (circle_id,))

    def set_circle_state(self, circle_id: int, name: str, monthly_rank: int | None,
                          monthly_point: int | None, member_count: int | None) -> None:
        self.db.execute(
            "INSERT INTO umamoe_circle_state(circle_id,name,monthly_rank,monthly_point,member_count,updated_at) "
            "VALUES (?,?,?,?,?,?) ON CONFLICT(circle_id) DO UPDATE SET "
            "name=excluded.name, monthly_rank=excluded.monthly_rank, monthly_point=excluded.monthly_point, "
            "member_count=excluded.member_count, updated_at=excluded.updated_at",
            (circle_id, name, monthly_rank, monthly_point, member_count, now_ts()),
        )

    def get_member_fans(self, circle_id: int, viewer_id: int) -> int | None:
        row = self.db.query_one(
            "SELECT total_fans FROM umamoe_member_state WHERE circle_id=? AND viewer_id=?", (circle_id, viewer_id)
        )
        return row["total_fans"] if row else None

    def set_member_fans(self, circle_id: int, viewer_id: int, trainer_name: str, total_fans: int) -> None:
        self.db.execute(
            "INSERT INTO umamoe_member_state(circle_id,viewer_id,trainer_name,total_fans,updated_at) "
            "VALUES (?,?,?,?,?) ON CONFLICT(circle_id,viewer_id) DO UPDATE SET "
            "trainer_name=excluded.trainer_name, total_fans=excluded.total_fans, updated_at=excluded.updated_at",
            (circle_id, viewer_id, trainer_name, total_fans, now_ts()),
        )

    def members_for_circle(self, circle_id: int) -> list[dict]:
        """Every member ever recorded for this circle (including ones no longer on the live
        roster), newest fan total first. `updated_at` freezes at a member's last-seen poll once
        they drop off the roster, so it doubles as their "last detected on uma.moe" timestamp.
        """
        return self.db.query(
            "SELECT viewer_id, trainer_name, total_fans, updated_at FROM umamoe_member_state "
            "WHERE circle_id=? ORDER BY total_fans DESC", (circle_id,)
        )
