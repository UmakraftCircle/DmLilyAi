import { api } from "/Shared/api.js";
import { h } from "/Shared/ui.js";

/** "SYSTEM: ONLINE" footer. Polls /api/health. */
export function createStatusBar() {
  const dot = h("span", { class: "dot" });
  const label = h("b", {}, "SYSTEM: CHECKING");
  const sub = h("small", {}, "");
  const el = h("div", { class: "status", role: "status" }, dot, h("div", {}, label, sub));
  let timer;

  async function check() {
    try {
      const r = await api("/api/health");
      dot.className = `dot ${r.discord ? "on" : "off"}`;
      label.replaceChildren("SYSTEM: ", h("span", { class: "ok" }, "ONLINE"));
      sub.textContent = r.discord ? "Discord bot connected" : "Discord bot not connected";
    } catch {
      dot.className = "dot off";
      label.replaceChildren("SYSTEM: ", h("span", { class: "bad" }, "OFFLINE"));
      sub.textContent = "Can't reach the API. Check Settings.";
    }
  }
  return { el, start() { check(); timer = setInterval(check, 15000); }, stop() { clearInterval(timer); } };
}
