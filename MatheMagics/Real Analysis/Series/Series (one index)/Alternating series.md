---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Alternating series test (Leibniz)**
>
> > [!warning]+ **IF**
> > - $S=\displaystyle\sum_{n=1}^{\infty}s_n=\sum_{n=1}^{\infty}(-1)^{\,n-1}\,t_n$  
> > - $t_n\ge 0$ for all $n\in\mathbb{N}$ (i.e., **positive**)  
> > - $t_{n+1}\le t_n$ for all $n\in\mathbb{N}$ (i.e., **decreasing**)  
> > - $\displaystyle\lim_{n\to\infty} t_n=0$  
>
> > [!tip]+ **THEN**
> > $S$ is **convergent**.  
> > 
> ---
>   - *(Moreover: if $\sum t_n$ diverges, then $S$ is only **conditionally** convergent.)*
>   - Remainder: 
>   $$
>    R_n:=S-S_n,\ \ S_n:=\sum_{k=1}^{n}s_k.
>  $$
>  
>   $$
>   \lvert R_n\rvert \ \le\ t_{n+1}
>   $$
>   
>    $$
> \lvert S - S_n\rvert \ \le\ t_{n+1}
> \quad \Leftrightarrow \quad
>S_n - t_{n+1}\ \le\ S\ \le\ S_n + t_{n+1}
>  $$
>  
>  $$
> \left\lvert \sum_{k=n+1}^{\infty} s_k \right\rvert \ \le\ t_{n+1}
> $$

### Proof 






