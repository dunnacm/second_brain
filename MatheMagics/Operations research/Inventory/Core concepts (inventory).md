---
down:
  - "[[State (stocks)]]"
  - "[[Flows]]"
  - "[[Control inputs (decision variables + policies)]]"
  - "[[System Structure & Feasibility (Planning Horizon)]]"
  - "[[Exogenous drivers - Demand process]]"
  - "[[Computed quantities (derived measure + metrics)]]"
tags:
  - mathemagics/operations_research/inventory/ODEmodeling_parallelism
---
## Unified Core Concepts 

Everything below is organized strictly by the categories promised in the intro:
**State → Flow → Derived → Constraint/Partition → Control → Metric**.

Each entry includes:
- **Business definition**
- **Bathtub intuition**
- **Math** (variable(s) + equation(s))

## Orienting principle

Each core concept answers a **different class of question**:

- **State** → *What exists?*
- **Flows** → *What moves?*
- **Constraints** → *What is forbidden or delayed?*
- **Controls** → *What do we choose?*
- **Metrics** → *How do we judge?*
- **Feasibility** → *Does it all work together over time?*

If you ever feel confused, the correct response is not “add detail” —  
it is to ask:

> *Which layer am I actually reasoning in right now?*

That question alone prevents most modeling errors.
