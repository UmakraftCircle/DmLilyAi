import { api } from "/Shared/api.js";
import { h, clear, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";

export function evaluationCard() {
  const out = h("div", { style: "margin-top:10px" });
  const btn = h("button", { class: "btn", onclick: async () => {
    btn.disabled = true; clear(out).append("Running…");
    try {
      const r = await api("/api/eval/run", { method: "POST" });
      clear(out).append(h("p", {}, h("b", {}, `${r.passed}/${r.total} passed`)), ...r.outcomes.map((o) => h("p", { class: o.passed ? "" : "err" }, `${o.passed ? "✓" : "✗"} ${o.name}${o.reason ? ": " + o.reason : ""}`)));
    } catch (e) { clear(out).append(errorBox(e)); }
    btn.disabled = false;
  } }, "Run checks");
  return card("Evaluation", h("p", { class: "muted", style: "margin-bottom:12px" }, "Runs the built-in prompt checks through the live chat workflow."), btn, out);
}
