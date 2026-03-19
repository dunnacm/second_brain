---
down:
  - "[[Existential vs Universal (formula)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition (syntactic)
An **existential formula** is a formula of first-order logic that begins with an existential quantifier.  
That is, it has the form $(\exists x)\,\varphi$ where $x$ is a variable symbol and $\varphi$ is a formula.

More generally, an existential formula may have several leading existential quantifiers:
$$
(\exists x_1)(\exists x_2)\cdots(\exists x_n)\,\varphi.
$$

## Free vs bound (what it guarantees)
In $(\exists x)\,\varphi$, the quantifier $\exists x$ **binds** the variable $x$ in $\varphi$ (within its scope).  
Other variables in $\varphi$ may remain **free**.

So:
- an **existential formula** need not be a sentence,
- it is a **sentence** exactly when it has no free variables.

## Semantic reading (how it is evaluated)
Let $\mathcal{M}$ be a structure with domain $D$, and let $s:\mathtt{VAR}\to D$ be a variable assignment.

Then
$$
\mathcal{M},s \models (\exists x)\,\varphi
$$
means:

> there is some subject $d\in D$ such that, if we change $s$ so that it sends $x$ to $d$ (leaving all other variables the same), the resulting assignment makes $\varphi$ true.

Informally: “**there exists** an object in the domain that makes $\varphi$ true.”

## Warning about multiple quantifiers
If both $\forall$ and $\exists$ occur, the **order matters** in general:
$$
(\forall x)(\exists y)\,\psi \quad \text{is usually different from} \quad (\exists y)(\forall x)\,\psi.
$$