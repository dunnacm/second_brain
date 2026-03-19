---
down:
  - "[[Exercises, derivatives and integrals]]"
  - "[[Summary (calculus) 1]]"
tags:
  - mathemagics/calculus
  - mathemagics/real_analysis
---
## Derivative notation

$$
\begin{aligned}
D_x f(x)\big|_{x=x_0}
&= \left.\frac{d}{dx}f(x)\right|_{x=x_0}
= f'(x_0)
\end{aligned}
$$

## Basic algebraic functions (power rule)

$$
\begin{array}{rcl}
\dfrac{d}{dx}\big(c\big)   &=& 0\\[6pt]
\dfrac{d}{dx}\big(x\big)   &=& 1\\[6pt]
\dfrac{d}{dx}\big(x^{n}\big) &=& n\,x^{\,n-1},\quad
n\in\mathbb{R}\ \text{(for noninteger }n\text{, assume }x>0)
\end{array}
$$

## Exponential functions

$$
\begin{array}{rcl|rcl}
\dfrac{d}{dx}\big(e^{x}\big) &=& e^{x}
& \dfrac{d}{dx}\big(a^{x}\big) &=& a^{x}\cdot\ln(a),\ a>0
\end{array}
$$

## Logarithmic functions

$$
\begin{array}{rcl|rcl}
\dfrac{d}{dx}\big(\ln(x)\big)   &=& \dfrac{1}{x},\ x>0
& \dfrac{d}{dx}\big(\log_a x\big) &=& \dfrac{1}{x}\cdot\dfrac{1}{\ln(a)},\ a>0,\ a\ne 1,\ x>0
\\[6pt]
\dfrac{d}{dx}\big(\ln(\lvert x\rvert)\big) &=& \dfrac{1}{x},\ x\ne 0
& & &
\end{array}
$$

## Trigonometric functions

$$
\begin{array}{rcl|rcl}
\dfrac{d}{dx}\big(\sin(x)\big) &=& \cos(x)
& \dfrac{d}{dx}\big(\csc(x)\big) &=& -\,\csc(x)\cdot\cot(x)
\\[6pt]
\dfrac{d}{dx}\big(\cos(x)\big) &=& -\,\sin(x)
& \dfrac{d}{dx}\big(\sec(x)\big) &=& \sec(x)\cdot\tan(x)
\\[6pt]
\dfrac{d}{dx}\big(\tan(x)\big) &=& \sec^{2}(x)
& \dfrac{d}{dx}\big(\cot(x)\big) &=& -\,\csc^{2}(x)
\end{array}
$$

## Inverse trigonometric functions

$$
\begin{array}{rcl|rcl}
\dfrac{d}{dx}\big(\sin^{-1}(x)\big) &=& \dfrac{1}{\sqrt{1-x^{2}}},\ \lvert x\rvert<1
& \dfrac{d}{dx}\big(\csc^{-1}(x)\big) &=& \dfrac{-1}{\lvert x\rvert\cdot\sqrt{x^{2}-1}},\ \lvert x\rvert>1
\\[6pt]
\dfrac{d}{dx}\big(\cos^{-1}(x)\big) &=& \dfrac{-1}{\sqrt{1-x^{2}}},\ \lvert x\rvert<1
& \dfrac{d}{dx}\big(\sec^{-1}(x)\big) &=& \dfrac{1}{\lvert x\rvert\cdot\sqrt{x^{2}-1}},\ \lvert x\rvert>1
\\[6pt]
\dfrac{d}{dx}\big(\tan^{-1}(x)\big) &=& \dfrac{1}{1+x^{2}},\ x\in\mathbb{R}
& \dfrac{d}{dx}\big(\cot^{-1}(x)\big) &=& \dfrac{-1}{1+x^{2}},\ x\in\mathbb{R}
\end{array}
$$

## Absolute value

$$
\frac{d}{dx}\big(\lvert x\rvert\big) = \frac{x}{\lvert x\rvert},\ x\ne 0
$$

## Quotient rule

$$
\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right)
= \frac{f'(x)\cdot g(x) - f(x)\cdot g'(x)}{[g(x)]^{2}},\quad g(x)\ne 0
$$

## Product rule

$$
\frac{d}{dx}\big(f(x)\cdot g(x)\big)
= f'(x)\cdot g(x) + f(x)\cdot g'(x)
$$
## Chain rule (composite functions)

$$
\frac{d}{dx}\big(f(g(x))\big)
= f'\big(g(x)\big)\cdot g'(x)
$$

A very common special case (generalized power rule):

$$
\frac{d}{dx}\big((g(x))^{n}\big)
= n\,(g(x))^{n-1}\cdot g'(x),\quad n\in\mathbb{R}
$$
