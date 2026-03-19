---
aliases:
down:
  - "[[Constituent parts (material implication)]]"
  - "[[Verbalizations (material implication)]]"
  - "[[Material implication + Logical Implication]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:

Implications sometimes presents **causation**:  
(if p, then q) ⇔ (p → q, i.e., p implies/entails q)

In mathematics, the expression A → B means: it is not the case that p is true but q is false. This understanding of the conditional is known as material implication.  
A (**antecedent**) → B (**consequent**) ⇔ $\lnot(A \land \lnot B)$ ⇔ $\lnot A\lor B$.

### Implication vs Material implication
An **implication** is the *semantic* claim that a conditional holds:  
“if $p$, then $q$”.
In symbolic logic, the expression $p\to q$ is defined truth-functionally. Here, **Material Implication** is the connective "$\to$" itself.

## Truth tables:

- $\mathtt{T}\to\mathtt{T}=\mathtt{T}$
- $\mathtt{T}\to\mathtt{F}=\mathtt{F}$
- $\mathtt{F}\to\mathtt{T}=\mathtt{T}$
- $\mathtt{F}\to\mathtt{F}=\mathtt{T}$
## Right-associativity (parsing convention)  
  
When you see a chain of conditionals with no parentheses, the standard convention is:  **Conditionals associate to the right** (group from the right).  

So, for propositional forms *a, b, c*:  $\mathtt{a}\to\mathtt{b}\to\mathtt{c}$ should be parsed as $\mathtt{a}\to(\mathtt{b}\to\mathtt{c}).$
And for propositional forms *a*, *b*, *c*, *d*: $\mathtt{a} \to \mathtt{b} \to \mathtt{c} \to \mathtt{d} \;\equiv\; \mathtt{a} \to (\mathtt{b} \to (\mathtt{c} \to \mathtt{d})).$
