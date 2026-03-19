---
down:
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
> [!note]+ **Definition — Boundary of a set**
> > [!warning]+ **IF**
> > $A\subseteq\mathbb{R}$.
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \begin{aligned}
> > \partial_{\mathbb{R}}A
> > &\;=\;\{\,x\in\mathbb{R} : x \text{ is a boundary point of } A\,\}
> > \\[6pt]
> > &\;=\;\{\,x\in\mathbb{R} : \forall \varepsilon>0\,[\,V_\varepsilon(x)\cap A\neq\varnothing \ \land\ V_\varepsilon(x)\cap (\mathbb{R}\setminus A)\neq\varnothing\,]\,\}
> > \\[6pt]
> > &\;=\;\operatorname{cl}_{\mathbb{R}}(A)\setminus \operatorname{int}_{\mathbb{R}}(A).
> > \end{aligned}
> > $$
