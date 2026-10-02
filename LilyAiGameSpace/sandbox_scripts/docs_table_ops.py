"""Fixed table-processing script. It runs INSIDE a PandaStack sandbox, never in the bot.

LilyAi uploads three files and runs this script:
    /workspace/input.md     the raw (unclipped) text of one docs section
    /workspace/params.json  what to do (chosen by the chat model, validated here)
    /workspace/docs_table_ops.py   this file

It prints exactly one JSON object to stdout: {"ok": true, "text": "..."} or {"ok": false, "error": "..."}.
Standard library only, so it works on any template. The model never supplies code, only parameters.

Operations (params["op"]):
    tables    list the markdown tables found
    table     re-emit a table (optionally only some columns) as clean markdown
    top       sort by a column and keep the first n rows
    filter    keep rows matching a condition
    stat      sum / avg / min / max / count of a column
    compare   put the named rows side by side and show the difference for numeric columns
Any op can also take a "where" condition (where_column, where_op, where_value) that is applied first.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

INPUT = Path("/workspace/input.md")
PARAMS = Path("/workspace/params.json")

MAX_ROWS = 200
_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_NUM_RE = re.compile(r"^[+-]?\d[\d,]*(?:\.\d+)?\s*(?:%|x|pt|pts)?$", re.IGNORECASE)
_STRIP_MD = re.compile(r"[*_`]+")


class OpError(Exception):
    pass


# ----------------------------------------------------------------- parsing
def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells = re.split(r"(?<!\\)\|", line)
    return [c.replace("\\|", "|").strip() for c in cells]


def parse_tables(text: str) -> list[dict]:
    tables: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and _SEP_RE.match(lines[i + 1]):
            header = _split_row(lines[i])
            rows: list[list[str]] = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                row = _split_row(lines[j])
                row = (row + [""] * len(header))[: len(header)]
                rows.append(row)
                j += 1
            tables.append({"columns": header, "rows": rows})
            i = j
        else:
            i += 1
    return tables


def to_number(cell: str):
    c = _STRIP_MD.sub("", cell).strip()
    if not _NUM_RE.match(c):
        return None
    c = re.sub(r"(?i)\s*(%|x|pts?)$", "", c).replace(",", "")
    try:
        return float(c)
    except ValueError:
        return None


def fmt_num(x: float) -> str:
    x = round(x, 4)
    return str(int(x)) if x == int(x) else f"{x:g}"


def _norm(s: str) -> str:
    return re.sub(r"[\W_]+", "", _STRIP_MD.sub("", s).casefold())


def find_column(columns: list[str], name: str) -> int:
    q = _norm(name)
    if not q:
        raise OpError("column name is empty")
    norm = [_norm(c) for c in columns]
    for test in (lambda c: c == q, lambda c: c.startswith(q), lambda c: q in c):
        hits = [i for i, c in enumerate(norm) if test(c)]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            raise OpError(f"column '{name}' is ambiguous: {', '.join(columns[i] for i in hits)}")
    raise OpError(f"no column '{name}'. Columns: {', '.join(columns)}")


# ----------------------------------------------------------------- helpers
def choose_table(tables: list[dict], params: dict) -> dict:
    if not tables:
        raise OpError("no markdown table found in this section")
    idx = params.get("table_index")
    if idx is not None:
        if not isinstance(idx, int) or not (0 <= idx < len(tables)):
            raise OpError(f"table_index must be 0-{len(tables) - 1}")
        return tables[idx]
    wanted = [params.get("column"), params.get("where_column")] + _csv(params.get("columns"))
    wanted = [w for w in wanted if w]
    if wanted:
        for t in tables:
            try:
                for w in wanted:
                    find_column(t["columns"], w)
                return t
            except OpError:
                continue
    if len(tables) == 1:
        return tables[0]
    return tables[0]


def _csv(value) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [p.strip() for p in str(value).split(",") if p.strip()]


def md_table(columns: list[str], rows: list[list[str]]) -> str:
    esc = lambda s: str(s).replace("|", "\\|")
    out = ["| " + " | ".join(esc(c) for c in columns) + " |",
           "| " + " | ".join("---" for _ in columns) + " |"]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def apply_where(table: dict, params: dict) -> tuple[list[list[str]], str]:
    rows = table["rows"]
    col = params.get("where_column")
    if not col:
        return rows, ""
    ci = find_column(table["columns"], col)
    op = (params.get("where_op") or "eq").lower()
    value = params.get("where_value")
    if value is None or str(value).strip() == "":
        raise OpError("where_value is required with where_column")
    value = str(value).strip()
    vnum = to_number(value)

    def keep(cell: str) -> bool:
        cnum = to_number(cell)
        if op in ("gt", "gte", "lt", "lte"):
            if cnum is None or vnum is None:
                return False
            return {"gt": cnum > vnum, "gte": cnum >= vnum, "lt": cnum < vnum, "lte": cnum <= vnum}[op]
        a, b = _STRIP_MD.sub("", cell).casefold().strip(), value.casefold()
        if op == "eq":
            return (cnum == vnum) if (cnum is not None and vnum is not None) else a == b
        if op == "ne":
            return (cnum != vnum) if (cnum is not None and vnum is not None) else a != b
        if op == "contains":
            return b in a
        raise OpError("where_op must be one of eq, ne, contains, gt, gte, lt, lte")

    kept = [r for r in rows if keep(r[ci])]
    return kept, f"{table['columns'][ci]} {op} {value}"


def select(table: dict, rows: list[list[str]], params: dict) -> tuple[list[str], list[list[str]]]:
    wanted = _csv(params.get("columns"))
    if not wanted:
        return table["columns"], rows
    idxs = [find_column(table["columns"], w) for w in wanted]
    return [table["columns"][i] for i in idxs], [[r[i] for i in idxs] for r in rows]


def clip(rows: list[list[str]], limit) -> tuple[list[list[str]], str]:
    cap = MAX_ROWS if not isinstance(limit, int) or limit <= 0 else min(limit, MAX_ROWS)
    if len(rows) > cap:
        return rows[:cap], f"(showing {cap} of {len(rows)} rows)"
    return rows, ""


# -------------------------------------------------------------------- ops
def op_tables(tables, params):
    if not tables:
        return "No markdown tables in this section."
    lines = []
    for i, t in enumerate(tables):
        lines.append(f"- table_index {i}: {len(t['rows'])} rows; columns: {', '.join(t['columns'])}")
    return "\n".join(lines)


def op_table(table, params):
    rows, cond = apply_where(table, params)
    cols, rows = select(table, rows, params)
    rows, note = clip(rows, params.get("limit"))
    head = f"{len(rows)} rows" + (f" where {cond}" if cond else "")
    return "\n".join(x for x in (head, md_table(cols, rows), note) if x)


def op_top(table, params):
    col = params.get("column")
    if not col:
        raise OpError("column is required for top")
    ci = find_column(table["columns"], col)
    rows, cond = apply_where(table, params)
    scored = [(to_number(r[ci]), r) for r in rows]
    numeric = [(v, r) for v, r in scored if v is not None]
    if not numeric:
        raise OpError(f"column '{table['columns'][ci]}' has no numeric values")
    desc = (params.get("order") or "desc").lower() != "asc"
    numeric.sort(key=lambda p: p[0], reverse=desc)
    n = params.get("n")
    n = n if isinstance(n, int) and n > 0 else 5
    chosen = [r for _, r in numeric[:n]]
    cols, chosen = select(table, chosen, params)
    skipped = len(rows) - len(numeric)
    head = f"Top {len(chosen)} by {table['columns'][ci]} ({'highest' if desc else 'lowest'} first)"
    if cond:
        head += f", where {cond}"
    note = f"({skipped} rows skipped: not numeric)" if skipped else ""
    return "\n".join(x for x in (head, md_table(cols, chosen), note) if x)


def op_filter(table, params):
    if not params.get("where_column"):
        raise OpError("where_column, where_op and where_value are required for filter")
    return op_table(table, params)


def op_stat(table, params):
    agg = (params.get("agg") or "").lower()
    if agg not in ("sum", "avg", "min", "max", "count"):
        raise OpError("agg must be one of sum, avg, min, max, count")
    rows, cond = apply_where(table, params)
    suffix = f" where {cond}" if cond else ""
    if agg == "count":
        return f"count{suffix} = {len(rows)}"
    col = params.get("column")
    if not col:
        raise OpError("column is required for sum/avg/min/max")
    ci = find_column(table["columns"], col)
    vals = [v for v in (to_number(r[ci]) for r in rows) if v is not None]
    if not vals:
        raise OpError(f"column '{table['columns'][ci]}' has no numeric values")
    result = {"sum": sum(vals), "avg": sum(vals) / len(vals), "min": min(vals), "max": max(vals)}[agg]
    return f"{agg} of {table['columns'][ci]}{suffix} = {fmt_num(result)} (over {len(vals)} numeric values)"


def op_compare(table, params):
    names = _csv(params.get("names"))
    if len(names) < 2:
        raise OpError("names needs at least two comma-separated row names")
    key_col = params.get("name_column")
    ki = find_column(table["columns"], key_col) if key_col else 0
    picked: list[list[str]] = []
    for name in names:
        q = _norm(name)
        exact = [r for r in table["rows"] if _norm(r[ki]) == q]
        part = exact or [r for r in table["rows"] if q and q in _norm(r[ki])]
        if len(part) != 1:
            why = "not found" if not part else f"matches {len(part)} rows"
            raise OpError(f"'{name}' {why} in column '{table['columns'][ki]}'")
        picked.append(part[0])
    cols, shown = select(table, picked, params)
    out = [md_table(cols, shown)]
    if len(picked) == 2:
        diffs = []
        for ci, c in enumerate(table["columns"]):
            if c not in cols or ci == ki:
                continue
            a, b = to_number(picked[0][ci]), to_number(picked[1][ci])
            if a is not None and b is not None:
                diffs.append(f"- {c}: {picked[1][ki]} minus {picked[0][ki]} = {fmt_num(b - a)}")
        if diffs:
            out.append("Differences (second minus first):\n" + "\n".join(diffs))
    return "\n\n".join(out)


OPS = {"tables": op_tables, "table": op_table, "top": op_top, "filter": op_filter,
       "stat": op_stat, "compare": op_compare}


def run(text: str, params: dict) -> dict:
    op = (params.get("op") or "").lower()
    if op not in OPS:
        return {"ok": False, "error": f"op must be one of {', '.join(OPS)}"}
    tables = parse_tables(text)
    try:
        if op == "tables":
            return {"ok": True, "text": op_tables(tables, params)}
        table = choose_table(tables, params)
        return {"ok": True, "text": OPS[op](table, params)}
    except OpError as e:
        return {"ok": False, "error": str(e)}


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        text = INPUT.read_text(encoding="utf-8")
        result = run(text, params if isinstance(params, dict) else {})
    except Exception as e:  # always answer with JSON
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
