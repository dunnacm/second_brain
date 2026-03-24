---
down:
  - "[[Propositional form or ((wffs) or (PL-formula))]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Goal
**Symbolization** in first-order logic (FOL) is the process of translating an informal statement about objects and their relationships into an **FOL formula** (S-formula), often a **sentence** (closed formula) when the result is meant to be a complete statement.

- Input: an informal proposition (semantic).
- Output: an S-formula / S-sentence (syntactic).

## Procedure
1) Fix a **domain of discourse** (what the variables range over).  
2) Choose the needed **theory symbols** (nonlogical vocabulary):
	- constant symbols (named objects),
	- function symbols (operations),
	- predicate/relation symbols (properties/relations).
3) Translate:
	- properties/relations as **atomic formulas** (e.g., $P(t)$, $R(t_1,t_2)$, $t_1=t_2$),
	- connectives as in PL,
	- “for all” / “there exists” using quantifiers $\forall,\exists$ with clear scope.
4) Check free vs bound variables; if you intend a complete statement, aim for a **closed formula**.

### Example (quantifiers)
Informal: “Every real number has a square that is at least $0$.”
One possible formalization:
$$
\forall x\,\exists y\,(y=x^2\land y\ge 0).
$$

## Semantics reminder (FOL)
Truth is evaluated in a structure $\mathcal{M}$ (domain + meanings for theory symbols).  
Open formulas may require a variable assignment $s:\mathtt{VAR}\to D$; sentences do not depend on $s$.

## Checklist
- The chosen predicates/functions/constants match the intended meaning.
- Quantifier scope is unambiguous (parentheses placed deliberately).
- No unintended free variables (unless you intentionally want an open formula).
- Substitution steps respect “free for” conditions (avoid variable capture).