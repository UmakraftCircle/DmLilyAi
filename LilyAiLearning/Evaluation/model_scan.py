"""Scheduled Groq model discovery: scan the model list, probe new chat models, grow the pool, write the catalog."""
import json
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from LilyAiCore.Config.models import ModelPool, ModelSpec
from LilyAiCore.Constants.constants import ROLE_ALTERNATE
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiLearning.Evaluation.model_probe import classify, probe_model

log = get_logger("learning.model_scan")

CATALOG_NAME = "MODEL_CATALOG.md"
MAX_PROBES_PER_SCAN = 3      # protects the free-tier quota
REJECT_RETRY_DAYS = 3        # don't re-probe a failed model every day


@dataclass
class ScanReport:
    ok: bool = True
    error: str = ""
    scanned: int = 0
    new: list[str] = field(default_factory=list)
    added: list[str] = field(default_factory=list)
    rejected: list[str] = field(default_factory=list)
    deferred: list[str] = field(default_factory=list)
    retired: list[str] = field(default_factory=list)
    first_scan: bool = False

    def summary(self) -> str:
        if not self.ok:
            return f"Model scan skipped: {self.error}"
        return (f"Model scan: {self.scanned} models, {len(self.new)} new, {len(self.added)} added, "
                f"{len(self.rejected)} rejected, {len(self.deferred)} deferred, {len(self.retired)} retired")


class ModelScanner:
    def __init__(self, provider: LLMProvider, pool: ModelPool, state_path: Path, docs_dir: Path,
                 fallback_docs_dir: Path | None = None, max_auto: int = 6):
        self.provider, self.pool = provider, pool
        self.state_path, self.docs_dir = Path(state_path), Path(docs_dir)
        self.fallback_docs_dir = Path(fallback_docs_dir) if fallback_docs_dir else None
        self.max_auto = max_auto
        self.base_ids = set(pool.ids())  # the hand-picked pool is never touched by the scanner

    # ---- state -------------------------------------------------------
    def load_state(self) -> dict:
        try:
            return json.loads(self.state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"last_run": 0, "models": {}}

    def _save_state(self, state: dict) -> None:
        tmp = self.state_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
        tmp.replace(self.state_path)

    def load_into_pool(self) -> int:
        """Re-add previously auto-added models at startup so the pool survives restarts."""
        n = 0
        for mid, e in self.load_state()["models"].items():
            if e.get("status") == "added" and not self.pool.has(mid):
                self.pool.add(ModelSpec(mid, ROLE_ALTERNATE, bool(e.get("tools")), e.get("note", "auto-added")))
                n += 1
        return n

    def seconds_until_due(self, interval_s: float) -> float:
        return max(0.0, interval_s - (time.time() - self.load_state().get("last_run", 0)))

    # ---- scan --------------------------------------------------------
    async def scan(self) -> ScanReport:
        report = ScanReport()
        try:
            infos = await self.provider.describe_models()
        except Exception as e:
            return ScanReport(ok=False, error=f"could not list models ({type(e).__name__}: {e})")
        if not infos:
            return ScanReport(ok=False, error="provider returned an empty model list (no changes made)")

        state = self.load_state()
        models: dict = state["models"]
        now = time.time()
        report.scanned = len(infos)
        report.first_scan = not models
        live_ids = {i["id"] for i in infos}
        probes_left = MAX_PROBES_PER_SCAN
        auto_count = sum(1 for e in models.values() if e.get("status") == "added")

        for info in sorted(infos, key=lambda i: i["id"]):
            mid = info["id"]
            entry = models.get(mid)
            meta = {k: info.get(k) for k in ("owned_by", "context_window", "max_completion_tokens")}
            if entry is None:
                report.new.append(mid)
                entry = models[mid] = {"first_seen": now}
            entry.update(meta)
            entry["last_seen"] = now

            if mid in self.base_ids:
                entry["status"] = "default"
                continue
            if entry.get("status") == "added":
                if info.get("active") is False:  # gone dormant
                    self._retire(mid, entry, report, "reported inactive")
                elif not self.pool.has(mid):
                    self.pool.add(ModelSpec(mid, ROLE_ALTERNATE, bool(entry.get("tools")), entry.get("note", "auto-added")))
                continue

            kind, reason = classify(info)
            if kind != "chat":
                entry.update(status=kind, reason=reason)
                continue
            if entry.get("status") == "rejected" and now - entry.get("checked_at", 0) < REJECT_RETRY_DAYS * 86400:
                continue
            if auto_count >= self.max_auto:
                entry.update(status="pending", reason=f"auto-add limit ({self.max_auto}) reached")
                continue
            if probes_left <= 0:
                entry.update(status="pending", reason="queued for next scan")
                continue

            probes_left -= 1
            log.info("probing new model %s", mid)
            result = await probe_model(self.provider, mid)
            entry.update(checked_at=now, probe=result.to_dict())
            if result.status == "passed":
                note = f"auto-added {datetime.now(timezone.utc):%Y-%m-%d}; tools {'yes' if result.tools else 'no'}"
                self.pool.add(ModelSpec(mid, ROLE_ALTERNATE, result.tools, note))
                entry.update(status="added", tools=result.tools, note=note, reason="")
                report.added.append(mid)
                auto_count += 1
            elif result.status == "deferred":
                entry.update(status="pending", reason="rate limited while probing; will retry")
                report.deferred.append(mid)
            else:
                entry.update(status="rejected", reason=result.error or "probe failed")
                report.rejected.append(mid)

        for mid, entry in models.items():  # models Groq no longer lists
            if entry.get("status") == "added" and mid not in live_ids:
                self._retire(mid, entry, report, "no longer listed by Groq")

        state["last_run"] = now
        self._save_state(state)
        self._write_catalog(state, report)
        log.info(report.summary())
        return report

    def _retire(self, mid: str, entry: dict, report: ScanReport, reason: str) -> None:
        self.pool.remove(mid)
        entry.update(status="retired", reason=reason)
        report.retired.append(mid)

    # ---- documentation -------------------------------------------------
    def _write_catalog(self, state: dict, report: ScanReport) -> None:
        text = render_catalog(state, self.pool, report)
        for folder in [self.docs_dir, self.fallback_docs_dir]:
            if not folder:
                continue
            try:
                folder.mkdir(parents=True, exist_ok=True)
                (folder / CATALOG_NAME).write_text(text, encoding="utf-8")
                return
            except OSError as e:
                log.warning("cannot write catalog to %s: %s", folder, e)

    def status(self) -> dict:
        state = self.load_state()
        return {
            "last_run": state.get("last_run", 0),
            "pool": self.pool.ids(),
            "models": [{"id": k, **{f: v.get(f) for f in ("status", "reason", "tools", "context_window", "checked_at")}} for k, v in sorted(state["models"].items())],
        }


def render_catalog(state: dict, pool: ModelPool, report: ScanReport) -> str:
    when = datetime.fromtimestamp(state.get("last_run") or time.time(), timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    label = {"default": "In pool (default)", "added": "In pool (auto-added)", "rejected": "Rejected", "pending": "Pending",
             "excluded": "Not a chat model", "agent": "Agent system", "inactive": "Inactive", "retired": "Retired"}
    lines = [
        "# Groq model catalog", "",
        "Generated by LilyAi's scheduled model scan. Do not edit by hand: it is overwritten on every scan.", "",
        f"Last scan: {when}. {report.summary()}", "",
    ]
    if report.new and not report.first_scan:
        lines += ["New since the previous scan: " + ", ".join(f"`{m}`" for m in report.new), ""]
    lines += ["| Model | Owner | Context | Max output | Status | Tools | Notes |", "|---|---|---|---|---|---|---|"]
    for mid, e in sorted(state["models"].items()):
        if e.get("last_seen", 0) < (state.get("last_run") or 0) and e.get("status") != "retired":
            continue  # no longer listed
        spec = next((m for m in pool.all() if m.id == mid), None)
        flag = e.get("tools") if isinstance(e.get("tools"), bool) else (spec.supports_tools if spec else None)
        tools = {True: "yes", False: "no"}.get(flag, "-")
        note = e.get("reason") or ((e.get("probe") or {}).get("latency_ms") and f"probe {e['probe']['latency_ms']} ms") or ""
        lines.append(f"| `{mid}` | {e.get('owned_by') or '-'} | {e.get('context_window') or '-'} | {e.get('max_completion_tokens') or '-'} | {label.get(e.get('status'), e.get('status') or '-')} | {tools} | {note} |")
    lines += ["", "## How models are added", "",
              "A new chat model gets three probe calls against that exact model: a plain reply, an arithmetic check and a tool call. "
              "It joins the pool if the first two pass; tool support is recorded. Speech, guard and embedding models are skipped, "
              "and agent systems (`groq/compound*`) are never auto-added. Rejected models are retried after a few days.", ""]
    return "\n".join(lines)
