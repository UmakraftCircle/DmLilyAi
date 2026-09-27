import time
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Callable

DEFAULT_TTL_SECONDS = 15 * 60


@dataclass
class FormStep:
    key: str
    prompt: str
    clean: Callable[[str], str | None]  # returns cleaned value or None if invalid
    error: str = "Sorry, I didn't catch that. Try again?"
    skippable: bool = False
    skip_value: str | None = None  # stored under `key` when skipped; None leaves the key unset


@dataclass
class FormDef:
    id: str
    steps: list[FormStep]
    on_complete: Callable[[str, dict[str, str]], str]
    on_cancel: Callable[[str, dict[str, str]], str] | None = None
    """Called (with whatever answers were collected so far) instead of the generic cancel
    message when the user types 'cancel'/'stop' mid-form. Leave unset for forms where
    cancelling should simply abandon the flow with no side effects (e.g. link_trainer - if you
    bail out of linking your Trainer ID, there's nothing left to finish). Set it for flows that
    must reach a terminal, persisted state no matter how the user exits, so they aren't
    re-prompted forever - see OnboardingFlow, which points this at the same handler as
    on_complete."""


@dataclass
class _Run:
    form: FormDef
    index: int = 0
    answers: dict[str, str] = field(default_factory=dict)
    touched_at: float = field(default_factory=time.time)


class FormManager:
    """Step-by-step DM questionnaires.

    'skip' moves past the current step only if that step's FormStep.skippable allows it;
    'cancel'/'stop' always ends the whole form (see FormDef.on_cancel for what happens then).

    Idle runs expire after ttl_seconds and the store is capped at max_active (LRU) - same
    pattern as SessionManager/RateLimiter/ReplyLog - so a user who starts a form and never
    finishes it doesn't leak memory forever, and a burst of distinct users doing the same
    can't grow this dict without bound.
    """

    def __init__(self, max_active: int = 500, ttl_seconds: float = DEFAULT_TTL_SECONDS):
        self.max_active, self.ttl_seconds = max_active, ttl_seconds
        self._runs: OrderedDict[str, _Run] = OrderedDict()

    def start(self, user_id: str, form: FormDef) -> str:
        self._prune_expired()
        self._runs[user_id] = _Run(form)
        self._runs.move_to_end(user_id)
        while len(self._runs) > self.max_active:
            self._runs.popitem(last=False)
        return form.steps[0].prompt

    def active(self, user_id: str) -> bool:
        self._expire_one(user_id)
        return user_id in self._runs

    def cancel(self, user_id: str) -> None:
        self._runs.pop(user_id, None)

    def submit(self, user_id: str, text: str) -> tuple[str, bool]:
        run = self._runs[user_id]
        run.touched_at = time.time()
        self._runs.move_to_end(user_id)
        t = text.strip().lower()
        step = run.form.steps[run.index]

        if t in {"cancel", "stop"}:
            self._runs.pop(user_id, None)
            if run.form.on_cancel:
                return run.form.on_cancel(user_id, run.answers), True
            return "No problem, I've cancelled that.", True

        if t == "skip":
            if not step.skippable:
                return "This one can't be skipped - go ahead and answer it, or say 'cancel'.", False
            if step.skip_value is not None:
                run.answers[step.key] = step.skip_value
            return self._advance(user_id, run)

        value = step.clean(text)
        if value is None:
            return step.error, False
        run.answers[step.key] = value
        return self._advance(user_id, run)

    def _advance(self, user_id: str, run: _Run) -> tuple[str, bool]:
        run.index += 1
        if run.index < len(run.form.steps):
            return run.form.steps[run.index].prompt, False
        self._runs.pop(user_id, None)
        return run.form.on_complete(user_id, run.answers), True

    def _expire_one(self, user_id: str) -> None:
        run = self._runs.get(user_id)
        if run and time.time() - run.touched_at > self.ttl_seconds:
            del self._runs[user_id]

    def _prune_expired(self) -> None:
        """Opportunistic sweep from the front of the LRU order (oldest-touched first) so
        memory is reclaimed from idle runs even if nobody happens to query them again."""
        now = time.time()
        while self._runs:
            uid, run = next(iter(self._runs.items()))
            if now - run.touched_at <= self.ttl_seconds:
                break
            del self._runs[uid]
