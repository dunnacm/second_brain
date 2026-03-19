---
down:
  - "[[Allocated vs ATS vs ATP]]"
  - "[[Reserved vs ATS vs ATP]]"
  - "[[Committed vs ATS vs ATP]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

What a selling channel exposes as sellable **right now** under its rules.

## Bathtub

“Drinkable” water after subtracting protected/held water.

## Math

### Typical rule‑based form (system‑specific)

$$ATS = \max(I - SS - \text{holds},\ 0).$$