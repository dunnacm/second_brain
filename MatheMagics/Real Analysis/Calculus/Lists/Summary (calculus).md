---
down:
tags:
  - mathemagics/calculus
  - mathemagics/geometry/euclidean
  - mathemagics/geometry/hyperbolic
---
## Part 1
### Derivatives
```columns
id: tFVmUaVBal2bKS_01oi1-
===
$$
\begin{array}{rcl|rcl}
\mathtt{\dfrac{d}{dx}\big(\sin(x)\big)} &=& \mathtt{\cos(x)}
& \mathtt{\dfrac{d}{dx}\big(\csc(x)\big)} &=& \mathtt{-\,\csc(x)\cdot\cot(x)}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(\cos(x)\big)} &=& \mathtt{-\,\sin(x)}
& \mathtt{\dfrac{d}{dx}\big(\sec(x)\big)} &=& \mathtt{\sec(x)\cdot\tan(x)}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(\tan(x)\big)} &=& \mathtt{\sec^{2}(x)}
& \mathtt{\dfrac{d}{dx}\big(\cot(x)\big)} &=& \mathtt{-\,\csc^{2}(x)}
\end{array}
$$

===
$$
\begin{array}{rcl|rcl}
\mathtt{\dfrac{d}{dx}\big(sinh(x)\big)} &=& \mathtt{cosh(x)}
& \mathtt{\dfrac{d}{dx}\big(csch(x)\big)} &=& \mathtt{-\,csch(x)\cdot coth(x)}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(cosh(x)\big)} &=& \mathtt{sinh(x)}
& \mathtt{\dfrac{d}{dx}\big(sech(x)\big)} &=& \mathtt{-\,sech(x)\cdot tanh(x)}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(tanh(x)\big)} &=& \mathtt{sech^{2}(x)}
& \mathtt{\dfrac{d}{dx}\big(coth(x)\big)} &=& \mathtt{-\,csch^{2}(x)}
\end{array}
$$

```
```columns
id: JTEzHQdz39OT0J15HEQXL
===
$$
\begin{array}{rcl|rcl}
\mathtt{\dfrac{d}{dx}\big(\sin^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{\sqrt{1-x^{2}}}},\ \mathtt{\lvert x\rvert<1}
& \mathtt{\dfrac{d}{dx}\big(\csc^{-1}(x)\big)} &=& \mathtt{\dfrac{-1}{\lvert x\rvert\cdot\sqrt{x^{2}-1}}},\ \mathtt{\lvert x\rvert>1}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(\cos^{-1}(x)\big)} &=& \mathtt{\dfrac{-1}{\sqrt{1-x^{2}}}},\ \mathtt{\lvert x\rvert<1}
& \mathtt{\dfrac{d}{dx}\big(\sec^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{\lvert x\rvert\cdot\sqrt{x^{2}-1}}},\ \mathtt{\lvert x\rvert>1}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(\tan^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{1+x^{2}}},\ \mathtt{x\in\mathbb{R}}
& \mathtt{\dfrac{d}{dx}\big(\cot^{-1}(x)\big)} &=& \mathtt{\dfrac{-1}{1+x^{2}}},\ \mathtt{x\in\mathbb{R}}
\end{array}
$$


===
$$
\begin{array}{rcl|rcl}
\mathtt{\dfrac{d}{dx}\big(sinh^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{\sqrt{1+x^{2}}}},\ \mathtt{x\in\mathbb{R}}
& \mathtt{\dfrac{d}{dx}\big(csch^{-1}(x)\big)} &=& \mathtt{\dfrac{-1}{\lvert x\rvert\cdot\sqrt{1+x^{2}}}},\ \mathtt{x\in\mathbb{R}\setminus\{0\}}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(cosh^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{\sqrt{x^{2}-1}}},\ \mathtt{x\in(1,\infty)}
& \mathtt{\dfrac{d}{dx}\big(sech^{-1}(x)\big)} &=& \mathtt{\dfrac{-1}{x\cdot\sqrt{1-x^{2}}}},\ \mathtt{x\in(0,1)}
\\[6pt]
\mathtt{\dfrac{d}{dx}\big(tanh^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{1-x^{2}}},\ \mathtt{x\in(-1,1)}
& \mathtt{\dfrac{d}{dx}\big(coth^{-1}(x)\big)} &=& \mathtt{\dfrac{1}{1-x^{2}}},\ \mathtt{x\in(-\infty,-1)\cup(1,\infty)}
\end{array}
$$

```
### Integrals:
```columns
id: mXj2a7BlKNxnNL8D99muu
===
$$
\begin{array}{rcl}
\mathtt{\displaystyle \int \sin(x)\,dx} &=& \mathtt{-\cos(x)}
\\[6pt]
\mathtt{\displaystyle \int \cos(x)\,dx} &=& \mathtt{\sin(x)}
\\[6pt]
\mathtt{\displaystyle \int \tan(x)\,dx} &=& \mathtt{\ln\!\lvert \sec(x)\rvert}
\\[6pt]
\mathtt{\displaystyle \int \csc(x)\,dx} &=& \mathtt{\ln\!\lvert \csc(x)-\cot(x)\rvert}
\\[6pt]
\mathtt{\displaystyle \int \sec(x)\,dx} &=& \mathtt{\ln\!\lvert \sec(x)+\tan(x)\rvert}
\\[6pt]
\mathtt{\displaystyle \int \cot(x)\,dx} &=& \mathtt{\ln\!\lvert \sin(x)\rvert}
\end{array}
$$


===
$$
\begin{array}{rcl}
\mathtt{\displaystyle \int \sinh(x)\,dx} &=& \mathtt{\cosh(x)}
\\[6pt]
\mathtt{\displaystyle \int \cosh(x)\,dx} &=& \mathtt{\sinh(x)}
\\[6pt]
\mathtt{\displaystyle \int \tanh(x)\,dx} &=& \mathtt{\ln\!\bigl(\cosh(x)\bigr)}
\\[6pt]
\mathtt{\displaystyle \int csch(x)\,dx} &=& \mathtt{\ln\!\Bigl\lvert \tanh\!\Bigl(\dfrac{x}{2}\Bigr)\Bigr\rvert}
\\[6pt]
\mathtt{\displaystyle \int sech(x)\,dx} &=& \mathtt{\arctan\!\bigl(\sinh(x)\bigr)}
\\[6pt]
\mathtt{\displaystyle \int coth(x)\,dx} &=& \mathtt{\ln\!\lvert\sinh(x)\rvert}
\end{array}
$$

```
```columns
id: 5mnJDzptVMgc2KOPUENG8
===
$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sin^{n}(x)\,dx}
&=& \mathtt{-\dfrac{1}{n}\,\sin^{n-1}(x)\cos(x)
    + \dfrac{n-1}{n}\int \sin^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int \csc^{n}(x)\,dx}
&=& \mathtt{-\dfrac{1}{\,n-1\,}\,\csc^{n-2}(x)\cot(x)
    + \dfrac{n-2}{\,n-1\,}\int \csc^{n-2}(x)\,dx}
\\[10pt]
\mathtt{\displaystyle \int \cos^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{n}\,\cos^{n-1}(x)\sin(x)
    + \dfrac{n-1}{n}\int \cos^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int \sec^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{\,n-1\,}\,\sec^{n-2}(x)\tan(x)
    + \dfrac{n-2}{\,n-1\,}\int \sec^{n-2}(x)\,dx}\\[10pt]
\mathtt{\displaystyle \int \tan^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{\,n-1\,}\,\tan^{n-1}(x)
    - \int \tan^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int \cot^{n}(x)\,dx}
&=& \mathtt{-\dfrac{1}{\,n-1\,}\,\cot^{n-1}(x)
    - \int \cot^{n-2}(x)\,dx}
\end{array}
$$


===
$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sinh^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{n}\,\sinh^{n-1}(x)\cosh(x)
    - \dfrac{n-1}{n}\int \sinh^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int csch^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,csch^{n-2}(x)coth(x)
    - \dfrac{n-2}{\,n-1\,}\int csch^{n-2}(x)\,dx}
\\[10pt]
\mathtt{\displaystyle \int \cosh^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{n}\,\cosh^{n-1}(x)\sinh(x)
    + \dfrac{n-1}{n}\int \cosh^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int sech^{n}(x)\,dx}
&=& \mathtt{\dfrac{1}{\,n-1\,}\,sech^{n-2}(x)\tanh(x)
    + \dfrac{n-2}{\,n-1\,}\int sech^{n-2}(x)\,dx}
\\[10pt]
\mathtt{\displaystyle \int \tanh^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,\tanh^{n-1}(x)
    + \int \tanh^{n-2}(x)\,dx}
&
\mathtt{\displaystyle \int coth^{n}(x)\,dx}
&=& \mathtt{-\,\dfrac{1}{\,n-1\,}\,coth^{n-1}(x)
    + \int coth^{n-2}(x)\,dx}
\end{array}
$$

```
```columns
id: 8lYX1qLmmzI2T6x1gyHji
===
$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sin^{-1}(x)\,dx}
&=& \mathtt{x\sin^{-1}(x) + \sqrt{1-x^{2}}}
&
\mathtt{\displaystyle \int \csc^{-1}(x)\,dx}
&=& \mathtt{x\csc^{-1}(x) + \ln\!\bigl\lvert x+\sqrt{x^{2}-1}\bigr\rvert}
\\[10pt]
\mathtt{\displaystyle \int \cos^{-1}(x)\,dx}
&=& \mathtt{x\cos^{-1}(x) - \sqrt{1-x^{2}}}
&
\mathtt{\displaystyle \int \sec^{-1}(x)\,dx}
&=& \mathtt{x\sec^{-1}(x) - \ln\!\bigl\lvert x+\sqrt{x^{2}-1}\bigr\rvert}
\\[10pt]
\mathtt{\displaystyle \int \tan^{-1}(x)\,dx}
&=& \mathtt{x\tan^{-1}(x) - \dfrac{1}{2}\ln\!\bigl(1+x^{2}\bigr)}
&
\mathtt{\displaystyle \int \cot^{-1}(x)\,dx}
&=& \mathtt{x\cot^{-1}(x) + \dfrac{1}{2}\ln\!\bigl(1+x^{2}\bigr)}
\end{array}
$$

===
$$
\begin{array}{rcl|rcl}
\mathtt{\displaystyle \int \sinh^{-1}(x)\,dx}
&=& \mathtt{x\,\sinh^{-1}(x) - \sqrt{1+x^{2}}}
&
\mathtt{\displaystyle \int csch^{-1}(x)\,dx}
&=& \mathtt{x\,csch^{-1}(x) + \sinh^{-1}(x)}
\\[10pt]
\mathtt{\displaystyle \int \cosh^{-1}(x)\,dx}
&=& \mathtt{x\,\cosh^{-1}(x) - \sqrt{x-1}\,\sqrt{x+1}}
&
\mathtt{\displaystyle \int sech^{-1}(x)\,dx}
&=& \mathtt{x\,sech^{-1}(x) + \sin^{-1}(x)}
\\[10pt]
\mathtt{\displaystyle \int \tanh^{-1}(x)\,dx}
&=& \mathtt{x\,\tanh^{-1}(x) + \dfrac{1}{2}\ln\!\bigl(1-x^{2}\bigr)}
&
\mathtt{\displaystyle \int coth^{-1}(x)\,dx}
&=& \mathtt{x\,coth^{-1}(x) + \dfrac{1}{2}\ln\!\bigl(x^{2}-1\bigr)}
\end{array}
$$


```


