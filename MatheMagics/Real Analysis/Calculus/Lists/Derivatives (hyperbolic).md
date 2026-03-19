---
down:
  - "[[Summary (calculus) 1]]"
tags:
  - mathemagics/calculus
  - mathemagics/real_analysis
---
## Hyperbolic functions

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
## Inverse hyperbolic functions

$$
\begin{array}{rcl|rcl}
\dfrac{d}{dx}\big({\mathtt{sinh}}^{-1}(x)\big) &=& \dfrac{1}{\sqrt{1+x^{2}}},\ x\in\mathbb{R}
& \dfrac{d}{dx}\big({\mathtt{csch}}^{-1}(x)\big) &=& \dfrac{-1}{\lvert x\rvert\,\sqrt{1+x^{2}}},\ x\in\mathbb{R}\setminus\{0\}
\\[6pt]
\dfrac{d}{dx}\big({\mathtt{cosh}}^{-1}(x)\big) &=& \dfrac{1}{\sqrt{x^{2}-1}},\ x\in(1,\infty)
& \dfrac{d}{dx}\big({\mathtt{sech}}^{-1}(x)\big) &=& \dfrac{-1}{x\,\sqrt{1-x^{2}}},\ x\in(0,1)
\\[6pt]
\dfrac{d}{dx}\big({\mathtt{tanh}}^{-1}(x)\big) &=& \dfrac{1}{1-x^{2}},\ x\in(-1,1)
& \dfrac{d}{dx}\big({\mathtt{coth}}^{-1}(x)\big) &=& \dfrac{1}{1-x^{2}},\ x\in(-\infty,-1)\cup(1,\infty)
\end{array}
$$
