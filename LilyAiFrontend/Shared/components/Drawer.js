import { h } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { Tile } from "/Shared/components/Tile.js";
import { createStatusBar } from "/Shared/components/StatusBar.js";

/** Slide-in drawer on phones, permanent sidebar on wide screens (same DOM, CSS decides). */
export function createDrawer({ routes, onNavigate, onClose }) {
  const status = createStatusBar();
  const tiles = new Map();
  const groups = [];
  for (const r of routes) {
    const name = r.group || "";
    let g = groups.find((x) => x.name === name);
    if (!g) groups.push((g = { name, routes: [] }));
    g.routes.push(r);
  }

  const nav = h("nav", { class: "drawer-nav", "aria-label": "Sections" });
  for (const g of groups) {
    if (g.name) nav.append(h("div", { class: "nav-group" }, g.name));
    nav.append(h("div", { class: "tile-grid" }, g.routes.map((r) => {
      const t = Tile({ icon: r.icon, label: r.label, href: `#/${r.id}`, onClick: onNavigate });
      tiles.set(r.id, t);
      return t;
    })));
  }

  const el = h("aside", { class: "drawer", id: "drawer", "aria-label": "Main menu" },
    h("div", { class: "drawer-head" },
      h("span", { class: "logo-mark" }, icon("sparkle", 22)),
      h("div", {}, h("b", {}, "LILYAI"), h("small", {}, "Intelligence portal")),
      h("button", { class: "icon-btn", "aria-label": "Close menu", onclick: onClose }, icon("close"))),
    nav,
    h("div", { class: "drawer-foot" }, status.el));

  status.start();
  return {
    el,
    setCurrent(id) { for (const [k, t] of tiles) k === id ? t.setAttribute("aria-current", "page") : t.removeAttribute("aria-current"); },
  };
}
