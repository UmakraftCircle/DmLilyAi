import httpx

from LilyAiCore.Logging.logger import get_logger

log = get_logger("webhook")


async def post_webhook(url: str, content: str) -> bool:
    """Fire-and-forget webhook for ops alerts."""
    if not url:
        return False
    try:
        async with httpx.AsyncClient(timeout=10) as http:
            r = await http.post(url, json={"content": content[:1900]})
        return r.status_code < 300
    except httpx.HTTPError as e:
        log.warning("webhook failed: %s", e)
        return False
