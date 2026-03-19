---
down:
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
fix this... this is a mess
## No supremum in ℚ
For $S:=\{\,x\in\mathbb{Q}:x^2<2\,\}=\{\,x\in\mathbb{Q}:\,(x-\sqrt{2})(x+\sqrt{2})<0\,\},$ let's show that **$S$ has no supremum in $\mathbb{Q}$**. This exhibits the need for the reals (completeness).


$$
\begin{aligned}
(1)\quad & S \;=\;\{\,q\in\mathbb{Q}:q^{2}<2\,\}.\\[6pt]
(2)\quad & q=\sup_{\mathbb{Q}} S 
\ \Leftrightarrow\ 
\big[(\forall s\in S)\,s\le q\big]\ \wedge\ \big[(\forall \varepsilon>0)(\exists s\in S)\,(q-\varepsilon<s)\big] \quad (\text{Assu} ).
\end{aligned}
$$

**CASE I**
$$(3) \quad q\le \sqrt{2}.$$
**Choose** $u\in\mathbb{Q}$ with $q<u<\sqrt{2}$ _(density of $\mathbb{Q}$)._
$$
\begin{aligned}
(4)\quad & q<u\in\mathbb{Q}\ \wedge\ u<\sqrt{2} \qquad (\text{combining }(3)\text{ and the choice of }u)\\
&  u\in S\cap\mathbb{Q}\qquad\ \qquad\ \qquad\ \, (\text{since }u<\sqrt{2}\Rightarrow u^{2}<2).\\[6pt]
(5)\quad & \exists s\in S\ [\,q<s\,] \qquad\ \qquad\ \ \ (\text{EG on }u\text{ from }(4)).
\end{aligned}
$$

From (2) and (5), $q$ cannot satisfy $(\forall s\in S)\,s\le q$; **Case I** is impossible.

**CASE II**
$$
(6) \quad q>\sqrt{2}\ \Rightarrow\ q^{2}\ge 2
$$
**UI: fix** $\varepsilon:=q-\sqrt{2}>0$.  
By (2), **EI gives** $s\in S$ with $q-\varepsilon<s$ (i.e., $\sqrt{2}<s$).  
But $s\in S \Rightarrow s^{2}<2 \Rightarrow s\le \sqrt{2}$ — **contradiction**.

Both cases lead to contradictions. Therefore no $q\in\mathbb{Q}$ satisfies the supremum condition in (2).

$$
\therefore\ \text{$S$ has no supremum in }\mathbb{Q}.
$$

