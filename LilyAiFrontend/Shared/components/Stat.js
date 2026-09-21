import { h, fmtNum } from "/Shared/ui.js";

export const stat = (label, value) => h("div", { class: "card stat" }, h("b", {}, fmtNum(value)), h("span", {}, label));
