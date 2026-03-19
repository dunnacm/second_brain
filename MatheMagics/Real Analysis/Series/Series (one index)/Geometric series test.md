---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Verbal definition:
A **geometric series** is a sum where each term equals the previous one times a constant **r** (the common ratio). 
It **converges if and only if** |**r**| < 1; when it converges, its sum equals the **first term** divided by **(1 − r)** (i.e., $\dfrac{\text{first term}}{1 - \text{common ratio}}$). 
If |**r**| ≥ 1 (and the first term isn’t zero), the series diverges. 
### Formal definition:

> [!note]+ **Geometric series — convergence and sum**
>
> > [!warning]+ **IFF**
> > - $S=\sum_{n=0}^{\infty} a\,r^{n},\qquad a,r\in\mathbb{R}-{0}$
> > - $|r|<1.$
>
> > [!tip]+ **THEN**
> > S converges to $S=\dfrac{a}{1-r}.$
> 
> ---
> *(Variant: for $\sum_{n=1}^{\infty} a\,r^{n}$ with $|r|<1$, the sum is $\dfrac{a\,r}{1-r}$.)*
## Proof:
$$
\begin{aligned}
(1)\quad 
& S_N=\sum_{n=1}^{N}s_n
=\sum_{n=1}^{N} a\,r^{\,n-1}
= a + a r + a r^{2} + \cdots + a r^{\,N-1}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& r\,S_N
= a r + a r^{2} + \cdots + a r^{\,N-1} + a r^{\,N}.
\end{aligned}
$$

Subtracting eqs. (1), (2):

$$
\begin{aligned}
(3)\quad 
& S_N - rS_N
= a + \bcancel{a r} + \bcancel{a r^{2}} + \cdots + a r^{\,N-1}
- \big[\bcancel{a r} + \bcancel{a r^{2}} + \cdots + a r^{\,N-1} + a r^{\,N}\big]\\[4pt]
&\Rightarrow\quad S_N(1-r)= a - a r^{\,N}
= a(1-r^{\,N})\\[4pt]
&\Rightarrow\quad S_N=\dfrac{a\,(1-r^{\,N})}{1-r}\,.
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
& \lim_{N\to\infty} S_N
= \lim_{N\to\infty}\dfrac{a\,(1-r^{\,N})}{1-r}.
\end{aligned}
$$

From eq. (4): 
$$
S=\dfrac{a}{1-r}\quad (\text{i.e., converges})\ \text{for }\ |r|<1,
\qquad
\text{and } \sum_{n=1}^{\infty}a r^{\,n-1}\ \text{diverges for } |r|\ge 1.
$$
