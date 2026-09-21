import { api } from "/Shared/api.js";
import { h } from "/Shared/ui.js";
import { card } from "/Shared/components/Card.js";
import { table } from "/Shared/components/Table.js";
import { toast } from "/Shared/components/Toast.js";

export function knowledgeCard(d, reload) {
  const sources = Object.entries(d.rag.sources);
  const name = h("input", { type: "text", placeholder: "Source name, e.g. handbook.md", "aria-label": "Source name" });
  const text = h("textarea", { rows: 5, placeholder: "Paste text to add to the knowledge base…", "aria-label": "Document text" });
  const remove = async (s) => { try { await api(`/api/rag/sources/${encodeURIComponent(s)}`, { method: "DELETE" }); reload(); } catch (e) { toast(e.message, "error"); } };
  const ingest = async () => {
    if (!name.value.trim() || !text.value.trim()) return toast("Add a name and some text first", "error");
    try { await api("/api/rag/ingest", { method: "POST", body: { source: name.value.trim(), text: text.value } }); toast("Ingested"); reload(); }
    catch (e) { toast(e.message, "error"); }
  };
  return card("Knowledge base",
    sources.length ? table(["source", "chunks", ""], sources.map(([s, n]) => [s, { num: n }, h("button", { class: "btn ghost small", onclick: () => remove(s) }, "Remove")])) : h("p", { class: "muted" }, "Empty."),
    h("label", {}, "Add a document"), name, h("div", { style: "height:8px" }), text,
    h("div", { class: "row", style: "margin-top:10px" }, h("button", { class: "btn", onclick: ingest }, "Ingest")));
}
