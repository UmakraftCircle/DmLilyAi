/** Tiny DOM helper. Text is always set via textContent/createTextNode, never innerHTML. */
export function h(tag, props = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(props || {})) {
    if (v == null || v === false) continue;
    if (k === "class") node.className = v;
    else if (k.startsWith("on")) node.addEventListener(k.slice(2), v);
    else if (k in node && k !== "list") node[k] = v;
    else node.setAttribute(k, v === true ? "" : v);
  }
  for (const c of children.flat()) {
    if (c == null || c === false) continue;
    node.append(c.nodeType ? c : document.createTextNode(String(c)));
  }
  return node;
}

export const clear = (node) => { while (node.firstChild) node.firstChild.remove(); return node; };
export const fmtTime = (ts) => new Date(ts * 1000).toLocaleTimeString([], { hour12: false });
export const fmtNum = (n) => (n ?? 0).toLocaleString();
/** Signed number for gain/loss columns, e.g. "+1,204" / "-38" / "0". */
export const fmtDelta = (n) => `${(n ?? 0) > 0 ? "+" : ""}${(n ?? 0).toLocaleString()}`;
/** Calendar date (no time) for "last seen"-style columns. */
export const fmtDate = (ts) => (ts ? new Date(ts * 1000).toLocaleDateString([], { year: "numeric", month: "short", day: "numeric" }) : "\u2014");

export function page(title, lede, ...body) {
  return [h("header", { class: "page-head" }, h("h1", {}, title), lede ? h("p", {}, lede) : null), ...body];
}

export const errorBox = (err) => h("p", { class: "err", role: "alert" }, err.message || String(err));
