---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Principal-value “reductions” 
### $\boldsymbol{\sin^{-1}(\sin x)=x\ \text{or}\ \pi-x.}$
**Assumption:** $x\in[0,\pi]$.

$$
\sin^{-1}(\sin x)=
\begin{cases}
x, & 0\le x\le \dfrac{\pi}{2},\\[8pt]
\pi-x, & \dfrac{\pi}{2}\le x\le \pi.
\end{cases}
$$

### $\boldsymbol{\cos^{-1}(\cos x)=x\ \text{or}\ 2\pi-x\ (\text{or }-x).}$
**Assumption:** $x\in[0,2\pi]$ (and also note: if $x\in[-\pi,0]$, then $-x\in[0,\pi]$).

$$
\cos^{-1}(\cos x)=
\begin{cases}
x, & 0\le x\le \pi,\\[8pt]
2\pi-x, & \pi\le x\le 2\pi.
\end{cases}
$$

### $\boldsymbol{\tan^{-1}(\tan x)=x\ \text{or}\ x\pm\pi.}$
**Assumption:** $x\in\mathbb{R}$ (principal-value adjustment by $\pi$).

$$
\tan^{-1}(\tan x)=x-k\pi,
\quad \text{where }k\in\mathbb{Z}\text{ is chosen so that }x-k\pi\in\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right).
$$

### $\boldsymbol{\cot^{-1}(\cot x)=x\ \text{or}\ x\pm\pi.}$
**Assumption:** $x\in\mathbb{R}$ (principal-value adjustment by $\pi$).

$$
\cot^{-1}(\cot x)=x-k\pi,
\quad \text{where }k\in\mathbb{Z}\text{ is chosen so that }x-k\pi\in(0,\pi).
$$

### $\boldsymbol{\sec^{-1}(\sec x)=x\ \text{or}\ 2\pi-x\ (\text{or }-x).}$
**Assumption:** interpret as “principal-value adjustment” (range convention dependent).

### $\boldsymbol{\csc^{-1}(\csc x)=x\ \text{or}\ \pi-x.}$
**Assumption:** interpret as “principal-value adjustment” (range convention dependent).