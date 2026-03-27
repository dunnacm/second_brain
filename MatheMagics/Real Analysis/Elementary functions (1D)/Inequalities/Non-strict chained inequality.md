---
down:
  - "[[Proof (non-strict inequality)]]"
  - "[[Mixed chained inequality]]"
tags:
  - mathemagics/real_analysis
---

## 1. converse of a chained inequality

### 1.1 flip chain

$a\le x\le b \;\Leftrightarrow\; b\ge x\ge a$.

### 1.2 mirror flip

$a\ge x\ge b \;\Leftrightarrow\; b\le x\le a$.

## 2. rigid shift (translate the band)

### 2.1 shift up

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\le x+c\le b+c$$

### 2.2 shift down, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x+c\ge b+c$$

## 3. superset expansion (widen the band)

### 3.1 right/left expand

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\le x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-c\le x\le b+c$$

### 3.2 mirror expand

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\ge x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x\ge b-c$$

## 4. scaling by a constant

### 4.1 scale by $c\ge 0$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\le x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xc\le bc$$

### 4.2 scale by $c\ge 0$, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\ge x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xc\ge bc$$

### 4.3 scale by $c<0$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a\le x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xc\ge bc$$

### 4.4 scale by $c<0$, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a\ge x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xc\le bc$$

## 5. combine two chains (sum / difference)

### 5.1 add bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x\le b,\\&c\le y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\le x+y\le b+d$$

### 5.2 add bands, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b,\\&c\ge y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x+y\ge b+d$$

### 5.3 subtract bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x\le b,\\&c\le y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d\le x-y\le b-c$$

### 5.4 subtract bands, mirror

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b,\\&c\ge y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d\ge x-y\ge b-c$$

## 6. product of two chains ($\mathbb{R}_{\ge 0}$)

### 6.1 both nonnegative

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x\le b,\\&0\le c\le y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xy\le bd$$

### 6.2 both nonpositive \& same signs

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b\ge 0,\\&c\ge y\ge d\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xy\ge bd$$

## 7. ratios (division of two chains)

### 7.1 positive denominators

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x\le b,\\&0< c\le y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}\le\dfrac{x}{y}\le\dfrac{b}{c}$$

### 7.2 mirror, positive denominators

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b\ge 0,\\&0< c\ge y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}\ge\dfrac{x}{y}\ge\dfrac{b}{c}$$

## 8. product of many chains (all $\ge 0$)

### 8.1 increasing bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a_1\le x_1\le b_1,\\&0\le a_2\le x_2\le b_2,\\&\vdots\\&0\le a_n\le x_n\le b_n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n\le x_1\cdots x_n\le b_1\cdots b_n$$

### 8.2 decreasing bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a_1\ge x_1\ge b_1\ge 0,\\&a_2\ge x_2\ge b_2\ge 0,\\&\vdots\\&a_n\ge x_n\ge b_n\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n\ge x_1\cdots x_n\ge b_1\cdots b_n$$

## 9. powers of a chain (natural exponents)

### 9.1 inside nonnegative band

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}\le x^{\,n}\le b^{\,n}$$
> > for all $n\in\mathbb{N}$

### 9.2 decreasing nonnegative band

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x\ge b\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}\ge x^{\,n}\ge b^{\,n}$$
> > for all $n\in\mathbb{N}$
