---
down:
  - "[[Comparison-to-zero, lemma]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Order Preservation of Limits (Monotonicity)**
>
> > [!warning]+ **IF**
> > - $\displaystyle \lim_{n\to\infty}\{s_n\}=K$  
> > - $\displaystyle \lim_{n\to\infty}\{t_n\}=L$  
> > - $\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$.
>
> > [!tip]+ **THEN**
> > $$
> > K\;\le\;L.
> > $$

## Proofs:
### Approach 1:

> [!abstract]+ **Proof outline — Order Preservation**
>
> 1) Argue by contradiction: assume $K>L$.
> 2) Let $\varepsilon:=\dfrac{K-L}{2}>0$ (midpoint trick).
> 3) From the two limits, find $N_1,N_2$ so that  
>    $n\ge N_1\Rightarrow |s_n-K|<\varepsilon$ and $n\ge N_2\Rightarrow |t_n-L|<\varepsilon$.
> 4) Take $N=\max\{N_1,N_2\}$. Then for $n\ge N$:  
>    $s_n> K-\varepsilon=\dfrac{K+L}{2}$ and $t_n< L+\varepsilon=\dfrac{K+L}{2}$.
> 5) Hence $s_n>t_n$ for $n\ge N$, contradicting $s_n\le t_n$. Therefore $K\le L$.

Assumption (for contradiction):
$$
\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]\ \wedge\
\lim_{n\to\infty}\{s_n\}=K\ \wedge\
\lim_{n\to\infty}\{t_n\}=L\ \wedge\
\neg(K\le L)\ \Rightarrow\ K>L.
$$

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{s_n\}=K
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2}\,\Big],\\[6pt]
&(2)\quad \lim_{n\to\infty}\{t_n\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}\,\Big].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N_1,N_2$, and **UI** on $n$ in (1), (2), sequentially:
$$
\begin{aligned}
&(3)\quad n\ge N_1 \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2},\\
&(4)\quad n\ge N_2 \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}.
\end{aligned}
$$

Choose the common index (Common–$N$ lemma):
$$
N_{\varepsilon}(K,L):=\max\{N_1,N_2\}.
$$

Substitute $N_{\varepsilon}(K,L)$ into (3),(4):
$$
\begin{aligned}
&(3')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |s_n-K|<\dfrac{\varepsilon}{2},\\
&(4')\quad n\ge N_{\varepsilon}(K,L) \Rightarrow |t_n-L|<\dfrac{\varepsilon}{2}.
\end{aligned}
$$

Now set $\varepsilon:=K-L$ (since $K>L$) in (3'), (4'):
![[segment_midpoint_K_L_no_star.png]]

$$
\begin{aligned}
(3'')\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow\ \big|\,s_n-K\,\big|<\dfrac{K-L}{2}
&&\text{(from (3'))}
\\
&\Rightarrow\ -\dfrac{K-L}{2}<s_n-K<\dfrac{K-L}{2}
&&\text{(expand }|x|<a\Rightarrow -a<x<a)
\\
&\Rightarrow\ K-\dfrac{K-L}{2}<s_n<\dfrac{K-L}{2}+K
&&\text{(add $K$)}
\\
&\Rightarrow\ \dfrac{K+L}{2}<s_n<\dfrac{K+L}{2}+(K-L)
&&\text{(since }K-\dfrac{K-L}{2}=\dfrac{K+L}{2})
\\
&\Rightarrow\ s_n>\dfrac{K+L}{2}
&&\text{(keep the left inequality).}
\end{aligned}
$$

$$
\begin{aligned}
(4'')\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow\ \big|\,t_n-L\,\big|<\dfrac{K-L}{2}
&&\text{(from (4'))}
\\
&\Rightarrow\ -\dfrac{K-L}{2}<t_n-L<\dfrac{K-L}{2}
&&\text{(expand)}
\\
&\Rightarrow\ L-\dfrac{K-L}{2}<t_n<\dfrac{K-L}{2}+L
&&\text{(add $L$)}
\\
&\Rightarrow\ t_n<\dfrac{K+L}{2}
&&\text{(since }L+\dfrac{K-L}{2}=\dfrac{K+L}{2})
\\
&\Rightarrow\ -t_n>-\dfrac{K+L}{2}
&&\text{(multiply by $-1$, reverse inequality)}
\\
&\Rightarrow\ -t_n+\dfrac{K+L}{2}>0
&&\text{(add }\dfrac{K+L}{2}\text{).}
\end{aligned}
$$

From (3'') and (4''):

$$
\begin{aligned}
(3''')\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow\ s_n>\dfrac{K+L}{2}
&&\text{(from (3''))}
\\
&\Rightarrow\ s_n-t_n>\dfrac{K+L}{2}-t_n
&&\text{(subtract $t_n$)}
\\
&\Rightarrow\ s_n-t_n>0
&&\text{(use the last line of (4''): }\dfrac{K+L}{2}-t_n>0\text{).}
\end{aligned}
$$

Record the positive gap and finish:

$$
\begin{aligned}
(5)\quad &K-L>0
&&\text{(assumed for contradiction)}
\\[2pt]
(3^{\mathrm{iv}})\quad n\ge N_{\varepsilon}(K,L)\ 
&\Rightarrow\ s_n-t_n>0
&&\text{(from (3''')).}
\end{aligned}
$$

This contradicts the antecedent $\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$. 
Therefore, this contradicts the antecedent $\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$. Therefore $K\le L$. $\blacksquare$


### Approach #2:

> [!abstract]+ **Proof outline — Order Preservation via the difference limit**
>
> 1) Start with the hypotheses $\displaystyle \lim s_n=K$, $\displaystyle \lim t_n=L$ and use the **difference rule** to get  
>    $\displaystyle \lim (s_n-t_n)=K-L$.
> 2) **Contradiction step:** assume $\neg(K\le L)$, i.e. $K-L>0$.
> 3) Apply the **Half-threshold above for positive limits** to the sequence $u_n:=s_n-t_n$ with limit $K-L>0$ to obtain an index $N$ such that  
>    $n\ge N \Rightarrow s_n-t_n>\dfrac{K-L}{2}>0$.
> 4) Hence $n\ge N \Rightarrow s_n>t_n$, contradicting $\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$. Conclude $K\le L$.
Assume $\displaystyle \lim_{n\to\infty}\{s_n\}=K$, $\displaystyle \lim_{n\to\infty}\{t_n\}=L$, and
$\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$.

From the **difference rule for limits**:
$$
\begin{aligned}
(1)\quad \lim_{n\to\infty}\{\,s_n-t_n\,\}
&=K-L.
\end{aligned}
$$

Assume, for contradiction, $\neg(K\le L)$; equivalently $K-L>0$.

Applying **Half-threshold above for positive limits** to (1):
$$
\begin{aligned}
(2)\quad \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\,n\ge N \Rightarrow \{\,s_n-t_n\,\}>\dfrac{K-L}{2}\,\Big].
\end{aligned}
$$

Applying **EI** on $N$ and **UG** on $n$ in (2), sequentially:
$$
\begin{aligned}
(3)\quad n\ge N\ 
&\Rightarrow\ s_n-t_n>\dfrac{K-L}{2}
&&\text{(from (2))}
\\
&\Rightarrow\ s_n-t_n>0
&&\text{(since }K-L>0\Rightarrow \dfrac{K-L}{2}>0)
\\
&\Rightarrow\ s_n>t_n
&&\text{(add $t_n$ to both sides).}
\end{aligned}
$$

But this contradicts the hypothesis $\forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$. Therefore the assumption
$K-L>0$ is false, and we must have
$$
K\le L.\ \blacksquare
$$