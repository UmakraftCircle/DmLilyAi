import { api } from "/Shared/api.js";
import { h, clear, page, errorBox } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { stat } from "/Shared/components/Stat.js";
import { toolsCard } from "/Dashboard/cards/toolsCard.js";
import { contextCard } from "/Dashboard/cards/contextCard.js";
import { knowledgeCard } from "/Dashboard/cards/knowledgeCard.js";
import { evaluationCard } from "/Dashboard/cards/evaluationCard.js";

const TABS = [
  { id: "tools", label: "Tools", icon: "wrench" },
  { id: "context", label: "Context", icon: "layers" },
  { id: "knowledge", label: "Knowledge", icon: "book" },
  { id: "eval", label: "Evaluation", icon: "check" },
];

/** Dashboard as one fixed-height page: the stat grid stays pinned at the top, an icon tab
 * strip below it, then a single scrolling panel (Tools / Context / Knowledge / Evaluation)
 * rendered one at a time - same shape as Settings. Cards are rebuilt on every load() (as
 * before) since they render server data that can change (tool stats, knowledge sources). */
export function mount(root) {
  root.classList.add("fill");
  const stats = h("div", { class: "stats" });
  const tabs = h("div", { class: "set-tabs" });
  const body = h("div", { class: "set-body" });
  const state = { tab: "tools" };
  let panels = null;

  function renderTabs() {
    clear(tabs).append(...TABS.map((t) => h("button", {
      class: "set-tab",
      "aria-current": state.tab === t.id ? "page" : null,
      onclick: () => { state.tab = t.id; renderTabs(); renderBody(); },
    }, h("span", { class: "tile-icon" }, icon(t.icon, 18)), t.label)));
  }

  function renderBody() {
    if (panels) clear(body).append(panels[state.tab]);
  }

  async function load() {
    try {
      const d = await api("/api/dashboard");
      const fb = d.learning.feedback;
      clear(stats).append(stat("users", d.users), stat("stored turns", d.turns), stat("user facts", d.facts), stat("active sessions", d.active_sessions), stat("knowledge chunks", d.rag.chunks), stat("thumbs up", fb.up), stat("thumbs down", fb.down));
      panels = { tools: toolsCard(d), context: contextCard(d), knowledge: knowledgeCard(d, load), eval: evaluationCard() };
      renderTabs();
      renderBody();
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  root.append(...page("Dashboard", "What LilyAi knows, remembers and has learned so far.", stats, tabs, body));
  load();
}
