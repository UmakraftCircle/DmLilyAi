import { api } from "/Shared/api.js";
import { h, clear } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { toast } from "/Shared/components/Toast.js";

/** Reusable chat thread (used by Chat and the DM Simulator). All messages go through POST /api/chat. */
export function createThread({ userId, source, displayName, placeholder = "Message Lily…", onReply }) {
  const msgs = h("div", { class: "msgs", "aria-live": "polite", "aria-label": "Conversation" });
  const input = h("textarea", { placeholder, rows: 1, "aria-label": "Message" });
  const send = h("button", { class: "btn", "aria-label": "Send message" }, icon("send", 20));
  let busy = false;

  const emptyState = () => h("div", { class: "empty" }, h("div", { class: "logo-mark" }, icon("sparkle", 26)), h("b", {}, "Say hello"), h("p", {}, "Messages here take the same path as Discord DMs."));
  const reset = () => { clear(msgs).append(emptyState()); };
  reset();

  const scroll = () => { msgs.scrollTop = msgs.scrollHeight; };
  function add(cls, text) {
    msgs.querySelector(".empty")?.remove();
    const b = h("div", { class: `bubble ${cls}` }, text);
    msgs.append(b); scroll();
    return b;
  }

  function autosize() { input.style.height = "auto"; input.style.height = `${Math.min(input.scrollHeight, 160)}px`; }

  async function submit(text) {
    text = (text ?? input.value).trim();
    if (!text || busy) return;
    busy = true; send.disabled = true; input.value = ""; autosize();
    add("me", text);
    const pending = add("system", "Thinking…");
    try {
      const res = await api("/api/chat", { method: "POST", body: { text, user_id: userId(), display_name: displayName?.() || "", source } });
      pending.remove();
      res.messages.forEach(render);
      onReply?.(res);
    } catch (e) {
      pending.remove();
      toast(e.message, "error");
    }
    busy = false; send.disabled = false; input.focus();
  }

  function render(m) {
    add(m.kind === "system" ? "system" : "bot", m.text);
    if (m.meta?.tools?.length) msgs.append(h("div", { class: "tools" }, m.meta.tools.map((t) => h("span", { class: "pill mono" }, t))));
    if (m.reply_id) {
      const rate = h("div", { class: "rate" });
      for (const [label, rating, name] of [["👍", 1, "Good reply"], ["👎", -1, "Bad reply"]]) {
        rate.append(h("button", { "aria-label": name, onclick: async () => {
          try {
            const r = await api("/api/feedback", { method: "POST", body: { user_id: userId(), reply_id: m.reply_id, rating } });
            rate.replaceChildren(h("span", { class: "muted" }, r.message));
          } catch (e) { toast(e.message, "error"); }
        } }, label));
      }
      msgs.append(rate);
    }
    if (m.menu?.length) msgs.append(h("div", { class: "chips" }, m.menu.map((i) => h("button", { class: "chip", onclick: () => submit(i.text) }, i.label))));
    scroll();
  }

  send.addEventListener("click", () => submit());
  input.addEventListener("input", autosize);
  input.addEventListener("keydown", (e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submit(); } });

  const el = h("section", { class: "card thread" }, msgs, h("div", { class: "compose" }, input, send));
  return { el, reset, say: submit, focus: () => input.focus() };
}
