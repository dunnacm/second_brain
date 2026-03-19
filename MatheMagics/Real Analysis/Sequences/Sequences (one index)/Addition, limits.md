---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Sum Rule for Limits (Sequences)**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}\{s_n\}=K \quad\wedge\quad \lim_{n\to\infty}\{t_n\}=L$.
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\big(\{s_n\}+\{t_n\}\big)=K+L.
> > $$
## Proof:
> [!abstract]+ **Proof outline — Sum Rule for Limits (Sequences)**
>
> 1) Start with hypotheses:
>    - $\displaystyle \lim_{n\to\infty}\{s_n\}=K$ and $\displaystyle \lim_{n\to\infty}\{t_n\}=L$.
>
> 2) **UI** on $\varepsilon$: fix an arbitrary $\varepsilon>0$ and split it via the $\varepsilon/2$ trick.
>
> 3) From each limit:
>    - **EI** to get $N_1$ with $n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2}$.
>    - **EI** to get $N_2$ with $n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}$.
>
> 4) Choose a common index using the Common–$N$ lemma:
>    - $N_\varepsilon(K,L):=\max\{N_1,N_2\}$.
>
> 5) For all $n\ge N_\varepsilon(K,L)$ apply the triangle inequality:
>
> $$
> \big|(s_n+t_n)-(K+L)\big|
> \;\le\;
> |s_n-K|+|t_n-L|
> \;<\;
> \dfrac{\varepsilon}{2}+\dfrac{\varepsilon}{2}
> \;=\;\varepsilon.
> $$
>
> 6) **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$:
>    - Conclude $\displaystyle \lim_{n\to\infty}(s_n+t_n)=K+L$.
>---
> **Key ingredients:** $\varepsilon/2$ device, Common–$N$ lemma, triangle inequality, and **UI/EI/UG/EG** flow.

Assume $\displaystyle \lim_{n\to\infty}\{s_n\}=K$ and $\displaystyle \lim_{n\to\infty}\{t_n\}=L$.

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=K
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2}\,].
\\[6pt]
&(2)\quad \lim_{n\to\infty}\{t_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N_1$ and $N_2$, and **UI** on $n$ in eqs. (1) and (2), sequentially:

$$
\begin{aligned}
&(3)\quad n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2},\\
&(4)\quad n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}.
\end{aligned}
$$

Informed by (3),(4), choose the common index
$$
N_{\varepsilon}(K,L):=\max\{N_1,N_2\}\qquad\text{(see Common–$N$ lemma).}
$$

Substitute $N_{\varepsilon}(K,L)$ in (3),(4):

$$
\begin{aligned}
&(3')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2},\\
&(4')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}.
\end{aligned}
$$

From the consequent of (4'):

$$
\begin{aligned}
&(5)\quad |t_n-L|<\dfrac{\varepsilon}{2}\ \Rightarrow\ |t_n-L|+\dfrac{\varepsilon}{2}<\varepsilon.
\end{aligned}
$$

From (4') and then (3'):

$$
\begin{aligned}
(6)\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow\ |s_n-K|<\dfrac{\varepsilon}{2} 
&&\text{(from (3'))}
\\
&\Rightarrow\ |s_n-K|+|t_n-L|
     < \dfrac{\varepsilon}{2} + |t_n-L|
&&\text{(add $|t_n-L|$ to both sides)}
\\
&\Rightarrow\ |s_n-K|+|t_n-L|
     < \varepsilon
&&\text{(use (5): $|t_n-L|+\dfrac{\varepsilon}{2}<\varepsilon$)}
\\
&\Rightarrow\ \big|(s_n+t_n)-(K+L)\big|
     \le |s_n-K|+|t_n-L|<\varepsilon
&&\text{(triangle inequality on the LHS).}
\end{aligned}
$$


Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to the last line, sequentially:

$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow
\big|(s_n+t_n)-(K+L)\big|<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}(s_n+t_n)=K+L.
$$



