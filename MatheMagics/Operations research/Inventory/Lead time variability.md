---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Lead time is not constant.

## Bathtub

Pipe travel time is random; arrivals are “smeared.”

## Math

#### Distributed delay / convolution

If lead time has density $g(\tau)$, then

$$R(t)=\int_0^{\infty} q(t-\tau)\,g(\tau)\,d\tau.$$