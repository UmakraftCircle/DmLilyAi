from LilyAiTool.Models.tool_models import ToolSpec


def _whoami(ctx, args):
    return f"The user is '{ctx.display_name or 'unknown'}' (Discord id {ctx.user_id or 'unknown'})."


def discord_tools() -> list[ToolSpec]:
    """Discord-flavoured tools. Kept free of the discord library: they only use ToolContextData."""
    return [
        ToolSpec(
            "whoami",
            "Get the display name and Discord id of the user you are chatting with.",
            {"type": "object", "properties": {}, "required": []},
            _whoami,
            category="discord",
        )
    ]
