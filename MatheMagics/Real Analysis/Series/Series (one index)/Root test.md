---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

### Formal definition, 1st. case:

> [!note]+ **Root test — convergence**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\displaystyle \lim_{n\to\infty}\sqrt[n]{\lvert a_n\rvert}=L<1.$
>
> > [!tip]+ **THEN**
> > $$S\ \text{is absolutely convergent (hence convergent).}$$
### Formal definition, 2nd. case:

> [!note]+ **Root test — divergence**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\displaystyle \lim_{n\to\infty}\sqrt[n]{\lvert a_n\rvert}=L>1\quad \text{or}\quad \lim_{n\to\infty}\sqrt[n]{\lvert a_n\rvert}=\infty.$
>
> > [!tip]+ **THEN**
> > $$S\ \text{is divergent.}$$
### Formal definition, 3rd. case:

> [!note]+ **Root test — inconclusive case**
>
> > [!warning]+ **IF**
> > - $S=\sum_{n=1}^{\infty} a_n,$
> > - $\displaystyle \lim_{n\to\infty}\sqrt[n]{\lvert a_n\rvert}=1.$
>
> > [!tip]+ **THEN**
> > *No conclusion* about convergence or divergence can be drawn from the ratio test.
> 
> ---
> If **convergent** the series would be **conditionally convergent**