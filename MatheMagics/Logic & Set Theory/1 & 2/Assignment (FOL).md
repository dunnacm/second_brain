---
down:
  - "[[Standard FOL semantics]]"
  - "[[Assignment (FOL), accompanying note]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Purpose
A **structure** is the semantic “universe” in which first-order formulas are evaluated.  
It provides:
- a **domain** of objects, and
- meanings for the **theory symbols** (constants, function symbols, relation symbols).

An **$S$-interpretation** (in O’Leary’s sense) supplies the current values of variables and thereby determines the denotations of all **terms** inside that structure.

## Structure (model-theoretic object)
Fix a first-order alphabet with theory-symbol set $S$.

A **structure** is a pair
$$
\mathfrak{A}=(A,a),
$$
where $A\neq\varnothing$ is the **domain** and $a$ is a function with domain $S$ such that:
- if $c\in S$ is a constant symbol, then $a(c)\in A$;
- if $R\in S$ is an $n$-ary relation symbol, then $a(R)\subseteq A^n$;
- if $f\in S$ is an $n$-ary function symbol, then $a(f):A^n\to A$.

Terminology:
- $A=\mathrm{dom}(\mathfrak{A})$ is the **domain**.
- For $s\in S$, $a(s)$ is the **meaning** of $s$ in $\mathfrak{A}$, and $s$ is the **name** of that object/relation/function.

## $S$-interpretation of a structure (term evaluation via variable assignment)
To evaluate formulas, we first evaluate **terms** as elements of the domain.

Given a structure $\mathfrak{A}=(A,a)$, an **$S$-interpretation of $\mathfrak{A}$** is a function
$$
I:\mathrm{TERMS}(\mathfrak{A})\to A
$$
satisfying:
- if $x$ is a variable symbol, then $I(x)\in A$;
- if $c$ is a constant symbol, then $I(c)=a(c)$;
- if $f$ is $n$-ary and $t_0,\ldots,t_{n-1}$ are terms, then
$$
I\bigl(f(t_0,\ldots,t_{n-1})\bigr)=a(f)\bigl(I(t_0),\ldots,I(t_{n-1})\bigr).
$$

**Idea:** $a$ fixes what the nonlogical symbols *mean*; choosing values $I(x)$ for variables fixes $I(t)$ for every term $t$ by recursion.

### Variant interpretations (changing one variable)
If $x$ is a variable and $b\in A$, define the modified interpretation $I_x^b$ by:
- $I_x^b(x)=b$,
- $I_x^b(y)=I(y)$ for every variable $y\neq x$,
- and extend to all terms by the same constant/function clauses above.

## Satisfaction (truth of formulas in a structure under an interpretation)
With a structure $\mathfrak{A}$ and an $S$-interpretation $I$, define satisfaction $\mathfrak{A}\vDash \varphi[I]$ recursively:

### Atomic formulas
- Equality:
$$
\mathfrak{A}\vDash (t_0=t_1)[I]\ \Leftrightarrow\ I(t_0)=I(t_1).
$$
- Relation symbols:
$$
\mathfrak{A}\vDash R(t_0,\ldots,t_{n-1})[I]\ \Leftrightarrow\ (I(t_0),\ldots,I(t_{n-1}))\in a(R).
$$

### Connectives
(Truth-functional, as usual; for example)
$$
\mathfrak{A}\vDash (\lnot\varphi)[I]\ \Leftrightarrow\ \text{not }(\mathfrak{A}\vDash \varphi[I]),
$$
$$
\mathfrak{A}\vDash (\varphi\to\psi)[I]\ \Leftrightarrow\ \text{if }\mathfrak{A}\vDash\varphi[I]\text{ then }\mathfrak{A}\vDash\psi[I].
$$
(Other connectives can be handled similarly or defined from $\lnot,\to$.)

### Quantifiers
- Existential:
$$
\mathfrak{A}\vDash (\exists x\,\varphi)[I]\ \Leftrightarrow\ \text{for some }b\in A,\ \mathfrak{A}\vDash \varphi[I_x^b].
$$
- Universal:
$$
\mathfrak{A}\vDash (\forall x\,\varphi)[I]\ \Leftrightarrow\ \text{for all }b\in A,\ \mathfrak{A}\vDash \varphi[I_x^b].
$$

## Summary
- **Structure** $\mathfrak{A}=(A,a)$: domain $A$ plus meanings $a(s)$ for each theory symbol $s\in S$.
- **$S$-interpretation** $I:\mathrm{TERMS}(\mathfrak{A})\to A$: assigns values to variables and thereby evaluates all terms.
- **Satisfaction** $\mathfrak{A}\vDash\varphi[I]$: defines truth of formulas in $\mathfrak{A}$ relative to $I$ (sentences are the special case with no free variables).