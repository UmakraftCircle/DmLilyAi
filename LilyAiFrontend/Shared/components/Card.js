import { h } from "/Shared/ui.js";

export const card = (title, ...body) => h("section", { class: "card" }, title ? h("h2", { class: "card-title" }, title) : null, ...body);
