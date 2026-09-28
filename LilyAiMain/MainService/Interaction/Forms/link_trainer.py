"""Link a Discord user to their uma.moe Trainer ID.

Triggered by phrases like "link me" (see the _LINK pattern in
LilyAiMain/MainService/Discord/Router/router.py). Reuses the same
one-question FormManager flow as onboarding - there's no Discord UI
modal in this bot; DMs are plain text, so a "form" here is just a
short back-and-forth.

A user can also skip the question by putting the ID in the sentence ("my trainer id is
123456789", "link me to 123456789") - see try_direct_link - and ask which ID is linked
(status).

Once linked, LilyAiTask/DailyTask/DeficitTask/Deficit.py can DM this
user their daily fan-gain quota report.
"""
import re

from LilyAiMain.MainService.Interaction.Forms.forms import FormDef, FormManager, FormStep
from LilyAiMemory.service import MemoryService

_MIN_LEN, _MAX_LEN = 5, 15

_ID = r"(\d[\d ,]{3,18}\d)"
# "my trainer id is 123456789" / "my uma.moe trainer id: 123,456,789"
# "link me to 123456789" / "link my trainer id 123456789" (but never "unlink ...")
_DIRECT = (
    re.compile(r"\bmy\s+(?:uma\.?moe\s+)?trainer\s*id\s*(?:is|:|=)\s*`?" + _ID, re.I),
    re.compile(r"\b(?<!un)link\s+(?:me|my\s+(?:account|trainer(?:\s*id)?))\s*(?:to|with|as|[:=])?\s*`?" + _ID, re.I),
)


def _clean_trainer_id(text: str) -> str | None:
    """Trainer IDs are numeric (uma.moe viewer_id); allow commas/spaces like '123,456,789'."""
    digits = "".join(ch for ch in text.strip() if ch.isdigit())
    if _MIN_LEN <= len(digits) <= _MAX_LEN:
        return digits
    return None


def extract_trainer_id(text: str) -> str | None:
    """Pull a Trainer ID out of a sentence that clearly states the user's own ID, else None."""
    for pattern in _DIRECT:
        m = pattern.search(text)
        if m:
            return _clean_trainer_id(m.group(1))
    return None


class LinkTrainerFlow:
    """Handles the "link me" DM flow: ask for a Trainer ID, then save the link."""

    def __init__(self, memory: MemoryService, forms: FormManager):
        self.memory, self.forms = memory, forms

    def start(self, user_id: str) -> str:
        existing = self.memory.trainer_link.by_discord_id(user_id)
        note = f" (currently linked to `{existing.trainer_id}` - this will replace it)" if existing else ""
        form = FormDef(
            "link_trainer",
            [FormStep(
                "trainer_id",
                f"What's your uma.moe Trainer ID?{note} (the numeric ID on your uma.moe profile, "
                "or say 'cancel')",
                _clean_trainer_id,
                error="That doesn't look like a Trainer ID - it should be all digits. Try again?",
            )],
            on_complete=self._after_form,
        )
        return self.forms.start(user_id, form)

    def try_direct_link(self, user_id: str, text: str) -> str | None:
        """Link straight from a sentence like "my trainer id is 123456789". None if the text isn't one."""
        trainer_id = extract_trainer_id(text)
        if not trainer_id:
            return None
        existing = self.memory.trainer_link.by_discord_id(user_id)
        if existing and existing.trainer_id == trainer_id:
            return f"You're already linked to Trainer ID `{trainer_id}`."
        self.memory.trainer_link.link(user_id, trainer_id)
        return self._linked_message(trainer_id)

    def status(self, user_id: str) -> str:
        link = self.memory.trainer_link.by_discord_id(user_id)
        if not link:
            return (
                "You're not linked to a Trainer ID yet. Say \"link me\", or just tell me "
                "\"my trainer id is 123456789\"."
            )
        name = f" ({link.trainer_name})" if link.trainer_name else ""
        return f"You're linked to Trainer ID `{link.trainer_id}`{name}."

    def _after_form(self, user_id: str, answers: dict[str, str]) -> str:
        trainer_id = answers["trainer_id"]
        self.memory.trainer_link.link(user_id, trainer_id)
        return self._linked_message(trainer_id)

    @staticmethod
    def _linked_message(trainer_id: str) -> str:
        return (
            f"You're linked! Trainer ID `{trainer_id}` is now tied to your Discord account, "
            "so I can DM you your daily fan quota reports."
        )
