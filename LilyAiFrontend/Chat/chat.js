import { h, page } from "/Shared/ui.js";
import { createThread } from "/Chat/thread.js";

export function mount(root) {
  root.classList.add("fill");
  const thread = createThread({ userId: () => "web:admin", source: "web", displayName: () => "Admin" });
  root.append(...page("Chat", "Talk to Lily exactly as a Discord user would.", h("div", { class: "chatwrap" }, thread.el)));
  thread.focus();
}
