# HTTP API

All routes except `/api/health` need `Authorization: Bearer <ADMIN_TOKEN>` (or a localhost caller when no token is set).

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/health` | liveness + Discord status |
| POST | `/api/chat` | `{text, user_id, source: web\|simulator}` -> `{messages: [...]}` (same router as Discord) |
| POST | `/api/feedback` | `{user_id, reply_id, rating: 1\|-1}` |
| GET/DELETE | `/api/memory/{user_id}` | inspect / wipe a user |
| GET | `/api/relay/events?after=&source=` | event feed for the Relay |
| GET | `/api/dashboard` | stats, learning report |
| GET | `/api/config` | model pool and non-secret settings |
| POST | `/api/rag/ingest`, `/api/rag/search` | knowledge base |
| DELETE | `/api/rag/sources/{source}` | remove a source |
| GET/POST | `/api/models/scan` | model auto-scan status / run a scan now |
| POST | `/api/eval/run` | run built-in evaluation cases |

Interactive docs: `/docs`. Every other path serves the web client (`LilyAiFrontend/`), so the same URL is the website.
