---
aliases:
down:
  - "[[Constituent parts (material implication)]]"
  - "[[Verbalizations (material implication)]]"
  - "[[Material implication + Logical Implication]]"
  - "[[Notation (object language)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:

In ordinary language, a conditional sometimes suggests **causation**:  
(if $\mathtt{p}$, then $\mathtt{q}$) $\Leftrightarrow$ ($\mathtt{p}\to \mathtt{q}$)

In mathematics, the expression $A\to B$ means: it is not the case that $A$ is true but $B$ is false. This understanding of the conditional is known as **material implication**.  
$A$ (**antecedent**) $\to$ $B$ (**consequent**) $\Leftrightarrow \lnot(A \land \lnot B) \Leftrightarrow \lnot A\lor B$.

### Implication vs Material implication
An **implication** is the *semantic* claim that a conditional holds:  
“if $\mathtt{p}$, then $\mathtt{q}$.”

In symbolic logic, the expression $\mathtt{p}\to \mathtt{q}$ is defined truth-functionally. Here, **material implication** is the connective `$\to$` itself.

Let $\mathtt{p}$ and $\mathtt{q}$ be propositional forms.

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

## Right-associativity (parsing convention)  
  
When you see a chain of conditionals with no parentheses, the standard convention is:  **Conditionals associate to the right** (group from the right).  

So, for propositional forms *a, b, c*:  $\mathtt{a}\to\mathtt{b}\to\mathtt{c}$ should be parsed as $\mathtt{a}\to(\mathtt{b}\to\mathtt{c}).$
And for propositional forms *a*, *b*, *c*, *d*: $\mathtt{a} \to \mathtt{b} \to \mathtt{c} \to \mathtt{d} \;\equiv\; \mathtt{a} \to (\mathtt{b} \to (\mathtt{c} \to \mathtt{d})).$
