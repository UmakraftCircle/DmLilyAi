import { api } from "/Shared/api.js";
import { h, clear, page, errorBox, fmtNum, fmtDelta, fmtAgo, fmtDate } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";
import { stat } from "/Shared/components/Stat.js";

const CIRCLE_PAGE_SIZE = 5;
const FORMER_PAGE_SIZE = 10;

function gain(n) {
  const cls = n > 0 ? "pos" : n < 0 ? "neg" : "zero";
  return h("span", { class: `gain ${cls}` }, fmtDelta(n));
}

/** Prev/number/Next pager. Page-count is whatever the caller hands it — club tabs naturally
 * cap at 6 (30-member roster / 5 per page), the Former Members tab is left uncapped. */
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

const RANK_CLASS = { 1: "gold", 2: "silver", 3: "bronze" };

/** One trainer entry, styled after uma.moe's own circle page: name/id up top, total +
 * monthly gain, then two two-up rows (today/daily gain, 7-day avg/last updated). Card
 * layout (not a table) so it never needs to scroll sideways on a phone. */
function memberCard(m, rank) {
  return h("article", { class: "lb-card" },
    h("div", { class: "lb-card-top" },
      h("span", { class: `lb-rank ${RANK_CLASS[rank] || ""}` }, `#${rank}`),
      h("div", { class: "lb-who" },
        h("div", { class: "lb-name" }, m.trainer_name || String(m.viewer_id)),
        h("div", { class: "lb-id" }, `ID ${m.viewer_id}`)),
      h("span", { class: "pill" }, "Member")),
    h("div", { class: "lb-row" },
      h("span", { class: "lb-label" }, "Total Fans"),
      h("span", { class: "lb-value" }, fmtNum(m.total_fans))),
    h("div", { class: "lb-row" },
      h("span", { class: "lb-label accent" }, "Monthly Gain"),
      h("span", { class: "lb-value" }, gain(m.monthly_gain))),
    h("div", { class: "lb-split" },
      h("div", { class: "lb-cell" },
        h("span", { class: "lb-label" }, "Today"),
        h("span", { class: "lb-value" }, gain(m.today_gain))),
      h("div", { class: "lb-cell" },
        h("span", { class: "lb-label" }, "Daily Gain"),
        h("span", { class: "lb-value" }, gain(m.daily_gain)))),
    h("div", { class: "lb-split" },
      h("div", { class: "lb-cell" },
        h("span", { class: "lb-label" }, "7 Day Avg", h("small", {}, " (resets Mon)")),
        h("span", { class: "lb-value" }, m.week_avg == null ? "\u2014" : gain(m.week_avg))),
      h("div", { class: "lb-cell" },
        h("span", { class: "lb-label" }, "Last Updated"),
        h("span", { class: "lb-value muted" }, fmtAgo(m.last_updated)))));
}

function memberCards(members, current) {
  const start = (current - 1) * CIRCLE_PAGE_SIZE;
  return h("div", { class: "lb-cards" },
    ...members.slice(start, start + CIRCLE_PAGE_SIZE).map((m, i) => memberCard(m, start + i + 1)));
}

function formerTable(members, current) {
  const start = (current - 1) * FORMER_PAGE_SIZE;
  const rows = members.slice(start, start + FORMER_PAGE_SIZE).map((m) => [
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
      const total = Math.max(1, Math.ceil(list.length / FORMER_PAGE_SIZE));
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
        const total = Math.max(1, Math.ceil(circle.members.length / CIRCLE_PAGE_SIZE));
        const cur = Math.min(state.clubPages[circle.circle_id] || 1, total);
        panel = h("div", { class: "lb-panel" },
          h("div", { class: "stats" },
            stat("monthly rank", circle.monthly_rank ?? "?"),
            stat("points", circle.monthly_point ?? 0),
            stat("members", circle.member_count ?? circle.members.length)),
          circle.members.length
            ? memberCards(circle.members, cur)
            : h("p", { class: "muted" }, "No member data yet."),
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
