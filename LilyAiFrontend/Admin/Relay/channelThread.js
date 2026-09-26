import { api } from "/Shared/api.js";
import { h, clear } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { toast } from "/Shared/components/Toast.js";

/** Discord-style live chat for whichever channel is currently being watched (picked from the
 * drawer's channel picker). Polls /api/relay/channel/messages for new messages and posts via
 * /api/relay/channel/send - tapping "Reply" under any message sends Discord's own reply
 * (message reference), the same as replying in the Discord app itself. */
export function createChannelThread() {
  const msgs = h("div", { class: "msgs", "aria-live": "polite", "aria-label": "Channel" });
  const replyBanner = h("div", { class: "reply-banner", hidden: true });
  const input = h("textarea", { placeholder: "Message the channel…", rows: 1, "aria-label": "Message" });
  const send = h("button", { class: "btn", "aria-label": "Send message" }, icon("send", 20));

  let replyTo = null; // {message_id, author, text}
  let currentChannelId = null;
  let seenAny = false;
  let after = 0;
  let timer = null;

  const emptyState = (text) => h("div", { class: "empty" }, h("div", { class: "logo-mark" }, icon("chat", 26)), h("p", {}, text));
  const scroll = () => { msgs.scrollTop = msgs.scrollHeight; };

  function setReply(m) {
    replyTo = m ? { message_id: m.message_id, author: m.author || "message", text: m.text || "" } : null;
    replyBanner.hidden = !replyTo;
    if (!replyTo) { clear(replyBanner); return; }
    clear(replyBanner).append(
      h("div", { class: "grow" }, h("small", {}, `Replying to ${replyTo.author}`), h("p", {}, replyTo.text.slice(0, 100))),
      h("button", { class: "icon-btn", "aria-label": "Cancel reply", onclick: () => setReply(null) }, icon("close", 16)));
  }

  function bubble(m) {
    const wrap = h("div", { class: "bubble-wrap" });
    if (m.reply_to) wrap.append(h("div", { class: "reply-quote" }, h("b", {}, m.reply_to.author || "a message"), " " + (m.reply_to.text || "")));
    wrap.append(
      h("div", { class: `bubble ${m.is_me ? "me" : "bot"}` },
        !m.is_me ? h("b", { class: "bubble-author" }, m.author) : null,
        h("div", {}, m.text || h("i", {}, "(no text)"))),
      h("button", { class: "bubble-reply", onclick: () => setReply(m) }, icon("reply", 13), "Reply"));
    return wrap;
  }

  function render(list) {
    msgs.querySelector(".empty")?.remove();
    list.forEach((m) => msgs.append(bubble(m)));
    scroll();
  }

  async function poll() {
    let r;
    try { r = await api(`/api/relay/channel/messages?after=${after}`); }
    catch { return; } // stay quiet on background polling errors, same as the Log tab's feed

    if (r.channel_id !== currentChannelId) { currentChannelId = r.channel_id; after = 0; seenAny = false; clear(msgs); }
    if (!r.channel_id) { clear(msgs).append(emptyState("No channel is being watched. Pick one from the drawer.")); return; }
    if (r.messages.length) { seenAny = true; after = r.messages[r.messages.length - 1].id; render(r.messages); }
    else if (!seenAny) { clear(msgs).append(emptyState(`Watching #${r.channel_name} — no messages yet.`)); }
  }

  function autosize() { input.style.height = "auto"; input.style.height = `${Math.min(input.scrollHeight, 160)}px`; }

  async function submit() {
    const text = input.value.trim();
    if (!text) return;
    send.disabled = true;
    try {
      await api("/api/relay/channel/send", { method: "POST", body: { text, reply_to: replyTo?.message_id ?? null } });
      input.value = ""; autosize(); setReply(null);
      poll();
    } catch (e) { toast(e.message, "error"); }
    send.disabled = false; input.focus();
  }

  send.addEventListener("click", submit);
  input.addEventListener("input", autosize);
  input.addEventListener("keydown", (e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submit(); } });

  clear(msgs).append(emptyState("Loading…"));
  const el = h("section", { class: "card thread" }, msgs, replyBanner, h("div", { class: "compose" }, input, send));

  return {
    el,
    start() { poll(); timer = setInterval(poll, 3000); },
    stop() { clearInterval(timer); },
  };
}
