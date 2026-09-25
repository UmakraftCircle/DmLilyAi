"""HTTP API for the web frontend (Chat, Dashboard, Settings, Relay, DM Simulator, Leaderboard)."""
import hmac
import time
from datetime import datetime, timezone
from pathlib import Path

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from LilyAiCore.Helpers.clock import now_ts
from LilyAiLearning.Evaluation.evaluator import DEFAULT_CASES, Evaluator
from LilyAiMain.MainService.Api.static import default_frontend_dir, resolve_static
from LilyAiMain.MainService.bootstrap import App
from LilyAiMain.MainService.Interaction.messages import IncomingMessage
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatRequest
from LilyAiMain.MainService.Interaction.Workflows.model_scan_job import make_model_scan_job

LOOPBACK = {"127.0.0.1", "::1", "localhost", "testclient"}


def _member_gains(daily_fans: list[int] | None) -> dict:
    """Fan-gain breakdown from uma.moe's daily-fan array (one cumulative-total entry per
    day of the currently-tracked month; days that haven't happened yet come back as 0
    padding, since get_circle() hands back a full calendar month of snapshots rather than
    "up to today").

    Returns:
      total_fans   - current cumulative fan count (last day with real data)
      today_gain   - fans gained so far on the current (possibly still in-progress) day
      daily_gain   - fans gained on the last FULL completed day (i.e. "yesterday")
      monthly_gain - fans gained since day 1 of the tracked month
      week_avg     - average daily gain since this week's Monday, resetting every Monday;
                     None when Monday falls before day 1 of the fetched month (edge of month)

    "Today" is the LAST NON-ZERO entry, not simply the last slot in the array - blindly
    using daily[-1] would pick up an unfilled future day (0) and produce a wildly negative
    gain. Same logic walks backward again to find the last full day, and again for Monday.
    """
    daily = daily_fans or []
    empty = {"total_fans": 0, "today_gain": 0, "daily_gain": 0, "monthly_gain": 0, "week_avg": None}
    if not daily:
        return empty

    def last_nonzero(upto: int) -> int | None:
        for i in range(upto, -1, -1):
            if daily[i]:
                return i
        return None

    latest_idx = last_nonzero(len(daily) - 1)
    if latest_idx is None:
        return empty
    current = daily[latest_idx]

    prev_idx = last_nonzero(latest_idx - 1)
    today_gain = current - daily[prev_idx] if prev_idx is not None else 0

    day_before_idx = last_nonzero(prev_idx - 1) if prev_idx is not None else None
    daily_gain = (daily[prev_idx] - daily[day_before_idx]
                  if prev_idx is not None and day_before_idx is not None else 0)

    monthly_gain = current - daily[0]

    # Resolve "this Monday" as a day-of-month against the same array. Assumes the array's
    # month matches the server's current UTC month (true unless this poll happens right at
    # a month boundary); a Monday that falls in the previous month reports week_avg=None.
    today = datetime.now(timezone.utc)
    monday_day = today.day - today.weekday()  # Monday == 0
    week_avg = None
    if monday_day >= 1:
        monday_idx = monday_day - 1
        if monday_idx <= latest_idx and daily[monday_idx]:
            elapsed = max(1, latest_idx - monday_idx + 1)
            week_avg = round((current - daily[monday_idx]) / elapsed)

    return {
        "total_fans": current, "today_gain": today_gain, "daily_gain": daily_gain,
        "monthly_gain": monthly_gain, "week_avg": week_avg,
    }


class ChatBody(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    user_id: str = Field(default="web:admin", max_length=64)
    display_name: str = Field(default="", max_length=64)
    source: str = Field(default="web", pattern="^(web|simulator)$")


class FeedbackBody(BaseModel):
    user_id: str
    reply_id: str
    rating: int = Field(ge=-1, le=1)
    comment: str = ""


class IngestBody(BaseModel):
    source: str = Field(min_length=1, max_length=120)
    text: str = Field(min_length=1, max_length=200_000)


class QueryBody(BaseModel):
    query: str = Field(min_length=1, max_length=500)


def create_api(app: App) -> FastAPI:
    s = app.settings
    api = FastAPI(title="LilyAi API", version="1.0.0")
    api.add_middleware(
        CORSMiddleware, allow_origins=list(s.cors_origins), allow_methods=["*"], allow_headers=["*"],
    )

    async def auth(request: Request, authorization: str = Header(default="")):
        if s.admin_token:
            supplied = authorization.removeprefix("Bearer ").strip()
            if not hmac.compare_digest(supplied, s.admin_token):
                raise HTTPException(401, "Invalid or missing admin token")
        elif (request.client.host if request.client else "") not in LOOPBACK:
            raise HTTPException(401, "Set ADMIN_TOKEN to use the API from a non-local address")

    guard = [Depends(auth)]

    @api.api_route("/api/health", methods=["GET", "HEAD"])  # HEAD too, so uptime pingers work
    async def health():
        return {"ok": True, "discord": app.discord_state.connected, "uptime_s": int(time.time() - app.started_at)}

    @api.get("/api/auth-check", dependencies=guard)
    async def auth_check():
        return {"ok": True}

    @api.post("/api/chat", dependencies=guard)
    async def chat(body: ChatBody):
        uid = body.user_id if body.user_id.startswith(("web:", "sim:")) else f"{body.source[:3]}:{body.user_id}"
        out = await app.router.route(IncomingMessage(uid, body.text, body.display_name or uid, body.source))
        return {"user_id": uid, "messages": [o.to_dict() for o in out]}

    @api.post("/api/feedback", dependencies=guard)
    async def feedback(body: FeedbackBody):
        note = app.feedback.handle(body.user_id, body.reply_id, body.rating, body.comment)
        app.bus.publish("feedback", "web", body.user_id, text=f"{body.rating:+d} on {body.reply_id}")
        return {"message": note}

    @api.get("/api/memory/{user_id}", dependencies=guard)
    async def get_memory(user_id: str):
        return {
            "facts": [vars(f) for f in app.memory.user.list(user_id)],
            "turns": app.memory.conversation.count(user_id),
        }

    @api.delete("/api/memory/{user_id}", dependencies=guard)
    async def delete_memory(user_id: str):
        app.memory.forget_user(user_id)
        return {"ok": True}

    @api.get("/api/relay/events", dependencies=guard)
    async def relay(after: int = 0, source: str = "all"):
        return {"events": app.bus.since(after, source), "discord": app.discord_state.connected, "bot": app.discord_state.bot_name}

    @api.get("/api/dashboard", dependencies=guard)
    async def dashboard():
        users = app.db.query_one("SELECT COUNT(DISTINCT user_id) AS n FROM conversation_turns") or {"n": 0}
        turns = app.db.query_one("SELECT COUNT(*) AS n FROM conversation_turns") or {"n": 0}
        facts = app.db.query_one("SELECT COUNT(*) AS n FROM user_facts") or {"n": 0}
        return {
            "users": users["n"], "turns": turns["n"], "facts": facts["n"],
            "active_sessions": app.memory.session.active_count(),
            "rag": app.rag.stats(), "tools": app.tools.registry.names(),
            "learning": app.learning.report(),
            "discord": {"connected": app.discord_state.connected, "bot": app.discord_state.bot_name},
            "provider": type(app.provider).__name__,
        }

    @api.get("/api/config", dependencies=guard)
    async def config():
        return {
            "models": [vars(m) for m in app.pool.all()],
            "chat_model": s.chat_model, "reasoning_model": s.reasoning_model,
            "history_turns": s.history_turns, "token_budget": s.token_budget,
            "web_enabled": s.web_enabled, "learn_from_chats": s.learn_from_chats,
            "allowlist_size": len(s.allowed_user_ids), "provider": type(app.provider).__name__,
        }

    @api.get("/api/models/scan", dependencies=guard)
    async def scan_status():
        return {"enabled": s.model_scan_enabled, "interval_hours": s.model_scan_interval_hours,
                "max_auto": s.model_scan_max_auto, **app.scanner.status()}

    @api.post("/api/models/scan", dependencies=guard)
    async def scan_now():
        if type(app.provider).__name__ == "OfflineProvider":
            raise HTTPException(400, "Model scan needs GROQ_API_KEY")
        report = await make_model_scan_job(app.scanner, app.bus)()
        return {"summary": report.summary(), **vars(report)}

    @api.post("/api/rag/ingest", dependencies=guard)
    async def rag_ingest(body: IngestBody):
        return {"chunks_added": app.rag.ingest_text(body.source, body.text), **app.rag.stats()}

    @api.post("/api/rag/search", dependencies=guard)
    async def rag_search(body: QueryBody):
        return {"hits": [{"source": h.chunk.source, "score": round(h.score, 3), "text": h.chunk.text} for h in app.rag.retrieve(body.query, 5)]}

    @api.delete("/api/rag/sources/{source:path}", dependencies=guard)
    async def rag_delete(source: str):
        return {"removed": app.rag.delete_source(source), **app.rag.stats()}

    @api.post("/api/web/search", dependencies=guard)
    async def web_search(body: QueryBody):
        if not s.web_enabled:
            raise HTTPException(400, "Web search is disabled (WEB_ENABLED)")
        results = await app.web.search(body.query, 5)
        return {"hits": [{"title": r.title, "url": r.url, "snippet": r.snippet, "domain": r.domain, "score": round(r.score, 3)} for r in results]}

    @api.get("/api/leaderboard", dependencies=guard)
    async def leaderboard():
        if not app.umamoe:
            raise HTTPException(400, "uma.moe is not configured (set UMAMOE_API_KEY)")
        if not s.umamoe_circle_ids:
            raise HTTPException(400, "No circles tracked (set UMAMOE_CIRCLE_IDS)")
        fetched_at = now_ts()
        circles = []
        former_members = []
        for circle_id in s.umamoe_circle_ids:
            data = await app.umamoe.get_circle(circle_id=circle_id)
            c = data.get("circle") or {}
            name = c.get("name", str(circle_id))
            seen_ids: set = set()
            members = []
            for m in data.get("members", []):
                viewer_id = m.get("viewer_id")
                seen_ids.add(viewer_id)
                gains = _member_gains(m.get("daily_fans"))
                members.append({
                    "viewer_id": viewer_id,
                    "trainer_name": m.get("trainer_name") or str(viewer_id),
                    # uma.moe's own per-record refresh time when it provides one (field name
                    # unconfirmed - passed through defensively); otherwise this poll's time.
                    "last_updated": m.get("updated_at") or m.get("last_updated") or fetched_at,
                    **gains,
                })
            members.sort(key=lambda m: m["total_fans"], reverse=True)
            circles.append({
                "circle_id": circle_id, "name": name,
                "monthly_rank": c.get("monthly_rank"), "monthly_point": c.get("monthly_point"),
                "member_count": c.get("member_count"), "members": members,
            })
            # Anyone we've ever recorded for this circle (via the background poll job) who is
            # missing from the live roster has left — their store row keeps their last-known
            # fan total and the poll timestamp they were last seen at.
            if app.umamoe_store:
                for row in app.umamoe_store.members_for_circle(circle_id):
                    if row["viewer_id"] not in seen_ids:
                        former_members.append({
                            "circle_id": circle_id, "circle_name": name,
                            "viewer_id": row["viewer_id"], "trainer_name": row["trainer_name"],
                            "total_fans": row["total_fans"], "last_seen": row["updated_at"],
                        })
        former_members.sort(key=lambda m: m["last_seen"] or 0, reverse=True)
        return {"circles": circles, "former_members": former_members, "fetched_at": fetched_at}

    @api.post("/api/eval/run", dependencies=guard)
    async def run_eval():
        async def respond(prompt: str) -> str:
            reply = await app.chat.handle(ChatRequest("sim:eval", prompt, "eval"))
            app.memory.conversation.clear("sim:eval")
            return reply.text

        report = await Evaluator(respond).run(DEFAULT_CASES)
        return {"passed": report.passed, "total": report.total, "outcomes": [vars(o) for o in report.outcomes]}

    # ---- web client (same origin as the API, so no CORS or API URL setup) ----
    frontend = Path(s.frontend_dir) if s.frontend_dir else default_frontend_dir()

    @api.middleware("http")
    async def no_stale_client_files(request: Request, call_next):
        resp = await call_next(request)
        if not request.url.path.startswith("/api"):
            resp.headers["Cache-Control"] = "no-cache"  # always revalidate, so edits show up on the next load
            resp.headers["X-Content-Type-Options"] = "nosniff"
        return resp

    @api.get("/{client_path:path}", include_in_schema=False)
    async def web_client(client_path: str):
        if client_path.startswith("api/") or client_path in {"api", "docs", "openapi.json", "redoc"}:
            return JSONResponse({"detail": "Not found"}, status_code=404)
        target = resolve_static(frontend, client_path)
        if target is None:
            return JSONResponse({"detail": "Not found"}, status_code=404)
        return FileResponse(target)

    return api
