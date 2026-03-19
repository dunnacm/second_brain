---
up:
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
The symbol $=$ expresses **identity**: two terms denote the **same object** in the domain.

In first-order logic, equality is commonly treated as a **logical symbol** (often: “FOL with identity”), and its intended meaning is fixed as genuine identity on the domain.

## Where it appears (syntax)
Equality forms an **atomic formula**:
$$
t_0=t_1,
$$
where $t_0,t_1$ are **terms** (i.e., $S$-terms).  
So $=$ is not a connective and not a quantifier; it is a formation rule for atomic formulas from terms.

## How it is evaluated (semantics)
Fix an $S$-structure
$$
\mathfrak{A}=(A,a)
$$
and an interpretation
$$
I:\mathrm{TERMS}(\mathfrak{A})\to A.
$$
Then:
$$
\mathfrak{A}\vDash (t_0=t_1)[I]
\ \Leftrightarrow\
I(t_0)=I(t_1).
$$

Informally: “$t_0$ and $t_1$ denote the same object of $A$ (under $I$).”

## Variables, constants, and complex terms
- Variables may take different values depending on the interpretation $I$ (specifically, on the values $I(x)$ assigned to variables).
- Constant symbols have fixed denotations in the structure: for any constant symbol $c$,
$$
I(c)=a(c)\in A.
$$
- Functional terms are evaluated by applying the function meaning from the structure:
if $f$ is $n$-ary, then
$$
I\bigl(f(t_0,\ldots,t_{n-1})\bigr)
=
a(f)\bigl(I(t_0),\ldots,I(t_{n-1})\bigr).
$$

Equality compares the resulting denotations $I(t_0)$ and $I(t_1)$, regardless of whether the terms are variables, constants, or built using function symbols.

## Equality properties (intended behavior)
Identity is intended to satisfy the usual laws (valid in every structure under the intended identity interpretation):

- **Reflexive:** $x=x$
- **Symmetric:** $x=y \to y=x$
- **Transitive:** $(x=y \land y=z)\to x=z$

It is also **substitutive** (Leibniz-style): if $t_0=t_1$, then replacing occurrences of $t_0$ by $t_1$ in a formula should preserve truth *when the replacement is legitimate*.

*(The exact substitution rule is proof-system dependent; some calculi include equality axioms/rules explicitly.)*