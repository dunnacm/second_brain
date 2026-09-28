---
down:
tags:
---
```dataviewjs
const root = dv.current();
const seen = new Set();
const lines = [];

function asPage(ref) {
  if (!ref) return null;

  // Dataview "Link" objects typically have .path
  if (typeof ref === "object" && ref.path) return dv.page(ref.path);

  // Strings like "Folder/Note" or "Note"
  if (typeof ref === "string") return dv.page(ref);

  return null;
}

function getChildren(page) {
  const down = (page && page.down) ? page.down : null;
  if (!down) return [];

  const kids = Array.isArray(down) ? down : [down];
  return kids.map(asPage).filter(Boolean);
}

function buildTree(page, prefix, isRoot, isLast) {
  if (!page || !page.file) return;

  const path = page.file.path;
  if (seen.has(path)) return;
  seen.add(path);

  const marker = isRoot ? "" : (isLast ? "└── " : "├── ");
  lines.push(prefix + marker + page.file.name);

  const children = getChildren(page);
  if (!children.length) return;

  const nextPrefix = isRoot ? "" : (prefix + (isLast ? "    " : "│   "));

  for (let i = 0; i < children.length; i++) {
    buildTree(children[i], nextPrefix, false, i === children.length - 1);
  }
}

buildTree(root, "", true, true);

// Render as monospace, preserves indentation, no markdown backticks needed
dv.el("pre", lines.join("\n"));

```