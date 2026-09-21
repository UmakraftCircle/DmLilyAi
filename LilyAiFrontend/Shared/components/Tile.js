import { h } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";

/** Navigation/feature tile. `locked` renders a disabled tile with a lock badge (for role-gated features). */
export function Tile({ icon: name, label, desc, href, current = false, locked = false, variant = "", onClick }) {
  const body = [
    h("span", { class: "tile-icon" }, icon(name, 22)),
    h("span", {}, label, desc && variant === "card" ? h("small", {}, desc) : null),
    locked ? h("span", { class: "lock", title: "Locked" }, icon("lock", 14)) : null,
  ];
  const cls = `tile ${variant === "card" ? "tile--card" : ""} ${locked ? "locked" : ""}`;
  if (locked) return h("div", { class: cls, "aria-disabled": "true" }, body);
  return h("a", { class: cls, href, "aria-current": current ? "page" : null, onclick: onClick }, body);
}
