---
down:
  - "[[Heron's formula]]"
tags:
  - mathemagics/geometry/euclidean
---
![[Pasted image 20251213155120.png|300]]## Law of Cosines:

### Notation:
Let $\triangle ABC$ be a (nondegenerate) triangle with side lengths
$a:=BC$, $b:=CA$, $c:=AB$, and opposite angles $A:=\angle A$, $B:=\angle B$, $C:=\angle C$.

## Formulas:

### $\boldsymbol{c^2=a^2+b^2-2ab\cos C.}$
### $\boldsymbol{a^2=b^2+c^2-2bc\cos A.}$
### $\boldsymbol{b^2=c^2+a^2-2ca\cos B.}$

## Proof (for $\boldsymbol{c^2=a^2+b^2-2ab\cos C}$):

**Assumption:** Standard triangle notation above; $a,b,c>0$ and $0<C<\pi$.

Place the triangle in the coordinate plane so that $C=(0,0)$, $B=(a,0)$, and
$$
A=\big(b\cos C,\ b\sin C\big).
$$

Then $c=AB$, so by the distance formula:

$$
\begin{aligned}
(1)\quad & c^2
=(a-b\cos C)^2+(0-b\sin C)^2 \\[6pt]
& \qquad\ \qquad\ =a^2-2ab\cos C+b^2\cos^2 C+b^2\sin^2 C \\[6pt]
& \qquad\ \qquad\ =a^2-2ab\cos C+b^2(\cos^2 C+\sin^2 C) \\[6pt]
& \qquad\ \qquad\ =a^2+b^2-2ab\cos C
\end{aligned}
$$

$$
\boldsymbol{\therefore\ c^2=a^2+b^2-2ab\cos C.}
$$

The other two forms follow by cyclic relabeling of $(a,b,c)$ and $(A,B,C)$.
## When to use (solving triangles):
- **SAS:** Given $a$, $b$, and included angle $C$, compute $c$ via $c^2=a^2+b^2-2ab\cos C$.
- **SSS:** Given $a,b,c$, compute an angle via $\cos C=\dfrac{a^2+b^2-c^2}{2ab}$ (similarly for $A,B$), then finish with Law of Sines if desired.
