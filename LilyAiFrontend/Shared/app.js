import { ROUTES, DEFAULT_ROUTE, findRoute } from "/Shared/routes.js";
import { createShell } from "/Shared/components/Shell.js";
import { clear, errorBox } from "/Shared/ui.js";

const shell = createShell({ routes: ROUTES });
document.getElementById("root").append(shell.el);

let cleanup = null;
let navToken = 0;

async function navigate() {
  const id = (location.hash.match(/^#\/([\w-]+)/) || [])[1];
  const route = findRoute(id) || findRoute(DEFAULT_ROUTE);
  const token = ++navToken;
  cleanup?.(); cleanup = null;
  shell.setCurrent(route);
  shell.close();
  clear(shell.main);
  shell.main.classList.remove("fill", "sim");
  try {
    const mod = await route.load();
    if (token !== navToken) return; // user navigated again while loading
    cleanup = mod.mount(shell.main, { main: shell.main }) || null;
  } catch (e) {
    shell.main.append(errorBox(e));
  }
  scrollTo(0, 0);
}

addEventListener("hashchange", navigate);
navigate();
