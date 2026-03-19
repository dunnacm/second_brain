---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Half Angle Identity (Sine):
### $\boldsymbol{\sin^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{2}.}$
$$
\begin{aligned}
(1)\quad & \cos(2u)=1-2\sin^2 u \\[10pt]
(2)\quad & \text{Let }u=\dfrac{x}{2}\ \Rightarrow\ \cos x=1-2\sin^2\!\left(\dfrac{x}{2}\right) \\[10pt]
(3)\quad & 2\sin^2\!\left(\dfrac{x}{2}\right)=1-\cos x \\[6pt]
& \qquad\ \qquad\ \Rightarrow\ \sin^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{2}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \sin^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{2}.}
$$
## Half Angle Identity (Cosine):
### $\boldsymbol{\cos^2\!\left(\dfrac{x}{2}\right)=\dfrac{1+\cos x}{2}.}$
$$
\begin{aligned}
(1)\quad & \cos(2u)=2\cos^2 u-1 \\[10pt]
(2)\quad & \text{Let }u=\dfrac{x}{2}\ \Rightarrow\ \cos x=2\cos^2\!\left(\dfrac{x}{2}\right)-1 \\[10pt]
(3)\quad & 2\cos^2\!\left(\dfrac{x}{2}\right)=1+\cos x \\[6pt]
& \qquad\ \qquad\ \Rightarrow\ \cos^2\!\left(\dfrac{x}{2}\right)=\dfrac{1+\cos x}{2}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos^2\!\left(\dfrac{x}{2}\right)=\dfrac{1+\cos x}{2}.}
$$



## Half Angle Identity (Tangent):
### $\boldsymbol{\tan^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{1+\cos x}.}$
**Assumption:** $1+\cos x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan^2\!\left(\dfrac{x}{2}\right)
=\dfrac{\sin^2\!\left(\dfrac{x}{2}\right)}{\cos^2\!\left(\dfrac{x}{2}\right)} \\[10pt]
(2)\quad & \tan^2\!\left(\dfrac{x}{2}\right)
=\dfrac{\dfrac{1-\cos x}{2}}{\dfrac{1+\cos x}{2}} \\[10pt]
(3)\quad & \tan^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{1+\cos x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan^2\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{1+\cos x}.}
$$


### $\boldsymbol{\tan\!\left(\dfrac{x}{2}\right)=\dfrac{\sin x}{1+\cos x}.}$
**Assumption:** $1+\cos x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan\!\left(\dfrac{x}{2}\right)=\dfrac{\sin\!\left(\dfrac{x}{2}\right)}{\cos\!\left(\dfrac{x}{2}\right)} \\[10pt]
(2)\quad & \dfrac{\sin x}{1+\cos x}
=\dfrac{2\sin\!\left(\dfrac{x}{2}\right)\cos\!\left(\dfrac{x}{2}\right)}{1+\big(2\cos^2\!\left(\dfrac{x}{2}\right)-1\big)} \\[10pt]
(3)\quad & \dfrac{\sin x}{1+\cos x}
=\dfrac{2\sin\!\left(\dfrac{x}{2}\right)\cos\!\left(\dfrac{x}{2}\right)}{2\cos^2\!\left(\dfrac{x}{2}\right)}
=\dfrac{\sin\!\left(\dfrac{x}{2}\right)}{\cos\!\left(\dfrac{x}{2}\right)}
=\tan\!\left(\dfrac{x}{2}\right)
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan\!\left(\dfrac{x}{2}\right)=\dfrac{\sin x}{1+\cos x}.}
$$


### $\boldsymbol{\tan\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{\sin x}.}$
**Assumption:** $\sin x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan\!\left(\dfrac{x}{2}\right)=\dfrac{\sin x}{1+\cos x} \\[10pt]
(2)\quad & \tan\!\left(\dfrac{x}{2}\right)
=\dfrac{\sin x}{1+\cos x}\cdot\dfrac{1-\cos x}{1-\cos x} \\[10pt]
(3)\quad & \tan\!\left(\dfrac{x}{2}\right)
=\dfrac{\sin x(1-\cos x)}{1-\cos^2 x}
=\dfrac{\sin x(1-\cos x)}{\sin^2 x}
=\dfrac{1-\cos x}{\sin x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{\sin x}.}
$$


### $\boldsymbol{\tan\!\left(\dfrac{x}{2}\right)=\csc x-\cot x.}$
**Assumption:** $\sin x\neq 0$.

$$
\begin{aligned}
(1)\quad & \csc x-\cot x=\dfrac{1}{\sin x}-\dfrac{\cos x}{\sin x} \\[10pt]
(2)\quad & \csc x-\cot x=\dfrac{1-\cos x}{\sin x} \\[10pt]
(3)\quad & \tan\!\left(\dfrac{x}{2}\right)=\dfrac{1-\cos x}{\sin x}
\quad \Rightarrow\quad
\tan\!\left(\dfrac{x}{2}\right)=\csc x-\cot x
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan\!\left(\dfrac{x}{2}\right)=\csc x-\cot x.}
$$


### $\boldsymbol{\tan\!\left(\dfrac{x}{2}\right)=\dfrac{\tan x}{1+\sec x}.}$
**Assumption:** $\cos x\neq 0$ and $1+\sec x\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan\!\left(\dfrac{x}{2}\right)=\dfrac{\sin x}{1+\cos x} \\[10pt]
(2)\quad & \tan\!\left(\dfrac{x}{2}\right)
=\dfrac{\dfrac{\sin x}{\cos x}}{\dfrac{1+\cos x}{\cos x}}
=\dfrac{\tan x}{\sec x+1}
=\dfrac{\tan x}{1+\sec x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan\!\left(\dfrac{x}{2}\right)=\dfrac{\tan x}{1+\sec x}.}
$$


### $\boldsymbol{\tan\!\left(\dfrac{x}{2}\right)=\dfrac{-1\pm\sqrt{1+\tan^2 x}}{\tan x}.}$
**Assumption:** $\tan x\neq 0$.

$$
\begin{aligned}
(1)\quad & \text{Let }t:=\tan\!\left(\dfrac{x}{2}\right) \\[10pt]
(2)\quad & \tan x=\tan\!\big(2\cdot\dfrac{x}{2}\big)
=\tan(2\cdot \arctan t)
=\dfrac{2t}{1-t^2} \\[10pt]
(3)\quad & \tan x(1-t^2)=2t \\[6pt]
& \qquad\ \qquad\ \Rightarrow\ \tan x\,t^2+2t-\tan x=0 \\[10pt]
(4)\quad & t=\dfrac{-2\pm\sqrt{4+4\tan^2 x}}{2\tan x}
=\dfrac{-1\pm\sqrt{1+\tan^2 x}}{\tan x}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan\!\left(\dfrac{x}{2}\right)=\dfrac{-1\pm\sqrt{1+\tan^2 x}}{\tan x}.}
$$
