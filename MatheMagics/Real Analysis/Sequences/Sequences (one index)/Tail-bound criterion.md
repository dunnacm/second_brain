---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal:
If every tail of the sequence is uniformly close to its first term $s_N$, then any two tail terms are close to each other, hence the sequence is Cauchy
### Formal:

> [!note]+ **Tail–Bound Criterion ⇒ Cauchy**
> > [!warning]+ **IFF**
> > $$\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\ \big[\,n\ge N \Rightarrow |s_n-s_N|<\varepsilon\,\big],$$
>
> > [!tip]+ **THEN**
> > $$\{s_n\}\ \text{is Cauchy.}$$

## Proof:
### Sufficiency: 
### Necessity:
$$
\begin{aligned}
\text{Assume }\{s_n\}\text{ is Cauchy}\quad
&\Leftrightarrow\quad
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall m,n\in\mathbb{N}\,
[\,m\ge N\wedge n\ge N \Rightarrow |s_m-s_n|<\varepsilon\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$ with the substitution $m:=N$:
$$
\begin{aligned}
n\ge N \Rightarrow |s_n-s_N|<\varepsilon.
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$:
$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-s_N|<\varepsilon\,].
$$



