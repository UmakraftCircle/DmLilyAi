/** Inline stroke icons (24x24). Add a name here, use it anywhere with icon("name"). */
const circle = (cx, cy, r) => `M${cx - r} ${cy}a${r} ${r} 0 1 0 ${2 * r} 0 ${r} ${r} 0 1 0-${2 * r} 0`;

const PATHS = {
  menu: ["M4 6h16M4 12h16M4 18h16"],
  close: ["M6 6l12 12M18 6L6 18"],
  home: ["M3 11l9-8 9 8", "M5 9.5V20h14V9.5"],
  chat: ["M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"],
  dashboard: ["M5 20v-9M12 20V4M19 20v-6"],
  settings: ["M4 6h9M17 6h3M4 12h3M11 12h9M4 18h11M19 18h1", circle(15, 6, 2), circle(9, 12, 2), circle(17, 18, 2)],
  relay: [circle(18, 5, 2), circle(6, 12, 2), circle(18, 19, 2), "M7.8 11l8.4-5M7.8 13l8.4 5"],
  simulator: ["M8 2h8a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z", "M11 18h2"],
  sparkle: ["M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z", "M19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"],
  send: ["M22 2L11 13", "M22 2l-7 20-4-9-9-4z"],
  sun: [circle(12, 12, 4), "M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"],
  moon: ["M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"],
  lock: ["M6 11h12v10H6z", "M8 11V7a4 4 0 0 1 8 0v4"],
  arrow: ["M5 12h14M13 6l6 6-6 6"],
  leaderboard: ["M4 20V11", "M10 20V4", "M16 20v-7"],
  plug: ["M9 2v6", "M15 2v6", "M6 8h12v3a6 6 0 0 1-12 0z", "M12 17v5"],
  cpu: ["M7 7h10v10H7z", "M12 3v4", "M12 17v4", "M3 12h4", "M17 12h4"],
  search: [circle(11, 11, 7), "M21 21l-4.3-4.3"],
  wrench: ["M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"],
  layers: ["M12 2 2 7l10 5 10-5-10-5z", "M2 17l10 5 10-5", "M2 12l10 5 10-5"],
  book: ["M4 19.5A2.5 2.5 0 0 1 6.5 17H20", "M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"],
  check: ["M20 6L9 17l-5-5"],
  reply: ["M9 17l-6-6 6-6", "M3 11h11a6 6 0 0 1 6 6v3"],
  hash: ["M5 9h14", "M5 15h14", "M9 3L7 21", "M17 3l-2 18"],
};

const NS = "http://www.w3.org/2000/svg";

export function icon(name, size = 20) {
  const svg = document.createElementNS(NS, "svg");
  for (const [k, v] of Object.entries({ viewBox: "0 0 24 24", width: size, height: size, fill: "none", stroke: "currentColor", "stroke-width": 1.8, "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true", class: "icon" })) svg.setAttribute(k, v);
  for (const d of PATHS[name] || []) {
    const p = document.createElementNS(NS, "path");
    p.setAttribute("d", d);
    svg.append(p);
  }
  return svg;
}
