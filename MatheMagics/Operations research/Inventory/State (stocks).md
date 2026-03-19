---
down:
  - "[[On-hand (OH)]]"
  - "[[On order - Pipeline]]"
  - "[[Work in progress (WIP)]]"
  - "[[Backorders - Backlog]]"
  - "[[Multi-echelon network state]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Introduction:
### Concept definition

**State (Stocks)** describes **what inventory exists at a point in time**.

It answers questions like:
- *Where is inventory right now?*
- *How much is physically present?*
- *How much is usable vs not yet usable?*

Stocks are **levels**, not actions.  
They do not move by themselves — they only change when flows act on them.

### How it differs from the rest

- Stocks are **static snapshots**.
- They are not decisions (controls).
- They are not rates or movements (flows).
- They are not measurements of performance (metrics).

If you can point to a moment on a calendar and say “this is how much exists,” you are in the **State** layer.

### Typical mistakes to watch for

- Treating pipeline inventory as usable stock  
- Treating backlog as inventory  
- Mixing “available” and “on-hand” without defining constraints

### The right questions to ask here

- What inventory exists *right now*, and where?
- Which stock is immediately usable?
- Which stock is delayed, constrained, or conditional?
## Diagrams
### On-hand + Pipeline + WIP (full internal state)
![[Pasted image 20260203134715.png]]

---
### On-hand inventory & On-order / Pipeline inventory
![[Pasted image 20260203134724.png]]
![[onHand_onOrder.png]]

---
### On-hand + Work in Progress (WIP)
![[Pasted image 20260203134729.png]]
![[Pasted image 20260203130312.png]]
![[Pasted image 20260203133315.png]]

---
### On-hand + Backorders / Backlog
![[Pasted image 20260203134735.png]]
![[Pasted image 20260203133315.png]]

---
### Multi-echelon network state (OH only)
![[Pasted image 20260203134740.png]]
