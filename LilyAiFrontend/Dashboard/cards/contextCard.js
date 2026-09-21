import { h, fmtNum } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";

export const contextCard = (d) => {
  const c = d.learning.context;
  return card("Context and providers",
    h("p", {}, `Average prompt about ${fmtNum(c.avg_tokens)} tokens (max ${fmtNum(c.max_tokens)}); history trimmed ${fmtNum(c.trims)} times.`),
    h("p", { class: "muted", style: "margin-top:8px" }, `Provider: ${d.provider}. Discord: ${d.discord.connected ? "connected as " + d.discord.bot : "not connected"}.`));
};
