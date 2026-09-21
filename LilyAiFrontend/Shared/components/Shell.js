import { h } from "/Shared/ui.js";
import { createDrawer } from "/Shared/components/Drawer.js";
import { createHeader } from "/Shared/components/Header.js";

/** App frame: drawer/sidebar + header + main. Pages mount into `main`. */
export function createShell({ routes }) {
  const desktop = matchMedia("(min-width: 900px)");
  let open = false;

  const drawer = createDrawer({ routes, onNavigate: () => setOpen(false), onClose: () => setOpen(false) });
  const header = createHeader({ onMenu: () => setOpen(!open) });
  const scrim = h("div", { class: "scrim", onclick: () => setOpen(false) });
  const main = h("main", { id: "main", class: "page", tabindex: "-1" });
  const el = h("div", { class: "app" }, drawer.el, scrim, h("div", { class: "content" }, header.el, main));

  function sync() {
    el.classList.toggle("drawer-open", open && !desktop.matches);
    drawer.el.inert = !desktop.matches && !open; // keep closed drawer out of tab order
    header.setExpanded(open);
  }
  function setOpen(v) { open = v; sync(); if (v) drawer.el.querySelector("a")?.focus(); }

  desktop.addEventListener("change", () => { open = false; sync(); });
  addEventListener("keydown", (e) => { if (e.key === "Escape" && open) setOpen(false); });
  sync();

  return {
    el, main,
    setCurrent(route) { drawer.setCurrent(route.id); header.setTitle(route.label); document.title = `${route.label} · LilyAi`; },
    close: () => setOpen(false),
  };
}
