---
down:
  - "[[Proof (strict chain inequalities)]]"
  - "[[Mixed chained inequality]]"
tags:
  - mathemagics/real_analysis
---

## 1. converse of a chained inequality

### 1.1 flip chain

$a<x<b \;\Leftrightarrow\; b>x>a$.

### 1.2 mirror flip

$a>x>b \;\Leftrightarrow\; b<x<a$.

## 2. rigid shift (translate the band)

### 2.1 shift up

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a<x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c<x+c<b+c$$

### 2.2 shift down, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c>x+c>b+c$$

## 3. superset expansion (widen the band)

### 3.1 right/left expand

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a<x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-c<x<b+c$$

### 3.2 mirror expand

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a>x>b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c>x>b-c$$

## 4. scaling by a constant

### 4.1 scale by $c>0$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a<x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac<xc<bc$$

### 4.2 scale by $c>0$, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a>x>b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac>xc>bc$$

### 4.3 scale by $c<0$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a<x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac>xc>bc$$

### 4.4 scale by $c<0$, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a>x>b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac<xc<bc$$

## 5. combine two chains (sum / difference)

### 5.1 add bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a<x<b,\\&c<y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c<x+y<b+d$$

### 5.2 add bands, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b,\\&c>y>d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c>x+y>b+d$$

### 5.3 subtract bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a<x<b,\\&c<y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d<x-y<b-c$$

### 5.4 subtract bands, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b,\\&c>y>d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d>x-y>b-c$$

## 6. product of two chains (positive)

### 6.1 both positive

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<a<x<b,\\&0<c<y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac<xy<bd$$

### 6.2 both positive, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b>0,\\&c>y>d>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac>xy>bd$$

## 7. ratios (division of two chains)

### 7.1 both positive

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<a<x<b,\\&0<c<y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}<\dfrac{x}{y}<\dfrac{b}{c}$$

### 7.2 both positive, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b>0,\\&c>y>d>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}>\dfrac{x}{y}>\dfrac{b}{c}$$

## 8. product of many chains (all $>0$)

### 8.1 increasing bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<a_1<x_1<b_1,\\&0<a_2<x_2<b_2,\\&\vdots\\&0<a_n<x_n<b_n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n<x_1\cdots x_n<b_1\cdots b_n$$

### 8.2 decreasing bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a_1>x_1>b_1>0,\\&a_2>x_2>b_2>0,\\&\vdots\\&a_n>x_n>b_n>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n>x_1\cdots x_n>b_1\cdots b_n$$

## 9. powers of a chain (natural exponents)

### 9.1 inside positive band

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<a<x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}<x^{\,n}<b^{\,n}$$
> > for all $n\in\mathbb{N}$

### 9.2 decreasing positive band

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a>x>b>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}>x^{\,n}>b^{\,n}$$
> > for all $n\in\mathbb{N}$
