---
down:
  - "[[Floor-ceiling fact]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Definition 1:
#### Verbal definition:
Given real numbers **a** and **b** with **a > 0**, the Archimedean idea says that no matter how small **a** is and how large **b** is, there exists a natural number **n** so that repeatedly adding **a** to itself **n** times will exceed **b**—intuitively, even a teaspoon (**a**) can “drain an ocean” (**b**) if you scoop enough times (**n**).
#### Formal definition

> [!note]+ **Archimedean lemma (na exceeds b)**
> > [!warning]+ **IF**
> > - $a,b\in\mathbb{R}$
> > - $a>0$
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \exists\,n\in\mathbb{N}\ \big[\,n a>b\,\big].
> > $$
##### Proof:
**Assumption by contradiction:**

$$
\begin{aligned}
(1)\quad 
& a,b\in\mathbb{R}\ \land\ a>0\ \Rightarrow\ \sim\exists n\in\mathbb{N}\,[\,an<b\,]\ \Leftrightarrow\ \forall n\in\mathbb{N}\,[\,an\le b\,]
\\[6pt]
& a,b\in\mathbb{R}\ \land\ a>0\ \Rightarrow\ \forall n\in\mathbb{N}\,[\,an\le b\,].
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& S:=\{\,an:\ n\in\mathbb{N}\,\}
\ \Rightarrow\ 
S\subseteq\mathbb{R}\ \land\ S\ne\varnothing.
\end{aligned}
$$

From eqs.(1), (2):

$$
\begin{aligned}
(3)\quad 
& \forall n\in\mathbb{N}\,[\,an\le b\,]\ \land\ [\,S\subseteq\mathbb{R}\ \land\ S\ne\varnothing\,] \overset{(\ast)\ \text{Supremum property}}{\Longleftrightarrow}\ 
\exists\,b\in\mathbb{R}\,[\,\sup(S)=b\,]
\\[6pt]
& \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad \ \Longleftrightarrow\ 
\forall s\in S\,[\,s\le b\,]\ \land\ \forall \varepsilon>0\ \exists s\in S\,[\,b-\varepsilon<s\,].
\end{aligned}
$$

![[diagram_s_b_splus1.png]]
**Applying UI on** $\varepsilon$, **fixing it in** $\mathbb{N}$ (e.g., $\varepsilon:=a$); **and EI on** $s$ in eq.\ (3), **fixing it as** $an$; sequentially:

$$
\begin{aligned}
(4)\quad 
& an\le b\ \land\ b-a<an
\\[6pt]
& an\le b\ \land\ b<an+a
\\[6pt]
& an\le b\ \land\ a(n+1)>b
\\[6pt]
& an\le b\ \land\ am>b,\ m\in\mathbb{N}
\\[6pt]
& an\le b\ \land\ \sim(am\le b),\ m\in\mathbb{N}
\\[6pt]
& p\ \land\ \sim p
\end{aligned}
$$

Eq.(4) results in a contradiction; therefore, by *reductio ad absurdum*, the initial assumption is false.
$$
\begin{aligned}
(5)\quad 
& a,b\in\mathbb{R}\ \land\ a>0\ \nRightarrow\ \forall n\in\mathbb{N}\,[\,an\le b\,]
\\[6pt]
& a,b\in\mathbb{R}\ \land\ a>0\ \Rightarrow\ \sim\forall n\in\mathbb{N}\,[\,an\le b\,]
\\[6pt]
& a,b\in\mathbb{R}\ \land\ a>0\ \Rightarrow\ \exists n\in\mathbb{N}\,[\,an>b\,].
\end{aligned}
$$


### Definition 2:
#### Verbal definition:
For any positive real **ε**, there exists a natural number **n** such that the reciprocal **1/n** is smaller than **ε**—in other words, reciprocals of natural numbers can be made arbitrarily small.
#### Formal definition:

> [!note]+ **Archimedean corollary (find $n$ with $1/n<\varepsilon$)**
> > [!warning]+ **IF**
> > - $\varepsilon\in\mathbb{R}$
> > - $\varepsilon>0$
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \exists\,n\in\mathbb{N}\ [\,\frac{1}{n}<\varepsilon\,].
> > $$

##### Proof (from Archimedean lemma)
