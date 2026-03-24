---
down:
  - "[[Substitution (PL)]]"
  - "[[Assignment (PL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
A **propositional variable** is a symbol (e.g., $\mathtt{p},\mathtt{q},\mathtt{r},\dots$$\mathtt{P,Q,R,}\dots,\text{ or } \mathtt{P_n,Q_n,R_n,}\dots$) that serves as an **atomic propositional form** in propositional logic.

A propositional variable is **syntactic**: it is a piece of the formal language.

A **proposition** is the meaningful, truth-apt content (a **semantic** object) that a propositional variable may be used to represent informally.

## Valuations
A **valuation** (truth assignment) is a function
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}
$$
that assigns each propositional variable a truth value.

Given a valuation $\upnu$, the truth value of any compound formula is determined from $\upnu$ by the usual truth tables for the connectives.

## Contrast with first-order variables
Do not confuse propositional variables with first-order (individual) variables.

- Propositional variables ($\mathtt{p},\mathtt{q},\dots$) stand for whole statements and receive truth values via $\upnu$.
- First-order variables ($x,y,z,\dots$) stand for objects in a domain (via an assignment $s:\mathtt{VAR}\to D$) and do **not** receive truth values.