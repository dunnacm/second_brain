---
down:
  - "[[Simultaneous substitution]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition

> [!note]+ **Parameterizing a formula by its free variables**
> > [!warning]+ **IF**
> > - $\mathrm{FV}(p)=\varnothing$, **or**
> > - $\mathrm{FV}(p)\subseteq\{x_0,\ldots,x_{n-1}\}$ where $x_0,\ldots,x_{n-1}$ are pairwise distinct.
>
> > [!tip]+ **THEN**
> > - $p(x_0,\ldots,x_{n-1}) \ \Leftrightarrow \ p$.
> > - if $p$ is a Closed Formula ($\mathrm{FV}(p)=\varnothing$), write $p() \ \Leftrightarrow \ p$.

> [!quote]+ **Note**:
> > This fixes an ordered list[^1] of variables to represent the free variables of $p$, so we can later write
> $$p(t_0,\ldots,t_{n-1})$$
> to mean **simultaneous substitution** of the terms $t_0,\ldots,t_{n-1}$ for $x_0,\ldots,x_{n-1}$.

## Examples
- Let $p:=R(x,x,z)$. Then:
	- $\mathrm{FV}(p)=\{x,z\}$.
	- Valid parameter lists include $(x,z)$ or $(x,z,w)$.
	- An invalid parameter list is $(x,x)$ (variables must be distinct).

- If $p$ is closed ($\mathrm{FV}(p)=\varnothing$), you may write $p() \Leftrightarrow p$.

---
[^1]: Choose an order once and use it consistently.