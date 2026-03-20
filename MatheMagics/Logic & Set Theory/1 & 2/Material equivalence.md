---
alases:
down:
  - "[[Verbalization (material equivalence)]]"
  - "[[Material equivalence + Logical equivalence]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Material equivalence

A **biconditional** is the propositional form built with the connective $\leftrightarrow$.  
Its truth-functional reading is called **material equivalence**.

## Definition

$$\mathtt{A}\leftrightarrow \mathtt{B}\ \Leftrightarrow\ (\mathtt{A}\to \mathtt{B})\land(\mathtt{B}\to \mathtt{A}).$$

Equivalently,

$$\mathtt{A}\leftrightarrow \mathtt{B}\ \Leftrightarrow\ (\mathtt{A}\land \mathtt{B})\lor(\neg \mathtt{A}\land \neg \mathtt{B}).$$

So, $\mathtt{A}\leftrightarrow \mathtt{B}$ is true **exactly when** $\mathtt{A}$ and $\mathtt{B}$ have the same truth value.

## Truth table for $\leftrightarrow$

| $\mathtt{A}$ | $\mathtt{B}$ | $\mathtt{A}\leftrightarrow \mathtt{B}$ |
| --- | --- | --- |
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ |
## Truth valuation
$$
\upnu(\mathtt{p}\leftrightarrow \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\upnu(\mathtt{q}),\\[6pt]
\mathtt{F} & \text{otherwise}.
\end{cases}
$$

## Parsing note
### 1. Formal Logic (The Associative Interpretation)

If the intent is to evaluate truth values strictly as sequential binary operations, parenthesize explicitly:

$$(\mathtt{A} \leftrightarrow \mathtt{B}) \leftrightarrow \mathtt{C} \quad \text{or} \quad \mathtt{A} \leftrightarrow (\mathtt{B} \leftrightarrow \mathtt{C})$$

_(Note: Because the logical biconditional is associative, **both groupings yield identical truth values**. The compound statement is True if all three propositions are True, or if exactly one is True)._

### Mathematical Proofs (The Chained Equivalence Interpretation)

If the intent is to declare that all propositions share the exact same truth value (mutual equivalence), rewrite using explicit conjunctions:

$$(\mathtt{A} \leftrightarrow \mathtt{B}) \land (\mathtt{B} \leftrightarrow \mathtt{C})$$

