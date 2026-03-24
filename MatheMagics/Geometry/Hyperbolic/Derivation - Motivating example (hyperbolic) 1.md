---
down:
  - "[[MatheMagics/Logic & Set Theory/Unit circle vs unit hyperbola]]"
  - "[[Primary (hyperbolic) 1]]"
  - "[[Primary's reciprocal (hyperbolic) 1]]"
tags:
  - mathemagics/geometry/hyperbolic
---
## Diagram
![[Pasted image 20260106191347.png|400]]
### Derivation of Cosh(t):
$$
\begin{aligned}
(1)\quad & \mathtt{\dfrac{\mathcal{A}}{2}=\mathcal{A}(\triangle OPX)-\mathcal{A}(APX)}
\\[22pt]
(2)\quad & \mathtt{x^{2}-y^{2}=1\ \Rightarrow\ y=\pm\sqrt{x^{2}-1}}
\\[22pt]
& \mathtt{Coordinates\ of\ point\ P,\ in\ terms\ of\ variable\ x}
\\[12pt]
(3)\quad & \mathtt{P(x,y)\quad (x^{2}-y^{2}=1\ \Rightarrow\ y=\pm\sqrt{x^{2}-1})}
\\[12pt]
& \mathtt{=P(x,\sqrt{x^{2}-1})\ ,\quad x\in[1,\infty)}
\\[22pt]
(4)\quad & \mathtt{\mathcal{A}(\triangle OPX)=\dfrac{1}{2}\cdot [base]\cdot [height]}
\\[12pt]
& \qquad\ \qquad \mathtt{=\dfrac{1}{2}\cdot \overline{OX}\cdot \overline{PX}}
\\[12pt]
& \qquad\ \qquad \mathtt{=\dfrac{1}{2}\cdot x\cdot y\quad (Sub.\ from\ (2))}
\\[12pt]
& \qquad\ \qquad \mathtt{=\dfrac{1}{2}\cdot x\cdot \sqrt{x^{2}-1}}
\\[22pt]
(5)\quad & \mathtt{\mathcal{A}(APX)=\int_{1}^{x}\int_{y=0}^{y=\sqrt{x^{2}-1}}dy\,dx\ ,\quad x\in[1,\infty)}
\\[12pt]
& \qquad\ \qquad \mathtt{=\int_{1}^{x}\sqrt{x^{2}-1}\ dx}
\\[22pt]
& \mathtt{Sub.\ (4),(5)\ into\ (1):}
\\[12pt]
(1')\quad & \mathtt{\dfrac{\mathcal{A}}{2}=\mathcal{A}(\triangle OPX)-\mathcal{A}(APX)}
\\[18pt]
& \mathtt{\mathcal{A}=2\cdot\left[\ \dfrac{1}{2}\cdot x\cdot \sqrt{x^{2}-1}-\int_{1}^{x}\sqrt{x^{2}-1}\ dx\ \right]}
\\[12pt]
& \mathtt{\mathcal{A}=x\cdot \sqrt{x^{2}-1}-2\cdot\int_{1}^{x}\sqrt{x^{2}-1}\ dx}
\\[18pt]
& \Rightarrow (6)\quad \mathtt{\dfrac{d\mathcal{A}}{dx}=\dfrac{d}{dx}\left(\ x\cdot \sqrt{x^{2}-1}-2\cdot\int_{1}^{x}\sqrt{x^{2}-1}\ dx\ \right)}
\\[18pt]
& \qquad\ \qquad \mathtt{\dfrac{d\mathcal{A}}{dx}=\sqrt{x^{2}-1}+\dfrac{x}{2\cdot\sqrt{x^{2}-1}}\cdot 2x-2\sqrt{x^{2}-1}\ ,\quad x\in[1,\infty)}
\\[12pt]
& \qquad\ \qquad \mathtt{\dfrac{d\mathcal{A}}{dx}=\dfrac{x^{2}}{\sqrt{x^{2}-1}}-\sqrt{x^{2}-1}}
\\[12pt]
& \qquad\ \qquad \mathtt{\dfrac{d\mathcal{A}}{dx}=\dfrac{x^{2}-(x^{2}-1)}{\sqrt{x^{2}-1}}}
\\[12pt]
& \qquad\ \qquad \mathtt{\dfrac{d\mathcal{A}}{dx}=\dfrac{1}{\sqrt{x^{2}-1}}\ ,\quad x\in[1,\infty)}
\\[18pt]
& \qquad\ \Rightarrow (7)\quad \mathtt{d\mathcal{A}=\dfrac{dx}{\sqrt{x^{2}-1}}}
\\[18pt]
& \qquad\ \qquad \Rightarrow (8)\quad \mathtt{\mathcal{A}=\int \dfrac{dx}{\sqrt{x^{2}-1}}\quad (letting\ x=\sec(u))}
\\[18pt]
& \qquad\ \qquad \qquad\ \qquad \mathtt{\mathcal{A}=\int \dfrac{\sec(u)\cdot\tan(u)}{\tan(u)}\ du}
\\[12pt]
& \qquad\ \qquad \qquad\ \qquad \mathtt{\mathcal{A}=\int \sec(u)\ du}
\\[12pt]
& \qquad\ \qquad \qquad\ \qquad \mathtt{\mathcal{A}=\ln\lvert \sec(u)+\tan(u)\rvert +C}
\\[18pt]
& \qquad\ \qquad \qquad\ \qquad \mathtt{\mathcal{A}=\ln(x+\sqrt{x^{2}-1})+C\ ,\quad x\in[1,\infty)}
\\[22pt]
& \mathtt{If\ x=1\ (from\ diagram)\ then:}
\\[18pt]
(9)\quad & \mathtt{\mathcal{A}=0\quad (Sub.\ from\ (8))}
\\[18pt]
& \mathtt{\ln(1+\sqrt{1^{2}-1})+C=0}
\\[12pt]
& \mathtt{\ln(1)+C=0}
\\[18pt]
& \Rightarrow (10)\quad \mathtt{C=0}
\\[22pt]
& \mathtt{Sub.\ (10)\ into\ (8):}
\\[18pt]
(8')\quad & \mathtt{\mathcal{A}=\ln(x+\sqrt{x^{2}-1})\ ,\quad x\in[1,\infty)}
\\[18pt]
& \Rightarrow (11)\quad \mathtt{e^{\mathcal{A}}=x+\sqrt{x^{2}-1}}
\\[18pt]
& \qquad\ \qquad \mathtt{e^{\mathcal{A}}-x=\sqrt{x^{2}-1}}
\\[18pt]
& \qquad\ \qquad \mathtt{(e^{\mathcal{A}}-x)^{2}=x^{2}-1}
\\[18pt]
& \qquad\ \qquad \mathtt{e^{2\mathcal{A}}-2\cdot e^{\mathcal{A}}\cdot x+x^{2}=x^{2}-1}
\\[18pt]
& \qquad\ \qquad \mathtt{2\cdot e^{\mathcal{A}}\cdot x=1+e^{2\mathcal{A}}}
\\[18pt]
& \qquad\ \qquad \mathtt{x=\dfrac{1+e^{2\mathcal{A}}}{2e^{\mathcal{A}}}}
\\[18pt]
& \qquad\ \Rightarrow (12)\quad \mathtt{x=\dfrac{1}{2}\cdot\left(e^{-\mathcal{A}}+e^{\mathcal{A}}\right)}
\\[22pt]
& \qquad\ \qquad\ \qquad\ \mathtt{x=\cosh(\mathcal{A})\ ,\quad \mathcal{A}\in[0,\infty)}
\end{aligned}
$$
### Derivation of Sinh(t):
$$
\begin{aligned}
(1)\quad & \mathtt{x^{2}-y^{2}=1}
\\[22pt]
& \Rightarrow (2)\quad \mathtt{y=\sqrt{x^{2}-1}\quad (taking\ the\ +\ branch)}
\\[22pt]
& \mathtt{From\ previous\ proof:\ (3)\ x=\cosh(t),\ t\in\mathbb{N}_{0}.}
\\[22pt]
& \mathtt{Sub.\ (3)\ into\ (2):}
\\[18pt]
(2')\quad & \mathtt{y=\sqrt{\cosh^{2}(t)-1}\quad (from\ def.\ of\ \cosh(t))}
\\[18pt]
& \mathtt{y=\sqrt{\left(\dfrac{e^{t}+e^{-t}}{2}\right)^{2}-1}}
\\[18pt]
& \mathtt{y=\sqrt{\dfrac{(e^{t}+e^{-t})^{2}}{4}-\dfrac{4}{4}}}
\\[18pt]
& \mathtt{y=\dfrac{1}{2}\cdot\sqrt{(e^{t}+e^{-t})^{2}-4}}
\\[18pt]
& \mathtt{y=\dfrac{1}{2}\cdot\sqrt{(e^{t}+e^{-t})^{2}-4\cdot e^{t}\cdot e^{-t}}\qquad (Applying\ (a+b)^{2}-4ab=(a-b)^{2})}
\\[18pt]
& \mathtt{y=\dfrac{1}{2}\cdot\sqrt{(e^{t}-e^{-t})^{2}}}
\\[18pt]
& \mathtt{y=\dfrac{1}{2}\cdot(e^{t}-e^{-t})\quad (t\in\mathbb{N}_{0})}
\\[18pt]
& \mathtt{y=\sinh(t),\ t\in\mathbb{N}_{0}.}
\end{aligned}
$$
## Exercises:

#### 1
![[Pasted image 20260106232727.png|400]]
$$
\begin{aligned}
& \mathtt{From\ proof\ in\ \cosh(t),\ eqs.\ (8'):}
\\[22pt]
(1)\quad & \mathtt{\mathcal{A}=\ln\left(x+\sqrt{x^{2}-1}\right)}
\\[22pt]
(2)\quad & \mathtt{\tan\left(\dfrac{\pi}{6}\right)=\dfrac{y}{x}\qquad (x^{2}-y^{2}=1\Rightarrow y=\sqrt{x^{2}-1})}
\\[22pt]
& \mathtt{\dfrac{\sqrt{3}}{3}=\dfrac{\sqrt{x^{2}-1}}{x}}
\\[22pt]
& \mathtt{x\cdot\sqrt{3}=3\cdot\sqrt{x^{2}-1}}
\\[22pt]
& \mathtt{3\cdot x^{2}=9\cdot(x^{2}-1)}
\\[22pt]
& \mathtt{3x^{2}=9x^{2}-9}
\\[22pt]
& \mathtt{6x^{2}=9}
\\[22pt]
& \Rightarrow (3)\quad \mathtt{x=\dfrac{\sqrt{6}}{2}}
\\[22pt]
& \mathtt{Sub.\ (3)\ into\ (1):}
\\[22pt]
(1')\quad & \mathtt{\mathcal{A}=\ln\left(x+\sqrt{x^{2}-1}\right)}
\\[22pt]
& \mathtt{\mathcal{A}=\ln\left(\dfrac{\sqrt{6}}{2}+\sqrt{\dfrac{3}{2}-1}\right)}^*
\\[22pt]
& \mathtt{\mathcal{A}=\ln\left(\sqrt{2+\sqrt{3}}\right)}
\end{aligned}
$$
---
*
$$
\begin{aligned}
& \mathtt{\dfrac{\sqrt{6}}{2}+\sqrt{\dfrac{3}{2}-1}=\dfrac{\sqrt{6}+\sqrt{2}}{2}}
\\[22pt]
& \mathtt{\qquad\qquad\qquad\quad=\left[\left(\dfrac{\sqrt{6}+\sqrt{2}}{2}\right)^{2}\right]^{\frac{1}{2}}}
\\[22pt]
& \mathtt{\qquad\qquad\qquad\quad=\left[\dfrac{6+2\sqrt{12}+2}{4}\right]^{\frac{1}{2}}}
\\[22pt]
& \mathtt{\qquad\qquad\qquad\quad=\left[2+\sqrt{3}\right]^{\frac{1}{2}}}
\end{aligned}
$$
