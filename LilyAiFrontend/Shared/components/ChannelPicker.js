import { api } from "/Shared/api.js";
import { h, clear } from "/Shared/ui.js";
import { icon } from "/Shared/icons.js";

/** Drawer footer control: pick which Discord channel the bot mirrors into the Relay page's
 * Channel tab. The choice is saved server-side (RelayChannelStore), not per-browser, so it's
 * the same for every admin and survives a refresh or a restart. Hides itself entirely when
 * Discord isn't connected (nothing to pick a channel on). */
export function createChannelPicker() {
  const select = h("select", { "aria-label": "Watched Discord channel" }, h("option", { value: "" }, "Loading…"));
  const el = h("div", { class: "channel-picker", hidden: true },
    h("span", { class: "cp-label" }, icon("hash", 14), "Relay channel"), select);
  let channels = [];

  function fill(current) {
    clear(select).append(
      h("option", { value: "" }, "Not watching"),
      ...channels.map((c) => h("option", { value: String(c.channel_id), selected: c.channel_id === current }, `#${c.channel_name} · ${c.guild_name}`)));
  }

  async function load() {
    try {
      const [{ channels: list }, status] = await Promise.all([api("/api/relay/channels"), api("/api/relay/channel")]);
      channels = list;
      fill(status.channel_id);
      el.hidden = channels.length === 0;
    } catch {
      el.hidden = true; // Discord not connected, or the API isn't reachable yet
    }
  }

  select.addEventListener("change", async () => {
    const channel_id = select.value ? Number(select.value) : null;
    select.disabled = true;
    try { await api("/api/relay/channel", { method: "POST", body: { channel_id } }); }
    catch { await load(); } // roll the dropdown back to whatever's actually watched
    finally { select.disabled = false; }
  });

  return { el, load };
}
