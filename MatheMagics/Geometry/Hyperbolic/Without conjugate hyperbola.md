---
down:
tags:
  - mathemagics/geometry/hyperbolic
---
## Diagram
```columns
id: YkIm93Crc4tElCeRdfhQw
===
![[Pasted image 20260109183750.png]]

===
![[Pasted image 20260109184336.png]]

```
## Explanation

### Unit circle $x^{2}+y^{2}=1$ (alternate definition of $\sec$ and $\text{cosec}$)

Let $P=(\mathtt{cos}\,\theta,\mathtt{sin}\,\theta)$ on the unit circle. Drop perpendiculars to the axes at $X$ and $Y$, so
- $OX=\mathtt{cos}\,\theta$,
- $OY=\mathtt{sin}\,\theta$.

Draw the **tangent at $P$**, meeting the $x$-axis at $M$ and the $y$-axis at $N$.  
Then the diagram’s intercept lengths define
- $OM=\mathtt{sec}\,\theta$,
- $ON=\mathtt{cosec}\,\theta$,

with signs determined by whether $M$ is left of the $y$-axis or $N$ is below the $x$-axis.

### Unit hyperbola $x^{2}-y^{2}=1$ (same pattern, using tangents to the unit circle)

Let $P=(\mathtt{cosh}\,t,\mathtt{sinh}\,t)$ on the unit hyperbola, and let $X$ and $Y$ be its axis projections, so
- $OX=\mathtt{cosh}\,t$,
- $OY=\mathtt{sinh}\,t$.

Draw the **unit circle** $x^{2}+y^{2}=1$ (auxiliary). Then copy the “tangent → intercept length” idea:

- From $X$, draw a tangent to the unit circle touching at $Q$. Drop a perpendicular from $Q$ to the $x$-axis at $M$.
	- $OM=\mathtt{sech}\,t$.

- From $Y$, draw a tangent to the unit circle touching at $Q'$. Drop a perpendicular from $Q'$ to the $y$-axis at $N$.
	- $ON=\mathtt{csch}\,t$.

(Sign: $\mathtt{sech}\,t>0$ always; $\mathtt{csch}\,t$ changes sign with $t$.)

**Geometric note:** the tangent from $Y$ to the unit circle requires $\lvert\sinh t\rvert\ge 1$ (as drawn in the diagram).

### What to compare across the two diagrams

In both cases the same “type-pairs” appear:
- $OX$ is the cosine-type length and $OM$ is the secant-type length.
- $OY$ is the sine-type length and $ON$ is the cosecant-type length.

The visual difference is the inside/outside reversal relative to the unit circle:
- Circle: $X,Y$ are interior and $M,N$ are exterior.
- Hyperbola: $X,Y$ are exterior and $M,N$ are interior.
