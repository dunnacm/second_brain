---
down:
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definitions:
### Closed set — via Complement of open

> [!note]+ **Definition 3.2.2 (Abbott) — Closed set (via complement of open)**
> > [!warning]+ **IF**
> > $F\subseteq\mathbb{R}$.
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \begin{aligned}
> > F \text{ is closed}
> > &\ \Leftrightarrow\ \mathbb{R}\setminus F \text{ is open} \Leftrightarrow\ \forall x\in \mathbb{R}\setminus F\ \exists \varepsilon>0\,[\,V_\varepsilon(x)\subseteq \mathbb{R}\setminus F\,]
> > \\[10pt]
> > &\ \Leftrightarrow\ F^c \text{ is open} \Leftrightarrow\ \forall x\in F^c\ \exists \varepsilon>0\,[\,V_\varepsilon(x)\subseteq F^c\,].
> > \\[6pt]
> > \end{aligned}
> > $$

### Closed set — via Limit points

> [!note]+ **Definition 3.2.3 (Abbott) — Closed set (via limit points)**
> > [!warning]+ **IF**
> > $F\subseteq\mathbb{R}$.
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \begin{aligned}
> > F \text{ is closed}
> > &\ \Leftrightarrow\
> > \forall x\in\mathbb{R}\ \Big[\,
> > \big(\forall \varepsilon>0\ \exists y\in F\ (y\neq x \land |y-x|<\varepsilon)\big)
> > \ \Rightarrow\
> > x\in F
> > \Big]
> > \\[10pt]
> > &\ \Leftrightarrow\
> > F'\subseteq F.
> > \end{aligned}
> > $$
> 
> Where $F':=\big\{\,x\in\mathbb{R}:\forall \varepsilon>0\ \exists y\in F\ (y\neq x \land |y-x|<\varepsilon)\big\}.$





