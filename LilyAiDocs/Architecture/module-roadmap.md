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
| **LilyAiTool** | ✅ Audited | 6 submodules, all wired: `Executor` runs `Validator.validate_args()` then the handler, catching timeout/`ToolError`/any crash. Added `remind_me` actuator (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. |
| **LilyAiWeb** | ✅ Audited | 5 submodules, all wired via `service.py`'s search -> process -> extract pipeline. `Cache/TTLCache` confirmed genuinely used. `Sources.is_safe_url` checked twice in the extractor (pre-fetch and post-redirect) - real SSRF guard. Added `/api/web/search` + Settings web card. |
| **LilyAiCore** (Infrastructure) | ✅ Audited | 8 submodules. `Database`, `Discord` helpers/notifier, `Search`, `Config`, `Constants`, `Exceptions` (all 7 error classes used), `Helpers` (all 4 text functions used, `tokenize` shared by Rag + Memory), `Logging`, `Providers` (Groq/offline) all confirmed wired. **One orphan found**: `ExternalServices/Webhooks/webhook.py` (`post_webhook` - ops-alert webhook) has zero callers anywhere and isn't wired into `settings.py` (no `WEBHOOK_URL` var). Decision: leave it alone for now, not removed, not wired up. |
| **LilyAiMain** (Entry) | ✅ Audited + fixed | `Api`, `Discord` (`Client`/`Router`/`Middleware`/`Session`/`Events`), `Interaction` (`Feedback`/`Forms`/`Menus`/`Onboarding`/`Polls`/`Workflows`) - all confirmed wired via `Router`, the central dispatcher. No orphans. Found and fixed the same unbounded-growth shape three times: `RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated` - all now capped with LRU/FIFO eviction (`SessionManager` specifically never evicts a *currently-held* lock, avoiding a real correctness bug). |
| **LilyAiFrontend** | ✅ Audited | Every `Shared/` file (9 components, `app.js`, `api.js`, `routes.js`, `theme.js`, `icons.js`, `ui.js`), every CSS file `index.html` references, and every page (`Home`, `Chat`, `Dashboard` + 4 cards, `Settings` + 4 cards, `Admin/Relay`, `Admin/DMSimulator`) confirmed wired via `routes.js`, the frontend's own "facade". No orphans. `Relay`'s polling loop correctly returns a cleanup function (`clearTimeout`) so it stops on navigation - no leak on route change. |

## All layers audited - remaining items are small and known

1. **`retriever.py` docstring** - still says "over user facts **and knowledge notes**", a stale reference
   to the retired `KnowledgeMemory`. One-line fix, no behavior change, still needs a go-ahead.
2. **Fold `LilyAiCore`/`LilyAiMain`/`LilyAiFrontend` findings into `overview.md`** - it currently only
   reflects the 6 intelligence-domain findings from the first docs pass.
3. **`GROQ_API_KEY` / `DISCORD_TOKEN`** still not set on the live Render service - highest real-world
   impact of anything on this list. Everything audited across all 9 layers runs against `OfflineProvider`
   with Discord disconnected until these are set.
4. **`remind_me` persistence** - reminders are in-memory only, lost on restart/redeploy.
5. **`ExternalServices/Webhooks`** - orphan, intentionally left alone per your call.

## Docs alignment pass - partial (6 intelligence domains only)

Checked the **live** `README.md` and `Architecture/overview.md` on GitHub (not the local mounted copy some
of this audit was originally compared against): neither actually contains the `PostgreSQL`/`VectorStorage`/
`Chroma`/`FAISS`/`Qdrant`/`DataTools` claims that were flagged during the domain audits - `README.md` only
lists top-level domain folders and defers detail to `overview.md`, and `overview.md` is a high-level
architecture doc that never went into that level of subfolder detail either. So there was nothing false to
remove from the live docs. `overview.md` was updated with the 6-domain findings; item 2 above still open.

## Repeatable audit process (used for all 9 layers - reuse for any future addition, e.g. LilyAiVoice/Vision)

1. `view`/list the layer's directory - confirm every documented subfolder actually exists.
2. Read `service.py` (or the closest equivalent facade - `routes.js` served this role for the frontend) -
   it shows what's actually wired together.
3. For anything that looks like a write path (a `.add()`, an `.ingest()`, a table insert), code-search
   the whole repo for real callers before trusting it's live - `KnowledgeMemory` and `post_webhook()` both
   looked complete but had zero callers.
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
