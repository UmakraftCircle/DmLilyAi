import { api } from "/Shared/api.js";
import { h, clear, page, errorBox, fmtNum, fmtDeltaCompact, fmtDate } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";
import { stat } from "/Shared/components/Stat.js";

const PAGE_SIZE = 10;

function gain(n) {
  const cls = n > 0 ? "pos" : n < 0 ? "neg" : "zero";
  return h("span", { class: `gain ${cls}` }, fmtDeltaCompact(n));
}

/** Prev/number/Next pager. Page-count is whatever the caller hands it — club tabs naturally
 * cap at 3 (30-member roster / 10 per page), the Former Members tab is left uncapped. */
function pager(current, total, onPage) {
  if (total <= 1) return null;
  const numbered = [];
  for (let p = 1; p <= total; p++) {
    numbered.push(h("button", { class: `btn small ${p === current ? "" : "ghost"}`, onclick: () => onPage(p) }, String(p)));
  }
  return h("div", { class: "pager row" },
    h("button", { class: "btn small ghost", disabled: current === 1, onclick: () => onPage(current - 1) }, "\u2039 Prev"),
    ...numbered,
    h("button", { class: "btn small ghost", disabled: current === total, onclick: () => onPage(current + 1) }, "Next \u203a"));
}

function memberTable(members, current) {
  const start = (current - 1) * PAGE_SIZE;
  const rows = members.slice(start, start + PAGE_SIZE).map((m, i) => [
    { num: start + i + 1 },
    m.trainer_name || m.viewer_id,
    { num: fmtNum(m.total_fans) },
    { num: gain(m.daily_gain) },
    { num: gain(m.monthly_gain) },
  ]);
  return table(["#", "trainer", "fans", "daily gain", "monthly gain"], rows);
}

function formerTable(members, current) {
  const start = (current - 1) * PAGE_SIZE;
  const rows = members.slice(start, start + PAGE_SIZE).map((m) => [
    m.trainer_name || m.viewer_id,
    m.circle_name,
    { num: fmtNum(m.total_fans) },
    fmtDate(m.last_seen),
  ]);
  return table(["trainer", "club", "fans contributed", "last detected"], rows);
}

export function mount(root) {
  root.classList.add("fill");
  const body = h("div", { class: "lb-body" });
  const state = { tab: null, clubPages: {}, formerPage: 1 };
  let data = null;

  function render() {
    if (!data) return;
    if (!state.tab) state.tab = data.circles[0] ? `c:${data.circles[0].circle_id}` : "former";
    clear(body);

    const tabBtn = (label, id) => h("button", {
      class: `btn small ${state.tab === id ? "" : "ghost"}`,
      onclick: () => { state.tab = id; render(); },
    }, label);

    const tabs = h("div", { class: "lb-tabs row" },
      ...data.circles.map((c) => tabBtn(c.name, `c:${c.circle_id}`)),
      tabBtn("Former Members", "former"));

    let panel;
    if (state.tab === "former") {
      const list = data.former_members || [];
      const total = Math.max(1, Math.ceil(list.length / PAGE_SIZE));
      const cur = Math.min(state.formerPage, total);
      panel = h("div", { class: "lb-panel" },
        card("Former Members",
          list.length
            ? h("div", { class: "table-wrap" }, formerTable(list, cur))
            : h("p", { class: "muted" }, "No former members recorded yet.")),
        pager(cur, total, (p) => { state.formerPage = p; render(); }));
    } else {
      const circle = data.circles.find((c) => `c:${c.circle_id}` === state.tab) || data.circles[0];
      if (!circle) {
        panel = h("p", { class: "muted" }, "No circles tracked.");
      } else {
        const total = Math.max(1, Math.ceil(circle.members.length / PAGE_SIZE));
        const cur = Math.min(state.clubPages[circle.circle_id] || 1, total);
        panel = h("div", { class: "lb-panel" },
          card(circle.name,
            h("div", { class: "stats" },
              stat("monthly rank", circle.monthly_rank ?? "?"),
              stat("points", circle.monthly_point ?? 0),
              stat("members", circle.member_count ?? circle.members.length)),
            circle.members.length
              ? h("div", { class: "table-wrap" }, memberTable(circle.members, cur))
              : h("p", { class: "muted" }, "No member data yet.")),
          pager(cur, total, (p) => { state.clubPages[circle.circle_id] = p; render(); }));
      }
    }
    body.append(tabs, panel);
  }

  async function load() {
    try {
      data = await api("/api/leaderboard");
      render();
    } catch (e) { clear(body).append(errorBox(e)); }
  }

  root.append(...page("Leaderboard", "Tracked uma.moe circle rank, points, member fans and daily/monthly gains.", body));
  load();
}
