---
down:
  - "[[Notation (inventory planning)]]"
  - "[[Core concepts (inventory)]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
Let's compare inventory concepts to a tank being filled with water. 

## Why it works
Inventory planning is mostly **conservation of mass** plus **time delays**:
- The inventory level moves because units flow in (receipts) and flow out (shipments).
- Orders you place today don’t arrive until later: lead time is a delay operator.

## Where it breaks 
- Real systems have **integer counts**, **batching**, and **constraints** (MOQ, case pack, capacity).
- Demand may be **censored by stockouts** (lost sales), so you don’t observe true demand.
- “Available”, “ATS”, “Unallocated”, “Committed” are often **system‑specific derived fields** rather than universal truths.
- Multi‑node supply chains are **networks of bathtubs**, not one.

## Appendix — A practical “definition discipline” checklist
When a system shows a field like **Available** / **ATS** / **Unallocated**:
1) Ask what it subtracts: allocations? holds? safety stock? future demand?
2) Ask time scope: point‑in‑time vs time‑phased.
3) Ask location scope: one DC vs all nodes.
4) Confirm whether backorders exist (or it’s lost sales).

That checklist prevents most “inventory numbers don’t match” confusion.