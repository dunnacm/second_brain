---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
If the even-indexed subsequence $\{s_{2n}\}$ and the odd-indexed subsequence $\{s_{2n+1}\}$ both converge to the same limit $L$, then the entire sequence $\{s_n\}$ also converges to $L$.
### Formal definition:

> [!note]+ **Even–Odd Subsequence Convergence Criterion**
> > [!warning]+ **IF**
> > $$\displaystyle \lim_{n\to\infty}\{s_{2n}\}=L \quad\text{and}\quad \lim_{n\to\infty}\{s_{2n+1}\}=L,$$
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\}=L.$$
## Proof:
$$
\begin{aligned}
\text{Assumptions:}\qquad
(1)\;&\lim_{n\to\infty}\{s_{2n}\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |s_{2n}-L|<\varepsilon\,],\\[4pt]
(2)\;&\lim_{n\to\infty}\{s_{2n+1}\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |s_{2n+1}-L|<\varepsilon\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N_1,N_2$, and **UI** on $n$ to (1), (2):

$$
\begin{aligned}
(3)\quad 
& n\ge N_1 \Rightarrow |s_{2n}-L|<\varepsilon\\[6pt]
\Rightarrow\ & \dfrac{n}{2}\ge N_1 \Rightarrow |s_n-L|<\varepsilon\\[6pt]
\Rightarrow\ & n\ge 2N_1 \Rightarrow |s_n-L|<\varepsilon
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
& n\ge N_2 \Rightarrow |s_{2n+1}-L|<\varepsilon\\[6pt]
\Rightarrow\ & \dfrac{n-1}{2}\ge N_2 \Rightarrow |s_n-L|<\varepsilon\\[6pt]
\Rightarrow\ & n\ge 2N_2+1 \Rightarrow |s_n-L|<\varepsilon
\end{aligned}
$$

Informed by (3), (4), choose the common index
$$
N_{\varepsilon}:=\max\{\,2N_1,\ 2N_2+1\,\}.
$$

Substitute $N_{\varepsilon}$ into (3), (4):

$$
\begin{aligned}
(3')\;&n\ge N_{\varepsilon}\ \wedge\ \text{$n$ even} \Rightarrow |s_n-L|<\varepsilon,\\[4pt]
(4')\;&n\ge N_{\varepsilon}\ \wedge\ \text{$n$ odd} \Rightarrow |s_n-L|<\varepsilon.
\end{aligned}
$$

Combining (3'), (4') (parity split):

$$
\begin{aligned}
(5)\;\; n\ge N_{\varepsilon}\ \Rightarrow\ |s_n-L|<\varepsilon.
\end{aligned}
$$

Therefore,
$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]
\quad \Leftrightarrow\quad 
\lim_{n\to\infty}\{s_n\}=L.
$$

