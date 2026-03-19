---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
An **S-sentence** is an S-formula with **no free variables**.  
Equivalently, an **S-sentence** is a **closed formula**, also called a **sentence**:
$$
\mathrm{FV}(\varphi)=\varnothing.
$$

Equivalently:
- every variable occurrence in $\varphi$ is **bound** by some quantifier, and
- the truth value of $\varphi$ (in a structure $\mathcal{M}$) is **independent of any variable assignment**.

## Why “closed” matters
A formula with free variables is more like a *condition* on objects: to evaluate it you typically need an assignment of domain elements to those free variables.  
A **closed** formula has no such “inputs,” so once a structure $\mathcal{M}$ is fixed, it expresses a complete statement that is either true or false.

*(Constants may appear in a closed formula, but they do not bind variables; closure is about quantifiers and free variables.)*

## Examples
### Example 1
$$
\forall x\,\forall y\,\forall z\;\bigl[(x+y)+z=x+(y+z)\bigr].
$$
This formula has **no free variables**, so it is an S-sentence (a closed formula).

### Example 2
$$
\forall x\,(x>5).
$$

### Example 3
$$
2>5.
$$

## Important remark (PL vs FOL)
An S-sentence is **not** a “propositional form” in the propositional-logic sense. It is a **first-order sentence**.

However, every S-sentence determines a proposition in the semantic sense: it has a truth value in each structure $\mathcal{M}$.  
It also has a **propositional skeleton** obtained by treating each **atomic** first-order subformula as a propositional variable and keeping the same connective pattern.