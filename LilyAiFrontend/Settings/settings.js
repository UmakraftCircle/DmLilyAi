import { h, clear, page } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { connectionCard } from "/Settings/cards/connectionCard.js";
import { modelsCard } from "/Settings/cards/modelsCard.js";
import { modelScanCard } from "/Settings/cards/modelScanCard.js";
import { webCard } from "/Settings/cards/webCard.js";

const TABS = [
  { id: "connection", label: "Connection", icon: "plug" },
  { id: "models", label: "Models", icon: "cpu" },
  { id: "scan", label: "Auto-scan", icon: "sparkle" },
  { id: "web", label: "Web search", icon: "search" },
];

/** Settings as one fixed-height page: an icon tab strip up top, one panel rendered
 * below at a time (mirrors Leaderboard's tabs/panel pattern). Each card is built once
 * so its loaded data and reload() survive switching tabs back and forth. */
export function mount(root) {
  root.classList.add("fill");

  const models = modelsCard();
  const scan = modelScanCard(() => models.reload());
  const web = webCard();
  const connection = connectionCard(() => { models.reload(); scan.reload(); });
  const panels = { connection, models: models.el, scan: scan.el, web: web.el };

  const state = { tab: "connection" };
  const tabs = h("div", { class: "set-tabs" });
  const body = h("div", { class: "set-body" });

  function renderTabs() {
    clear(tabs).append(...TABS.map((t) => h("button", {
      class: "set-tab",
      "aria-current": state.tab === t.id ? "page" : null,
      onclick: () => { state.tab = t.id; renderTabs(); renderBody(); },
    }, h("span", { class: "tile-icon" }, icon(t.icon, 18)), t.label)));
  }

  function renderBody() {
    clear(body).append(panels[state.tab]);
  }

  renderTabs();
  renderBody();
  root.append(...page("Settings", "Connection settings live in this browser only. Model and behaviour settings come from the server's environment variables.", tabs, body));
}
