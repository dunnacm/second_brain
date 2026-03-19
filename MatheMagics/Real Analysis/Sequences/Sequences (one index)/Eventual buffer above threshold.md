---
down:
  - "[[Lemmas, half thresholds]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
- If a sequence converges to a limit $L$ that is **strictly larger** than a constant $c$, then **from some index $N$ onward** all its terms stay **above** a number $k$ with $k>c$.
	- Intuition: once you go far enough into the sequence, it never dips back below a fixed buffer above $c$.

- A concrete “buffer” you can pick is the midpoint $k=\frac{L+c}{2}\quad\text{with}\quad c<k<L.$ By convergence, there exists $N$ such that for every $n\ge N$, $|s_n-L|<\tfrac{L-c}{2}\ \Longrightarrow\ s_n>k.$ So the **tail** of the sequence lies entirely in $(k,\infty)$, safely above $c$.

- Big picture: convergence doesn’t only mean “terms get close to $L$”; it also gives **eventual one-sided behavior** relative to any strict threshold below $L$. Once close enough to $L$, there’s no room left to cross back below $c$.

- Symmetry: if $L<c$, the same reasoning shows that **eventually** $s_n<k<c$ (e.g., take $k=\tfrac{L+c}{2}$), so the tail stays strictly **below** $c$. This is often called a **tail bound** or **eventual separation** from the threshold.

### Formal definition:

> [!note]+ **Lemma 1 — Eventual buffer above a threshold**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty} s_n=L$ with $L>c\in\mathbb{R}$.
>
> > [!tip]+ **THEN**
> > $\displaystyle \exists N\in\mathbb{N}\ \exists k,c\in\mathbb{R}\ \forall n\in\mathbb{N}\,\big[\,n\ge N \Rightarrow s_n>k>c\,\big]$.

## Proof 
Assumption:

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

Informed by eq. (2), choose $k:=L-\hat{\varepsilon}$, where $\hat{\varepsilon}$ is the chosen witness.

Assumption:
$$
(3)\quad k>c \ \Longleftrightarrow\ k:=L-\hat{\varepsilon}>c.
$$

Sub. eq. (3) into eq. (2):

$$
\begin{aligned}
&(4)\quad  n\ge N_{\hat{\varepsilon}}(L)\ \Rightarrow\ L-\hat{\varepsilon}<s_n<\hat{\varepsilon}+L\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow k<s_n<\hat{\varepsilon}+L\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow c<k<s_n<\hat{\varepsilon}+L \ \ (\text{applying simpl})\\
&\qquad \, \, n\ge N_{\hat{\varepsilon}}(L) \Rightarrow c<k<s_n
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $k$, and **EG** on $N$ to eq. (4), sequentially:

$$
\begin{aligned}
&(5)\quad \lim_{n\to\infty}s_n=L \ \Rightarrow\ \exists N\in\mathbb{N}\ \exists k\in\mathbb{R}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow c<k<s_n\,].
\end{aligned}
$$