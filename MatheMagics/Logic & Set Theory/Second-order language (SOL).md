---
down:
  - "[[Alphabet (SOL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
# Second-order language (SOL)

## Alphabet
A **second-order language** extends a first-order language by adding **second-order variables** (variables that range over predicates/relations and sometimes functions).

It includes:
- **All first-order symbols**:
  - individual variables $x,y,z,\dots$
  - (optionally) constant symbols, function symbols, relation symbols
  - logical connectives $\lnot,\land,\lor,\to,\leftrightarrow$
  - quantifiers $\forall,\exists$
  - (usually) equality $=$
- **Second-order variables**, typically typed by arity:
  - unary predicate variables $P,Q,\dots$ (intended to range over subsets of the domain),
  - $n$-ary relation variables $R,S,\dots$ (intended to range over relations $A^n\to\{\mathtt{T},\mathtt{F}\}$),
  - sometimes **function variables** $F,G,\dots$ (intended to range over functions $A^n\to A$).

> Many presentations treat “sets” as a special case of **unary predicates**: a set of individuals is identified with its characteristic predicate.

## Syntax (what formulas can say)
SOL has (at least) the usual first-order formation rules **plus** quantification over second-order variables:
- If $\varphi$ is a formula and $P$ is a unary predicate variable, then $\forall P\,\varphi$ and $\exists P\,\varphi$ are formulas.
- More generally, if $R$ is $n$-ary, then $\forall R\,\varphi$ and $\exists R\,\varphi$ are formulas.

Second-order variables can appear in atomic formulas, e.g.:
- $P(t)$ for unary $P$,
- $R(t_1,\dots,t_n)$ for $n$-ary $R$,
where the $t_i$ are first-order terms.

### Examples
- $\forall P\,\exists x\,P(x)$
  “Every unary predicate holds of some object.”  
  (This is *not* valid in general; it depends on what predicates are allowed in the semantics.)

- $\exists R\,\forall x\,\forall y\,(R(x,y)\leftrightarrow x<y)$
  “There exists a binary relation that coincides with $<$.”  
  (If $<$ is already a relation symbol in the language, this is always satisfiable by taking $R$ to interpret the same relation as $<$.)

## Semantics (crucial fork)
Second-order logic depends heavily on what second-order variables are allowed to range over.

### Full (standard) semantics
If the domain is $A$, then:
- unary predicate variables range over **all** subsets of $A$ (i.e., $\mathcal{P}(A)$),
- $n$-ary relation variables range over **all** subsets of $A^n$,
- (if present) function variables range over **all** functions $A^n\to A$.

This is the “maximally intended” reading (quantifying over *all* properties/relations/functions on the domain).

### Henkin (general) semantics
Second-order variables range over some specified collections:
- unary predicate variables range over some $\mathcal{P}^\ast\subseteq \mathcal{P}(A)$,
- $n$-ary relation variables range over some $\mathcal{R}_n^\ast\subseteq \mathcal{P}(A^n)$,
- etc.

This makes SOL behave more like many-sorted first-order logic.

## Expressive power
SOL (especially with **full semantics**) can express properties not definable in FOL.

Typical examples (full semantics):
- **Finiteness** of the domain is expressible in SOL but not in FOL.
- Many “categoricity” statements become possible (e.g., second-order characterizations that pin down a structure up to isomorphism, where FOL cannot).

## Trade-offs (metatheory)
### First-order logic (FOL)
- Has a sound and complete proof system: all semantically valid FOL formulas are derivable (Gödel completeness theorem).
- Compactness and Löwenheim–Skolem theorems hold.

### Second-order logic (SOL)
- Under **full semantics**, there is **no** sound and complete effective proof system for all validities (“full SOL is not complete” in the proof-theoretic sense).
- Classical metatheorems such as **compactness** and **Löwenheim–Skolem** fail for full SOL.

- Under **Henkin semantics**, one can recover a **completeness theorem** (but then “SOL” is closer in spirit to a many-sorted first-order theory, and loses the “quantify over all subsets/relations” reading).

## Summary
- SOL = FOL + quantification over **predicate/relation (and sometimes function) variables**.
- The big distinction is **full** vs **Henkin** semantics.
- Full SOL is far more expressive than FOL, but sacrifices major proof-theoretic and model-theoretic properties (notably completeness).