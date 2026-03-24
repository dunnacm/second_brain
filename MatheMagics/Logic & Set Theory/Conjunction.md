---
down:
  - "[[Conjunction (Conj)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
Proposition formed by combining two propositions (conjuncts) with the connective word "and": p $\land$ q

Let $\mathtt{p}$ and $\mathtt{q}$ be propositional forms.

#### Conjunction

##### Valuation form
$$
\upnu(\mathtt{p}\land \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{T},\\[6pt]
\mathtt{F} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\land \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |
