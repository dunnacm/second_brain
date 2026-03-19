---
down:
  - "[[Parametrizing a formula by its FVs]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
A **closed formula** (also called a **sentence**) is a formula with **no free variables**.

Equivalently:
- every variable occurrence in the formula is **bound** by a quantifier, and
- no truth evaluation needs a variable assignment.

Because a closed formula has no “loose” variables left, it expresses a complete statement: once an interpretation (structure) is fixed, it is either true or false.

*(Minor correction: variables are not “replaced by a constant” to become closed; rather, closure is about being bound by quantifiers. Constants can appear, but they don’t bind variables.)*

## Notation
If $\varphi$ is closed (i.e., $\mathrm{FV}(\varphi)=\varnothing$), then its truth in a structure $\mathcal{M}$ is independent of any assignment $s$. Some authors express this by suppressing assignments/arguments (informally “no inputs”), but the specific notation $p()$ is not standard.

## Examples
- $\forall x\,(x>5).$
- $2>5.$