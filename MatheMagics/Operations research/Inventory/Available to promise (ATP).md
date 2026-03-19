---
down:
  - "[[Allocated vs ATS vs ATP]]"
  - "[[Reserved vs ATS vs ATP]]"
  - "[[Committed vs ATS vs ATP]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Feasible quantity you can promise for a **date**, considering future receipts and commitments.

## Bathtub

“Can I guarantee water will be there on date $T$?”

## Math

### Time‑phased feasibility idea

For promise date bucket $T$, require that projected on‑hand never goes negative under commitments. A minimal discrete check is:

$$I_0 + \sum_{k=1}^{t} R_k - \sum_{k=1}^{t} C_k \ge 0\quad\text{for all }t\le T,$$

where $C_k$ is the committed/firm demand you must serve.