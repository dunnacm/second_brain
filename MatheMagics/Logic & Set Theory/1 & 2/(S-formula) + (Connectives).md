---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Rule 3 (S-formulas under propositional connectives)

### What the rule says
If $\varphi$ and $\psi$ are **formulas**, then combining them with propositional connectives produces new formulas:
$$
\lnot\varphi,\quad
(\varphi\land\psi),\quad
(\varphi\lor\psi),\quad
(\varphi\to\psi),\quad
(\varphi\leftrightarrow\psi).
$$

### Why it matters
This is how FOL inherits the “Boolean” structure of propositional logic: once you have formulas (atomic or not), you can build more complex formulas with connectives.

### Examples
Let $\varphi$ be $P(x)$ and $\psi$ be $Q(y)$.
- $\lnot P(x)$
- $(P(x)\lor Q(y))$
- $(P(x)\to Q(x))$
- $(x=y)\to R(x)$