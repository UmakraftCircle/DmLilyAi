# Module Roadmap: the 6 Intelligence Domains + Core/Main/Frontend

Purpose: track audit status and build order for every layer, so future work on any one of them starts
from a known state instead of re-discovering it. Update this file whenever a layer gets audited or a
listed gap gets resolved.

## Status - ALL 9 layers audited

| Domain | Status | Summary |
|---|---|---|
| **LilyAiContext** | ✅ Audited | 7 submodules, all wired via `ContextBuilder/builder.py`. No orphans, no doc gaps. |
| **LilyAiMemory** | ✅ Audited + cleaned | 6 submodules (was 7). `KnowledgeMemory` retired - dead write path, fully duplicated by Rag's `learned:qa` promotion. `ConversationMemory` now capped (500 turns/user), matching `UserMemory`'s existing 200-fact cap. |
| **LilyAiRag** | ✅ Audited | Fully wired: Document -> Chunking -> Embedding -> VectorStore -> Retrieval -> Ranking. No orphans. `HashingEmbedder` is lexical (word/bigram hashing), not semantic - deliberate zero-cost tradeoff, stated in its own docstring. |
| **LilyAiLearning** | ✅ Audited + fixed | 7 submodules, all real and wired. `LearningStore`'s `learning_events` table now has a per-kind trim (2000 rows/kind) - it was unbounded despite being written on every chat message and every tool call. |
| **LilyAiTool** | ✅ Audited | 6 submodules, all wired: `Executor` runs `Validator.validate_args()` then the handler, catching timeout/`ToolError`/any crash. Added `remind_me` actuator (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. `check_umamoe` added since (see Umamoe section below). |
| **LilyAiWeb** | ✅ Audited | 5 submodules, all wired via `service.py`'s search -> process -> extract pipeline. `Cache/TTLCache` confirmed genuinely used. `Sources.is_safe_url` checked twice in the extractor (pre-fetch and post-redirect) - real SSRF guard. Added `/api/web/search` + Settings web card. |
| **LilyAiCore** (Infrastructure) | ✅ Audited + fixed | 8 submodules. `Database`, `Discord` helpers/notifier, `Search`, `Config`, `Constants`, `Exceptions` (all 7 error classes used, plus `UmamoeError` added since), `Helpers` (all 4 text functions used, `tokenize` shared by Rag + Memory), `Logging`, `Providers` (Groq/offline) all confirmed wired. `ExternalServices/Webhooks/webhook.py` (`post_webhook`) is no longer an orphan - see item 5 below. `ExternalServices/Umamoe/` (client + store) added since - see Umamoe section below. |
| **LilyAiMain** (Entry) | ✅ Audited + fixed | `Api`, `Discord` (`Client`/`Router`/`Middleware`/`Session`/`Events`), `Interaction` (`Feedback`/`Forms`/`Menus`/`Onboarding`/`Polls`/`Workflows`) - all confirmed wired via `Router`, the central dispatcher. No orphans. Found and fixed the same unbounded-growth shape three times: `RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated` - all now capped with LRU/FIFO eviction (`SessionManager` specifically never evicts a *currently-held* lock, avoiding a real correctness bug). Also fixed a process-isolation bug: `run()`'s `asyncio.wait(FIRST_COMPLETED)` tore down the whole app (API included) on any Discord connect failure - Discord's `client.start()` now runs via `run_forever()`, which retries with backoff instead of raising. `Interaction/Workflows/umamoe_job.py` + `/api/leaderboard` added since - see Umamoe section below. |
| **LilyAiFrontend** | ✅ Audited | Every `Shared/` file (9 components, `app.js`, `api.js`, `routes.js`, `theme.js`, `icons.js`, `ui.js`), every CSS file `index.html` references, and every page (`Home`, `Chat`, `Dashboard` + 4 cards, `Settings` + 4 cards, `Admin/Relay`, `Admin/DMSimulator`) confirmed wired via `routes.js`, the frontend's own "facade". No orphans. `Relay`'s polling loop correctly returns a cleanup function (`clearTimeout`) so it stops on navigation - no leak on route change. `Leaderboard` page added since - see Umamoe section below. |

## In progress: Umamoe fan tracking (uma.moe)

New integration, added across four layers - built, not yet audit-passed the way the 9 layers above were:

- **`LilyAiCore/ExternalServices/Umamoe/`** - `client.py` (uma.moe API wrapper: `get_circle`, `list_circles`,
  `monthly_rankings`, `gains_rankings`, `profile`; `X-API-Key` auth) + `store.py` (SQLite last-seen
  circle/member state, for diffing).
- **`LilyAiTool`** - `check_umamoe` actuator (bootstrap's `_umamoe_tools`), on-demand circle standing.
- **`LilyAiMain`** - `Interaction/Workflows/umamoe_job.py`, a scheduled job (`umamoe-poll`, default every
  `UMAMOE_POLL_INTERVAL_HOURS`=6h) that diffs tracked circles' rank/points and member fan totals against
  `UmamoeStore`, publishes to the event bus, and DMs `UMAMOE_NOTIFY_USER_ID` on real changes. `GET
  /api/leaderboard` returns the tracked circles + members (sorted by fans) for the frontend.
- **`LilyAiFrontend`** - new `Leaderboard` page (`LilyAiFrontend/Leaderboard/leaderboard.js`), registered in
  `routes.js` under the Workspace group, own icon in `icons.js`.
- **Config** - `UMAMOE_API_KEY`, `UMAMOE_CIRCLE_IDS` (currently 2 tracked clubs), `UMAMOE_NOTIFY_USER_ID`,
  `UMAMOE_POLL_INTERVAL_HOURS` on `Settings` + `.env.example`. Everything no-ops cleanly (tool unregistered,
  job not scheduled, `/api/leaderboard` 400s) when `UMAMOE_API_KEY` is unset.

**Not yet done**: `UMAMOE_API_KEY` and the two `UMAMOE_CIRCLE_IDS` need to be set on the live Render service
before any of this does anything real. Hasn't had a full audit pass (steps 1-8 below) - built directly
from the OpenAPI spec (`https://uma.moe/api/docs/openapi.yaml`) and the existing `remind_me`/model-scan
patterns, not yet re-checked against a live API response shape.

## All layers audited - remaining items are small and known

1. ~~**`retriever.py` docstring**~~ - fixed. `LilyAiMemory/Retrieval/retriever.py`'s docstring no longer
   references the retired `KnowledgeMemory`; now correctly says it ranks over user facts only.
2. ~~**Fold `LilyAiCore`/`LilyAiMain`/`LilyAiFrontend` findings into `overview.md`**~~ - fixed. Added a
   `## Resilience` section (the `FIRST_COMPLETED`/`run_forever` fix), the three `LilyAiMain`
   unbounded-growth guards, the `LilyAiCore` Webhooks orphan, updated the reminder-persistence note under
   "Actions, not just replies", and expanded the Frontend section with its audit confirmation.
3. ~~**`GROQ_API_KEY` / `DISCORD_TOKEN`**~~ - both now set on the live Render service. Groq provider
   confirmed ready with 6 API key(s); Discord connects (subject to Cloudflare rate-limit blocks - see
   the `run_forever()` backoff fix under LilyAiMain above).
4. ~~**`remind_me` persistence**~~ - fixed. New `ReminderStore` (SQLite, same pattern as `LearningStore`)
   persists each reminder on creation; `NotifierBox.resume_pending()` replays anything still outstanding
   once the real Discord client is wired in on startup, firing overdue ones immediately instead of
   dropping them.
5. ~~**`ExternalServices/Webhooks`**~~ - implemented. Added `WEBHOOK_URL` to `Settings`/`.env.example`.
   `post_webhook` now has two real callers: `LilyAiMain/main.py` fires it when the API or Discord task
   crashes (the `FIRST_COMPLETED` handler), and `Scheduler._loop` fires it when a scheduled job raises
   (previously logged only). Both are fire-and-forget and stay silent when `WEBHOOK_URL` is unset - a
   startup log line says so once, at boot.
6. **Umamoe fan tracking** - see the "In progress" section above. Needs `UMAMOE_API_KEY` +
   `UMAMOE_CIRCLE_IDS` set on Render, then a real-response audit pass before it's marked done here.

## Docs alignment pass - now covers all 9 layers

Checked the **live** `README.md` and `Architecture/overview.md` on GitHub (not the local mounted copy some
of this audit was originally compared against): neither actually contains the `PostgreSQL`/`VectorStorage`/
`Chroma`/`FAISS`/`Qdrant`/`DataTools` claims that were flagged during the domain audits - `README.md` only
lists top-level domain folders and defers detail to `overview.md`, and `overview.md` is a high-level
architecture doc that never went into that level of subfolder detail either. So there was nothing false to
remove from the live docs. `overview.md` now reflects all 9 layers' findings (item 2 above, closed).

## Repeatable audit process (used for all 9 layers - reuse for any future addition, e.g. LilyAiVoice/Vision, or to audit-pass Umamoe above)

1. `view`/list the layer's directory - confirm every documented subfolder actually exists.
2. Read `service.py` (or the closest equivalent facade - `routes.js` served this role for the frontend) -
   it shows what's actually wired together.
3. For anything that looks like a write path (a `.add()`, an `.ingest()`, a table insert), code-search
   the whole repo for real callers before trusting it's live - `KnowledgeMemory` and `post_webhook()` both
   looked complete but had zero callers (the latter now fixed - see item 5 above).
4. For anything that looks like a shared/duplicate concept across domains, check both before building
   either further - `KnowledgeMemory` vs Rag's `learned:qa` promotion was exactly this. (A near-miss:
   `chunk_for_discord` vs `split_reply` looked like a possible duplicate but was clean layering instead -
   check before assuming duplication too.)
5. Check write frequency, not just write existence - a real, wired write path can still be an unbounded-growth
   risk if nothing caps it. Found in three shapes: a DB table (`learning_events`), in-memory per-user
   dicts/sets (`RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated`), and confirmed *not*
   a problem where a cleanup function already existed (`Relay`'s polling loop).
6. Compare the directory against the **live** repo's docs, not a locally mounted/cached copy that may be
   stale - confirm a claim actually exists in the current file before treating it as a gap to fix.
7. Not every gap needs code built to close it - some are better resolved by fixing the doc's claim instead
   of building unrequested scope, and some orphans are fine to just leave alone if that's the call made.
8. Report findings, get a decision, then act - never restructure a layer without that go-ahead.
