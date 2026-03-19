---
down:
  - "[[Alphabet (PL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
A **propositional language** is the formal language used in **propositional logic**.  
Its basic expressions represent whole statements (propositions), and more complex expressions are built using logical connectives.

## Alphabet (symbols of PL)

### Propositional variables (sentence letters)
These are the atomic symbols:
$$
\mathtt{p},\mathtt{q},\mathtt{r},\dots
$$
They stand for whole propositions (informally), and receive truth values under a valuation.

### Logical connectives
$$
\lnot,\ \land,\ \lor,\ \to,\ \leftrightarrow
$$

### Grouping symbols
Parentheses (and sometimes brackets) are used for disambiguation:
$$
(\,),\quad [\,]
$$

## Grammar (formation rules)
PL-formulas (propositional forms) are defined recursively:

1. Every propositional variable is a PL-formula.  
2. If $\varphi$ and $\psi$ are PL-formulas, then so are:
   - $\lnot\varphi$
   - $(\varphi\land\psi)$
   - $(\varphi\lor\psi)$
   - $(\varphi\to\psi)$
   - $(\varphi\leftrightarrow\psi)$
1. Nothing else is a PL-formula.

## Semantics (truth in PL)
A **valuation** is a function
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}
$$
assigning each propositional variable a truth value.

The truth value of any compound formula is then determined from $\upnu$ by the truth tables for the connectives.

## What PL can and cannot express
- PL can express truth-functional combinations of whole statements.
- PL does **not** talk about objects in a domain, relations, or “for all/there exists” claims.  
  (Those belong to ***first-order logic*** via variables, predicates, and quantifiers.)