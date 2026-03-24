---
down:
  - "[[Examples (truth tables)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:

So a truth table is a **tabular presentation of truth valuation** for propositional forms.

Truth tables are important because they make the valuation of compound propositional forms explicit and systematic.
Truth tables provide a mechanical procedure for evaluating propositional forms and for comparing their truth conditions.

## Relation to truth valuation:

A truth valuation begins with propositional variables:
$$
\upnu:\mathtt{PropVar}\to\{\mathtt{T},\mathtt{F}\}.
$$

The valuation is then extended from atomic propositional forms to compound propositional forms by the recursive clauses for the connectives.

A truth table is the tabular display of that extension.

So:

- **truth valuation** gives the semantic rule;
- **truth table** displays the results of applying that rule in all possible cases.

## Standard truth tables for the connectives
[[Truth valuations#Recursive clauses for compound propositional forms|Recursive Clauses]]

## Number of rows in a truth table

### Case 1: one propositional form

Let $\mathtt{P}_1$ be a propositional form. To find the number of rows:

$$
\upnu(\mathtt{P}_1)=\mathtt{T}\ \text{or}\ \mathtt{F}.
$$

Therefore, the truth table has $2$ rows.

| $\upnu(\mathtt{P}_1)$ |
|---|
| $\mathtt{T}$ |
| $\mathtt{F}$ |

### Case 2: two propositional forms

Let $\mathtt{P}_1$ and $\mathtt{P}_2$ be propositional forms. To find the number of rows:

$$
\upnu(\mathtt{P}_1)\ \text{and}\ \upnu(\mathtt{P}_2),
\quad \text{each of which can be } \mathtt{T}\ \text{or}\ \mathtt{F}.
$$

Hence, $2\cdot 2=4.$

| $\upnu(\mathtt{P}_1)$ | $\upnu(\mathtt{P}_2)$ |
|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ |

Column 2 is obtained by writing the one-variable case twice.

### Case 3: three propositional forms

Let $\mathtt{P}_1,\mathtt{P}_2,$ and $\mathtt{P}_3$ be propositional forms.

$$
\upnu(\mathtt{P}_1),\ \upnu(\mathtt{P}_2),\ \text{and}\ \upnu(\mathtt{P}_3),
\quad \text{each of which can be } \mathtt{T}\ \text{or}\ \mathtt{F}.
$$

Hence, $2\cdot 2\cdot 2=8.$

| $\upnu(\mathtt{P}_1)$ | $\upnu(\mathtt{P}_2)$ | $\upnu(\mathtt{P}_3)$ |
|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |

Column 2 is obtained by writing Column 1 of the two-variable case twice.  
Column 3 is obtained by writing Column 2 of the two-variable case twice.

### General case

Let $\mathtt{P}_1,\mathtt{P}_2,\ldots,\mathtt{P}_n$ be propositional forms.

Since each of
$$
\upnu(\mathtt{P}_1),\ \upnu(\mathtt{P}_2),\ \ldots,\ \upnu(\mathtt{P}_n)
$$
can be either $\mathtt{T}$ or $\mathtt{F}$, the number of rows in the truth table is

$$
\underbrace{2\cdot 2\cdots 2}_{n\text{ factors}}=2^n.
$$

So the number of rows is, therefore,

$$
2^n.
$$
## How to construct a truth table
### Algorithmic steps:

### 1. Decompose the propositional form through a parsing tree

Start with the given propositional form and decompose it into its immediate parts by means of a parsing tree.

This shows the logical structure of the form and makes clear which subforms must be evaluated first.

#### Example
For
$$
(\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P}),
$$
its parsing tree displays the two immediate components
$$
\mathtt{P}\leftrightarrow\mathtt{Q}
\qquad\text{and}\qquad
\mathtt{R}\to\mathtt{P},
$$
together with their atomic parts.

![[Pasted image 20260323045654.png|280]]

### 2. Write the formation sequence

List the atomic propositional forms first, and then list the compound propositional forms in the order in which they are built.

This gives the order in which the columns of the truth table should be constructed.

#### Example
For
$$
(\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P}),
$$
the formation sequence is
$$
\mathtt{P},\ \mathtt{Q},\ \mathtt{R},\ \mathtt{P}\leftrightarrow\mathtt{Q},\ \mathtt{R}\to\mathtt{P},\ (\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P}).
$$

### 3. Determine the number of rows

Count the distinct atomic propositional forms occurring in the formation sequence.

If there are $n$ distinct propositional variables, then the truth table must have
$$
2^n
$$
rows.

#### Example
Since
$$
(\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P})
$$
contains the three distinct propositional variables
$$
\mathtt{P},\ \mathtt{Q},\ \mathtt{R},
$$
its truth table must have
$$
2^3=8
$$
rows.

### 4. Evaluate the propositional forms in the formation sequence through truth tables

Construct the truth table by following the formation sequence from left to right.

- First, create columns for the atomic propositional forms.
- Then, using the truth tables for the connectives, compute the value of each compound propositional form from the columns already obtained.
- Continue until the column for the whole propositional form has been completed.

#### Example

| $\upnu(\mathtt{P})$ | $\upnu(\mathtt{Q})$ | $\upnu(\mathtt{R})$ | $\upnu(\mathtt{P}\leftrightarrow\mathtt{Q})$ | $\upnu(\mathtt{R}\to\mathtt{P})$ | $\upnu\bigl((\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P})\bigr)$ |
|---|---|---|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |

## Final summary  
  
A truth table is a complete tabular display of the truth value of a propositional form under every possible truth valuation of its propositional variables.  
  
So the clean conceptual order is:  
  
$$  
\text{propositional form}  
\;\longrightarrow\;  
\text{assignment of truth values to its propositional variables}  
\;\longrightarrow\;  
\text{row-by-row evaluation by truth table}  
\;\longrightarrow\;  
\text{truth value of the whole form}.  
$$  
  
So:  
  
- **truth valuation** assigns truth values to the atoms,  
- **truth tables** display the resulting evaluations systematically,  
- **compound propositional forms** are evaluated column by column from their simpler parts.