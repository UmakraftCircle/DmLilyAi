# LilyAiFrontend

Buildless web console for LilyAi: plain ES modules, no bundler, no dependencies. Mobile-first, works on desktop.
Dark by default with a gradient look; light theme via the header toggle.

This folder is only the web client. The bot's server (`LilyAiMain`) serves it, so the bot's URL is the website.
There is no build, no `src` folder and no separate deploy: edit a file, refresh, and after a push Render redeploys.

```bash
python -m LilyAiMain.main        # then open http://localhost:8000 and enter ADMIN_TOKEN in Settings
```

## Responsive behaviour

- **Phones (< 900px):** top bar with a gradient menu button; the menu is a slide-in drawer of tiles, with a "System: Online" footer.
- **Desktop (>= 900px):** the same drawer becomes a permanent sidebar; Home shows a tile grid; Chat/Simulator use the full height, the simulator adds a side panel at >= 1100px.

## Structure (one concern per file)

```
Public/index.html          shell + stylesheet links
Assets/styles/             tokens.css (colours, gradients, themes) . base.css . layout.css . components.css . pages.css
Shared/
  app.js                   router + boot        routes.js   the ONLY place pages are registered
  api.js  ui.js  icons.js  theme.js
  components/              Shell . Header . Drawer . Tile . StatusBar . Card . Stat . Table . Toast
Home/  Chat/  Dashboard/  Settings/  Admin/Relay/  Admin/DMSimulator/     one folder per page
  Dashboard/cards/  Settings/cards/                                       one file per card
```

## Adding a page

1. Create `MyPage/myPage.js` exporting `mount(root)` (optionally return a cleanup function).
2. Add one entry to `Shared/routes.js`. It appears in the drawer/sidebar and on Home automatically.

## Changing the look

Edit `Assets/styles/tokens.css` only: brand colours, gradients, radii and the light/dark palettes live there.
`Tile` supports `locked: true` (dimmed, lock badge) for role-gated features later.

Text is always inserted with `textContent`, never `innerHTML`.
