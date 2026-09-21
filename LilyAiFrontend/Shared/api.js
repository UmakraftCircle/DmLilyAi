const KEY_API = "lily.api", KEY_TOKEN = "lily.token";

export const settings = {
  /** The site is served by the API itself, so the default is this page's own origin. */
  get base() { return (localStorage.getItem(KEY_API) || location.origin).replace(/\/$/, ""); },
  get token() { return localStorage.getItem(KEY_TOKEN) || ""; },
  save(base, token) {
    const url = base.trim().replace(/\/$/, "");
    if (!url || url === location.origin) localStorage.removeItem(KEY_API); else localStorage.setItem(KEY_API, url);
    localStorage.setItem(KEY_TOKEN, token.trim());
  },
};

export async function api(path, { method = "GET", body } = {}) {
  const headers = { "Content-Type": "application/json" };
  if (settings.token) headers.Authorization = `Bearer ${settings.token}`;
  let res;
  try {
    res = await fetch(settings.base + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  } catch {
    throw new Error(`Can't reach the API at ${settings.base}. Check Settings.`);
  }
  if (!res.ok) {
    let detail = res.statusText;
    try { const j = await res.json(); detail = typeof j.detail === "string" ? j.detail : JSON.stringify(j.detail); } catch {}
    throw new Error(`${res.status}: ${detail}`);
  }
  return res.json();
}
