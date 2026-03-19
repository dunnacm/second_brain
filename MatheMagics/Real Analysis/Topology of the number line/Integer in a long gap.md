---
down:
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definition:

> [!note]+ **Integer in a long gap**
> > [!warning]+ **IF**
> > $b-a>1$
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \exists\,z\in\mathbb{Z}\ [\,a<c<b\,].
> > $$

## Proof:
$$
\begin{aligned}
& \text{Assumption: } (1)\ \ b-a>1 \ \Rightarrow\ b>1+a.
\end{aligned}
$$

Floor-ceiling fact:

$$
\begin{aligned}
(2)\quad 
& z\le a<z+1,\ z\in\mathbb{Z}
\\[6pt]
& z\le a\ \land\ a<z+1,\ z\in\mathbb{Z}
\\[6pt]
& z+1\le a+1\ \land\ a<z+1,\ z\in\mathbb{Z}
\\[6pt]
& z+1\le a+1<b\ \land\ a<z+1,\ z\in\mathbb{Z}
\qquad (\text{sub. } b>1+a)
\\[6pt]
& a<z+1\le a+1<b,\ z\in\mathbb{Z}
\\[6pt]
& a<z+1<b,\ z\in\mathbb{Z}
\\[6pt]
& a<c<b,\ c\in\mathbb{Z}\qquad (\text{let } c:=z+1)
\end{aligned}
$$
