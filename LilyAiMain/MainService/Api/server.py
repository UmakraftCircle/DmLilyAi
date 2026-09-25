"""HTTP API for the web frontend (Chat, Dashboard, Settings, Relay, DM Simulator, Leaderboard)."""
import hmac
import time
from pathlib import Path

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from LilyAiLearning.Evaluation.evaluator import DEFAULT_CASES, Evaluator
from LilyAiMain.MainService.Api.static import default_frontend_dir, resolve_static
from LilyAiMain.MainService.bootstrap import App
from LilyAiMain.MainService.Interaction.messages import IncomingMessage
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatRequest
from LilyAiMain.MainService.Interaction.Workflows.model_scan_job import make_model_scan_job

LOOPBACK = {"127.0.0.1", "::1", "localhost", "testclient"}


def _member_gains(daily_fans: list[int] | None) -> tuple[int, int, int]:
    """(current_fans, daily_gain, monthly_gain) from uma.moe's daily-fan array.

    get_circle() accepts month/year, which means uma.moe hands back one full calendar
    month's worth of daily snapshots (day 1 .. last day of month) rather than "up to
    today" - days later in the month that haven't happened yet come back as 0 padding.
    So "today" is the LAST NON-ZERO entry, not simply the last slot in the array; blindly
    using daily[-1] picks up an unfilled future day (0) and produces a wildly negative
    monthly_gain (0 - day-1's real total).
    """
    daily = daily_fans or []
    if not daily:
        return 0, 0, 0
    latest_idx = 0
    for i, v in enumerate(daily):
        if v:
            latest_idx = i
    current = daily[latest_idx]
    prev_idx = None
    for i in range(latest_idx - 1, -1, -1):
        if daily[i]:
            prev_idx = i
            break
    daily_gain = current - daily[prev_idx] if prev_idx is not None else 0
    monthly_gain = current - daily[0]
    return current, daily_gain, monthly_gain


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
                total_fans, daily_gain, monthly_gain = _member_gains(m.get("daily_fans"))
                members.append({
                    "viewer_id": viewer_id,
                    "trainer_name": m.get("trainer_name") or str(viewer_id),
                    "total_fans": total_fans,
                    "daily_gain": daily_gain,
                    "monthly_gain": monthly_gain,
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
        return {"circles": circles, "former_members": former_members}

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
