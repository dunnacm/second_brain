---
down:
  - "[[IP vs (s,Q)]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

When inventory position is at/below $s$, order a fixed amount $Q$.

## Bathtub

If water drops below a sensor line, dump one bucket of fixed size.

## Math

$$q_k = Q\cdot \mathbf{1}\{IP_k\le s\}.$$