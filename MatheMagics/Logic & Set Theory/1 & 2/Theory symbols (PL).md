---
up:
down:
  - "[[Propositional variables]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Preface
Terminology note (following O’Leary): in FOL, the subject-specific nonlogical vocabulary is explicitly called **theory symbols** (constant symbols, function symbols, predicate symbols).

> **Note:**
> In PL, O’Leary does not typically use the label “theory symbols”; instead, the analogous nonlogical vocabulary is carried by **propositional variables** (sentence letters).  
> So it is more accurate to call $\mathtt{P},\mathtt{Q},\mathtt{R}$ **propositional variables** (or **sentence letters**), not “theory symbols,” even though they fill the nonlogical-vocabulary role in PL.

## Definition
In **propositional logic (PL)**, the “content-bearing” symbols are the **propositional variables** (sentence letters) such as $\mathtt{P},\mathtt{Q},\mathtt{R}$. Each is intended to stand for an entire **proposition** (a declarative statement that is true or false).

By themselves, propositional variables have no fixed meaning. They become meaningful only once we decide what statements they are being used to represent, and—formally—once we choose a **valuation**
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}
$$
which assigns a truth value to each propositional variable (and thereby determines the truth value of any compound propositional form built from them).

## Helpful analogy with FOL (limited but useful)
Propositional variables in PL play a role analogous to **atomic formulas** in FOL: they are the basic statement-units that are treated as indivisible at that level, and then the logic uses connectives (and, in FOL, also quantifiers) to build more complex statements.

*(Caveat: in FOL, atomic formulas have internal structure—predicate symbols applied to terms—even though they count as “atomic” for building larger formulas.)*