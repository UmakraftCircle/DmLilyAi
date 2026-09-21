import { api } from "/Shared/api.js";
import { h, clear, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";

const INTERESTING = ["added", "rejected", "pending", "retired"];

export function modelScanCard(onScanned) {
  const body = h("div", {});
  async function load() {
    try {
      const s = await api("/api/models/scan");
      const last = s.last_run ? new Date(s.last_run * 1000).toLocaleString() : "never";
      const counts = {};
      for (const m of s.models) counts[m.status] = (counts[m.status] || 0) + 1;
      const rows = s.models.filter((m) => INTERESTING.includes(m.status));
      const out = h("p", { class: "muted", style: "margin-top:10px", role: "status" });
      const btn = h("button", { class: "btn", onclick: async () => {
        btn.disabled = true; out.className = "muted"; out.textContent = "Scanning and probing new models…";
        try {
          const r = await api("/api/models/scan", { method: "POST" });
          out.className = r.ok ? "" : "err"; out.textContent = r.summary; load(); onScanned?.();
        } catch (e) { out.className = "err"; out.textContent = e.message; }
        btn.disabled = false;
      } }, "Scan now");
      clear(body).append(
        h("p", {}, `${s.enabled ? `Runs every ${s.interval_hours} h` : "Scheduled scan is off"}. Last scan: ${last}.`),
        h("p", { class: "muted", style: "margin:4px 0 10px" }, Object.entries(counts).map(([k, v]) => `${v} ${k}`).join(", ") || "No scan data yet."),
        rows.length ? table(["model", "status", "note"], rows.map((m) => [h("span", { class: "mono" }, m.id), m.status, h("span", { class: "muted" }, m.reason || (m.tools ? "tools" : ""))])) : null,
        h("div", { class: "row", style: "margin-top:12px" }, btn), out);
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  load();
  return { el: card("Groq model auto-scan", body), reload: load };
}
