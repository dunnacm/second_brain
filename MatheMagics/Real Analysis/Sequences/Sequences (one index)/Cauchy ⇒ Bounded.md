---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Cauchy ⇒ Bounded**
> > [!warning]+ **IF**
> > $$\{s_n\}\ \text{is Cauchy}$$
>
> > [!tip]+ **THEN**
> > $$\exists M>0\ \forall n\in\mathbb{N}\ \big[\,|s_n|\le M\,\big]\quad\text{(i.e., $\{s_n\}$ is bounded).}$$
## Proof:
$$
\begin{aligned}
(1)\quad 
&\{s_n\}\ \text{is Cauchy}\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-s_N|<\varepsilon\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, making $\hat{\varepsilon}$ a particular variable; **EI** on $N$; and **UI** on $n$:

$$
\begin{aligned}
(2)\quad 
&\{s_n\}\ \text{is Cauchy}\ \Leftrightarrow\
n\ge N_{\hat{\varepsilon}} \Rightarrow |s_n-s_{N_{\hat{\varepsilon}}}|<\hat{\varepsilon}.
\end{aligned}
$$

From eq.\,(2)’s RHS:

$$
\begin{aligned}
(3)\quad 
&n\ge N_{\hat{\varepsilon}} \Rightarrow |s_n-s_{N_{\hat{\varepsilon}}}|<\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow \big||s_n|-|s_{N_{\hat{\varepsilon}}}|\big|\le |\,s_n-s_{N_{\hat{\varepsilon}}}\,|<\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow \big||s_n|-|s_{N_{\hat{\varepsilon}}}|\big|<\hat{\varepsilon}
\qquad\text{(Replace $s_{N_{\hat{\varepsilon}}}:=L$)}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow \big||s_n|-|L|\big|<\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow -\hat{\varepsilon}<|s_n|-|L|<\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow |L|-\hat{\varepsilon}<|s_n|<|L|+\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow \ \ |L|-\hat{\varepsilon}<|s_n|\ \ \wedge\ \ |s_n|<|L|+\hat{\varepsilon}\\[4pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow |s_n|<|L|+\hat{\varepsilon}
\end{aligned}
$$

Define global bound:

$$
\begin{aligned}
(4)\quad 
&M:=\max\{\,|s_1|,|s_2|,\dots,|s_{N_{\hat{\varepsilon}}-1}|,\ |L|+\hat{\varepsilon}\,\}.
\end{aligned}
$$

Sub. eq.\,(4) into eq.\,(3):

$$
\begin{aligned}
(3')\quad 
&n\ge N_{\hat{\varepsilon}} \Rightarrow |s_n|<|L|+\hat{\varepsilon}\le M\\[2pt]
&n\ge N_{\hat{\varepsilon}} \Rightarrow |s_n|\le M
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N_{\hat{\varepsilon}}$, **EG** on $M$:

$$
\begin{aligned}
(5)\quad 
&\exists M\in\mathbb{R}^+\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n|\le M\,].
\end{aligned}
$$
