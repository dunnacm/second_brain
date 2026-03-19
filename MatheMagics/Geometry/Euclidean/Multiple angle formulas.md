---
down:
  - "[[Multiple angle formulas (specific cases)]]"
tags:
  - mathemagics/geometry/euclidean
---
## Preliminaries:
### Chebyshev Polynomial (First Kind): $\boldsymbol{T_n}$
$$
T_n(x)
=
\begin{vmatrix}
x & 1 & 0 & 0 & \cdots & 0 \\
1 & 2x & 1 & 0 & \ddots & \vdots \\
0 & 1 & 2x & 1 & \ddots & 0 \\
0 & 0 & 1 & 2x & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & \ddots & 1 \\
0 & \cdots & 0 & 0 & 1 & 2x
\end{vmatrix}
$$
### Chebyshev Polynomial (Second Kind): $\boldsymbol{U_n}$
$$
U_n(x)
=
\begin{vmatrix}
2x & 1 & 0 & 0 & \cdots & 0 \\
1 & 2x & 1 & 0 & \ddots & \vdots \\
0 & 1 & 2x & 1 & \ddots & 0 \\
0 & 0 & 1 & 2x & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & \ddots & 1 \\
0 & \cdots & 0 & 0 & 1 & 2x
\end{vmatrix}
$$
## Formulas:
### Version 1:
#### $\boldsymbol{\sin(nx)=\sin x\cdot U_{n-1}(\cos x).}$
#### $\boldsymbol{\cos(nx)=T_n(\cos x).}$

### Version 2:
#### $\boldsymbol{\sin(nx)\big|_{n=1,3,5,\dots}=(-1)^{\frac{n}{2}-\frac{1}{2}}\,T_n(\sin x).}$
#### $\boldsymbol{\sin(nx)\big|_{n=2,4,6,\dots}=(-1)^{\frac{n}{2}-\frac{2}{2}}\,\cos x\cdot U_{n-1}(\sin x).}$

#### $\boldsymbol{\cos(nx)\big|_{n=1,3,5,\dots}=(-1)^{\frac{n}{2}-\frac{1}{2}}\,\cos x\cdot U_{n-1}(\sin x).}$
#### $\boldsymbol{\cos(nx)\big|_{n=2,4,6,\dots}=(-1)^{\frac{n}{2}}\,T_n(\sin x).}$
