---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Formal definition, 1st case

> [!note]+ **Absolute convergence ⇒ convergence**
>> [!warning]+ **IF**  
>> • $S^{(1)}=\sum_{n=1}^{\infty} s_n$  
>> • $S^{(2)}=\sum_{n=1}^{\infty} t_n=\sum_{n=1}^{\infty}\lvert s_n\rvert$  
>> • $S^{(2)}$ **converges**
>
>
>> [!tip]+ **THEN**  
>> • $S^{(1)}$ is **absolutely convergent**, hence **convergent**.
>
> ---
> If $S^{(1)}$ is **absolutely convergent** with sum $S$, then **every rearrangement** of $S^{(1)}$ has the same sum $S$.
### Formal definition, 2nd case

> [!note]+ **When $\sum\lvert s_n\rvert$ diverges (no absolute convergence)**
>> [!warning]+ **IF**  
>> • $S^{(1)}=\sum_{n=1}^{\infty} s_n$  
>> • $S^{(2)}=\sum_{n=1}^{\infty} t_n=\sum_{n=1}^{\infty}\lvert s_n\rvert$  
>> • $S^{(2)}$ **diverges**
>
>
>> [!tip]+ **THEN**  
>> Exactly one of the following holds:  
>> &emsp;– **Conditional convergence:** $S^{(1)}$ converges but $\sum\lvert s_n\rvert$ diverges.  
>> &emsp;– **Divergence:** $S^{(1)}$ diverges.
>
> ---
> (**Riemann Rearrangement Theorem, real series**) If $S^{(1)}$ is **conditionally convergent**, then for every $r\in\mathbb{R}$ there exists a **rearrangement** of $S^{(1)}$ whose sum is $r$; there are also rearrangements that diverge to $+\infty$, to $-\infty$, or diverge without a limit.
