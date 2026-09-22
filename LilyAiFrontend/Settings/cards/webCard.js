import { api } from "/Shared/api.js";
import { h, clear, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";

/** Web search status + a manual query tester, mirroring the Knowledge card's tester. */
export function webCard() {
  const status = h("p", { class: "muted" }, "Loading…");
  const out = h("div", {});
  const q = h("input", { type: "text", placeholder: "Test a web search…", "aria-label": "Web search query" });

  async function loadStatus() {
    try {
      const c = await api("/api/config");
      clear(status).append(`Status: ${c.web_enabled ? "enabled" : "disabled"}.`);
    } catch (e) { clear(status).append(errorBox(e)); }
  }

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

  loadStatus();
  return { el: card("Web search", status, h("div", { class: "row", style: "margin-top:10px" }, h("div", { class: "grow" }, q), h("button", { class: "btn ghost small", onclick: run }, "Search")), out) };
}
