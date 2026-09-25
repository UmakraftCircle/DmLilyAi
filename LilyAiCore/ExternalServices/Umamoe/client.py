"""Client for the uma.moe API (Umamusume circle/fan tracking and leaderboards).

Spec: https://uma.moe/api/docs/openapi.yaml
Every endpoint except /api/health and /api/ver* requires an X-API-Key header.
"""
import httpx

from LilyAiCore.Exceptions.errors import UmamoeError

_BASE = "https://uma.moe"


class UmamoeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _headers(self) -> dict:
        return {"X-API-Key": self.api_key} if self.api_key else {}

    async def _get(self, path: str, params: dict | None = None) -> dict:
        clean = {k: v for k, v in (params or {}).items() if v is not None and v != ""}
        try:
            async with httpx.AsyncClient(timeout=15, headers=self._headers()) as http:
                r = await http.get(f"{_BASE}{path}", params=clean)
        except httpx.HTTPError as e:
            raise UmamoeError(f"uma.moe request failed: {e}") from e
        if r.status_code != 200:
            raise UmamoeError(f"uma.moe {path} failed: HTTP {r.status_code}: {r.text[:200]}")
        return r.json()

    async def get_circle(self, circle_id: int | None = None, viewer_id: int | None = None,
                          month: int | None = None, year: int | None = None) -> dict:
        """Circle details + member fan data. One of circle_id/viewer_id is required."""
        if circle_id is None and viewer_id is None:
            raise UmamoeError("get_circle needs circle_id or viewer_id")
        return await self._get("/api/v4/circles", {
            "circle_id": circle_id, "viewer_id": viewer_id, "month": month, "year": year,
        })

    async def list_circles(self, query: str = "", page: int = 0, limit: int | None = None) -> dict:
        return await self._get("/api/v4/circles/list", {"query": query, "page": page, "limit": limit})

    async def monthly_rankings(self, query: str = "", page: int = 0, limit: int = 100,
                                sort_by: str = "monthly_gain") -> dict:
        return await self._get("/api/v4/rankings/monthly", {
            "query": query, "page": page, "limit": limit, "sort_by": sort_by,
        })

    async def gains_rankings(self, query: str = "", page: int = 0, limit: int = 100,
                              sort_by: str = "gain_30d") -> dict:
        return await self._get("/api/v4/rankings/gains", {
            "query": query, "page": page, "limit": limit, "sort_by": sort_by,
        })

    async def profile(self, account_id: str) -> dict:
        return await self._get(f"/api/v4/user/profile/{account_id}")
