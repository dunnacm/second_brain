---
down:
  - "[[Examples (trigonometric equations)]]"
tags:
  - mathemagics/geometry/euclidean
---
## Methods:
### Auxiliary angle method (R-sine / phase-shift)
$$
\begin{aligned}
& \text{Solve }a\cos\theta+b\sin\theta=c,\ \text{where }(a,b)\ne(0,0). \\[12pt]
& \text{Let }R:=\sqrt{a^2+b^2}\ (>0). \\[10pt]
& \text{Choose }\phi\text{ so that }\sin\phi=\dfrac{a}{R}\ \text{and }\cos\phi=\dfrac{b}{R}. \\[18pt]
& a\cos\theta+b\sin\theta=c \\[10pt]
& \Longleftrightarrow\ a\cos\theta+b\sin\theta=Rc \\[10pt]
& \Longleftrightarrow\ \dfrac{a}{R}\cos\theta+\dfrac{b}{R}\sin\theta=\dfrac{c}{R} \\[10pt]
& \Longleftrightarrow\ \sin\phi\cos\theta+\cos\phi\sin\theta=\dfrac{c}{R} \\[10pt]
& \Longleftrightarrow\ \sin(\theta+\phi)=\dfrac{c}{R}. \\[18pt]
& \text{Therefore:} \\[10pt]
& \qquad\ \qquad \text{If }\left|\dfrac{c}{R}\right|>1,\ \text{there is no real solution.} \\[10pt]
& \qquad\ \qquad \text{If }\left|\dfrac{c}{R}\right|\le 1,\ \text{let }\alpha:=\sin^{-1}\!\left(\dfrac{c}{R}\right). \\[10pt]
& \qquad\ \qquad \text{Then the solutions are} \\[10pt]
& \qquad\ \qquad\qquad \theta=-\phi+\alpha+2k\pi \quad \text{or}\quad \theta=-\phi+(\pi-\alpha)+2k\pi,\qquad k\in\mathbb{Z}.
\end{aligned}
$$