---
down:
  - "[[Lost sales]]"
  - "[[Single-echelon vs Multi-echelon]]"
  - "[[Planning horizon]]"
  - "[[Review policy]]"
  - "[[Fulfillment regime]]"
  - "[[Capacity constraints]]"
  - "[[Lead time model]]"
  - "[[Constraints and Delays]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Introduction:
### What this concept is

This layer answers the most important question:

> **Can the system actually work over time, given everything above?**

It combines:
- stock–flow dynamics,
- constraints,
- control choices,
- and a time horizon.

Feasibility is not a metric; it is a **logical consequence**.

### How it differs from the rest

- This is the **integrative layer**.
- It is where models succeed or fail.
- It is not visible in a single snapshot.

You cannot determine feasibility by looking at totals alone — timing is decisive.

### Typical mistakes to watch for

- Checking totals instead of trajectories
- Ignoring stub months or timing mismatches
- Mixing incompatible definitions (e.g., Available vs On-hand)

### The right questions to ask here

- Do we ever run out of inventory?
- *When* is the tightest point?
- What assumptions must hold for feasibility to remain true?

## Structure:
```dataviewjs  
const root = dv.current();  
const seen = new Set();  
const lines = [];  
  
function asPage(ref) {  
  if (!ref) return null;  
  
  // Dataview "Link" objects typically have .path  
  if (typeof ref === "object" && ref.path) return [dv.page](http://dv.page/)(ref.path);  
  
  // Strings like "Folder/Note" or "Note"  
  if (typeof ref === "string") return [dv.page](http://dv.page/)(ref);  
  
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
  lines.push(prefix + marker + [page.file.name](http://page.file.name/));  
  
  const children = getChildren(page);  
  if (!children.length) return;  
  
  const nextPrefix = isRoot ? "" : (prefix + (isLast ? "    " : "│   "));  
  
  for (let i = 0; i < children.length; i++) {  
    buildTree(children[i], nextPrefix, false, i === children.length - 1);  
  }  
}  
  
buildTree(root, "", true, true);  
  
// Render as monospace, preserves indentation, no markdown backticks needed  
dv.el("pre", lines.join("\n"));  
  
```



