"""Groq tools that give LilyAi read access to the Umamusume docs (LilyAiGameSpace)."""

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiGameSpace.UmamusumeGameSpaceEngine import get_engine
from LilyAiTool.Models.tool_models import ToolSpec

CATEGORY = "gamespace"


def _opt_str(args: dict, key: str) -> str | None:
    value = args.get(key)
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def _list(ctx, args):
    engine = get_engine()
    category = _opt_str(args, "category")
    docs = engine.list_docs(category)
    if not docs:
        cats = ", ".join(f"{c} ({n})" for c, n in engine.categories().items()) or "none indexed"
        return f"No docs found for category {category!r}. Categories: {cats}." if category else "No docs indexed."
    if not category:
        cats = ", ".join(f"{c} ({n})" for c, n in engine.categories().items())
        return f"Categories: {cats}\nPass a category to list its docs."
    return "\n".join(f"- {d.title} [{d.id}]" for d in docs[:200])


def _search(ctx, args):
    query = _opt_str(args, "query")
    if not query:
        raise ToolError("query is required")
    hits = get_engine().search(query, _opt_str(args, "category"), args.get("limit") or 5)
    if not hits:
        return f"No matches for {query!r}."
    return "\n".join(f"- {h.title} > {h.section} [{h.doc_id}]: {h.snippet}" for h in hits)


def _read(ctx, args):
    ref = _opt_str(args, "doc")
    if not ref:
        raise ToolError("doc is required")
    engine = get_engine()
    result = engine.read(ref, _opt_str(args, "section"), args.get("max_chars") or 6000, _opt_str(args, "category"))
    if result is None:
        similar = engine.suggest(ref)
        hint = f" Did you mean: {', '.join(similar)}?" if similar else ""
        return f"No doc found for {ref!r}.{hint}"
    head = f"{result.title} [{result.doc_id}]" + (f" - section: {result.section}" if result.section else "")
    parts = [head]
    if result.note:
        parts.append(result.note)
    if result.text:
        parts.append(result.text)
    if result.truncated or result.note:
        parts.append("Sections:\n" + "\n".join(f"- {o}" for o in result.outline))
    if result.sources:
        parts.append("Sources:\n" + "\n".join(f"- {u}" for u in result.sources))
    return "\n\n".join(parts)


def game_space_tools() -> list[ToolSpec]:
    return [
        ToolSpec(
            "game_docs_search",
            "Search the Umamusume game docs (characters, guides, skills, support cards, glossary, race list) "
            "and return the best-matching sections. Use this first when you do not know which doc has the answer.",
            {"type": "object", "properties": {
                "query": {"type": "string", "description": "Keywords, e.g. 'Special Week unique skill'"},
                "category": {"type": ["string", "null"], "description": "Optional: Character, Guide, Skill, Glossary, Support Cards"},
                "limit": {"type": ["integer", "null"], "description": "Max results (default 5, max 10)"},
            }, "required": ["query"]},
            _search,
            category=CATEGORY,
        ),
        ToolSpec(
            "game_docs_read",
            "Read an Umamusume game doc by name (e.g. 'Special Week') or id (e.g. 'Character/Special_Week'). "
            "Pass a section heading to read just that part; long docs return an intro plus a section outline. "
            "Results include source URLs, so cite them when relevant.",
            {"type": "object", "properties": {
                "doc": {"type": "string", "description": "Doc title, alias or id"},
                "section": {"type": ["string", "null"], "description": "Optional section heading, e.g. 'Version 3'"},
                "category": {"type": ["string", "null"], "description": "Optional category to disambiguate"},
                "max_chars": {"type": ["integer", "null"], "description": "Optional size cap (default 6000)"},
            }, "required": ["doc"]},
            _read,
            category=CATEGORY,
        ),
        ToolSpec(
            "game_docs_list",
            "List what Umamusume game docs exist. Without a category, returns the categories and counts; "
            "with one, lists every doc in it.",
            {"type": "object", "properties": {
                "category": {"type": ["string", "null"], "description": "Optional category name"},
            }, "required": []},
            _list,
            category=CATEGORY,
        ),
    ]
