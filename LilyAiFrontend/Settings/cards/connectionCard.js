import { api, settings } from "/Shared/api.js";
import { h } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";

export function connectionCard(onConnected) {
  const base = h("input", { type: "text", value: settings.base, "aria-label": "API URL", inputMode: "url" });
  const token = h("input", { type: "password", value: settings.token, placeholder: "ADMIN_TOKEN", "aria-label": "Admin token", autocomplete: "off" });
  const result = h("p", { style: "margin-top:10px", role: "status" });
  const save = async () => {
    settings.save(base.value, token.value);
    try { await api("/api/auth-check"); result.className = ""; result.textContent = "Connected."; onConnected(); }
    catch (e) { result.className = "err"; result.textContent = e.message; }
  };
  return card("API connection", h("p", { class: "muted" }, "Stored in this browser only. Leave the API URL as it is unless the API runs on a different address."),
    h("label", {}, "API URL"), base, h("label", {}, "Admin token"), token,
    h("div", { class: "row", style: "margin-top:14px" }, h("button", { class: "btn", onclick: save }, "Save and test")), result);
}
