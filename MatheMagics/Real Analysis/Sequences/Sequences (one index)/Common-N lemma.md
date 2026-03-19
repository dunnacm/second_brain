---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
Each sequence comes with its own “enter-and-stay” threshold. Taking the larger threshold guarantees simultaneous control of both sequences from the same point onward. (For any finite family of convergent sequences, take the maximum of their individual thresholds.)
### Formal definition:

> [!note]+ **Common-N Lemma (joint tail for two convergent sequences)**
>
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{n\to\infty} s_n = K$, and  
> > - $\displaystyle \lim_{n\to\infty} t_n = L$.
>
> > [!tip]+ **THEN**
> > $$
> >   \forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,\big[\,n\ge N \Rightarrow (\,|s_n-K|<\varepsilon \ \wedge\ |t_n-L|<\varepsilon\,)\big].
> >   $$

## Proof:
### Outline:
- If $\lim s_n=K$ and $\lim t_n=L$, then for any fixed $\varepsilon>0$ there are indices $N_1,N_2$ such that
  $$
  n\ge N_1 \Rightarrow |s_n-K|<\varepsilon,\qquad
  n\ge N_2 \Rightarrow |t_n-L|<\varepsilon.
  $$
- Set the common index
  $$
  N:=\max\{N_1,N_2\}.
  $$
  Why the maximum? Because tails shrink as $N$ grows: if $n\ge N$ and $N\ge N_1$, then automatically $n\ge N_1$ (transitivity of $\ge$). So the tail $\{n\ge N\}$ is contained in both tails $\{n\ge N_1\}$ and $\{n\ge N_2\}$.
- Consequently,
  $$
  n\ge N \ \Rightarrow\ |s_n-K|<\varepsilon \ \text{and}\ |t_n-L|<\varepsilon.
  $$
### Derivation:
Assume

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=K
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |s_n-K|<\varepsilon\,].
\end{aligned}
$$

$$
\begin{aligned}
&(2)\quad \lim_{n\to\infty}\{t_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |t_n-L|<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$, and UI on $n$ to (1) and (2), sequentially:

$$
\begin{aligned}
&(3)\quad n\ge N_1 \Rightarrow |s_n-K|<\varepsilon
\end{aligned}
$$

$$
\begin{aligned}
&(4)\quad n\ge N_2 \Rightarrow |t_n-L|<\varepsilon
\end{aligned}
$$

Choose the common index
$$
N_\varepsilon := \max\{N_1,N_2\}.
$$

Substitute $N_\varepsilon$ in (3):

$$
\begin{aligned}
&(3')\quad n\ge N_1\ [\,N_\varepsilon=\max\{N_1,N_2\}\,]\ \Rightarrow\ |s_n-K|<\varepsilon\\[10pt]
&\qquad \, \, \, n\ge N_\varepsilon \Rightarrow |s_n-K|<\varepsilon
\end{aligned}
$$

Substitute $N_\varepsilon$ in (4) (since $n\ge N_\varepsilon$ and $N_\varepsilon\ge N_2$ imply $n\ge N_2$):

$$
\begin{aligned}
&(4')\quad n\ge N_2\ [\,N_\varepsilon=\max\{N_1,N_2\}\,]\ \Rightarrow\ |t_n-L|<\varepsilon\\[10pt]
&\qquad \, \, \, n\ge N_\varepsilon \Rightarrow |t_n-L|<\varepsilon
\end{aligned}
$$

From (3′) and (4′) simultaneously:

$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N} [ \ 
n\ge N \Rightarrow (\,|s_n-K|<\varepsilon\ \wedge\ |t_n-L|<\varepsilon\,)].
$$
