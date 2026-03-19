---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Canonical notation 

I’ll use these as the baseline (you can translate to weekly buckets later). 
This is the minimum “symbol hygiene” needed to keep definitions consistent.

### State (stocks) 
- $I(t)$ / $I_k$: on‑hand inventory (units physically in the DC/node)
- $P(t)$ / $P_k$ or $(p^1_k,\dots,p^L_k)$: pipeline/on‑order inventory (ordered but not received)
- $B(t)$ / $B_k$: backlog/backorders (unserved demand that is owed, if allowed)

### Flows
- $R(t)$ / $R_k$: receipts into on‑hand
- $d(t)$ / $D_k$: demand requested
- $S(t)$ / $S_k$: shipments/sales actually fulfilled
- $L(t)$ / $L_k$: leakage (shrink, damage, obsolescence)

### Control inputs
- $q(t)$ / $q_k$: orders placed (your control input)

### Delays / parameters
- $\tau$: lead time in continuous time
- $L$: lead time measured in discrete planning buckets (e.g., weeks)
