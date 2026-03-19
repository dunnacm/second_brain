---
down:
  - "[[Limit comparison test (convergence)]]"
  - "[[Limit comparison test (divergence)]]"
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Limit comparison test**
> > [!warning]+ **IF**
> > - $S^{(1)}=\sum_{n=1}^{\infty} s_n$  
> >   ∘ $s_n\ge 0$ for all $n\in\mathbb{N}$ (i.e., **positive**)  
> > 
> > - $S^{(2)}=\sum_{n=1}^{\infty} t_n$  
> >   ∘ $t_n\ge 0$ for all $n\in\mathbb{N}$ (i.e., **positive**)  
> > 
> >- $\displaystyle \lim_{n\to\infty}\frac{s_n}{t_n}=c,\quad c\in\mathbb{R}^+.$
>
> > [!tip]+ **THEN**
> > $S^{(1)}$ and $S^{(2)}$ have the **same convergence behavior**  (i.e., either both **converge** or both **diverge**).
> 
> ---
> $$
\begin{aligned}
(1)\quad 
& \int_{n+1}^{\infty} s(x)\,dx \ \le\ R_{n}^{(1)}\ \le\ \int_{n}^{\infty} s(x)\,dx
\\[8pt]
(2)\quad 
& \int_{n+1}^{\infty} t(x)\,dx \ \le\ R_{n}^{(2)}\ \le\ \int_{n}^{\infty} t(x)\,dx
\\[8pt]
(3)\quad 
& s_n \le t_n
\\[8pt]
& \therefore\quad R_{n}^{(1)}\ \le\ R_{n}^{(2)}\ \le\ \int_{n}^{\infty} t(x)\,dx .
\end{aligned}
$$
## Proof:
**Assumption:**

$$
\sum_{n=1}^{\infty} t_n \ \text{is convergent}
\ \Rightarrow\
\Big[\, \sum_{n=1}^{\infty} t_n = T \in \mathbb{R}
\ \Leftrightarrow\
\sum_{n=N}^{\infty} t_n = T \in \mathbb{R}\,\Big].
$$
From definition of a limit:
$$
\begin{aligned}
(1)\quad 
& \lim_{n\to\infty}\frac{a_n}{b_n}=c 
\ \Leftrightarrow\ 
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
\Big[\, n\ge N \Rightarrow \Big|\frac{a_n}{b_n}-c\Big|<\varepsilon \,\Big].
\end{aligned}
$$
Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$:

$$
\begin{aligned}
(2)\quad 
& n \ge N_{\varepsilon}(c) 
&& \Rightarrow && \left|\frac{a_n}{b_n}-c\right|<\varepsilon \\[6pt]
& 
&& \Rightarrow && -\varepsilon \;<\; \frac{a_n}{b_n}-c \;<\; \varepsilon \\[6pt]
& 
&& \Rightarrow && c-\varepsilon \;<\; \frac{a_n}{b_n} \;<\; c+\varepsilon \\[6pt]
& 
&& \Rightarrow && (c-\varepsilon)\,b_n \;<\; a_n \;<\; (c+\varepsilon)\,b_n \\[6pt]
& 
&& \Rightarrow && m\,b_n \;<\; a_n \;<\; M\,b_n
\end{aligned}
$$

where $m:=c-\varepsilon$ and $M:=c+\varepsilon$.

Applying addition of an arbitrary number of inequalities to eq. (2):

$$
\begin{aligned}
(2')\quad 
& n \ge N_{\varepsilon}(c) 
&& \Rightarrow && m\,b_n \;<\; a_n \;<\; M\,b_n \\[8pt]
& 
&& \Rightarrow && \sum_{n=N_{\varepsilon}(c)}^{N} m\,b_n 
\;<\; \sum_{n=N_{\varepsilon}(c)}^{N} a_n 
\;<\; \sum_{n=N_{\varepsilon}(c)}^{N} M\,b_n \\[8pt]
& 
&& \Rightarrow && m \cdot \sum_{n=N_{\varepsilon}(c)}^{N} b_n 
\;<\; \sum_{n=N_{\varepsilon}(c)}^{N} a_n 
\;<\; M \cdot \sum_{n=N_{\varepsilon}(c)}^{N} b_n
\end{aligned}
$$
As $N\to\infty$ eq. $(2')$ becomes:
$$
\begin{aligned}
(2'')\quad 
& n \ge N_{\varepsilon}(c)
&& \Rightarrow && m\!\cdot\!\sum_{n=N_{\varepsilon}(c)}^{\infty} b_n
\;<\; \sum_{n=N_{\varepsilon}(c)}^{\infty} a_n
\;<\; M\!\cdot\!\sum_{n=N_{\varepsilon}(c)}^{\infty} b_n \\[8pt]
& 
&& \Rightarrow && m\!\cdot\!T
\;<\; \sum_{n=N_{\varepsilon}(c)}^{\infty} a_n
\;<\; M\!\cdot\!T
\end{aligned}
$$

By **comparison test** applied to eq. $(2'')$:
$$
\Bigg(
\sum_{n=N_{\varepsilon}(c)}^{\infty} b_n = T
\ \Leftrightarrow\
\sum_{n=1}^{\infty} b_n = T
\Bigg)
\ \Rightarrow\
\sum_{n=N_{\varepsilon}(c)}^{\infty} a_n = S \in \mathbb{R}.
$$
