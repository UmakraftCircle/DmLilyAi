from LilyAiMain.MainService.Interaction.messages import MenuItem

HELP_TEXT = (
    "Hi, I'm Lily. Just talk to me like a normal chat, no commands needed.\n\n"
    "I can search the web, do exact math, remember things you tell me "
    "(say \"remember that ...\"), and answer from documents I've been given.\n"
    "Ask \"what do you remember about me?\" any time, or \"forget everything\" to wipe it."
)


def main_menu() -> list[MenuItem]:
    return [
        MenuItem("What do you remember?", "What do you remember about me?"),
        MenuItem("Forget everything", "Forget everything about me"),
        MenuItem("Redo setup", "Set me up again"),
    ]
