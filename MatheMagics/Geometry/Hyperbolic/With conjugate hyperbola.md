---
down:
tags:
  - mathemagics/geometry/hyperbolic
---
## Diagram:
```columns
id: -rLktbR7NwGQFDleWznCP
===
![[Pasted image 20260109172521.png]]

===
![[Pasted image 20260109172914.png]]

```
## Explanation

### Unit circle $x^{2}+y^{2}=1$
Fix $\theta$ and draw the $\theta$-ray from $O$.

- Let $B$ be the $y$-axis intercept. Draw the tangent at $B$ (horizontal). Let it meet the $\theta$-ray at $Q'$.
  - $BQ'=\cot(\theta)$
  - $OQ'=\csc(\theta)$

- Let $A$ be the $x$-axis intercept. Draw the tangent at $A$ (vertical). Let it meet the same $\theta$-ray at $Q$.
  - $OQ=\sec(\theta)$
  - (also $AQ=\tan(\theta)$)

So, for the circle: **one ray from $O$ + the two axis tangents** $\Rightarrow$ reciprocal trig values appear as **straight-line lengths**.

### Unit hyperbola $x^{2}-y^{2}=1$
Fix the parameter $A$ and use the ray $OP$ (the hyperbolic analogue of the $\theta$-ray).

**Key obstruction:** $x^{2}-y^{2}=1$ does **not** meet the $y$-axis, so the circle’s “tangent at the $y$-axis intercept” has no direct hyperbola version.

**Repair:** use the conjugate hyperbola $y^{2}-x^{2}=1$, which *does* meet the $y$-axis at a point $B$.

#### (1) $\mathtt{coth}$ is the direct mirror of the circle’s $\cot$
Draw the tangent at $B$ on $y^{2}-x^{2}=1$ (horizontal), and let it meet the ray $OP$ at $Q'$.
Then the labeled tangent length is
$$
BQ'=\mathtt{coth}(A).
$$

#### (2) $\mathtt{sech}$ and $\mathtt{csch}$ come from a “circle-like ray” built from $OP$
On the circle, the *same* ray hits both tangents immediately.  
On the hyperbola, we first build a substitute ray $OR$ (still from $O$) that will play that role.

Construction (as in the diagram):
- Extend the vertical through $P$ to meet the conjugate at $P'$; project to the $y$-axis at $Y'$.
- Use the vertical tangent at the vertex $A=(1,0)$ (the line $AQ$) to locate the point $R$.
- Draw the ray $OR$.

Now read lengths exactly like the circle reads them from intersections:
- Let $OR$ meet the conjugate at $C$; drop to the $y$-axis at $M$. Then
$$
CM=\mathtt{sech}(A).
$$
- Let $OR$ meet the vertical tangent at $A$ at $C'$. Then the labeled vertical segment is
$$
AC'=\mathtt{csch}(A).
$$

## Mirror summary (what corresponds to what)

- **Circle:** one ray from $O$ intersects  
  - the tangent at $B$ $\Rightarrow$ $BQ'=\cot(\theta)$ and $OQ'=\csc(\theta)$,  
  - the tangent at $A$ $\Rightarrow$ $OQ=\sec(\theta)$ (and also $AQ=\tan(\theta)$).

- **Hyperbola:** the ray $OP$ gives the cotangent-type length only after repairing the missing $y$-axis intercept via the conjugate:
  - tangent at $B$ on $y^{2}-x^{2}=1$ $\Rightarrow$ $BQ'=\mathtt{coth}(A)$.
  - then a constructed “circle-like” ray $OR$ is built (using $P',Y',R$) so that its intersections yield:
    - $CM=\mathtt{sech}(A)$ (via the conjugate),
    - $AC'=\mathtt{csch}(A)$ (on the tangent at $A$).


