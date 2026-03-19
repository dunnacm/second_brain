---
down:
  - "[[OH vs Receipts]]"
  - "[[State partitions]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition:
Physical units currently available at a node (DC/warehouse/store).
## Bathtub: 
The **water level** in the tub.
## Math:
### Nonnegativity:
$I(t)\ge 0$.
### Time
#### Continuous‑time conservation:
$$\frac{dI(t)}{dt}=R(t)-S(t)-L(t).$$
#### Discrete‑time (bucketed planning, e.g., weekly):
$$I_{k+1}=I_k+R_{k+1}-S_{k+1}-L_{k+1}.$$
