"""Link a Discord user to their uma.moe Trainer ID.

Triggered by phrases like "link me" (see the _LINK pattern in
LilyAiMain/MainService/Discord/Router/router.py). Reuses the same
one-question FormManager flow as onboarding - there's no Discord UI
modal in this bot; DMs are plain text, so a "form" here is just a
short back-and-forth.

Once linked, LilyAiTask/DailyTask/DeficitTask/Deficit.py can DM this
user their daily fan-gain quota report.
"""
from LilyAiMain.MainService.Interaction.Forms.forms import FormDef, FormManager, FormStep
from LilyAiMemory.service import MemoryService

_MIN_LEN, _MAX_LEN = 5, 15


def _clean_trainer_id(text: str) -> str | None:
    """Trainer IDs are numeric (uma.moe viewer_id); allow commas/spaces like '123,456,789'."""
    digits = "".join(ch for ch in text.strip() if ch.isdigit())
    if _MIN_LEN <= len(digits) <= _MAX_LEN:
        return digits
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

    def _after_form(self, user_id: str, answers: dict[str, str]) -> str:
        trainer_id = answers["trainer_id"]
        self.memory.trainer_link.link(user_id, trainer_id)
        return (
            f"You're linked! Trainer ID `{trainer_id}` is now tied to your Discord account, "
            "so I can DM you your daily fan quota reports."
        )
