---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Formal definition, 1st. case:

> [!note]+ **Direct comparison test — convergence via upper bound**
>
> > [!warning]+ **IF**
> > - $S^{(1)}=\sum_{n=1}^{\infty} s_n$
> > 	∘ $s_n\ge 0$ for all *n* in $\mathbb{N},$ (i.e., **positive**)
> > 	∘ $S^{(1)}$ is **convergent** 
> > 
> > - $S^{(2)}=\sum_{n=1}^{\infty} t_n$ 
> > 	  ∘ $t_n\ge 0\ \text{for all }n\in\mathbb{N},$ (i.e., **positive**)
> > 
> > - $0\le t_n\le s_n\ \text{for all }n\in\mathbb{N}.$
>
> > [!tip]+ **THEN**
> > $$S^{(2)}\ \text{is convergent.}$$
### Proof:

$$
\begin{aligned}
(1)\quad & S_n \;:=\; \sum_{k=1}^{n} s_k \\[6pt]
(2)\quad & T_n \;:=\; \sum_{k=1}^{n} t_k
\end{aligned}
$$

**Assumptions:**

$$
\begin{aligned}
(3)\quad & \lim_{n\to\infty}\{S_n\}=S\in\mathbb{R}\qquad (\text{i.e., convergent}) \\[6pt]
(4)\quad & 0\le t_n \le s_n,\ \ \forall n\in\mathbb{N}
\end{aligned}
$$

$$
\begin{aligned}
(5)\quad 
& M := \max\{\, s_1, s_2, \ldots, s_{n-1},\, |S|+\varepsilon \,\}
\qquad (\forall n\in\mathbb{N}\ [\, s_n \ge 0 \,])\\[2pt]
& \phantom{M}
= \max\{\, s_1, s_2, \ldots, s_n,\, S+\varepsilon \,\}
\end{aligned}
$$

From eq. (3):

$$
\begin{aligned}
& \lim_{n\to\infty}\{S_n\}=\sum_{n=1}^{\infty} s_n = S 
\ \Rightarrow\ 
\forall n\in\mathbb{N}\ [\, |S| \le M \,]\quad (\text{convergent} \Rightarrow \text{bounded})\\[4pt]
& \qquad\ \qquad\ \qquad\ \qquad\ \quad\ \Rightarrow\ \forall n\in\mathbb{N}\ [\, S \le M \,] 
\qquad (S_n \ge 0 \Rightarrow S \ge 0)
\end{aligned}
$$

Applying **addition of an arbitrary number of inequalities** to eq. (4):

$$
\begin{aligned}
(6)\quad 
& 0\le t_n \le s_n,\ \forall n\in\mathbb{N} \\[4pt]
& \forall N\in\mathbb{N}:\quad
0 \le \sum_{n=1}^{N} t_n \;\le\; \sum_{n=1}^{N} s_n 
\;=\; S_N \;\le\; M \\
\end{aligned}
$$
Hence $\{T_N\}_{N\in\mathbb{N}}$ is bounded by M



From eq. (4):

$$
\begin{aligned}
(7)\quad 
& t_n \ge 0 \ \Rightarrow\ \sum_{k=1}^{n+1} t_k \ge \sum_{k=1}^{n} t_k 
\quad (\text{sub. from (2)})\\[2pt]
&  t_n \ge 0 \ \Rightarrow\ \forall n\in\mathbb{N}\,[\, T_{n+1}\ge T_n \,]
\quad (\text{i.e., monotone non-decreasing})
\end{aligned}
$$

Combining eqs. (5), (6):

$$
\begin{aligned}
(8)\quad 
& 0 \le \sum_{n=1}^{\infty} t_n \le S \le M \\[2pt]
& \sum_{n=1}^{\infty} t_n \le M \qquad (\text{i.e., bounded})
\end{aligned}
$$
From equations (7) and (8):
$$
\begin{aligned}
&\forall n\in\mathbb{N}\,[\,T_{n+1}\ge T_n\,]\ \land\ \sum_{n=1}^{\infty} t_n \le M
\ \xRightarrow{\ \text{monotone convergence theorem}\ }\ 
\sum_{n=1}^{\infty} t_n \;=\; T \in \mathbb{R}\,.
\end{aligned}
$$


### Formal definition, 2nd. case:

> [!note]+ **Direct comparison test — divergence via lower bound**
>
> > [!warning]+ **IF**
> > - $S^{(1)}=\sum_{n=1}^{\infty} s_n$
> >   ∘ $s_n\ge 0$ for all $n\in\mathbb{N}$ (i.e., **positive**)  
> >   ∘ $S^{(1)}$ is **divergent**
> >
> > - $S^{(2)}=\sum_{n=1}^{\infty} t_n$
> >   ∘ $t_n\ge 0$ for all $n\in\mathbb{N}$ (i.e., **positive**)
> >
> > - $0\le s_n\le t_n$ for all $n\in\mathbb{N}$.
>
> > [!tip]+ **THEN**
> > $$S^{(2)}\ \text{is divergent.}$$
