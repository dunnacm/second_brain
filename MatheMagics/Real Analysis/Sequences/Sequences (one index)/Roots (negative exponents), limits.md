---
down:
tags:
  - mathemagics/real_analysis
---
## Definition: 

> [!note]+ **Root Limit Theorem (Negative Exponents)**
> > [!warning]+ **IF**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\}=L\ge 0,$$
>
> > [!tip]+ **THEN**
> > $$\forall m\in\mathbb{Z}^{-}\ \Bigl[\ \lim_{n\to\infty}\{s_n^{1/m}\}=L^{1/m}\ \Bigr].$$
## Proof:

$$
\begin{aligned}
\lim_{n\to\infty}\{s_n\}^{1/m} 
&= \lim_{n\to\infty} \dfrac{1}{\{s_n\}^{-1/m}}
\qquad \text{(applying Reciprocal Limit Lemma)}\\[6pt]
&= \dfrac{1}{\displaystyle \lim_{n\to\infty}\{s_n\}^{-1/m}}\\[8pt]
&= \dfrac{1}{L^{-1/m}}\\[6pt]
&= L^{1/m}.
\end{aligned}
$$
