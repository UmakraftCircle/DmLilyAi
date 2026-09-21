# LilyAi

LilyAi is a modular AI agent platform built with Python and powered by Groq.

The project is designed around independent intelligence domains that separate memory, context, knowledge retrieval, web retrieval, learning, and tool execution.

LilyAi primarily operates through Discord Direct Messages and includes a web administration interface for testing, monitoring, and development.

---

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                   # add GROQ_API_KEY, DISCORD_TOKEN, ADMIN_TOKEN
python -m LilyAiMain.main                              # bot + API + website on http://localhost:8000
```

Open **http://localhost:8000**: the website is served by the same process as the bot. In **Settings**, enter your `ADMIN_TOKEN` (from `.env`).

No keys yet? Leave them empty: the API and DM Simulator run against an offline provider so you can explore the flow.
Run the tests with `python -m unittest discover -s tests -v`.

**Discord setup:** create an application at discord.com/developers, add a bot, enable **Message Content Intent**, copy the token into `DISCORD_TOKEN`, then DM the bot (no server or slash commands needed).

---

## Vision

LilyAi is designed to be:

- Modular
- Provider agnostic
- Infrastructure agnostic
- Maintainable
- Extensible
- DM-first

The goal is to ensure that LilyAi owns its intelligence while external systems remain replaceable.

---

## Features

**Discord Direct Messages** - DM-first interaction, no slash commands, conversation management, user session management

**Web Search** - internet search, content extraction, source processing

**Memory** - user memory, conversation memory, session memory

**Knowledge Retrieval** - document ingestion, embeddings, vector search, Retrieval-Augmented Generation (RAG)

**Learning** - feedback collection, memory learning, knowledge learning, evaluation workflows

**Tools** - tool execution, utility actions, Discord actions

**Frontend** - chat interface, dashboard, settings, relay, DM simulator

---

## Technology Stack

| Layer | Choice |
|-------|--------|
| Language | Python |
| AI Provider | Groq (free-tier models) |
| Platform | Discord |
| Deployment | Docker, Render |

---

## Architecture Philosophy

LilyAi is built using a domain-first architecture. Instead of organizing code by technology, LilyAi organizes code by responsibility.

Benefits: easier maintenance, testing, onboarding and scalability; lower coupling; better long-term stability.

---

## Core Domains

| Domain | Responsible for |
|--------|-----------------|
| LilyAiContext | what LilyAi sees |
| LilyAiMemory | what LilyAi remembers |
| LilyAiTool | what LilyAi can do |
| LilyAiWeb | what LilyAi finds online |
| LilyAiRag | what LilyAi knows |
| LilyAiLearning | how LilyAi improves |

---

## Project Structure

```
LilyAi/
├── LilyAiDocs/
├── LilyAiGroqSupport/
├── LilyAiMain/
├── LilyAiContext/
├── LilyAiMemory/
├── LilyAiTool/
├── LilyAiWeb/
├── LilyAiRag/
├── LilyAiLearning/
├── LilyAiCore/
└── LilyAiFrontend/
```

See `LilyAiDocs/Architecture/` for the detailed scaffold, layers and ownership model.

---

## Interaction Flow

```
Discord DM  (or DM Simulator / Chat via the API)
      │
      ▼
LilyAiMain  ── middleware → session lock → router
      │
      ▼
Interaction Layer  (onboarding, forms, polls, menus, feedback, workflows)
      │
      ▼
Core Domains
      ├── Context   builds the prompt
      ├── Memory    user facts, history, sessions
      ├── Rag       document knowledge
      ├── Web       search + page reading (as tools)
      ├── Tool      registry, validation, execution
      └── Learning  feedback, fact extraction, evaluation
      │
      ▼
LilyAiCore  (Groq provider, database, search, config, logging)
```

---

## Frontend Features

**Relay** - connect to a live Discord bot for monitoring, debugging and testing.

**DM Simulator** - simulate Discord conversations without Discord, for prompt, memory, RAG, tool and workflow testing.

---

## Documentation

**LilyAiDocs** - project-wide documentation: Architecture, Development, Deployment, API, Guides.

**LilyAiGroqSupport** - Groq-specific notes: prompting notes, benchmarks, experiments, provider limitations.

---

## Development Rules

- Python-first
- Domain-first architecture
- No business logic inside infrastructure
- No business logic inside providers
- No slash command dependency
- DM-first design
- Modular development

---

## Future Expansion

Potential future domains: LilyAiVoice, LilyAiVision, LilyAiMobile, LilyAiAnalytics, added without modifying existing domains.

---

## License

MIT License
