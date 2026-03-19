---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Formulas:
### Angle Addition Identity (Sine): 
#### $\boldsymbol{\sin(x+y)=\sin x\cos y+\cos x\sin y.}$

##### Proof 1: Complex analysis
**Assumption:** $i^2=-1$ and $e^{it}=\cos t+i\sin t$ for all $t\in\mathbb{R}$.

$$
\begin{aligned}
(1)\quad & e^{i(x+y)}=e^{ix}e^{iy} \\[6pt]
& \qquad\ \qquad\ =(\cos x+i\sin x)(\cos y+i\sin y) \\[6pt]
& \qquad\ \qquad\ =(\cos x\cos y-\sin x\sin y)+i(\sin x\cos y+\cos x\sin y) \\[6pt]
& \qquad\ \qquad\ =\cos(x+y)+i\sin(x+y) \\[10pt]
(2)\quad & \sin(x+y)=\sin x\cos y+\cos x\sin y
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \sin(x+y)=\sin x\cos y+\cos x\sin y.}
$$

##### Proof 2: Matrices
**Assumption:** For $t\in\mathbb{R}$, let
$$
R(t):=
\begin{pmatrix}
\cos t & -\sin t\\
\sin t & \cos t
\end{pmatrix},
\qquad
\text{and use }R(x+y)=R(x)R(y)\text{ (composition of rotations).}
$$

$$
\begin{aligned}
(1)\quad & R(x)R(y)
=
\begin{pmatrix}
\cos x & -\sin x\\
\sin x & \cos x
\end{pmatrix}
\begin{pmatrix}
\cos y & -\sin y\\
\sin y & \cos y
\end{pmatrix} \\[10pt]
(2)\quad & R(x)R(y)
=
\begin{pmatrix}
\cos x\cos y-\sin x\sin y & -(\sin x\cos y+\cos x\sin y)\\
\sin x\cos y+\cos x\sin y & \cos x\cos y-\sin x\sin y
\end{pmatrix} \\[10pt]
(3)\quad & R(x+y)
=
\begin{pmatrix}
\cos(x+y) & -\sin(x+y)\\
\sin(x+y) & \cos(x+y)
\end{pmatrix} \\[10pt]
(4)\quad & R(x+y)=R(x)R(y)
\quad \Rightarrow \quad
\sin(x+y)=\sin x\cos y+\cos x\sin y
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \sin(x+y)=\sin x\cos y+\cos x\sin y.}
$$


### Angle Addition Identity (Cosine): 
#### $\boldsymbol{\cos(x+y)=\cos x\cos y-\sin x\sin y.}$

##### Proof 1: Complex analysis
**Assumption:** $i^2=-1$ and $e^{it}=\cos t+i\sin t$ for all $t\in\mathbb{R}$.

$$
\begin{aligned}
(1)\quad & e^{i(x+y)}=e^{ix}e^{iy} \\[6pt]
& \qquad\ \qquad\ =(\cos x+i\sin x)(\cos y+i\sin y) \\[6pt]
& \qquad\ \qquad\ =(\cos x\cos y-\sin x\sin y)+i(\sin x\cos y+\cos x\sin y) \\[6pt]
& \qquad\ \qquad\ =\cos(x+y)+i\sin(x+y) \\[10pt]
(2)\quad & \cos(x+y)=\cos x\cos y-\sin x\sin y
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(x+y)=\cos x\cos y-\sin x\sin y.}
$$

##### Proof 2: Matrices
**Assumption:** For $t\in\mathbb{R}$,
$$
R(t):=
\begin{pmatrix}
\cos t & -\sin t\\
\sin t & \cos t
\end{pmatrix},
\qquad
\text{and }R(x+y)=R(x)R(y).
$$

$$
\begin{aligned}
(1)\quad & R(x)R(y)
=
\begin{pmatrix}
\cos x & -\sin x\\
\sin x & \cos x
\end{pmatrix}
\begin{pmatrix}
\cos y & -\sin y\\
\sin y & \cos y
\end{pmatrix} \\[10pt]
(2)\quad & R(x)R(y)
=
\begin{pmatrix}
\cos x\cos y-\sin x\sin y & -(\sin x\cos y+\cos x\sin y)\\
\sin x\cos y+\cos x\sin y & \cos x\cos y-\sin x\sin y
\end{pmatrix} \\[10pt]
(3)\quad & R(x+y)
=
\begin{pmatrix}
\cos(x+y) & -\sin(x+y)\\
\sin(x+y) & \cos(x+y)
\end{pmatrix} \\[10pt]
(4)\quad & R(x+y)=R(x)R(y)
\quad \Rightarrow \quad
\cos(x+y)=\cos x\cos y-\sin x\sin y
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \cos(x+y)=\cos x\cos y-\sin x\sin y.}
$$


### Angle Addition Identity (Tangent): 
#### $\boldsymbol{\tan(x+y)=\dfrac{\tan x+\tan y}{1-\tan x\tan y}.}$

##### Proof 1: From sine/cosine
**Assumption:** $\cos x\neq 0$, $\cos y\neq 0$, and $1-\tan x\tan y\neq 0$.

$$
\begin{aligned}
(1)\quad & \tan(x+y)=\dfrac{\sin(x+y)}{\cos(x+y)} \\[10pt]
(2)\quad & \tan(x+y)
=\dfrac{\sin x\cos y+\cos x\sin y}{\cos x\cos y-\sin x\sin y} \\[8pt]
& \qquad\ \qquad\ =\dfrac{\dfrac{\sin x}{\cos x}+\dfrac{\sin y}{\cos y}}
{1-\dfrac{\sin x}{\cos x}\dfrac{\sin y}{\cos y}} \\[10pt]
& \qquad\ \qquad\ =\dfrac{\tan x+\tan y}{1-\tan x\tan y}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan(x+y)=\dfrac{\tan x+\tan y}{1-\tan x\tan y}.}
$$

##### Proof 2: Matrices (entry-ratio)
**Assumption:** $\cos x\neq 0$, $\cos y\neq 0$, and $\cos(x+y)\neq 0$.

$$
\begin{aligned}
(1)\quad & R(x+y)=R(x)R(y) \\[10pt]
(2)\quad & \sin(x+y)=\sin x\cos y+\cos x\sin y \\[6pt]
& \qquad\ \qquad\ \cos(x+y)=\cos x\cos y-\sin x\sin y \\[10pt]
(3)\quad & \tan(x+y)
=\dfrac{\sin(x+y)}{\cos(x+y)}
=\dfrac{\sin x\cos y+\cos x\sin y}{\cos x\cos y-\sin x\sin y} \\[10pt]
(4)\quad & \tan(x+y)
=\dfrac{\dfrac{\sin x}{\cos x}+\dfrac{\sin y}{\cos y}}
{1-\dfrac{\sin x}{\cos x}\dfrac{\sin y}{\cos y}}
=\dfrac{\tan x+\tan y}{1-\tan x\tan y}
\end{aligned}
$$

$$
\boldsymbol{\therefore\ \tan(x+y)=\dfrac{\tan x+\tan y}{1-\tan x\tan y}.}
$$

## Graphical derivation:
![[Pasted image 20251213135155.png|300]]
**Assumption:** Use the diagram’s right triangles $\triangle ABE$, $\triangle ABC$, $\triangle ADE$, $\triangle CDE$ with segment labels $a,b,c,d,e,f,g$ as shown.

From the right-triangle definitions in the diagram:

$$
\begin{aligned}
(1)\quad & \cos(x+y)=\dfrac{a}{d} \\[10pt]
(2)\quad & \cos x=\dfrac{a}{c} \\[6pt]
(3)\quad & \sin x=\dfrac{b}{c} \\[10pt]
(4)\quad & \cos y=\dfrac{c+f}{d} \\[6pt]
(5)\quad & \sin y=\dfrac{g}{d} \\[10pt]
(6)\quad & \cos z=\dfrac{g}{e} \\[6pt]
(7)\quad & \sin z=\dfrac{f}{e}
\end{aligned}
$$
Since $\angle ACB\cong \angle DCE$ (vertical angles), the remaining acute angles satisfy $z=x$, hence:

$$
\begin{aligned}
(8)\quad & \cos x=\dfrac{g}{e} \\[6pt]
(9)\quad & \sin x=\dfrac{f}{e}
\end{aligned}
$$

Equate the two expressions for $\cos x$ and $\sin x$, then solve for $g$ and $f$:

$$
\begin{aligned}
(10)\quad & \cos x=\dfrac{a}{c}=\dfrac{g}{e}
\quad \Rightarrow \quad g=\dfrac{ae}{c} \\[10pt]
(11)\quad & \sin x=\dfrac{b}{c}=\dfrac{f}{e}
\quad \Rightarrow \quad f=\dfrac{be}{c}
\end{aligned}
$$

Substitute (10)–(11) into (4)–(5):

$$
\begin{aligned}
(12)\quad & \cos y=\dfrac{c+f}{d}
=\dfrac{c}{d}+\dfrac{f}{d}
=\dfrac{c}{d}+\dfrac{be}{cd} \\[10pt]
(13)\quad & \sin y=\dfrac{g}{d}
=\dfrac{ae}{cd}
\end{aligned}
$$

Now compute $\cos x\cos y-\sin x\sin y$ using (2), (3), (12), (13):

$$
\begin{aligned}
(14)\quad & \cos x\cos y-\sin x\sin y \\[6pt]
& \qquad\ \qquad\ =\left(\dfrac{a}{c}\right)\left(\dfrac{c}{d}+\dfrac{be}{cd}\right)-\left(\dfrac{b}{c}\right)\left(\dfrac{ae}{cd}\right) \\[10pt]
& \qquad\ \qquad\ =\dfrac{ac}{cd}+\dfrac{abe}{c^2d}-\dfrac{abe}{c^2d} \\[10pt]
& \qquad\ \qquad\ =\dfrac{ac}{cd}
=\dfrac{a}{d}
\end{aligned}
$$

From (1), $\cos(x+y)=\dfrac{a}{d}$, so combining with (14) gives:

$$
\boldsymbol{\therefore\ \cos(x+y)=\cos x\cos y-\sin x\sin y.}
$$