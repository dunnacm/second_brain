---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Scalar Multiple Rule for Limits (Sequences)**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}\{s_n\}=L$ with fixed $c\in\mathbb{R}$.
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\big(c\cdot\{s_n\}\big)=c\,L.
> > $$
## Proof

> [!abstract]+ **Proof outline — Scalar Multiple Rule**
>
> 1) Split cases:  
>    • If $c=0$, then $c\,s_n\equiv 0$ so the limit is $0=cL$.  
>    • If $c\neq 0$, proceed below.
>
> 2) **UI** on $\varepsilon$: use $\varepsilon/|c|$ inside the limit definition for $\{s_n\}$.
>
> 3) **EI** to get $N$ and **UI** on $n$: for all $n\ge N$, have $|s_n-L|<\varepsilon/|c|$.
>
> 4) Multiply by $|c|$ (positive): obtain $|c\,s_n-c\,L|<\varepsilon$.
>
> 5) **UG** on $n$, **EG** on $N$, **UG** on $\varepsilon$: conclude $\lim (c\,s_n)=c\,L$.
>---
> **Key ingredients:** built-in $\varepsilon/|c|$ device, positivity of $|c|$, and the **UI/EI/UG** flow.

*Trivial case.* If $c=0$, then $c\,s_n\equiv 0$ and $\displaystyle\lim_{n\to\infty}(c\,s_n)=0=cL$.

*Assume now $c\neq 0$.*

Assumption (already choosing the usual **UI** substitution $\varepsilon\mapsto \varepsilon/|c|$ inside the definition):

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N \Rightarrow \big|s_n-L\big|<\dfrac{\varepsilon}{|c|}\,\Big].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$ to (1), sequentially:

$$
\begin{aligned}
(2)\quad n\ge N\ 
&\Rightarrow\ \big|s_n-L\big|<\dfrac{\varepsilon}{|c|}
&&\text{(from (1))}
\\
&\Rightarrow\ |c|\cdot\big|s_n-L\big|<\varepsilon
&&\text{(multiply both sides by $|c|>0$)}
\\
&\Rightarrow\ \big|c\,s_n-c\,L\big|<\varepsilon
&&\text{(since $|c|\cdot|x|=|cx|$).}
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to (2), sequentially:

$$
\begin{aligned}
&(3)\quad
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\big[\,n\ge N \Rightarrow |c\,s_n-c\,L|<\varepsilon\,\big]
\ \Leftrightarrow\
\lim_{n\to\infty}(c\,s_n)=c\,L.
\end{aligned}
$$
