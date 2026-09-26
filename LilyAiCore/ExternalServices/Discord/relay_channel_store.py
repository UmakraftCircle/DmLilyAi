"""Persists which Discord channel the admin's web Relay page is watching, so the choice
survives a page refresh and a process restart - and applies for every admin, since it's a
single server-side value rather than something stored per-browser (contrast with the API
connection settings, which deliberately live in localStorage instead).
"""
from LilyAiCore.ExternalServices.Database.sqlite import Database

SCHEMA = """
CREATE TABLE IF NOT EXISTS discord_relay_channel (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    channel_id INTEGER,
    channel_name TEXT,
    guild_id INTEGER,
    guild_name TEXT
);
"""


class RelayChannelStore:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def get(self) -> dict | None:
        row = self.db.query_one(
            "SELECT channel_id, channel_name, guild_id, guild_name FROM discord_relay_channel WHERE id=1"
        )
        return dict(row) if row and row["channel_id"] else None

    def set(self, channel_id: int, channel_name: str, guild_id: int, guild_name: str) -> None:
        self.db.execute(
            "INSERT INTO discord_relay_channel(id,channel_id,channel_name,guild_id,guild_name) VALUES (1,?,?,?,?) "
            "ON CONFLICT(id) DO UPDATE SET channel_id=excluded.channel_id, channel_name=excluded.channel_name, "
            "guild_id=excluded.guild_id, guild_name=excluded.guild_name",
            (channel_id, channel_name, guild_id, guild_name),
        )

    def clear(self) -> None:
        self.db.execute("DELETE FROM discord_relay_channel WHERE id=1")
