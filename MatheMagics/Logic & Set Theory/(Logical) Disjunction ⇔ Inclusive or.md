---
down:
  - "[[Exclusive disjunction Ã¢â€¡â€ XOR]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea

**Logical disjunction** is the connective expressed by **or**.

If $\mathtt{p}$ and $\mathtt{q}$ are propositional forms, then

$$
\mathtt{p}\lor \mathtt{q}
$$

is true when **at least one** of $\mathtt{p},\mathtt{q}$ is true, and false only when **both** are false **(** i.e., ($\mathtt{p}$ or $\mathtt{q}$) or ($\mathtt{p}$ & $\mathtt{q}$) **)**

So logical disjunction is an **inclusive or**, not an exclusive one.

## Notation

The standard symbol for disjunction is

$$
\mathtt{p}\lor \mathtt{q}.
$$

It is read as:

- $\mathtt{p}$ or $\mathtt{q}$,
- either $\mathtt{p}$ or $\mathtt{q}$.

In logic, this **includes** the case in which both $\mathtt{p}$ and $\mathtt{q}$ are true.

Let $\mathtt{p}$ and $\mathtt{q}$ be propositional forms.

#### (Logical) Disjunction (Inclusive or)

##### Valuation form

$$
\upnu(\mathtt{p}\lor \mathtt{q})=
\begin{cases}
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{F}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]
\mathtt{T} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\lor \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |

## Reading guide

The disjunction

$$
\mathtt{p}\lor \mathtt{q}
$$

asserts that **at least one** of the two propositional forms is true.

So:

- if both are true, the disjunction is true;
- if exactly one is true, the disjunction is true;
- only if both are false is the disjunction false.

## Final summary

Logical disjunction is the **inclusive or**.

It is written as

$$
\mathtt{p}\lor \mathtt{q},
$$

and its truth valuation is determined by this rule:

$$
\upnu(\mathtt{p}\lor \mathtt{q})=\mathtt{T}
\quad \text{unless both } \upnu(\mathtt{p})=\mathtt{F} \text{ and } \upnu(\mathtt{q})=\mathtt{F}.
$$

