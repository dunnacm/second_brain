---
down:
  - "[[Orders placed (q)]]"
  - "[[Reorder Point (ROP)]]"
  - "[[Order Quantity (Q)]]"
  - "[[(s, Q) policy]]"
  - "[[Order-up-to-level (S)]]"
  - "[[Safety stock (SS)]]"
  - "[[EOQ]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Introduction:
### Concept definition

**Control Inputs** describe **what decisions we actively make**.

They answer questions like:
- *How much do we order?*
- *When do we order?*
- *Who gets inventory when it’s scarce?*
- *Do unmet orders backlog or disappear?*

Controls are **levers**, not outcomes.

### How it differs from the rest

- Controls are **choices**, not measurements.
- They regulate flow but are not flows themselves.
- They operate *through* constraints.

Two systems with the same stocks, flows, and constraints can behave very differently depending on control policies.

### Typical mistakes to watch for

- Treating forecasts as facts rather than inputs
- Forgetting that service rules change system dynamics
- Assuming controls are neutral or automatic

### The right questions to ask here

- What knobs can we actually turn?
- Which decisions affect timing vs quantity vs priority?
- Are we modeling policy, or just replaying history?
## Diagrams
### Replenishment decision layer (qty, timing, frequency, reorder policy)
![[Pasted image 20260203143653.png]]

---
### Service decision layer (allocation priority + backlog vs lost sales)
![[Pasted image 20260203143858.png]]

---
### Plan adjustment layer (frozen horizon + ETA updates)
![[Pasted image 20260203144120.png]]
