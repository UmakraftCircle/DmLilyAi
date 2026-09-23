# Module Roadmap: the 6 Intelligence Domains

Purpose: track audit status and build order for Context, Memory, Tool, Web, Rag, Learning, so future
work on any one of them starts from a known state instead of re-discovering it. Update this file
whenever a domain gets audited or a listed gap gets resolved.

## Status

| Domain | Status | Summary |
|---|---|---|
| **LilyAiContext** | ✅ Audited | 7 submodules, all wired via `ContextBuilder/builder.py`. No orphans, no doc gaps. |
| **LilyAiMemory** | ✅ Audited + cleaned | 6 submodules (was 7). `KnowledgeMemory` retired - dead write path, fully duplicated by Rag's `learned:qa` promotion. `ConversationMemory` now capped (500 turns/user), matching `UserMemory`'s existing 200-fact cap. |
| **LilyAiRag** | ✅ Audited | Fully wired: Document -> Chunking -> Embedding -> VectorStore -> Retrieval -> Ranking. No orphans. Two things to know, not bugs: (1) doc gap - `VectorStore/Chroma,FAISS,Qdrant` are documented, not built; it's one JSON-backed in-memory store. (2) `HashingEmbedder` is lexical (word/bigram hashing), not semantic - deliberate zero-cost tradeoff, stated in its own docstring. |
| **LilyAiLearning** | ✅ Audited | 7 submodules, all real and wired (Evaluation is wired directly from bootstrap/server rather than through the `LearningService` facade - fine, probing is naturally decoupled from per-message learning). No orphans, no doc gaps. **Open issue**: `LearningStore`'s `learning_events` table has zero trim, and gets written on every chat message (`context_tokens`) and every tool call (`tool`) - the highest-frequency, least-bounded table in the system. Needs the same kind of cap `ConversationMemory` got. |
| **LilyAiTool** | 🟡 Partial | Added `remind_me` actuator (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. Not yet done: full sweep of `Registry`/`Validator`/`Executor`; open doc gap - `DataTools/` is documented, not built. |
| **LilyAiWeb** | 🟡 Partial | Added `/api/web/search` + Settings web card, so it has frontend parity with the other 5 domains. Not yet done: full sweep; `Cache/` folder's actual usage unconfirmed. |

## Build order from here

1. **Fix `learning_events` growth** - add a trim to `LearningStore`, same pattern as `ConversationMemory`'s cap. Highest-priority open item: it's the fastest-growing unbounded table in the whole system.
2. **`LilyAiTool`** - finish the sweep (`Registry`/`Validator`/`Executor`) and decide `DataTools/`: build it for real, or drop it from the README like `KnowledgeMemory` was dropped from code.
3. **`LilyAiWeb`** - finish the sweep; confirm `Cache/` is wired to `WebService`, or flag it as another gap.
4. **Docs alignment pass** - once all 6 are fully audited, update `README.md` and `Architecture/overview.md` in
   one pass to drop every doc-vs-reality gap found (`PostgreSQL`/`VectorStorage` backends, `Chroma`/`FAISS`/`Qdrant`,
   `DataTools/`) and add what's been built since `overview.md` was last written (multi-key Groq rotation,
   `remind_me` actuator, model-scan seconds override, `learning_events` trim).

## Repeatable audit process (used for Context/Memory/Rag/Learning, use for what's left)

1. `view`/list the domain's directory - confirm every documented subfolder actually exists.
2. Read `service.py` (the facade) - it shows which submodules are actually wired together.
3. For anything that looks like a write path (a `.add()`, an `.ingest()`, a table insert), code-search
   the whole repo for real callers before trusting it's live - `KnowledgeMemory` looked complete but had
   zero callers.
4. For anything that looks like a shared/duplicate concept across domains, check both before building
   either further - `KnowledgeMemory` vs Rag's `learned:qa` promotion was exactly this.
5. Check write frequency, not just write existence - a real, wired write path can still be an unbounded-growth
   risk if nothing caps it (`learning_events` - written on every message/tool call, zero trim).
6. Compare the directory against the README's documented structure; note gaps, don't silently "fix" the
   docs or the code without flagging the gap first.
7. Report findings, get a decision, then act - never restructure a domain without that go-ahead.
