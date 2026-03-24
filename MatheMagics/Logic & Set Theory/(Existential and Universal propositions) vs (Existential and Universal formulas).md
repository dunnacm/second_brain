---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Existential/Universal propositions vs Existential/Universal formulas

### Key distinction: proposition (sentence) vs formula
- A **formula** may have **free variables**.
- A **proposition** (in this context) is a **sentence** (closed formula): it has **no free variables** and so has a truth value in a structure (independent of any assignment).

### Existential and universal *formulas* (syntactic labels)
These describe how a formula begins.

- **Existential formula:** has the form
  $$ (\exists x)\,\varphi. $$
  It may still have free variables other than $x$.

- **Universal formula:** has the form
  $$ (\forall x)\,\varphi. $$
  It may still have free variables other than $x$.

(With multiple quantifiers: $(\exists x_1)\cdots(\exists x_n)\varphi$ and $(\forall x_1)\cdots(\forall x_n)\varphi$.)

### Existential and universal *propositions* (closed cases)
These are just the **sentence** versions of the above.

- **Existential proposition:** an existential **formula** with **no free variables** (an existential sentence).  
  Example:
  $$ (\exists x\in\mathbb{R})\,[\,2x^2+1=1\,]. $$

- **Universal proposition:** a universal **formula** with **no free variables** (a universal sentence).  
  Example:
  $$ (\forall x\in\mathbb{R})\,[\,2x^2+1\ge 1\,]. $$

### Practical test
- If, after writing the quantified expression, there is **any** variable left unquantified, you have a **formula** (open).  
- If **every** variable occurrence is bound by some quantifier, you have a **proposition** (sentence/closed).

### Reminder (when both quantifiers appear)
A sentence/formula can contain both $\forall$ and $\exists$.  
When people label something “existential” or “universal,” they usually mean the **leading (outermost) quantifier** (often after rewriting into prenex form), and the **order** of quantifiers generally matters.