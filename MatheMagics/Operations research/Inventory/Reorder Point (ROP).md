---
down:
  - "[[IP vs ROP]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Threshold; when inventory position falls below it, you place an order.

## Bathtub

Float valve triggers refill when water falls below a mark.

## Math

### Switching rule

$$\text{If }IP\le r\text{ then order.}$$