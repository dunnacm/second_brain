---
down:
tags:
  - mathemagics/geometry/hyperbolic
---
## Logarithms
### Logarithmic forms (basic)

$$
\begin{aligned}
\ln x=\tanh^{-1}\!\Bigl(\frac{x^{2}-1}{x^{2}+1}\Bigr)
\end{aligned}
$$

### Logarithmic forms with a scale parameter

$$
\begin{aligned}
(1)\quad & \sinh^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\ln\!\Bigl(\frac{x+\sqrt{x^{2}+a^{2}}}{a}\Bigr)\\[12pt]
(2)\quad & \cosh^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\ln\!\Bigl(\frac{x+\sqrt{x^{2}-a^{2}}}{a}\Bigr)\\[12pt]
(3)\quad & \tanh^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\frac{1}{2}\ln\!\Bigl(\frac{a+x}{a-x}\Bigr)\\[12pt]
(4)\quad & \operatorname{csch}^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\ln\!\Bigl(\frac{a+\sqrt{x^{2}+a^{2}}}{x}\Bigr)\\[12pt]
(5)\quad & \operatorname{sech}^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\ln\!\Bigl(\frac{a+\sqrt{a^{2}-x^{2}}}{x}\Bigr)\\[12pt]
(6)\quad & \coth^{-1}\!\Bigl(\frac{x}{a}\Bigr)=\frac{1}{2}\ln\!\Bigl(\frac{x+a}{x-a}\Bigr)
\end{aligned}
$$

## Conversions between inverse hyperbolic functions

$$
\begin{aligned}
(1)\quad & \sinh^{-1}x=\cosh^{-1}\!\sqrt{x^{2}+1}\\[12pt]
(2)\quad & \cosh^{-1}x=\sinh^{-1}\!\sqrt{x^{2}-1}\\[12pt]
(3)\quad & \coth^{-1}x=\operatorname{csch}^{-1}\!\sqrt{x^{2}-1}\\[12pt]
(4)\quad & \operatorname{sech}^{-1}x=\tanh^{-1}\!\sqrt{1-x^{2}}\\[12pt]
(5)\quad & \tanh^{-1}x=\operatorname{sech}^{-1}\!\sqrt{1-x^{2}}\\[18pt]
(6)\quad & \sinh^{-1}x=\tanh^{-1}\!\Bigl(\frac{x}{\sqrt{x^{2}+1}}\Bigr)\\[12pt]
(7)\quad & \cosh^{-1}x=\tanh^{-1}\!\sqrt{1-\frac{1}{x^{2}}}\\[12pt]
(8)\quad & \tanh^{-1}x=\sinh^{-1}\!\Bigl(\frac{x}{\sqrt{1-x^{2}}}\Bigr)
\end{aligned}
$$
### Proofs:
#### 1:
##### 1.1:
$$
\begin{aligned}
(1)\quad & \mathtt{cosh}^{-1}(u)=\mathtt{ln}\!\Bigl(u+\sqrt{u^{2}-1}\Bigr)\\[18pt]
(2)\quad & u=\sqrt{x^{2}+1}\\[22pt]
& \mathtt{Sub.\ (2)\ into\ (1):}\\[18pt]
(1')\quad & \mathtt{cosh}^{-1}\!\Bigl(\sqrt{x^{2}+1}\Bigr)=\mathtt{ln}\!\Bigl(\sqrt{x^{2}+1}+\sqrt{\bigl(\sqrt{x^{2}+1}\bigr)^{2}-1}\Bigr)\\[18pt]
& \qquad\qquad\qquad\quad\ \ =\mathtt{ln}\!\Bigl(\sqrt{x^{2}+1}+x\Bigr)\\[18pt]
& \qquad\qquad\qquad\quad\ \ =\mathtt{sinh}^{-1}(x)
\end{aligned}
$$
##### 1.2:
$$\begin{aligned}
(1)\quad & u := \mathtt{sinh}(x) \\[12pt]
& \Rightarrow (2)\quad x = \mathtt{sinh}^{-1}(u) \\[22pt]
& \mathtt{From\ pythagorean-like\ identities:} \\[12pt]
(3)\quad & \mathtt{cosh}^2 x - \mathtt{sinh}^2 x = 1 \\[12pt]
& \Rightarrow (4)\quad \mathtt{cosh}\,x = \sqrt{1 + \mathtt{sinh}^2 x} \\[12pt]
& \qquad\ \Rightarrow (5)\quad x = \mathtt{cosh}^{-1}\bigl(\sqrt{1+\mathtt{sinh}^2 x}\,\bigr) && (\mathtt{sub.\ from\ (1)};\ \text{requires } x \ge 0) \\[12pt]
& \qquad\ \phantom{\Rightarrow (5)\quad} x = \mathtt{cosh}^{-1}\bigl(\sqrt{1+u^2}\,\bigr) && (\mathtt{sub.\ from\ (2)}) \\[18pt]
& \qquad\ \phantom{\Rightarrow (5)\quad} \mathtt{sinh}^{-1}(u) = \mathtt{cosh}^{-1}\bigl(\sqrt{1+u^2}\,\bigr) && (\text{valid for } u \ge 0)
\end{aligned}$$

## Doubling / halving identities

$$
\begin{aligned}
(1)\quad & 2\cosh^{-1}x=\cosh^{-1}(2x^{2}-1)\\[12pt]
(2)\quad & 2\sinh^{-1}x=\cosh^{-1}(2x^{2}+1)\\[12pt]
(3)\quad & 2\sinh^{-1}x=\sinh^{-1}\!\Bigl(2x\sqrt{x^{2}+1}\Bigr)\\[12pt]
(4)\quad & 2\cosh^{-1}x=\sinh^{-1}\!\Bigl(2x\sqrt{x^{2}-1}\Bigr)\\[18pt]
(5)\quad & \cosh^{-1}x=2\sinh^{-1}\!\sqrt{\frac{x-1}{2}}\\[12pt]
(6)\quad & 2\tanh^{-1}x=\tanh^{-1}\!\Bigl(\frac{2x}{1+x^{2}}\Bigr)\\[12pt]
(7)\quad & 2\tanh^{-1}x=\sinh^{-1}\!\Bigl(\frac{2x}{1-x^{2}}\Bigr)\\[12pt]
(8)\quad & 2\tanh^{-1}x=\cosh^{-1}\!\Bigl(\frac{1+x^{2}}{1-x^{2}}\Bigr)
\end{aligned}
$$
### Proofs:
#### 1. 
$$\begin{aligned}
(1)\quad & \mathtt{cosh}^{-1}(u) = \mathtt{ln}\bigl(u + \sqrt{u^2-1}\,\bigr) \\[12pt]
(2)\quad & u := 2x^2 - 1 \\[18pt]
& \mathtt{Sub.\ (2)\ into\ (1):} \\[12pt]
(1')\quad & \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( (2x^2-1) + \sqrt{(2x^2-1)^2 - 1} \Bigr) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( (2x^2-1) + \sqrt{4x^4 - 4x^2} \Bigr) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( 2x^2-1 + 2x\sqrt{x^2-1} \Bigr) && (\text{requires } x \ge 1) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( x^2 + (x^2-1) + 2x\sqrt{x^2-1} \Bigr) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( x^2 + 2x\sqrt{x^2-1} + (x^2-1) \Bigr) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = \mathtt{ln}\Bigl( \bigl(x + \sqrt{x^2-1}\,\bigr)^2 \Bigr) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = 2 \cdot \mathtt{ln}\bigl( x + \sqrt{x^2-1} \bigr) && (\text{valid since } x+\sqrt{x^2-1} > 0) \\[12pt]
& \mathtt{cosh}^{-1}(2x^2-1) = 2 \cdot \mathtt{cosh}^{-1}(x) && (\text{valid for } x \ge 1)
\end{aligned}$$
## Exponential / logarithmic reconstructions

$$
\begin{aligned}
(1)\quad & \mathtt{exp}\!\Bigl(\mathtt{sinh}^{-1}x\Bigr)=x+\sqrt{x^{2}+1}\\[12pt]
(2)\quad & \mathtt{exp}\!\Bigl(\mathtt{cosh}^{-1}x\Bigr)=x+\sqrt{x^{2}-1} \qquad (x\ge 1)\\[12pt]
(3)\quad & \frac{\mathtt{exp}\!\Bigl(2\mathtt{tanh}^{-1}x\Bigr)-1}{\mathtt{exp}\!\Bigl(2\mathtt{tanh}^{-1}x\Bigr)+1}=x \qquad (\lvert x\rvert<1)\\[12pt]
(4)\quad & \mathtt{tanh}^{-1}\!\Bigl(\frac{\mathtt{exp}(2x)-1}{\mathtt{exp}(2x)+1}\Bigr)=x\\[12pt]
(5)\quad & \mathtt{exp}\!\Bigl(\mathtt{tanh}^{-1}\!\Bigl(\frac{x^{2}-1}{x^{2}+1}\Bigr)\Bigr)=\lvert x\rvert \qquad (x\ne 0)
\end{aligned}
$$
## Sum (addition) identities

$$
\begin{aligned}
(1)\quad & \sinh^{-1}x+\sinh^{-1}y=\sinh^{-1}\!\Bigl(x\sqrt{y^{2}+1}+y\sqrt{x^{2}+1}\Bigr)\\[12pt]
(2)\quad & \cosh^{-1}x+\cosh^{-1}y=\sinh^{-1}\!\Bigl(x\sqrt{y^{2}-1}+y\sqrt{x^{2}-1}\Bigr)\\[12pt]
(3)\quad & \sinh^{-1}x+\cosh^{-1}y=\cosh^{-1}\!\Bigl(x\sqrt{y^{2}-1}+y\sqrt{x^{2}+1}\Bigr)\\[12pt]
(4)\quad & \sinh^{-1}x+\cosh^{-1}y=\sinh^{-1}\!\Bigl(xy+\sqrt{(y^{2}-1)(x^{2}+1)}\Bigr)\\[12pt]
(5)\quad & \sinh^{-1}x+\sinh^{-1}y=\cosh^{-1}\!\Bigl(xy+\sqrt{(y^{2}+1)(x^{2}+1)}\Bigr)\\[12pt]
(6)\quad & \cosh^{-1}x+\cosh^{-1}y=\cosh^{-1}\!\Bigl(xy+\sqrt{(y^{2}-1)(x^{2}-1)}\Bigr)
\end{aligned}
$$
### Proofs:
#### 1. 
$$
\begin{aligned}
(1)\quad & x:=\mathtt{sinh}(u) \\[12pt]
& \Rightarrow (2)\quad u=\mathtt{sinh}^{-1}(x) \\[18pt]
(3)\quad & y=\mathtt{sinh}(v) \\[12pt]
& \Rightarrow (4)\quad v=\mathtt{sinh}^{-1}(y) \\[22pt]
& \mathtt{Addition/ subtraction\ property:} \\[12pt]
(5)\quad & \mathtt{sinh}(u\pm v)=\mathtt{sinh}(u)\mathtt{cosh}(v)\pm \mathtt{sinh}(v)\cdot \mathtt{cosh}(u) \\[22pt]
& \mathtt{Applying\ }\mathtt{sinh}^{-1}\ \mathtt{on\ LHS\ and\ RHS:} \\[12pt]
(6)\quad & \mathtt{sinh}^{-1}\!\bigl(\mathtt{sinh}(u\pm v)\bigr)=\mathtt{sinh}^{-1}\!\bigl(\mathtt{sinh}(u)\mathtt{cosh}(v)\pm \mathtt{sinh}(v)\cdot \mathtt{cosh}(u)\bigr) \\[12pt]
& u\pm v=\mathtt{sinh}^{-1}\!\bigl(x\cdot \mathtt{cosh}(v)\pm y\cdot \mathtt{cosh}(u)\bigr) 
&& (\mathtt{sub.\ from\ (2),(4);\ and\ }\mathtt{sinh}^{-1}\circ\mathtt{sinh}=\mathtt{id\ on\ }\mathbb{R}) \\[12pt]
& \mathtt{sinh}^{-1}x\pm \mathtt{sinh}^{-1}y=\mathtt{sinh}^{-1}\!\bigl(x\cdot \mathtt{cosh}(v)\pm y\cdot \mathtt{cosh}(u)\bigr) \\[22pt]
& \mathtt{From\ pithagorean-like\ identity:} \\[12pt]
(7)\quad & \mathtt{cosh}^{2}(u)-\mathtt{sinh}^{2}(u)=1 \\[12pt]
& \Rightarrow (8)\quad \mathtt{cosh}(u)=\sqrt{1+\mathtt{sinh}^{2}(u)} 
&& (\mathtt{sub.\ from\ (1);\ and\ }\mathtt{cosh}\,u>0) \\[12pt]
& \qquad\ \Rightarrow (9)\quad \mathtt{cosh}(u)=\sqrt{1+x^{2}} \\[22pt]
& \mathtt{Similarly\ to\ process\ (7)\ through\ (9):\ (10)\ }\mathtt{cosh}(v)=\sqrt{1+y^{2}}
\qquad (\mathtt{and\ }\mathtt{cosh}\,v>0) \\[22pt]
& \mathtt{Sub.\ (9)\ and\ (10)\ into\ (6):} \\[12pt]
(6')\quad & \mathtt{sinh}^{-1}x\pm \mathtt{sinh}^{-1}y=\mathtt{sinh}^{-1}\!\bigl(x\cdot \mathtt{cosh}(v)\pm y\cdot \mathtt{cosh}(u)\bigr) \\[12pt]
& \mathtt{sinh}^{-1}x\pm \mathtt{sinh}^{-1}y=\mathtt{sinh}^{-1}\!\bigl(x\cdot \sqrt{1+y^{2}}\pm y\cdot \sqrt{1+x^{2}}\bigr)
\end{aligned}
$$