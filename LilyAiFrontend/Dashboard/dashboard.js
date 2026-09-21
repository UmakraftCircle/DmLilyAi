import { api } from "/Shared/api.js";
import { h, clear, page, errorBox } from "/Shared/ui.js";
import { stat } from "/Shared/components/Stat.js";
import { toolsCard } from "/Dashboard/cards/toolsCard.js";
import { contextCard } from "/Dashboard/cards/contextCard.js";
import { knowledgeCard } from "/Dashboard/cards/knowledgeCard.js";
import { evaluationCard } from "/Dashboard/cards/evaluationCard.js";

export function mount(root) {
  const body = h("div", {});
  async function load() {
    try {
      const d = await api("/api/dashboard");
      const fb = d.learning.feedback;
      clear(body).append(
        h("div", { class: "stats" }, stat("users", d.users), stat("stored turns", d.turns), stat("user facts", d.facts), stat("active sessions", d.active_sessions), stat("knowledge chunks", d.rag.chunks), stat("thumbs up", fb.up), stat("thumbs down", fb.down)),
        h("div", { class: "cols" }, toolsCard(d), contextCard(d), knowledgeCard(d, load), evaluationCard()));
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  root.append(...page("Dashboard", "What LilyAi knows, remembers and has learned so far.", body));
  load();
}
