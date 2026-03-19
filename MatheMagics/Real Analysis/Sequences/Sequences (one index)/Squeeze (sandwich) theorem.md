---
down:
  - "[[Product with a bounded sequence]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Squeeze (Sandwich) Theorem — Sequences**
> > [!warning]+ **IF**
> > - $\{t_n\}\le \{s_n\}\le \{u_n\}$ for all $n\in\mathbb{N}$,
> > - $\displaystyle \lim_{n\to\infty}\{t_n\}=\lim_{n\to\infty}\{u_n\}=L$,
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\}=L.$$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\{t_n\}\le \{s_n\}\le \{u_n\}
\Rightarrow\ 0\le \{\,s_n-t_n\,\}\le \{\,u_n-t_n\,\}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
&\lim_{n\to\infty}\{u_n\}=\lim_{n\to\infty}\{t_n\}(=L)
\\
& \lim_{n\to\infty}\{u_n\}-\lim_{n\to\infty}\{t_n\}=0
\quad \text{(applying difference of limits thm.)}
\\
& \lim_{n\to\infty}\{\,u_n-t_n\,\}=0.
\end{aligned}
$$

From eqs. (1), (2) and comparison-to-zero lemma:
$$
\begin{aligned}
&0\le \{\,s_n-t_n\,\}\le \{\,u_n-t_n\,\}\ \wedge\ 
\lim_{n\to\infty}\{\,u_n-t_n\,\}=0
\Rightarrow\ \lim_{n\to\infty}\{\,s_n-t_n\,\}=0.
\end{aligned}
$$

$$
\begin{aligned}
(3)\quad 
\lim_{n\to\infty}\{s_n\}
&=\lim_{n\to\infty}\{\,s_n-t_n+t_n\,\}
\quad \text{(applying addition of limits thm.)}
\\
&=\lim_{n\to\infty}\{\,s_n-t_n\,\}+\lim_{n\to\infty}\{t_n\}
\\
&=0+L
\\
&=L.
\end{aligned}
$$
