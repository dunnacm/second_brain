---
down:
  - "[[Summary (calculus) 1]]"
tags:
  - mathemagics/calculus
  - mathemagics/real_analysis
---
## Exponential integrals

$$
\begin{array}{rcl|rcl}
\displaystyle \int e^{x}\,dx &=& e^{x}
&
\displaystyle \int a^{x}\,dx &=& \dfrac{a^{x}}{\ln(a)},\quad a>0,\ a\ne 1
\end{array}
$$

## Logarithmic integrals

$$
\begin{array}{rcl}
\displaystyle \int \dfrac{1}{x}\,dx &=& \ln\lvert x\rvert
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \ln(x)\,dx &=& x\ln(x)-x,\quad x>0
&
\displaystyle \int \log_a x\,dx &=& \dfrac{x\ln(x)-x}{\ln(a)},\quad a>0,\ a\ne 1,\ x>0
\\[6pt]
\displaystyle \int \ln\lvert x\rvert\,dx &=& x\ln\lvert x\rvert - x,\quad x\ne 0
& & &
\end{array}
$$

## Trigonometric:
### Basic trigonometric integrals

$$
\begin{array}{rcl}
\displaystyle \int \sin(x)\,dx &=& -\cos(x)
\\[4pt]
\displaystyle \int \cos(x)\,dx &=& \sin(x)
\\[4pt]
\displaystyle \int \tan(x)\,dx &=& \ln\lvert \sec(x)\rvert
\\[4pt]
\displaystyle \int \csc(x)\,dx &=& \ln\lvert \csc(x)-\cot(x)\rvert
\\[4pt]
\displaystyle \int \sec(x)\,dx &=& \ln\lvert \sec(x)+\tan(x)\rvert
\\[4pt]
\displaystyle \int \cot(x)\,dx &=& \ln\lvert \sin(x)\rvert
\end{array}
$$

### Reduction formulas:
#### Reduction formulas for powers of $sin$ and $csc$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \sin^{n}(x)\,dx
&=& -\dfrac{1}{n}\,\sin^{n-1}(x)\cos(x)
    + \dfrac{n-1}{n}\int \sin^{n-2}(x)\,dx
&
\displaystyle \int \csc^{n}(x)\,dx
&=& -\dfrac{1}{\,n-1\,}\,\csc^{n-2}(x)\cot(x)
    + \dfrac{n-2}{\,n-1\,}\int \csc^{n-2}(x)\,dx
\end{array}
$$

#### Reduction formulas for powers of $cos$ and $sec$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \cos^{n}(x)\,dx
&=& \dfrac{1}{n}\,\cos^{n-1}(x)\sin(x)
    + \dfrac{n-1}{n}\int \cos^{n-2}(x)\,dx
&
\displaystyle \int \sec^{n}(x)\,dx
&=& \dfrac{1}{\,n-1\,}\,\sec^{n-2}(x)\tan(x)
    + \dfrac{n-2}{\,n-1\,}\int \sec^{n-2}(x)\,dx
\end{array}
$$

#### Reduction formulas for powers of $tan$ and $cot$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \tan^{n}(x)\,dx
&=& \dfrac{1}{\,n-1\,}\,\tan^{n-1}(x)
    - \int \tan^{n-2}(x)\,dx
&
\displaystyle \int \cot^{n}(x)\,dx
&=& -\dfrac{1}{\,n-1\,}\,\cot^{n-1}(x)
    - \int \cot^{n-2}(x)\,dx
\end{array}
$$

### Integrals of inverse trigonometric functions

$$
\begin{array}{rcl|rcl}
\displaystyle \int \sin^{-1}(x)\,dx
&=& x\sin^{-1}(x) + \sqrt{1-x^{2}}
&
\displaystyle \int \csc^{-1}(x)\,dx
&=& x\csc^{-1}(x) + \ln\!\bigl\lvert x+\sqrt{x^{2}-1}\bigr\rvert
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \cos^{-1}(x)\,dx
&=& x\cos^{-1}(x) - \sqrt{1-x^{2}}
&
\displaystyle \int \sec^{-1}(x)\,dx
&=& x\sec^{-1}(x) - \ln\!\bigl\lvert x+\sqrt{x^{2}-1}\bigr\rvert
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\displaystyle \int \tan^{-1}(x)\,dx
&=& x\tan^{-1}(x) - \dfrac{1}{2}\ln\bigl(1+x^{2}\bigr)
&
\displaystyle \int \cot^{-1}(x)\,dx
&=& x\cot^{-1}(x) + \dfrac{1}{2}\ln\bigl(1+x^{2}\bigr)
\end{array}
$$

## Integration by parts

$$
\displaystyle
\int u(x)\,v'(x)\,dx
= u(x)\,v(x) - \int u'(x)\,v(x)\,dx
$$

A handy layout for choosing \(u\) and \(v\):

$$
\begin{array}{c\quad c}
u(x) & v'(x)\\[4pt]
u'(x) & \longleftarrow v(x)
\end{array}
$$
