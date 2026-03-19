---
down:
  - "[[Even-odd subsequence convergence, corollary]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Limit of a Subsequent Sequence**
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{k\to\infty}\{s_k\}=L$  (i.e., the sequence converges),  
> > - $\{t_n\}_{n=1}^{\infty}=\{s_{k_n}\}_{n=1}^{\infty}$  (i.e., any subsequence of $\{s_k\}$),
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{t_n\}=L,$$  
> > equivalently,  
> > $$\displaystyle \lim_{n\to\infty}\{s_{k_n}\}=L.$$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\{s_n\}=L 
\quad \Leftrightarrow \quad
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall m\in\mathbb{N}\,[\,m\ge N \Rightarrow |s_m-L|<\varepsilon\,].
\end{aligned}
$$

Apply **UI** on $\varepsilon$ and **EI** on $N$ from (1).  
Fix a strictly increasing sequence of indices $\{k_n\}$ and define $t_n:=s_{k_n}$.  
We aim to verify the antecedent of (1) with the substitution $m:=k_n$.

Since $\{{k_n}\}$ is strictly increasing, $(2) \quad k_{n+1}>k_n \text{ for all } n.$

From (2), two consequences:

$$
\begin{aligned}
(3)\quad 
&k_N \ge N \qquad \text{(strictly increasing integer sequence gives } k_n\ge n\text{ by induction),}
\\[4pt]
(4)\quad 
&n\ge N \Rightarrow k_n \ge k_N \qquad \text{(monotonicity of } \{k_n\}\text{).}
\end{aligned}
$$

Combine (3) and (4) to obtain the needed antecedent:

$$
\begin{aligned}
(5)\quad 
&n\ge N \Rightarrow k_n \ge k_N \ge N 
\quad \Rightarrow \quad k_n \ge N.
\end{aligned}
$$

Now substitute $m:=k_n$ in (1) and use (5):

$$
\begin{aligned}
(6)\quad 
&n\ge N 
\ \Rightarrow\ \underbrace{k_n\ge N}_{\text{by (5)}}
\ \Rightarrow\ \underbrace{|s_{k_n}-L|<\varepsilon}_{\text{from (1) with } m:=k_n}
\ \Rightarrow\ |t_n-L|<\varepsilon\ (\text{since } t_n:=s_{k_n}).
\end{aligned}
$$

Finally, apply **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$:

$$
\begin{aligned}
(7)\quad 
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |t_n-L|<\varepsilon\,]
\quad \Leftrightarrow \quad 
\lim_{n\to\infty}\{t_n\}=L.
\end{aligned}
$$
