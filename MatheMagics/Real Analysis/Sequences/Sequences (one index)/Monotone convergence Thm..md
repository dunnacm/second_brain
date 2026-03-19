---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Monotone convergence (bounded ⇒ convergent)**
> > [!warning]+ **IFF**
> > - $\forall n\in\mathbb{N}\ [\,s_n\le s_{n+1}\,]\ \ \vee\ \ \forall n\in\mathbb{N}\ [\,s_n\ge s_{n+1}\,]$  *(i.e., $\{s_n\}$ is monotone)*  
> > - $\exists M>0\ \forall n\in\mathbb{N}\ [\,\lvert s_n\rvert\le M\,]$  *(i.e., $\{s_n\}$ is bounded)*
> 
> 
> > [!tip]+ **THEN**
> > - **If nondecreasing:**  
> >   $$
> >   \exists L\in\mathbb{R}\quad \lim_{n\to\infty}s_n=L=\sup\{\,s_n:n\in\mathbb{N}\,\}.
> >   $$
> > - **If nonincreasing:**  
> >   $$
> >   \exists L\in\mathbb{R}\quad \lim_{n\to\infty}s_n=L=\inf\{\,s_n:n\in\mathbb{N}\,\}.
> >   $$
## Proof:
**Assumptions:**

$$
\begin{aligned}
(1)\quad 
& \forall n\in\mathbb{N}\ \exists M\in\mathbb{R}\ [\,|s_n|\le M\,] 
\qquad (\text{i.e., }\{s_n\}\text{ is bounded})
\\[6pt]
& 
\overset{\text{(supremum property)}}{\Longrightarrow}
\ \exists U\in\mathbb{R}\ [\,\sup\{s_n\}=U\,].\\[15pt]
(2)\quad 
& \forall m,n\in\mathbb{N}\ [\,n\ge m \Rightarrow s_n\ge s_m\,]
\qquad (\text{i.e., }\{s_n\}\text{ is monotone nondecreasing}).
\end{aligned}
$$

Applying **UI** on n, **EI** on M, and **EI** on U in eq. (1), sequentially:
$$
\begin{aligned}
(1')\quad 
& |s_n|\le M \Rightarrow \sup\{s_n\}=U .
\end{aligned}
$$

Applying **UI** on m,n, fixing $m:=N_{\varepsilon}$ in eq. (2):
$$
\begin{aligned}
(2')\quad 
& n\ge N_{\varepsilon} \Rightarrow s_n\ge s_{N_{\varepsilon}} .
\end{aligned}
$$
By definition of the supremum of a set:
$$
\begin{aligned}
(3)\quad 
& \sup\{s_n\}=U 
\quad \Leftrightarrow \quad
\forall s_n\in\{s_n\}\,[\,s_n\le U\,]\ \land\ 
\forall \varepsilon>0\ \exists s_n\in\{s_n\}\,[\,U-\varepsilon<s_n\,].
\end{aligned}
$$

Applying **UI** on $s_n$; **UI** on $\varepsilon$ and **EI** on $s_n$, fixing $s_n:=s_{N_{\varepsilon}}$ sequentially:
$$
\begin{aligned}
(3')\quad 
& \sup\{s_n\}=U 
\quad \Leftrightarrow \quad
s_n\le U\ \land\ U-\varepsilon<s_{N_{\varepsilon}} .
\end{aligned}
$$

Sub. eq. (3')’s consequent into eq. (2'):
$$
\begin{aligned}
(2'')\quad 
& n\ge N_{\varepsilon} \Rightarrow U\ge s_n\ge s_{N_{\varepsilon}}>U-\varepsilon
\\[6pt]
& n\ge N_{\varepsilon} \Rightarrow U + \varepsilon \ge s_n\ge s_{N_{\varepsilon}}>U-\varepsilon
\\[6pt]
& n\ge N_{\varepsilon} \Rightarrow U+\varepsilon\ge s_n>U-\varepsilon
\\[6pt]
& n\ge N_{\varepsilon} \Rightarrow -\varepsilon\le s_n-U\le \varepsilon
\\[6pt]
& n\ge N_{\varepsilon} \Rightarrow |s_n-U|<\varepsilon .
\end{aligned}
$$

Applying **UG** on $n$, **EI** on $N_{\varepsilon}$, and **UG** on $\varepsilon$ in eq. (2''):
$$
\begin{aligned}
(2''')\quad 
& \forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-U|<\varepsilon\,].
\end{aligned}
$$
