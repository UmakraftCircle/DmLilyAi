import { h } from "/Shared/ui.js";

let box;
export function toast(message, kind = "info", ms = 4200) {
  if (!box) { box = h("div", { class: "toasts", role: "status", "aria-live": "polite" }); document.body.append(box); }
  const t = h("div", { class: `toast ${kind === "error" ? "bad" : ""}` }, message);
  box.append(t);
  setTimeout(() => t.remove(), ms);
}
