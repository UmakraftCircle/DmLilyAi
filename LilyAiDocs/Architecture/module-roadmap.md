# Module Roadmap: the 6 Intelligence Domains

Purpose: track audit status and build order for Context, Memory, Tool, Web, Rag, Learning, so future
work on any one of them starts from a known state instead of re-discovering it. Update this file
whenever a domain gets audited or a listed gap gets resolved.

## Status - all 6 domains audited

| Domain | Status | Summary |
|---|---|---|
| **LilyAiContext** | ✅ Audited | 7 submodules, all wired via `ContextBuilder/builder.py`. No orphans, no doc gaps. |
| **LilyAiMemory** | ✅ Audited + cleaned | 6 submodules (was 7). `KnowledgeMemory` retired - dead write path, fully duplicated by Rag's `learned:qa` promotion. `ConversationMemory` now capped (500 turns/user), matching `UserMemory`'s existing 200-fact cap. |
| **LilyAiRag** | ✅ Audited | Fully wired: Document -> Chunking -> Embedding -> VectorStore -> Retrieval -> Ranking. No orphans. Two things to know, not bugs: (1) doc gap - `VectorStore/Chroma,FAISS,Qdrant` are documented, not built; it's one JSON-backed in-memory store. (2) `HashingEmbedder` is lexical (word/bigram hashing), not semantic - deliberate zero-cost tradeoff, stated in its own docstring. |
| **LilyAiLearning** | ✅ Audited + fixed | 7 submodules, all real and wired (Evaluation is wired directly from bootstrap/server rather than through the `LearningService` facade - fine, probing is naturally decoupled from per-message learning). `LearningStore`'s `learning_events` table now has a per-kind trim (2000 rows/kind) - it was unbounded despite being written on every chat message and every tool call. |
| **LilyAiTool** | ✅ Audited | 6 submodules (Registry, Executor, Validator, DiscordTools, UtilityTools, Models), all wired: `Executor` runs `Validator.validate_args()` then the handler, catching timeout/`ToolError`/any crash so a bad tool never breaks the chat loop. Added `remind_me` actuator this cycle (`NotifierBox` + Discord `send_dm`) - first real action, not just read/reply. Open doc gap: `DataTools/` is documented, not built - decision: don't build speculatively, reframe as Future Expansion in the docs pass below rather than leave it claiming to be existing structure. |
| **LilyAiWeb** | ✅ Audited | 5 submodules, all wired via `service.py`'s search -> process -> extract pipeline. `Cache/TTLCache` (15min search / 30min doc TTL, 256-item cap) is genuinely used - the "unconfirmed" item from the last pass turns out to be a non-issue. `Sources.is_safe_url` (blocks localhost/private-IP/link-local) is checked twice in the extractor - pre-fetch and post-redirect, guarding against SSRF via redirect. Added `/api/web/search` + Settings web card this cycle, so it has frontend parity with the other 5 domains. |

## Remaining work

1. **Docs alignment pass** (the only item left): update `README.md` and `Architecture/overview.md` in one pass:
   - Remove: `PostgreSQL`/`VectorStorage` backends (Memory/Rag), `Chroma`/`FAISS`/`Qdrant` (Rag), `KnowledgeMemory` (Memory)
   - Reframe: `DataTools/` (Tool) -> move to the README's existing "Future Expansion" section instead of "Complete Project Structure"
   - Add: multi-key Groq rotation, `remind_me` actuator, model-scan seconds override, `learning_events` trim, `/api/web/search` + Settings web card

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
6. Compare the directory against the README's documented structure; note gaps, don't silently "fix" the
   docs or the code without flagging the gap first. Not every gap needs code built to close it - some
   (like `DataTools/`) are better resolved by fixing the doc's claim instead of building unrequested scope.
7. Report findings, get a decision, then act - never restructure a domain without that go-ahead.
