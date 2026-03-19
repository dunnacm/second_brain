---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Triple Angle Identity (Sine):
### $\boldsymbol{\sin(3x)=3\sin x-4\sin^3 x.}$

$$
\begin{aligned}
(1)\quad & \sin(3x)=\sin(2x+x) \\[10pt]
(2)\quad & \sin(3x)=\sin(2x)\cos x+\cos(2x)\sin x \\[6pt]
& \qquad\ \qquad\ =(2\sin x\cos x)\cos x+(1-2\sin^2 x)\sin x \\[6pt]
& \qquad\ \qquad\ =2\sin x\cos^2 x+\sin x-2\sin^3 x \\[6pt]
& \qquad\ \qquad\ =2\sin x(1-\sin^2 x)+\sin x-2\sin^3 x \\[6pt]
& \qquad\ \qquad\ =3\sin x-4\sin^3 x
\end{aligned}
$$
$$
\boldsymbol{\therefore\ \sin(3x)=3\sin x-4\sin^3 x.}
$$
## Triple Angle Identity (Cosine):
### $\boldsymbol{\cos(3x)=4\cos^3 x-3\cos x.}$

$$
\begin{aligned}
(1)\quad & \cos(3x)=\cos(2x+x) \\[10pt]
(2)\quad & \cos(3x)=\cos(2x)\cos x-\sin(2x)\sin x \\[6pt]
& \qquad\ \qquad\ =(2\cos^2 x-1)\cos x-(2\sin x\cos x)\sin x \\[6pt]
& \qquad\ \qquad\ =2\cos^3 x-\cos x-2\sin^2 x\cos x \\[6pt]
& \qquad\ \qquad\ =2\cos^3 x-\cos x-2(1-\cos^2 x)\cos x \\[6pt]
& \qquad\ \qquad\ =4\cos^3 x-3\cos x
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(3x)=4\cos^3 x-3\cos x.}
$$
## Triple Angle Identity (Tangent):
### $\boldsymbol{\tan(3x)=\dfrac{3\tan x-\tan^3 x}{1-3\tan^2 x}.}$
**Assumption:** $\cos x\neq 0$, $1-\tan^2 x\neq 0$, and $1-3\tan^2 x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan(3x)=\tan(2x+x)
=\dfrac{\tan(2x)+\tan x}{1-\tan(2x)\tan x} \\[10pt]
(2)\quad & \tan(2x)=\dfrac{2\tan x}{1-\tan^2 x} \\[10pt]
(3)\quad & \tan(3x)
=\dfrac{\dfrac{2\tan x}{1-\tan^2 x}+\tan x}{1-\left(\dfrac{2\tan x}{1-\tan^2 x}\right)\tan x} \\[10pt]
(4)\quad & \tan(3x)
=\dfrac{\dfrac{2\tan x+\tan x(1-\tan^2 x)}{1-\tan^2 x}}
{\dfrac{1-\tan^2 x-2\tan^2 x}{1-\tan^2 x}} \\[12pt]
(5)\quad & \tan(3x)=\dfrac{3\tan x-\tan^3 x}{1-3\tan^2 x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan(3x)=\dfrac{3\tan x-\tan^3 x}{1-3\tan^2 x}.}
$$
