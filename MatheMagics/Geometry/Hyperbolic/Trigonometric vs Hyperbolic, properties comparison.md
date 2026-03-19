---
down:
tags:
  - mathemagics/geometry/euclidean
  - mathemagics/geometry/hyperbolic
---
## Properties
### Pythagorean
```columns
id: 2ebFjfwNQh-739J3JI5AI
===
$$
\begin{aligned}
(1)\quad & \mathtt{cos}^{2}(\theta)+\mathtt{sin}^{2}(\theta)=1\\[12pt]
(2)\quad & 1+\mathtt{tan}^{2}(\theta)=\mathtt{sec}^{2}(\theta)\\[12pt]
(3)\quad & 1+\mathtt{cot}^{2}(\theta)=\mathtt{csc}^{2}(\theta)
\end{aligned}
$$
===
$$
\begin{aligned}
(1)\quad & \mathtt{cosh}^{2}(x)-\mathtt{sinh}^{2}(x)=1\\[12pt]
(2)\quad & 1-\mathtt{tanh}^{2}(x)=\mathtt{sech}^{2}(x)\\[12pt]
(3)\quad & \mathtt{coth}^{2}(x)-1=\mathtt{csch}^{2}(x)
\end{aligned}
$$

```
### Addition / subtraction
```columns
id: aYNtTv0gEaUJEDBM6arQ9
===
$$
\begin{aligned}
(1)\quad & \mathtt{sin}(\phi\pm \psi)=\mathtt{sin}(\phi)\,\mathtt{cos}(\psi)\pm \mathtt{sin}(\psi)\,\mathtt{cos}(\phi)\\[12pt]
(2)\quad & \mathtt{cos}(\phi\pm \psi)=\mathtt{cos}(\phi)\,\mathtt{cos}(\psi)\mp \mathtt{sin}(\phi)\,\mathtt{sin}(\psi)\\[12pt]
(3)\quad & \mathtt{tan}(\phi\pm \psi)=\dfrac{\mathtt{tan}(\phi)\pm \mathtt{tan}(\psi)}{1\mp \mathtt{tan}(\phi)\,\mathtt{tan}(\psi)}
\end{aligned}
$$
===
$$
\begin{aligned}
(1)\quad & \mathtt{sinh}(x\,\textcolor{orange}{\pm}\,y)=\mathtt{sinh}(x)\,\mathtt{cosh}(y)\,\textcolor{orange}{\pm}\,\mathtt{sinh}(y)\,\mathtt{cosh}(x)\\[12pt]
(2)\quad & \mathtt{cosh}(x\,\textcolor{orange}{\pm}\,y)=\mathtt{cosh}(x)\,\mathtt{cosh}(y)\,\textcolor{orange}{\pm}\,\mathtt{sinh}(x)\,\mathtt{sinh}(y)\\[12pt]
(3)\quad & \mathtt{tanh}(x\,\textcolor{orange}{\pm}\,y)=\dfrac{\mathtt{tanh}(x)\,\textcolor{orange}{\pm}\,\mathtt{tanh}(y)}{1\,\textcolor{orange}{\pm}\,\mathtt{tanh}(x)\cdot\mathtt{tanh}(y)}
\end{aligned}
$$
```
### Double
```columns
id: l3_SGXEC9wpWfmvhfRowS
===
$$
\begin{aligned}
& \mathtt{sin}(2\theta)=2\cdot\mathtt{sin}(\theta)\cdot\mathtt{cos}(\theta)\\[22pt]
& \mathtt{cos}(2\theta)=\mathtt{cos}^{2}(\theta)-\mathtt{sin}^{2}(\theta)\\[12pt]
& \qquad\qquad =1-2\cdot\mathtt{sin}^{2}(\theta)\\[12pt]
& \qquad\qquad =2\cdot\mathtt{cos}^{2}(\theta)-1\\[12pt]
& \qquad\qquad =\dfrac{1-\mathtt{tan}^{2}(\theta)}{1+\mathtt{tan}^{2}(\theta)}\\[22pt]
& \mathtt{tan}(2\theta)=\dfrac{2\cdot\mathtt{tan}(\theta)}{1-\mathtt{tan}^{2}(\theta)}
\end{aligned}
$$
===
$$
\begin{aligned}
& \mathtt{sinh}(2x)=2\cdot\mathtt{sinh}(x)\cdot\mathtt{cosh}(x)\\[22pt]
& \mathtt{cosh}(2x)=\mathtt{cosh}^{2}(x)+\mathtt{sinh}^{2}(x)\\[12pt]
& \qquad\qquad ={\color{orange}\underline{\color{black}{2\cdot\mathtt{sinh}^{2}(x)}}}+1\\[12pt]
& \qquad\qquad ={\color{orange}\underline{\color{black}{2\cdot\mathtt{cosh}^{2}(x)}}}-1\\[12pt]
& \qquad\qquad =\dfrac{1+\mathtt{tanh}^{2}(x)}{1-\mathtt{tanh}^{2}(x)}\\[22pt]
& \mathtt{tanh}(2x)=\dfrac{2\cdot\mathtt{tanh}(x)}{1+\mathtt{tanh}^{2}(x)}
\end{aligned}
$$
```
### Half
```columns
id: IUP2P9n7chn7AZC5zTCgH
===
$$
\begin{aligned}
(1)\quad & \mathtt{cos}^{2}\!\Bigl(\dfrac{\theta}{2}\Bigr)=\dfrac{1+\mathtt{cos}(\theta)}{2}\\[18pt]
(2)\quad & \mathtt{sin}^{2}\!\Bigl(\dfrac{\theta}{2}\Bigr)=\dfrac{1-\mathtt{cos}(\theta)}{2}
\end{aligned}
$$

===
$$
\begin{aligned}
(1)\quad & \mathtt{cosh}^{2}\!\Bigl(\dfrac{x}{2}\Bigr)=\dfrac{{\color{orange}\underline{\color{black}{\mathtt{cosh}(x)}}}+1}{2}\\[18pt]
(2)\quad & \mathtt{sinh}^{2}\!\Bigl(\dfrac{x}{2}\Bigr)=\dfrac{{\color{orange}\underline{\color{black}{\mathtt{cosh}(x)}}}-1}{2}
\end{aligned}
$$
```
### Look-alikes
```columns
id: 00pLAcl29U3Z2kf72aqz6
===
$$
\begin{aligned}
& \mathtt{tan}(2\theta)=\dfrac{2\mathtt{tan}\,\theta}{1-\mathtt{tan}^{2}\theta}
\end{aligned}
$$

===
$$
\begin{aligned}
& \mathtt{sinh}(2x)=\dfrac{2\mathtt{tanh}\,x}{1-\mathtt{tanh}^{2}x} 
\end{aligned}
$$
```
### Product-to-sum
Hyperbolic: Positive | Negative
```columns
id: MVU4ZUaWw0Pq78P9I_-R2
===
$$
\begin{aligned}
(1)\quad & \mathtt{sin}(\phi)\cdot\mathtt{cos}(\psi)=\frac{1}{2}\Bigl(\mathtt{sin}(\phi-\psi)+\mathtt{sin}(\phi+\psi)\Bigr)\\[18pt]
(2)\quad & \mathtt{cos}(\phi)\cdot\mathtt{cos}(\psi)=\frac{1}{2}\Bigl(\mathtt{cos}(\phi-\psi)+\mathtt{cos}(\phi+\psi)\Bigr)\\[18pt]
(3)\quad & \mathtt{sin}(\phi)\cdot\mathtt{sin}(\psi)=\frac{1}{2}\Bigl(\mathtt{cos}(\phi-\psi)-\mathtt{cos}(\phi+\psi)\Bigr)
\end{aligned}
$$

===
$$
\begin{aligned}
(1)\quad & \mathtt{sinh}\,x\cdot\mathtt{cosh}\,y=\frac{1}{2}\Bigl(\mathtt{sinh}(x+y)+\mathtt{sinh}(x-y)\Bigr)\\[18pt]
(2)\quad & \mathtt{cosh}\,x\cdot\mathtt{cosh}\,y=\frac{1}{2}\Bigl(\mathtt{cosh}(x+y)+\mathtt{cosh}(x-y)\Bigr)\\[18pt]
(3)\quad & \mathtt{sinh}\,x\cdot\mathtt{sinh}\,y=\frac{1}{2}\Bigl(\mathtt{cosh}(x+y)-\mathtt{cosh}(x-y)\Bigr)
\end{aligned}
$$
```
### Sum-to-product
Hyperbolic: Positive | Negative
```columns
id: sMVhFQ8OuStL_RrOOJNp1
===
$$
\begin{aligned}
(1)\quad & \mathtt{sin}(\phi)+\mathtt{sin}(\psi)=2\cdot\Bigl(\mathtt{sin}\!\Bigl(\dfrac{\phi+\psi}{2}\Bigr)\cdot\mathtt{cos}\!\Bigl(\dfrac{\phi-\psi}{2}\Bigr)\Bigr)\\[22pt]
(2)\quad & \mathtt{cos}(\phi)+\mathtt{cos}(\psi)=2\cdot\Bigl(\mathtt{cos}\!\Bigl(\dfrac{\phi+\psi}{2}\Bigr)\cdot\mathtt{cos}\!\Bigl(\dfrac{\phi-\psi}{2}\Bigr)\Bigr)\\[22pt]
(3)\quad & \mathtt{cos}(\phi)-\mathtt{cos}(\psi)=2\cdot\Bigl(\mathtt{sin}\!\Bigl(\dfrac{\phi+\psi}{2}\Bigr)\cdot\mathtt{sin}\!\Bigl(\dfrac{\phi-\psi}{2}\Bigr)\Bigr)
\end{aligned}
$$
===
$$
\begin{aligned}
(1)\quad & \mathtt{sinh}(x)+\mathtt{sinh}(y)=2\cdot\Bigl(\mathtt{sinh}\!\Bigl(\dfrac{x+y}{2}\Bigr)\cdot\mathtt{cosh}\!\Bigl(\dfrac{x-y}{2}\Bigr)\Bigr)\\[22pt]
(2)\quad & \mathtt{cosh}(x)+\mathtt{cosh}(y)=2\cdot\Bigl(\mathtt{cosh}\!\Bigl(\dfrac{x+y}{2}\Bigr)\cdot\mathtt{cosh}\!\Bigl(\dfrac{x-y}{2}\Bigr)\Bigr)\\[22pt]
(3)\quad & \mathtt{cosh}(x)-\mathtt{cosh}(y)=2\cdot\Bigl(\mathtt{sinh}\!\Bigl(\dfrac{x+y}{2}\Bigr)\cdot\mathtt{sinh}\!\Bigl(\dfrac{x-y}{2}\Bigr)\Bigr)
\end{aligned}
$$
```

## Calculus:
### Derivatives
#### Part I:
Hyperbolic: All positive | All negative
```columns
id: tFVmUaVBal2bKS_01oi1-
===
$$
\begin{array}{rcl|rcl}
\mathtt{\dfrac{d}{d\theta}\big(\sin(\theta)\big)} &=& \mathtt{\cos(\theta)}
& \mathtt{\dfrac{d}{d\theta}\big(\csc(\theta)\big)} &=& \mathtt{-\,\csc(\theta)\cdot\cot(\theta)}
\\[6pt]
\mathtt{\dfrac{d}{d\theta}\big(\cos(\theta)\big)} &=& \mathtt{-\,\sin(\theta)}
& \mathtt{\dfrac{d}{d\theta}\big(\sec(\theta)\big)} &=& \mathtt{\sec(\theta)\cdot\tan(\theta)}
\\[6pt]
\mathtt{\dfrac{d}{d\theta}\big(\tan(\theta)\big)} &=& \mathtt{\sec^{2}(\theta)}
& \mathtt{\dfrac{d}{d\theta}\big(\cot(\theta)\big)} &=& \mathtt{-\,\csc^{2}(\theta)}
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
#### Part II:

- Inverse order, compared with trig. counterparts, e.g., $$
\begin{aligned}
& \bigl(\mathtt{sin}^{-1}(x)\bigr)'=\dfrac{1}{\sqrt{1-x^{2}}}\qquad \mathtt{vs.}\qquad \bigl(\mathtt{sinh}^{-1}(x)\bigr)'=\dfrac{1}{\sqrt{x^{2}+1}}
\qquad (\mathtt{for\ }\mathtt{sin}^{-1}:\ -1<x<1)
\end{aligned}
$$
	- Stemming from hyperbolic inverse formulas, e.g., $$
\begin{aligned}
& \mathtt{sinh}^{-1}(x)=\mathtt{ln}\bigl(x+\sqrt{x^{2}+1}\,\bigr)\qquad \mathtt{vs.}\qquad \bigl(\mathtt{sinh}^{-1}(x)\bigr)'=\dfrac{1}{\sqrt{x^{2}+1}}
\qquad (\mathtt{valid\ for\ all\ }x\in\mathbb{R})
\end{aligned}
$$
- Same pattern as hyperbolic inverse formulas for Tanh and Coth
```columns
id: DDOvjpE5PYp7Ngl1Gq1aL
===
$$
\begin{array}{rcl|rcl}
\bigl(\mathtt{sin}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{\sqrt{1-x^{2}}}}\ (\mathtt{-1<x<1})
& \bigl(\mathtt{csc}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{\lvert x\rvert\cdot \sqrt{x^{2}-1}}}\ (\mathtt{\lvert x\rvert>1})
\\[6pt]
\bigl(\mathtt{cos}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{\sqrt{1-x^{2}}}}\ (\mathtt{-1<x<1})
& \bigl(\mathtt{sec}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{\lvert x\rvert\cdot \sqrt{x^{2}-1}}}\ (\mathtt{\lvert x\rvert>1})
\\[6pt]
\bigl(\mathtt{tan}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{1+x^{2}}}
& \bigl(\mathtt{cot}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{1+x^{2}}}
\end{array}
$$

===
$$
\begin{array}{rcl|rcl}
\bigl(\mathtt{sinh}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{\sqrt{x^{2}+1}}}
& \bigl(\mathtt{csch}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{\lvert x\rvert\cdot \sqrt{1+x^{2}}}}\ (\mathtt{x\ne 0})
\\[6pt]
\bigl(\mathtt{cosh}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{\sqrt{x^{2}-1}}}\ (\mathtt{x>1})
& \bigl(\mathtt{sech}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{x\cdot \sqrt{1-x^{2}}}}\ (\mathtt{0<x<1})
\\[6pt]
\bigl(\mathtt{tanh}^{-1}(x)\bigr)' &=& \mathtt{\dfrac{1}{1-x^{2}}}\ (\mathtt{-1<x<1})
& \bigl(\mathtt{coth}^{-1}(x)\bigr)' &=& \mathtt{-\,\dfrac{1}{x^{2}-1}}\ (\mathtt{\lvert x\rvert>1})
\end{array}
$$
```
### Integrals
#### Part III:
- For the trig. non-simple ones (i.e., tan, csc, sec, cot), the hyperbolic counterparts have their inside reciprocated, e.g., $$
\begin{aligned}
& \int \mathtt{tan}\,\theta\,d\theta=\mathtt{ln}\lvert \mathtt{sec}\,\theta\rvert \ \to\ \int \mathtt{tanh}\,x\,dx=\mathtt{ln}\Bigl\lvert \bigl(\mathtt{sech}(x)\bigr)^{-1}\Bigr\rvert
\end{aligned}
$$
- If it has two expression, choose the nonrepeating one, e.g.,$$
\begin{aligned}
& \int \mathtt{csc}\,\theta\,d\theta=\mathtt{ln}\lvert \mathtt{csc}\,\theta-\mathtt{cot}\,\theta\rvert \ \to\ \int \mathtt{csch}\,x\,dx=\mathtt{ln}\Bigl\lvert \bigl(\mathtt{coth}\bigl(\dfrac{x}{2}\bigr)\bigr)^{-1}\Bigr\rvert
\end{aligned}
$$
- The previous two rules do not apply to Sech(x)

```columns
id: XKNc9NKvHKj-VmmRLtZ3i
===
$$
\begin{array}{rcl|rcl}
\int \mathtt{sin}\,\theta\,d\theta &=& -\,\mathtt{cos}\,\theta
& \int \mathtt{csc}\,\theta\,d\theta &=& \mathtt{ln}\lvert \mathtt{csc}\,\theta-\mathtt{cot}\,\theta\rvert
\\[6pt]
\int \mathtt{cos}\,\theta\,d\theta &=& \mathtt{sin}\,\theta
& \int \mathtt{sec}\,\theta\,d\theta &=& \mathtt{ln}\lvert \mathtt{sec}\,\theta+\mathtt{tan}\,\theta\rvert
\\[6pt]
\int \mathtt{tan}\,\theta\,d\theta &=& \mathtt{ln}\lvert \mathtt{sec}\,\theta\rvert
& \int \mathtt{cot}\,\theta\,d\theta &=& \mathtt{ln}\lvert \mathtt{sin}\,\theta\rvert
\end{array}
$$

===
$$
\begin{array}{rcl|rcl}
\int \mathtt{sinh}\,x\,dx &=& \mathtt{cosh}\,x
& \int \mathtt{csch}\,x\,dx &=& \mathtt{ln}\Bigl\lvert \bigl(\mathtt{coth}\bigl(\dfrac{x}{2}\bigr)\bigr)^{-1}\Bigr\rvert
\\[6pt]
\int \mathtt{cosh}\,x\,dx &=& \mathtt{sinh}\,x
& \int \mathtt{sech}\,x\,dx &=& \mathtt{tan}^{-1}\!\bigl(\mathtt{sinh}\,x\bigr)
\\[6pt]
\int \mathtt{tanh}\,x\,dx &=& \mathtt{ln}\Bigl\lvert \bigl(\mathtt{sech}\,x\bigr)^{-1}\Bigr\rvert
& \int \mathtt{coth}\,x\,dx &=& \mathtt{ln}\Bigl\lvert \bigl(\mathtt{csch}\,x\bigr)^{-1}\Bigr\rvert
\end{array}
$$
```
#### Part IV:
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
#### Part V:
Hyperbolic: All negative & Part II's rules | All positive & Sech(x)'s exception in Part III
```columns
id: 0jQwtwSoIODhIjbUdnud5
===
$$
\begin{array}{rcl|rcl}
\int \mathtt{sin}^{-1}x\,dx &=& x\cdot \mathtt{sin}^{-1}x+\sqrt{1-x^{2}}\ (\mathtt{-1<x<1})
& \int \mathtt{csc}^{-1}x\,dx &=& x\cdot \mathtt{csc}^{-1}x+\mathtt{ln}\lvert x+\sqrt{x^{2}-1}\rvert\ (\mathtt{\lvert x\rvert>1})
\\[6pt]
\int \mathtt{cos}^{-1}x\,dx &=& x\cdot \mathtt{cos}^{-1}x-\sqrt{1-x^{2}}\ (\mathtt{-1<x<1})
& \int \mathtt{sec}^{-1}x\,dx &=& x\cdot \mathtt{sec}^{-1}x-\mathtt{ln}\lvert x+\sqrt{x^{2}-1}\rvert\ (\mathtt{\lvert x\rvert>1})
\\[6pt]
\int \mathtt{tan}^{-1}x\,dx &=& x\cdot \mathtt{tan}^{-1}x-\dfrac{1}{2}\cdot \mathtt{ln}(1+x^{2})
& \int \mathtt{cot}^{-1}x\,dx &=& x\cdot \mathtt{cot}^{-1}x+\dfrac{1}{2}\cdot \mathtt{ln}(1+x^{2})\ (\mathtt{typo\ fixed:\ }x)
\end{array}
$$

===
$$
\begin{array}{rcl|rcl}
\int \mathtt{sinh}^{-1}x\,dx &=& x\cdot \mathtt{sinh}^{-1}x-\sqrt{x^{2}+1}
& \int \mathtt{csch}^{-1}x\,dx &=& x\cdot \mathtt{csch}^{-1}x+\mathtt{ln}\lvert x+\sqrt{x^{2}+1}\rvert\ (\mathtt{x\ne 0})
\\[6pt]
\int \mathtt{cosh}^{-1}x\,dx &=& x\cdot \mathtt{cosh}^{-1}x-\sqrt{x^{2}-1}\ (\mathtt{x>1})
& \int \mathtt{sech}^{-1}x\,dx &=& x\cdot \mathtt{sech}^{-1}x+\mathtt{sin}^{-1}x\ (\mathtt{0<x<1})
\\[6pt]
\int \mathtt{tanh}^{-1}x\,dx &=& x\cdot \mathtt{tanh}^{-1}x-\dfrac{1}{2}\cdot \mathtt{ln}\bigl((1-x^{2})^{-1}\bigr)\ (\mathtt{\lvert x\rvert<1})
& \int \mathtt{coth}^{-1}x\,dx &=& x\cdot \mathtt{coth}^{-1}x+\dfrac{1}{2}\cdot \mathtt{ln}\lvert 1-x^{2}\rvert\ (\mathtt{\lvert x\rvert>1;\ abs.\ added})
\end{array}
$$
```
