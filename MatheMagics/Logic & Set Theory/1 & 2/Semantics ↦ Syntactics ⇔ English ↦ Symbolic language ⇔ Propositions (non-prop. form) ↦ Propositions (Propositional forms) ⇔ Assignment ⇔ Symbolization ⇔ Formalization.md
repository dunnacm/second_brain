---
down:
  - "[[Assignment (PL)]]"
  - "[[Assignment (FOL)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Goal
**Symbolization** (also called **formalization**) is the process of turning a meaning-bearing declarative statement (in informal English or math prose) into a **well-formed formula** of a chosen logical language (PL or FOL).

- Input: a **proposition** (semantic object; truth-apt meaning).
- Output: a **formula** (syntactic object; a well-formed string in the language).
## Steps

### Preemptive: Fix the language (alphabet + grammar)
Before symbolizing anything, fix the **alphabet** and **formation rules** of your language.

- **PL (propositional logic):** propositional variables + connectives + grouping.
- **FOL (first-order logic):** logic symbols (variables, connectives, quantifiers, equality, grouping) **plus** a chosen set of **theory symbols** (constants, function symbols, relation symbols).

Your formalization must use only symbols from the chosen alphabet and must satisfy the grammar for terms/formulas.

### Symbolization in PL (semantic → PL-formula) OR
#### Procedure
1) Identify the component declarative sentences in the English statement.  
2) Assign propositional variables to them (sentence letters).  
3) Rebuild the structure using connectives and parentheses.

##### Example (PL)
Proposition: “If squares are rectangles, then squares are quadrilaterals.”
- Let $\mathtt{P}$ := “Squares are rectangles.”
- Let $\mathtt{Q}$ := “Squares are quadrilaterals.”
- Symbolization: $$\mathtt{P}\to\mathtt{Q}.$$
#### Semantics reminder (PL)
A valuation
$$
\upnu:\mathtt{PropVar}\to\{\top,\bot\}
$$
assigns truth values to propositional variables, and the truth tables determine $\upnu(\varphi)$ for any PL-formula $\varphi$.

### Symbolization in FOL (semantic → S-formula / S-sentence)
#### Procedure
1) **Choose a domain of discourse** (what “objects” you are talking about).  
2) Choose theory symbols to match the subject matter:
	- predicates/relations (properties and relations),
	- function symbols (operations),
	- constants (named objects).
3) Decide which words/phrases should be represented as:
	- **terms** (object-denoting expressions),
	- **atomic formulas** (predicate applied to terms, or equality),
	- then build larger formulas with connectives and quantifiers.
4) Make quantifier **scope** explicit; rename bound variables when needed to avoid confusion.

##### Example (FOL: universal statement)
Informal: “Every real number has a square that is nonnegative.”
One possible formalization (with domain $\mathbb{R}$ implicit):
$$
\forall x\,\exists y\,(y=x^2\land y\ge 0).
$$

##### Example (FOL: uniqueness pattern)
Informal: “There exists exactly one $x$ such that $P(x)$.”
A standard formalization:
$$
\exists x\,\Big(P(x)\land \forall y\,(P(y)\to y=x)\Big).
$$

#### Semantics reminder (FOL)
Truth is evaluated in a structure $\mathcal{M}$ (domain + meanings for theory symbols).  
Open formulas may also require an assignment $s:\mathtt{VAR}\to D$, while sentences (closed formulas) have truth values in $\mathcal{M}$ independent of $s$.

## Good practice checkpoints
- **Wff check:** the output must be a well-formed formula in the chosen language.
- **Scope check:** parentheses and quantifier scope are unambiguous.
- **Free/bound check:** know which variables are free vs bound; if your target is a statement, aim for a **sentence** (closed formula).
- **Vocabulary check:** PL cannot express quantifiers; FOL cannot treat “if…then…” as a function unless your language explicitly includes such a symbol.
- **Non-uniqueness:** symbolization is often not unique; different formalizations can express the same idea, but they may differ in strength.