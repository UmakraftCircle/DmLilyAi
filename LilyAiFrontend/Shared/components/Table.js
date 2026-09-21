import { h } from "/Shared/ui.js";

/** rows: array of arrays. A cell can be a string/number/Node, or {num: value} for right-aligned numbers. */
export function table(headers, rows) {
  return h("div", { class: "table-wrap" }, h("table", {},
    h("thead", {}, h("tr", {}, headers.map((t) => h("th", {}, t)))),
    h("tbody", {}, rows.map((r) => h("tr", {}, r.map((c) => (c && c.num !== undefined ? h("td", { class: "num" }, c.num) : h("td", {}, c))))))));
}
