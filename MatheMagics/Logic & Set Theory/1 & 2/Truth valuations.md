---
down:
  - "[[Outcomes (truth valuations)]]"
  - "[[Limitations (truth valuations)]]"
  - "[[Proposition]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea

A **proposition** has a truth value.  
A **propositional form** does **not** have a truth value by itself.

Why not? Because a propositional form is only a **syntactic pattern**.  
It can represent many different propositions, depending on what propositions are assigned to its propositional variables.

So the semantic process has **two stages**:

1. **Assignment of atoms**  
   Associate propositional variables with propositions.

2. **Truth valuation**  
   Once that assignment has been fixed, apply a valuation to determine whether the resulting propositional form is true or false.
## Procedure:

### Stage 1: assignment of atoms

Examples of assignments:
$$
\begin{aligned}
\mathtt{P}\;:=\;& \text{The sine function is not one-to-one}.\\[12pt]
\mathtt{Q}\;:=\;& \text{The square root function is one-to-one}.\\[12pt]
\mathtt{R}\;:=\;& \text{The absolute value function is not onto}.
\end{aligned}
$$

At this stage, the symbols $\mathtt{P},\mathtt{Q},\mathtt{R}$ have been tied to definite propositions.

### Stage 2: truth valuation

A **truth valuation** is a rule
$$
\upnu:\{\text{propositional forms}\}\to \{\mathtt{T},\mathtt{F}\}.
$$

It assigns a truth value to a propositional form **relative to the chosen assignment of its propositional variables**.

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
$$  
\upnu(\neg \mathtt{p})=  
\begin{cases}  
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{F},\\[6pt]  
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{T}.  
\end{cases}  
$$  
  
#### Conjunction  
$$  
\upnu(\mathtt{p}\land \mathtt{q})=  
\begin{cases}  
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{T},\\[6pt]  
\mathtt{F} & \text{otherwise}.  
\end{cases}  
$$  
  
#### Disjunction  
$$  
\upnu(\mathtt{p}\lor \mathtt{q})=  
\begin{cases}  
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{F}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]  
\mathtt{T} & \text{otherwise}.  
\end{cases}  
$$  
  
#### Implication  
$$  
\upnu(\mathtt{p}\to \mathtt{q})=  
\begin{cases}  
\mathtt{F} & \text{if } \upnu(\mathtt{p})=\mathtt{T}\ \text{and}\ \upnu(\mathtt{q})=\mathtt{F},\\[6pt]  
\mathtt{T} & \text{otherwise}.  
\end{cases}  
$$  
  
#### Biconditional  
$$  
\upnu(\mathtt{p}\leftrightarrow \mathtt{q})=  
\begin{cases}  
\mathtt{T} & \text{if } \upnu(\mathtt{p})=\upnu(\mathtt{q}),\\[6pt]  
\mathtt{F} & \text{otherwise}.  
\end{cases}  
$$

## Algorithm: Why truth tables appear here

Truth tables are the **algorithmic display** of the recursive valuation rules.

They do not create meaning from nothing.  
They compute the truth value of a compound propositional form **after** the atomic propositions have been assigned and valued.

So the conceptual order is:

$$
\text{proposition} \;\to\; \text{symbolization} \;\to\; \text{assignment of atoms} \;\to\; \text{valuation}.
$$

### A useful slogan

A propositional form is **syntax**.  
A valuation is **semantics**.

Or more fully:

$$
\text{syntax first, semantics second.}
$$

You first write the propositional form.  
You then assign its atoms to propositions.  
Only then do you evaluate its truth value by $\upnu$.