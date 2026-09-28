## 1) Fast access menus & system navigation

- **Power user menu (hidden Start menu menu)**
  - Right-click **Start** (or press **Win + X**) for quick links (Settings, Device Manager, Terminal, etc.).
  - In that menu, you can often press the **highlighted letter** to launch the item.

- **Task Manager (fast launch)**
  - **Ctrl + Shift + Esc**

- **Task View / Virtual desktops**
  - In **Task View**, right-click a desktop to:
    - **Rename** it
    - Set a **different wallpaper** per desktop

- **Advanced startup options**
  - Hold **Shift** while clicking **Restart** to open recovery/boot/reset/repair options.

- **“Slide to shut down”**
  - Create a desktop shortcut targeting:
    - `C:\Windows\System32\SlideToShutDown.exe`

---

## 2) Drag & drop “modifier keys” (file operations)

When dragging a file:

- **Ctrl** → **Copy** (duplicate)
- **Shift** → **Move**
- **Alt** → **Create shortcut**
- **Right-drag** (drag with right mouse button) → drop to get a **menu** (copy/move/shortcut, etc.)

---

## 3) Trackpad + window focus tricks

- **Trackpad gestures**
  - Settings → **Bluetooth & devices** → **Touchpad** → **Advanced gestures**

- **Shake to minimize others**
  - Shake a window’s title bar to minimize all other windows (toggle in Settings).

- **Alt + Tab behavior**
  - Settings → **System** → **Multitasking** (configure Alt-Tab showing tabs/windows).

---

## 4) Multitasking shortcuts (high-leverage set)

- **Alt + Esc**: cycle through apps (different feel than Alt-Tab)
- **Win + (number)**: open/switch to the app pinned in that taskbar position
- **Win + T**: focus/cycle taskbar items
- **Win + M**: minimize all
- **Win + Shift + M**: restore minimized windows
- **Win + Arrow keys**: snap/move window around; can also minimize
- **Alt + F4**: close active app/window
- **Win + Home**: minimize everything except the active window

---

## 5) Home/End keys (and selection)

- **Home**: top of document/page (depends on app)
- **End**: bottom of document/page (depends on app)
- **Ctrl + Home**: top of a text field/document
- **Ctrl + End**: bottom of a text field/document
- **Shift + Home/End**: select to start/end of line (or doc in some apps)
- Laptop mapping: **Fn + ←** = Home, **Fn + →** = End (common layout)

---

## 6) Win + R (Run) shortcuts worth remembering

- `.` → your user folder
- `..` → parent directory
- `control` → Control Panel
- `control printers` → printers / devices area
- `perfmon` → Performance Monitor
- `cleanmgr` → Disk Cleanup
- `mrt` → Microsoft Malicious Software Removal Tool
- `shell:AppsFolder` → “All apps” folder (Launchpad-like list)

---

## 7) Start menu + taskbar customization (Windows 11)

- Taskbar alignment, Start layout (pins vs recommendations), quick File Explorer folders, etc.
- **Quick Settings panel** (taskbar) can be customized by rearranging tiles/icons.

- **Show seconds in clock**
  - Settings → **Time & language** → **Date & time** → **Show seconds** (system tray clock)

- **Extra time zones**
  - Right-click date/time → adjust settings → add up to **two extra** time zones (visible on hover/calendar panel).

---

## 8) Taskbar “middle click” actions

- Middle-click a taskbar app icon → open a **new instance**
- Middle-click a browser tab → **close tab**
- (Video notes also mention “Ctrl + N” as a new-window shortcut in many apps.)

---

## 9) File Explorer efficiency kit

**Creation / navigation**
- **Ctrl + Shift + N**: new folder
- **Ctrl + L**: address bar focus
- **Alt + ↑**: up one level
- **Alt + Enter**: properties
- **F11**: full screen

**Views**
- **Ctrl + Shift + 1 … 8**: switch view layouts quickly (varies by system/version)

**Tabs**
- **Ctrl + T**: new tab
- **Ctrl + W**: close tab
- Middle-click: open in new tab (behavior can vary by context/app)

**Organize**
- Right-click inside folder → **Group by**
- In Details view, add columns by using the column header context options.

**Selection**
- Explorer “…” menu includes **Invert selection** (handy for bulk actions)

---

## 10) Windows Search + indexing (find faster)

- Windows Search is strong for **settings**, calculations, conversions.
- Use search categories/filters where available.
- Refiners like `file:` or `folder:` can narrow results (as shown in the video).

**Exclude folders from indexing**
- Settings → **Privacy & security** → **Searching Windows** → exclusions

**Indexing Options**
- Search “**Indexing Options**” → select locations (useful with multiple drives).

---

## 11) “Housekeeping” editing + desktop micro-tricks

- **Ctrl + Scroll** (in Explorer): adjust icon size
- **Shift + Right-click**: show “classic” context menu (Win 11)
- Desktop right-click options can hide desktop icons
- **Ctrl + Backspace**: delete previous word
- **Ctrl + Delete**: delete next word
- **Shift + Arrow**: select by character/line
- **Ctrl + Shift + Arrow**: select by word
- Click bottom-right corner of taskbar → show desktop

---

## 12) Universal shortcuts & window tiling

- **Alt + PrtScn**: screenshot active window (behavior depends on OS/settings)
- **Win + V**: clipboard history
- **Shift + Scroll**: horizontal scroll (in apps that support it)
- **Virtual desktops**
  - **Win + Ctrl + D**: new desktop
  - **Win + Ctrl + F4**: close current desktop
  - **Win + Ctrl + ←/→**: switch desktops

**Snap layouts**
- Hover maximize button or press **Win + Z** to choose a layout (then select with number).

---

## 13) Notepad, Calculator, Snipping Tool (built-ins that are better than expected)

### Notepad
- Put `.LOG` (caps) at top: inserts date/time on open
- **F5**: insert date/time
- Settings can adjust theme, font/text size, wrap, autocorrect, resume behavior

### Calculator
- “Keep on top” pin
- History panel
- Keyboard shortcuts (video mentions Alt + 1–5 for some modes)
- Currency conversions pull local rates (accuracy depends on source/update timing)

### Snipping Tool
- **Win + Shift + S**: snip UI (and screen recording depending on version)
- Markup, color picker, text extraction
- App settings: border, clipboard behavior, save location, delays, etc.

---

## 14) Support & diagnostics tools (quietly useful)

- **Quick Assist**: built-in remote help tool (no third-party needed)
- **Clock app**: built-in Pomodoro timer
- **Reliability Monitor**: search it to view app/system failure history over time

**Battery / energy reports**
- `powercfg /batteryreport` (Command Prompt) → generates battery health report
- `powercfg /energy` → energy efficiency report

**Laptop lid & power behavior**
- Search “lid” → control what happens on lid close (battery vs plugged-in)

---

## 15) Task Manager power-user bits

- Right-click a process/app → **Open file location**
- Details tab → set **Priority**
- Settings allow startup page selection, refresh rate, always-on-top behavior

---

## 16) Command Prompt / Terminal quick wins

- In File Explorer address bar: type `cmd` → opens terminal in that folder
- `tree` → folder tree diagram
- `color` command controls console colors (`color /?` for options)
- QR creation in the video depends on having a QR utility available (not default on all systems)

**Run as Administrator shortcut**
- Hold **Shift + Ctrl** while launching an app (video also mentions **Win** key; behavior can vary—test on your system).

---

## 17) Settings deep cuts (small changes, daily comfort)

- Disable “Finish setting up your device” splash screen:
  - Settings → **Notifications** → **Additional settings**
- App-by-app GPU choice:
  - Settings → **Display** → **Graphics** (graphics performance preference)
- Storage:
  - Storage Sense, recommendations, advanced storage settings, default save locations
- Hide Recycle Bin icon:
  - Settings → **Personalization** → **Themes** → **Desktop icon settings**
- Recycle Bin max size:
  - Recycle Bin → Properties → set limit

- Default apps:
  - set by file type/protocol (not just browser defaults)

---

## 18) Sharing features (built-in)

- **Nearby sharing**
  - Enable in Quick Settings
  - Right-click file → Share → Nearby sharing

- **Wi-Fi sharing**
  - Wi-Fi network settings → show password + QR (where supported)

---

## 19) Third-party utilities mentioned (optional upgrades)

**Small utilities**
- Battery Percentage Icon (adds % to taskbar)
- Twinkle Tray (external display brightness control)
- EarTrumpet (audio device/volume control)
- SoundSwitch (hotkey audio device switch)
- Auto Dark Mode
- f.lux
- Espanso (text expander)

**Bigger apps**
- Everything Search (fast file search)
- KeePass (local password manager)
- TeraCopy (advanced file copy)
- LocalSend (AirDrop-like cross-platform sharing)
- ImageGlass (photo viewer)
- DaVinci Resolve (video editor)
- Obsidian (notes)
- Hardware Info tools (system diagnostics)

---

# Suggested refinements (to make these notes more usable)

## A) “Use daily” shortlist (quick muscle-memory set)
- **Ctrl + Shift + Esc** (Task Manager)
- **Win + X** (power user menu)
- **Win + V** (clipboard history)
- **Win + Shift + S** (Snipping Tool)
- **Win + Z** (snap layouts)
- **Win + Ctrl + D / ←/→ / F4** (virtual desktops)
- **Ctrl + L**, **Alt + ↑**, **Ctrl + Shift + N** (File Explorer core)

## B) “Troubleshoot” shortlist
- Reliability Monitor
- `powercfg /batteryreport`
- Indexing Options / Searching Windows exclusions

## C) “You’ll forget these unless they’re written down”
- Drag modifiers: Ctrl/Shift/Alt + right-drag menu
- `shell:AppsFolder`
- Shift+Restart advanced boot menu
- SlideToShutDown shortcut