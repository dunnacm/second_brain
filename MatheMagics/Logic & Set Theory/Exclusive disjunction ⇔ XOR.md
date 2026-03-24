---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea

**Exclusive disjunction** expresses **either ... or ..., but not both** **(** i.e., ($\mathtt{p}$ or $\mathtt{q}$) and ~($\mathtt{p}$ & $\mathtt{q}$) **)**

If $\mathtt{p}$ and $\mathtt{q}$ are propositional forms, then their exclusive disjunction is true exactly when **one** of them is true and the other is false.

## Notation

A common notation for exclusive disjunction is

$$
\mathtt{p}\veebar \mathtt{q}.
$$

Another common notation is

$$
\mathtt{p}\oplus \mathtt{q}.
$$

In this note, we will use

$$
\mathtt{p}\veebar \mathtt{q}.
$$

The propositional form for the exclusive or is

$$
(\mathtt{p}\lor \mathtt{q})\land \neg(\mathtt{p}\land \mathtt{q}).
$$

So, in this notation, $\mathtt{p}\veebar \mathtt{q}$ is understood as the form $(\mathtt{p}\lor \mathtt{q})\land \neg(\mathtt{p}\land \mathtt{q}).$, i.e., $\vDash (p \veebar q) \leftrightarrow ((p \lor q) \land \neg(p \land q))$ or $\mathtt{p}\veebar \mathtt{q}\;\equiv\;(\mathtt{p}\lor \mathtt{q})\land \neg(\mathtt{p}\land \mathtt{q}).$

This means:

- at least one of $\mathtt{p},\mathtt{q}$ is true, and
- not both are true.

## Truth valuation

Let $\mathtt{p}$ and $\mathtt{q}$ be propositional forms.

### Valuation form

$$
\upnu(\mathtt{p}\veebar \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})\neq \upnu(\mathtt{q}),\\[6pt]
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\upnu(\mathtt{q}).
\end{cases}
$$

Equivalently,

$$
\upnu(\mathtt{p}\veebar \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{F}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{T},\\[6pt]
\mathtt{F} & \text{otherwise}.
\end{cases}
$$

### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\veebar \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |

### Expanded truth table

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\land \mathtt{q})$ | $\upnu\bigl(\neg(\mathtt{p}\land \mathtt{q})\bigr)$ | $\upnu(\mathtt{p}\lor \mathtt{q})$ | $\upnu\bigl((\mathtt{p}\lor \mathtt{q})\land \neg(\mathtt{p}\land \mathtt{q})\bigr)$ |
|---|---|---|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |

## Final summary

Exclusive disjunction is true exactly when **one, and only one**, of $\mathtt{p}$ and $\mathtt{q}$ is true.

In this note, it is written as

$$
\mathtt{p}\veebar \mathtt{q}.
$$

Its truth conditions are those of the propositional form

$$
(\mathtt{p}\lor \mathtt{q})\land \neg(\mathtt{p}\land \mathtt{q}).
$$