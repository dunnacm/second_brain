---
down:
  - "[[Parametrizing a formula by its FVs]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
For a term or formula, **FV( . )** denotes the set of **free variables**.
**Free variables** are those with at least one **free occurrence**, i.e., not bound by a quantifier at that occurrence
>[!quote]+ **FV — Free Variables**
>**Meaning.** For a term or formula, $\mathrm{FV}(\,\cdot\,)$ denotes the set of **free variables**.
>
>**Terms.** $\mathrm{FV}(x)=\{x\}$, $\mathrm{FV}(c)=\varnothing$, and variables in a compound term are the union of variables in its arguments.
>
>**Formulas.** Free variables are those with at least one **free occurrence** (not bound by a quantifier at that occurrence).

**Core laws (terms & formulas).**
$$
\begin{aligned}
& \mathrm{FV}(x)=\{x\}, \qquad \mathrm{FV}(c)=\varnothing, \qquad
  \mathrm{FV}\!\big(f(t_0,\ldots,t_{n-1})\big)=\bigcup_{i<n}\mathrm{FV}(t_i) \\[6pt]
& \mathrm{FV}\!\big(R(t_0,\ldots,t_{n-1})\big)=\bigcup_{i<n}\mathrm{FV}(t_i) \\[6pt]
& \mathrm{FV}(\lnot \varphi)=\mathrm{FV}(\varphi) \\[6pt]
& \mathrm{FV}(\varphi \circ \psi)=\mathrm{FV}(\varphi)\cup\mathrm{FV}(\psi)
   \qquad(\circ\in\{\land,\lor,\to,\leftrightarrow\}) \\[6pt]
& \mathrm{FV}(\forall x\,\varphi)=\mathrm{FV}(\varphi)\setminus\{x\}, \qquad
  \mathrm{FV}(\exists x\,\varphi)=\mathrm{FV}(\varphi)\setminus\{x\}
\end{aligned}
$$

**Examples.**
$$
\begin{aligned}
& \mathrm{FV}(x=y)=\{x,y\} \\[6pt]
& \mathrm{FV}\!\big(\forall x\,P(x,y)\big)=\{y\} \\[6pt]
& \mathrm{FV}\!\big(P(x)\ \lor\ \exists y\,Q(y,z)\big)=\{x,z\}
\end{aligned}
$$

**Safe substitution**  
If $t$ is **free for** $x$ **in** $p$ (i.e., substitution causes **no variable capture**), then
$$
\mathrm{FV}\big(p[x:=t]\big)=\big(\mathrm{FV}(p)\setminus\{x\}\big)\ \cup\ \mathrm{FV}(t).
$$

