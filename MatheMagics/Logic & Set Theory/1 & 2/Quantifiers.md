---
down:
  - "[[Types of quantifiers]]"
  - "[[Quantifiers (what they do)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
A **quantifier** indicates whether **all** objects (subjects) in the domain, or **at least one** object (subject) in the domain, satisfy a given **property** (i.e., make a formula true).

Equivalently: a quantifier tells you how a formula $\varphi(x)$ depends on the possible values of a variable $x$.

## Types:
In first-order logic, there are two quantifiers:

- [[Universal quantifier]]: $\forall$  
  Read: “for all” or “for every.”  
  $\forall x\,\varphi(x)$ says that **every** object (subject) in the domain satisfies $\varphi$.

- [[Existential quantifier]]: $\exists$  
  Read: “there exists.”  
  $\exists x\,\varphi(x)$ says that **at least one** object (subject) in the domain satisfies $\varphi$.

## Binding and scope (needed for correct parsing)
In $\forall x\,\varphi$ and $\exists x\,\varphi$, the quantifier **binds** the variable $x$ (variable) in $\varphi$ (S-formula).  
The part of the formula $\varphi$ that the quantifier governs is called its **scope**.

A variable occurrence is:
- **bound** if it lies in the scope of a quantifier for that variable,
- **free** otherwise.

A formula with **no free variables** is a **sentence** (closed formula).