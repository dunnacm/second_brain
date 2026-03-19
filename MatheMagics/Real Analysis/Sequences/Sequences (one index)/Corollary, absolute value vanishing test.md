---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Absolute-Value Vanishing Test**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}\,|s_n|=0$.
>
> > [!tip]+ **THEN**
> > $\displaystyle \lim_{n\to\infty}\,s_n=0$.

## Proof

Assumption:

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}|s_n|=0
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow \big||s_n|-0\big|<\varepsilon\,].
\end{aligned}
$$

Apply **UI** on $\varepsilon$ (arbitrary), then by **EI** obtain $N(\varepsilon)\in\mathbb{N}$, and finally apply **UI** on $n$ to (1), sequentially:

$$
\begin{aligned}
&(2)\quad n\ge N_\varepsilon(0) \Rightarrow \big||s_n|-0\big|<\varepsilon.
\end{aligned}
$$

Since $\big||s_n|-0\big|=|s_n|=|s_n-0|$, we have

$$
\begin{aligned}
&(3)\quad n\ge N_\varepsilon(0) \Rightarrow |s_n-0|<\varepsilon.
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to (3), sequentially:

$$
\begin{aligned}
&(4)\quad
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-0|<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}s_n=0.
\end{aligned}
$$
