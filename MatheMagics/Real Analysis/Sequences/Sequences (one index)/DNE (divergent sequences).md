---
down:
tags:
  - mathemagics/real_analysis
---
**Prove:** $\{(-1)^n\}$ is divergent.  

**Assumption:**

$$
\begin{aligned}
&(1)\quad 
\lim_{n\to\infty}\{(-1)^n\}=L
\Leftrightarrow
\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N\Rightarrow\lvert(-1)^n - L\rvert<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$, and UI on $n$ sequentially:

$$
\begin{aligned}
(2)\quad n\ge N & \Rightarrow \lvert(-1)^n - L\rvert < \varepsilon\\
n\ge N &\Rightarrow \lvert -1 - L\rvert < \varepsilon,\quad n\ \text{odd}\\
&\ \ \ \ \ \ \ \ \ \ \ \lor\\
n\ge N &\Rightarrow \lvert 1 - L\rvert < \varepsilon,\quad n\ \text{even}
\end{aligned}
$$

Combining the two conjuncts in eq. (2)’s consequent through addition:

$$
\begin{aligned}
&(3)\quad \lvert 1 + L\rvert + \lvert 1 - L\rvert < 2\varepsilon \quad \text{(Applying triangle inequality)}\\[4pt]
&\qquad \lvert 1 + L\rvert + \lvert 1 - L\rvert \le \lvert 1 + L\rvert + \lvert 1 - L\rvert < 2\varepsilon\\[4pt]
&\qquad \lvert 1 + L\rvert + \lvert 1 - L\rvert < 2\varepsilon
\end{aligned}
$$

Informed by eq. (3), choose  

$$
(4)\quad \varepsilon := \frac{\lvert 1 + L\rvert + \lvert 1 - L\rvert}{2}.
$$

Substitute (4) into (3):

$$
\begin{aligned}
&(3')\quad \lvert 1 + L\rvert + \lvert 1 - L\rvert < 2\cdot\frac{\lvert 1 + L\rvert + \lvert 1 - L\rvert}{2}\\[4pt]
&\qquad \lvert 1 + L\rvert + \lvert 1 - L\rvert < \lvert 1 + L\rvert + \lvert 1 - L\rvert\\[4pt]
&\qquad 1 < 2 < 2
\end{aligned}
$$

By $\textit{reductio ad absurdum:}$

$$
\lim_{n\to\infty}\{(-1)^n\}=\varnothing.
$$
