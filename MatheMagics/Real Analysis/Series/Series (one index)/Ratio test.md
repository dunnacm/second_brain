---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Formal definition, 1st. case:

> [!note]+ **Ratio test — convergence**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1.$
>
> > [!tip]+ **THEN**
> > $$S\ \text{is absolutely convergent (hence convergent).}$$
### Formal definition, 2nd. case:

> [!note]+ **Ratio test — divergence**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1\quad \text{or}\quad \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty.$
>
> > [!tip]+ **THEN**
> > $$S\ \text{is divergent.}$$
### Formal definition, 3rd. case:

> [!note]+ **Ratio test — inconclusive case**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1.$
>
> > [!tip]+ **THEN**
> > *No conclusion* about convergence or divergence can be drawn from the ratio test.
> 
> ---
> If **convergent** the series would be **conditionally convergent**

Let $\sum a_n$ be a series with positive terms and let $r_n = \dfrac{a_{n+1}}{a_n}$.
Suppose that $\lim_{n\to\infty} r_n = L < 1$, so $\sum a_n$ converges by the
Ratio Test. As usual, we let $R_n$ be the remainder after $n$ terms,
that is,

$$
R_n = a_{n+1} + a_{n+2} + a_{n+3} + \cdots
$$

(a) If $\{r_n\}$ is a decreasing sequence and $r_{n+1} < 1$, show, by
summing a geometric series, that

$$
R_n \le \dfrac{a_{n+1}}{1 - r_{n+1}}
$$

(b) If $\{r_n\}$ is an increasing sequence, show that

$$
R_n \le \dfrac{a_{n+1}}{1 - L}
$$
