# Module Roadmap: the 6 Intelligence Domains

Purpose: track audit status and build order for Context, Memory, Tool, Web, Rag, Learning, so future
work on any one of them starts from a known state instead of re-discovering it. Update this file
whenever a domain gets audited or a listed gap gets resolved.

## Status - all 6 domains audited, docs aligned

| Domain | Status | Summary |
|---|---|---|
| **LilyAiContext** | ✅ Audited | 7 submodules, all wired via `ContextBuilder/builder.py`. No orphans, no doc gaps. |
| **LilyAiMemory** | ✅ Audited + cleaned | 6 submodules (was 7). `KnowledgeMemory` retired - dead write path, fully duplicated by Rag's `learned:qa` promotion. `ConversationMemory` now capped (500 turns/user), matching `UserMemory`'s existing 200-fact cap. |
| **LilyAiRag** | ✅ Audited | Fully wired: Document -> Chunking -> Embedding -> VectorStore -> Retrieval -> Ranking. No orphans. `HashingEmbedder` is lexical (word/bigram hashing), not semantic - deliberate zero-cost tradeoff, stated in its own docstring. |
| **LilyAiLearning** | ✅ Audited + fixed | 7 submodules, all real and wired. `LearningStore`'s `learning_events` table now has a per-kind trim (2000 rows/kind) - it was unbounded despite being written on every chat message and every tool call. |
| **LilyAiTool** | ✅ Audited | 6 submodules, all wired: `Executor` runs `Validator.validate_args()` then the handler, catching timeout/`ToolError`/any crash. Added `remind_me` actuator (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. |
| **LilyAiWeb** | ✅ Audited | 5 submodules, all wired via `service.py`'s search -> process -> extract pipeline. `Cache/TTLCache` confirmed genuinely used. `Sources.is_safe_url` checked twice in the extractor (pre-fetch and post-redirect) - real SSRF guard. Added `/api/web/search` + Settings web card. |

## Docs alignment pass - done

Checked the **live** `README.md` and `Architecture/overview.md` on GitHub (not the local mounted copy some of
this audit was originally compared against): neither actually contains the `PostgreSQL`/`VectorStorage`/
`Chroma`/`FAISS`/`Qdrant`/`DataTools` claims that were flagged during the domain audits - `README.md` only
lists top-level domain folders and defers detail to `overview.md`, and `overview.md` is a high-level
architecture doc that never went into that level of subfolder detail either. So there was nothing false to
remove from the live docs.

What `overview.md` *did* need: everything built this session was missing from it. Added:
- Multi-key `GROQ_API_KEY` rotation (shuffled-bag `KeyRotator`, auto-switch on 429)
- The `remind_me` actuator and the `NotifierBox` seam behind it (`LilyAiCore/ExternalServices/Discord/notifier.py`)
- `MODEL_SCAN_INTERVAL_SECONDS` override for sub-hour model-scan intervals
- The `KnowledgeMemory` removal and why (duplicated Rag's `learned:qa` promotion)
- The new unbounded-growth guards (`ConversationMemory`, `learning_events`)
- The Settings web card / `/api/web/search`
- A pointer to this file, so `overview.md` readers can find current per-domain audit status

`README.md` needed no edits - confirmed accurate as-is.

## Repeatable audit process (used for all 6 domains - reuse for any future domain, e.g. LilyAiVoice/Vision)

1. `view`/list the domain's directory - confirm every documented subfolder actually exists.
2. Read `service.py` (the facade) - it shows which submodules are actually wired together.
3. For anything that looks like a write path (a `.add()`, an `.ingest()`, a table insert), code-search
   the whole repo for real callers before trusting it's live - `KnowledgeMemory` looked complete but had
   zero callers.
4. For anything that looks like a shared/duplicate concept across domains, check both before building
   either further - `KnowledgeMemory` vs Rag's `learned:qa` promotion was exactly this.
5. Check write frequency, not just write existence - a real, wired write path can still be an unbounded-growth
   risk if nothing caps it (`learning_events` - written on every message/tool call, now trimmed per-kind).
6. Compare the directory against the **live** repo's docs, not a locally mounted/cached copy that may be
   stale - confirm a claim actually exists in the current file before treating it as a gap to fix.
7. Not every gap needs code built to close it - some are better resolved by fixing the doc's claim instead
   of building unrequested scope (this is why `DataTools/` was left alone: it wasn't actually claimed by the
   live docs in the first place).
8. Report findings, get a decision, then act - never restructure a domain without that go-ahead.

## Status: roadmap complete

All 6 domains audited, all found issues fixed or documented, docs aligned with reality. No open items.
