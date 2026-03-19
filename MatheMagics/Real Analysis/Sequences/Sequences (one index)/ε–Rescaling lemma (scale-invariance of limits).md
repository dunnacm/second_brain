---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **ε–Rescaling Lemma (scale-invariance of limits)**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty} s_n = L \ \Leftrightarrow\  \forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]$
>
> > [!tip]+ **THEN**
> > $$
> >   \forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|< c\,\varepsilon\,], \, \text{c>0 is fixed}.
> >   $$
## Proof:
Assumption:

$$
\begin{aligned}
&(1)\quad \forall\,\varepsilon>0\ \exists\,N\in\mathbb{N}\ \forall\,n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<c\,\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$, and UI on $n$ to (1), sequentially:

$$
\begin{aligned}
&(2)\quad n\ge N \Rightarrow |s_n-L|<c\,\varepsilon.
\end{aligned}
$$

Choose $\varepsilon' := c\,\varepsilon$ (so $\varepsilon=\varepsilon'/c$). Substitute into (2):

$$
\begin{aligned}
&(2')\quad n\ge N \Rightarrow |s_n-L|<c\cdot\frac{\varepsilon'}{c}\\[6pt]
&\qquad \, \, \, n\ge N \Rightarrow |s_n-L|<\varepsilon'.
\end{aligned}
$$

Applying UG on $n$, EG on $N$, and UG on $\varepsilon'$ to (2′), sequentially:

$$
\begin{aligned}
&(3)\quad \forall\,\varepsilon'>0\ \exists\,N\in\mathbb{N}\ \forall\,n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon'\,]
\ \Leftrightarrow\ 
\lim_{n\to\infty} s_n = L.
\end{aligned}
$$
