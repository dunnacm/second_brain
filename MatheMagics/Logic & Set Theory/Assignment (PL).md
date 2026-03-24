---
down:
  - "[[Propositional form or ((wffs) or (PL-formula))]]"
  - "[[Assignment operator (≔)]]"
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
## From propositions to truth valuation (PL)

### Big picture

In propositional logic, the process moves through these stages:

$$
\text{proposition(s)} \;\longrightarrow\; \text{assignment of atoms} \;\longrightarrow\; \text{symbolization} \;\longrightarrow\; \text{truth valuation}.
$$
## Steps:
### 0. Proposition(s)

Start with an ordinary-language or mathematical statement that expresses a proposition.

#### Example
“If squares are rectangles, then squares are quadrilaterals.”

This is a proposition because it is a declarative statement and is either true or false.

### 1. Assignment of atoms

Break the proposition into its component propositions and assign a propositional variable to each one.

#### Example
$$
\begin{aligned}
\mathtt{P}\;:=\;& \text{``Squares are rectangles''},\\[6pt]
\mathtt{Q}\;:=\;& \text{``Squares are quadrilaterals''}.
\end{aligned}
$$

This step is called **assignment (PL)**.

#### What assignment does
It tells us what the sentence letters stand for.

### 2. Symbolization

Now rebuild the logical structure using connectives.

#### Example
The original proposition

> “If squares are rectangles, then squares are quadrilaterals.”

is symbolized as

$$
\mathtt{P}\to \mathtt{Q}.
$$

This step is called **symbolization** or **formalization**.

#### What symbolization does
It turns the original meaning-bearing statement into a **propositional form**.

### 3. Truth valuation

Once the propositional variables have been assigned propositions, a truth valuation can be applied.

A valuation begins on propositional variables:
$$
\upnu:\mathtt{PropVar}\to\{\mathtt{T},\mathtt{F}\}.
$$

For example:
$$
\upnu(\mathtt{P})=
\begin{cases}
\mathtt{T} & \text{if the proposition assigned to } \mathtt{P} \text{ is true},\\[6pt]
\mathtt{F} & \text{if the proposition assigned to } \mathtt{P} \text{ is false}.
\end{cases}
$$

The valuation then extends to compound propositional forms by the truth tables.

#### Example
If
$$
\upnu(\mathtt{P})=\mathtt{T}
\qquad\text{and}\qquad
\upnu(\mathtt{Q})=\mathtt{T},
$$
then
$$
\upnu(\mathtt{P}\to \mathtt{Q})=\mathtt{T}.
$$

If instead
$$
\upnu(\mathtt{P})=\mathtt{T}
\qquad\text{and}\qquad
\upnu(\mathtt{Q})=\mathtt{F},
$$
then
$$
\upnu(\mathtt{P}\to \mathtt{Q})=\mathtt{F}.
$$

## Worked examples
### Example 1

#### Informal proposition
“If the sine function is not one-to-one, then the absolute value function is not onto.”

#### Step 1: assignment of atoms
$$
\begin{aligned}
\mathtt{P}\;:=\;& \text{``The sine function is not one-to-one''},\\[6pt]
\mathtt{Q}\;:=\;& \text{``The absolute value function is not onto''}.
\end{aligned}
$$

#### Step 2: symbolization
$$
\mathtt{P}\to \mathtt{Q}
$$

#### Step 3: truth valuation
Suppose:
$$
\upnu(\mathtt{P})=\mathtt{T},\qquad \upnu(\mathtt{Q})=\mathtt{F}.
$$

Then:
$$
\upnu(\mathtt{P}\to \mathtt{Q})=\mathtt{F}.
$$

### Example 2

#### Informal proposition
“The sine function is not one-to-one and the square root function is one-to-one.”

#### Step 1: assignment of atoms
$$
\begin{aligned}
\mathtt{P}\;:=\;& \text{``The sine function is not one-to-one''},\\[6pt]
\mathtt{Q}\;:=\;& \text{``The square root function is one-to-one''}.
\end{aligned}
$$

#### Step 2: symbolization
$$
\mathtt{P}\land \mathtt{Q}
$$

#### Step 3: truth valuation
If
$$
\upnu(\mathtt{P})=\mathtt{T},\qquad \upnu(\mathtt{Q})=\mathtt{T},
$$
then
$$
\upnu(\mathtt{P}\land \mathtt{Q})=\mathtt{T}.
$$

If
$$
\upnu(\mathtt{P})=\mathtt{T},\qquad \upnu(\mathtt{Q})=\mathtt{F},
$$
then
$$
\upnu(\mathtt{P}\land \mathtt{Q})=\mathtt{F}.
$$

## Final summary

The clean conceptual order is:

$$
\text{ordinary-language proposition}
\;\longrightarrow\;
\text{assignment of component propositions to variables}
\;\longrightarrow\;
\text{symbolization into a propositional form}
\;\longrightarrow\;
\text{truth valuation of that propositional form}.
$$

So:

- **assignment** tells you what the atoms mean,
- **symbolization** builds the formula,
- **truth valuation** tells you whether the formula is true or false.