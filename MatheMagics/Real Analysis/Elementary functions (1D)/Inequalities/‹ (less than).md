---
down:
  - "[[Proofs (less than)]]"
  - "[[Mixed strict inequalities]]"
tags:
  - mathemagics/real_analysis
---

## 1. order axiom (trichotomy)

$x<0$ or $x=0$ or $x>0$ (exactly one holds).

## 2. transitivity

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x<z$$

## 3. addition rules

### 3.1 add constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x<y$
>
> > [!tip]+ **THEN**
> > $$x+w<y+w$$

### 3.2 add two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y,\\&w<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x+w<y+z$$

### 3.3 add three inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x_1<y_1,\\&x_2<y_2,\\&x_3<y_3\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1+x_2+x_3<y_1+y_2+y_3$$

### 3.4 add $n$ inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x_1<y_1,\\&\vdots\\&x_n<y_n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1+\cdots+x_n<y_1+\cdots+y_n$$

## 4. subtraction

### 4.1 subtract constant

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x<y$
>
> > [!tip]+ **THEN**
> > $$x-w<y-w$$

### 4.2 subtract two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&x<y,\\&w<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x-w<y-z$$

## 5. multiplication by scalars

### 5.1 positive scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w>0,\\&x<y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx<wy$$

### 5.2 multiplication by $-1$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x<y$
>
> > [!tip]+ **THEN**
> > $$-y<-x$$

### 5.3 negative scalar

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w<0,\\&x<y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$wx>wy$$

## 6. product & power rules on $\mathbb{R}^+$

### 6.1 multiply two inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x<y,\\&0<w<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$xw<yz$$

### 6.2 multiply three inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x_1<y_1,\\&0<x_2<y_2,\\&0<x_3<y_3\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1x_2x_3<y_1y_2y_3$$

### 6.3 multiply $n$ inequalities

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x_1<y_1,\\&\vdots\\&0<x_n<y_n\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x_1\cdots x_n<y_1\cdots y_n$$

### 6.4 squaring on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $0<x<y$
>
> > [!tip]+ **THEN**
> > $$x^{2}<y^{2}$$

### 6.5 raising to $n$ on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x<y,\\&n\in\mathbb{N}\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$x^{n}<y^{n}$$

## 7. division & reciprocals

### 7.1 reciprocal positive on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $x>0$
>
> > [!tip]+ **THEN**
> > $$\dfrac{1}{x}>0$$

### 7.2 divide by positive

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&w>0,\\&x<y\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{w}<\dfrac{y}{w}$$

### 7.3 reciprocal reverses order on $\mathbb{R}^+$

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $0<x<y$
>
> > [!tip]+ **THEN**
> > $$\dfrac{1}{y}<\dfrac{1}{x}$$

### 7.4 quotient monotonicity

> [!note]+ **Property**
> > [!warning]+ **IF**
> > - $$
> > \begin{aligned}&0<x<y,\\&0<w<z\end{aligned}
> > $$
>
> > [!tip]+ **THEN**
> > $$\dfrac{x}{z}<\dfrac{y}{w}$$

> [!abstract]+

> > [!info]+ Constants

> > - **Addition & subtraction**:

> > >$x<y \Rightarrow x \pm c < y \pm c,\quad c\in\mathbb{R}.$

> > - **Multiplication (& division)**:

> > > $x<y \Rightarrow \lvert c\rvert\,x < \lvert c\rvert\,y.$

> > > $x<y \Rightarrow -\,\lvert c\rvert\,x > -\,\lvert c\rvert\,y.$

>

> > [!info]+ **Addition & subtraction** of inequalities

> > - **Addition**:

> > > $$\begin{aligned}

> > > &x_{0}<y_{0}\\

> > > &\vdots\\

> > > &x_{N}<y_{N}

> > > \end{aligned}

> > > \;\Rightarrow\;

> > > \sum_{n=0}^{N} x_{n} \;<\; \sum_{n=0}^{N} y_{n}. $$

> > - **Subtraction**:

> > > $\begin{aligned}&x<y,\\&w<z\end{aligned} \Rightarrow x-z<y-z$

>

> > [!info]+ **Multiplication & division** of inequalities

> > - **Multiplication**:

> > > $$\begin{aligned}

> > > &0<x_{0}<y_{0}\\

> > > &\vdots\\

> > > &0<x_{N}<y_{N}

> > > \end{aligned}

> > > \;\Rightarrow\;

> > > \prod_{n=0}^{N} x_{n} \;<\; \prod_{n=0}^{N} y_{n}. $$

> > - **Division (quotient monotonicity)**:

> > > $$\begin{aligned}&0<x<y,\\&0<w<z\end{aligned}\Rightarrow \dfrac{x}{z}<\dfrac{y}{w}.$$
