---
down:
  - "[[Lead time (LT)]]"
  - "[[MOQ - Case pack]]"
  - "[[Service constraints]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Introduction:
### Concept definition

**Constraints** describe **what is not allowed**, even if inventory and flows exist.

They answer questions like:
- *Why can’t we use inventory that is physically present?*
- *Why does supply arrive late or unpredictably?*
- *Why doesn’t demand always turn into sales?*

Constraints **shape behavior** without being inventory or movement themselves.

### How it differs from the rest

- Constraints are **rules, limits, or conditions**.
- They do not add or remove inventory.
- They restrict *when*, *how*, or *whether* flows can occur.

If stocks are “what exists” and flows are “what moves,”  
constraints are **what prevents the obvious thing from happening**.

### Typical mistakes to watch for

- Treating constraints as flows
- Mixing temporal constraints (lead time) with availability constraints (allocation)
- Ignoring constraints when interpreting metrics

### The right questions to ask here

- What inventory is unusable, and why?
- What delays or uncertainty exist?
- What rules override otherwise valid flows?

## Diagrams
### Allocated, Reserved, Committed, Unallocated
![[Pasted image 20260203142347.png]]

---
### Lead Time + Lead Time Variability
![[Pasted image 20260203142515.png]]

---
### Lost Sales
![[Pasted image 20260203142656.png]]

---
### MOQ / Case Pack
![[Pasted image 20260203142842.png]]