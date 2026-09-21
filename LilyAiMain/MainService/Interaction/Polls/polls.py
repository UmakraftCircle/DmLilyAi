from dataclasses import dataclass
from typing import Callable


@dataclass
class Poll:
    question: str
    options: list[str]
    on_pick: Callable[[str, int, str], str]  # (user_id, index, option) -> reply

    def render(self) -> str:
        lines = [self.question, ""] + [f"{i}. {o}" for i, o in enumerate(self.options, 1)]
        return "\n".join(lines) + "\n\nReply with a number (or 'skip')."


class PollManager:
    """Quick-pick questions: the user answers with a number or the option text."""

    def __init__(self):
        self._polls: dict[str, Poll] = {}

    def start(self, user_id: str, poll: Poll) -> str:
        self._polls[user_id] = poll
        return poll.render()

    def active(self, user_id: str) -> bool:
        return user_id in self._polls

    def cancel(self, user_id: str) -> None:
        self._polls.pop(user_id, None)

    def answer(self, user_id: str, text: str) -> tuple[str, bool]:
        poll = self._polls[user_id]
        t = text.strip().lower().rstrip(".)")
        if t in {"skip", "cancel", "stop"}:
            self.cancel(user_id)
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
