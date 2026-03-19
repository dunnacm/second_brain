---
down:
  - "[[IP vs ROP]]"
  - "[[IP vs (s,Q)]]"
  - "[[IP vs S]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition: 
Planning state: on‑hand + on‑order − backlog. Used because it “sees” inventory that will arrive.
## Bathtub: 
Tub + pipe − owed deficit.
## Math:
### Continuous:
  $$IP(t)=I(t)+P(t)-B(t).$$
### Discrete with pipeline buckets:
$$IP_k = I_k + \sum_{i=1}^{L} p^i_k - B_k.$$
