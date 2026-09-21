import { h, fmtTime } from "/Shared/ui.js";

export function eventRow(e) {
  const who = e.kind === "dm_out" ? "Lily" : (e.name || e.user_id || "system");
  return h("div", { class: "ev" },
    h("span", { class: "muted" }, fmtTime(e.ts)),
    h("span", { class: `k-${e.kind}` }, e.kind),
    h("span", { class: "muted" }, e.source),
    h("span", { class: "t" }, `${who}: ${e.text}`));
}
