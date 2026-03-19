---
down:
  - "[[Infinity (divergent sequences)]]"
  - "[[-Infinity (divergent sequences)]]"
  - "[[DNE (divergent sequences)]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
> [!note]+ **Theorem — Non-convergence (Divergence) of a sequence**
>
> > [!warning]+ **IFF**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=\varnothing$  **or**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=\pm\infty$.
>
> > [!tip]+ **THEN**
> > - $\displaystyle \neg\Big(\exists\,L\in\mathbb{R}\ \forall\,\varepsilon>0\ \exists\,N\in\mathbb{N}\ \forall\,n\in\mathbb{N}\,[\,n\ge N \Rightarrow \lvert s_n-L\rvert<\varepsilon\,]\Big)$
>---
> > [!note]+ **Notes**
> > - “$\lim\{s_n\}=\varnothing$” means **no real limit exists** (e.g., oscillation).  
> > - The logical negation can be pushed inside (equivalent form):
> >   $$
> >   \forall\,L\in\mathbb{R}\ \exists\,\varepsilon>0\ \forall\,N\in\mathbb{N}\ \exists\,n\in\mathbb{N}\ (n\ge N\ \wedge\ \lvert s_n-L\rvert\ge\varepsilon).
> >   $$
> >   This says: **no matter which real $L$ you pick**, there is an $\varepsilon>0$ such that **beyond every $N$** you can find an index $n\ge N$ with the term **staying at least $\varepsilon$ away** from $L$.
