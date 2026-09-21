import { api, settings } from "/Shared/api.js";
import { ROUTES } from "/Shared/routes.js";
import { h } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { Tile } from "/Shared/components/Tile.js";
import { stat } from "/Shared/components/Stat.js";

export function mount(root) {
  const live = h("div", {});
  const explore = h("section", { class: "explore", id: "explore" },
    h("h2", { class: "section-title" }, "Explore"),
    h("div", { class: "tile-grid" }, ROUTES.filter((r) => r.id !== "home").map((r) =>
      Tile({ icon: r.icon, label: r.label, desc: r.desc, href: `#/${r.id}`, variant: "card" }))));

  root.append(
    h("section", { class: "hero" },
      h("span", { class: "eyebrow" }, icon("sparkle", 14), "Intelligence portal"),
      h("h1", { class: "wordmark" }, "LILYAI"),
      h("p", { class: "hero-sub" }, "A DM-first AI agent with memory, tools, web search and knowledge. Chat with it, watch it work, and tune it from here."),
      h("div", { class: "hero-actions" },
        h("a", { class: "btn btn--lg", href: "#/chat" }, icon("chat", 22), "Chat with Lily"),
        h("button", { class: "btn ghost btn--lg", onclick: () => explore.scrollIntoView({ behavior: "smooth", block: "start" }) }, icon("menu", 20), "Explore apps"))),
    live, explore);

  (async () => {
    try {
      const d = await api("/api/dashboard");
      live.append(h("div", { class: "stats" }, stat("users", d.users), stat("stored turns", d.turns), stat("knowledge chunks", d.rag.chunks), stat("active sessions", d.active_sessions)));
    } catch (e) {
      live.append(h("div", { class: "card banner" },
        h("div", { class: "grow" }, h("b", {}, "Not connected to the API"), h("p", { class: "muted" }, `${e.message} (looking at ${settings.base})`)),
        h("a", { class: "btn small", href: "#/settings" }, "Open settings")));
    }
  })();
}
