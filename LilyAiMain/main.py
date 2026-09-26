"""LilyAi entry point.  Run from the repo root:  python -m LilyAiMain.main"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.ExternalServices.Webhooks.webhook import post_webhook  # noqa: E402
from LilyAiCore.Logging.logger import get_logger, setup_logging  # noqa: E402
from LilyAiMain.MainService.bootstrap import build_app  # noqa: E402


async def run() -> None:
    settings = load_settings()
    setup_logging(settings.log_level)
    log = get_logger("main")
    app = build_app(settings)

    tasks: dict[str, asyncio.Task] = {}
    server = client = None

    if settings.enable_api:
        import uvicorn

        from LilyAiMain.MainService.Api.server import create_api

        if not settings.admin_token:
            log.warning("ADMIN_TOKEN is not set: the API only accepts requests from localhost")
        server = uvicorn.Server(uvicorn.Config(create_api(app), host=settings.api_host, port=settings.api_port, log_level="warning"))
        tasks["api"] = asyncio.create_task(server.serve(), name="api")
        log.info("API listening on %s:%s", settings.api_host, settings.api_port)

    if settings.enable_discord:
        if settings.discord_token:
            from LilyAiMain.MainService.Discord.Client.client import LilyDiscordClient

            client = LilyDiscordClient(app)
            app.discord_client = client  # lets the API (/api/relay/channel*) reach the live bot for channel listing/watch/send
            app.notifier_box.notifier = client  # actuator online: tools registered earlier (e.g. remind_me) can now reach Discord
            app.notifier_box.resume_pending()  # replay any reminders left over from before a restart/redeploy
            # run_forever() retries with backoff on connect failures (e.g. Cloudflare
            # rate-limit blocks) instead of raising, so a Discord outage can't take
            # the API server down with it via the FIRST_COMPLETED wait below. The backoff
            # itself is persisted via app.discord_reconnect, so a redeploy landing mid-cooldown
            # resumes waiting instead of resetting to the floor and re-triggering the block.
            tasks["discord"] = asyncio.create_task(
                client.run_forever(settings.discord_token, app.discord_reconnect), name="discord"
            )
        else:
            log.warning("DISCORD_TOKEN is not set: Discord is disabled (API and DM Simulator still work)")

    app.scheduler.start()

    if not tasks:
        log.error("Nothing to run: enable the API or provide DISCORD_TOKEN")
        await app.aclose()
        return

    try:
        done, _ = await asyncio.wait(tasks.values(), return_when=asyncio.FIRST_COMPLETED)
        for t in done:
            if t.exception():
                log.error("%s stopped: %r", t.get_name(), t.exception())
                if settings.webhook_url:
                    await post_webhook(settings.webhook_url, f"🚨 LilyAi `{t.get_name()}` task stopped: {t.exception()!r}")
    finally:
        if server:
            server.should_exit = True
        if client:
            await client.close()
        for t in tasks.values():
            t.cancel()
        await asyncio.gather(*tasks.values(), return_exceptions=True)
        await app.aclose()


def main() -> None:
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
