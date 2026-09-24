# Module Roadmap: the 6 Intelligence Domains + Core/Main

Purpose: track audit status and build order for every layer, so future work on any one of them starts
from a known state instead of re-discovering it. Update this file whenever a layer gets audited or a
listed gap gets resolved.

## Status - 6 intelligence domains + LilyAiCore + LilyAiMain audited

| Domain | Status | Summary |
|---|---|---|
| **LilyAiContext** | ✅ Audited | 7 submodules, all wired via `ContextBuilder/builder.py`. No orphans, no doc gaps. |
| **LilyAiMemory** | ✅ Audited + cleaned | 6 submodules (was 7). `KnowledgeMemory` retired - dead write path, fully duplicated by Rag's `learned:qa` promotion. `ConversationMemory` now capped (500 turns/user), matching `UserMemory`'s existing 200-fact cap. |
| **LilyAiRag** | ✅ Audited | Fully wired: Document -> Chunking -> Embedding -> VectorStore -> Retrieval -> Ranking. No orphans. `HashingEmbedder` is lexical (word/bigram hashing), not semantic - deliberate zero-cost tradeoff, stated in its own docstring. |
| **LilyAiLearning** | ✅ Audited + fixed | 7 submodules, all real and wired. `LearningStore`'s `learning_events` table now has a per-kind trim (2000 rows/kind) - it was unbounded despite being written on every chat message and every tool call. |
| **LilyAiTool** | ✅ Audited | 6 submodules, all wired: `Executor` runs `Validator.validate_args()` then the handler, catching timeout/`ToolError`/any crash. Added `remind_me` actuator (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. |
| **LilyAiWeb** | ✅ Audited | 5 submodules, all wired via `service.py`'s search -> process -> extract pipeline. `Cache/TTLCache` confirmed genuinely used. `Sources.is_safe_url` checked twice in the extractor (pre-fetch and post-redirect) - real SSRF guard. Added `/api/web/search` + Settings web card. |
| **LilyAiCore** (Infrastructure) | ✅ Audited | 8 submodules. `Database`, `Discord` helpers/notifier, `Search`, `Config`, `Constants`, `Exceptions` (all 7 error classes used), `Helpers` (all 4 text functions used, `tokenize` shared by Rag + Memory), `Logging`, `Providers` (Groq/offline) all confirmed wired. **One orphan found**: `ExternalServices/Webhooks/webhook.py` (`post_webhook` - ops-alert webhook) has zero callers anywhere and isn't wired into `settings.py` (no `WEBHOOK_URL` var). Decision: leave it alone for now, not removed, not wired up. |
| **LilyAiMain** (Entry) | ✅ Audited + fixed | `Api`, `Discord` (`Client`/`Router`/`Middleware`/`Session`/`Events`), `Interaction` (`Feedback`/`Forms`/`Menus`/`Onboarding`/`Polls`/`Workflows`) - all confirmed wired via `Router`, the central dispatcher. **No orphans** - first layer with zero dead code. Found the same unbounded-growth shape three times (a per-user dict/set that never shrank) and fixed all three: `RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated` - all now capped with LRU/FIFO eviction (`SessionManager` specifically never evicts a *currently-held* lock, to avoid a real correctness bug). |
| `LilyAiFrontend` | ⬜ Not formally audited | Most files read incidentally while building features. Lower priority - least likely to hide real bugs. |

## Known minor cleanup (not yet done, trivial when picked up)
`LilyAiMemory/Retrieval/retriever.py`'s docstring still says "over user facts **and knowledge notes**" - a
stale reference to `KnowledgeMemory`, which was retired. One-line fix, no behavior change, needs a go-ahead
since it's still a code edit.

## Docs alignment pass - done (for the 6 intelligence domains)

Checked the **live** `README.md` and `Architecture/overview.md` on GitHub (not the local mounted copy some of
this audit was originally compared against): neither actually contains the `PostgreSQL`/`VectorStorage`/
`Chroma`/`FAISS`/`Qdrant`/`DataTools` claims that were flagged during the domain audits - `README.md` only
lists top-level domain folders and defers detail to `overview.md`, and `overview.md` is a high-level
architecture doc that never went into that level of subfolder detail either. So there was nothing false to
remove from the live docs.

`overview.md` was updated with everything built this session (multi-key Groq rotation, `remind_me` actuator,
`NotifierBox`, `MODEL_SCAN_INTERVAL_SECONDS`, `KnowledgeMemory` removal, growth guards, Settings web card).
`README.md` needed no edits. Not yet updated with the `LilyAiCore`/`LilyAiMain` findings (Webhooks orphan,
the three per-user dict fixes) - fold into the next docs pass once `LilyAiFrontend` is also audited.

## Also still open (outside this roadmap's original scope, but worth remembering)
- `GROQ_API_KEY` / `DISCORD_TOKEN` still not set on the live Render service - everything audited runs
  against `OfflineProvider` with Discord disconnected until these are set.
- `remind_me` reminders are in-memory only - lost on restart/redeploy, no persistence yet.

## Remaining work
1. `LilyAiFrontend` - the only unaudited layer left.
2. Fold `LilyAiCore`/`LilyAiMain` findings into `overview.md` (currently only has the 6-domain findings).
3. The `retriever.py` docstring cleanup, still pending a go-ahead.
4. `GROQ_API_KEY`/`DISCORD_TOKEN` on Render - highest real-world impact, still not done.

## Repeatable audit process (used for all 6 domains + LilyAiCore + LilyAiMain - reuse for LilyAiFrontend next)

1. `view`/list the domain's directory - confirm every documented subfolder actually exists.
2. Read `service.py` (the facade) - it shows which submodules are actually wired together.
3. For anything that looks like a write path (a `.add()`, an `.ingest()`, a table insert), code-search
   the whole repo for real callers before trusting it's live - `KnowledgeMemory` looked complete but had
   zero callers. Same pattern found again in `LilyAiCore`: `post_webhook()`.
4. For anything that looks like a shared/duplicate concept across domains, check both before building
   either further - `KnowledgeMemory` vs Rag's `learned:qa` promotion was exactly this. (A near-miss in
   `LilyAiCore`: `chunk_for_discord` vs `split_reply` looked like a possible duplicate but turned out to be
   clean layering - check before assuming duplication too.)
5. Check write frequency, not just write existence - a real, wired write path can still be an unbounded-growth
   risk if nothing caps it. Found in three different shapes so far: a DB table (`learning_events`), and
   in-memory per-user dicts/sets (`RateLimiter._hits`, `SessionManager._locks`, `FeedbackHandler._rated`) -
   both count, and both need the same "cap it, evict the oldest" treatment.
6. Compare the directory against the **live** repo's docs, not a locally mounted/cached copy that may be
   stale - confirm a claim actually exists in the current file before treating it as a gap to fix.
7. Not every gap needs code built to close it - some are better resolved by fixing the doc's claim instead
   of building unrequested scope, and some orphans are fine to just leave alone if that's the call made.
8. Report findings, get a decision, then act - never restructure a domain without that go-ahead.
