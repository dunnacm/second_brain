---
down:
  - "[[Substitution in Formulas]]"
  - "[[Set of FVs]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
cssclasses:
---
## Introduction:
### Definition:
In the section of [[Substitution in Formulas]], we saw the rules that govern substitution in universal and existential quantifiers:

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

Let's explore representative illustrations of these two important rules:

#### Example:
*(1)*  **Formula**: $p := \exists y \,(x + y = 0)$  

*(2)*  **Interpretation**: Given $x$, there exists a number $y$ such that $x + y = 0$.  

Let $f$ be a unary function symbol and $z$ be a variable symbol:  

- **Substitute** $x := z$ in *(1)*:  

  Formula: $p[x := z] \Leftrightarrow \exists y \,(z + y = 0)$  
  Interpretation: Same as *(2)*.  

- **Substitute** $x := f(z)$ in *(1)*:  

  Formula: $p[x := f(z)] \Leftrightarrow \exists y \,(f(z) + y = 0)$  
  Interpretation: Same as *(2)*.  

Both of these substitutions work because **no variable capture occurs** (the substitution is **safe**): variables in the term replacing $x$ remain **free**, and no quantifier newly binds them.

>[!warning] **Wrong approach to substitution in quantifiers**
> Formula:  $p[x := y] \Leftrightarrow \exists y \,(y + y = 0)$  
> Interpretation: There exists a number $y$ such that $y + y = 0$.  
>
> The proposition is reasonable, but **not** in the spirit of the original $p$.  
> **Why? Variable capture.** The $y$ in the substituted term becomes **bound** by the quantifier $\exists y$, changing the pattern of free vs. bound occurrences (originally $p$ had one free variable; the result has **none**).

## Governing principle:
### Verbal explanation:
$Q \, y\,p[x := t]$ (where *Q* can be any quantifier)

What is required is **safe (capture-avoiding) substitution**: 
- Replacing only the **free** occurrences of *x* by a term *t* **without** turning any variable occurring in *t* from free to bound, i.e., **free → bound** (no **variable capture**). This is exactly “*t* is free for *x* in *p*.”
- **When making a substitution**, the free/bound status of variables **must be preserved** (no capture), not the raw **number** of occurrences.
### Formal explanation:
Formally, if $t$ is **free for** $x$ **in** $p$ (safe substitution), then
$$
\mathrm{FV}\big(p[x:=t]\big) \;=\; \big(\mathrm{FV}(p)\setminus\{x\}\big)\ \cup\ \mathrm{FV}(t).
$$
- Only the **free** occurrences of $x$ are replaced.  
- Variables from $t$ remain **free** after substitution (no new bindings).  
- Bound variables and their scopes are unchanged

For this reason, the “blocked” substitution under a conflicting quantifier does nothing:

$$(\exists y \,(x + y = 0))[x := y] \;\Leftrightarrow\; \exists y \,(x + y = 0)$$

---
## ***Abstract***:
>[!abstract] **Safe substitution (recap)**
>- Substitute only **free occurrences** of the variable. Bound occurrences (under a quantifier for that variable) are **never** replaced.
>- The replacement must be **capture-avoiding**: no variable occurring in the replacing term becomes bound after substitution (i.e., never **free → bound**).
>- If capture would occur, **block** the substitution.
>- You may replace a free variable by **any term** *t* (variable, constant, or compound term). When *t* is free for *x* in *p*,
>  $\mathrm{FV}\big(p[x:=t]\big)=\big(\mathrm{FV}(p)\setminus\{x\}\big)\cup \mathrm{FV}(t).$
>>  ◦ Replace by another variable (remains free if safe).
> > ◦ Replace by a constant (removes \(x\) from the free set).
> > ◦ Replace by a compound term ($f(t_0,\ldots,t_{n-1})$) (adds the free vars of that term).
> ---
### Example revisited: 
*(1)*  **Formula**: $p := \exists y\,(x + y = 0)$

**Substitute** $[x := y]$ in *(1)*:

*(1')*  $p[x := y] \;\Leftrightarrow\; \exists y\,(x + y = 0)[x := y]$

In *(1')*, $x$ is **free**. Substituting $x$ by $y$ (which is **bound** by the quantifier $\exists y$) would cause **variable capture**, turning a free occurrence into a bound one ($\text{free}\mapsto\text{bound}$). Therefore, this substitution is **blocked** and does nothing.

*(2)*  $p[x := y] \;\Leftrightarrow\; \exists y\,(x + y = 0)[x := y] \;\Leftrightarrow\; \exists y\,(x + y = 0)$

## Examples:
$$ \begin{aligned} & (1)\;\; p \;\Leftrightarrow\; \forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + x_2\big) \\[10pt] & \text{Substitute } x_0 := 0 \text{ in (1):} \\[3pt] & (2) \qquad p[x_0 := 0] \;\Leftrightarrow\; \forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + x_2\big) \;\;(x_0 \text{ is bound, therefore substitution is "blocked"}) \\[10pt] & \text{Substitute } x_1 := y \text{ in (2):} \\[3pt] & (3) \qquad \big(p[x_0 := 0]\big)[x_1 := y] \;\Leftrightarrow\; \forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + x_2\big) \;\;(x_1 \text{ is bound, therefore substitution is "blocked"}) \\[10pt] & \text{Substitute } x_2 := 1 \text{ in (3):} \\[3pt] & (4) \qquad \big(\,(p[x_0 := 0])[x_1 := y]\,\big)[x_2 := 1] \;\Leftrightarrow\; \forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + 1\big) \;\;(x_2 \text{ was free, therefore, substitution is lawful}) \\[10pt] & \text{Substitute } x_2 := x_1 \text{ in (1):} \\[3pt] & \qquad p[x_2 := x_1] \;\Leftrightarrow\; \big(\forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + x_2\big)\big)[x_2 := x_1] \\[3pt] & \qquad \qquad \qquad \quad \, \Leftrightarrow\; \forall x_0 \forall x_1 \,\big(x_0 = x_1 \;\to\; x_0 + x_2 = x_1 + x_2\big) \;\;(\text{blocked to avoid capture since } x_1 \text{ occurs in the substituting term } x_1) \end{aligned} $$

