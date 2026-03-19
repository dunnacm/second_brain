---
down:
  - "[[Infimum property]]"
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definitions:
### Definition 1:
#### Verbal definition:
The *infimum* **ℓ** of **S** is the exact lower frontier of the set: (1) every element of **S** is at or above **L**, and (2) no matter how tightly you zoom just **above** **L**, you can always find a point of **S** inside that tiny window—so points of **S** can approach **L** from above as closely as you like.
#### Formal definition:

> [!note]+ **Infimum — $\varepsilon$-form**
> > [!warning]+ **IFF**
> > - $S\subseteq\mathbb{R}\ \wedge\ S\neq\varnothing$
> > - $L=\inf S$
>
> > [!tip]+ **THEN**
> > $$
> > (\forall s\in S)\,[\,L\le s\,]\ \wedge\ (\forall \varepsilon>0)\,(\exists s\in S)\,[\,s<L+\varepsilon\,]
> > $$


### Definition 2:
#### Verbal definition:
Among all floors for **S**, the *infimum* **L** is the **highest** floor that still lies below (or at) every element of **S**. Everything in **S** is ≥ **L**, and if you try any number **v** larger than **L** as a floor, it fails—some element of **S** sits below **v**. The set may or may not actually contain **L**.
#### Formal definition:

> [!note]+ **Infimum — “no greater lower bound” form**
> > [!warning]+ **IFF**
> > - $S\subseteq\mathbb{R}\ \wedge\ S\neq\varnothing$
> > - $L=\inf S$
>
> > [!tip]+ **THEN**
> > $$
> > (\forall s\in S)\,[\,L\le s\,]\ \wedge\ (\forall v\in\mathbb{R})\,(\,L<v\ \Rightarrow\ \exists s\in S\,[\,s<v\,]\,)
> > $$






