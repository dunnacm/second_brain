---
down:
  - "[[Demand vs Sales]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition: 
Units actually shipped/sold (fulfilled demand).
## Bathtub: 
Actual water leaving the tub (limited by water level).
## Math (saturation by availability):
### Lost‑sales world (no backlog):
$$S_k = \min(D_k,\ I_k+R_k).$$
### Backorder world (with backlog):
$$S_k = \min(D_k+B_k,\ I_k+R_k).$$
  (Same idea in continuous time: shipments are a demand‑like outflow but saturated by availability.)
