# Development

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v      # no network or keys needed
python -m LilyAiMain.main                    # runs bot + API
```

Rules: put a feature in the domain that owns it; no business logic in `LilyAiCore`; no slash commands.
Each domain exposes a `service.py` facade; keep other domains on that surface.

Environment variables are documented in `.env.example`.
