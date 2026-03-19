---
down:
  - "[[Demand modeling, information]]"
  - "[[Demand vs Sales]]"
  - "[[Demand vs LostSales vs Backorders]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition: 
Customer request for units (the “true” demand signal, even if not all can be fulfilled).
## Bathtub:
The drain “wants” to pull this much water.
## Math:
Exogenous forcing $d(t)$ (continuous) or $D_k$ (bucketed). Often treated as stochastic:
  $$D_k = \mu_k + \varepsilon_k,$$
 where $\mu_k$ is forecastable structure (trend/seasonality/promo) and $\varepsilon_k$ is noise.
