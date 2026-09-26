import { h } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";

export function mount(root) {
  root.append(
    h("section", { class: "hero hero--solo" },
      h("span", { class: "eyebrow" }, icon("sparkle", 14), "Intelligence portal"),
      h("h1", { class: "wordmark" }, "LILYAI"),
      h("p", { class: "hero-sub" }, "A DM-first AI agent with memory, tools, web search and knowledge. Chat with it, watch it work, and tune it from here."),
      h("div", { class: "hero-actions" },
        h("a", { class: "btn btn--lg", href: "#/chat" }, icon("chat", 22), "Chat with Lily"))));
}
