---
down:
  - "[[Outcomes (truth valuations)]]"
  - "[[Limitations (truth valuations)]]"
  - "[[Proposition]]"
  - "[[Truth tables]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea
### Introduction:
A **proposition** has a truth value.  
A **propositional form** does **not** have a truth value by itself, because a propositional form is only a **syntactic pattern**, a purely syntactic object.  
It can represent many different propositions, depending on what propositions are assigned to its propositional variables.

So the semantic process has **two stages**:

1. **Assignment of atoms**  
   Associate propositional variables with propositions.

2. **Truth valuation**  
   Once that assignment has been fixed, apply a valuation to determine whether the resulting propositional form is true or false.
### Importance (summarized)
Truth valuations are necessary because one needs a mechanism that would give propositional variables truth values, since only propositions do. A truth valuation, then, assigns truth values to propositional variables ($\upnu:\mathtt{PropVar}\to{\mathtt{T},\mathtt{F}}$). One can then extend this mechanism from **atomic propositional forms** to **compound propositional forms** through the truth tables, thereby making it possible to determine the truth value of the whole form.
#### Example:
If $\mathtt{P}$ is assigned the proposition $2+3=5$ ($\mathtt{P} := 2+3=5$), then $\mathtt{P}$ stands for a true proposition, and so $\upnu(\mathtt{P})=\mathtt{T}$.

Thus, $\upnu$ does not make $\mathtt{P}$ true; rather, once an assignment has fixed what $\mathtt{P}$ stands for, $\upnu$ gives its truth value.

If no proposition has been assigned to $\mathtt{P}$, then in propositional semantics one may define $\upnu(\mathtt{P})$ arbitrarily as either $\mathtt{T}$ or $\mathtt{F}$.

## Cases:

### Base case: *atomic propositional forms*

If $\mathtt{P}$ has been assigned a proposition, then
$$
\upnu(\mathtt{P})=
\begin{cases}
\mathtt{T} & \text{if } \mathtt{P} \text{ is true},\\[6pt]
\mathtt{F} & \text{if } \mathtt{P} \text{ is false}.
\end{cases}
$$

Thus:

- if $\mathtt{P}$ stands for a true proposition, then $\upnu(\mathtt{P})=\mathtt{T}$;
- if $\mathtt{P}$ stands for a false proposition, then $\upnu(\mathtt{P})=\mathtt{F}$.
### Recursive clauses for *compound propositional forms*

Let $\mathtt{p}$ and $\mathtt{q}$ be propositional forms.

#### Negation

##### Valuation form
$$
\upnu(\neg \mathtt{p})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{F},\\[6pt]
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{T}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\neg \mathtt{p})$ |
|---|---|
| $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ |

#### Conjunction

##### Valuation form
$$
\upnu(\mathtt{p}\land \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{T},\\[6pt]
\mathtt{F} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\land \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |

#### (Logical) Disjunction (Inclusive or)

##### Valuation form
$$
\upnu(\mathtt{p}\lor \mathtt{q})=
\begin{cases}
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{F}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]
\mathtt{T} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\lor \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |

#### Implication

##### Valuation form
$$
\upnu(\mathtt{p}\to \mathtt{q})=
\begin{cases}
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]
\mathtt{T} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\to \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ |

#### Biconditional

##### Valuation form
$$
\upnu(\mathtt{p}\leftrightarrow \mathtt{q})=
\begin{cases}
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\upnu(\mathtt{q}),\\[6pt]
\mathtt{F} & \text{otherwise}.
\end{cases}
$$

##### Truth table form

| $\upnu(\mathtt{p})$ | $\upnu(\mathtt{q})$ | $\upnu(\mathtt{p}\leftrightarrow \mathtt{q})$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ |
## Algorithmic steps:
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

