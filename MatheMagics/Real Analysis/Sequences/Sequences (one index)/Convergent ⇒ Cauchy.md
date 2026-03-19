---
down:
tags:
  - mathemagics/real_analysis
---
$$
\begin{aligned}
\text{Assumption: }(1)\quad 
&\lim_{n\to\infty}\{s_n\}=L\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$, making $m,n$ particular variables:

$$ \begin{aligned} (2)\quad &m\ge N_\varepsilon \Rightarrow |s_m-L|<\dfrac{\varepsilon}{2} \ \ \wedge\ \ n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2} \qquad\ \text{(Turn into propositional variables)} \\[6pt] &\ a\!\Rightarrow\! b\ \wedge\ c\!\Rightarrow\! d \qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \qquad\ \quad\ \text{(Applying inference and replacement rules)} \\[6pt] &\ a\!\Rightarrow\! b\ \wedge\ c\!\Rightarrow\! d\ \Rightarrow\ (a\wedge c)\!\Rightarrow\!(b\wedge d) \qquad\ \qquad\ \qquad\ \qquad\ \quad\ \text{(Turning propositional variables back)} \\[6pt] &\big(m\!\ge\! N_\varepsilon \Rightarrow |s_m\!-\!L|<\dfrac{\varepsilon}{2}\big)\ \wedge\ \big(n\!\ge\! N_\varepsilon \Rightarrow |s_n\!-\!L|<\dfrac{\varepsilon}{2}\big) \\[6pt] &\Rightarrow\ \big((m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow (|s_m\!-\!L|<\dfrac{\varepsilon}{2}\ \wedge\ |s_n\!-\!L|<\dfrac{\varepsilon}{2})\big). \end{aligned} $$

From eq. (2) line one eqs. (3),(4) can be derived:

$$
\begin{aligned}
(3)\quad 
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_n\!-\!L|<\dfrac{\varepsilon}{2}
\\[2pt]
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_n\!-\!L|+\dfrac{\varepsilon}{2}<\varepsilon
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_m\!-\!L|<\dfrac{\varepsilon}{2}
\\
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_m\!-\!L|+|s_n\!-\!L|<\dfrac{\varepsilon}{2}+|s_n\!-\!L|
\qquad \qquad \text{(sub.\ from last consequent in (4))}
\\
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_m\!-\!L|+|s_n\!-\!L|
<\dfrac{\varepsilon}{2}+\dfrac{\varepsilon}{2}<\varepsilon
\qquad \qquad \ \text{(applying transitivity)}
\\
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow 
|s_m\!-\!L|+|s_n\!-\!L|\ge |s_m\!-\!L+L\!-\!s_n|
\qquad\text{(applying triangle inequality)}
\\
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow 
|s_m\!-\!L\!+\!L\!-\!s_n|\le |s_m\!-\!L|+|s_n\!-\!L|<\varepsilon
\quad\text{(applying transitivity)}
\\
&n\ge N_\varepsilon \Rightarrow |s_n-L|<\dfrac{\varepsilon}{2}
\ \Rightarrow\ 
(m\!\ge\! N_\varepsilon \wedge n\!\ge\! N_\varepsilon)\Rightarrow |s_m-s_n|<\varepsilon
\end{aligned}
$$

Applying **UG** on $m,n$, **EG** on $N$, and **UG** on $\varepsilon$:

$$
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall m,n\in\mathbb{N}\,
\big[\,m\ge N\wedge n\ge N \Rightarrow |s_m-s_n|<\varepsilon\,\big].
$$

Sub. definition of limits and Cauchy sequences into (6):

$$
(6')\quad \lim_{n\to\infty}\{s_n\}=L\ \Rightarrow\ \{s_n\}\ \text{is Cauchy}.
$$
