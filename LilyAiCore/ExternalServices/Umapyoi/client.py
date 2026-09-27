"""Client for the umapyoi.net API (Uma Musume game data: characters, gacha banners, news).

Docs: https://umapyoi.net/docs/endpoints.html
Fully public/keyless - no auth header needed, unlike UmamoeClient. Rate limits are generous
(500/min, 7200/hour, 172800/day as of writing) so no key rotation is needed either.

This is a supplementary/flavor data source, not a primary one. See bootstrap.py's tool
descriptions: check_umamoe / check_fan_gain (circle+fan tracking) and web_search (everything
else current/factual) remain the bot's main tools - these are for game-trivia questions
(banners, character info, official news, birthdays) that don't fit either of those.
"""
import httpx

from LilyAiCore.Exceptions.errors import UmapyoiError

_BASE = "https://umapyoi.net/api/v1"


class UmapyoiClient:
    async def _get(self, path: str) -> dict | list:
        try:
            async with httpx.AsyncClient(timeout=15) as http:
                r = await http.get(f"{_BASE}{path}")
        except httpx.HTTPError as e:
            raise UmapyoiError(f"umapyoi.net request failed: {e}") from e
        if r.status_code != 200:
            raise UmapyoiError(f"umapyoi.net {path} failed: HTTP {r.status_code}: {r.text[:200]}")
        return r.json()

    async def gacha_current(self) -> dict | list:
        """Detailed info about the currently-live gacha banner(s)."""
        return await self._get("/gacha/current")

    async def news_latest(self, count: int = 5, english: bool = True) -> list:
        """Latest `count` (<=32) official news posts. English posts via the /en/ prefix."""
        count = max(1, min(count, 32))
        prefix = "/en" if english else ""
        return await self._get(f"{prefix}/news/latest/{count}")

    async def character_birthdays(self) -> dict:
        """Characters with a birthday today, plus the next upcoming birthday."""
        return await self._get("/character/currentbirthdays")

    async def character_list(self) -> list:
        """All characters' info needed for a list view - used for name-based lookup since the
        API itself is ID-based, not name-search."""
        return await self._get("/character/list")

    async def character(self, chara_id: int) -> dict:
        return await self._get(f"/character/{chara_id}")

    async def find_character(self, name: str) -> dict | None:
        """Best-effort name lookup: scans character_list() for any string field containing
        `name` (case-insensitive), since the exact field names aren't guaranteed stable and
        the API has no built-in search. Returns the first match's full list-view entry, or
        None if nothing matched."""
        name_lower = name.strip().lower()
        if not name_lower:
            return None
        chars = await self.character_list()
        for entry in chars:
            if not isinstance(entry, dict):
                continue
            for value in entry.values():
                if isinstance(value, str) and name_lower in value.lower():
                    return entry
        return None
