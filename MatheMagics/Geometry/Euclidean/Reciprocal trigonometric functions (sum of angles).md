---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Angle Addition Identity (Cosecant): 
### $\boldsymbol{\csc(x+y)=\dfrac{\csc x\,\sec y\,\csc y\,\sec x}{\csc y\,\sec x+\csc x\,\sec y}.}$
**Assumption:** $\sin(x+y)\neq 0,\ \sin x\neq 0,\ \sin y\neq 0,\ \cos x\neq 0,\ \cos y\neq 0$.

$$
\begin{aligned}
(1)\quad & \csc(x+y)=\frac{1}{\sin(x+y)} \\[6pt]
& \qquad\ \qquad\ =\frac{1}{\sin x\cos y+\sin y\cos x} \\[6pt]
& \qquad\ \qquad\ =\frac{1}{\dfrac{1}{\csc x\,\sec y}+\dfrac{1}{\csc y\,\sec x}} \\[8pt]
& \qquad\ \qquad\ =\frac{1}{\dfrac{\csc y\,\sec x+\csc x\,\sec y}{\csc x\,\sec y\,\csc y\,\sec x}} \\[10pt]
& \qquad\ \qquad\ =\frac{\csc x\,\sec y\,\csc y\,\sec x}{\csc y\,\sec x+\csc x\,\sec y}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \csc(x+y)=\dfrac{\csc x\,\sec y\,\csc y\,\sec x}{\csc y\,\sec x+\csc x\,\sec y}.}
$$
## Angle Addition Identity (Secant): 
### $\boldsymbol{\sec(x+y)=\dfrac{\sec x\,\sec y\,\csc x\,\csc y}{\csc x\,\csc y-\sec x\,\sec y}.}$
**Assumption:** $\cos(x+y)\neq 0,\ \cos x\neq 0,\ \cos y\neq 0,\ \sin x\neq 0,\ \sin y\neq 0$.

$$
\begin{aligned}
(1)\quad & \sec(x+y)=\frac{1}{\cos(x+y)} \\[6pt]
& \qquad\ \qquad\ =\frac{1}{\cos x\cos y-\sin x\sin y} \\[6pt]
& \qquad\ \qquad\ =\frac{1}{\dfrac{1}{\sec x\,\sec y}-\dfrac{1}{\csc x\,\csc y}} \\[8pt]
& \qquad\ \qquad\ =\frac{1}{\dfrac{\csc x\,\csc y-\sec x\,\sec y}{\sec x\,\sec y\,\csc x\,\csc y}} \\[10pt]
& \qquad\ \qquad\ =\frac{\sec x\,\sec y\,\csc x\,\csc y}{\csc x\,\csc y-\sec x\,\sec y}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \sec(x+y)=\dfrac{\sec x\,\sec y\,\csc x\,\csc y}{\csc x\,\csc y-\sec x\,\sec y}.}
$$
## Angle Addition Identity (Cotangent): 
### $\boldsymbol{\cot(x+y)=\dfrac{\cot x\,\cot y-1}{\cot x+\cot y}.}$
**Assumption:** $\sin(x+y)\neq 0,\ \sin x\neq 0,\ \sin y\neq 0$.

$$
\begin{aligned}
(1)\quad & \cot(x+y)=\frac{\cos(x+y)}{\sin(x+y)} \\[6pt]
& \qquad\ \qquad\ =\frac{\cos x\cos y-\sin x\sin y}{\sin x\cos y+\cos x\sin y} \\[8pt]
& \qquad\ \qquad\ =\frac{\dfrac{\cos x}{\sin x}\dfrac{\cos y}{\sin y}-1}{\dfrac{\cos y}{\sin y}+\dfrac{\cos x}{\sin x}} \\[10pt]
& \qquad\ \qquad\ =\frac{\cot x\,\cot y-1}{\cot x+\cot y}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cot(x+y)=\dfrac{\cot x\,\cot y-1}{\cot x+\cot y}.}
$$
