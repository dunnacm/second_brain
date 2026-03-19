---
down:
tags:
---
## Business definition: 
Real supply chains are multiple coupled stocks (supplier/WIP → transit → DC → customer/backlog).
## Bathtub: 
A **network of tubs** connected by pipes; each node has its own level.
## Math: 
Stack states into a vector $\mathbf{x}(t)$ (e.g., upstream supply, in‑transit, on‑hand, backlog) and write:
  $$\dot{\mathbf{x}}(t)=\mathbf{f}(\mathbf{x}(t),\mathbf{u}(t),t),$$
  with coupling flows, saturations (can’t ship what you don’t have), and delays.
