---
down:
tags:
  - mathemagics/real_analysis
---
**Triangle inequality on $\mathbb{R}$ via $\operatorname{sgn}$**

Recall $\operatorname{sgn}(t)\in\{-1,0,1\}$ and $\lvert t\rvert=\operatorname{sgn}(t)\,t$ for all $t\in\mathbb{R}$.

**Lemma.** For any $u\in\{-1,0,1\}$ and any $x\in\mathbb{R}$,
$$
u\,x \le \lvert x\rvert.
$$
*Proof of lemma.* Since $-1\le u\le 1$, we have $-\,\lvert x\rvert \le u\,x \le \lvert x\rvert$. The right-hand inequality is the claim. $\square$

**Proof of triangle inequality.**
Let $s:=\operatorname{sgn}(x+y)$. Then
$$
\lvert x+y\rvert \;=\; s(x+y) \;=\; s\,x + s\,y
\;\le\; \lvert x\rvert + \lvert y\rvert,
$$
where we used the lemma twice (with $u=s$). $\square$

**Equality condition (in $\mathbb{R}$).**
Equality holds iff $s\,x=\lvert x\rvert$ and $s\,y=\lvert y\rvert$, i.e. iff $\operatorname{sgn}(x)=\operatorname{sgn}(y)$ (or one of $x,y$ is $0$).
