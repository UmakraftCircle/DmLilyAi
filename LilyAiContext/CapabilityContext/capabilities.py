"""What Lily can actually do, written for the model.

Why this exists: a chat model only knows a capability if the prompt says so. Without this Lily
answered "I don't have a way to see which trainer is linked" to a user who HAD linked one, then
improvised other ways to do it. Two things fix that:

1. Explicit rules for claiming / denying abilities, plus the DM actions a user can trigger
   (format_capabilities).
2. Live account state (account_status_note), so facts like "is this user linked" sit in the prompt
   instead of depending on the model choosing to call a tool.

DM_ACTIONS must stay in sync with the intent patterns in
LilyAiMain/MainService/Discord/Router/router.py; tests/test_dm_capabilities.py checks the examples
against those patterns so the two can't drift silently.
"""

# (example phrases the user can say, what happens)
DM_ACTIONS: tuple[tuple[str, str], ...] = (
    ('"help" or "menu"', "shows the menu of what Lily can do"),
    ('"link me" or "my trainer id is 123456789"', "links the user's uma.moe Trainer ID to their Discord account"),
    ('"unlink me"', "removes that link"),
    ('"what\'s my trainer id" or "am I linked?"', "tells the user which Trainer ID is linked to them"),
    ('"remember that ..."', "saves a fact about the user"),
    ('"what do you remember about me"', "lists the facts saved about the user"),
    ('"forget everything about me"', "erases saved facts and chat history (asks for confirmation first)"),
    ('"set me up again"', "redoes the first-time setup questions"),
)

CAPABILITY_RULES = """Your abilities - what you can and can't do:
- Your real abilities are exactly the tools listed under "Tools available" and the DM actions below. Nothing else.
- Before saying you can't do something, or asking the user for information, check both lists and the "Account status" note. If a tool or DM action covers the request, use the tool or tell the user the exact words that trigger the action.
- If the request needs something that isn't on either list, say plainly that you can't do that and offer the closest thing you can do. Never invent a command, page, setting or workaround.
- Tool results and the Account status note are ground truth about the user's account. Never guess account data such as a Trainer ID.
- If an earlier message of yours said you couldn't do something these lists say you can, correct yourself."""


def format_capabilities(tool_schemas: list[dict] | None = None) -> str:
    lines = [CAPABILITY_RULES]
    if not tool_schemas:
        lines.append("\nYou have no tools available right now, so you can't look anything up or run actions.")
    lines.append(
        "\nDM actions (handled before a message reaches you - the user triggers them by saying the phrase; "
        "you can't run them yourself, but you can tell the user exactly what to say):"
    )
    lines.extend(f"- {examples}: {what}" for examples, what in DM_ACTIONS)
    return "\n".join(lines)


def account_status_note(trainer_id: str | None = None, trainer_name: str | None = None) -> str:
    """One line of live account state for the prompt: is this Discord user linked to a Trainer ID?"""
    if trainer_id:
        name = f" ({trainer_name})" if trainer_name else ""
        return (
            f"Account status: this Discord user IS linked to uma.moe Trainer ID {trainer_id}{name}. "
            "If they ask which trainer is linked, or whether they're linked, answer with that ID directly - "
            "don't say you can't see it and don't ask them to repeat it. For their own stats or fan gain, "
            f"look them up by this Trainer ID (trainer_id=\"{trainer_id}\") with a lookup tool if you have one, "
            "rather than asking for their name."
        )
    return (
        "Account status: this Discord user is NOT linked to a uma.moe Trainer ID yet. If they ask about their own "
        'trainer, tell them to say "link me" or "my trainer id is <digits>" to link one.'
    )
