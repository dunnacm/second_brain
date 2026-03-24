---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## From formulas to truth in a structure (FOL)

### Big picture

In first-order logic, the process moves through these stages:

$$
\text{ordinary-language statement}
\;\longrightarrow\;
\text{symbolization}
\;\longrightarrow\;
\text{choice of structure}
\;\longrightarrow\;
\text{assignment of free variables}
\;\longrightarrow\;
\text{satisfaction / truth}.
$$

Unlike propositional logic, first-order logic usually needs **more semantic setup** before truth can be evaluated.

## Steps:
### 0. Statement

Start with an ordinary-language or mathematical statement.

#### Example
“Every real number has a square that is nonnegative.”

This is a declarative statement, so it is truth-apt.

### 1. Symbolization

Translate the statement into a first-order formula.

#### Example
$$
\forall \mathtt{x}\,\exists \mathtt{y}\,\bigl(\mathtt{y}=\mathtt{x}^2\land \mathtt{y}\ge 0\bigr).
$$

This step is called **symbolization** or **formalization**.

#### What symbolization does
It turns the original meaning-bearing statement into a **first-order formula**.

### 2. Choice of structure

To evaluate a first-order formula, we must specify a **structure**.

A structure provides:
- a **domain** of objects,
- meanings for the nonlogical symbols.

#### Example
For the formula above, take the standard structure on the real numbers:
- domain: $\mathbb{R}$
- the symbols $0,1,+,\cdot,\ge$ have their usual meanings.

This step is called choosing a **structure**.

#### What the structure does
It tells us what the language is **about** and what its nonlogical symbols **mean**.

### 3. Assignment of free variables

If the formula contains **free variables**, we must also specify which objects they denote.

An **assignment** in FOL is a function
$$
\mathtt{s}:\mathtt{VAR}\to A,
$$
where $A$ is the domain of the chosen structure.

So:
- each variable gets assigned an object of the domain;
- this allows terms and open formulas to be evaluated.

This step is called **assignment (FOL)**.

#### What assignment does
It tells us what the **free variables** stand for **right now**.

### 4. Satisfaction / truth

Once the structure and assignment have been fixed, we can ask whether the formula is **true** in that setup.

This is written using the satisfaction symbol:
$$
\mathfrak{A}\vDash \varphi[\mathtt{s}].
$$

It reads:
- “$\varphi$ is satisfied in the structure $\mathfrak{A}$ under the assignment $\mathtt{s}$,”
- or informally, “$\varphi$ is true in $\mathfrak{A}$ under $\mathtt{s}$.”

If the formula is a **sentence** (that is, it has no free variables), then no separate assignment is needed in any essential way.

## Worked examples
### Example 1

#### Informal statement
“Every real number has a square that is nonnegative.”

#### Step 1: symbolization
$$
\forall \mathtt{x}\,\exists \mathtt{y}\,\bigl(\mathtt{y}=\mathtt{x}^2\land \mathtt{y}\ge 0\bigr)
$$

#### Step 2: choice of structure
Take the standard structure with domain $\mathbb{R}$.

#### Step 3: assignment of free variables
No separate assignment is needed, because the formula is a **sentence**.

#### Step 4: satisfaction / truth
$$
\mathbb{R}\vDash \forall \mathtt{x}\,\exists \mathtt{y}\,\bigl(\mathtt{y}=\mathtt{x}^2\land \mathtt{y}\ge 0\bigr)
$$

This is true in the standard real-number structure.

### Example 2

#### Open formula
$$
\mathtt{x}<\mathtt{y}
$$

This is **not** a sentence, because $\mathtt{x}$ and $\mathtt{y}$ are free.

#### Step 1: choice of structure
Take the standard structure with domain $\mathbb{R}$.

#### Step 2: assignment of free variables
Choose an assignment $\mathtt{s}$ such that
$$
\mathtt{s}(\mathtt{x})=2,\qquad \mathtt{s}(\mathtt{y})=5.
$$

#### Step 3: satisfaction / truth
Then
$$
\mathbb{R}\vDash (\mathtt{x}<\mathtt{y})[\mathtt{s}]
$$
because $2<5$.

But if $\mathtt{t}$ is another assignment with
$$
\mathtt{t}(\mathtt{x})=7,\qquad \mathtt{t}(\mathtt{y})=1,
$$
then
$$
\mathbb{R}\not\vDash (\mathtt{x}<\mathtt{y})[\mathtt{t}],
$$
because $7<1$ is false.

## Comparison with PL

### In propositional logic
$$
\text{assignment of atoms}
\;\longrightarrow\;
\text{truth valuation } \upnu
$$

### In first-order logic
$$
\text{structure}
\;+\;
\text{assignment of free variables}
\;\longrightarrow\;
\text{satisfaction / truth}
$$

So the first-order case is the richer analogue of the propositional case.

## Final summary

The clean conceptual order is:

$$
\text{ordinary-language statement}
\;\longrightarrow\;
\text{symbolization into an FOL-formula}
\;\longrightarrow\;
\text{choice of structure}
\;\longrightarrow\;
\text{assignment of free variables}
\;\longrightarrow\;
\text{satisfaction / truth in that structure}.
$$

So:

- **symbolization** builds the formula,
- **the structure** gives meaning to the nonlogical symbols,
- **the assignment** gives values to free variables,
- **satisfaction** tells you whether the formula is true in that setup.