---
down:
  - "[[(Existential and Universal propositions) vs (Existential and Universal formulas)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Existential propositions vs Universal propositions

### Terminology note
In FOL, a statement can contain **both** $\forall$ and $\exists$.  
When people say “existential proposition” vs “universal proposition,” they usually mean the **leading (outermost) quantifier**:

- **Existential proposition:** starts with $\exists$ (in prenex form).
- **Universal proposition:** starts with $\forall$ (in prenex form).

Also: the **order** of quantifiers generally matters (e.g., $\forall x\,\exists y\,\varphi$ is usually different from $\exists y\,\forall x\,\varphi$).

## Existential proposition
An **existential proposition** asserts that **at least one** subject in the domain makes a property true.

It may contain multiple quantifiers (including universal quantifiers inside), but it is “existential” in the sense that it begins with an existential claim.

### Example
Let $f(x)=2x^2+1$.
$$
(\exists x\in\mathbb{R})\,[\,f(x)=1\,].
$$
Read: “There exists a real number $x$ such that $2x^2+1=1$.”

## Universal proposition
A **universal proposition** asserts that **every** subject in the domain makes a property true.

It may contain multiple quantifiers (including existential quantifiers inside), but it is “universal” in the sense that it begins with a universal claim.

### Example (your quadratic, corrected)
Define the function
$$
f:\mathbb{R}\to[1,\infty),\qquad f(x)=2x^2+1.
$$

One natural quantified proposition is:
$$
(\forall x\in\mathbb{R})(\exists y\in[1,\infty))\,[\,y=2x^2+1\,].
$$

Read: “For every real number $x$, there exists a number $y$ in $[1,\infty)$ such that $y=2x^2+1$.”

*(Here it’s important that $y$ is taken from $[1,\infty)$, not from all of $\mathbb{R}$.)*