---
down:
tags:
  - mathemagics/geometry/euclidean
---
## 1. 
**Statement**: Show that if a triangle is inscribed in a circle with a diameter equal to *d*, then $\boldsymbol{\dfrac{\sin A}{a}=\dfrac{\sin B}{b}=\dfrac{\sin C}{c}=\dfrac{1}{d}.}$

![[Pasted image 20251218152334.png|200]]
**Solution**:
$$
\begin{aligned}
(1)\quad & \text{By inscribed angle thm.: } B=B'. \\[10pt]
(2)\quad & \text{By Thales's thm.: } \angle C'=\dfrac{\pi}{2}. \\[14pt]
(3)\quad & \text{From }\triangle ABC: \\[8pt]
\qquad\ \qquad\ & \dfrac{b}{\sin(B)}=k=\left(\dfrac{a}{\sin(A)}=\dfrac{c}{\sin(C)}\right). \\[16pt]
(4)\quad & \text{From }\triangle AB'C: \\[8pt]
\qquad\ \qquad\ & \dfrac{b}{\sin(B')} \qquad (\text{sub. from (1)}) \\[8pt]
\qquad\ \qquad\ & =\dfrac{b}{\sin(B)} \\[8pt]
\qquad\ \qquad\ & =k. \\[16pt]
(5)\quad & \dfrac{d}{\sin(C')} \qquad (\text{sub. from (2)}) \\[8pt]
\qquad\ \qquad\ & =\dfrac{d}{\sin\!\left(\dfrac{\pi}{2}\right)}. \\[16pt]
(6)\quad & \text{From Law of Sines and (4), (5):} \\[8pt]
\qquad\ \qquad\ & \dfrac{d}{\sin\!\left(\dfrac{\pi}{2}\right)}=k \\[8pt]
\qquad\ \qquad\ & d=k. \\[16pt]
(3')\quad & \text{Sub. (6) into (3):} \\[8pt]
\qquad\ \qquad\ & \dfrac{b}{\sin(B)}=d=\left(\dfrac{a}{\sin(A)}=\dfrac{c}{\sin(C)}\right).
\end{aligned}
$$


$$
\boldsymbol{\therefore\ \dfrac{\sin(A)}{a}=\dfrac{\sin(B)}{b}=\dfrac{\sin(C)}{c}=\dfrac{1}{d}.}
$$
## 2.
**Statement**: $$A=30^\circ,\quad a=1,\quad b=1.$$ (One triangle from two possible ones)
**Solution**:
$$
\begin{aligned}
A=30^\circ,\ a=b=1. \\[14pt]
(1)\quad & \dfrac{1}{\sin(30^\circ)}=\dfrac{1}{\sin(B)} \\[10pt]
& \Rightarrow (2)\quad \sin(B)=\dfrac{1}{2}. \\[18pt]
\textbf{Case I: $B$ is acute} \\[10pt]
(3)\quad & \sin(B)=\dfrac{1}{2} \\[8pt]
& \Rightarrow (4)\quad B=\dfrac{\pi}{6}. \\[14pt]
(5)\quad & A+B+C=\pi \\[8pt]
\qquad\ \qquad\ &  \dfrac{\pi}{6}+\dfrac{\pi}{6}+C=\pi \\[8pt]
& \Rightarrow (6)\quad C=\dfrac{\pi}{3}. \\[18pt]
(7)\quad & \dfrac{1}{\sin(30^\circ)}=\dfrac{c}{\sin(C)} \\[8pt]
\qquad\ \qquad\ &  \dfrac{1}{\sin(30^\circ)}=\dfrac{c}{\dfrac{\sqrt{3}}{2}} \\[8pt]
& \Rightarrow (8)\quad c=\dfrac{1}{\dfrac{1}{2}}\cdot \dfrac{\sqrt{3}}{2} \\[8pt]
& \qquad\ \qquad\ =\sqrt{3}. \\[22pt]
\textbf{Case II: $B$ is obtuse} \\[10pt]
(9)\quad & \sin(\pi-B)=\sin(B) \qquad (\text{sub. from (4)}) \\[8pt]
\qquad\ \qquad\ & \sin(\pi-B)=\dfrac{1}{2} \\[12pt]
& \Rightarrow (10)\quad \pi-B=\dfrac{\pi}{6} \\[8pt]
& \qquad\ \Rightarrow (11)\quad B=\dfrac{5\pi}{6}. \\[16pt]
(12)\quad & A+B+C=\dfrac{\pi}{6}+\dfrac{5\pi}{6}+C \\[8pt]
& \qquad\ \qquad\ \pi=\pi+C \\[8pt]
& \qquad\ \qquad\ C=0. \\[10pt]
& \therefore\ \text{Case II is impossible for a triangle.}
\end{aligned}
$$
## 3.
**Statement**: $$
A=30^\circ,\quad a=1,\quad b=\sqrt{3}.
$$
(Two triangles from two possible ones)
**Solution**:
$$
\begin{aligned}
A=30^\circ,\ a=1,\ b=\sqrt{3}. \\[14pt]
(1)\quad & \dfrac{b}{\sin(B)}=\dfrac{a}{\sin(A)} \\[10pt]
\qquad\ \qquad\ & \dfrac{\sqrt{3}}{\sin(B)}=\dfrac{1}{\sin(30^\circ)} \\[8pt]
\qquad\ \qquad\ & \dfrac{\sqrt{3}}{\sin(B)}=\dfrac{1}{\dfrac{1}{2}} \\[12pt]
& \Rightarrow (2)\quad \sin(B)=\dfrac{\sqrt{3}}{2}. \\[18pt]
\textbf{Case I: $B$ is acute} \\[10pt]
& \text{From (2):} \\[8pt]
(3)\quad & \sin(B)=\dfrac{\sqrt{3}}{2} \\[10pt]
& \Rightarrow (4)\quad B=\dfrac{\pi}{3}. \\[14pt]
(5)\quad & A+B+C=\pi \\[8pt]
\qquad\ \qquad\ & \dfrac{\pi}{6}+\dfrac{\pi}{3}+C=\pi \\[10pt]
& \Rightarrow (6)\quad C=\dfrac{\pi}{2}. \\[18pt]
(7)\quad & \dfrac{c}{\sin(C)}=\dfrac{a}{\sin(A)} \\[8pt]
\qquad\ \qquad\ & \dfrac{c}{\sin\!\left(\dfrac{\pi}{2}\right)}=\dfrac{1}{\dfrac{1}{2}} \\[10pt]
\qquad\ \qquad\ & c=2. \\[22pt]
\textbf{Case II: $B$ is obtuse} \\[10pt]
& \text{From (2):} \\[8pt]
(8)\quad & \sin(B)=\dfrac{\sqrt{3}}{2} \\[10pt]
& \Rightarrow (9)\quad B=\dfrac{2\pi}{3}. \\[14pt]
(10)\quad & A+B+C=\pi \\[8pt]
\qquad\ \qquad\ & \dfrac{\pi}{6}+\dfrac{2\pi}{3}+C=\pi \\[10pt]
& \Rightarrow (11)\quad C=\dfrac{\pi}{6}. \\[16pt]
(12)\quad & \dfrac{c}{\sin(C)}=\dfrac{a}{\sin(A)} \\[8pt]
\qquad\ \qquad\ & \dfrac{c}{\sin\!\left(\dfrac{\pi}{6}\right)}=\dfrac{1}{\dfrac{1}{2}} \\[10pt]
\qquad\ \qquad\ & c=1.
\end{aligned}
$$

## 4.
**Statement**: $$
A=30^\circ,\quad a=\frac{1}{2},\quad b=2.
$$
**Solution**:
$$
\begin{aligned}
A=30^\circ,\ a=\dfrac{1}{2},\ b=2. \\[14pt]
(1)\quad & \dfrac{b}{\sin(B)}=\dfrac{a}{\sin(A)} \\[10pt]
\qquad\ \qquad\ & \dfrac{2}{\sin(B)}=\dfrac{\dfrac{1}{2}}{\dfrac{1}{2}} \\[12pt]
& \Rightarrow (2)\quad \sin(B)=2. \\[18pt]
\textbf{Case I: $B$ is acute} \\[10pt]
(3)\quad & \sin(B)=2. \\[12pt]
& \therefore\ \textbf{Case I (acute) and Case II (obtuse) are impossible.}
\end{aligned}
$$


