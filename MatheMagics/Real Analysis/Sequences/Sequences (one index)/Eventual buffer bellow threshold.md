---
down:
  - "[[Lemmas, half thresholds]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
- If a sequence converges to a limit $L$ that is **strictly less** than a number $c$, then **from some index $N$ onward** every term of the sequence is **strictly below** a constant $k$ with $k<c$.

- A concrete choice is the midpoint $k=\frac{L+c}{2}\quad\text{so}\quad L<k<c.$ By convergence, there exists $N$ such that for all $n\ge N$, $|s_n-L|<\frac{c-L}{2}\ \Longrightarrow\ s_n<k.$ Thus the **tail** of the sequence lies entirely in $(-\infty,k)$.

- Intuition: convergence below $c$ forces **eventual one-sided behavior**—once the terms are close to $L$, there isn’t room to cross back above $c$. The sequence not only stays below $c$; it stays below a fixed margin $k<c$ forever after.

- Symmetry with the “above-threshold” case: if $L>c$, then eventually $s_n>k>c$ (e.g., pick $k=\tfrac{L+c}{2}$).
### Formal definition:

> [!note]+ **Lemma 2 — Eventual buffer below a threshold**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty} s_n=L$ with $L<c$ and $c\in\mathbb{R}$.
>
> > [!tip]+ **THEN**
> > $\displaystyle \exists N\in\mathbb{N}\ \exists k,c\in\mathbb{R}\ \forall n\in\mathbb{N}\,\big[\,n\ge N \Rightarrow s_n<k<c\,\big]$.

## Proof
Assume $L<c$ and $\displaystyle \lim_{n\to\infty}\{s_n\}=L$.

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$ and **UI** on $n$ in eq. (1), sequentially:

$$
\begin{aligned}
&(2)\quad n\ge N_{\varepsilon}(L) \Rightarrow |s_n-L|<\varepsilon\\
&\qquad \, \, n\ge N_{\varepsilon}(L) \Rightarrow -\varepsilon<s_n-L<\varepsilon\\
&\qquad \, \, n\ge N_{\varepsilon}(L) \Rightarrow L-\varepsilon<s_n<\varepsilon+L
\end{aligned}
$$

Informed by eq. (2), choose $k:=L+\hat{\varepsilon}$, where $\hat{\varepsilon}$ is the chosen witness.

Assumption:
$$
(3)\quad k<c \ \Longleftrightarrow\ k:=L+\hat{\varepsilon}<c.
$$

Sub. eq. (3) into eq. (2):

$$
\begin{aligned}
&(4)\quad  n\ge N_{\hat{\varepsilon}}(L)\ \Rightarrow\ L-\hat{\varepsilon}<s_n<\hat{\varepsilon}+L\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow\ L-\hat{\varepsilon}<s_n<k\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow\ L-\hat{\varepsilon}<s_n<k\ <c \ \ \ (\text{applying simpl})\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow\ L-\hat{\varepsilon}  < s_n \ \wedge\ s_n<k<c \\ 
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow\ L-\hat{\varepsilon}  < s_n
\end{aligned}
$$

Applying **UG** on $n$ and **EG** on $k$ and $N$ to eq. (4), sequentially:

$$
\begin{aligned}
&(5)\quad \lim_{n\to\infty}s_n=L \ \Rightarrow\ \exists N\in\mathbb{N}\ \exists k\in\mathbb{R}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow s_n<k<c\,].
\end{aligned}
$$
