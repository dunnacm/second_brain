---
down:
  - "[[Universal generalization (UG)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
> [!note]+ **Arbitrary constant symbol**
>
> > [!warning] **IF**
> > - $p(x)$ is an $\mathcal{S}$-**formula** 
> > - $p(x)$ contains no particular constants (e.g., $\hat a$)
> > - A constant symbol $a$ first appears in the proof by **UI** (i.e.,  $\forall x\, p(x) \Rightarrow p(a)$)
>
> > [!tip] **THEN**
> > - $a$ is an **arbitrary** constant symbol.
>
>It may later be applied to **UG** to obtain $\forall x\, p(x)$ from $p(a)$, provided no particular constants occur in $p(x)$.
## Examples:
### Not arbitrary:
$$
\begin{aligned}
\text{1.}\;& p(a) && \text{Given} \\
\text{2.}\;& p(a)\lor q(a) && \text{Add}
\end{aligned}
$$
The constant symbol*a* in the previous example is **not arbitrary** because its first occurrence of of *a* in line 1 is not the result of **UI**.
Therefore, these two lines should be written using $\hat a$:
$$
\begin{aligned}
\text{1.}\;& p(\hat a) && \text{Given} \\
\text{2.}\;& p(\hat a)\lor q(\hat a) && \text{Add}
\end{aligned}
$$
### Arbitrary:
$$
\begin{aligned}
\text{1.}\;& \forall x\, p(x) && \text{Given} \\
\text{2.}\;& p(a)            && \text{1 UI} \\
\text{3.}\;& p(a)\lor q(a)   && \text{Add}
\end{aligned}
$$
