def format_tool_hint(tool_schemas: list[dict]) -> str:
    if not tool_schemas:
        return ""
    names = ", ".join(t["function"]["name"] for t in tool_schemas)
    return f"Tools available: {names}."
