const KEY = "lily.theme";
const root = document.documentElement;

export const currentTheme = () => root.dataset.theme || "dark";

export function setTheme(theme) {
  root.dataset.theme = theme;
  try { localStorage.setItem(KEY, theme); } catch {}
  document.querySelector('meta[name="theme-color"]')?.setAttribute("content", theme === "light" ? "#f4f3ff" : "#090b17");
}

export const toggleTheme = () => { setTheme(currentTheme() === "dark" ? "light" : "dark"); return currentTheme(); };
