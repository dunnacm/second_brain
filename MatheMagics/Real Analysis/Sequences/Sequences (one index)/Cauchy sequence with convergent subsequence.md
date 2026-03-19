---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Cauchy Sequence with a Convergent Subsequence**
> > [!warning]+ **IF**
> > - $\{s_n\}$ is Cauchy,  
> > - $\displaystyle \lim_{n\to\infty}\{\,s_{k_n}\,\}=L$,
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\{s_n\}
> > \;=\;
> > \lim_{n\to\infty}\{\,s_{k_n}\,\}
> > \;=\; L.
> > $$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\{s_{k_n}\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,k_n\ge N_1 \Rightarrow |s_{k_n}-L|<\varepsilon\,]
\\[8pt]
(2)\quad 
&\{s_n\}\ \text{is Cauchy}
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall m,n\in\mathbb{N}\,[\,m\ge N_2 \wedge n\ge N_2 \Rightarrow |s_m-s_n|<\varepsilon\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$; **EI** on $N_1,N_2$; and **UI** on $m,n$ in (1), (2):

$$
\begin{aligned}
(3)\quad 
&\lim_{n\to\infty}\{s_{k_n}\}=L\ \Leftrightarrow\ k_n\ge N_1 \Rightarrow |s_{k_n}-L|<\varepsilon\\[4pt]
(4)\quad 
&\{s_n\}\ \text{is Cauchy}\ \Leftrightarrow\ m\ge N_2 \wedge n\ge N_2 \Rightarrow |s_m-s_n|<\varepsilon.
\end{aligned}
$$

Applying the **Common–$N$ lemma** to (3), (4); i.e., set $N:=\max\{N_1,N_2\}$:

$$
\begin{aligned}
(3')\quad 
&\lim_{n\to\infty}\{s_{k_n}\}=L
\ \Leftrightarrow\
\big[\,k_n\ge N \Rightarrow |s_{k_n}-L|<\dfrac{\varepsilon}{2}\,\big]
\\[6pt]
&\lim_{n\to\infty}\{s_{k_n}\}=L
\ \Leftrightarrow\
\big[\,k_n\ge N \Rightarrow |s_{k_n}-L|+\dfrac{\varepsilon}{2}<\varepsilon\,\big]
\\[10pt]
(4')\quad 
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ (m\ge N \wedge n\ge N) \Rightarrow |s_m-s_n|<\varepsilon\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ (m\ge N \wedge n\ge N) \Rightarrow |s_m-s_n|<\dfrac{\varepsilon}{2}
&&\text{(simpl.)}\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ (n\ge N \wedge k_n\ge N) \Rightarrow |s_n-s_{k_n}|<\dfrac{\varepsilon}{2}
&&\text{(replace $m:=n$, $n:=k_n$)}\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ n\ge N \Rightarrow |s_n-s_{k_n}|<\dfrac{\varepsilon}{2}
&&\text{(sub.\ from (3') last consequent)}\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ n\ge N \Rightarrow 
|s_n-L|<|s_n-s_{k_n}|+|s_{k_n}-L|<\dfrac{\varepsilon}{2}+\dfrac{\varepsilon}{2}
&&\text{(by transitivity)}\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ n\ge N \Rightarrow 
|s_n-L|<|s_n-s_{k_n}|+|s_{k_n}-L|<\varepsilon
&&\text{(by triangle inequality)}\\[4pt]
&\{s_n\}\ \text{is Cauchy}\ \Rightarrow\ n\ge N \Rightarrow |s_n-L|<\varepsilon.
\end{aligned}
$$

From the definition of subsequence: (5) $k_{n+1}>k_n,\ \forall n\in\mathbb{N}$.

Two consequences from (5) (eqs.\,(6), (7)):

$$
\begin{aligned}
(6)\quad &k_n\ge n \Rightarrow k_n\ge N \qquad (A\Rightarrow B)\\[2pt]
(7)\quad &n\ge N \Rightarrow k_n\ge k_N \qquad (C\Rightarrow D)
\end{aligned}
$$

Combining (6), (7)\; (i.e., $a\wedge c \Rightarrow b\wedge d$):

$$
\begin{aligned}
(8)\quad 
&k_n\ge n \wedge n\ge N \Rightarrow k_n\ge N \wedge k_n\ge k_N\\
&k_n\ge n \wedge n\ge N \Rightarrow k_n\ge k_n \wedge k_n\ge N
&&\text{(applying transitivity)}\\
&k_n\ge n \wedge n\ge N \Rightarrow k_n\ge N
&&\text{(simpl.)}\\
&n\ge N \Rightarrow k_n\ge N.
\end{aligned}
$$

From (4') last line and (8) last line (in propositional-logic terms).  
By propositional logic:
$$
\begin{aligned}
(9)\quad (A\Rightarrow B)\wedge(C\Rightarrow A)\ \Rightarrow\ (C\Rightarrow B).
\end{aligned}
$$

Turning terms in (9) back from propositional variables:
$$
\begin{aligned}
(10)\quad 
&[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,],\ [\,n\ge N \Rightarrow k_n\ge N\,]\ \vDash\ [\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,].
\end{aligned}
$$

From the conclusion of (10):
$$
\begin{aligned}
(11)\quad &n\ge N \Rightarrow |s_n-L|<\varepsilon.
\end{aligned}
$$

Applying **UG** on $\varepsilon$, **EI** on $N$, and **UI** on $n$ in (11):

$$
\begin{aligned}
(12)\quad 
&\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}\{s_n\}=L.
\end{aligned}
$$
