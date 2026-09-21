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

## Scheduled jobs

`Interaction/Workflows/scheduler.py` runs named async jobs in-process. The only job today is the Groq model scan
(`model_scan_job.py`): it feeds `LilyAiLearning/Evaluation/model_scan.py`, which grows the shared `ModelPool` and writes
`LilyAiGroqSupport/MODEL_CATALOG.md`. It is disabled with `MODEL_SCAN_ENABLED=false` and never runs on the offline provider.

## Frontend

See `LilyAiFrontend/README.md`: modular ES modules, one folder per page, shared components in `Shared/components/`, all pages registered in `Shared/routes.js`, styling tokens in `Assets/styles/tokens.css`.

## Additions to the README scaffold

- `LilyAiMain/MainService/Api/` - FastAPI server; also serves the web client (`static.py`) so one URL is the site
- `LilyAiMain/MainService/bootstrap.py`, `Interaction/messages.py` - wiring and shared message types
- `Interaction/Workflows/scheduler.py`, `model_scan_job.py` - scheduled model scan
- `service.py` facade in each domain root; `tests/`; root `Dockerfile` and `render.yaml` (one service for bot, API and website)
