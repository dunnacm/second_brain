---
down:
  - "[[Demand vs LostSales vs Backorders]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition: 
Demand customers still want but hasn’t shipped yet (owed demand).
## Bathtub: 
A “negative tank” that **fills when demand exceeds shipments**.
## Math:
### Discrete update (backorder world):
$$B_{k+1}=\max(B_k + D_k - S_k,\ 0).$$
### Continuous analogue (conceptual):
$$\dot B(t)=d(t)-S(t),\quad B(t)\ge 0.$$
