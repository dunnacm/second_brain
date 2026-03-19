---
down:
  - "[[(Existential and Universal propositions) vs (Existential and Universal formulas)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Existential formulas vs Universal formulas

### Terminology note
In FOL, a **formula** need not be a **sentence**: it may contain **free variables**.  
So here “existential formula” and “universal formula” are **syntactic** labels about how the formula begins, not (necessarily) about a closed statement.

When people say “existential formula” vs “universal formula,” they usually mean the **leading (outermost) quantifier** (often after rewriting into prenex form):

- **Existential formula:** begins with $\exists$.
- **Universal formula:** begins with $\forall$.

Also: the **order** of quantifiers generally matters (e.g., $\forall x\,\exists y\,\varphi$ is usually different from $\exists y\,\forall x\,\varphi$).

## Existential formula
An **existential formula** is a formula of the form
$$
(\exists x)\,\varphi,
$$
where $x$ is a variable symbol and $\varphi$ is a formula.

It may contain multiple leading existential quantifiers:
$$
(\exists x_1)(\exists x_2)\cdots(\exists x_n)\,\varphi.
$$

An existential formula may still have **free variables** (variables of $\varphi$ not bound by these quantifiers).

### Example (open formula)
Let $f(x)=2x^2+1$. Then
$$
(\exists x\in\mathbb{R})\,[\,f(x)=y\,]
$$
is an existential formula with **free variable** $y$.

### Example (sentence)
$$
(\exists x\in\mathbb{R})\,[\,2x^2+1=1\,]
$$
is an existential **sentence** (no free variables).

## Universal formula
A **universal formula** is a formula of the form
$$
(\forall x)\,\varphi,
$$
where $x$ is a variable symbol and $\varphi$ is a formula.

It may contain multiple leading universal quantifiers:
$$
(\forall x_1)(\forall x_2)\cdots(\forall x_n)\,\varphi.
$$

A universal formula may still have **free variables** (variables of $\varphi$ not bound by these quantifiers).

### Example (open formula)
Let $f(x)=2x^2+1$. Then
$$
(\forall x\in\mathbb{R})\,[\,y=2x^2+1\,]
$$
is a universal formula with **free variable** $y$.

### Example (sentence)
$$
(\forall x\in\mathbb{R})\,[\,2x^2+1\ge 1\,]
$$
is a universal **sentence** (no free variables).

## Contrast: formulas vs propositions (sentences)
- A **proposition** (in this context) is typically a **sentence**: it has no free variables and is true/false in a structure.
- A **formula** may have free variables and generally needs an assignment to be evaluated.