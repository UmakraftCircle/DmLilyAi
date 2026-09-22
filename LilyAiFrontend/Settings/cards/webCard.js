import { api } from "/Shared/api.js";
import { h, clear, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { toast } from "/Shared/components/Toast.js";

/** Web search status + a manual query tester, mirroring the Knowledge card's tester. */
export function webCard(c) {
  const out = h("div", {});
  const q = h("input", { type: "text", placeholder: "Test a web search…", "aria-label": "Web search query" });
  const run = async () => {
    if (!q.value.trim()) return;
    try {
      const r = await api("/api/web/search", { method: "POST", body: { query: q.value } });
      clear(out).append(...(r.hits.length
        ? r.hits.map((x) => h("p", { class: "mono", style: "margin-top:8px" }, `${x.domain} — ${x.title}: ${x.snippet.slice(0, 160)}`))
        : [h("p", { class: "muted", style: "margin-top:8px" }, "No hits.")]));
    } catch (e) { clear(out).append(errorBox(e)); }
  };
  q.addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  return card("Web search",
    h("p", { class: "muted" }, `Status: ${c.web_enabled ? "enabled" : "disabled"}.`),
    h("div", { class: "row", style: "margin-top:10px" }, h("div", { class: "grow" }, q), h("button", { class: "btn ghost small", onclick: run }, "Search")),
    out);
}
