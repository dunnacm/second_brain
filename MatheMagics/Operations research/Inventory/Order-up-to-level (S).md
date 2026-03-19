---
down:
  - "[[IP vs S]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Periodic review: order enough to raise inventory position to $S$.

## Bathtub

At each review, top up to a mark.

## Math

$$q_k=\max(S-IP_k,\ 0).$$