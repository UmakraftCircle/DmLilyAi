import { api } from "/Shared/api.js";
import { h, clear, errorBox, fmtNum } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";

/** Trace of the last reply. */
export function tracePanel() {
  const dl = h("dl", { class: "trace" }, h("dd", { class: "muted" }, "Send a message to see its trace."));
  return {
    el: card("Last reply", dl),
    update(res) {
      const m = res.messages.find((x) => x.meta?.model) || res.messages[0];
      const meta = m?.meta || {};
      clear(dl);
      const rows = [["kind", m?.kind], ["model", meta.model], ["tools", (meta.tools || []).join(", ") || "none"], ["web domains", (meta.domains || []).join(", ") || "none"], ["prompt tokens (est.)", meta.tokens], ["latency", meta.ms != null ? `${meta.ms} ms` : ""]];
      for (const [k, v] of rows) if (v !== "" && v != null) dl.append(h("dt", {}, k), h("dd", {}, String(v)));
    },
    clear: () => clear(dl).append(h("dd", { class: "muted" }, "Send a message to see its trace.")),
  };
}

/** Stored facts for the simulated user. */
export function memoryPanel(userId) {
  const body = h("div", {});
  async function refresh() {
    try {
      const m = await api(`/api/memory/${encodeURIComponent(userId())}`);
      clear(body).append(
        m.facts.length ? h("ul", { class: "plain" }, m.facts.map((f) => h("li", {}, f.fact, " ", h("span", { class: "pill" }, f.source)))) : h("p", { class: "muted" }, "No facts stored."),
        h("p", { class: "muted", style: "margin-top:8px" }, `${fmtNum(m.turns)} stored turns`));
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  return { el: card("Memory", body), refresh };
}

/** Quick RAG query tester. */
export function ragPanel() {
  const out = h("div", {});
  const q = h("input", { type: "text", placeholder: "Test a knowledge query…", "aria-label": "RAG query" });
  const run = async () => {
    if (!q.value.trim()) return;
    try {
      const r = await api("/api/rag/search", { method: "POST", body: { query: q.value } });
      clear(out).append(...(r.hits.length ? r.hits.map((x) => h("p", { class: "mono", style: "margin-top:8px" }, `${x.score} ${x.source}: ${x.text.slice(0, 160)}`)) : [h("p", { class: "muted", style: "margin-top:8px" }, "No hits.")]));
    } catch (e) { clear(out).append(errorBox(e)); }
  };
  q.addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  return { el: card("Knowledge test", h("div", { class: "row" }, h("div", { class: "grow" }, q), h("button", { class: "btn ghost small", onclick: run }, "Search")), out) };
}
