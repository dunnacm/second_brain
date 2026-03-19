---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Formal definition, 1st. case:

> [!note]+ **Integral test (oCPD) **
>
> > [!warning]+ **IF**
> > - $s_n\ge 0$ for all *n* in $\mathbb{N}$ (i.e., **positive**)
> > - $s_{n}$ **continuous**
> > - $s_{n+1}\le s_n$ for all large *n* (i.e., eventually **decreasing**)
> > - $\int_{N}^{\infty} s(x)\,dx$ **converges**
>
> > [!tip]+ **THEN**
> > $\sum_{n=N}^{\infty} s_n$ **converges**
> 
> ---
>  *Moreover (remainder bounds for $n\ge N$):*
>  $$S_n:=\sum_{k=1}^{n} s_k,\qquad S:=\sum_{k=1}^{\infty}s_k,\qquad R_n:=S-S_n.$$
>  $$\int_{n+1}^{\infty} s(x)\,dx \ \le\ R_n\ \le\ \int_{n}^{\infty} s(x)\,dx$$
>  $$\Leftrightarrow\quad \int_{n+1}^{\infty} s(x)\,dx \ \le\ \sum_{k=n+1}^{\infty} s_k \ \le\ \int_{n}^{\infty} s(x)\,dx$$
>  $$\Leftrightarrow\quad\int_{n+1}^{\infty} s(x)\,dx \ \le\ S - S_n \ \le\ \int_{n}^{\infty} s(x)\,dx$$
### Formal definition, 2nd. case:

> [!note]+ **Integral test (oCPD) **
>
> > [!warning]+ **IF**
> > - $s_n\ge 0$ for all *n* in $\mathbb{N}$ (i.e., **positive**)
> > - $s_{n}$ **continuous**
> > - $s_{n+1}\le s_n$ for all large *n* (i.e., eventually **decreasing**)
> > - $\int_{N}^{\infty} s(x)\,dx$ **diverges**
>
> > [!tip]+ **THEN**
> > $\sum_{n=N}^{\infty} s_n$ **diverges**
> 
> ---
>  *Moreover (remainder bounds for $n\ge N$):*
>  $$S_n:=\sum_{k=1}^{n} s_k,\qquad S:=\sum_{k=1}^{\infty}s_k,\qquad R_n:=S-S_n.$$
>  $$\int_{n+1}^{\infty} s(x)\,dx \ \le\ R_n\ \le\ \int_{n}^{\infty} s(x)\,dx$$
>  $$\Leftrightarrow\quad \int_{n+1}^{\infty} s(x)\,dx \ \le\ \sum_{k=n+1}^{\infty} s_k \ \le\ \int_{n}^{\infty} s(x)\,dx$$
>  $$\Leftrightarrow\quad\int_{n+1}^{\infty} s(x)\,dx \ \le\ S - S_n \ \le\ \int_{n}^{\infty} s(x)\,dx$$