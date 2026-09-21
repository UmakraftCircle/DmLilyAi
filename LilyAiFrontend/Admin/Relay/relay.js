import { api } from "/Shared/api.js";
import { h, page, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { eventRow } from "/Admin/Relay/eventRow.js";

export function mount(root) {
  let after = 0, timer, paused = false;
  const feed = h("div", { class: "feed", role: "log" });
  const box = h("div", { class: "relay-box" }, feed);
  const status = h("span", { class: "muted" }, "connecting…");
  const dot = h("span", { class: "dot" });
  const source = h("select", { "aria-label": "Source filter", style: "width:auto" }, ["discord", "simulator", "web", "all"].map((s) => h("option", { value: s }, s)));
  const pause = h("button", { class: "btn ghost small", onclick: () => { paused = !paused; pause.textContent = paused ? "Resume" : "Pause"; } }, "Pause");
  source.addEventListener("change", () => { after = 0; feed.replaceChildren(); });

  async function poll() {
    if (!paused) {
      try {
        const r = await api(`/api/relay/events?after=${after}&source=${source.value}`);
        dot.className = `dot ${r.discord ? "on" : "off"}`;
        status.textContent = r.discord ? `Live bot: ${r.bot}` : "Discord bot not connected";
        const stick = box.scrollHeight - box.scrollTop - box.clientHeight < 60;
        for (const e of r.events) { after = Math.max(after, e.id); feed.append(eventRow(e)); }
        if (r.events.length && stick) box.scrollTop = box.scrollHeight;
      } catch (e) { status.replaceChildren(errorBox(e)); dot.className = "dot off"; }
    }
    timer = setTimeout(poll, 2000);
  }

  root.append(...page("Relay", "Watch the live Discord bot: every DM in and out, plus connection events.",
    h("div", { class: "row", style: "margin-bottom:14px" }, dot, status, h("span", { class: "grow" }), source, pause),
    card(null, box)));
  poll();
  return () => clearTimeout(timer);
}
