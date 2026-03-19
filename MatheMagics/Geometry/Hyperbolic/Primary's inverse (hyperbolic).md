---
down:
  - "[[Properties, primary's inverse hyperbolic]]"
tags:
  - mathemagics/geometry/hyperbolic
---
## Definition:
$$
\begin{array}{rcl}
\mathtt{sinh^{-1}(x)} &:=& \mathtt{\ln\!\Bigl(x+\sqrt{x^{2}+1}\Bigr)},\quad \mathtt{x\in\mathbb{R}}
\\[6pt]
\mathtt{cosh^{-1}(x)} &:=& \mathtt{\ln\!\Bigl(x+\sqrt{x^{2}-1}\Bigr)},\quad \mathtt{x\in[1,\infty)}
\\[6pt]
\mathtt{tanh^{-1}(x)} &:=& \mathtt{\dfrac{1}{2}\ln\!\Bigl(\dfrac{1+x}{1-x}\Bigr)},\quad \mathtt{x\in(-1,1)}
\end{array}
$$
### Proofs:
#### ArcSinh(x):
$$
\begin{aligned}
(1)\quad & \mathtt{y = \sinh^{-1}(x)}
\\[18pt]
& \mathtt{By\ definition\ of\ inverse\ function:}
\\[12pt]
(2)\quad & \mathtt{x = \sinh(y)}
\\[12pt]
& \mathtt{x = \dfrac{e^y - e^{-y}}{2}}
\\[12pt]
& \mathtt{2x = e^y - e^{-y}}
\\[22pt]
& \mathtt{2x = (e^y - e^{-y}) \left( \dfrac{e^y}{e^y} \right)}
\\[12pt]
& \mathtt{2x = \dfrac{e^{2y} - 1}{e^y}}
\\[22pt]
& \mathtt{2x e^y = e^{2y} - 1}
\\[12pt]
& \mathtt{e^{2y} - 2x e^y - 1 = 0}
\\[12pt]
& \mathtt{(e^y)^2 - 2x(e^y) - 1 = 0}
\\[22pt]
& \Rightarrow (3)\quad \mathtt{e^y = x \pm \sqrt{x^2 + 1}}
\\[12pt]
& \qquad \qquad \mathtt{\ln(e^y) = \ln(x \pm \sqrt{x^2 + 1})}
\\[18pt]
& \qquad \qquad \Rightarrow (4)\quad \mathtt{y = \ln(x \pm \sqrt{x^2 + 1}) \qquad (sub.\ from\ (1))}
\\[12pt]
& \qquad \qquad \qquad \qquad \mathtt{\sinh^{-1}(x) = \ln(x \pm \sqrt{x^2 + 1})}
\end{aligned}
$$
## Graphs:
### ArcSinh(x)
```columns
id: f__w9vbpOqa2GCUijWldE
===
![[Pasted image 20260111142000.png]]
===
$$
\begin{aligned}
& \mathcal{D}_{\mathtt{sinh}^{-1}}=\mathbb{R}
\\[12pt]
& \mathcal{R}_{\mathtt{sinh}^{-1}}=\mathbb{R}
\\[12pt]
& \mathtt{sinh}^{-1}\in C(\mathbb{R})
\end{aligned}
$$
```
### ArcCosh(x)
```columns
id: wr3VXV0MqscW9cCNcfyiu
===
![[Pasted image 20260111142111.png]]
===
$$
\begin{aligned}
& \mathcal{D}_{\mathtt{cosh}^{-1}}=[1,\infty)
\\[12pt]
& \mathcal{R}_{\mathtt{cosh}^{-1}}=[0,\infty)
\\[12pt]
& \mathtt{cosh}^{-1}\in C\bigl([1,\infty)\bigr)
\end{aligned}
$$

```
### ArcTanh(x)
```columns
id: MJ67V1VztU6SZ4_Byz2Bb
===
![[Pasted image 20260111142255.png]]
===
$$
\begin{aligned}
& \mathcal{D}_{\mathtt{coth}^{-1}}=(-\infty,-1)\cup(1,\infty)
\\[12pt]
& \mathcal{R}_{\mathtt{coth}^{-1}}=\mathbb{R}\setminus\{0\}
\\[12pt]
& \mathtt{coth}^{-1}\in C\bigl((-\infty,-1)\cup(1,\infty)\bigr)
\end{aligned}
$$
```
