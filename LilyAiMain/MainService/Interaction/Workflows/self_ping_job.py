"""Scheduled job: ping the service's own /api/health endpoint so a free-tier host
(e.g. Render's free plan, which spins down a web service after ~15 minutes of no
inbound traffic) sees regular traffic and doesn't put it to sleep.
"""
import httpx

from LilyAiCore.Logging.logger import get_logger

log = get_logger("self_ping_job")


def make_self_ping_job(url: str):
    async def run() -> None:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(url)
            log.info("self-ping %s -> %d", url, resp.status_code)
        except Exception as e:
            # Don't let a transient network blip look like a real failure to the
            # scheduler (which would fire the ops webhook) - just log and retry
            # on the next interval.
            log.warning("self-ping to %s failed: %r", url, e)

    return run
