---
down:
  - "[[Product with a bounded sequence]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Product Rule for Limits (Sequences)**
>
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=K$
> > - $\displaystyle \lim_{n\to\infty}\{t_n\}=L$
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\big(\{s_n\}\cdot\{t_n\}\big)=K\cdot L.
> > $$
## Proof:

> [!abstract]+ **Proof outline — Product Rule for Limits (Sequences)**
>
> 1) **Start with limits and a global bound.**  
>    - Hypotheses: $\displaystyle \lim s_n=K$, $\displaystyle \lim t_n=L$.  
>    - Fix $\varepsilon>0$ and choose a bound $M$ for $\{s_n\}$ (from convergence):  
>      $|s_n|\le M:=\max\{\,|s_1|,\dots,|s_{N_1-1}|,\ |K|+\varepsilon\,\}$.
>
> 2) **UI/EI on each limit with the same target precision.**  
>    - From $\lim s_n=K$: **EI** $N_1$ s.t. for $n\ge N_1$, $|s_n-K|<\dfrac{\varepsilon}{M+|L|}$.  
>    - From $\lim t_n=L$: **EI** $N_2$ s.t. for $n\ge N_2$, $|t_n-L|<\dfrac{\varepsilon}{M+|L|}$.
>
> 3) **Common–$N$ selection.**  
>    - Set $N_\varepsilon(K,L):=\max\{N_1,N_2\}$ so both estimates hold for $n\ge N_\varepsilon(K,L)$.
>
> 4) **Prepare the product split.**  
>    - Use the identity
> $$
> s_n t_n - KL=(s_n-K)L+(t_n-L)s_n.
> $$
>
> 5) **Bound each term separately using the chosen precision and $M$.**  
>    - From $|s_n-K|<\dfrac{\varepsilon}{M+|L|}$ get
>      $|s_n-K|\cdot|L|<\dfrac{\varepsilon}{M+|L|}\,|L|$.  
>    - From $|t_n-L|<\dfrac{\varepsilon}{M+|L|}$ and $|s_n|\le M$ get
>      $|t_n-L|\cdot|s_n|<\dfrac{\varepsilon}{M+|L|}\,M$.
>
> 6) **Add the two bounds and apply the triangle inequality.**  
>    - Triangle inequality on the split gives
> $$
> |s_nt_n-KL|
> \le |s_n-K|\,|L|+|t_n-L|\,|s_n|
> < \varepsilon\,\frac{|L|+M}{M+|L|}
> = \varepsilon.
> $$
>
> 7) **Quantifier wrap-up.**  
>    - **UG** on $n$, **EG** on $N$, **UG** on $\varepsilon$:
>      $\forall\varepsilon>0\,\exists N\,\forall n\ge N:\ |s_nt_n-KL|<\varepsilon$, i.e.  
>      $\displaystyle \lim_{n\to\infty}(s_n t_n)=KL$.
>
> **Key ingredients:** global bound $M$ for $\{s_n\}$, Common–$N$ lemma, product-splitting identity, triangle inequality, and the **UI/EI/UG/EG** flow.

**Let** $M$ be a global bound for $\{s_n\}$; for the fixed $\varepsilon>0$ we may take  
$|s_n|<M:=\max\{\,|s_1|,|s_2|,\dots,|s_{N_1-1}|,\ |K|+\varepsilon\,\}$.

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=K
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{\,M+|L|\,}\,\Big].
\\[6pt]
&(2)\quad \lim_{n\to\infty}\{t_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{\,M+|L|\,}\,\Big].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N_1$ and $N_2$, and **UI** on $n$ in (1)–(2), sequentially:
$$
\begin{aligned}
&(3)\quad n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{\,M+|L|\,},\\
&(4)\quad n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{\,M+|L|\,}.
\end{aligned}
$$

Choose the common index
$$
N_{\varepsilon}(K,L):=\max\{N_1,N_2\}.
$$

Substitute $N_{\varepsilon}(K,L)$ in (3),(4):
$$
\begin{aligned}
&(3')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |s_n-K|<\dfrac{\varepsilon}{\,M+|L|\,},\\
&(4')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |t_n-L|<\dfrac{\varepsilon}{\,M+|L|\,}.
\end{aligned}
$$

From (4'):
$$
\begin{aligned}
(4'')\quad n\ge N_{\varepsilon}(K,L)\
&\Rightarrow\ |t_n-L|<\dfrac{\varepsilon}{\,M+|L|\,}
\\
&\Rightarrow\ |t_n-L|\cdot|s_n|<\dfrac{\varepsilon}{\,M+|L|\,}\cdot|s_n|
\\
&\Rightarrow\ |t_n-L|\cdot|s_n|<\dfrac{\varepsilon}{\,M+|L|\,}\cdot M
\qquad\text{(since $|s_n|<M$).}
\end{aligned}
$$

From (3'):
$$
\begin{aligned}
&(3'')\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow&\ |s_n-K|<\dfrac{\varepsilon}{\,M+|L|\,}
&&\text{(from (3'))}
\\
&&\Rightarrow&\ |s_n-K|\cdot|L|
   <\dfrac{\varepsilon}{\,M+|L|\,}\cdot|L|
\\
&&\Rightarrow&\ |s_n-K|\cdot|L|+|t_n-L|\cdot|s_n|
   <\dfrac{\varepsilon}{\,M+|L|\,}\cdot|L|
    +|t_n-L|\cdot|s_n|
&&\text{(add $|t_n-L||s_n|$)}
\\
&&\Rightarrow&\ |s_n-K|\cdot|L|+|t_n-L|\cdot|s_n|
   <\dfrac{\varepsilon}{\,M+|L|\,}\cdot|L|
    +\dfrac{\varepsilon}{\,M+|L|\,}\cdot M
&&\text{(use (4''): $|t_n-L||s_n|<\tfrac{\varepsilon}{M+|L|}M$)}
\\
&&\Rightarrow&\ |s_n-K|\cdot|L|+|t_n-L|\cdot|s_n|
   <\varepsilon\,\dfrac{|L|+M}{\,M+|L|\,}
\\
&&\Rightarrow&\ |s_n-K|\cdot|L|+|t_n-L|\cdot|s_n|<\varepsilon
\\
&&\Rightarrow&\ \big|\,(s_n-K)L+(t_n-L)s_n\,\big|
   \le |s_n-K|\cdot|L|+|t_n-L|\cdot|s_n|
&&\text{(triangle inequality)}
\\
&&\Rightarrow&\ \big|\,(s_n-K)L+(t_n-L)s_n\,\big|<\varepsilon
\\
&&\Rightarrow&\ |s_nt_n-KL|<\varepsilon.
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to the last line, sequentially:
$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\big[\,n\ge N \Rightarrow |s_n t_n - K L|<\varepsilon\,\big]
\ \Leftrightarrow\
\lim_{n\to\infty}(s_n t_n)=K L.\ \blacksquare
$$
