---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Introduction:
Before writing formal proofs, one needs a rule that will **attach** a universal quantifier. It does not have an "iff" relationship with *universal instantiation*, for it requires a criterion on the constant. 
## Definition:
> [!note] **Inference Rule 2.3.8 — Universal Generalization (UG)**
>
> > [!warning] **IF**
> > - $p(x)$ is an $\mathcal{S}$-**formula**.
> > - $a \in \overline{S}$ is an **arbitrary** constant
> > > - its first occurrence was by **UI** or otherwise marked arbitrary; .
> > - $a$ does **not** occur in any **open assumption** in the proof up to this line.
> > - **no particular/fresh** constants occur in $p(x)$)
> > 
>
> > [!tip] **THEN**
> >  $p(a) \Rightarrow \forall x\, p(x)$.
> 
> - **UG** lifts a statement proved for an **arbitrary** element to “**for all**” elements.
> - If needed, replacing $a$ by a variable $x$ yields $p(x)$ with $x$ **free** where $a$ occurred (no variable capture).

## Examples:
### Legal uses:
Consider the following argument:
	*All squares are rectangles*
	*All rectangles are quadrilaterals*
Representing the the premises as a formal proof:
$$
\begin{aligned}
\text{1.}\;& \forall x\,[\, s(x) \to r(x) \,] && \text{Given} \\
\text{2.}\;& \forall x\,[\, r(x) \to q(x) \,] && \text{Given} \\
\text{3.}\;& s(a) \to r(a)                   && \text{1 UI} \\
\text{4.}\;& r(a) \to q(a)                   && \text{2 UI} \\
\text{5.}\;& s(a) \to q(a)                   && \text{3,4 HS} \\
\text{6.}\;& \forall x\,(\, s(x) \to q(x) \,) && \text{5 UG}
\end{aligned}
$$

Since *a* was introduced in line 3 by **UI**, it is an arbitrary constant symbol.
In addition $s(a) \rightarrow q(a)$ contains no particular constant symbols that appeared in the proof by substitution. 
Hence, the application of **UG** in line 6 is legal.
Interpreting the conclusion, given the premises, is that *all squares are quadrilaterals*.
### Illegal uses:
#### Example 1:
Let $p(x)$ be an $\mathcal{S}$-formula with $c$ a constant symbol.

$$
\begin{aligned}
\text{1.}\;& p(c) && \text{Given} \\
\text{2.}\;& \forall x\, p(x) && \text{1 UG [error]}
\end{aligned}
$$

The constant symbol $c$ in line 1 is particular, even without being written as $\hat c$. It was not introduced to the proof by UI. Therefore, universal generalization does not apply.
#### Example 2:
Suppose that $a$ is an arbitrary constant symbol.

$$
\begin{aligned}
\text{1.}\;& a+\hat{b}=0 \\
\text{2.}\;& \forall x\,(x+\hat{b}=0) && \text{1 UG [error]}
\end{aligned}
$$

The restriction against $p(x)$ containing particular symbols prevents the errant conclusion in line 2.
#### Example 3:
The following is an attempt to prove $\forall x \forall y (x+y=2\cdot x)$ from the formula $\forall x(x+x=2\cdot x)$.

$$
\begin{aligned}
\text{1.}\;& \forall x(x+x=2\cdot x) && \text{Given} \\
\text{2.}\;& a+a=2\cdot a           && \text{1 UI} \\
\text{3.}\;& \forall y(a+y=2\cdot a) && \text{2 UG [error]} \\
\text{4.}\;& \forall x\forall y(x+y=2\cdot x) && \text{3 UG}
\end{aligned}
$$

Although the constant symbol $a$ in line 2 is arbitrary, the proof is not valid. The reason is that an illegal substitution was made in line 3.
#### Example 4:

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
- Refer to [[Universal generalization (UG)#Exercise 3|exercise 3]] in the illustrations section for a correction
## Illustrations:
### Exercise 1:
$\text { Prove: } \quad \forall x \forall y p(x, y) \vdash \forall y \forall x p(x, y)$
$$
\begin{aligned}
1\quad & \forall x\,\forall y\, p(x,y)        && \text{Given} \\
2\quad & \forall y\, p(a,y)                   && \text{1 UI} \\
3\quad & p(a,b)                                && \text{2 UI} \\
4\quad & \forall x\, p(x,b)                    && \text{3 UG} \\
5\quad & \forall y\,\forall x\, p(x,y)         && \text{4 UG}
\end{aligned}
$$
Since both _a_ and _b_ appear by **UI**, they are **arbitrary**, so **UG** may be applied to each.
### Exercise 2:
$\text { Prove: } \forall x[p(x) \rightarrow q(x)], \forall x \neg[q(x) \vee r(x)] \vdash \forall x \neg p(x)$
$$
\begin{aligned}
1\quad & \forall x\,[\, p(x) \to q(x) \,]          && \text{Given} \\
2\quad & \forall x\, \neg[\, q(x) \lor r(x) \,]    && \text{Given} \\
3\quad & p(a) \to q(a)                              && \text{1 UI} \\
4\quad & \neg[\, q(a) \lor r(a) \,]                 && \text{2 UI} \\
5\quad & \neg q(a) \land \neg r(a)                  && \text{4 DeM} \\
6\quad & \neg q(a)                                  && \text{5 Simp} \\
7\quad & \neg p(a)                                  && \text{3,6 MT} \\
8\quad & \forall x\, \neg p(x)                      && \text{7 UG}
\end{aligned}
$$
The constant *a* first appears by **UI** at *3*, so *a* is **arbitrary** and **UG** at *8* is legal.
### Exercise 3:
Correction of [[Universal generalization (UG)#Example 4 correction|example 4]], in the illegal uses section. 
$$
\begin{aligned}
\text{1.}\;& \forall x\,\exists y\, (x+y=0) && \text{Given} \\
\text{2.}\;& \exists y\, (a+y=0)             && \text{1 UI} \\
\text{3.}\;& a+\hat b = 0                    && \text{2 EI} \\
\text{4.}\;& \exists y\, (a+y=0)             && \text{3 EG} \\
\text{5.}\;& \forall x\,\forall y\, (x+y=0)  && \text{4 UG}
\end{aligned}
$$
Notice that there is no particular constant symbol in line 4, so line 5 is legally followed by UG