---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Difference Rule for Limits (Sequences)**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}\{s_n\}=K \quad\wedge\quad \lim_{n\to\infty}\{t_n\}=L$.
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\big(\{s_n\}-\{t_n\}\big)=K-L.
> > $$
## Proof:

> [!abstract]+ **Proof outline — Difference Rule**
>
> 1) From $\lim t_n=L$ and the **Scalar Multiple Rule**, get $\lim (c\,t_n)=cL$ for any $c$.
> 2) Let $u_n:=c\,t_n$; then $\lim u_n=cL$.
> 3) With $\lim s_n=K$, apply the **Sum Rule** to $s_n$ and $u_n$ to get $\lim(s_n+u_n)=K+cL$.
> 4) Pick $c=-1$ so that $u_n=-t_n$ and $K+cL=K-L$.
> 5) Conclude $\lim(s_n-t_n)=K-L$.


Let $c\in\mathbb{R}$ and suppose $\displaystyle \lim_{n\to\infty}\{t_n\}=L$.

From the **Scalar Multiple Rule**,
$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\big(c\cdot\{t_n\}\big)=c\cdot L,\qquad \forall c\in\mathbb{R}.
\end{aligned}
$$

Define $c\cdot\{t_n\}:=\{u_n\}$:

$$
(2)\quad u_n := c\,t_n.
$$

Substitute (2) into (1):

$$
\begin{aligned}
&(1')\quad \lim_{n\to\infty}\{u_n\}=c\,L,\qquad \forall c\in\mathbb{R}.
\end{aligned}
$$

Assume also $\displaystyle \lim_{n\to\infty}\{s_n\}=K$. By the **Sum Rule**,

$$
\begin{aligned}
&(3)\quad \lim_{n\to\infty}\{s_n\}=K \ \wedge\ \lim_{n\to\infty}\{u_n\}=c\,L
\ \Rightarrow\
\lim_{n\to\infty}\{s_n\}+\lim_{n\to\infty}\{u_n\}=K+cL,\quad \forall c\in\mathbb{R}.
\end{aligned}
$$

Choose $c:=-1$:

$$
(4)\quad c:=-1.
$$

Substitute (4) into (3):

$$
\begin{aligned}
&(3')\quad \lim_{n\to\infty}\{s_n\}=K \ \wedge\ \lim_{n\to\infty}\{u_n\}=(-1)L
\ \Rightarrow\
\lim_{n\to\infty}\{s_n\}+\lim_{n\to\infty}\{u_n\}=K-L.
\end{aligned}
$$

But $u_n=c\,t_n=-t_n$, hence $\{u_n\}=-\{t_n\}$ and
$$
\lim_{n\to\infty}\big(\{s_n\}-\{t_n\}\big)
=\lim_{n\to\infty}\big(\{s_n\}+\{u_n\}\big)
=K-L.
$$
