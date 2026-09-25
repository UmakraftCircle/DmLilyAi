import { api } from "/Shared/api.js";
import { h, clear, page, errorBox, fmtNum } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";
import { stat } from "/Shared/components/Stat.js";

function circleCard(c) {
  return card(c.name,
    h("div", { class: "stats" }, stat("monthly rank", c.monthly_rank ?? "?"), stat("points", c.monthly_point ?? 0), stat("members", c.member_count ?? c.members.length)),
    c.members.length
      ? table(["trainer", "fans"], c.members.map((m) => [m.trainer_name || m.viewer_id, { num: fmtNum(m.total_fans) }]))
      : h("p", { class: "muted" }, "No member data yet."));
}

export function mount(root) {
  const body = h("div", {});
  async function load() {
    try {
      const d = await api("/api/leaderboard");
      clear(body).append(h("div", { class: "cols" }, ...d.circles.map(circleCard)));
    } catch (e) { clear(body).append(errorBox(e)); }
  }
  root.append(...page("Leaderboard", "Tracked uma.moe circle rank, points and member fan counts.", body));
  load();
}
