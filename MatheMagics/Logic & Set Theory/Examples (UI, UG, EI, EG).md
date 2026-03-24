---
down:
  - "[[Universal instantiation (UI)]]"
  - "[[Universal generalization (UG)]]"
  - "[[Existential instantiation (EI)]]"
  - "[[Existential generalization (EG)]]"
  - "[[Continuity (function)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Example 1:
$\text { Prove: } \exists x[p(x) \wedge q(x)], \forall x[p(x) \rightarrow r(x)] \vdash \exists x r(x)$
$$
\begin{aligned}
1\quad & \exists x\,[\, p(x)\land q(x)\,] && \text{Given} \\
2\quad & \forall x\,[\, p(x)\to r(x)\,]   && \text{Given} \\
3\quad & p(\hat a)\land q(\hat a)         && \text{1 EI} \\
4\quad & p(\hat a)\to r(\hat a)           && \text{2 UI} \\
5\quad & p(\hat a)                         && \text{3 Simp} \\
6\quad & r(\hat a)                         && \text{4,5 MP} \\
7\quad & \exists x\, r(x)                  && \text{6 EG}
\end{aligned}
$$

## Example 2:
$\text { Prove: } \forall x \exists y[q(x) \wedge t(y)] \vdash \forall x[q(x) \wedge(\exists y) t(y)]$
$$
\begin{aligned}
1\quad & \forall x\,\exists y\,[\, q(x) \land t(y) \,]          && \text{Given} \\
2\quad & \exists y\,[\, q(a) \land t(y) \,]                      && \text{1 UI} \\
3\quad & q(a) \land t(\hat b)                                    && \text{2 EI} \\
4\quad & t(\hat b) \land q(a)                                    && \text{3 Com} \\
5\quad & t(\hat b)                                               && \text{4 Simp} \\
6\quad & \exists y\, t(y)                                        && \text{5 EG} \\
7\quad & q(a)                                                    && \text{3 Simp} \\
8\quad & q(a) \land \exists y\, t(y)                              && \text{7,6 Conj} \\
9\quad & \forall x\,[\, q(x) \land \exists y\, t(y) \,]          && \text{8 UG}
\end{aligned}
$$

## Example 3:
$\text { Prove : } p(a) \rightarrow \exists x[q(x) \wedge r(x)], p(a) \vdash \exists x r(x)$
$$
\begin{aligned}
1\quad & p(a)\ \rightarrow\ \exists x\,[\,q(x)\land r(x)\,] && \text{Given} \\
2\quad & p(a)                                              && \text{Given} \\
3\quad & p(a)\ \rightarrow\ \big(q(\hat b)\land r(\hat b)\big) && \text{1 EI} \\
4\quad & q(\hat b)\land r(\hat b)                          && \text{2,3 MP} \\
5\quad & r(\hat b)\land q(\hat b)                          && \text{4 Com} \\
6\quad & r(\hat b)                                         && \text{5 Simp} \\
7\quad & \exists x\, r(x)                                  && \text{6 EG}
\end{aligned}
$$
## Example 4:
 $\neg \forall x p(x) \Leftrightarrow \forall x \neg p(x)$
## Example 5:
$\neg \exists x p(x) \Leftrightarrow \neg \forall x p(x)$
## Example 6:
$\forall x \neg p(x) \Leftrightarrow \exists x p(x)$
## Example 7:
$\exists x[p(x) \rightarrow q(x)] \Leftrightarrow \neg \forall x[\neg p(x) \rightarrow \neg q(x)]$
## Example 8:
$\neg \forall x \exists y p(x, y) \Leftrightarrow \exists x \forall y \neg p(x, y)$
## Example 9:
$\neg \forall x \exists y p(x, y) \Leftrightarrow \exists y \forall x p(x, y)$
## Example 10:
Let $f$ be a function and $c$ be a real number in the open interval $I$. Then, $f$ is **[[Continuity (function)|continuous]]** at $c$ if for every $\epsilon>0$, there exists $\delta>0$ such that for all $x$ in $I$, if $0<|x-c|<\delta$, then $|f(x)-f(c)|<\epsilon$.
	**(a)** Write what it means for $f$ to be not continuous at $c$.
	**(b)** The function $f$ is continuous on an open interval if it is continuous at every point of the interval. Write what it means for $f$ to be not continuous on an open interval.
## Example 11:
Let $f$ be a function and $c$ a real number in the open interval $I$. Then, $f$ is **[[Uniform continuity|uniformly continuous]]** on $I$ means that for every $\epsilon>0$, there exists $\delta>0$ such that for all $c$ and $x$ in $I$, if $0<|x-c|<\delta$, then $|f(x)-f(c)|<\epsilon$.
	**(a)** Write what it means for $f$ to be not uniformly continuous on $I$.
	**(b)** How does $f$ being continuous on $I$ differ from $f$ being uniformly continuous on $I$ ?