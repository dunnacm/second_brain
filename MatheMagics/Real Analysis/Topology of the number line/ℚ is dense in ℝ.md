---
down:
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definition:

> [!note]+ **Density of Q in R**
> > [!warning]+ **IF**
> > - $x,y\in\mathbb{R}$ and $x<y$.
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \exists q\in\mathbb{Q}\ [\,x<q<y\,].
> > $$
## Proof:
$$
\begin{aligned}
& x,y\in\mathbb{R},\ x<y \ \Rightarrow\ \exists q\in\mathbb{Q}\ [\,x<q<y\,].
\end{aligned}
$$

**CASE I** — Assumption: $x\in\mathbb{R}^{-}\ \land\ y\in\mathbb{R}^{+}$

$$
\begin{aligned}
(1)\quad 
& x<0<y,\qquad 0\in\mathbb{Q}
\\[6pt]
& \therefore\ \exists q\in\mathbb{Q}\ [\,x<q<y\,] \quad (\text{take } q:=0).
\end{aligned}
$$

---

**CASE II** — Assumption: $x,y\in\mathbb{R}^{+}$

$$
\begin{aligned}
(2)\quad 
& 0<x<y
\\[6pt]
& -x<0<y-x
\\[6pt]
& -x<0\ \land\ 0<y-x
\\[6pt]
& 0<x\ \land\ 0<y-x .
\end{aligned}
$$

From assumption and eq. (2)’s second conjunct:

$$
\begin{aligned}
(3)\quad 
& (y-x)\in\mathbb{R},\ 1\in\mathbb{R},\ y-x>0
\\[6pt]
& \overset{\text{Archimedean}}{\Longrightarrow}\ \exists n\in\mathbb{N}\ [\, (y-x)n>1 \,]
\\[6pt]
& \overset{\text{integer in gap}}{\Longrightarrow}\ \exists z\in\mathbb{Z}\ [\, x n< z< y n \,]
\\[6pt]
& \quad\ \Longrightarrow\ x<\dfrac{z}{n}<y\quad \big[\, q:=\dfrac{z}{n}\in\mathbb{Q}\,\big].
\end{aligned}
$$

---

**CASE III** — Assumption: $x,y\in\mathbb{R}^{-}$

Apply the result of Case II to $-y<-x$ (both positive):

$$
\begin{aligned}
(4)\quad 
& -y<z<-x,\ z\in\mathbb{Q}
\\[6pt]
& \Rightarrow\ x< -z < y \quad \big[\, q:=-z\in\mathbb{Q}\,\big].
\end{aligned}
$$

---

All cases yield $\exists q\in\mathbb{Q}\ [\,x<q<y\,]$.
