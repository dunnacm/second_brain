---
down:
  - "[[Convergent (sequences)]]"
  - "[[Divergent (sequences)]]"
  - "[[Monotone convergence Thm.]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
- The definition of the convergence of a sequence states that for each prescribed neighborhood $V_{\varepsilon}(L)$, there exists an index $N$ such that all subsequent terms $a_n$ (with $n > N$) lie inside this neighborhood.  
- In other words, the terms of the sequence **eventually enter and remain within** every $\varepsilon$-neighborhood of $L$; equivalently, the sequence becomes **arbitrarily close** to $L$ as $n$ increases.
#### Geometric interpretations:
##### Geometric interpretation in the number line
![[Pasted image 20251012115329.png]]
##### Geometric interpretation in the x-y axis
![[Gemini_Generated_Image_rzrjperzrjperzrj.png]]
### Formal definition:
> [!note]+ **Convergence of a sequence**
>
> > [!warning]+ **IFF**
> > $$
> > \lim_{n\to\infty}\{s_n\}=L,\quad L\in\mathbb{R}.
> > $$
>
> > [!tip]+ **THEN**
> > $$
> > \forall\,\varepsilon>0\ \exists\,N\in\mathbb{N}\ \forall\,n\in\mathbb{N}\,[\,n\ge N\ \Rightarrow\ \lvert s_n - L\rvert < \varepsilon\,].
> > $$
>
> > [!note]+ **Notes**
> > - The integer $N$ **depends on** $\varepsilon$. This set is denoted $N_{\varepsilon}(L)$.  
> > - $\lvert s_n - L\rvert < \varepsilon$ describes that $s_n$ lies in the $\varepsilon$-neighborhood of $L$.  
> > - Other notation: $\{s_n\}\to L$ as $n\to\infty$.
## Examples:
### Example 1:
**Prove:** $\left\{\dfrac{1}{n}\right\}$ converges to $0$.

**Assume:**

$$
\begin{aligned}
&(1)\quad 
\lim_{n\to\infty}\left\{\frac{1}{n}\right\}
\Leftrightarrow
\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
[\,n\ge N\Rightarrow\lvert(\tfrac{1}{n})-0\rvert<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$, and UI on $n$ sequentially:

$$
\begin{aligned}
&(2)\quad n\ge N\Rightarrow\lvert(\tfrac{1}{n})-0\rvert<\varepsilon.
\end{aligned}
$$

From eq. (2)’s consequent:

$$
\begin{aligned}
&(3)\quad \lvert(\tfrac{1}{n})-0\rvert<\varepsilon\quad(\varepsilon>0)\\
&\qquad \frac{1}{n}-0<\varepsilon\\
&\qquad \frac{1}{n}<\varepsilon\\
&\qquad n>\frac{1}{\varepsilon}.
\end{aligned}
$$

Informed by (3), choose  

$$
\begin{aligned}
&(4)\quad N_{\varepsilon}(L):=\left\lceil\frac{1}{\varepsilon}\right\rceil.
\end{aligned}
$$

From eq. (2)’s antecedent:

$$
\begin{aligned}
&(5)\quad n\ge N_{\varepsilon}(L)\Rightarrow n\ge\left\lceil\frac{1}{\varepsilon}\right\rceil>\frac{1}{\varepsilon}\quad\text{(sub. eq. (3))}\\
&\qquad n\ge N_{\varepsilon}(L)\Rightarrow n>\frac{1}{\varepsilon}\\
&\qquad n\ge N_{\varepsilon}(L)\Rightarrow\frac{1}{n}<\varepsilon\\
&\qquad n\ge N_{\varepsilon}(L)\Rightarrow\frac{1}{n}-0<\varepsilon\\
&\qquad n\ge N_{\varepsilon}(L)\Rightarrow\lvert(\tfrac{1}{n})-0\rvert<\varepsilon.
\end{aligned}
$$

Applying UG on $n$, EG on $N_{\varepsilon}(L)$, and UG on $\varepsilon$ sequentially:

$$
\begin{aligned}
&(6)\quad 
\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,
[\,n\ge N\Rightarrow\lvert\tfrac{1}{n}-0\rvert<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}\frac{1}{n}=0.
\end{aligned}
$$
### Example 2:
Consider the sequence $a_n = \dfrac{1}{n^2 + 1}$.  
This sequence is convergent to $0$.  

Consider the open interval centered at $0$ and of radius $\varepsilon = 10^{-2}$.  
What is the rank (in this sequence) of the first element that belongs to this interval?  
Your answer should be a natural number.

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\left\{\frac{1}{n^2+1}\right\}=0
\end{aligned}
$$

From convergence definition:

$$
\begin{aligned}
&(2)\quad \forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N\Rightarrow\lvert s_n - L\rvert<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$, and UI on $n$ sequentially:

$$
\begin{aligned}
&(3)\quad n\ge N \Rightarrow \lvert s_n - L\rvert < \varepsilon
\end{aligned}
$$

$$
\begin{aligned}
(3) \quad n\ge N & \Rightarrow \lvert s_n - L\rvert < \varepsilon\\
n\ge N &\Rightarrow \lvert s_n - L\rvert < \varepsilon\\
n\ge N &\Rightarrow \left|\frac{1}{n^2+1}-0\right| < 10^{-2}\\
n\ge N &\Rightarrow \frac{1}{n^2+1} < 10^{-2}\\
n\ge N &\Rightarrow n^2 + 1 > 10^2\\
n\ge N &\Rightarrow n^2 > 10^2 - 1\\
n\ge N &\Rightarrow n > \sqrt{10^2 - 1},\quad n\in\mathbb{N}\\
n\ge N &\Rightarrow n > 10
\end{aligned}
$$

From eq. (3), choose  

$$
N_{10^{-2}}(0):=10
$$

$$
\therefore\ \text{The rank of }\{s_n\}\text{ is }10.
$$


