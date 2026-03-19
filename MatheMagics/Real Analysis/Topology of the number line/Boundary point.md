---
down:
  - "[[Boundary of a set (∂A)]]"
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
> [!note]+ **Definition — Boundary point**
> > [!warning]+ **IF**
> > - $A\subseteq\mathbb{R}$,
> > - $x\in\mathbb{R}$.
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \begin{aligned}
> > x\in\partial_{\mathbb{R}}A
> > &\ \Leftrightarrow\ x\in\partial A
> > \\[6pt]
> > &\ \Leftrightarrow\ x \text{ is a boundary point of } A
> > \\[6pt]
> > &\ \Leftrightarrow\ \forall \varepsilon>0\,[\,V_\varepsilon(x)\cap A\neq\varnothing \ \land\ V_\varepsilon(x)\cap A^c\neq\varnothing\,]
> > \\[6pt]
> > &\ \Leftrightarrow\ \forall \varepsilon>0\,[\,V_\varepsilon(x)\cap A\neq\varnothing \ \land\ V_\varepsilon(x)\cap (\mathbb{R}\setminus A)\neq\varnothing\,].
> > \end{aligned}
> > $$
