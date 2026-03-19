---
down:
  - "[[Squeeze (sandwich) theorem]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Comparison-to-Zero (Squeeze)**
> > [!warning]+ **IF**
> > - $0\le s_n \le t_n,\ \forall n\in\mathbb{N}$  
> > - $\displaystyle \lim_{n\to\infty}\{t_n\}=0$
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\}=0.$$
## Proof:
### Version 1:
$$
\begin{aligned}
(1)\quad 
&\forall n\in\mathbb{N}\,[\,s_n\ge 0\,]
\ \Rightarrow\
\liminf_{n\to\infty} s_n \ge 0. 
\end{aligned}
$$

From order preservation of limits applied to $\{s_n\}\le \{t_n\}$ with $\lim t_n=0$:
$$
\begin{aligned}
(2)\quad 
&s_n \le t_n\ \text{ and }\ \lim_{n\to\infty} t_n=0
\ \Rightarrow\
\limsup_{n\to\infty} s_n \le \lim_{n\to\infty} t_n = 0.
\end{aligned}
$$

Combine (1) and (2):
$$
\begin{aligned}
(3)\quad 
0 \le \liminf_{n\to\infty} s_n \le \limsup_{n\to\infty} s_n \le 0
\ \Rightarrow\
\liminf_{n\to\infty} s_n = \limsup_{n\to\infty} s_n = 0.
\end{aligned}
$$

Therefore the limit exists and
$$
\begin{aligned}
(4)\quad 
\lim_{n\to\infty} s_n = 0.
\end{aligned}
$$

### Version 2:
$$
\begin{aligned}
\text{Assumptions:}\qquad
(1)\;&\lim_{n\to\infty}\{t_n\}=0 
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |t_n-0|<\varepsilon\,],\\[4pt]
(2)\;&0\le s_n \le t_n,\ \forall n\in\mathbb{N}.
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$ to assumption (1):
$$
\begin{aligned}
(3)\quad & n\ge N \Rightarrow |t_n-0|<\varepsilon\\[4pt]
& \qquad \quad\Rightarrow\ |t_n|<\varepsilon.
\end{aligned}
$$

From assumption (2):
$$
\begin{aligned}
(4)\quad & 0\le s_n \le t_n\\[4pt]
\qquad \Rightarrow\ & 0\le |s_n| \le |t_n|.
\end{aligned}
$$

Substitute (4) into (3):
$$
\begin{aligned}
(3')\quad & n\ge N \Rightarrow |t_n|<\varepsilon\\[4pt]
& \qquad \quad \Rightarrow\ |s_n|\le |t_n|<\varepsilon\\[4pt]
& \qquad \quad \Rightarrow\ |s_n|<\varepsilon.
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to (3') sequentially:
$$
\begin{aligned}
(3'')\quad 
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n|<\varepsilon\,]
\ \Leftrightarrow\ 
\lim_{n\to\infty}\{s_n\}=0.
\end{aligned}
$$
### Version 3:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\{s_n\}=K 
\;\;\Leftrightarrow\;\;
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |s_n-K|<\varepsilon\,],\\[4pt]
&\lim_{n\to\infty}\{t_n\}=L 
\;\;\Leftrightarrow\;\;
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |t_n-L|<\varepsilon\,],\\[4pt]
&\forall n\in\mathbb{N}\;[\,s_n\le t_n\,].
\end{aligned}
$$

Assume for contradiction that
$$
\begin{aligned}
(2)\quad K>L.
\end{aligned}
$$

Fix (**UI**) 
$$
\begin{aligned}
(3)\quad \varepsilon:=\frac{K-L}{3}\;>\;0.
\end{aligned}
$$

From (1) with **EI** on \(N_1,N_2\) and **UI** on \(n\):
$$
\begin{aligned}
(4)\quad &n\ge N_1 \Rightarrow |s_n-K|<\varepsilon \;\Rightarrow\; s_n> K-\varepsilon,\\[2pt]
(5)\quad &n\ge N_2 \Rightarrow |t_n-L|<\varepsilon \;\Rightarrow\; t_n< L+\varepsilon.
\end{aligned}
$$

Let
$$
\begin{aligned}
(6)\quad N:=\max\{N_1,N_2\}.
\end{aligned}
$$

Then for all \(n\ge N\), combining (4)–(5) and using (3):
$$
\begin{aligned}
(7)\quad s_n &> K-\varepsilon = K-\frac{K-L}{3}=\frac{2K+L}{3},\\[4pt]
(8)\quad t_n &< L+\varepsilon = L+\frac{K-L}{3}=\frac{K+2L}{3}.
\end{aligned}
$$

But from \(K>L\) we have
$$
\begin{aligned}
(9)\quad \frac{2K+L}{3} - \frac{K+2L}{3} = \frac{K-L}{3}=\varepsilon>0
\;\Rightarrow\;
\frac{2K+L}{3}>\frac{K+2L}{3}.
\end{aligned}
$$

Hence, for all \(n\ge N\),
$$
\begin{aligned}
(10)\quad s_n>\frac{2K+L}{3}>\frac{K+2L}{3}>t_n,
\end{aligned}
$$
which contradicts \(s_n\le t_n\) for all \(n\) from (1).

Therefore the assumption (2) is false, and we conclude
$$
\begin{aligned}
(11)\quad K\le L.\ \ \ \square
\end{aligned}
$$
