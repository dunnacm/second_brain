---
down:
  - "[[Corollary, absolute value vanishing test]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Absolute Value Preserves Limits**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty} s_n = L$.
>
> > [!tip]+ **THEN**
> > $\displaystyle \lim_{n\to\infty} |s_n| = |L|$.
## Proof:
Assumption:

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,].
\end{aligned}
$$

Apply **UI** on $\varepsilon$; then by **EI** obtain $N_{\varepsilon}\in\mathbb{N}$; finally apply **UI** on $n$ to (1), sequentially.

$$
\begin{aligned}
&(2)\quad n\ge N \Rightarrow |s_n-L|<\varepsilon
\qquad\text{(inverse triangle inequality: }||x|-|y||\le|x-y|\text{)}
\\[6pt]
&\qquad \, n\ge N \Rightarrow \big||s_n|-|L|\big|\le |s_n-L|<\varepsilon\\
&\qquad \, n\ge N \Rightarrow \big||s_n|-|L|\big|\le \varepsilon.
\end{aligned}
$$
Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ (with witness $\hat{\varepsilon}$) to (3), sequentially:

$$
\begin{aligned}
&(4)\quad
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow \big||s_n|-|L|\big|<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}|s_n|=|L|.
\end{aligned}
$$