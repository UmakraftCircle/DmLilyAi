"""In-memory buffer of recent messages for the single Discord channel the admin is
currently watching via the web Relay page's Channel tab. Deliberately not persisted here -
only the *choice* of channel is (see RelayChannelStore) - since LilyDiscordClient.watch_channel
backfills recent history from Discord itself whenever watching (re)starts.
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

    def since(self, after: int = 0, limit: int = 300) -> list[dict]:
        return [m for m in self._messages if m["id"] > after][-limit:]

    def status(self) -> dict:
        return {
            "channel_id": self.channel_id, "channel_name": self.channel_name,
            "guild_id": self.guild_id, "guild_name": self.guild_name,
        }
