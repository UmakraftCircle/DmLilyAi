"""Groq tools for the user's own Umamusume collection: support cards, trainees and inheritance parents.

The model passes the user's own words ("kitasan ssr speed mlb"); name matching, id lookup and range
checks happen here in code, so the model never writes an id or an unchecked value to the database.
Everything is keyed by ctx.user_id, which the system sets - the model cannot read or write another user's data.

`collection` is a LilyAiMemory CollectionStore and `session` a SessionMemory, passed in by the composition
root (bootstrap.py) so this domain does not import Memory.
"""
from __future__ import annotations

import re
from typing import Any, Callable

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiCore.Helpers.clock import now_ts
from LilyAiGameSpace import UmamusumeCatalog as cat
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec

from .parent_ranking import parent_line, rank_parents

CATEGORY = "collection"
_PENDING, _UNDO = "collection_pending", "collection_undo"
MAX_OPTIONS = 8
MAX_LIST_LINES = 80
MAX_BULK_LINES = 300


# --------------------------------------------------------------------------- argument helpers


def _uid(ctx: ToolContextData) -> str:
    if not ctx.user_id:
        raise ToolError("No Discord user in this context.")
    return ctx.user_id


def _opt_str(args: dict, key: str) -> str | None:
    value = args.get(key)
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def _flag(args: dict, key: str) -> bool:
    value = args.get(key)
    if isinstance(value, str):
        return value.strip().lower() in ("true", "yes", "y", "1")
    return bool(value)


def _opt_int(args: dict, key: str, lo: int, hi: int, what: str) -> int | None:
    value = args.get(key)
    if value is None or str(value).strip() == "":
        return None
    try:
        n = int(str(value).strip().lstrip("#"))
    except ValueError:
        raise ToolError(f"{what} must be a whole number")
    if not lo <= n <= hi:
        raise ToolError(f"{what} must be between {lo} and {hi}")
    return n


def _lb_arg(args: dict, key: str = "limit_break") -> int | None:
    value = args.get(key)
    if value is None or str(value).strip() == "":
        return None
    s = str(value).strip()
    if s.isdigit():
        n = int(s)
        if 0 <= n <= 4:
            return n
        raise ToolError("limit_break must be 0-4 (MLB = 4)")
    _, n = cat.split_limit_break(s)
    if n is None:
        raise ToolError("limit_break must be 0-4 or 'MLB'")
    return n


def _stars(value: Any, what: str) -> int:
    try:
        n = int(str(value).strip().rstrip("★* "))
    except ValueError:
        raise ToolError(f"{what} must be 1-3")
    if not 1 <= n <= 3:
        raise ToolError(f"{what} must be 1-3")
    return n


def _ago(ts: float | None) -> str:
    if not ts:
        return "never"
    days = int(max(0.0, now_ts() - ts) // 86400)
    return "today" if days == 0 else f"{days} day{'s' if days != 1 else ''} ago"


def _list_arg(args: dict, key: str) -> list | None:
    value = args.get(key)
    if value is None:
        return None
    if not isinstance(value, list):
        raise ToolError(f"{key} must be a list")
    return value


# --------------------------------------------------------------------------- the tools


def collection_tools(collection: Any, session: Any) -> list[ToolSpec]:
    def data_for(uid: str) -> dict:
        return session.touch(uid)[0].data

    def offer(uid: str, intro: str, options: list[tuple[str, Any]], apply: Callable[[Any], str]) -> str:
        """Park a choice in the session; collection_followup(action='choose') runs apply(value)."""
        shown = options[:MAX_OPTIONS]
        data_for(uid)[_PENDING] = {"options": shown, "apply": apply}
        lines = [f"{i}. {label}" for i, (label, _) in enumerate(shown, 1)]
        more = (f"\n(+{len(options) - len(shown)} more - ask for the rarity/type or full name to narrow it down)"
                if len(options) > len(shown) else "")
        return (f"{intro}\n" + "\n".join(lines) + more +
                "\nAsk the user which one, then call collection_followup with action='choose' and choice=<number>.")

    # ------------------------------------------------------------------ support cards

    def card_set(uid: str, card: cat.Card, lb: int) -> str:
        prev = collection.set_card(uid, card.card_id, lb)

        def undo() -> None:
            if prev is None:
                collection.remove_card(uid, card.card_id)
            else:
                collection.set_card(uid, card.card_id, prev)

        data_for(uid)[_UNDO] = (f"{card.label} -> {cat.lb_label(lb)}", undo)
        was = "new card" if prev is None else f"was {cat.lb_label(prev)}"
        return (f"Saved: {card.label} is now {cat.lb_label(lb)} ({was}). "
                "Tell the user exactly this, and that they can say 'undo'.")

    def card_remove(uid: str, card: cat.Card) -> str:
        prev = collection.remove_card(uid, card.card_id)
        if prev is None:
            return f"{card.label} was not on file."
        data_for(uid)[_UNDO] = (f"removal of {card.label}", lambda: collection.set_card(uid, card.card_id, prev))
        return f"Removed: {card.label} (it was {cat.lb_label(prev)}). Tell the user, and that they can say 'undo'."

    def cards_list(uid: str, args: dict) -> str:
        rows = collection.list_cards(uid)
        if not rows:
            return "No support cards on file yet. Ask the user which cards they own and each one's limit break (MLB = 4)."
        rar = (_opt_str(args, "rarity") or "").upper() or None
        typ = cat.norm_type(_opt_str(args, "type"))
        items = []
        for r in rows:
            card = cat.card_by_id(r["card_id"])
            if card and ((rar and card.rarity != rar) or (typ and card.type != typ)):
                continue
            if not card and (rar or typ):
                continue
            sort_key = (cat.RARITIES.index(card.rarity), cat.TYPE_ORDER.index(card.type) if card.type in cat.TYPE_ORDER else 9,
                        card.label) if card else (9, 9, r["card_id"])
            text = (f"{card.label} - {cat.lb_label(r['limit_break'])}" if card
                    else f"{r['card_id']} - {cat.lb_label(r['limit_break'])} (not in the current docs)")
            items.append((sort_key, text))
        items.sort(key=lambda t: t[0])
        updated = max(r["updated_at"] for r in rows)
        head = f"{len(rows)} support cards on file (last updated {_ago(updated)})"
        if rar or typ:
            head += f"; showing {len(items)} matching the filter"
        lines = [t for _, t in items[:MAX_LIST_LINES]]
        if len(items) > MAX_LIST_LINES:
            lines.append(f"...(+{len(items) - MAX_LIST_LINES} more - filter by rarity or type)")
        return head + ".\n" + "\n".join(lines)

    def cards_set(uid: str, args: dict) -> str:
        text = _opt_str(args, "card")
        if not text:
            raise ToolError("card is required (character name, plus rarity/type if the user gave them)")
        clean, lb_in_text = cat.split_limit_break(text)
        lb = _lb_arg(args)
        lb = lb if lb is not None else lb_in_text
        if lb is None:
            raise ToolError("limit_break is required (0-4, MLB = 4). Ask the user for it.")
        cards = cat.resolve_card(clean, _opt_str(args, "rarity"), _opt_str(args, "type"))
        if not cards:
            return (f"No support card matches {text!r}. Check the character's name, or add the rarity/type "
                    "(e.g. 'SSR Speed'). Nothing was saved.")
        if len(cards) == 1:
            return card_set(uid, cards[0], lb)
        return offer(uid, f"{len(cards)} cards match {text!r} (setting {cat.lb_label(lb)}):",
                     [(c.label, c) for c in cards], lambda c: card_set(uid, c, lb))

    def cards_remove(uid: str, args: dict) -> str:
        text = _opt_str(args, "card")
        if not text:
            raise ToolError("card is required")
        clean, _ = cat.split_limit_break(text)
        owned = [c for c in cat.resolve_card(clean, _opt_str(args, "rarity"), _opt_str(args, "type"))
                 if collection.get_card(uid, c.card_id) is not None]
        if not owned:
            return f"No card matching {text!r} is on file, so nothing was removed."
        if len(owned) > 1:
            return offer(uid, f"{len(owned)} owned cards match {text!r} - which one should be removed?",
                         [(c.label, c) for c in owned], lambda c: card_remove(uid, c))
        if not _flag(args, "confirm"):
            return (f"This would remove {owned[0].label} from the collection. Ask the user to confirm, "
                    "then call again with confirm=true.")
        return card_remove(uid, owned[0])

    def cards_bulk(uid: str, args: dict) -> str:
        text = _opt_str(args, "text")
        if not text:
            raise ToolError("text is required: one card per line, e.g. 'Kitasan Black SSR Speed MLB'")
        default_lb = _lb_arg(args, "default_limit_break")
        lines = [ln for ln in text.splitlines() if ln.strip()]
        if len(lines) > MAX_BULK_LINES:
            raise ToolError(f"Too many lines ({len(lines)}); send at most {MAX_BULK_LINES} at a time.")
        changes: list[tuple[str, int | None]] = []
        problems: list[str] = []
        for ln in lines:
            line = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s*", "", ln).strip()
            clean, lb = cat.split_limit_break(line)
            lb = lb if lb is not None else default_lb
            if lb is None:
                problems.append(f"no limit break given: {line}")
                continue
            cards = cat.resolve_card(clean)
            if not cards:
                problems.append(f"not found: {line}")
            elif len(cards) > 1:
                shown = "; ".join(c.label for c in cards[:3]) + ("; ..." if len(cards) > 3 else "")
                problems.append(f"ambiguous: {line} -> {shown}")
            else:
                changes.append((cards[0].card_id, collection.set_card(uid, cards[0].card_id, lb)))

        if changes:
            def undo() -> None:
                for card_id, prev in reversed(changes):
                    if prev is None:
                        collection.remove_card(uid, card_id)
                    else:
                        collection.set_card(uid, card_id, prev)

            data_for(uid)[_UNDO] = (f"bulk update of {len(changes)} cards", undo)
        out = [f"Saved {len(changes)} of {len(lines)} lines."]
        if problems:
            out.append("These lines need the user's help (they can resend them with rarity/type or a limit break):")
            out += [f"- {p}" for p in problems[:15]]
            if len(problems) > 15:
                out.append(f"- ...and {len(problems) - 15} more")
        if changes:
            out.append("The user can say 'undo' to revert this whole batch.")
        return "\n".join(out)

    def my_cards(ctx: ToolContextData, args: dict) -> str:
        uid = _uid(ctx)
        action = (_opt_str(args, "action") or "list").lower()
        handlers = {"list": cards_list, "set": cards_set, "remove": cards_remove, "bulk": cards_bulk}
        if action not in handlers:
            raise ToolError("action must be one of: list, set, remove, bulk")
        return handlers[action](uid, args)

    # ------------------------------------------------------------------ trainees

    def trainee_label(row: dict) -> str:
        v = f" ({row['version']})" if row.get("version") else ""
        pot = f", Potential {row['potential_level']}" if row.get("potential_level") is not None else ""
        return f"{cat.uma_name(row['uma_id'])}{v}{pot}"

    def trainee_set(uid: str, char: cat.Character, version: str, potential: int | None) -> str:
        prev = collection.set_trainee(uid, char.uma_id, version, potential)
        data_for(uid)[_UNDO] = (f"trainee {char.name}",
                                lambda: collection.restore_trainee(uid, char.uma_id, version, prev))
        row = collection.get_trainee(uid, char.uma_id, version) or {"uma_id": char.uma_id, "version": version}
        return f"Saved trainee: {trainee_label(row)}. Tell the user exactly this, and that they can say 'undo'."

    def trainee_remove(uid: str, char: cat.Character, version: str) -> str:
        prev = collection.remove_trainee(uid, char.uma_id, version)
        if prev is None:
            return f"{char.name} was not on file."
        data_for(uid)[_UNDO] = (f"removal of trainee {char.name}",
                                lambda: collection.restore_trainee(uid, char.uma_id, version, prev))
        return f"Removed trainee: {trainee_label(prev)}. Tell the user, and that they can say 'undo'."

    def my_trainees(ctx: ToolContextData, args: dict) -> str:
        uid = _uid(ctx)
        action = (_opt_str(args, "action") or "list").lower()
        if action == "list":
            rows = collection.list_trainees(uid)
            if not rows:
                return "No trainees on file yet. Ask the user which trainees they have (and their Potential level if they know it)."
            return f"{len(rows)} trainees on file:\n" + "\n".join(f"- {trainee_label(r)}" for r in rows)
        if action not in ("set", "remove"):
            raise ToolError("action must be one of: list, set, remove")
        text = _opt_str(args, "uma")
        if not text:
            raise ToolError("uma is required (the character's name)")
        version = _opt_str(args, "version") or ""
        chars = cat.resolve_uma(text)
        if not chars:
            return f"No character matches {text!r}. Check the spelling. Nothing was changed."
        if action == "set":
            potential = _opt_int(args, "potential_level", 0, 10, "potential_level")
            if len(chars) == 1:
                return trainee_set(uid, chars[0], version, potential)
            return offer(uid, f"{len(chars)} characters match {text!r}:", [(c.name, c) for c in chars],
                         lambda c: trainee_set(uid, c, version, potential))
        owned = [c for c in chars if collection.get_trainee(uid, c.uma_id, version)]
        if not owned:
            return f"No trainee matching {text!r} is on file, so nothing was removed."
        if len(owned) > 1:
            return offer(uid, f"{len(owned)} saved trainees match {text!r} - which one should be removed?",
                         [(c.name, c) for c in owned], lambda c: trainee_remove(uid, c, version))
        if not _flag(args, "confirm"):
            return f"This would remove trainee {owned[0].name}. Ask the user to confirm, then call again with confirm=true."
        return trainee_remove(uid, owned[0], version)

    # ------------------------------------------------------------------ inheritance parents

    def parse_fields(args: dict) -> dict:
        """Validate the optional parent fields the model passed; returns only the ones that were given."""
        fields: dict[str, Any] = {}
        if args.get("nickname") is not None:
            fields["nickname"] = _opt_str(args, "nickname")
        if args.get("scenario") is not None and _opt_str(args, "scenario"):
            fields["scenario"] = cat.norm_scenario(args["scenario"])
        wc = _opt_int(args, "white_count", 0, 500, "white_count")
        if wc is not None:
            fields["white_count"] = wc
        if args.get("unique_skill") is not None:
            fields["unique_skill"] = _opt_str(args, "unique_skill")

        spirits = _list_arg(args, "scenario_white")
        if spirits is not None:
            parsed = []
            for item in spirits:
                spirit = cat.parse_spirit(item)
                if not spirit:
                    raise ToolError(f"scenario_white entry {item!r} must be Racing Spirit or Burning Spirit plus a stat")
                parsed.append(spirit)
            fields["scenario_white"] = parsed

        pinks = _list_arg(args, "pink")
        if pinks is not None:
            parsed = []
            for item in pinks:
                if not isinstance(item, dict):
                    raise ToolError("each pink entry must be an object: {kind: distance|track|style, aptitude, stars: 1-3}")
                kind = str(item.get("kind", "")).strip().lower()
                if kind not in ("distance", "track", "style"):
                    raise ToolError("pink kind must be distance, track or style")
                apt = cat.norm_aptitude(kind, item.get("aptitude"))
                if not apt:
                    raise ToolError(f"unknown {kind} aptitude {item.get('aptitude')!r}")
                parsed.append({"kind": kind, "aptitude": apt, "stars": _stars(item.get("stars"), "pink stars")})
            fields["pink"] = parsed

        blue = args.get("blue")
        if blue is not None:
            if not isinstance(blue, dict):
                raise ToolError("blue must be an object: {stat, stars: 1-3}")
            stat = cat.norm_stat(blue.get("stat"))
            if not stat:
                raise ToolError("blue stat must be speed, stamina, power, guts or wit")
            fields["blue"] = {"stat": stat, "stars": _stars(blue.get("stars"), "blue stars")}

        whites = _list_arg(args, "key_whites")
        if whites is not None:
            fields["key_whites"] = [str(w).strip()[:60] for w in whites if str(w).strip()][:30]

        gps = _list_arg(args, "grandparents")
        if gps is not None:
            parsed = []
            for item in gps[:2]:
                if isinstance(item, str):
                    item = {"uma": item}
                if not isinstance(item, dict):
                    raise ToolError("each grandparent must be a name or an object {uma, unique_skill, scenario_white}")
                raw = str(item.get("uma") or item.get("name") or "").strip()
                if not raw:
                    continue
                chars = cat.resolve_uma(raw)
                gp: dict[str, Any] = ({"uma_id": chars[0].uma_id, "name": chars[0].name} if len(chars) == 1
                                      else {"name": raw, "unresolved": True})
                if item.get("unique_skill"):
                    gp["unique_skill"] = str(item["unique_skill"]).strip()[:80]
                if isinstance(item.get("scenario_white"), list):
                    gp["scenario_white"] = [s for s in map(cat.parse_spirit, item["scenario_white"]) if s]
                parsed.append(gp)
            fields["grandparents"] = parsed
        return fields

    def parent_ref(uid: str, ref: Any) -> dict:
        text = str(ref).strip().lstrip("#")
        if text.isdigit():
            parent = collection.get_parent(uid, int(text))
            if not parent:
                raise ToolError(f"No saved parent #{text}.")
            return parent
        parents = collection.list_parents(uid)
        low = text.lower()
        hits = [p for p in parents if (p.get("nickname") or "").lower() == low]
        if not hits:
            ids = {c.uma_id for c in cat.resolve_uma(text)}
            hits = [p for p in parents if p["uma_id"] in ids or low in (p.get("nickname") or "").lower()]
        if not hits:
            raise ToolError(f"No saved parent matches {text!r}.")
        if len(hits) > 1:
            listing = "; ".join(f"#{p['parent_id']} {cat.uma_name(p['uma_id'])}"
                                + (f' "{p["nickname"]}"' if p.get("nickname") else "") for p in hits)
            raise ToolError(f"{len(hits)} saved parents match {text!r}: {listing}. Ask the user which number.")
        return hits[0]

    def parent_create(uid: str, char: cat.Character, fields: dict) -> str:
        parent_id = collection.add_parent(uid, {"uma_id": char.uma_id, **fields})
        data_for(uid)[_UNDO] = (f"new parent #{parent_id}", lambda: collection.delete_parent(uid, parent_id))
        parent = collection.get_parent(uid, parent_id)
        return (f"Saved parent #{parent_id}: {parent_line(parent, cat.uma_name)}\n"
                "Read these values back to the user so they can correct any spark you got wrong; they can also say 'undo'.")

    def parents_save(uid: str, args: dict) -> str:
        fields = parse_fields(args)
        existing_id = _opt_int(args, "parent_id", 1, 10**9, "parent_id")
        if existing_id is not None:
            prev = collection.get_parent(uid, existing_id)
            if not prev:
                raise ToolError(f"No saved parent #{existing_id}.")
            if not fields:
                raise ToolError("Nothing to change: pass the fields that should be updated.")
            collection.update_parent(uid, existing_id, fields)
            data_for(uid)[_UNDO] = (f"edit of parent #{existing_id}", lambda: collection.replace_parent(uid, prev))
            return (f"Updated parent #{existing_id}: {parent_line(collection.get_parent(uid, existing_id), cat.uma_name)}\n"
                    "Tell the user what changed; they can say 'undo'.")
        text = _opt_str(args, "uma")
        if not text:
            raise ToolError("uma is required to save a new parent (or pass parent_id to edit one)")
        if not any(k in fields for k in ("white_count", "scenario_white", "pink", "blue", "unique_skill")):
            raise ToolError("Give at least some of the parent's sparks (white_count, scenario_white, pink, blue, unique_skill).")
        chars = cat.resolve_uma(text)
        if not chars:
            return f"No character matches {text!r}. Check the spelling. Nothing was saved."
        if len(chars) == 1:
            return parent_create(uid, chars[0], fields)
        return offer(uid, f"{len(chars)} characters match {text!r}:", [(c.name, c) for c in chars],
                     lambda c: parent_create(uid, c, fields))

    def parents_list(uid: str, args: dict) -> str:
        uma = _opt_str(args, "uma")
        if uma:
            chars = cat.resolve_uma(uma)
            parents = [p for p in collection.list_parents(uid) if p["uma_id"] in {c.uma_id for c in chars}]
        else:
            parents = collection.list_parents(uid)
        if not parents:
            return ("No parents on file" + (f" for {uma!r}" if uma else "") +
                    ". Ask the user to describe their inheritance umas, or offer to save the one from a finished career.")
        return f"{len(parents)} saved parents:\n" + "\n".join(parent_line(p, cat.uma_name) for p in parents[:40])

    def parents_delete(uid: str, args: dict) -> str:
        ref = args.get("parent")
        if ref is None or str(ref).strip() == "":
            raise ToolError("parent is required (its number like 3, a nickname, or the uma's name)")
        parent = parent_ref(uid, ref)
        if not _flag(args, "confirm"):
            return (f"This would delete parent #{parent['parent_id']}: {parent_line(parent, cat.uma_name)}\n"
                    "Ask the user to confirm, then call again with confirm=true.")
        collection.delete_parent(uid, parent["parent_id"])
        data_for(uid)[_UNDO] = (f"deletion of parent #{parent['parent_id']}", lambda: collection.replace_parent(uid, parent))
        return f"Deleted parent #{parent['parent_id']}. Tell the user, and that they can say 'undo'."

    def parents_find(uid: str, args: dict) -> str:
        trainee = _opt_str(args, "trainee")
        if not trainee:
            raise ToolError("trainee is required (the character the career is for)")
        chars = cat.resolve_uma(trainee)
        if len(chars) != 1:
            hint = ("No character matches that name." if not chars
                    else "Several characters match: " + ", ".join(c.name for c in chars[:8]) + ". Ask the user which.")
            raise ToolError(hint)
        targets: dict[str, str | None] = {}
        for kind in ("distance", "track", "style"):
            raw = _opt_str(args, kind)
            targets[kind] = None
            if raw:
                targets[kind] = cat.norm_aptitude(kind, raw)
                if not targets[kind]:
                    raise ToolError(f"unknown {kind} {raw!r}")
        scenario = cat.norm_scenario(args.get("scenario")) if _opt_str(args, "scenario") else None
        parents = collection.list_parents(uid)
        if not parents:
            return ("No parents on file. Ask the user to describe their inheritance umas "
                    "(or save them after a career), then try again.")
        limit = _opt_int(args, "limit", 1, 10, "limit") or 5
        ranked = rank_parents(parents, trainee_uma_id=chars[0].uma_id, scenario=scenario, **targets)[:limit]
        goal = ", ".join(x for x in (scenario, targets["distance"], targets["track"], targets["style"]) if x) or "no target given"
        out = [f"Best {len(ranked)} of {len(parents)} saved parents for {chars[0].name} ({goal}), ranked by the guide's "
               "priority (scenario white > pinks > white count):"]
        for score, p, why in ranked:
            out.append(f"- {parent_line(p, cat.uma_name)}\n  score {score:g}: " + ", ".join(why))
        out.append("Not checked here: the Unique Skill Gate (does the unique activate on the target track? check the Skill docs) "
                   "and compatibility (ask the user for the ◎ rating in the game).")
        return "\n".join(out)

    def my_parents(ctx: ToolContextData, args: dict) -> str:
        uid = _uid(ctx)
        action = (_opt_str(args, "action") or "list").lower()
        handlers = {"list": parents_list, "save": parents_save, "delete": parents_delete, "find": parents_find}
        if action not in handlers:
            raise ToolError("action must be one of: list, save, delete, find")
        return handlers[action](uid, args)

    # ------------------------------------------------------------------ follow-ups

    def followup(ctx: ToolContextData, args: dict) -> str:
        uid = _uid(ctx)
        action = (_opt_str(args, "action") or "").lower()
        data = data_for(uid)
        if action == "choose":
            pending = data.get(_PENDING)
            if not pending:
                return "Nothing is waiting for a choice (it may have expired). Ask the user to repeat the request."
            options = pending["options"]
            n = _opt_int(args, "choice", 1, 99, "choice")
            if n is None:
                raise ToolError("choice is required (the number from the list)")
            if n > len(options):
                raise ToolError(f"choice must be between 1 and {len(options)}")
            data.pop(_PENDING, None)
            return pending["apply"](options[n - 1][1])
        if action == "undo":
            entry = data.pop(_UNDO, None)
            if not entry:
                return "Nothing to undo (undo only covers the last change made in this chat session)."
            label, fn = entry
            fn()
            return f"Undone: {label}. Tell the user."
        if action == "clear":
            scope = (_opt_str(args, "scope") or "all").lower()
            if scope not in ("all", "cards", "trainees", "parents"):
                raise ToolError("scope must be one of: all, cards, trainees, parents")
            counts = collection.counts(uid)
            target = list(counts) if scope == "all" else [scope]
            summary = ", ".join(f"{counts[s]} {s}" for s in target)
            if not _flag(args, "confirm"):
                return (f"This would permanently delete {summary}. It cannot be undone. Ask the user to confirm "
                        "explicitly, then call again with confirm=true.")
            collection.clear(uid, scope)
            data.pop(_UNDO, None)
            data.pop(_PENDING, None)
            return f"Deleted {summary}. Tell the user."
        raise ToolError("action must be one of: choose, undo, clear")

    # ------------------------------------------------------------------ specs

    nullable_int = {"type": ["integer", "string", "null"]}
    confirm_prop = {"type": ["boolean", "null"], "description": "true only after the user explicitly agreed"}

    return [
        ToolSpec(
            "my_cards",
            "The CURRENT user's own support card collection: which cards they own and each card's limit break "
            "(MLB = limit break 4). Use it when they say what they own or what changed (\"I MLB'd Kitasan SSR Speed\"), "
            "and call action='list' whenever you need their owned cards, e.g. to build a Budget Deck. Only save what the "
            "user states about THEIR cards in the first person, never for questions or hypotheticals. Actions: list "
            "(optional rarity/type filter); set (card + limit_break 0-4); remove (only after the user agrees, then "
            "confirm=true); bulk (a pasted list, one card per line; pass default_limit_break if they said e.g. 'all MLB'). "
            "Pass the user's own words as 'card' (character name plus rarity/type if given); the tool resolves it. If it "
            "returns a numbered list, ask the user which one and call collection_followup with action='choose'. Always "
            "tell the user exactly what was saved.",
            {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["list", "set", "remove", "bulk"]},
                "card": {"type": ["string", "null"], "description": "User's words, e.g. 'kitasan black ssr speed'"},
                "limit_break": {**nullable_int, "description": "0-4, or 'MLB' for 4"},
                "rarity": {"type": ["string", "null"], "description": "SSR, SR or R (optional filter)"},
                "type": {"type": ["string", "null"], "description": "Speed, Stamina, Power, Guts, Wit, Friend or Group (optional filter)"},
                "text": {"type": ["string", "null"], "description": "bulk only: the pasted list, one card per line"},
                "default_limit_break": {**nullable_int, "description": "bulk only: used for lines without a limit break"},
                "confirm": confirm_prop,
            }, "required": ["action"]},
            my_cards, category=CATEGORY,
        ),
        ToolSpec(
            "my_trainees",
            "The CURRENT user's own trainees (playable umas they have) with Potential level. Use when they say which "
            "trainees they have or a Potential level changed. Only save what the user states in the first person. "
            "Actions: list; set (uma, optional potential_level and version/outfit); remove (only after the user agrees, "
            "then confirm=true). If it returns a numbered list, ask the user which one and call collection_followup with "
            "action='choose'.",
            {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["list", "set", "remove"]},
                "uma": {"type": ["string", "null"], "description": "Character name in the user's words"},
                "version": {"type": ["string", "null"], "description": "Outfit/version label if the user gave one"},
                "potential_level": {**nullable_int, "description": "Potential level, 0-10"},
                "confirm": confirm_prop,
            }, "required": ["action"]},
            my_trainees, category=CATEGORY,
        ),
        ToolSpec(
            "my_parents",
            "The CURRENT user's saved inheritance umas (parents) - what Step 4 of the Career Start Workflow needs. "
            "Actions: list (optional uma filter); save (a new parent, or pass parent_id to correct one); delete (by number "
            "like 3, nickname or uma name; confirm=true after the user agrees); find (rank their saved parents for a "
            "trainee/target: needs trainee, optionally scenario, distance, track, style). Save only after the user has "
            "confirmed the values, never guess a spark, and read the saved result back to them. find applies the guide's "
            "deterministic priority only; you must still check the Unique Skill Gate in the Skill docs and ask the user "
            "for the compatibility rating.",
            {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["list", "save", "delete", "find"]},
                "parent_id": {**nullable_int, "description": "save: edit this saved parent instead of creating one"},
                "parent": {**nullable_int, "description": "delete: number, nickname or uma name"},
                "uma": {"type": ["string", "null"], "description": "Character name of the parent (save/list)"},
                "nickname": {"type": ["string", "null"]},
                "scenario": {"type": ["string", "null"], "description": "Ura Finale, Unity Cup, ... (the career that made it)"},
                "white_count": {**nullable_int, "description": "Number of white skills on the parent"},
                "scenario_white": {"type": ["array", "null"], "items": {"type": "object", "properties": {
                    "name": {"type": "string", "description": "Racing Spirit or Burning Spirit"},
                    "stat": {"type": ["string", "null"], "description": "speed, stamina, power, guts, wit or mood"},
                    "plus": {"type": ["boolean", "null"]}}}},
                "pink": {"type": ["array", "null"], "items": {"type": "object", "properties": {
                    "kind": {"type": "string", "enum": ["distance", "track", "style"]},
                    "aptitude": {"type": "string", "description": "e.g. mile, turf, pace chaser"},
                    "stars": {"type": "integer"}}}},
                "blue": {"type": ["object", "null"], "properties": {
                    "stat": {"type": "string"}, "stars": {"type": "integer"}}},
                "unique_skill": {"type": ["string", "null"]},
                "key_whites": {"type": ["array", "null"], "items": {"type": "string"}},
                "grandparents": {"type": ["array", "null"], "items": {"type": "object", "properties": {
                    "uma": {"type": "string"}, "unique_skill": {"type": ["string", "null"]}}}},
                "trainee": {"type": ["string", "null"], "description": "find: the character the career is for"},
                "distance": {"type": ["string", "null"], "description": "find: sprint, mile, medium or long"},
                "track": {"type": ["string", "null"], "description": "find: turf or dirt"},
                "style": {"type": ["string", "null"], "description": "find: front runner, pace chaser, late surger or end closer"},
                "limit": {**nullable_int, "description": "find: how many to return (default 5, max 10)"},
                "confirm": confirm_prop,
            }, "required": ["action"]},
            my_parents, category=CATEGORY,
        ),
        ToolSpec(
            "collection_followup",
            "Follow-up for the collection tools (my_cards, my_trainees, my_parents). action='choose' with choice=<number> "
            "after one of them returned a numbered list and the user picked; action='undo' when the user asks to undo the "
            "last collection change; action='clear' to delete the user's whole collection (or scope='cards'/'trainees'/"
            "'parents') - only after the user explicitly confirmed, then pass confirm=true. Clear cannot be undone.",
            {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["choose", "undo", "clear"]},
                "choice": {**nullable_int, "description": "choose: the number the user picked"},
                "scope": {"type": ["string", "null"], "enum": ["all", "cards", "trainees", "parents", None]},
                "confirm": confirm_prop,
            }, "required": ["action"]},
            followup, category=CATEGORY,
        ),
    ]
