---
down:
  - "[[Strings (PL)]]"
  - "[[Strings (FOL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core similarity
Both PL and FOL use the same **propositional connectives**
$$
\lnot,\ \land,\ \lor,\ \to,\ \leftrightarrow
$$
so they share the same connective-composition behavior.  
This is why propositional **inference** and **replacement** rules apply to the connective part of FOL proofs.

## Propositional form in PL
In **propositional logic (PL)**, a **propositional form** is simply a **PL-formula** (a wff) built from:
- propositional variables (sentence letters) $\mathtt{p},\mathtt{q},\mathtt{r},\dots$
- connectives $\lnot,\land,\lor,\to,\leftrightarrow$
- grouping symbols.

So in PL:
- **propositional form = formula (wff)**,
- and semantics uses a valuation
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\},
$$
which assigns truth values to propositional variables and thereby determines the truth value of any compound propositional form.

---

## Propositional form in FOL (propositional skeleton)
In **first-order logic (FOL)**, formulas may contain:
- terms (S-terms),
- predicate/relation symbols,
- equality,
- quantifiers ($\forall,\exists$),
in addition to the propositional connectives.

The phrase “propositional form” is best understood here as a **propositional skeleton**:

> The **propositional skeleton** of an FOL formula is obtained by treating each **atomic** FOL formula as a propositional variable, while keeping the same connective pattern.

Example:
$$
(\forall x)\bigl(P(x)\to Q(x)\bigr)
$$
has connective pattern “$\forall x(\,\_ \to \_\,)$”, and inside the scope the skeleton is
$$
\mathtt{p}\to \mathtt{q},
$$
where $\mathtt{p}$ stands for $P(x)$ and $\mathtt{q}$ stands for $Q(x)$.

**Use:** this is what justifies reusing PL proof steps on the connective structure that appears inside FOL derivations.

---

## Main differences (PL forms vs FOL skeletons)
- In PL, the “atoms” $\mathtt{p},\mathtt{q},\dots$ are **primitive** (no internal structure).
- In FOL, the “atoms” (atomic formulas) **do** have internal structure (predicates applied to terms, or equalities like $t_0=t_1$).
- FOL has **quantifiers**, so propositional reasoning alone is incomplete for FOL.

---

## Why FOL still needs extra rules (quantifiers)
Propositional rules do not handle $\forall$ and $\exists$. Additional **quantifier rules** are needed, especially when proving $S$-sentences (closed formulas).

Typical quantifier rules enable:

- **Instantiation** (removal of quantifiers), e.g.
	- **universal instantiation (UI)**
	- **existential instantiation (EI)** (with the usual “fresh witness” restriction)

- **Generalization** (adjoining of quantifiers), e.g.
	- **existential generalization (EG)**
	- **universal generalization (UG)** (with the usual restrictions)

- **Quantifier–negation interaction** (often treated as replacement rules), e.g.
	- $\neg\forall x\,\varphi \ \Leftrightarrow\ \exists x\,\neg\varphi$
	- $\neg\exists x\,\varphi \ \Leftrightarrow\ \forall x\,\neg\varphi$

---

## Summary
- **PL:** propositional form = PL-formula (wff), evaluated by a valuation $\upnu$.
- **FOL:** “propositional form” (usefully) = propositional skeleton of an FOL formula.
- **Reuse:** PL inference/replacement rules control connective reasoning in both settings.
- **Extra:** FOL requires quantifier rules beyond the propositional apparatus.