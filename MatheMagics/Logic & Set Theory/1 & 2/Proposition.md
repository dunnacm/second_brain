---
down:
  - "[[Assignment (PL)]]"
  - "[[Alphabet + Proposition]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition

A **propositional sentence** (a **proposition**) is a declarative statement that is either **true** or **false**.

A **proposition** is a **semantic** object. One then commences the process of transfiguring this meaning-bearing declarative statement (in informal English or math prose) into a **well-formed formula** of a chosen logical language (PL or FOL). This process is called **Assignment**, **Symbolization** or **Formalization** ; symbolic logic uses formulas to represent propositions.

A **propositional form** (PL-formula) is **syntactic** (a string in the formal symbolic logic language).

### Example (a proposition)
- “If squares are rectangles, then squares are quadrilaterals.”

## Symbolization (proposition → propositional form)
To symbolize a proposition, choose propositional variables to stand for its component sentences:

- Let $\mathtt{P}$ := “Squares are rectangles.”
- Let $\mathtt{Q}$ := “Squares are quadrilaterals.”

Then the proposition above is represented by the propositional form
$$
\mathtt{P}\to \mathtt{Q}.
$$

## Truth assignment
A valuation assigns truth values to propositional variables:
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}.
$$
Given $\upnu$, the truth value of the whole propositional form is determined by the truth tables for the connectives.