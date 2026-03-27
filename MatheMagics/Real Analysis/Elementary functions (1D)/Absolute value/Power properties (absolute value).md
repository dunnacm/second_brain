---
down:
  - "[[Proofs (properties absolute value, powers)]]"
tags:
  - mathemagics/real_analysis
---
$n \in \mathbb{N}$

## 1. order/equality via squares

### 1.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert<\lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{2}<x^{2}$$

### 1.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert>\lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{2}>x^{2}$$

### 1.3

$\lvert w\rvert=\lvert x\rvert \ \Leftrightarrow \ w^{2}=x^{2}$.

## 2. powers of magnitudes (round-trip & order transfer)

### 2.1

$\lvert x^{n}\rvert=\lvert x\rvert^{\,n}$.

### 2.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert<\lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\lvert w\rvert^{\,n}<\lvert x\rvert^{\,n}$$

### 2.3

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert>\lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\lvert w\rvert^{\,n}>\lvert x\rvert^{\,n}$$

### 2.4

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert\neq\lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\lvert w\rvert^{\,n}\neq\lvert x\rvert^{\,n}$$

### 2.5

$\lvert w^{n}\rvert=\lvert x^{n}\rvert \quad \Leftrightarrow \quad \lvert w\rvert=\lvert x\rvert$.

### 2.7

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert\ge \lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\lvert w\rvert^{\,n}\ge \lvert x\rvert^{\,n}$$

### 2.8

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&\lvert w\rvert\le \lvert x\rvert\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\lvert w\rvert^{\,n}\le \lvert x\rvert^{\,n}$$

## 7. equality via powers

### 7.1

$w^{\,n}=x^{\,n} \ \Leftrightarrow\ \lvert w\rvert=\lvert x\rvert$ (even $n$).

### 7.2

$w^{\,n}=x^{\,n} \ \Leftrightarrow\ w=x$ (odd $n$).

## 3. odd powers: order preserved on $\mathbb{R}$

### 3.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\le x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\le x^{\,n}$$
> > (odd $n$)

### 3.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w< x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}< x^{\,n}$$
> > (odd $n$)

### 3.3

$w^{\,n}\le x^{\,n} \ \Leftrightarrow\ w\le x$ (odd $n$).

### 3.4

$w^{\,n}=x^{\,n} \ \Leftrightarrow\ w=x$ (odd $n$).

## 4. even powers: nonnegative band (monotone increasing)

### 4.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le w\le x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\le x^{\,n}$$
> > (even $n$)

### 4.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le w< x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}< x^{\,n}$$
> > (even $n$)

### 4.3

$0\le w\le x \ \Leftrightarrow\ w^{\,n}\le x^{\,n}$ (even $n$).

### 4.4

$0\le w< x \ \Leftrightarrow\ w^{\,n}< x^{\,n}$ (even $n$).

## 5. even powers: nonpositive band (order reverses)

### 5.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\le x\le 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\ge x^{\,n}$$
> > (even $n$)

### 5.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w< x\le 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}> x^{\,n}$$
> > (even $n$)

### 5.3

$w\le x\le 0 \ \Leftrightarrow\ w^{\,n}\ge x^{\,n}$ (even $n$).

### 5.4

$w< x\le 0 \ \Leftrightarrow\ w^{\,n}> x^{\,n}$ (even $n$).

## 6. even powers: opposite signs

### 6.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\le 0\le x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\le x^{\,n}$$
> > ; strict unless $w=x=0$ (even $n$)

## 8. MIRROR FORMS (≥ / >), odd powers

### 8.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\ge x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\ge x^{\,n}$$
> > (odd $n$)

### 8.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w> x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}> x^{\,n}$$
> > (odd $n$)

### 8.3

$w^{\,n}\ge x^{\,n} \ \Leftrightarrow\ w\ge x$ (odd $n$).

### 8.4

$w^{\,n}> x^{\,n} \ \Leftrightarrow\ w> x$ (odd $n$).

## 9. MIRROR FORMS (≥ / >), even nonnegative band

### 9.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x\le w\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\ge x^{\,n}$$
> > (even $n$)

### 9.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0\le x< w\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}> x^{\,n}$$
> > (even $n$)

### 9.3

$0\le x\le w \ \Leftrightarrow\ w^{\,n}\ge x^{\,n}$ (even $n$).

### 9.4

$0\le x< w \ \Leftrightarrow\ w^{\,n}> x^{\,n}$ (even $n$).

## 10. MIRROR FORMS (≥ / >), even nonpositive band

### 10.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x\le w\le 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\le x^{\,n}$$
> > (even $n$)

### 10.2

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x< w\le 0\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}< x^{\,n}$$
> > (even $n$)

### 10.3

$x\le w\le 0 \ \Leftrightarrow\ w^{\,n}\le x^{\,n}$ (even $n$).

### 10.4

$x< w\le 0 \ \Leftrightarrow\ w^{\,n}< x^{\,n}$ (even $n$).

## 11. MIRROR FORMS (≥ / >), opposite signs

### 11.1

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w\ge 0\ge x\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$w^{\,n}\ge x^{\,n}$$
> > ; strict unless $w=x=0$ (even $n$)
