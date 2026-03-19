---
down:
  - "[[Propositional form or ((wffs) or (PL-formula))]]"
  - "[[Assignment operator]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition

An **assignment** is the process of associating each **propositional variable** with a specific **proposition** (a declarative sentence that is TRUE or FALSE).  
It is the step that gives propositional variables their intended meaning (what they “stand for”).

Example:
- $P :=$ “Squares are rectangles.”
- $Q :=$ “Squares are quadrilaterals.”

After an assignment is fixed, a valuation $\upnu$ can evaluate propositional forms by outputting $T/F$ (starting with the assigned propositional variables and extending by truth tables).
## Goal
**Symbolization** in propositional logic (PL) is the process of translating an informal, truth-apt statement into a **PL-formula** (a propositional form).

- Input: an informal proposition (semantic).
- Output: a PL-formula (syntactic).

## Procedure
1) Identify the **component declarative statements** (the parts that can each be true/false).  
2) Assign a **propositional variable** (sentence letter) to each component statement.  
3) Rebuild the overall structure using the connectives
$$
\lnot,\ \land,\ \lor,\ \to,\ \leftrightarrow
$$
and grouping symbols.

### Example
Proposition: “If squares are rectangles, then squares are quadrilaterals.”
- Let $\mathtt{P}$ := “Squares are rectangles.”
- Let $\mathtt{Q}$ := “Squares are quadrilaterals.”
- Symbolization:
$$
\mathtt{P}\to \mathtt{Q}.
$$

### Semantics reminder (PL)
A valuation assigns truth values to sentence letters:
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}.
$$
Truth tables then determine the truth value of any PL-formula under $\upnu$.
A **valuation** $\upnu$ then associates a truth value to (at least) each propositional variable by looking at the truth value of the proposition assigned to it:
- if $\mathtt{P}$ has been assigned a proposition, then
  - $\upnu(\mathtt{P})=\top$ if that proposition is true,
  - $\upnu(\mathtt{P})=\bot$ if that proposition is false. 

The valuation of **compound** propositional forms is then computed using truth tables. 
## Checklist
- Every component sentence got a single sentence letter (consistent use).
- Parentheses reflect the intended scope.
- The result is a wff (PL-formula).