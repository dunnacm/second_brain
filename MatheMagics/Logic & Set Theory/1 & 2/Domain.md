---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
Fix a first-order alphabet with theory-symbol set $S$.

If
$$
\mathfrak{A}=(A,a)
$$
is an $S$-structure, then its **domain** (or **universe**) is the nonempty set
$$
A=\mathrm{dom}(\mathfrak{A})\neq\varnothing,
$$
the set of **objects** that variables range over.

## Role in interpretation of the language
An $S$-structure $\mathfrak{A}=(A,a)$ interprets the nonlogical symbols by a single **meaning map**
$$
a:S\to \bigcup_{n\ge 0}\bigl(A\cup A^n\cup A^{A^n}\bigr)
$$
(Informally: $a$ assigns to each theory symbol its semantic value in $\mathfrak{A}$), with the clauses:
- if $c\in S$ is a constant symbol, then $a(c)\in A$;
- if $R\in S$ is an $n$-ary relation symbol, then $a(R)\subseteq A^n$;
- if $f\in S$ is an $n$-ary function symbol, then $a(f):A^n\to A$.

## Connection to assignments and quantifiers
To evaluate formulas with free variables, use an **interpretation**
$$
I:\mathrm{TERMS}(\mathfrak{A})\to A
$$
(which assigns values to variables in $A$ and extends recursively to all terms).

If $x$ is a variable and $b\in A$, let $I_x^b$ be the interpretation that agrees with $I$ on all variables except that $I_x^b(x)=b$.

Quantifiers “range over” $A$:
$$
\mathfrak{A}\vDash (\forall x\,\varphi)[I]
\ \Leftrightarrow\
\text{for all }b\in A,\ \mathfrak{A}\vDash \varphi[I_x^b],
$$
$$
\mathfrak{A}\vDash (\exists x\,\varphi)[I]
\ \Leftrightarrow\
\text{for some }b\in A,\ \mathfrak{A}\vDash \varphi[I_x^b].
$$