---
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
down:
  - "[[Receipts]]"
  - "[[Sales - Shipments]]"
  - "[[Returns]]"
  - "[[Leakage (Shrink - Damage - Obsolescence)]]"
---
## Introduction:
### Concept definition

**Flows** describe **how inventory changes over time**.

They answer questions like:
- *What is entering inventory?*
- *What is leaving inventory?*
- *At what rate does inventory change?*

Flows are **actions over time**, not quantities at rest.

### How it differs from the rest

- Flows are **rates or quantities per time bucket**.
- They are not inventory levels.
- They do not describe restrictions or policies.
- They are the *only* way stocks change.

If you remove all flows, inventory stays frozen forever.

### Typical mistakes to watch for

- Treating demand as a flow (it is a request, not movement)
- Double-counting forecast and orders as separate outflows
- Forgetting loss flows (shrink, damage, obsolescence)

### The right questions to ask here

- What actually moves inventory?
- Which flows are planned vs uncontrolled?
- Are we modeling **requested demand** or **fulfilled shipments**?

## Diagrams
### Demand + Sales / Shipments
![[Pasted image 20260203135538.png]]

---
### Demand + Sales + Backorders
![[Pasted image 20260203135643.png]]

---
### Receipts and Sales / Shipments
![[Pasted image 20260203145534.png]]

---
### Receipts + Returns
![[Pasted image 20260203140658.png]]

---
### Losses (Shrink, Damage, Obsolescence, Leakage)
![[Pasted image 20260203141554.png]]

---
### Net Outflow (Shipments + Losses)

![[Pasted image 20260203140945.png]]