---
down:
  - "[[Operational computed quantities (decision-state transforms)]]"
  - "[[Performance metrics (KPIs - Outcomes)]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Introduction:
### Concept definition

**Metrics** describe **how we evaluate the system**.

They answer questions like:
- *Is performance good or bad?*
- *Are we efficient?*
- *Are customers satisfied?*
- *Is inventory too high or too low?*

Metrics do not change the system — they **observe it**.

### How it differs from the rest

- Metrics are **derived quantities**.
- They depend on stocks, flows, constraints, and controls.
- They do not cause behavior (unless tied back into control rules).

Metrics answer *questions*; they do not *solve problems* by themselves.

### Typical mistakes to watch for

- Optimizing one metric at the expense of system behavior
- Comparing metrics without aligning definitions
- Treating metrics as states or controls

### The right questions to ask here

- What question is this metric answering?
- What tradeoff does this metric hide?
- Which layer does this metric depend on?