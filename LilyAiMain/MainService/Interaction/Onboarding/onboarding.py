from LilyAiLearning.MemoryLearning.memory_learning import is_safe_fact
from LilyAiMain.MainService.Interaction.Forms.forms import FormDef, FormManager, FormStep
from LilyAiMain.MainService.Interaction.Polls.polls import Poll, PollManager
from LilyAiMemory.service import MemoryService

STYLES = ["Casual and chatty", "Short and to the point", "Detailed and thorough"]
STYLE_FACTS = [
    "Prefers casual, chatty replies",
    "Prefers short, to-the-point replies",
    "Prefers detailed, thorough replies",
]


def _clean_name(text: str) -> str | None:
    name = " ".join(text.strip().split())
    return name[:40] if 1 <= len(name) <= 40 and is_safe_fact(name) else None


class OnboardingFlow:
    """First-contact setup: a short form (name) followed by a poll (reply style).

    needs_onboarding() below treats "has any saved fact or conversation turn" as the sole
    signal that setup is done. That means every exit path here - answer, skip, or cancel, at
    either step - must write at least one fact, or a user who skips/cancels their way through
    gets silently reset to "needs onboarding" and re-prompted forever. on_cancel/on_skip exist
    specifically to close that gap: they're wired to the same completion logic as a normal
    answer, just with a "no name given" / "no style picked" fallback.
    """

    def __init__(self, memory: MemoryService, forms: FormManager, polls: PollManager):
        self.memory, self.forms, self.polls = memory, forms, polls

    def needs_onboarding(self, user_id: str) -> bool:
        return self.memory.conversation.count(user_id) == 0 and not self.memory.user.list(user_id)

    def start(self, user_id: str) -> str:
        form = FormDef(
            "onboarding",
            [FormStep(
                "name", "Hey, I'm Lily! What should I call you? (or say 'skip')",
                _clean_name, skippable=True,
            )],
            on_complete=self._after_form,
            on_cancel=self._after_form,  # cancelling the name step must still reach a terminal state
        )
        return self.forms.start(user_id, form)

    def _after_form(self, user_id: str, answers: dict[str, str]) -> str:
        name = answers.get("name")
        if name:
            self.memory.user.add(user_id, f"User's name is {name}", source="onboarding")
        greeting = f"Nice to meet you, {name}!" if name else "Hey there!"
        poll = Poll(f"{greeting} How do you like replies?", STYLES, self._on_style, on_skip=self._on_style_skip)
        return self.polls.start(user_id, poll)

    def _on_style(self, user_id: str, idx: int, option: str) -> str:
        self.memory.user.add(user_id, STYLE_FACTS[idx], source="onboarding")
        return "Got it. Ask me anything, or say \"help\" to see what I can do."

    def _on_style_skip(self, user_id: str) -> str:
        # No style preference recorded, but still a real fact - this is what actually stops
        # needs_onboarding() from firing again on the user's next message.
        self.memory.user.add(user_id, "Completed onboarding without picking a reply-style preference", source="onboarding")
        return "No worries. Ask me anything, or say \"help\" to see what I can do."
