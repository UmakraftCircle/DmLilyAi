import { h } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";

export const toolsCard = (d) => card("Tools", d.learning.tools.length
  ? table(["tool", "calls", "failed", "avg ms"], d.learning.tools.map((t) => [t.tool, { num: t.calls }, { num: t.failures }, { num: t.avg_ms }]))
  : h("p", { class: "muted" }, `No tool calls yet. Registered: ${d.tools.join(", ")}`));
