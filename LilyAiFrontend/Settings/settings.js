import { h, page } from "/Shared/ui.js";
import { connectionCard } from "/Settings/cards/connectionCard.js";
import { modelsCard } from "/Settings/cards/modelsCard.js";
import { modelScanCard } from "/Settings/cards/modelScanCard.js";
import { webCard } from "/Settings/cards/webCard.js";

export function mount(root) {
  const models = modelsCard();
  const scan = modelScanCard(() => models.reload());
  root.append(...page("Settings", "Connection settings live in this browser only. Model and behaviour settings come from the server's environment variables.",
    h("div", { class: "cols" }, connectionCard(() => { models.reload(); scan.reload(); }), models.el, scan.el, webCard().el)));
}
