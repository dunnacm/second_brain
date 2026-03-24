---
down:
  - "[[Fresh constant]]"
  - "[[Particular constant]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
> [!note] **Inference Rule — Existential Instantiation (EI)**
>
> > [!warning] **IF**
> > - $p(x)$ is an $\mathcal{S}$-**formula**.
> > - $\hat a \in \overline{\mathcal{S}}$.
> > - $\hat a$ is a **fresh** constant (new symbol: it has not occurred earlier anywhere in the proof or in any open assumption).
>
> > [!tip] **THEN**
> > $\exists x\,p(x) \Rightarrow p(\hat a)$.
> 
>The constant symbol $\hat a$ obtained by EI is called **witness** of $\exists x p(x)$

> [!warning] **Restriction**
> - **UG** may **not** be applied to formulas containing $\hat a$.
> - **Why** $\hat a$ **must be a fresh constant?**
> 	$\hat a$ must have no prior occurrence in a proof when applying **EI** because a used symbol already represents some object.

### Proof:
... pending

## Examples:
### Legal uses:
- $\exists x\,[\,p(x)\land q(x)\,] \;\Rightarrow\; p(\hat a)\land q(\hat a)$
- $\exists y\,[\,r(a,y,c) \to r(a,y,c)\,] \;\Rightarrow\; r(a,\hat b,c) \to r(a,\hat b,c)$
- $\exists x\,\forall y\,\exists z\, q(x,y,z) \;\Rightarrow\; \forall y\,\exists z\, q(\hat a,y,z)$
### Illegal uses:
#### Example 1: 
$$
\begin{aligned}
1\quad & \exists z\,[\,p(z)\lor q(z)\,] && \text{Given} \\
2\quad & p(\hat b)\lor q(z)            && \text{1 EI [error]} \\
3\quad & p(\hat b)\lor q(\hat b)       && \text{1 EI [correct]}
\end{aligned}
$$
#### Example 2:
$$
\begin{aligned}
1\quad & \exists x\,\exists y\, p(a,x,y) && \text{Given} \\
2\quad & \exists y\, p(a,a,y)            && \text{1 EI [error]}^{[1]}
\end{aligned}
$$
---
[\[1.\]]:
- $a$ already appears in the premise, so it is **not fresh**.  
- **Hat notation** for a fresh witness (e.g., $\hat a$) was not used.
#### Example 3:
$$
\begin{aligned}
\text{1.}\;& \forall x\,\exists y\,(x+y=0)              && \text{Given} \\
\text{2.}\;& \exists y\,(a+y=0)                          && \text{1 UI} \\
\text{3.}\;& a+\hat b=0                                  && \text{2 EG} \\
\text{4.}\;& \forall x\,(x+\hat b=0)                     && \text{3 UG [error]}^{[2]} \\
\text{5.}\;& \exists y\,\forall x\,(x+y=0)               && \text{4 EG}
\end{aligned}
$$
---
[\[2.\]]:
- UG was applied despite the particular constant symbol in line 3.
- This example makes clear why there is a restriction on particular elements in UG. Since *b* represents a particular real number, line 3 cannot be used to conclude that *all real numbers plus b equals 0*. *b* is the witness to line 2, but that is all one knows about it. 