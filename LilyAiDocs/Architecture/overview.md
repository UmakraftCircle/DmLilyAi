# Architecture

## Layers

```
Documentation   LilyAiDocs, LilyAiGroqSupport
Entry           LilyAiMain (Discord + API), LilyAiFrontend
Intelligence    LilyAiContext, LilyAiMemory, LilyAiTool, LilyAiWeb, LilyAiRag, LilyAiLearning
Infrastructure  LilyAiCore
```

Dependencies point downward only. Intelligence domains depend on `LilyAiCore` abstractions
(`LLMProvider`, `SearchProvider`, `Database`, `Embedder`), never on Groq, Discord or DuckDuckGo directly.

For per-domain audit status (what's built, what's wired, what's still a doc-only gap), see
`LilyAiDocs/Architecture/module-roadmap.md` - all 9 layers (the 6 intelligence domains plus
`LilyAiCore`, `LilyAiMain` and `LilyAiFrontend`) have been swept as of this writing.

## Ownership

LilyAi owns Context, Memory, Tool, Web, Rag and Learning. Replaceable: Groq, Discord, search providers, databases, Docker, Render.

## Where the wiring lives

`LilyAiMain/MainService/bootstrap.py` is the composition root: the only file that knows which concrete
provider, search engine and database are in use. Domains are decoupled from each other too:
Context receives plain data (`ContextInput`) rather than importing Memory or Rag; web tools are registered into
the Tool registry at bootstrap, so Tool never imports Web.

## Life of a DM

1. `Discord/Client` (or `Api/server.py`) turns the event into an `IncomingMessage` and calls `DMRouter.route`.
2. Middleware: access control, rate limit (8/min/user by default), input cleaning. A per-user lock keeps replies ordered.
3. Router order: pending confirmation/form/poll, onboarding for first contact, natural-language intents
   (help, "what do you remember", "forget everything", "remember that ..."), then chat.
4. `ChatWorkflow`: RAG retrieval + memory lookup, `ContextBuilder` assembles and trims the prompt, the model runs
   (with up to 4 tool rounds), the turn is stored, and facts are learned in the background.
5. The reply carries a `reply_id`; thumbs up/down feed `LilyAiLearning` and can promote good, evidence-backed answers into the RAG index.

## Models

Free-tier only: `openai/gpt-oss-20b` for chat, `openai/gpt-oss-120b` for hard prompts, `qwen/qwen3.6-27b` as an alternate and fallback.
`groq/compound-mini` is registered for agent workflows and is excluded from chat fallbacks. Rate-limited or failing models fall through to the next one (`Providers/Groq/client.py`).

`GROQ_API_KEY` accepts one key or several comma-separated (`gsk_a,gsk_b,gsk_c`). With multiple keys, `Providers/Groq/key_rotator.py`
draws from a shuffled bag (no replacement, reshuffles when empty) so load spreads evenly rather than favoring one key, and a key that
hits a 429 is benched (cooldown = its `retry-after`, or 30s default) so the next call switches to a working key immediately instead
of just sleeping it out.

## Actions, not just replies

`LilyAiTool`'s `remind_me` (`DiscordTools/discord_tools.py`) is the first tool that *acts* rather than only reading/answering: it
schedules a Discord DM to arrive later, unprompted. The plumbing behind it - `LilyAiCore/ExternalServices/Discord/notifier.py`
(`NotifierBox`) - exists because the Discord client is only constructed after the rest of the app (tools included); the box is a
mutable seam tools can hold at registration time, and `main.py` swaps in the real client once Discord connects. Until then (or if
Discord is disabled), a `NullNotifier` no-ops safely. Reminders are persisted via `ReminderStore` (SQLite,
`LilyAiCore/ExternalServices/Discord/reminder_store.py`): each is written when scheduled and removed once the send is attempted, so
a restart/redeploy in between no longer loses it. `NotifierBox.resume_pending()` replays anything still outstanding right after the
real Discord client is wired in on startup - anything overdue fires immediately instead of being dropped.

## Resilience

Discord connect failures (including Cloudflare-level rate-limit blocks, not just Discord's own 429s) no longer take the whole
process down. `main.py`'s `run()` waits on the API server and Discord tasks together via `asyncio.wait(FIRST_COMPLETED)`, and used
to run the Discord client via a bare `client.start(token)` - so any connect exception was treated the same as the API server dying,
tearing down both. The Discord task now runs via `LilyDiscordClient.run_forever()`, which retries with exponential backoff
(30s, capped at 15min) on `HTTPException` and other connect failures instead of raising - a Discord outage can no longer take
the API server down with it.

## Scheduled jobs

`Interaction/Workflows/scheduler.py` runs named async jobs in-process. The only job today is the Groq model scan
(`model_scan_job.py`): it feeds `LilyAiLearning/Evaluation/model_scan.py`, which grows the shared `ModelPool` and writes
`LilyAiGroqSupport/MODEL_CATALOG.md`. It is disabled with `MODEL_SCAN_ENABLED=false` and never runs on the offline provider.
The interval defaults to `MODEL_SCAN_INTERVAL_HOURS` (24h, 1h floor); `MODEL_SCAN_INTERVAL_SECONDS` overrides it for
sub-hour intervals (60s floor) when faster detection of new Groq models is needed.

## Unbounded-growth guards

Every table or in-memory collection written on a high-frequency path is capped, trimmed or evicted on insert:
- `ConversationMemory` - 500 turns/user (`LilyAiMemory/ConversationMemory/conversation_memory.py`)
- `UserMemory` - 200 facts/user (pre-existing)
- `LearningStore.learning_events` - 2000 rows/kind (`LilyAiLearning/store.py`) - this one matters most since
  `context_tokens` writes on every chat message and `tool` writes on every tool call.
- `RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated` (`LilyAiMain`) - all in-memory per-user
  dicts/sets, found unbounded during the Main audit, now capped with LRU/FIFO eviction. `SessionManager`
  specifically never evicts a *currently-held* lock, avoiding a real correctness bug that a naive LRU cap would
  have introduced.

`LilyAiMemory/KnowledgeMemory` (shared, user-independent notes) has been removed: it was a dead write path -
read every chat turn via `relevant_notes()`, but nothing ever called `.add()` - fully duplicated by
`LilyAiLearning/RagLearning`'s `learned:qa` promotion into the Rag index, which is the real, working version
of the same idea.

## Known orphan

`LilyAiCore/ExternalServices/Webhooks/webhook.py` (`post_webhook` - an ops-alert webhook) has zero callers anywhere
and isn't wired into `settings.py` (no `WEBHOOK_URL` var). Found during the Core audit; left in place and
intentionally not wired up.

## Frontend

See `LilyAiFrontend/README.md`: modular ES modules, one folder per page, shared components in `Shared/components/`, all pages registered in `Shared/routes.js`, styling tokens in `Assets/styles/tokens.css`.

`Settings` now has a Web card (`Settings/cards/webCard.js`) showing `web_enabled` status plus a manual query
tester against `/api/web/search` - giving `LilyAiWeb` the same frontend visibility as the other 5 domains.

Every `Shared/` file, every CSS file `index.html` references, and every page (`Home`, `Chat`, `Dashboard` + 4
cards, `Settings` + 4 cards, `Admin/Relay`, `Admin/DMSimulator`) were confirmed wired via `routes.js` during the
Frontend audit - no orphans. `Relay`'s polling loop correctly returns a cleanup function (`clearTimeout`) so it
stops on navigation, avoiding a leak on route change.

## Additions to the README scaffold

- `LilyAiMain/MainService/Api/` - FastAPI server; also serves the web client (`static.py`) so one URL is the site
- `LilyAiMain/MainService/bootstrap.py`, `Interaction/messages.py` - wiring and shared message types
- `Interaction/Workflows/scheduler.py`, `model_scan_job.py` - scheduled model scan
- `service.py` facade in each domain root; `tests/`; root `Dockerfile` and `render.yaml` (one service for bot, API and website)
- `LilyAiCore/ExternalServices/Discord/notifier.py`, `reminder_store.py` - actuator seam for tools that need to reach Discord directly, and the persistence behind scheduled reminders (see "Actions, not just replies" above)
