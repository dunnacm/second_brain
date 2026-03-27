---
down:
  - "[[Proof (mixed chained inequalities)]]"
tags:
  - mathemagics/real_analysis
---

## 1. converse of a mixed chain

### 1.1 flip ≤/<

$a\le x<b \;\Leftrightarrow\; b> x\ge a$.

### 1.2 flip </≤

$a< x\le b \;\Leftrightarrow\; b\ge x> a$.

### 1.3 mirror flip ≥/>

$a\ge x> b \;\Leftrightarrow\; b< x\le a$.

### 1.4 mirror flip >/≥

$a> x\ge b \;\Leftrightarrow\; b\le x< a$.

## 2. rigid shift (translate the band)

### 2.1 shift ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\le x+c<b+c$$

### 2.2 shift </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a< x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c< x+c\le b+c$$

### 2.3 mirror ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x+c> b+c$$

### 2.4 mirror >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c> x+c\ge b+c$$

## 3. superset expansion (widen the band)

### 3.1 expand ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\le x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-c\le x<b+c$$

### 3.2 expand </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a< x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-c< x\le b+c$$

### 3.3 mirror expand ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a\ge x> b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x> b-c$$

### 3.4 mirror expand >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c\ge 0,\\&a> x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c> x\ge b-c$$

## 4. scaling by a constant

### 4.1 by $c>0$, ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a\le x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xc<bc$$

### 4.2 by $c>0$, </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a< x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac< xc\le bc$$

### 4.3 by $c<0$, ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a\le x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xc>bc$$

### 4.4 by $c<0$, </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a< x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac> xc\ge bc$$

### 4.5 mirror, $c>0$, ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a\ge x> b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xc>bc$$

### 4.6 mirror, $c>0$, >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c>0,\\&a> x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac> xc\ge bc$$

### 4.7 mirror, $c<0$, ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a\ge x> b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xc<bc$$

### 4.8 mirror, $c<0$, >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&c<0,\\&a> x\ge b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac< xc\le bc$$

## 5. combine two mixed chains (sum/diff)

### 5.1 add: ≤/< with ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x<b,\\&c\le y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\le x+y<b+d$$

### 5.2 add: </≤ with </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a< x\le b,\\&c< y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c< x+y\le b+d$$

### 5.3 subtract: ≤/< with ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\le x<b,\\&c\le y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d\le x-y<b-c$$

### 5.4 subtract: </≤ with </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a< x\le b,\\&c< y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d< x-y\le b-c$$

### 5.5 mirror add: ≥/> with ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b,\\&c\ge y> d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c\ge x+y> b+d$$

### 5.6 mirror add: >/≥ with >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b,\\&c> y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a+c> x+y\ge b+d$$

### 5.7 mirror subtract: ≥/> with ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b,\\&c\ge y> d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d\ge x-y> b-c$$

### 5.8 mirror subtract: >/≥ with >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b,\\&c> y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a-d> x-y\ge b-c$$

## 6. product of two mixed chains ($>0$)

### 6.1 ≤/< with ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x<b,\\&0\le c\le y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\le xy<bd$$

### 6.2 </≤ with </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0< a< x\le b,\\&0< c< y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac< xy\le bd$$

### 6.3 mirror ≥/> with ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b>0,\\&c\ge y> d>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac\ge xy> bd$$

### 6.4 mirror >/≥ with >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b>0,\\&c> y\ge d>0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$ac> xy\ge bd$$

## 7. ratios (division; positive denominators)

### 7.1 ≤/< with ≤/<

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x<b,\\&0< c\le y<d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}\le\dfrac{x}{y}<\dfrac{b}{c}$$

### 7.2 </≤ with </≤

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0< a< x\le b,\\&0< c< y\le d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}<\dfrac{x}{y}\le\dfrac{b}{c}$$

### 7.3 mirror ≥/> with ≥/>

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b\ge 0,\\&0< c\ge y> d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}\ge\dfrac{x}{y}>\dfrac{b}{c}$$

### 7.4 mirror >/≥ with >/≥

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b\ge 0,\\&0< c> y\ge d\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{a}{d}>\dfrac{x}{y}\ge\dfrac{b}{c}$$

## 8. product of many mixed chains ($\ge 0$)

### 8.1 ≤/< bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a_i\le x_i<b_i\ \text{for }i=1,\dots,n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n\le x_1\cdots x_n< b_1\cdots b_n$$

### 8.2 </≤ bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0< a_i< x_i\le b_i\ \text{for }i=1,\dots,n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n< x_1\cdots x_n\le b_1\cdots b_n$$

### 8.3 mirror ≥/> bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a_i\ge x_i> b_i\ge 0\ \text{for }i=1,\dots,n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n\ge x_1\cdots x_n> b_1\cdots b_n$$

### 8.4 mirror >/≥ bands

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a_i> x_i\ge b_i\ge 0\ \text{for }i=1,\dots,n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a_1\cdots a_n> x_1\cdots x_n\ge b_1\cdots b_n$$

## 9. powers of a mixed chain ($n\in\mathbb{N}$)

### 9.1 ≤/< in $\mathbb{R}_{\ge 0}$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le a\le x<b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}\le x^{\,n}< b^{\,n}$$

### 9.2 </≤ in $\mathbb{R}_{\ge 0}$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0< a< x\le b\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}< x^{\,n}\le b^{\,n}$$

### 9.3 mirror ≥/> in $\mathbb{R}_{\ge 0}$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a\ge x> b\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}\ge x^{\,n}> b^{\,n}$$

### 9.4 mirror >/≥ in $\mathbb{R}_{\ge 0}$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&a> x\ge b\ge 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$a^{\,n}> x^{\,n}\ge b^{\,n}$$
