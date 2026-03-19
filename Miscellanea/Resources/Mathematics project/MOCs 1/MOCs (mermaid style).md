---
down:
tags:
---
```dataviewjs
// Auto-MOC Mermaid flowchart from frontmatter `down:`
// Root is hidden; diagram shows children/grandchildren/etc.

const root = dv.current();

const MAX_DEPTH = 20;
const MAX_NODES = 600;

const seen = new Set();       // prevents infinite recursion
const ids  = new Map();       // stable Mermaid ids per file
let nodeCount = 0;
let nextId = 1;

function asPage(x) {
  if (!x) return null;
  if (typeof x === "object" && x.path) return dv.page(x.path); // dv Link
  if (typeof x === "string") return dv.page(x);
  return dv.page(String(x));
}

function childrenOf(page) {
  const d = page?.down;
  if (!d) return [];
  const arr = Array.isArray(d) ? d : [d];
  return arr.map(asPage).filter(Boolean);
}

function keyOf(page) {
  return page?.file?.path ?? page?.file?.name ?? String(page);
}

function idOf(page) {
  const key = keyOf(page);
  if (!ids.has(key)) ids.set(key, "N" + (nextId++));
  return ids.get(key);
}

function labelOf(page) {
  // Mermaid-safe string; JSON.stringify handles quotes/backslashes safely.
  const s = page?.file?.name ?? String(page);
  return String(s).replace(/\r?\n/g, " ");
}

function walk(parentId, page, depth, nodes, edges) {
  if (!page) return;
  if (depth > MAX_DEPTH) return;
  if (nodeCount >= MAX_NODES) return;

  const k = keyOf(page);
  const cid = idOf(page);

  // Always register node + edge (even if already seen), but recurse only once.
  nodes.set(cid, labelOf(page));
  if (parentId) edges.push(`${parentId} --> ${cid}`);

  if (seen.has(k)) return;
  seen.add(k);
  nodeCount++;

  for (const kid of childrenOf(page)) {
    walk(cid, kid, depth + 1, nodes, edges);
  }
}

// Build Mermaid source
const nodes = new Map();
const edges = [];

const topKids = childrenOf(root);

// Add ROOT -> topKids edges first (so we can hide exactly these link indices)
for (const kid of topKids) {
  walk("ROOT", kid, 1, nodes, edges);
}

const lines = [];
lines.push("graph LR");

// Use an explicit string label for ROOT (blank-ish) to avoid parse issues.
lines.push(`ROOT[" "]`);

// Node declarations
for (const [id, label] of nodes.entries()) {
  lines.push(`${id}[${JSON.stringify(label)}]`);
}

// Edges
lines.push(...edges);

// Hide ROOT node
lines.push("style ROOT fill:none,stroke:none,color:none;");

// Hide ONLY the ROOT->child links (the first topKids.length links)
if (topKids.length > 0) {
  const idx = Array.from({ length: topKids.length }, (_, i) => i).join(",");
  lines.push(`linkStyle ${idx} opacity:0,stroke-width:0px;`);
}

const mermaidCode = lines.join("\n");

// Render via Obsidian MarkdownRenderer (more stable than window.mermaid in many setups)
dv.container.innerHTML = "";
const host = dv.container.createEl("div", { cls: "moc-mermaid" });

const md = "```mermaid\n" + mermaidCode + "\n```";

(async () => {
  try {
    host.innerHTML = "";
    await obsidian.MarkdownRenderer.render(
      app,
      md,
      host,
      root.file?.path ?? "",
      dv.container
    );
  } catch (e) {
    host.createEl("div", { text: "Mermaid render failed; showing Mermaid source instead:" });
    host.createEl("pre", { text: mermaidCode });
  }
})();

```
