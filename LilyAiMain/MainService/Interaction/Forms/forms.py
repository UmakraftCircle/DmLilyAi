from dataclasses import dataclass, field
from typing import Callable


@dataclass
class FormStep:
    key: str
    prompt: str
    clean: Callable[[str], str | None]  # returns cleaned value or None if invalid
    error: str = "Sorry, I didn't catch that. Try again?"


@dataclass
class FormDef:
    id: str
    steps: list[FormStep]
    on_complete: Callable[[str, dict[str, str]], str]


@dataclass
class _Run:
    form: FormDef
    index: int = 0
    answers: dict[str, str] = field(default_factory=dict)


class FormManager:
    """Step-by-step DM questionnaires. Type 'cancel' or 'skip' to leave one."""

    def __init__(self):
        self._runs: dict[str, _Run] = {}

    def start(self, user_id: str, form: FormDef) -> str:
        self._runs[user_id] = _Run(form)
        return form.steps[0].prompt

    def active(self, user_id: str) -> bool:
        return user_id in self._runs

    def cancel(self, user_id: str) -> None:
        self._runs.pop(user_id, None)

    def submit(self, user_id: str, text: str) -> tuple[str, bool]:
        run = self._runs[user_id]
        if text.strip().lower() in {"cancel", "skip", "stop"}:
            self.cancel(user_id)
            return "No problem, we can skip that.", True
        step = run.form.steps[run.index]
        value = step.clean(text)
        if value is None:
            return step.error, False
        run.answers[step.key] = value
        run.index += 1
        if run.index < len(run.form.steps):
            return run.form.steps[run.index].prompt, False
        self._runs.pop(user_id, None)
        return run.form.on_complete(user_id, run.answers), True
