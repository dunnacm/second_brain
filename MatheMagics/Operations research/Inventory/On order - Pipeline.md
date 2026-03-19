---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition:
Units ordered but not yet received (in production / in transit / “on the water”).
## Bathtub:
Water **in the pipe**, not yet usable in the tub.
## Math:
### Pipeline conservation:    
$$\frac{dP(t)}{dt}=q(t)-R(t).$$
### Discrete lead‑time queue:
represent in‑transit orders as a FIFO vector  
  
$(p^1_k,\dots,p^L_k)$ where $p^i_k$ arrives in $i$ buckets. Then:
receipts next bucket: $R_{k+1}=p^1_k$
shift: $p^{i}_{k+1}=p^{i+1}_k$ for $i=1,\dots,L-1$
append new order: $p^{L}_{k+1}=q_k$
total pipeline: $P_k=\sum_{i=1}^{L} p^i_k$