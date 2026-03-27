---
down:
  - "[[Proofs (greater than or equal to)]]"
tags:
---

## 1. order axioms & transitivity

### 1.1 reflexivity

$x\ge x$.

### 1.2 antisymmetry

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y,\\&y\ge x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x=y$$

### 1.3 totality

$x\ge y$ **or** $y\ge x$.

### 1.4 transitivity, non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y\ge z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x\ge z$$

### 1.5 transitivity, dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x>y,\\&y\ge z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x>z$$

### 1.6 transitivity, dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y,\\&y>z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x>z$$

## 2. addition & subtraction

### 2.1 add constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x\ge y$
>
> > [!tip]+ **THEN**
> > $$x+w\ge y+w$$

### 2.2 add two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y,\\&w\ge z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x+w\ge y+z$$

### 2.3 subtract constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x\ge y$
>
> > [!tip]+ **THEN**
> > $$x-w\ge y-w$$

### 2.4 subtract two: both non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y,\\&w\ge z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-z\ge y-w$$

### 2.5 subtract two: dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y,\\&w>z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-z> y-w$$

### 2.6 subtract two: dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x>y,\\&w\ge z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-z>y-w$$

## 3. multiplication by scalars

### 3.1 nonnegative scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\ge 0,\\&x\ge y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx\ge wy$$

### 3.2 negative scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w<0,\\&x\ge y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx\le wy$$

## 4. products & powers on $\mathbb{R}^+$

### 4.1 multiply two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y\ge 0,\\&w\ge z\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw\ge yz$$

### 4.2 multiply $n$ inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x_1\ge y_1,\\&\vdots\\&x_n\ge y_n,\\&y_1,\dots,y_n\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1\cdots x_n\ge y_1\cdots y_n$$

### 4.3 multiply three: one dissimilar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x_1>y_1>0,\\&x_2\ge y_2\ge 0,\\&x_3\ge y_3\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1x_2x_3>y_1y_2y_3$$

### 4.4 raise to $n$ on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y\ge 0,\\&n\in\mathbb{N}\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x^{\,n}\ge y^{\,n}$$

## 5. division & reciprocals

### 5.1 divide by positive constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w>0,\\&x\ge y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{w}\ge\dfrac{y}{w}$$

### 5.2 quotient monotonicity: both non-strict

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y>0,\\&w\ge z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}\ge\dfrac{y}{w}$$

### 5.3 quotient monotonicity: dissimilar I

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\ge y>0,\\&w>z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}>\dfrac{y}{w}$$

### 5.4 quotient monotonicity: dissimilar II

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x>y>0,\\&w\ge z>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}>\dfrac{y}{w}$$
