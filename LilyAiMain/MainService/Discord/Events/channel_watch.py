"""In-memory buffer of recent messages for the single Discord channel the admin is
currently watching via the web Relay page's Channel tab. Deliberately not persisted here -
only the *choice* of channel is (see RelayChannelStore) - since LilyDiscordClient.watch_channel
backfills recent history from Discord itself whenever watching (re)starts.

Snowflake IDs (channel_id, guild_id, message_id) are kept as Python ints internally - that's
what discord.py and comparisons like `message.channel.id != watch.channel_id` need - but every
public method that hands data to the web API (status(), since()) converts them to strings
first. Discord IDs are 64-bit and JavaScript's Number can't represent that exactly, so an ID
that goes out as a JSON number comes back from the browser silently corrupted (a different,
usually nonexistent, channel/message) - "Unknown Channel"/"Unknown Message" 404s are the
symptom. Strings round-trip exactly.
"""
import itertools
from collections import deque
from typing import Any


class ChannelWatch:
    def __init__(self, maxlen: int = 300):
        self._messages: deque[dict[str, Any]] = deque(maxlen=maxlen)
        self._ids = itertools.count(1)
        self.channel_id: int | None = None
        self.channel_name = ""
        self.guild_id: int | None = None
        self.guild_name = ""

    def reset(self, channel_id: int | None, channel_name: str, guild_id: int | None, guild_name: str) -> None:
        self.channel_id, self.channel_name = channel_id, channel_name
        self.guild_id, self.guild_name = guild_id, guild_name
        self._messages.clear()

    def add(self, *, message_id: int, author: str, is_me: bool, text: str, ts: float, reply_to: dict | None = None) -> dict:
        m = {
            "id": next(self._ids), "message_id": message_id, "author": author, "is_me": is_me,
            "text": text, "ts": ts, "reply_to": reply_to,
        }
        self._messages.append(m)
        return m

    @staticmethod
    def _out(m: dict) -> dict:
        out = {**m, "message_id": str(m["message_id"])}
        if m.get("reply_to"):
            out["reply_to"] = {**m["reply_to"], "message_id": str(m["reply_to"]["message_id"])}
        return out

    def since(self, after: int = 0, limit: int = 300) -> list[dict]:
        return [self._out(m) for m in self._messages if m["id"] > after][-limit:]

    def status(self) -> dict:
        return {
            "channel_id": str(self.channel_id) if self.channel_id is not None else None,
            "channel_name": self.channel_name,
            "guild_id": str(self.guild_id) if self.guild_id is not None else None,
            "guild_name": self.guild_name,
        }
