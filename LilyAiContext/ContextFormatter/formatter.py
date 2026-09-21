def format_block(title: str, items: list[str]) -> str:
    if not items:
        return ""
    body = "\n\n".join(f"[{i}] {s}" for i, s in enumerate(items, 1))
    return f"{title}:\n{body}"
