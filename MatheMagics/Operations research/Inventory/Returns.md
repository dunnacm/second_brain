---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition:
Units coming back (customer returns, RTV).
## Bathtub: 
A small reverse faucet adding water back.
## Math: 
Treat as an additional inflow:
  $$R_{\text{return}}(t)\ge 0,\qquad R_{\text{total}}(t)=R(t)+R_{\text{return}}(t).$$
  (Equivalently, model “net demand” as $d_{\text{net}}(t)=d(t)-R_{\text{return}}(t)$.)
