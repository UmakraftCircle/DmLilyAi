"""LilyAi entry point.  Run from the repo root:  python -m LilyAiMain.main"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiCore.Config.settings import load_settings  # noqa: E402
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
            tasks["discord"] = asyncio.create_task(client.start(settings.discord_token), name="discord")
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
