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


## Part 2 (hyperbolic)
### Derivatives
#### Note:
For the ==hyperbolic functions==, all the identities in the **right column are positive**, while all those in the **left column are negative**
```columns
id: tFVmUaVBal2bKS_01oi1-
===
$$
\begin{aligned}
& \left(\mathtt{sin}\,x\right)' \,=\, \textcolor{green}{\mathtt{cosh}\,x}
\\[18pt]
& \left(\mathtt{cos}\,x\right)' \,=\, \textcolor{orange}{\mathtt{-sin}\,x}
\\[18pt]
& \left(\mathtt{tanh}\,x\right)' \,=\, \textcolor{blue}{\mathtt{sec}^{2}x}
\end{aligned}
$$
---
$$
\begin{aligned}
& \left(\mathtt{sinh}\,x\right)' \,=\, \textcolor{green}{\mathtt{cosh}\,x}
\\[18pt]
& \left(\mathtt{cosh}\,x\right)' \,=\, \textcolor{orange}{\mathtt{sinh}\,x}
\\[18pt]
& \left(\mathtt{tanh}\,x\right)' \,=\, \textcolor{blue}{\mathtt{sech}^{2}x}
\end{aligned}
$$
===
$$
\begin{aligned}
& \left(\mathtt{csc}\,x\right)' \,=\, \textcolor{green}{-\mathtt{csc}\,x\cdot \mathtt{cot}\,x}
\\[18pt]
& \left(\mathtt{sec}\,x\right)' \,=\, \textcolor{orange}{\mathtt{sec}\,x\cdot \mathtt{tan}\,x}
\\[18pt]
& \left(\mathtt{cot}\,x\right)' \,=\, \textcolor{blue}{-\mathtt{csc}^{2}x}
\end{aligned}
$$
---
$$
\begin{aligned}
& \left(\mathtt{csch}\,x\right)' \,=\, \textcolor{green}{-\mathtt{csch}\,x\cdot \mathtt{coth}\,x}
\\[18pt]
& \left(\mathtt{sech}\,x\right)' \,=\, \textcolor{orange}{-\mathtt{sech}\,x\cdot \mathtt{tanh}\,x}
\\[18pt]
& \left(\mathtt{coth}\,x\right)' \,=\, \textcolor{blue}{-\mathtt{csch}^{2}x}
\end{aligned}
$$
```
---
```columns
id: tFVmUaVBal2bKS_01oi1-
===
$$
\begin{aligned}
& \left(\mathtt{sinh}^{-1}x\right) \,=\, \ln\!\left(x+\sqrt{\textcolor{green}{x^{2}+1}}\right)
\\[22pt]
& \left(\mathtt{cosh}^{-1}x\right) \,=\, \ln\!\left(x+\sqrt{\textcolor{orange}{x^{2}-1}}\right)
\\[22pt]
& \left(\mathtt{tanh}^{-1}x\right) \,=\, \dfrac{1}{2}\,\ln\!\left(\dfrac{1+x}{1-x}\right)
\ \left(=\, \ln\!\left[\left(\dfrac{(1+x)^{2}}{\textcolor{blue}{1-x^{2}}}\right)^{\frac{1}{2}}\right]\right)
\end{aligned}
$$
---
$$
\begin{aligned}
& \left(\mathtt{sinh}^{-1}x\right)' \,=\, \dfrac{1}{\sqrt{\textcolor{green}{x^{2}+1}}}
\\[18pt]
& \left(\mathtt{cosh}^{-1}x\right)' \,=\, \dfrac{1}{\sqrt{\textcolor{orange}{x^{2}-1}}}
\\[18pt]
& \left(\mathtt{tanh}^{-1}x\right)' \,=\, \dfrac{1}{\textcolor{blue}{1-x^{2}}}
\end{aligned}
$$

===
$$
\begin{aligned}
& \left(\mathtt{csch}^{-1}x\right) \,=\, \ln\!\left(\dfrac{1+\sqrt{\textcolor{green}{1+x^{2}}}}{\textcolor{green}{x}}\right)
\\[22pt]
& \left(\mathtt{sech}^{-1}x\right) \,=\, \ln\!\left(\dfrac{1+\sqrt{\textcolor{orange}{1-x^{2}}}}{\textcolor{orange}{x}}\right)
\\[22pt]
& \left(\mathtt{coth}^{-1}x\right) \,=\, \dfrac{1}{2}\,\ln\!\left(\dfrac{x+1}{x-1}\right)
\ \left(=\, \ln\!\left[\left(\dfrac{(x+1)^{2}}{\textcolor{blue}{x^{2}-1}}\right)^{\frac{1}{2}}\right]\right)
\end{aligned}
$$
---
$$
\begin{aligned}
& \left(\mathtt{csch}^{-1}x\right)' \,=\, \dfrac{-1}{\textcolor{green}{\lvert x\rvert\cdot \sqrt{1+x^{2}}}}
\\[18pt]
& \left(\mathtt{sech}^{-1}x\right)' \,=\, \dfrac{-1}{\textcolor{orange}{x\cdot \sqrt{1-x^{2}}}}
\\[18pt]
& \left(\mathtt{coth}^{-1}x\right)' \,=\, \dfrac{-1}{\textcolor{blue}{x^{2}-1}}
\end{aligned}
$$

```
### Integrals:

```columns
id: IZxXeii4WMck0OL1rmB9v
===
$$
\begin{aligned}
& \int \mathtt{sin}\,x\,dx \,=\, \textcolor{blue}{-\mathtt{cos}\,x}
\\[22pt]
& \int \mathtt{cos}\,x\,dx \,=\, \textcolor{green}{\mathtt{sin}\,x}
\\[22pt]
& \int \mathtt{tan}\,x\,dx \,=\, \textcolor{orange}{\ln\lvert \mathtt{sec}\,x\rvert}
\end{aligned}
$$

---

$$
\begin{aligned}
& \int \mathtt{sinh}\,x\,dx \,=\, \textcolor{blue}{\mathtt{cosh}\,x}
\\[22pt]
& \int \mathtt{cosh}\,x\,dx \,=\, \textcolor{green}{\mathtt{sinh}\,x}
\\[22pt]
& \int \mathtt{tanh}\,x\,dx \,=\, \textcolor{orange}{\ln\!\left\lvert\left(\mathtt{sech}\,x\right)^{-1}\right\rvert}
\end{aligned}
$$


===
$$
\begin{aligned}
& \int \mathtt{csc}\,x\,dx \,=\,
\textcolor{blue}{\ln}\!\left\lvert \mathtt{csc}\,x-\textcolor{blue}{\mathtt{cot}}\,x \right\rvert
\\[22pt]
& \int \mathtt{sec}\,x\,dx \,=\,
\ln\!\left\lvert \mathtt{sec}\,x+\textcolor{green}{\mathtt{tan}}\,x \right\rvert
\\[22pt]
& \int \mathtt{cot}\,x\,dx \,=\,
\textcolor{orange}{\ln\!\left\lvert \left(\mathtt{csc}\,x\right)^{-1}\right\rvert}
\end{aligned}
$$

---

$$
\begin{aligned}
& \int \mathtt{csch}\,x\,dx \,=\,
\textcolor{blue}{\ln}\!\left\lvert \left(\textcolor{blue}{\mathtt{coth}}\!\left(\dfrac{\textcolor{blue}{x}}{2}\right)\right)^{-1}\right\rvert
\\[22pt]
& \int \mathtt{sech}\,x\,dx \,=\, \textcolor{green}{\mathtt{tan}}^{-1}\!\bigl(\mathtt{sinh}(x)\bigr)
\\[22pt]
& \int \mathtt{coth}\,x\,dx \,=\, \textcolor{orange}{\ln\!\left\lvert \left(\mathtt{csch}\,x\right)^{-1}\right\rvert}
\end{aligned}
$$

```
---
```columns
id: sSLDa5V6sqctDvCwOF6hX
===

| $\color{blue}{+}$       | $\color{green}{-}$ |
| ----------------------- | ------------------ |
| $\color{orange}{-}$<br> | $\color{red}{-}$   |

===
$$
\begin{aligned}
& \int \mathtt{sinh}^{n}(x)\,dx
\,=\, \textcolor{blue}{+}\ \dfrac{1}{n}\,\mathtt{sinh}^{n-1}(x)\,\mathtt{cosh}(x)
\ \textcolor{green}{-}\ \dfrac{n-1}{n}\int \mathtt{sinh}^{\,n-2}(x)\,dx
\\[22pt]
& \int \mathtt{csch}^{n}(x)\,dx
\,=\, \textcolor{orange}{-}\ \dfrac{1}{n-1}\,\mathtt{csch}^{\,n-2}(x)\,\mathtt{coth}(x)
\ \textcolor{red}{-}\ \dfrac{n-2}{n-1}\int \mathtt{csch}^{\,n-2}(x)\,dx
\end{aligned}
$$


```
```columns
id: sSLDa5V6sqctDvCwOF6hX
===

| $\color{blue}{+}$   | $\color{green}{+}$ |
| ------------------- | ------------------ |
| $\color{orange}{+}$ | $\color{red}{+}$   |

===
$$
\begin{aligned}
& \int \mathtt{cosh}^{n}(x)\,dx
\,=\, \textcolor{blue}{+}\ \dfrac{1}{n}\,\mathtt{cosh}^{\,n-1}(x)\,\mathtt{sinh}(x)
\ \textcolor{green}{+}\ \dfrac{n-1}{n}\int \mathtt{cosh}^{\,n-2}(x)\,dx
\\[22pt]
& \int \mathtt{sech}^{n}(x)\,dx
\,=\, \textcolor{orange}{+}\ \dfrac{1}{n-1}\,\mathtt{sech}^{\,n-2}(x)\,\mathtt{tanh}(x)
\ \textcolor{red}{+}\ \dfrac{n-2}{n-1}\int \mathtt{sech}^{\,n-2}(x)\,dx
\end{aligned}
$$


```
```columns
id: sSLDa5V6sqctDvCwOF6hX
===

| $\color{blue}{-}$   | $\color{green}{+}$ |
| ------------------- | ------------------ |
| $\color{orange}{-}$ | $\color{red}{+}$   |

===
$$
\begin{aligned}
& \int \mathtt{tanh}^{n}(x)\,dx
\,=\, \textcolor{blue}{-}\ \dfrac{1}{n-1}\,\mathtt{tanh}^{\,n-1}(x)
\ \textcolor{green}{+}\ \int \mathtt{tanh}^{\,n-2}(x)\,dx
\\[22pt]
& \int \mathtt{coth}^{n}(x)\,dx
\,=\, \textcolor{orange}{-}\ \dfrac{1}{n-1}\,\mathtt{coth}^{\,n-1}(x)
\ \textcolor{red}{+}\ \int \mathtt{coth}^{\,n-2}(x)\,dx
\end{aligned}
$$


```
---
#### Note:
For the ==hyperbolic functions==, the second terms in all the identities in the **right column are negative**, while all those in the **left column are positive**
```columns
id: Cm-2Vk52DETfQz9oVLo7P
===
$$
\begin{aligned}
& \mathtt{sinh}^{-1}(x) \,=\, \ln\!\left(x+\sqrt{\textcolor{blue}{x^{2}+1}}\right)
\\[22pt]
& \mathtt{cosh}^{-1}(x) \,=\, \ln\!\left(x+\sqrt{\textcolor{green}{x^{2}-1}}\right)
\\[22pt]
& \mathtt{tanh}^{-1}(x) \,=\, \dfrac{1}{2}\,\ln\!\left(\dfrac{1+x}{1-x}\right)
\ \left(=\, \textcolor{orange}{\dfrac{1}{2}\,\ln}\!\left[\left(\dfrac{(1+x)^{2}}{\textcolor{orange}{1-x^{2}}}\right)\right]\right)
\end{aligned}
$$

---

$$
\begin{aligned}
& \int \mathtt{sinh}^{-1}x\,dx \,=\, x\cdot \mathtt{sinh}^{-1}x - \textcolor{blue}{\sqrt{x^{2}+1}}
\\[22pt]
& \int \mathtt{cosh}^{-1}x\,dx \,=\, x\cdot \mathtt{cosh}^{-1}x - \textcolor{green}{\sqrt{x^{2}-1}}
\\[22pt]
& \int \mathtt{tanh}^{-1}x\,dx \,=\, x\cdot \mathtt{tanh}^{-1}x \ -\ \textcolor{orange}{\dfrac{1}{2}\,\ln}\!\left(\dfrac{1}{\textcolor{orange}{1-x^{2}}}\right)
\end{aligned}
$$

===
$$
\begin{aligned}
& \mathtt{tanh}^{-1}(x)
\,=\, \dfrac{1}{2}\,\ln\!\left(\dfrac{x+1}{x-1}\right)
\left(=\, \textcolor{orange}{\dfrac{1}{2}\,\ln}\!\left[\left(\dfrac{(x+1)^{2}}{\textcolor{orange}{x^{2}-1}}\right)\right]\right)
\end{aligned}
$$

---

$$
\begin{aligned}
& \int \mathtt{csch}^{-1}x\,dx \,=\, x\cdot \mathtt{csch}^{-1}x + \mathtt{sinh}^{-1}\!\bigl(\lvert x\rvert\bigr)
\\[22pt]
& \int \mathtt{sech}^{-1}x\,dx \,=\, x\cdot \mathtt{sech}^{-1}x + \sin^{-1}x
\\[22pt]
& \int \mathtt{coth}^{-1}x\,dx \,=\, x\cdot \mathtt{coth}^{-1}x + \textcolor{orange}{\dfrac{1}{2}}\,\textcolor{orange}{\ln}\!\bigl(\textcolor{orange}{x^{2}-1}\bigr)
\end{aligned}
$$

```
