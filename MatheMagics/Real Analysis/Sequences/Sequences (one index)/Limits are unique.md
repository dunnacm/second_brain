---
down:
tags:
  - mathemagics/real_analysis
---
Assuming $\displaystyle \lim_{n\to\infty}s_n$ has at least two limits, $L_1$ and $L_2$, where $L_1 \ne L_2$:

$$
\begin{aligned}
&(1)\quad 
\lim_{n\to\infty}s_n=L_1
\Leftrightarrow
\forall\varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1\Rightarrow |s_n - L_1|<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N_1$, and UI on $n$ sequentially to eq. (1):

$$
\begin{aligned}
&(2)\quad n\ge N_1 \Rightarrow |s_n - L_1| < \varepsilon.
\end{aligned}
$$

$$
\begin{aligned}
&(3)\quad 
\lim_{n\to\infty}s_n=L_2
\Leftrightarrow
\forall\varepsilon>0\ \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2\Rightarrow |s_n - L_2|<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N_2$, and UI on $n$ sequentially to eq. (3):

$$
\begin{aligned}
&(4)\quad n\ge N_2 \Rightarrow |s_n - L_2| < \varepsilon.
\end{aligned}
$$

Informed by eqs. (2), (4), choose $N := \max\{N_1, N_2\}$, which will hold for both eqs. (2), (4):

$$
\begin{aligned}
&(2')\quad n\ge N \Rightarrow |s_n - L_1| < \varepsilon\\
&(3')\quad n\ge N \Rightarrow |s_n - L_2| < \varepsilon
\end{aligned}
$$

From (2′):

$$
\begin{aligned}
(2'') \quad & n\ge N \Rightarrow |s_n - L_1| + |s_n - L_2| < \varepsilon + |s_n - L_2|\\
\qquad & n\ge N \Rightarrow |s_n - L_1| + |s_n - L_2| < \varepsilon + \varepsilon < 2\varepsilon\\
\qquad & n\ge N \Rightarrow |s_n - L_1| + |s_n - L_2| < 2\varepsilon \quad (\text{Applying triangle inequality})\\
\qquad & n\ge N \Rightarrow |s_n - L_1 + L_2 - s_n| \le |s_n - L_1| + |s_n - L_2| < 2\varepsilon\\
\qquad & n\ge N \Rightarrow |L_1 - L_2| < 2\varepsilon
\end{aligned}
$$

Informed by eq. (2″), choose  

$$
(4)\quad \varepsilon := \frac{|L_1 - L_2|}{2}.
$$

Substitute (4) into (2″):

$$
\begin{aligned}
&(2''')\quad |L_1 - L_2| < 2\cdot\frac{|L_1 - L_2|}{2}\\[4pt]
&\qquad \Rightarrow |L_1 - L_2| < |L_1 - L_2|\\[4pt]
&\qquad \bot
\end{aligned}
$$

By $\textit{reductio ad absurdum}$, the initial assumption is false; therefore,  

$$
\lim_{n\to\infty}s_n \text{ has a unique limit.}
$$
