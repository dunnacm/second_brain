---
down:
  - "[[Assignment (PL)]]"
  - "[[Alphabet + Proposition]]"
  - "[[Assignment (FOL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition

A **proposition** is the **meaning** expressed by a declarative sentence that is either **true** or **false**.  
In introductory logic, one often speaks more loosely and says that a **propositional sentence** is a sentence that is either true or false.

So:

- a **proposition** is **semantic**;
- a **propositional form** is **syntactic**.

A **propositional form** (a **PL-formula**) is a well-formed formula of propositional logic, built from propositional variables, connectives, and grouping symbols.

A proposition may be expressed in ordinary English or in mathematical prose, and then **symbolized** (or **formalized**) in a chosen logical language.

- In **propositional logic (PL)**, the resulting syntactic object is a **propositional form**.
- In **first-order logic (FOL)**, the resulting syntactic object is a **formula** (and, when it has no free variables, a **sentence**).

## Example (a proposition)

“If squares are rectangles, then squares are quadrilaterals.”

## Symbolization (proposition $\to$ propositional form)

To symbolize the proposition, choose propositional variables for its component propositions:

- Let $\mathtt{P}$ := “Squares are rectangles.”
- Let $\mathtt{Q}$ := “Squares are quadrilaterals.”

Then the proposition is represented in propositional logic by
$$
\mathtt{P}\to \mathtt{Q}.
$$

## Assignment vs symbolization

These should be kept distinct:

- **Symbolization / formalization**: translating ordinary-language mathematical content into a logical formula.
- **Assignment**: stipulating what a symbol stands for.

So in $\mathtt{P}$ := “Squares are rectangles.”
the symbol $\mathtt{P}$ has been **assigned** that proposition.

## Truth values

A **proposition** has a truth value.  
A **propositional form** does **not** have a truth value by itself.

A propositional form receives a truth value only after its propositional variables have been associated with propositions and a valuation has been fixed.

More precisely, a valuation starts on propositional variables:
$$
\upnu:\mathtt{PropVar}\to\{\mathtt{T},\mathtt{F}\},
$$
and then extends recursively to all propositional forms by the truth-table rules for
$\neg,\land,\lor,\to,\leftrightarrow$.

So the conceptual order is:

$$
\text{proposition} \;\to\; \text{symbolization} \;\to\; \text{assignment of atoms} \;\to\; \text{valuation}.
$$