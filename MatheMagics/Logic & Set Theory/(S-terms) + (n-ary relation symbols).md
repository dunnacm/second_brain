---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Rule 2 (Atomic S-formulas from relation symbols)

### What the rule says
If $R$ is an $n$-ary **relation (predicate) symbol** and $t_0,\dots,t_{n-1}$ are **terms**, then
$$
R(t_0,\dots,t_{n-1})
$$
is an **atomic formula** (an “S-formula” at the base level).

### Why it matters
Predicate symbols are the other main bridge from **terms** to **formulas**: they assert that the tuple of objects denoted by the terms stands in the relation $R$.

### Examples
- Unary: $\mathtt{Prime}(x)$
- Binary: $<(x,y)$ (often written $x<y$)
- Mixed terms: $R(x,f(y))$
- Ternary: $\mathtt{Between}(x,y,z)$