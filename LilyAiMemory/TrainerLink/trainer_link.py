"""Discord <-> uma.moe trainer ID linking.

A member must be linked (both a Discord ID and a uma.moe trainer ID on
file) before daily/monthly quota DMs are sent - see LilyAiTask/DailyTask/
DeficitTask/Deficit.py.
"""
from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Models.records import TrainerLink
from LilyAiMemory.Storage.store import MemoryStore


class TrainerLinkStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db

    def link(self, discord_id: str, trainer_id: str, trainer_name: str | None = None) -> TrainerLink:
        """Create or update the link for this Discord user.

        A Discord ID may only be linked to one trainer ID at a time; a
        fresh call for the same discord_id replaces the previous link.
        """
        self.db.execute("DELETE FROM trainer_links WHERE discord_id=?", (discord_id,))
        self.db.execute("DELETE FROM trainer_links WHERE trainer_id=? AND discord_id!=?", (trainer_id, discord_id))
        ts = now_ts()
        lid = self.db.execute(
            "INSERT INTO trainer_links(discord_id, trainer_id, trainer_name, created_at) VALUES (?,?,?,?)",
            (discord_id, trainer_id, trainer_name, ts),
        )
        return TrainerLink(lid, discord_id, trainer_id, trainer_name, ts)

    def by_discord_id(self, discord_id: str) -> TrainerLink | None:
        row = self.db.query_one("SELECT * FROM trainer_links WHERE discord_id=?", (discord_id,))
        return TrainerLink(**row) if row else None

    def by_trainer_id(self, trainer_id: str) -> TrainerLink | None:
        row = self.db.query_one("SELECT * FROM trainer_links WHERE trainer_id=?", (trainer_id,))
        return TrainerLink(**row) if row else None

    def is_linked(self, discord_id: str) -> bool:
        return self.by_discord_id(discord_id) is not None

    def unlink(self, discord_id: str) -> bool:
        before = self.by_discord_id(discord_id)
        self.db.execute("DELETE FROM trainer_links WHERE discord_id=?", (discord_id,))
        return before is not None

    def all_linked(self) -> list[TrainerLink]:
        rows = self.db.query("SELECT * FROM trainer_links ORDER BY id", ())
        return [TrainerLink(**r) for r in rows]
