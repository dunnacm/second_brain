---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Business definition: 
Units started in production but not finished.
## Bathtub: 
A **tank upstream** of the pipeline (another tub feeding yours).
## Math: 
Model as an upstream stock $W(t)$ with its own inflow/outflow:
  $$\dot W(t)=\text{starts}(t)-\text{finishes}(t).$$
  (Where “finishes” becomes inflow to downstream pipeline or receipts.)
