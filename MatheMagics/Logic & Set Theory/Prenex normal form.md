---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
> [!note] **Prenex Normal Form (PNF)**
>
> > [!warning] **IF**
> > - $p$ is an $\mathcal{S}$-**formula**.
> > - Variables $x_1,\dots,x_n$ (After $\alpha$-renaming if needed) 
> > - Quantifiers $Q_i\in\{\forall,\exists\}$ such that
> >   $$Q_1 x_1\, Q_2 x_2\, \cdots\, Q_n x_n \;\; \varphi$$
> >   where $\varphi$ has **no quantifiers** (i.e., $\varphi$ is a quantifier-free Boolean combination of atomic formulas).
>
> > [!tip] **THEN**
> > - $p$ is **in prenex normal form** iff it has the above shape:
> >   - the **prefix** is $Q_1 x_1 \cdots Q_n x_n$ (possibly $n=0$),
> >   - the **matrix** is the quantifier-free part $\varphi$.
>
> When converting a formula to PNF, **rename bound variables** (α-conversion) to avoid **variable capture** and to keep the set of **free variables unchanged**.

## Illustrations:
### Example 1:
$$
\begin{aligned}
(1)\quad & \forall x\bigl(P(x)\ \to\ \exists y\,Q(x,y)\bigr) \\
(2)\quad & \forall x\bigl(\neg P(x)\ \lor\ \exists y\,Q(x,y)\bigr) && \text{elim } \to \\
(3)\quad & \forall x\,\exists y\bigl(\neg P(x)\ \lor\ Q(x,y)\bigr) && \text{pull } \exists y \\
\Rightarrow\quad & \forall x\,\exists y\,[\,\neg P(x)\ \lor\ Q(x,y)\,]
\end{aligned}
$$
### Example 2:
$$
\begin{aligned}
(1)\quad & \neg\,\exists x\,\forall y\,R(x,y) \\
(2)\quad & \forall x\,\neg\,\forall y\,R(x,y) && \text{QN} \\
(3)\quad & \forall x\,\exists y\,\neg R(x,y) && \text{QN} \\
\Rightarrow\quad & \forall x\,\exists y\,[\,\neg R(x,y)\,]
\end{aligned}
$$
### Example 3:
$$
\begin{aligned}
(1)\quad & (\exists x\,P(x))\ \to\ \forall y\,Q(y) \\
(2)\quad & \neg\exists x\,P(x)\ \lor\ \forall y\,Q(y) && \text{elim } \to \\
(3)\quad & \forall x\,\neg P(x)\ \lor\ \forall y\,Q(y) && \text{QN} \\
(4)\quad & \forall y\bigl(\forall x\,\neg P(x)\ \lor\ Q(y)\bigr) && y\notin \forall x\,\neg P(x) \\
(5)\quad & \forall y\,\forall x\bigl(\neg P(x)\ \lor\ Q(y)\bigr) && x\notin Q(y) \\
\Rightarrow\quad & \forall x\,\forall y\,[\,\neg P(x)\ \lor\ Q(y)\,]
\end{aligned}
$$
### Example 4:
$$
\begin{aligned}
(1)\quad & \exists x\bigl(P(x)\ \land\ \forall y\,S(y)\bigr) \\
(2)\quad & (\exists x\,P(x))\ \land\ \forall y\,S(y) && x\notin \forall y\,S(y) \\
(3)\quad & \exists x\,\forall y\bigl(P(x)\ \land\ S(y)\bigr) && y\notin P(x),\ x\notin S(y) \\
\Rightarrow\quad & \exists x\,\forall y\,[\,P(x)\ \land\ S(y)\,]
\end{aligned}
$$
### Example 5:
$$
\begin{aligned}
(1)\quad & \forall x\ \neg\,\exists y\bigl(P(y)\ \to\ R(x)\bigr) \\
(2)\quad & \forall x\ \neg\,\exists y\bigl(\neg P(y)\ \lor\ R(x)\bigr) && \text{elim } \to \\
(3)\quad & \forall x\ \forall y\ \neg\bigl(\neg P(y)\ \lor\ R(x)\bigr) && \text{QN} \\
(4)\quad & \forall x\ \forall y\bigl(P(y)\ \land\ \neg R(x)\bigr) && \text{De Morgan} \\
\Rightarrow\quad & \forall x\,\forall y\,[\,P(y)\ \land\ \neg R(x)\,]
\end{aligned}
$$
