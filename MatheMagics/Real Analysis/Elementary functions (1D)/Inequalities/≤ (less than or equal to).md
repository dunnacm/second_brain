---
down:
  - "[[Proofs (less than or equal to)]]"
tags:
  - mathemagics/real_analysis
---

## 1. reflexivity

$x \le x$.

## 2. antisymmetry

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x \le y,\\&y \le x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x = y$$

## 3. totality (trichotomy for $\le$)

$x \le y$ **or** $y \le x$.

## 4. transitivity of dissimilar inequalities

### 4.1 First form

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y,\\&y\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x<z$$

### 4.2 Second form

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&y<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x<z$$

## 5. transitivity of inequality

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x \le y,\\&y \le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x \le z$$

## 6. addition of two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x \le y,\\&w \le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x+w \le y+z$$

## 7. multiplication of inequality by a nonnegative constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w \ge 0,\\&x \le y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw \le yw$$

## 8. subtraction of a constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x \le y$
>
> > [!tip]+ **THEN**
> > $$x-w \le y-w$$

## 9. subtraction of two inequalities

### 9.1 Both non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x \le y,\\&w \le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x - z \le y - w$$

### 9.2 Dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x \le y,\\&w < z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x - z \le y - w$$

### 9.3 Dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x < y,\\&w \le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x - z < y - w$$

## 10. multiplication of dissimilar inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x<y,\\&0<w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw<yz$$

## 11. multiplication of two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0 \le x\le y,\\& 0\le w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw\le yz$$

## 12. multiplication of an arbitrary number of inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x_1\le y_1,\\&0\le x_2\le y_2,\\&\vdots\\&0\le x_n\le y_n\,\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1x_2\cdots x_n \le y_1y_2\cdots y_n$$

## 13. multiplication of three inequalities (one dissimilar)

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x_1<y_1,\\&0\le x_2\le y_2,\\&0\le x_3\le y_3 \end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1x_2x_3<y_1y_2y_3$$

## 14. raising both sides to a power (non-strict)

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y \ge 0,\\&n\in\mathbb{N}\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x^{\,n}\le y^{\,n}$$

## 15. division of inequalities

### 15.1 Divide by a positive constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w>0,\\&x\le y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{w}\le\dfrac{y}{w}$$

### 15.2 Division (both non-strict)

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y>0,\\&w\le z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}\le\dfrac{y}{w}$$

### 15.3 Division of dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y>0,\\&w< z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}\le\dfrac{y}{w}$$

### 15.4 Division of dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x< y >0,\\&w\le z >0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}<\dfrac{y}{w}$$

## 1. order axioms & transitivity

### 1.1 reflexivity

$x\le x$.

### 1.2 antisymmetry

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&y\le x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x=y$$

### 1.3 totality

$x\le y$ **or** $y\le x$.

### 1.4 transitivity, non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x\le z$$

### 1.5 transitivity, dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y,\\&y\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x<z$$

### 1.6 transitivity, dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&y<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x<z$$

## 2. addition & subtraction

### 2.1 add constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x\le y$
>
> > [!tip]+ **THEN**
> > $$x+w\le y+w$$

### 2.2 add two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x+w\le y+z$$

### 2.3 subtract constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x\le y$
>
> > [!tip]+ **THEN**
> > $$x-w\le y-w$$

### 2.4 subtract two: both non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-w\le y-z$$

### 2.5 subtract two: dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y,\\&w<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-z < y-w$$

### 2.6 subtract two: dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y,\\&w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-z<y-w$$

## 3. multiplication by scalars

### 3.1 nonnegative scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\ge 0,\\&x\le y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx\le wy$$

### 3.2 negative scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w<0,\\&x\le y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx\ge wy$$

## 4. products & powers on $\mathbb{R}^+$

### 4.1 multiply two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x\le y,\\&0\le w\le z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw\le yz$$

### 4.2 multiply $n$ inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x_1\le y_1,\\&\vdots\\&0\le x_n\le y_n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1\cdots x_n\le y_1\cdots y_n$$

### 4.3 multiply three: one dissimilar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x_1<y_1,\\&0\le x_2\le y_2,\\&0\le x_3\le y_3\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1x_2x_3<y_1y_2y_3$$

### 4.4 raise to $n$ on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x\le y,\\&n\in\mathbb{N}\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x^{\,n}\le y^{\,n}$$

## 5. division & reciprocals

### 5.1 divide by positive constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w>0,\\&x\le y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{w}\le\dfrac{y}{w}$$

### 5.2 quotient monotonicity: both non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y>0,\\&w\le z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}\le\dfrac{y}{w}$$
> > (equality iff $x=y$ and $w=z$)

### 5.3 quotient monotonicity: dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le y>0,\\&w<z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}<\dfrac{y}{w}$$

### 5.4 quotient monotonicity: dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y>0,\\&w\le z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}<\dfrac{y}{w}$$
