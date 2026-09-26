import { api } from "/Shared/api.js";
import { h, clear, page, errorBox } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { card } from "/Shared/components/Card.js";
import { eventRow } from "/Admin/Relay/eventRow.js";
import { createChannelThread } from "/Admin/Relay/channelThread.js";

const TABS = [
  { id: "log", label: "Log", icon: "relay" },
  { id: "channel", label: "Channel", icon: "chat" },
];

/** Relay as one fixed-height page with icon tabs (same shape as Settings/Dashboard): the
 * existing DM/system event Log, plus a new Channel tab - a live, two-way Discord-style thread
 * for whichever channel is picked in the drawer, with tap-to-reply. */
export function mount(root) {
  root.classList.add("fill");
  let after = 0, timer, paused = false;
  const feed = h("div", { class: "feed", role: "log" });
  const box = h("div", { class: "relay-box" }, feed);
  const status = h("span", { class: "muted" }, "connecting…");
  const source = h("select", { "aria-label": "Source filter", style: "width:auto" }, ["discord", "simulator", "web", "all"].map((s) => h("option", { value: s }, s)));
  const pause = h("button", { class: "btn ghost small", onclick: () => { paused = !paused; pause.textContent = paused ? "Resume" : "Pause"; } }, "Pause");
  source.addEventListener("change", () => { after = 0; feed.replaceChildren(); });

  async function poll() {
    if (!paused) {
      try {
        const r = await api(`/api/relay/events?after=${after}&source=${source.value}`);
        status.textContent = r.discord ? `Live bot: ${r.bot}` : "Discord bot not connected";
        const stick = box.scrollHeight - box.scrollTop - box.clientHeight < 60;
        for (const e of r.events) { after = Math.max(after, e.id); feed.append(eventRow(e)); }
        if (r.events.length && stick) box.scrollTop = box.scrollHeight;
      } catch (e) { status.replaceChildren(errorBox(e)); }
    }
    timer = setTimeout(poll, 2000);
  }

  const logPanel = card(null, h("div", { class: "row", style: "margin-bottom:14px" }, status, h("span", { class: "grow" }), source, pause), box);
  const channel = createChannelThread();
  const panels = { log: logPanel, channel: channel.el };

  const state = { tab: "log" };
  const tabs = h("div", { class: "set-tabs" });
  const body = h("div", { class: "set-body" });

  function renderTabs() {
    clear(tabs).append(...TABS.map((t) => h("button", {
      class: "set-tab",
      "aria-current": state.tab === t.id ? "page" : null,
      onclick: () => { state.tab = t.id; renderTabs(); renderBody(); },
    }, h("span", { class: "tile-icon" }, icon(t.icon, 18)), t.label)));
  }
  function renderBody() { clear(body).append(panels[state.tab]); }

  renderTabs();
  renderBody();
  root.append(...page("Relay", "Watch the live Discord bot: every DM in and out, plus connection events.", tabs, body));
  poll();
  channel.start();
  return () => { clearTimeout(timer); channel.stop(); };
}
