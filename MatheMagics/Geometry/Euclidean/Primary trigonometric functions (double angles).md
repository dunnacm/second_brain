---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Double Angle Identity (Sine):
### $\boldsymbol{\sin(2x)=2\sin x\cos x.}$
$$
\begin{aligned}
(1)\quad & \sin(x+y)=\sin x\cos y+\cos x\sin y \\[10pt]
(2)\quad & \sin(2x)=\sin(x+x) \\[6pt]
& \qquad\ \qquad\ =\sin x\cos x+\cos x\sin x \\[6pt]
& \qquad\ \qquad\ =2\sin x\cos x
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \sin(2x)=2\sin x\cos x.}
$$

### $\boldsymbol{\sin(2x)=\dfrac{2\tan x}{1+\tan^2 x}.}$
$$
\begin{aligned}
& \mathsf{Assumption:} \mathtt{\cos\theta\neq 0}\\[10pt]
& (1)\quad \mathtt{\sin(2\theta)=2\cdot \sin\theta\cdot \cos\theta\cdot \dfrac{\cos\theta}{\cos\theta}}\\
& \qquad\ \quad\ \mathtt{=2\cdot \tan\theta\cdot \cos^2\theta}
\\[12pt]
& (2)\quad \mathtt{\tan^2\theta=\dfrac{\sin^2\theta}{\cos^2\theta}}
\\[10pt]
& \Rightarrow (3)\quad \mathtt{\tan^2\theta=\dfrac{1-\cos^2\theta}{\cos^2\theta}}\\
& \qquad\ \quad\ \ \mathtt{\tan^2\theta=\dfrac{1}{\cos^2\theta}-1}
\\[12pt]
& \qquad\ \quad\ \Rightarrow (4)\quad \mathtt{\dfrac{1}{\cos^2\theta}=1+\tan^2\theta}
\\[14pt]
& \mathsf{Sub.\ (4)\ into\ (1):}
\\[10pt]
& (1')\quad \mathtt{\sin(2\theta)=2\cdot \tan\theta\cdot \cos^2\theta}\\
& \qquad\ \quad\ \mathtt{=\dfrac{2\tan\theta}{1+\tan^2\theta}}\\[14pt]
& \boldsymbol{\therefore\ \mathtt{\sin(2\theta)=\dfrac{2\tan\theta}{1+\tan^2\theta}}.}
\end{aligned}
$$

## Double Angle Identity (Cosine):
### $\boldsymbol{\cos(2x)=\cos^2 x-\sin^2 x.}$
$$
\begin{aligned}
(1)\quad & \cos(x+y)=\cos x\cos y-\sin x\sin y \\[10pt]
(2)\quad & \cos(2x)=\cos(x+x) \\[6pt]
& \qquad\ \qquad\ =\cos x\cos x-\sin x\sin x \\[6pt]
& \qquad\ \qquad\ =\cos^2 x-\sin^2 x
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(2x)=\cos^2 x-\sin^2 x.}
$$
### $\boldsymbol{\cos(2x)=2\cos^2 x-1.}$
$$
\begin{aligned}
(1)\quad & \cos(2x)=\cos^2 x-\sin^2 x \\[6pt]
& \qquad\ \qquad\ =\cos^2 x-(1-\cos^2 x) \\[6pt]
& \qquad\ \qquad\ =2\cos^2 x-1
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(2x)=2\cos^2 x-1.}
$$
### $\boldsymbol{\cos(2x)=1-2\sin^2 x.}$
$$
\begin{aligned}
(1)\quad & \cos(2x)=\cos^2 x-\sin^2 x \\[6pt]
& \qquad\ \qquad\ =(1-\sin^2 x)-\sin^2 x \\[6pt]
& \qquad\ \qquad\ =1-2\sin^2 x
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(2x)=1-2\sin^2 x.}
$$
### $\boldsymbol{\cos(2x)=\dfrac{1-\tan^2 x}{1+\tan^2 x}.}$
**Assumption:** $\cos x\neq 0$.

$$
\begin{aligned}
(1)\quad & \cos(2x)=\cos^2 x-\sin^2 x \\[6pt]
& \qquad\ \qquad\ =\cos^2 x\left(1-\dfrac{\sin^2 x}{\cos^2 x}\right) \\[6pt]
& \qquad\ \qquad\ =\cos^2 x(1-\tan^2 x) \\[10pt]
(2)\quad & 1+\tan^2 x=\dfrac{1}{\cos^2 x}
\quad \Rightarrow \quad
\cos^2 x=\dfrac{1}{1+\tan^2 x} \\[10pt]
(3)\quad & \cos(2x)=\dfrac{1}{1+\tan^2 x}(1-\tan^2 x)
=\dfrac{1-\tan^2 x}{1+\tan^2 x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(2x)=\dfrac{1-\tan^2 x}{1+\tan^2 x}.}
$$
## Double Angle Identity (Tangent):
### $\boldsymbol{\tan(2x)=\dfrac{2\tan x}{1-\tan^2 x}.}$
**Assumption:** $\cos x\neq 0$ and $1-\tan^2 x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan(2x)=\dfrac{\sin(2x)}{\cos(2x)} \\[10pt]
(2)\quad & \tan(2x)=\dfrac{2\sin x\cos x}{\cos^2 x-\sin^2 x} \\[6pt]
& \qquad\ \qquad\ =\dfrac{2\left(\dfrac{\sin x}{\cos x}\right)}{1-\left(\dfrac{\sin x}{\cos x}\right)^2} \\[10pt]
& \qquad\ \qquad\ =\dfrac{2\tan x}{1-\tan^2 x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan(2x)=\dfrac{2\tan x}{1-\tan^2 x}.}
$$
