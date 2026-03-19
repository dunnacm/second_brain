---
down:
  - "[[Absolute value preserves limits]]"
  - "[[Product with a bounded sequence]]"
  - "[[Cauchy ⇒ Bounded]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Convergence ⇒ Boundedness**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}s_n=L$ (i.e., $\{s_n\}$ is convergent).
>
> > [!tip]+ **THEN**
> > $\{s_n\}$ is **bounded**; (i.e., $\exists\,M>0\ \forall n\in\mathbb{N}:\ |s_n|\le M$).
>---
> > [!note]+ **Notes**
> > - The **converse is false**: a bounded sequence need not converge.  
> >   Examples: $\{(-1)^n\}$, and $\{\sin n\}$ are both bounded but do not converge.
> > - Useful relations:  
> >  > - Convergent $\Rightarrow$ Cauchy $\Rightarrow$ bounded.  
> >  > - Bounded **and** monotone $\Rightarrow$ convergent (Monotone Convergence Theorem).
## Proof:
Assumption:

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,].
\end{aligned}
$$

Apply **UI** on $\varepsilon$ with the specific example (witness) $\hat{\varepsilon}$; then by **EI** obtain $N(\hat{\varepsilon})\in\mathbb{N}$; finally apply **UI** on $n$ to (1), sequentially.

$$
\begin{aligned}
&(2)\quad n\ge N \Rightarrow |s_n-L|<\varepsilon
\qquad\text{(inverse triangle inequality: }||x|-|y||\le|x-y|\text{)}
\\[6pt]
&\qquad \, n\ge N \Rightarrow \big||s_n|-|L|\big|\le |s_n-L|<\varepsilon\\
&\qquad \, n\ge N \Rightarrow \big||s_n|-|L|\big|\le \varepsilon\\
&\qquad \, n\ge N \Rightarrow -\varepsilon \le |s_n|-|L| \le \varepsilon\\
&\qquad \, n\ge N \Rightarrow |L|-\varepsilon \le |s_n| \le |L|+\varepsilon\\
&\qquad \, n\ge N(\hat{\varepsilon}) \Rightarrow |L|-\hat{\varepsilon} \le |s_n| \le |L|+\hat{\varepsilon}.
\end{aligned}
$$
![[convergence_sketch_clean_v3.png]]
Define a global bound
$$
M \;:=\; \max\{\,|s_1|,\ |s_2|,\ \dots,\ |s_{\,N(\hat{\varepsilon})-1}|,\ |L|+\hat{\varepsilon}\,\}.
$$

Then
$$
\begin{aligned}
&(2'')\quad n\ge N(\hat{\varepsilon}) \Rightarrow |s_n|\le |L|+\hat{\varepsilon} \le M,\\[4pt]
&\qquad \, \, \, \, n< N(\hat{\varepsilon}) \Rightarrow |s_n|\le M \quad\text{(by the definition of $M$).}
\end{aligned}
$$

Applying **UG** on $n$ and **EG** on $N$ and $M$:

$$
\begin{aligned}
&(3)\quad \exists M\in\mathbb{R^{+}}\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n|\le M\,].
\end{aligned}
$$

Therefore,
$$
\begin{aligned}
&(4)\quad \lim_{n\to\infty}\{s_n\}=L\ \Rightarrow\ \exists M\in\mathbb{R^{+}}\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n|\le M\,].
\end{aligned}
$$
