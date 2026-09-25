"""Minimal in-process scheduler: named async jobs that run every N seconds."""
import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable

from LilyAiCore.ExternalServices.Webhooks.webhook import post_webhook
from LilyAiCore.Logging.logger import get_logger

log = get_logger("scheduler")


@dataclass
class Job:
    name: str
    interval_s: float
    fn: Callable[[], Awaitable[None]]
    initial_delay_s: float = 0.0


class Scheduler:
    def __init__(self, webhook_url: str = ""):
        self._jobs: list[Job] = []
        self._tasks: list[asyncio.Task] = []
        self._webhook_url = webhook_url

    def every(self, name: str, interval_s: float, fn: Callable[[], Awaitable[None]], initial_delay_s: float = 0.0) -> None:
        self._jobs.append(Job(name, interval_s, fn, initial_delay_s))

    def start(self) -> None:
        self._tasks = [asyncio.create_task(self._loop(j), name=f"job:{j.name}") for j in self._jobs]

    async def stop(self) -> None:
        for t in self._tasks:
            t.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks = []

    async def _loop(self, job: Job) -> None:
        await asyncio.sleep(job.initial_delay_s)
        while True:
            try:
                await job.fn()
            except asyncio.CancelledError:
                raise
            except Exception as e:
                log.exception("job %s failed", job.name)
                if self._webhook_url:
                    await post_webhook(self._webhook_url, f"⚠️ scheduled job `{job.name}` failed: {e!r}")
            await asyncio.sleep(job.interval_s)
