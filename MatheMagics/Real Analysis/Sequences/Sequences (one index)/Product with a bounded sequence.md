---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Product with a Bounded Sequence**
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=0,$  
> > - $\exists M>0\ \forall n\in\mathbb{N}\,[\,|t_n|<M\,],$
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\cdot t_n\}=0.$$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\{s_n\}=0 \;\Rightarrow\; \{s_n\}\ \text{is bounded.}
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
&|t_n|\le M\\[4pt]
& 0\le |t_n|\le M\\[4pt]
& 0\le |s_n|\,|t_n|\le |s_n|\,M\\[4pt]
& 0\le |s_n t_n|\le |s_n|\,M,\ \ \forall n\in\mathbb{N}.
\end{aligned}
$$

Applying the squeeze theorem to (2):
$$
\begin{aligned}
(3)\quad 
&\lim_{n\to\infty}0\ \le\ \lim_{n\to\infty}\lvert s_n\cdot t_n\rvert\ \le\ \lim_{n\to\infty}\bigl(\,|s_n|\cdot M\,\bigr)
\qquad \text{(from (2), taking limits)}\\[6pt]
&\qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \  M\cdot \lim_{n\to\infty}|s_n|
\qquad \text{(constant–multiple rule)}\\[4pt]
&\qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \ M\cdot 0\ =\ 0
\qquad \text{(substitute $\lim |s_n|=0$ from (1)).}
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
0\ \le\ \lim_{n\to\infty}|s_n t_n|\ \le\ 0
\;\Rightarrow\;
\lim_{n\to\infty}|s_n t_n|=0
\;\Leftrightarrow\;
\lim_{n\to\infty}(s_n t_n)=0.
\end{aligned}
$$
