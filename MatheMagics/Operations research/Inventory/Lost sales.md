---
down:
  - "[[Demand vs LostSales vs Backorders]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Demand that disappears if you can’t fulfill (customer leaves); no backlog accumulates.

## Bathtub

Drain pulls, but if the tub is empty, the remainder is “spilled” (gone).

## Math

#### Unmet requested outflow

$$\text{Lost}_k = D_k - S_k\quad (\ge 0\text{ in lost‑sales world}).$$