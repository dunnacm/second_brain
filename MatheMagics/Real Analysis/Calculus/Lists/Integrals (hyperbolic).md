---
down:
  - "[[Summary (calculus) 1]]"
tags:
  - mathemagics/calculus
  - mathemagics/real_analysis
---
## Basic hyperbolic integrals

$$
\begin{array}{rcl}
\mathtt{\displaystyle \int \sinh(x)\,dx} &=& \mathtt{\cosh(x)},\ \mathtt{x\in\mathbb{R}}
\\[6pt]
\mathtt{\displaystyle \int \cosh(x)\,dx} &=& \mathtt{\sinh(x)},\ \mathtt{x\in\mathbb{R}}
\\[6pt]
\mathtt{\displaystyle \int \tanh(x)\,dx} &=& \mathtt{\ln\!\bigl(\cosh(x)\bigr)},\ \mathtt{x\in\mathbb{R}}
\\[6pt]
\mathtt{\displaystyle \int csch(x)\,dx} &=& \mathtt{\ln\!\Bigl\lvert \tanh\!\Bigl(\dfrac{x}{2}\Bigr)\Bigr\rvert},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\\[6pt]
\mathtt{\displaystyle \int sech(x)\,dx} &=& \mathtt{\arctan\!\bigl(\sinh(x)\bigr)},\ \mathtt{x\in\mathbb{R}}
\\[6pt]
\mathtt{\displaystyle \int coth(x)\,dx} &=& \mathtt{\ln\!\lvert\sinh(x)\rvert},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\end{array}
$$

## Reduction formulas for powers 

$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sinh^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{n}\,\sinh^{n-1}(x)\cosh(x)
    - \dfrac{n-1}{n}\int \sinh^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}}
&
\mathtt{\displaystyle \int csch^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,csch^{n-2}(x)coth(x)
    - \dfrac{n-2}{\,n-1\,}\int csch^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \cosh^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{n}\,\cosh^{n-1}(x)\sinh(x)
    + \dfrac{n-1}{n}\int \cosh^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}}
&
\mathtt{\displaystyle \int sech^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{\,n-1\,}\,sech^{n-2}(x)\tanh(x)
    + \dfrac{n-2}{\,n-1\,}\int sech^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}}
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \tanh^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,\tanh^{n-1}(x)
    + \int \tanh^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}}
&
\mathtt{\displaystyle \int coth^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,coth^{n-1}(x)
    + \int coth^{n-2}(x)\,dx},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\end{array}
$$

## Integrals of inverse hyperbolic functions

$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sinh^{-1}(x)\,dx}
&=& \mathtt{x\,\sinh^{-1}(x) - \sqrt{1+x^{2}}},\ \mathtt{x\in\mathbb{R}}
&
\mathtt{\displaystyle \int csch^{-1}(x)\,dx}
&=& \mathtt{x\,csch^{-1}(x) + \sinh^{-1}\!\bigl(\lvert x\rvert\bigr)},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\end{array}
$$

$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \cosh^{-1}(x)\,dx}
&=& \mathtt{x\,\cosh^{-1}(x) - \sqrt{x^{2}-1}},\ \mathtt{x\in(1,\infty)}
&
\mathtt{\displaystyle \int sech^{-1}(x)\,dx}
&=& \mathtt{x\,sech^{-1}(x) + \sin^{-1}(x)},\ \mathtt{x\in(0,1)}
\end{array}
$$
$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \tanh^{-1}(x)\,dx}
&=& \mathtt{x\,\tanh^{-1}(x) + \dfrac{1}{2}\ln\!\bigl(1-x^{2}\bigr)},\ \mathtt{x\in(-1,1)}
&
\mathtt{\displaystyle \int coth^{-1}(x)\,dx}
&=& \mathtt{x\,coth^{-1}(x) + \dfrac{1}{2}\ln\!\bigl(x^{2}-1\bigr)},\ \mathtt{x\in(-\infty,-1)\cup(1,\infty)}
\end{array}
$$
