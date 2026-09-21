# Deployment

One Render web service runs everything: the Discord bot, the API and the website. **The Render URL is the website.**

1. Push the repo, then create a Blueprint from the root `render.yaml` (or a Docker web service using the root `Dockerfile`).
2. Set `GROQ_API_KEY` and `DISCORD_TOKEN`. `ADMIN_TOKEN` is generated: copy it from the service's environment tab.
3. Open the Render URL, go to **Settings**, paste the admin token, then **Save and test**.

**Updating the site:** edit files in `LilyAiFrontend/`, push to git, Render redeploys. There is no build step. The server tells browsers to revalidate on every load, so changes show up on the next refresh.

**Keep-alive:** point your pinger at `GET /api/health` (HEAD works too). Free Render web services sleep when idle, which also disconnects the Discord bot.

**Persistence:** the free plan's filesystem is ephemeral, so memory, feedback, the RAG index and model-scan state reset on redeploy. Attach a disk on a paid plan (commented block in `render.yaml`).

**Security:** the pages are public, but every API call needs `ADMIN_TOKEN`. Keep it secret. Without `ADMIN_TOKEN` the API only answers localhost.
