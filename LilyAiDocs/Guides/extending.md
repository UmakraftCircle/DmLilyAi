# Guides

**Add a tool** - create a `ToolSpec(name, description, JSON-schema parameters, handler)` in `LilyAiTool/UtilityTools/` (or `DiscordTools/`)
and add it to the list returned there. Handlers receive `(ToolContextData, args)` and may be sync or async. Arguments are validated before the call.
Tools that need another domain (like `web_search`) are registered in `bootstrap.py`.

**Swap the LLM provider** - implement `LLMProvider` (`LilyAiCore/Providers/base.py`) and pass it to `build_app`.

**Swap search** - implement `SearchProvider` (`LilyAiCore/ExternalServices/Search/base.py`).

**Better embeddings** - implement `Embedder` (`LilyAiRag/Embedding/embedder.py`). The default hashing embedder is local and free but only matches on shared words; delete `data/rag_index.json` after switching.

**Load documents at startup** - `RagService.ingest_path("docs/")` accepts a file or folder of `.md/.txt` files.
