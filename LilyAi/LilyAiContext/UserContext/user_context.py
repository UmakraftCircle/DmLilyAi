def format_user_context(facts: list[str]) -> str:
    if not facts:
        return ""
    return "Known about the user:\n" + "\n".join(f"- {f}" for f in facts)
