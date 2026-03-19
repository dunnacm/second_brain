---
down:
  - "[[Exercises (law of sines)]]"
tags:
  - mathemagics/geometry/euclidean
---
## Law of Sines:
### $\boldsymbol{\dfrac{\sin A}{a}=\dfrac{\sin B}{b}=\dfrac{\sin C}{c}.}$
### SSA (Ambiguous Cases) using the Law of Sines
Why ambiguity at all? because $\sin(x) = \sin(x + \pi /2)$ for x < $\pi / 2$
#### Case 1: One triangle (from two possible)

| $\angle A$ is acute                       | $\angle A$ is obtuse                      |
| ----------------------------------------- | ----------------------------------------- |
| ![[Pasted image 20251212182648.png\|200]] | ![[Pasted image 20251212182925.png\|230]] |
| $h=b\sin A$<br>$a>h \quad \wedge \quad a>b$ | $a>b$                                     |


#### Case 2: Two triangles (from two possible)

![[Pasted image 20251212183651.png|270]]

$h=b\sin A \quad \wedge \quad h<a<b$


#### Case 3: No triangle (from two possible)

| $\angle A$ is acute                       | $\angle A$ is obtuse                      |
| ----------------------------------------- | ----------------------------------------- |
| ![[Pasted image 20251212181502.png\|200]] | ![[Pasted image 20251212181601.png\|280]] |
| $h=b\sin A$<br>$a<h$                      | $a\le b$                                  |
With $h=b\sin A$:

> [!abstract]+ Summary
> - If $A$ is **acute**:
  >	- $a<h$  $\Rightarrow$ no triangle
  >	- $a=h$  $\Rightarrow$ one triangle (right triangle)
  >	- $h<a<b$ $\Rightarrow$ two triangles
  >	- $a\ge b$ $\Rightarrow$ one triangle
>- If $A$ is **obtuse**:
  >	- $a\le b$ $\Rightarrow$ no triangle
  >	- $a>b$ $\Rightarrow$ one triangle

