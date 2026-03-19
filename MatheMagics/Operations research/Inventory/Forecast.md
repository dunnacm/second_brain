---
down:
  - "[[Forecast error]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition

Estimate of future demand (often by time bucket and item/location).

## Bathtub

Predicted drain schedule.

## Math

### Conditional expectation

$$\hat D_{t+h}=\mathbb{E}[D_{t+h}\mid\mathcal{F}_t].$$