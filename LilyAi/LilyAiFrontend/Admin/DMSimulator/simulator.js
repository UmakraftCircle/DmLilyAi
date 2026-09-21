import { api } from "/Shared/api.js";
import { h, page } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { toast } from "/Shared/components/Toast.js";
import { createThread } from "/Chat/thread.js";
import { memoryPanel, ragPanel, tracePanel } from "/Admin/DMSimulator/panels.js";

export function mount(root) {
  const who = h("input", { type: "text", value: "alice", "aria-label": "Simulated user name" });
  const uid = () => `sim:${who.value.trim() || "alice"}`;

  const trace = tracePanel();
  const memory = memoryPanel(uid);
  const rag = ragPanel();
  const thread = createThread({
    userId: uid, source: "simulator", displayName: () => who.value,
    onReply: (res) => { trace.update(res); memory.refresh(); },
  });

  const resetUser = async () => {
    try { await api(`/api/memory/${encodeURIComponent(uid())}`, { method: "DELETE" }); thread.reset(); trace.clear(); memory.refresh(); toast("User reset"); }
    catch (e) { toast(e.message, "error"); }
  };
  who.addEventListener("change", () => { thread.reset(); trace.clear(); memory.refresh(); });

  const user = card("Simulated user", who,
    h("div", { class: "row", style: "margin-top:10px" }, h("button", { class: "btn danger small", onclick: resetUser }, "Reset this user")));

  root.classList.add("fill", "sim");
  root.append(...page("DM Simulator", "Each name is a separate user with its own memory. Test onboarding, memory, tools and knowledge from scratch.",
    h("div", { class: "chatwrap with-side simwrap" }, thread.el, h("aside", { class: "side" }, user, trace.el, memory.el, rag.el))));
  memory.refresh();
}
