from LilyAiCore.Exceptions.errors import ToolError
from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiTool.Models.tool_models import ToolSpec


def _whoami(ctx, args):
    return f"The user is '{ctx.display_name or 'unknown'}' (Discord id {ctx.user_id or 'unknown'})."


def discord_tools(notifier_box: NotifierBox) -> list[ToolSpec]:
    """Discord-flavoured tools. Kept free of the discord library: they only use ToolContextData."""

    def _remind_me(ctx, args):
        minutes = args["minutes"]
        if not 1 <= minutes <= 1440:
            raise ToolError("minutes must be between 1 and 1440 (24 hours)")
        if not ctx.user_id:
            raise ToolError("no Discord user to remind (not running in a Discord DM)")
        notifier_box.schedule_dm(ctx.user_id, args["message"], minutes * 60)
        return f'Okay, I\'ll DM you in {minutes} minute(s): "{args["message"]}"'

    return [
        ToolSpec(
            "whoami",
            "Get the display name and Discord id of the user you are chatting with.",
            {"type": "object", "properties": {}, "required": []},
            _whoami,
            category="discord",
        ),
        ToolSpec(
            "remind_me",
            "Schedule a Discord DM to be sent to the current user after a delay, unprompted "
            "(a reminder). Use when the user asks to be reminded or notified later.",
            {
                "type": "object",
                "properties": {
                    "minutes": {"type": "number", "description": "Delay before sending, 1-1440 (24h max)."},
                    "message": {"type": "string", "description": "What to remind the user about."},
                },
                "required": ["minutes", "message"],
            },
            _remind_me,
            category="discord",
        ),
    ]
