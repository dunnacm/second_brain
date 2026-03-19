---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
If a real sequence ${s_n}$ has **infinitely many peaks**—i.e., there are infinitely many indices $N$ with $s_N \ge s_n$ for all $n \ge N$—then listing those peak indices in increasing order $k_1<k_2<k_3<\cdots$ yields a **nonincreasing subsequence**: $s_{k_1}\ge s_{k_2}\ge s_{k_3}\ge\cdots$.
![[40a26e0e-2373-466f-bc5a-884a9d9553a6_white.png]]
### Formal definition:

> [!note]+ **Infinite peaks ⇒ nonincreasing subsequence**
> > [!warning]+ **IF**
> > - $\exists\,\{k_n\}_{n\in\mathbb{N}}\subseteq\mathbb{N}\ \wedge \ \forall n\in\mathbb{N}\,[\,k_{n+1}>k_n\,].$ (i.e., there exists a strictly increasing index sequence $(k_n)$)
> > - $\forall m,n\in\mathbb{N}\,[\,m\ge k_n \Rightarrow s_{k_n}\ge s_m\,]$ (i.e., every $s_{k_n}$ is a peak).
> 
> 
> > [!tip]+ **THEN**
> >$$
> > \forall n\in\mathbb{N}\,[\,s_{k_{n+1}}\le s_{k_n}\,]
> > \quad\text{($\{s_{k_n}\}$ is nonincreasing).}
> > $$

## Proof:
**Assumptions**
- There are infinitely many peaks.
- Every $s_{k_n}$ is a peak, and $\{k_n\}$ is (weakly) increasing: $\forall n\in\mathbb{N}\,[\,k_{n+1}\ge k_n\,]$.

**First assumption**:
$$
\begin{aligned}
(1)\quad 
& s_{k_n}\ \text{is a peak}
\ \Leftrightarrow\
\forall m\in\mathbb{N}\,[\,m\ge k_n \Rightarrow s_{k_n}\ge s_m\,].
\end{aligned}
$$

Applying **UI** on $n$ in (1), and **EI** on $m$ with $m:=k_{n+1}$:
$$
\begin{aligned}
(1')\quad 
& s_{k_n}\ \text{is a peak}
\ \Leftrightarrow\
\big(k_n\le k_{n+1}\ \Rightarrow\ s_{k_n}\ge s_{k_{n+1}}\big)
\qquad \text{(In PL:\quad \ $A\Leftrightarrow(B\Rightarrow C)$)}.
\end{aligned}
$$

**Second assumption**:
$$
\begin{aligned}
(2)\quad 
& \forall n\in\mathbb{N}\,[\,k_n\le k_{n+1}\,].
\end{aligned}
$$

Applying **UI** on $n$ in eq. (2):
$$
\begin{aligned}
(2')\quad 
& k_n\le k_{n+1}
\qquad \text{(In PL:\quad \ $B$)}.
\end{aligned}
$$

Combining eqs. (1'), (2') by **Modus ponens** :
$$
\begin{aligned}
(3)\quad 
& s_{k_n}\ge s_{k_{n+1}} .
\end{aligned}
$$
![[peak_step_diagram_fixed.png]]
Applying **UG** on $n$ in eq. (3):
$$
\begin{aligned}
(3')\quad 
& \forall n\in\mathbb{N}\,[\,s_{k_n}\ge s_{k_{n+1}}\,].
\end{aligned}
$$

$\therefore$ ${s_{k_n}}$ is nonincreasing (a monotone subsequence).



