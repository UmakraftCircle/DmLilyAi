import time
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Callable

DEFAULT_TTL_SECONDS = 15 * 60


@dataclass
class Poll:
    question: str
    options: list[str]
    on_pick: Callable[[str, int, str], str]  # (user_id, index, option) -> reply
    on_skip: Callable[[str], str] | None = None
    """Called instead of the generic 'Skipped.' message when the user skips/cancels this
    poll. Set it for flows that must reach a terminal, persisted outcome no matter how the
    user exits (see OnboardingFlow) - leave unset for a poll where skipping has no
    consequences beyond not answering."""

    def render(self) -> str:
        lines = [self.question, ""] + [f"{i}. {o}" for i, o in enumerate(self.options, 1)]
        return "\n".join(lines) + "\n\nReply with a number (or 'skip')."


@dataclass
class _PollRun:
    poll: Poll
    touched_at: float = field(default_factory=time.time)


class PollManager:
    """Quick-pick questions: the user answers with a number or the option text.

    Idle polls expire after ttl_seconds and the store is capped at max_active (LRU) - same
    pattern as FormManager - so an abandoned or flooded set of started polls can't grow
    memory without bound.
    """

    def __init__(self, max_active: int = 500, ttl_seconds: float = DEFAULT_TTL_SECONDS):
        self.max_active, self.ttl_seconds = max_active, ttl_seconds
        self._polls: OrderedDict[str, _PollRun] = OrderedDict()

    def start(self, user_id: str, poll: Poll) -> str:
        self._prune_expired()
        self._polls[user_id] = _PollRun(poll)
        self._polls.move_to_end(user_id)
        while len(self._polls) > self.max_active:
            self._polls.popitem(last=False)
        return poll.render()

    def active(self, user_id: str) -> bool:
        self._expire_one(user_id)
        return user_id in self._polls

    def cancel(self, user_id: str) -> None:
        self._polls.pop(user_id, None)

    def answer(self, user_id: str, text: str) -> tuple[str, bool]:
        run = self._polls[user_id]
        run.touched_at = time.time()
        self._polls.move_to_end(user_id)
        poll = run.poll
        t = text.strip().lower().rstrip(".)")

        if t in {"skip", "cancel", "stop"}:
            self._polls.pop(user_id, None)
            if poll.on_skip:
                return poll.on_skip(user_id), True
            return "Skipped. You can always tell me later.", True

        idx = None
        if t.isdigit() and 1 <= int(t) <= len(poll.options):
            idx = int(t) - 1
        else:
            for i, o in enumerate(poll.options):
                if t == o.lower():
                    idx = i
        if idx is None:
            return f"Pick a number from 1 to {len(poll.options)} (or 'skip').", False
        self._polls.pop(user_id, None)
        return poll.on_pick(user_id, idx, poll.options[idx]), True

    def _expire_one(self, user_id: str) -> None:
        run = self._polls.get(user_id)
        if run and time.time() - run.touched_at > self.ttl_seconds:
            del self._polls[user_id]

    def _prune_expired(self) -> None:
        now = time.time()
        while self._polls:
            uid, run = next(iter(self._polls.items()))
            if now - run.touched_at <= self.ttl_seconds:
                break
            del self._polls[uid]
