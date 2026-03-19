---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Complementary-sum identities (inverse trig)

**Principal values :**  

- $-\dfrac{\pi}{2}\le \theta\le \dfrac{\pi}{2}$ for $\sin\theta,\tan\theta,\csc\theta$;  
- $0\le \theta\le \pi$ for $\cos\theta,\cot\theta,\sec\theta$ (excluding undefined values).

### $\boldsymbol{\sin^{-1}x+\cos^{-1}x=\dfrac{\pi}{2}.}$
#### Proof:
```tikz
\usepackage{tikz}
\usetikzlibrary{calc}

\begin{document}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]

% Key points - matching your coordinate scale
\coordinate (A) at (0,0);
\coordinate (B) at (0,3);
\coordinate (C) at (4,3);
\coordinate (D) at (4,0);

% Axes - extending beyond points for arrowheads
\draw[very thick, ->] (A) -- ($(D)+(0.7,0)$);
\draw[very thick, ->] (A) -- ($(B)+(0,0.7)$);

% Dashed projections (top and right) - matching user thickness
\draw[very thick, dashed] (B) -- (C);
\draw[very thick, dashed] (C) -- (D);

% Diagonal vector
\draw[very thick, ->] (A) -- (C);

% Angle arcs at A
% diagonal angle ≈ 36.87°

% phi: from x-axis to diagonal
\draw[very thick] ($(A)+(0.9,0)$) arc (0:36.87:0.9);
\node at ($(A)+(1.25,0.30)$) {\Large $\phi$};

% psi: from diagonal to y-axis (Reverted from theta to match proof notes)
\draw[very thick] ($(A)+(0,1.15)$) arc (90:36.87:1.15);
\node at ($(A)+(0.55,1.30)$) {\Large $\psi$};

% Labels for vertices
\node[left]  at (A) {\Large $A$};
\node[left]  at (B) {\Large $B$};
\node[above right] at (C) {\Large $C$};
\node[below right] at (D) {\Large $D$};

\end{tikzpicture}
\end{document}
```
$$
\begin{aligned}
& \mathtt{From\ diagram,\ eqs.\ (1),(2),(4)\ follow:}
\\[12pt]
(1)\quad & \phi+\psi=\frac{\pi}{2}
\\[18pt]
(2)\quad & \sin\phi=y \ \Rightarrow\ (3)\quad \sin^{-1}(y)=\phi
\\[18pt]
(4)\quad & \cos\psi=y \ \Rightarrow\ (5)\quad \cos^{-1}(y)=\psi
\\[22pt]
& \mathtt{Sub.\ (3),(5)\ into\ (1):}
\\[12pt]
(1')\quad & \phi+\psi=\frac{\pi}{2}
\\[12pt]
& \sin^{-1}(y)+\cos^{-1}(y)=\frac{\pi}{2}
\end{aligned}
$$


### $\boldsymbol{\sec^{-1}x+\csc^{-1}x=\dfrac{\pi}{2}.}$
**Assumption:** $\lvert x\rvert\ge 1$ (principal-value convention as stated above).

### $\boldsymbol{\tan^{-1}x+\cot^{-1}x=\dfrac{\pi}{2}.}$
**Assumption:** $x\in\mathbb{R}$ (with $\cot^{-1}x\in(0,\pi)$ under the stated principal values).
## Principal-value sum/difference formulas

### $\boldsymbol{\sin^{-1}x\pm\sin^{-1}y=\sin^{-1}\!\Big(x\sqrt{1-y^2}\pm y\sqrt{1-x^2}\Big).}$
**Assumption:** $-1\le x\le 1$, $-1\le y\le 1$, and the resulting angle is in the principal range of $\sin^{-1}$.
#### Proof  1:

```tikz
\usepackage{tikz}
\usetikzlibrary{calc}

\begin{document}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]

% Key points
\coordinate (A) at (0,0);
\coordinate (B) at (0,3);
\coordinate (C) at (4,3);
\coordinate (D) at (4,0);

% Axes
\draw[very thick, ->] (A) -- ($(D)+(0.7,0)$);
\draw[very thick, ->] (A) -- ($(B)+(0,0.7)$);

% Dashed projections (top and right)
\draw[very thick, dashed] (B) -- (C);
\draw[very thick, dashed] (C) -- (D);

% Diagonal vector
\draw[very thick, ->] (A) -- (C);

% Angle arcs at A
% diagonal angle = arctan(3/4) ≈ 36.87°
\def\diagAng{36.87}

% phi: from x-axis to diagonal
\draw[very thick] ($(A)+(0.9,0)$) arc (0:\diagAng:0.9);
\node at ($(A)+(1.25,0.30)$) {\Large $\phi$};

% theta: from diagonal to y-axis
\draw[very thick] ($(A)+(0,1.15)$) arc (90:\diagAng:1.15);
\node at ($(A)+(0.55,1.30)$) {\Large $\theta$};

% Labels
\node[left]  at (A) {\Large $A$};
\node[left]  at (B) {\Large $B$};
\node[above right] at (C) {\Large $C$};
\node[below right] at (D) {\Large $D$};

\end{tikzpicture}
\end{document}

```
$$
\begin{aligned}
(1)\quad & \sin(\theta\pm\phi)=\sin\theta\cdot\cos\phi \pm \sin\phi\cdot\cos\theta \\[18pt]
& \mathtt{From\ diagram,\ eqs.\ (2),(3),(4),(5)\ follow:} \\[12pt]
(2)\quad & \sin\theta=x \\[12pt]
(3)\quad & \sin\phi=y \\[12pt]
(4)\quad & \cos\theta=y \\[12pt]
(5)\quad & \cos\phi=x \\[22pt]
& \mathtt{Expressing\ }y\mathtt{\ in\ terms\ of\ }x\mathtt{\ (from\ }\triangle ABC\mathtt{\ perspective):} \\[12pt]
(6)\quad & y=\sqrt{1-x^2} \\[22pt]
& \mathtt{Expressing\ }x\mathtt{\ in\ terms\ of\ }y\mathtt{\ (from\ }\triangle ABC\mathtt{\ perspective):} \\[12pt]
(7)\quad & x=\sqrt{1-y^2} \\[22pt]
& \mathtt{Sub.\ (6)\ into\ (3):} \\[12pt]
(3')\quad & \sin\phi=\sqrt{1-x^2} \\[22pt]
& \mathtt{Sub.\ (7)\ into\ (2):} \\[12pt]
(2')\quad & \sin\theta=\sqrt{1-y^2} \\[22pt]
& \mathtt{Sub.\ (2'),(3'),(4),(5)\ into\ (1):} \\[12pt]
(1')\quad & \sin(\theta\pm\phi)=\sin\theta\cdot\cos\phi \pm \sin\phi\cdot\cos\theta \\[12pt]
& \qquad\ \qquad\ \ \ =\sqrt{1-y^2}\cdot x \pm \sqrt{1-x^2}\cdot y \\[22pt]
& \Rightarrow (8)\quad \sin^{-1}\!\Big(\sqrt{1-y^2}\cdot x \pm \sqrt{1-x^2}\cdot y\Big)=\theta\pm\phi
\qquad (\mathtt{Implied\ by\ eqs.\ (2),(3)}) \\[14pt]
& \qquad\ \qquad\sin^{-1}\!\Big(\sqrt{1-y^2}\cdot x \pm \sqrt{1-x^2}\cdot y\Big)=\sin^{-1}(x)\pm\sin^{-1}(y)
\end{aligned}
$$

#### Proof 2:
##### Part 1:
```tikz
\usepackage{tikz}
\usetikzlibrary{calc}

\begin{document}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]

% Key points
\coordinate (A) at (0,0);
\coordinate (B) at (0,3);
\coordinate (C) at (4,3);
\coordinate (D) at (4,0);

% Axes
\draw[very thick, ->] (A) -- ($(D)+(0.7,0)$);
\draw[very thick, ->] (A) -- ($(B)+(0,0.7)$);

% Dashed projections (top and right)
\draw[very thick, dashed] (B) -- (C);
\draw[very thick, dashed] (C) -- (D);

% Diagonal vector
\draw[very thick, ->] (A) -- (C);

% Angle arcs at A
% diagonal angle = arctan(3/4) ≈ 36.87°
\def\diagAng{36.87}

% phi: from x-axis to diagonal
\draw[very thick] ($(A)+(0.9,0)$) arc (0:\diagAng:0.9);
\node at ($(A)+(1.25,0.30)$) {$\phi$};

% theta: from diagonal to y-axis
\draw[very thick] ($(A)+(0,1.15)$) arc (90:\diagAng:1.15);
\node at ($(A)+(0.55,1.30)$) {$\theta$};

% Labels
\node[left]  at (A) {\Large $A$};
\node[left]  at (B) {\Large $B$};
\node[above right] at (C) {\Large $C$};
\node[below right] at (D) {\Large $D$};

\end{tikzpicture}
\end{document}

```
$$
\begin{aligned}
& \text{From diagram, eqs. (1), (2), (3) follow:} \\[12pt]
(1)\quad & \theta+\phi=\dfrac{3\pi}{2}. \\[14pt]
(2)\quad & \sin(\theta)\big(=-\sin(\pi-\theta)\big)=-(-y)=y. \\[14pt]
(3)\quad & \sin(\phi)=-x. \\[22pt]
& \text{Expressing }y\text{ in terms of }x: \\[12pt]
(4)\quad & y=\sqrt{1-(-x)^2} \\[10pt]
& \ \ =\sqrt{1-x^2}. \\[26pt]
& \text{From diagram, eqs. (5), (6) follow:} \\[12pt]
(5)\quad & \cos(\phi)=-y. \\[14pt]
(6)\quad & \cos(\theta)\big(=-\cos(\pi-\phi)\big)=-x. \\[22pt]
& \text{Expressing }-x\text{ in terms of }y: \\[12pt]
(7)\quad & -x=\sqrt{1-y^2}. \\[26pt]
& \text{From pythagoras thm:} \\[12pt]
(8)\quad & y^2+(-x)^2=1 \\[12pt]
& y\cdot(y)-x\cdot(-x)=1 \qquad (\text{Sub. from (4), (7)}) \\[12pt]
& y\sqrt{1-x^2}-x\sqrt{1-y^2}=1. \\[26pt]
(9)\quad & \sin\!\left(\dfrac{3\pi}{2}\right)=-1 \qquad (\text{sub. from (1), (8)}) \\[12pt]
& \sin(\theta+\phi)=x\sqrt{1-y^2}-y\sqrt{1-x^2}. \\[26pt]
& \Rightarrow (10)\quad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\theta+\phi 
\qquad (\text{Implied by eqs. (2), (3)}) \\[14pt]
& \qquad\ \qquad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\sin^{-1}(y)+\sin^{-1}(-x) \\[14pt]
& \qquad\ \qquad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\sin^{-1}(y)-\sin^{-1}(x).
\end{aligned}
$$

##### Part 2:
```tikz
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta}

\begin{document}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round, >=Stealth]

%---------------------------
% Vector data (3rd quadrant)
%---------------------------
\pgfmathsetmacro{\vx}{-4}
\pgfmathsetmacro{\vy}{-3}

% Angle of the vector (degrees, normalized to [0,360))
\pgfmathsetmacro{\angraw}{atan2(\vy,\vx)}
\pgfmathsetmacro{\ang}{ifthenelse(\angraw<0,\angraw+360,\angraw)}

% Radii for arcs (kept comparable to your other diagram)
\def\rtheta{0.9}
\def\rphi{1.15}

% Key points
\coordinate (O)  at (0,0);
\coordinate (P)  at (\vx,\vy);
\coordinate (Px) at (\vx,0);
\coordinate (Py) at (0,\vy);

% Axes (match thickness/style of your reference)
\draw[very thick, <->] (-5,0) -- (5,0);
\draw[very thick, <->] (0,-4) -- (0,4);

% Dashed projections
\draw[very thick, dashed] (P) -- (Px) node[midway, left] {$-y$};
\draw[very thick, dashed] (P) -- (Py) node[midway, below] {$-x$};

% Vector
\draw[very thick, -Stealth] (O) -- (P);

%---------------------------
% Angle arcs (NO arrows)
%---------------------------
% theta: from +x-axis to the vector
\draw[very thick] ($(O)+(\rtheta,0)$) arc (0:\ang:\rtheta);
\node at ($(O)+(1.25,0.35)$) {\Large $\theta$};

% phi: from 3pi/2 (270°) to the vector
\draw[very thick] ($(O)+(0,-\rphi)$) arc (270:\ang:\rphi);
\node at ($(O)+(-0.55,-1.10)$) {\Large $\phi$};

\end{tikzpicture}
\end{document}

```
$$
\begin{aligned}
& \text{From diagram, eqs. (1), (2), (3) follow:} \\[12pt]
(1)\quad & \theta+\phi=\dfrac{3\pi}{2}. \\[14pt]
(2)\quad & \sin(\theta)\big(=-\sin(\pi-\theta)\big)=-(-y)=y. \\[14pt]
(3)\quad & \sin(\phi)=-x. \\[22pt]
& \text{Expressing }y\text{ in terms of }x: \\[12pt]
(4)\quad & y=\sqrt{1-(-x)^2} \\[10pt]
& \ \ =\sqrt{1-x^2}. \\[26pt]
& \text{From diagram, eqs. (5), (6) follow:} \\[12pt]
(5)\quad & \cos(\phi)=-y. \\[14pt]
(6)\quad & \cos(\theta)\big(=-\cos(\pi-\phi)\big)=-x. \\[22pt]
& \text{Expressing }-x\text{ in terms of }y: \\[12pt]
(7)\quad & -x=\sqrt{1-y^2}. \\[26pt]
& \text{From pythagoras thm:} \\[12pt]
(8)\quad & y^2+(-x)^2=1 \\[12pt]
& y\cdot(y)-x\cdot(-x)=1 \qquad (\text{Sub. from (4), (7)}) \\[12pt]
& y\sqrt{1-x^2}-x\sqrt{1-y^2}=1. \\[26pt]
(9)\quad & \sin\!\left(\dfrac{3\pi}{2}\right)=-1 \qquad (\text{sub. from (1), (8)}) \\[12pt]
& \sin(\theta+\phi)=x\sqrt{1-y^2}-y\sqrt{1-x^2}. \\[26pt]
& \Rightarrow (10)\quad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\theta+\phi 
\qquad (\text{Implied by eqs. (2), (3)}) \\[14pt]
& \qquad\ \qquad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\sin^{-1}(y)+\sin^{-1}(-x) \\[14pt]
& \qquad\ \qquad \sin^{-1}\!\Big(x\sqrt{1-y^2}-y\sqrt{1-x^2}\Big)=\sin^{-1}(y)-\sin^{-1}(x).
\end{aligned}
$$

### $\boldsymbol{\cos^{-1}x\pm\cos^{-1}y=\cos^{-1}\!\Big(xy\mp \sqrt{(1-x^2)(1-y^2)}\Big).}$
**Assumption:** $-1\le x\le 1$, $-1\le y\le 1$, and the resulting angle is in the principal range of $\cos^{-1}$.

### $\boldsymbol{\tan^{-1}x\pm\tan^{-1}y=\tan^{-1}\!\left(\dfrac{x\pm y}{1\mp xy}\right).}$
**Assumption:** $x,y\in\mathbb{R}$, $1\mp xy\ne 0$, and the resulting angle is in the principal range of $\tan^{-1}$.

### $\boldsymbol{\cot^{-1}x\pm\cot^{-1}y=\cot^{-1}\!\left(\dfrac{xy\mp 1}{y\pm x}\right).}$
**Assumption:** $x,y\in\mathbb{R}$, $y\pm x\ne 0$, and the resulting angle is in the principal range of $\cot^{-1}$.
