---
down:
  - "[[Supremum property]]"
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definitions:
### Definition 1:
#### Verbal definition:
Among all ceilings for **S**, the *supremum* **U** is the **lowest** ceiling that still covers **S**: everything in **S** is at or below **U**, and the moment you try any smaller number, it fails because some element of **S** would stick out above it. The set may or may not actually hit **U**.
#### Formal definition:

> [!note]+ **Supremum — $\varepsilon$-form**
> > [!warning]+ **IFF**
> > - $S\subseteq\mathbb{R}\ \wedge\ S\neq\varnothing$
> > - $U=\sup S$
>
> > [!tip]+ **THEN**
> > $$
> > (\forall s\in S)\,[\,s\le U\,]\ \wedge\ (\forall \varepsilon>0)\,(\exists s\in S)\,(U-\varepsilon<s)
> > $$
### Definition 2:
#### Verbal definition:
Among all possible ceilings for **S**, the **supremum** (**sup(S)**) is the **lowest ceiling that still works**. It’s a tight lid: everything in **S** is at or below it, and if you try to lower the lid even a tiny bit, it would fail (something in **S** would poke above). The set may or may not actually touch that lid; the supremum can be a genuine element (a maximum) or just a boundary value the set approaches.
#### Formal definition:
> [!note]+ **Supremum — “no smaller upper bound” form**
> > [!warning]+ **IFF**
> > - $S\subseteq\mathbb{R}\ \wedge\ S\neq\varnothing$
> > - $U=\sup S$
>
> > [!tip]+ **THEN**
> > $$
> > (\forall s\in S)\,[\,s\le U\,]\ \wedge\ (\forall v\in\mathbb{R})\,(\,v<U\ \Rightarrow\ \exists s\in S\,[\,v<s\,]\,)
> > $$