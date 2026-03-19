---
down:
  - "[[ForecastError vs SS]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Buffer to protect against demand/lead‑time variability during replenishment delay.

## Bathtub

“Do not drain below this buffer line.”

## Math

### Canonical quantile buffer

$$SS = z\,\sigma_{DLT},$$

where $\sigma_{DLT}$ is the standard deviation of demand during lead time and $z$ is a service‑level factor.