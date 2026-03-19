---
down:
  - "[[Lead time variability]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Time from placing an order to receiving it.

## Bathtub

Travel time in the pipe.

## Math

#### Fixed lead time, delay differential equation view

$$R(t)=q(t-\tau).$$

In bucketed planning with integer lead time $L$: orders placed in bucket $k$ arrive in bucket $k+L$.