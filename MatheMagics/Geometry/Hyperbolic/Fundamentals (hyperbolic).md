---
down:
  - "[[Derivation - Motivating example (hyperbolic) 1]]"
  - "[[Properties (primary, hyperbolic)]]"
tags:
  - mathemagics/geometry/hyperbolic
---
```dataviewjs
// Auto-MOC from frontmatter `down:`
// Output: plain text nested list (no links), styled via CSS class .moc-tree
const root = dv.current();
const seen = new Set();
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
function addNode(parentUl, page) {
  const key = page.file?.path ?? page.file?.name ?? String(page);
  if (seen.has(key)) return;
  seen.add(key);
  const li = document.createElement("li");
  li.textContent = page.file.name; // plain text (no link)
  parentUl.appendChild(li);
  const kids = childrenOf(page);
  if (kids.length) {
    const ul = document.createElement("ul");
    li.appendChild(ul);
    for (const kid of kids) addNode(ul, kid);
  }
}
// Render
dv.container.innerHTML = "";
const wrap = document.createElement("div");
wrap.className = "moc-tree";
dv.container.appendChild(wrap);
const topUl = document.createElement("ul");
wrap.appendChild(topUl);

// Instead of adding the root node, add only its children
const rootChildren = childrenOf(root);
for (const child of rootChildren) {
  addNode(topUl, child);
}

```

