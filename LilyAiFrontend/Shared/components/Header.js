import { settings } from "/Shared/api.js";
import { h } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";
import { currentTheme, toggleTheme } from "/Shared/theme.js";

export function createHeader({ onMenu }) {
  const menuBtn = h("button", { class: "icon-btn menu-btn", "aria-label": "Open menu", "aria-controls": "drawer", "aria-expanded": "false", onclick: onMenu }, icon("menu", 22));
  const title = h("h2", { class: "header-title" }, "LilyAi");

  const themeBtn = h("button", { class: "icon-btn", onclick: () => { toggleTheme(); paintTheme(); } });
  function paintTheme() {
    const dark = currentTheme() === "dark";
    themeBtn.replaceChildren(icon(dark ? "sun" : "moon"));
    themeBtn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }
  paintTheme();

  const secured = !!settings.token;
  const chip = h("a", { class: "user-chip", href: "#/settings", "aria-label": "Connection settings" },
    h("div", {}, h("b", {}, "Admin"), h("span", { class: "tag" }, secured ? "TOKEN" : "LOCAL")),
    icon(secured ? "lock" : "settings", 18));

  const el = h("header", { class: "header" }, menuBtn, title, h("span", { class: "spacer" }), themeBtn, chip);
  return {
    el,
    setTitle(t) { title.textContent = t; },
    setExpanded(open) { menuBtn.setAttribute("aria-expanded", String(open)); },
  };
}
