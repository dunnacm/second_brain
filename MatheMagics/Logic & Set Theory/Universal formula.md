---
down:
  - "[[Existential vs Universal (formula)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition (syntactic)
A **universal formula** is a formula of first-order logic that begins with a universal quantifier.  
That is, it has the form $(\forall x)\,\varphi$ where $x$ is a variable symbol and $\varphi$ is a formula.

More generally, a universal formula may have several leading universal quantifiers:
$$
(\forall x_1)(\forall x_2)\cdots(\forall x_n)\,\varphi.
$$

## Free vs bound (what it guarantees)
In $(\forall x)\,\varphi$, the quantifier $\forall x$ **binds** the variable $x$ in $\varphi$ (within its scope).  
Other variables in $\varphi$ may remain **free$.$**

So:
- a **universal formula** need not be a sentence,
- it is a **sentence** exactly when it has no free variables.

## Semantic reading (how it is evaluated)
Let $\mathcal{M}$ be a structure with domain $D$, and let $s:\mathtt{VAR}\to D$ be a variable assignment.

Then
$$
\mathcal{M},s \models (\forall x)\,\varphi
$$
means:

> for every subject $d\in D$, if we change $s$ so that it sends $x$ to $d$ (leaving all other variables the same), the resulting assignment makes $\varphi$ true.

Informally: “**for every** object in the domain, $\varphi$ holds.”

## Warning about multiple quantifiers
If both $\forall$ and $\exists$ occur, the **order matters** in general:
$$
(\forall x)(\exists y)\,\psi \quad \text{is usually different from} \quad (\exists y)(\forall x)\,\psi.
$$
---