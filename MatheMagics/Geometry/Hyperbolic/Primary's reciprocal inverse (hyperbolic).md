---
down:
tags:
  - mathemagics/geometry/hyperbolic
---
## Definitions:
$$
\begin{aligned}
{\mathtt{sech}}^{-1}(x) &:= \ln\!\left(\dfrac{1 + \sqrt{1 - x^{2}}}{x}\right), \quad \mathtt{x \in (0, 1]}
\\[12pt]
{\mathtt{csch}}^{-1}(x) &:= \ln\!\left(\dfrac{1 + \sqrt{1 + x^{2}}}{x}\right), \quad \mathtt{x \in \mathbb{R} \setminus \{0\}}
\\[12pt]
{\mathtt{coth}}^{-1}(x) &:= \dfrac{1}{2} \ln\!\left(\dfrac{x + 1}{x - 1}\right), \qquad \quad \mathtt{x \in (-\infty, -1) \cup (1, \infty)}
\end{aligned}
$$
### Proofs:
#### ArcCsch(x):
$$
\begin{aligned}
(1)\quad & \mathtt{y = }{\mathtt{csch}}^{-1}(x)
\\[18pt]
& \mathtt{By\ definition\ of\ inverse\ function:}
\\[12pt]
(2)\quad & \mathtt{x = }{\mathtt{csch}}(y)
\\[12pt]
& \mathtt{x = \dfrac{1}{\sinh(y)}}
\\[12pt]
& \mathtt{x = \dfrac{2}{e^{y}-e^{-y}}}
\\[22pt]
& \mathtt{x = \dfrac{2}{e^{y}-e^{-y}}\cdot\left(\dfrac{e^{y}}{e^{y}}\right)}
\\[12pt]
& \mathtt{x = \dfrac{2e^{y}}{e^{2y}-1}}
\\[22pt]
& \mathtt{xe^{2y}-x = 2e^{y}}
\\[12pt]
& \mathtt{x(e^{y})^{2}-2(e^{y})-x = 0}
\\[22pt]
& \Rightarrow (3)\quad \mathtt{e^{y}=\dfrac{1\pm\sqrt{1+x^{2}}}{x}}
\\[12pt]
& \qquad\ \qquad \mathtt{\ln(e^{y})=\ln\!\left(\dfrac{1\pm\sqrt{1+x^{2}}}{x}\right)}
\\[18pt]
& \qquad\ \qquad \Rightarrow (4)\quad \mathtt{y=\ln\!\left(\dfrac{1\pm\sqrt{1+x^{2}}}{x}\right)\qquad (sub.\ from\ (1))}
\\[12pt]
& \qquad\ \qquad\ \qquad\ \qquad \mathtt{{\mathtt{csch}}^{-1}(x)=\ln\!\left(\dfrac{1\pm\sqrt{1+x^{2}}}{x}\right)}
\end{aligned}
$$

## Graphs:
### ArcCsch(x)
```columns
id: f__w9vbpOqa2GCUijWldE
===
![[Pasted image 20260109023506.png]]
===
$$
\begin{aligned}
& \mathcal{D}_{\mathtt{csch}^{-1}}=\mathbb{R}\setminus\{0\}
\\[12pt]
& \mathcal{R}_{\mathtt{csch}^{-1}}=\mathbb{R}\setminus\{0\}
\\[12pt]
& \mathtt{csch}^{-1}\in C\bigl((-\infty,0)\cup(0,\infty)\bigr)
\end{aligned}
$$
```
### ArcSech(x)
```columns
id: wr3VXV0MqscW9cCNcfyiu
===
![[Pasted image 20260109023613.png]]
===
$$
\begin{aligned}
& \mathcal{D}_{\mathtt{sech}^{-1}}=(0,1]
\\[12pt]
& \mathcal{R}_{\mathtt{sech}^{-1}}=[0,\infty)
\\[12pt]
& \mathtt{sech}^{-1}\in C\bigl((0,1]\bigr)
\end{aligned}
$$
```
### ArcCoth(x)
```columns
id: MJ67V1VztU6SZ4_Byz2Bb
===
![[Pasted image 20260109023755.png]]
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
