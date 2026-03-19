---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Rule 4 (Quantified formulas)

### What the rule says
If $x$ is a **variable** and $\varphi$ is a **formula**, then
$$
\exists x\,\varphi
\qquad\text{and}\qquad
\forall x\,\varphi
$$
are formulas. Quantifiers **bind** $x$ in $\varphi$ (within their scope).

### Why it matters
Quantifiers let formulas say something about **all** subjects in the domain ($\forall$) or **at least one** subject ($\exists$). They are what makes FOL richer than PL.

### Examples
- $\forall x\,(\mathtt{Prime}(x)\to \mathtt{Odd}(x))$
- $\exists x\,\mathtt{Prime}(x)$
- Mixed quantifiers: $\forall x\,\exists y\,R(x,y)$
- Binding a variable in an equality context: $\exists x\,(x=c)$