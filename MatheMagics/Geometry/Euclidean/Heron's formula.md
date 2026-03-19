---
down:
tags:
  - mathemagics/geometry/euclidean
---

$$
\begin{aligned}
(1)\quad & \mathcal{A}=\dfrac{1}{2}\,ab\,\sin(C). \\[12pt]
& \Rightarrow (2)\quad \mathcal{A}^2=\dfrac{(ab)^2\sin^2(C)}{4} \\[10pt]
& \qquad\ \qquad\ \ \ =\dfrac{(ab)^2\big(1-\cos^2(C)\big)}{4} \\[10pt]
& \qquad\ \qquad\ \ \ =\dfrac{(ab)^2\big(1-\cos(C)\big)\big(1+\cos(C)\big)}{4}. \\[18pt]
& \text{From law of cosines:} \\[10pt]
(3)\quad & c^2=a^2+b^2-2ab\cos(C). \\[10pt]
& \Rightarrow (4)\quad \cos(C)=\dfrac{a^2+b^2-c^2}{2ab}. \\[18pt]
&\text{From (4), eqs. (5), (6) follow:} \\[10pt]
(5)\quad & \cos(C)+1=\dfrac{a^2+b^2-c^2}{2ab}+1 \\[10pt]
& \qquad\ \qquad\  =\dfrac{a^2+b^2-c^2+2ab}{2ab} \\[10pt]
& \qquad\ \qquad\  =\dfrac{(a+b)^2-c^2}{2ab} \\[10pt]
& \qquad\ \qquad\  =\dfrac{\big((a+b)-c\big)\big((a+b)+c\big)}{2ab}. \\[18pt]
(6)\quad & \cos(C)-1=\dfrac{a^2+b^2-c^2}{2ab}-1 \\[10pt]
& \qquad\ \qquad\  =\dfrac{a^2+b^2-c^2-2ab}{2ab} \\[10pt]
& \qquad\ \qquad\  =\dfrac{(a-b)^2-c^2}{2ab} \\[10pt]
& \qquad\ \qquad\  =\dfrac{\big((a-b)-c\big)\big((a-b)+c\big)}{2ab}. \\[14pt]
& \Rightarrow (7)\quad 1-\cos(C)=\dfrac{(c+b-a)(c+a-b)}{2ab}. \\[22pt]
& \text{Sub. (5), (7) into (2):} \\[10pt]
(2')\quad & \mathcal{A}^2=\dfrac{(ab)^2\big(1-\cos(C)\big)\big(1+\cos(C)\big)}{4} \\[12pt]
& \quad\  =\dfrac{(ab)^2}{4}\left[\dfrac{(a+b-c)(a+b+c)}{2ab}\cdot \dfrac{(c+b-a)(c+a-b)}{2ab}\right] \\[12pt]
& \quad\  =\dfrac{(ab)^2}{4}\cdot \dfrac{1}{4(ab)^2}\cdot (a+b+c)(a+b-c)(c+a-b)(c-a+b) \\[12pt]
& \quad\  =\dfrac{a+b+c}{2}\cdot \dfrac{a+b-c}{2}\cdot \dfrac{c+a-b}{2}\cdot \dfrac{c-a+b}{2}. \\[22pt]
& \text{Let }(8)\ s:=\dfrac{a+b+c}{2} \qquad (\text{semiperimeter of triangle}). \\[16pt]
& \text{Let's express }\dfrac{a+b+c}{2},\ \dfrac{a+b-c}{2},\ \dfrac{c+a-b}{2},\ \text{and }\dfrac{c-a+b}{2}\text{ in terms of the semiperimeter }s: \\[14pt]
(9)\quad & \dfrac{a+b-c}{2}=\dfrac{a+b+c}{2}-\dfrac{2c}{2} \\[10pt]
& \qquad\ \qquad\  =s-c. \\[16pt]
(10)\quad & \dfrac{c+a-b}{2}=\dfrac{a+b+c}{2}-\dfrac{2b}{2} \\[10pt]
& \qquad\ \qquad\  =s-b. \\[16pt]
(11)\quad & \dfrac{c-a+b}{2}=\dfrac{a+b+c}{2}-\dfrac{2a}{2} \\[10pt]
& \qquad\ \qquad\  =s-a. \\[22pt]
& \text{Sub. eqs. (8), (9), (10), (11) into (2'):} \\[12pt]
(2'')\quad & \mathcal{A}^2=s\cdot(s-a)\cdot(s-b)\cdot(s-c). \\[12pt]
& \Rightarrow (12)\quad \mathcal{A}=\sqrt{s\cdot(s-a)\cdot(s-b)\cdot(s-c)}.
\end{aligned}
$$
