/** Single source of truth for navigation. Add a page here and it appears in the drawer and on Home. */
export const ROUTES = [
  { id: "home", label: "Home", icon: "home", desc: "Overview", load: () => import("/Home/home.js") },
  { id: "chat", label: "Chat", icon: "chat", group: "Workspace", desc: "Talk to Lily like a Discord user", load: () => import("/Chat/chat.js") },
  { id: "dashboard", label: "Dashboard", icon: "dashboard", group: "Workspace", desc: "Stats, tools, knowledge and evaluation", load: () => import("/Dashboard/dashboard.js") },
  { id: "relay", label: "Relay", icon: "relay", group: "Admin", desc: "Live feed of the Discord bot", load: () => import("/Admin/Relay/relay.js") },
  { id: "simulator", label: "DM Simulator", icon: "simulator", group: "Admin", desc: "Test users with a full trace", load: () => import("/Admin/DMSimulator/simulator.js") },
  { id: "settings", label: "Settings", icon: "settings", group: "System", desc: "Connection, models and auto-scan", load: () => import("/Settings/settings.js") },
];

export const DEFAULT_ROUTE = "home";
export const findRoute = (id) => ROUTES.find((r) => r.id === id);
