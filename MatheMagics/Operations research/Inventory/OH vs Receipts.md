---
down:
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
### Why OH appears in multiple core concepts:
- **Derived:** $IP = OH + \text{OnOrder} - \text{Backlog}$; $ATS/ATP$ are functions of $OH$ after subtracting reservations/commitments.
- **Control:** reorder rules act on $IP$ (and therefore on $OH$).
- **Metrics:** $DOS \approx OH/\bar d$ and $WOS \approx OH/\bar D_{\text{weekly}}$.