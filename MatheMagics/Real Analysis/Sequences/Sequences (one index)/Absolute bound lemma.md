---
down:
  - "[[Convergence ⇒ Boundedness]]"
  - "[[Product with a bounded sequence]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
- Think of $\lvert s_n\rvert$ as the **distance** from $s_n$ to $0$ on the number line.  
- If there is a single number $M>0$ with $\lvert s_n\rvert\le M$ for **every** $n$, then **every term** of the sequence lies within the interval
  $$
  -M \le s_n \le M,
  $$
  i.e., inside the “fence” of height $M$ around $0$.  
- That’s exactly what **bounded** means: all the terms fit inside some finite window. Formally, a sequence is bounded if $\exists A,B\in\mathbb{R}$ such that $A\le s_n\le B$ for all $n$.  
  From $\lvert s_n\rvert\le M$ we can simply take $A=-M$ and $B=M$.
- If you only know $\lvert s_n\rvert < M$ (strict), it’s still bounded—the same idea works with the open interval $(-M,M)$, or pick $A=-(M+1)$ and $B=M+1$ to make the bounds weak.
### Formal definition:
> [!note]+ **Absolute-Bound Lemma**
>
> > [!warning]+ **IF**
> > - $\{s_n\}$ is a real sequence, and  
> > - $\forall n\in\mathbb{N}$, $\ |s_n|\le (M > 0)$.
>
> > [!tip]+ **THEN**
> > $\{s_n\}$ is **bounded**.
