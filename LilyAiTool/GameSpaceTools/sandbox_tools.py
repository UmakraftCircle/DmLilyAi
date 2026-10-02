"""Groq tools that run in a PandaStack sandbox: table operations on game docs, and exact game calculators.

Only registered when PANDASTACK_API_KEY is set and the `pandastack` package is installed, so a bot
without it behaves exactly as before and the model never sees a tool it cannot use.
"""
from __future__ import annotations

import json

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


CALCULATORS = ["help", "pvp_score", "legacy_blue_bonus", "blue_spark_odds", "white_spark_odds", "start_delay",
               "rush_duration", "stat_effective", "wit_effectiveness", "race_phases", "length_convert",
               "speed_boost", "acceleration_gain"]


async def _calculate(ctx, args: dict) -> str:
    calc = _opt(args, "calculator")
    if not calc:
        raise ToolError("calculator is required")
    inputs = args.get("inputs")
    if isinstance(inputs, str):
        try:
            inputs = json.loads(inputs)
        except json.JSONDecodeError:
            raise ToolError("inputs must be a JSON object")
    if inputs is None:
        inputs = {}
    if not isinstance(inputs, dict):
        raise ToolError("inputs must be an object")
    try:
        result = await sandbox_runner.run_calc_async(str(calc), inputs)
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    return f"Calculated in a sandbox with the game docs' rules ({calc}):\n{result}"


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
        ToolSpec(
            "game_calculate",
            "Exact Umamusume calculations from the game docs' rules: Team Trials (PvP) score, legacy/inheritance blue-spark "
            "bonus and spark odds, start-delay and rush odds, effective stat for races, race phases, length/speed/acceleration. "
            "Use it for ANY number the user wants worked out, never do the maths yourself. Call with calculator='help' to see "
            "each calculator's inputs. Compatibility (triangle/circle) is NOT available. Quote results exactly.",
            {"type": "object", "properties": {
                "calculator": {"type": "string", "enum": CALCULATORS, "description": "Which calculator; 'help' lists inputs"},
                "inputs": {"type": ["object", "null"], "description": "Inputs for that calculator, e.g. {\"final_stat\": 850} or "
                           "{\"sparks\": [{\"stat\": \"Speed\", \"stars\": 3}]}"},
            }, "required": ["calculator"]},
            _calculate,
            category=CATEGORY,
            timeout=60.0,
        ),
    ]
