---
down:
  - "[[Free variables (FVs)]]"
  - "[[Bound variables]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:

> [!important]+ **Preconditions**
> > - Let **S** be *theory symbols*.
> > - Let $t_0,\, t_1,\, \ldots,\, t_{n-1}$ be **S-terms**.
> > - Let $R$ be an $n$-ary relation symbol from **S**.
> > - Let $p$ and $q$ be **S-formulas**.
>
> An **occurrence** of a variable in a formula is **free** or not free only according to the following rules:

> [!note]+ **Rule 1 (Atomic formulas)**
> > [!warning]+ **IF**
> > There is a variable occurrence in
> >   - $t_0=t_1$, or
> >   - $R(t_0, t_1, \ldots, t_{n-1})$.
>
> > [!tip]+ **THEN**
> > The variable occurrence is **free**.
>
> > [!example]+ **Example**
> > In $x=y$, both $x$ and $y$ are free.

> [!note]+ **Rule 2 (Connectives)**
> > [!warning]+ **IFF**
> > The occurrence in $p$ or $q$ is free in
> >  - $\lnot p$, or
> >  - $p\land q$, or
> >  - $p\lor q$, or
> >  - $p\to q$, or
> >  - $p\leftrightarrow q$.
>
> > [!tip]+ **THEN**
> > The variable occurrence is **free**.
>
> > [!example]+ **Example**
> > In $(x>0)\land(y>0)$, the occurrences of $x$ and $y$ are free if they were free in $x>0$ and $y>0$.

> [!note]+ **Rule 3 (Bound variable of a quantifier)**
> > [!warning]+ **IF**
> > There is an occurrence of $x$ in
> >  - $\forall x\,p$, or
> >  - $\exists x\,p$.
>
> > [!tip]+ **THEN**
> > That occurrence of $x$ is **bound**.
>
> > [!example]+ **Example**
> > In $\forall x\,(x>0)$, $x$ is bound.

> [!note]+ **Rule 4 (Binding within scope)**
> > [!warning]+ **IF**
> > A formula has the form $\forall x\,p$ or $\exists x\,p$.
>
> > [!tip]+ **THEN**
> > Every occurrence of $x$ **within $p$** is **bound** (by that quantifier).
>
> > [!example]+ **Example**
> > In $\exists x\,(P(x)\land Q(x))$, both occurrences of $x$ are bound by $\exists x$.

> [!note]+ **Rule 5 (Other variables under quantifiers)**
> > [!warning]+ **IFF**
> > - The occurrence of $y$ is free in $P$.
> > - $x\neq y$.
>
> > [!tip]+ **THEN**
> > The occurrence of $y$ is free in
> >  - $\forall x\,P$, and
> >  - $\exists x\,P$.
>
> > [!example]+ **Example**
> > In $\forall x\,(y>x)$, $y$ is free (since $y\neq x$).

## Examples:
$$
\begin{aligned}
 & \forall x \exists y \; (x = y \;\lor\; f(x) = y) \;\to\; R(x,y,z) \\[3pt]
 & \qquad \text{All occurrences of $x$ and $y$ are } \textbf{bound} \\[3pt]
 & \qquad \text{The occurrence of $z$ is } \textbf{free} \\[12pt]

 & \exists y \; (x = y \;\lor\; f(x) = y) \;\to\; R(x,y,z) \\[3pt]
 & \qquad \text{All occurrences of $y$ are } \textbf{bound} \\[3pt]
 & \qquad \text{The occurrences of $x$ and $z$ are } \textbf{free} \\[12pt]

 & (x = y \;\lor\; f(x) = y) \;\to\; R(x,y,z) \\[3pt]
 & \qquad \text{All occurrences of $x, y,$ and $z$ are } \textbf{free}
\end{aligned}
$$
$$
\text{In } P(x) \lor Q(y), \text{ the occurrence of } x \text{ in } P(x) \text{ is free, and the occurrence of } y \text{ in } Q(y) \text{ is free.}
$$
