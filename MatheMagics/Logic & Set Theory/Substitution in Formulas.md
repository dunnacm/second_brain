---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Fundamentals:
### Introduction:
Substitution for a variable in a formula is a bit more involved.
This is because of the influence of any possible quantifiers. For example, take the formula 
$$(1) \quad x = y \, \lor \, x = f(y))$$
By *substitution in term's* definition, one knows that  the constants *c* and *d* can be substituted by the variables *x* and *y*, respectively, and the function *f(y)*, resulting in
$$c = d \, \lor \, c = f(d)$$
However, in the formula 
$$
\begin{aligned}
(2) \quad & \forall x \exists y \; (\, x = y \; \lor \; x = f(y) \,)
\end{aligned}
$$
the situation is different because of the **quantifiers**.
Even though each occurrence of *x* and *y* in *eq. (1)* can receive a substitution, each corresponding occurrence in *eq. (2)* cannot because the **quantifiers** are *binding* the variables. 

---
## Definition:
>[!important] **Preconditions**
>> - Let **S** be *theory symbols* from a first-order *alphabet* **A**.
>> - Let *x* and *y* be variable symbols of **A** 
>> - Let $t_0, \, t_1, \, ... \, t_{n-1}$ be **S-terms**.
>> - Let ***R*** be an *n*-ary relation symbol from **S**
>> - Let **p**, **q** be **S-formulas**
>
**Substitution in formulas** are governed according to the following rules:

>[!quote]+ **Substitution (Equality)**
>$(t_0 = t_1)[x := t] \;\Leftrightarrow\; \big(t_0[x := t] = t_1[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Relation symbol)**
>$\big(R(t_0, \ldots, t_{n-1})\big)[x := t] \;\Leftrightarrow\; R\!\big(t_0[x := t], \ldots, t_{n-1}[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Negation)**
>$(\lnot p)[x := t] \;\Leftrightarrow\; \lnot\big(p[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Conjunction)**
>$(p \land q)[x := t] \;\Leftrightarrow\; \big(p[x := t] \land q[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Disjunction)**
>$(p \lor q)[x := t] \;\Leftrightarrow\; \big(p[x := t] \lor q[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Implication)**
>$(p \to q)[x := t] \;\Leftrightarrow\; \big(p[x := t] \to q[x := t]\big)$
>
>---

>[!quote]+ **Substitution (Biconditional)**
>$(p \leftrightarrow q)[x := t] \;\Leftrightarrow\; \big(p[x := t] \leftrightarrow q[x := t]\big)$
>
>---

>[!quote]+ **Substitution under Universal Quantifier**
>$$
>(\forall y\,p)[x := t] \;\Leftrightarrow\;
>\begin{cases}
>\forall y\,\big(p[x := t]\big) & \text{if } x \neq y \text{ and } y \notin \mathrm{FV}(t),\\
>\forall y\,p & \text{otherwise.}
>\end{cases}
>$$
>
>---

>[!quote]+ **Substitution under Existential Quantifier**
>$$
>(\exists y\,p)[x := t] \;\Leftrightarrow\;
>\begin{cases}
>\exists y\,\big(p[x := t]\big) & \text{if } x \neq y \text{ and } y \notin \mathrm{FV}(t),\\
>\exists y\,p & \text{otherwise.}
>\end{cases}
>$$
>
>---






