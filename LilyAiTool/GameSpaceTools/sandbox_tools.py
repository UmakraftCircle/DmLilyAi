"""Groq tool: run fixed table operations (top N, sums, filters, comparisons) on Umamusume docs in a sandbox.

Only registered when PANDASTACK_API_KEY is set and the `pandastack` package is installed, so a bot
without it behaves exactly as before and the model never sees a tool it cannot use.
"""
from __future__ import annotations

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiGameSpace import sandbox_runner
from LilyAiTool.Models.tool_models import ToolSpec

CATEGORY = "gamespace"

_PARAM_KEYS = ("op", "column", "columns", "n", "order", "agg", "names", "name_column",
               "where_column", "where_op", "where_value", "table_index", "limit")


def _opt(args: dict, key: str):
    value = args.get(key)
    if isinstance(value, str):
        value = value.strip()
    return value if value not in (None, "") else None


async def _process(ctx, args: dict) -> str:
    doc = _opt(args, "doc")
    if not doc:
        raise ToolError("doc is required")
    params = {k: _opt(args, k) for k in _PARAM_KEYS}
    params = {k: v for k, v in params.items() if v is not None}
    try:
        doc_id, title, path, text = sandbox_runner.raw_section_text(doc, _opt(args, "section"), _opt(args, "category"))
        result = await sandbox_runner.run_table_op_async(text, params)
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    where = f"{title} > {path}" if path else title
    return f"Computed from {where} [{doc_id}] (exact values from the docs table, calculated in a sandbox):\n{result}"


def sandbox_tools() -> list[ToolSpec]:
    if not sandbox_runner.is_configured():
        return []
    return [
        ToolSpec(
            "game_docs_process",
            "Calculate on a TABLE in an Umamusume game doc: top N by a column, sum/avg/min/max/count, filter rows, "
            "compare named rows, or print a table cleanly. Use this instead of doing arithmetic yourself or reading "
            "long tables. Start with op='tables' if you don't know the columns. Quote the numbers exactly as returned.",
            {"type": "object", "properties": {
                "doc": {"type": "string", "description": "Doc title, alias or id, e.g. 'Support Cards'"},
                "op": {"type": "string", "enum": ["tables", "table", "top", "filter", "stat", "compare"],
                       "description": "tables=list tables, table=show, top=sort+limit, filter=where only, stat=aggregate, compare=named rows"},
                "section": {"type": ["string", "null"], "description": "Section heading holding the table (recommended)"},
                "column": {"type": ["string", "null"], "description": "Column to sort or aggregate (top, stat)"},
                "columns": {"type": ["string", "null"], "description": "Comma-separated columns to show"},
                "n": {"type": ["integer", "null"], "description": "Rows to keep for top (default 5)"},
                "order": {"type": ["string", "null"], "description": "desc (default) or asc, for top"},
                "agg": {"type": ["string", "null"], "description": "sum, avg, min, max or count, for stat"},
                "names": {"type": ["string", "null"], "description": "Comma-separated row names, for compare (2+)"},
                "name_column": {"type": ["string", "null"], "description": "Column holding row names (default: first column)"},
                "where_column": {"type": ["string", "null"], "description": "Column for an optional row filter"},
                "where_op": {"type": ["string", "null"], "description": "eq, ne, contains, gt, gte, lt or lte"},
                "where_value": {"type": ["string", "null"], "description": "Value for the filter"},
                "table_index": {"type": ["integer", "null"], "description": "Which table in the section (0-based), if several"},
                "limit": {"type": ["integer", "null"], "description": "Max rows to print"},
                "category": {"type": ["string", "null"], "description": "Optional category to disambiguate the doc"},
            }, "required": ["doc", "op"]},
            _process,
            category=CATEGORY,
            timeout=60.0,
        ),
    ]
