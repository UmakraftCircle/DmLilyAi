import { api } from "/Shared/api.js";
import { h, clear, errorBox } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";

export function modelsCard() {
  const body = h("div", {});
  async function load() {
    try {
      const c = await api("/api/config");
      clear(body).append(
        table(["model", "role", "tools", "note"], c.models.map((m) => [h("span", { class: "mono" }, m.id), m.role, m.supports_tools ? "yes" : "no", h("span", { class: "muted" }, m.note)])),
        h("p", { class: "muted", style: "margin-top:10px" }, `Chat: ${c.chat_model}. Reasoning: ${c.reasoning_model}. History ${c.history_turns} turns, ${c.token_budget} token budget. Web ${c.web_enabled ? "on" : "off"}, learning ${c.learn_from_chats ? "on" : "off"}. Provider: ${c.provider}. Allowlist: ${c.allowlist_size || "open"}.`));
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  load();
  return { el: card("Model pool", body), reload: load };
}
