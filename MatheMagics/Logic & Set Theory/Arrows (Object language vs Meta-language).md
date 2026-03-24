---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Introduction

The symbols `→`, `↔`, `⇒`, and `⇔` do **not** all belong to the same level.

There are two levels to distinguish:

1. **Object language** (`→` and `↔`)
   These are connectives that occur **inside propositional forms**. correspond to **object-language connectives**; use **inside formulas**

2. **Meta-language** (`⇒` and `⇔`)
   These are symbols used **outside propositional forms** to describe implication, equivalence, inference, or rewrite at the level of explanation, derivation, or semantics. correspond to **meta-level implication/equivalence symbols**; use in replacement rules

## The four symbols
### Object language:

#### 1. Conditional connective / Material implication $\rightarrow$ 

This is the **conditional connective**.

So

$$
\mathtt{p}\to\mathtt{q}
$$

is itself a **propositional form**.

#### 2. Biconditional connective / Material equivalence $\leftrightarrow$ 

This is the **biconditional connective**.

So

$$
\mathtt{p}\leftrightarrow\mathtt{q}
$$

is itself a **propositional form**.
### Meta-language

#### 3. Inference rule $\Rightarrow$

This is a **meta-level implication symbol**.

It is not usually treated as a connective inside a propositional form.  
Instead, it is used when an inference rule is applied

##### Example
$$
\upnu(\mathtt{p}\to\mathtt{q})=\mathtt{F}
\quad \Rightarrow \quad
\upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F}.
$$

Here, the symbol `⇒` is not part of the propositional form.  
It connects one statement **about** the form to another.

#### 4. Replacement rule / Equivalence $\Leftrightarrow$ 

This is a **meta-level equivalence symbol**.

It is not usually treated as a connective inside a propositional form.  
Instead, it is used to state that two meta-level statements are equivalent, or that one line in a derivation is equivalent to another after applying a replacement rule.

##### Example
$$
\upnu(\mathtt{p}\to\mathtt{q})=\mathtt{F}
\quad \Leftrightarrow \quad
\upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F}.
$$

Again, the symbol `⇔` is not part of the propositional form itself.  
It is a statement **about** truth conditions.

