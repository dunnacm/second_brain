---
down:
  - "[[Ratio criterion for vanishing sequence]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Quotient Limit Theorem**
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=K,$  
> > - $\displaystyle \lim_{n\to\infty}\{t_n\}=L$ with $L\ne 0$ and $\forall n\in\mathbb{N},\, t_n\ne 0$.
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\frac{s_n}{t_n}=\frac{K}{L}.$$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\{s_n\}=K 
\quad \Leftrightarrow \quad 
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |s_n-K|<\varepsilon\,].
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
&\lim_{n\to\infty}\{t_n\}=L\ne 0
\quad \Leftrightarrow \quad 
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |t_n-L|<\varepsilon\,].
\\
&\text{In particular, there exists }N_0\text{ such that }n\ge N_0 \Rightarrow t_n\neq 0.
\end{aligned}
$$

From (2), via the reciprocal lemma (proved separately):
$$
\begin{aligned}
(3)\quad 
&\lim_{n\to\infty}\{t_n\}=L\ne 0 
\ \Rightarrow\ 
\lim_{n\to\infty}\left\{\dfrac{1}{t_n}\right\}=\dfrac{1}{L}.
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
\lim_{n\to\infty}\dfrac{s_n}{t_n}
&= \lim_{n\to\infty}\{s_n\}\cdot\lim_{n\to\infty}\left\{\dfrac{1}{t_n}\right\}
\quad \text{(product limit law, using (1) and (3))}\\[6pt]
&= K\cdot\dfrac{1}{L}
= \dfrac{K}{L}.
\end{aligned}
$$
