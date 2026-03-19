---
down:
tags:
  - mathemagics/geometry/euclidean
---
```columns
id: DR3Ii62Iyj9crHfZ1-Xly
===
![[Pasted image 20260118153147.png|200]]
===
$$
\begin{aligned}
& \mathtt{Preliminaries:}\\[18pt]
& \bullet\ \mathtt{Axis:\ }+\hat y\ \mathtt{upward.}\ \mathtt{Set}\ y(0)=0.\\[12pt]
& \bullet\ \mathtt{Signed\ velocity:\ }v(t)=\dfrac{dy}{dt}.\\[12pt]
& \bullet\ \mathtt{Signed\ accel:\ }a_y(t)=\dfrac{dv}{dt}.\\[18pt]
& \bullet\ \mathtt{Weight:\ }F_g=-mg.\\[18pt]
& \bullet\ \mathtt{Quad.\ drag:\ magnitude}\ k\,v^2,\ \mathtt{opposite\ motion.}\\[12pt]
& \qquad\qquad\qquad\ F_{\mathtt{drag}}=-k\,v\lvert v\rvert.\\[18pt]
& \bullet\ \mathtt{Falling\ phase:\ }y(t)\le 0,\ v(t)\le 0.\\[12pt]
& \qquad\qquad\qquad\ \mathtt{(}y(t)\le 0\mathtt{: below\ release\ point.)}\\[18pt]
& \bullet\ \mathtt{Released\ from\ rest:\ }v(0)=0\ \Rightarrow\ a_y(0)=-g.\\[18pt]
& \bullet\ \mathtt{Terminal\ speed:\ }v_T\\[12pt]
& \qquad\qquad\qquad\ \mathtt{Expect}\ -v_T\le v(t)\le 0,\ a_y(t)\le 0.\\[12pt]
& \qquad\qquad\qquad\ \mathtt{As}\ v(t)\to -v_T,\ \mathtt{then}\ a_y(t)\to 0.
\end{aligned}
$$

```

## Question 1:
Find speed and distance traveled by the previously described falling object after time *t*
$$
\begin{aligned}
(1)\quad & \sum \vec{F}=m\vec{a} \\[18pt]
& \sum F_y=m a_y \qquad (\mathtt{from\ diagram}) \\[12pt]
& \mathtt{Take\ downward\ as\ the\ positive\ direction.} \\[22pt]
& F_g\cdot(+1)+F_{\mathtt{drag}}\cdot(-1)=m\cdot a_y\cdot(-1) \\[12pt]
& k\cdot v^{2}-m g=m\cdot(-a_y) \qquad \Bigl(a_y=\dfrac{dv}{dt}\Bigr) \\[18pt]
& g-\dfrac{k}{m}\cdot v^{2}=\dfrac{dv}{dt} \\[22pt]
& \Rightarrow (2)\quad \dfrac{dv}{g-\dfrac{k}{m}\cdot v^{2}}=dt \\[18pt]
& \qquad\ \quad\ \dfrac{dv}{g\cdot\Bigl(1-\dfrac{k}{mg}\cdot v^{2}\Bigr)}=dt \\[18pt]
& \qquad\ \quad\ \dfrac{dv}{\Bigl(1-\dfrac{k}{mg}\cdot v^{2}\Bigr)}=g\,dt \\[22pt]
(3)\quad & u:=\sqrt{\dfrac{k}{mg}} \\[22pt]
& \mathtt{Sub.\ (3)\ into\ (2):} \\[12pt]
(2')\quad & \dfrac{dv}{1-(u v)^{2}}=g\,dt \\[18pt]
& \int \dfrac{dv}{1-(u v)^{2}}=\int g\,dt \qquad \Bigl(\int \dfrac{dx}{1-x^{2}}=\mathtt{tanh}\,x\Bigr) \\[22pt]
& \mathtt{tanh}^{-1}(u v)\cdot \dfrac{1}{u}=g\cdot t+C_1 \\[18pt]
& \mathtt{tanh}^{-1}(u v)=u\cdot(g\cdot t+C_1) \\[22pt]
& \mathtt{The\ object\ is\ dropped\ from\ rest,\ therefore,}\ (4)\ t=0,\ (5)\ v(0)=0 \\[22pt]
& \mathtt{Sub.\ (4)\ and\ (5)\ into\ (2'):} \\[12pt]
(2'')\quad & \mathtt{tanh}^{-1}\bigl(u\cdot v(0)\bigr)=u\cdot(g\cdot 0+C_1) \\[18pt]
& \mathtt{tanh}^{-1}(0)=u\cdot C_1 \\[18pt]
& 0=u\cdot C_1 \qquad (\mathtt{Assumption\ }\forall t\ (u\neq 0)) \\[18pt]
& \Rightarrow (6)\quad C_1=0 \\[22pt]
& \mathtt{Sub.\ (6)\ into\ (2'):} \\[12pt]
(2''')\quad & \mathtt{tanh}^{-1}(u v)=u g t \qquad (\mathtt{solving\ for\ }v) \\[18pt]
& \Rightarrow (7)\quad v=\dfrac{1}{u}\cdot \mathtt{tanh}(u g t) \qquad (v=y') \\[18pt]
& \qquad\ \quad\ \dfrac{dy}{dt}=\dfrac{1}{u}\cdot \mathtt{tanh}(u g t) \\[22pt]
& \qquad\ \quad\ \Rightarrow (8)\quad dy=\dfrac{1}{u}\cdot \mathtt{tanh}(u g t)\,dt \\[18pt]
& \qquad\ \qquad\ \qquad\ \int dy=\int \dfrac{1}{u}\cdot \mathtt{tanh}(u g t)\,dt \\[22pt]
& \qquad\ \qquad\ \qquad\ y=\dfrac{1}{u}\cdot \mathtt{ln}\Bigl((\mathtt{sec}(u g t))^{-1}\Bigr)\cdot \dfrac{1}{u g}+C_2 \\[18pt]
& \qquad\ \qquad\ \qquad\ y=\dfrac{1}{u^{2}\cdot g}\cdot \mathtt{ln}\Bigl((\mathtt{sec}(u g t))^{-1}\Bigr)+C_2 \\[22pt]
(9)\quad & y(0)=0 \qquad (\mathtt{From\ preliminaries,\ and\ sub.\ from\ (8)}) \\[18pt]
& \dfrac{1}{u^{2}\cdot g}\cdot \mathtt{ln}\Bigl((\mathtt{sech}(u g\cdot 0))^{-1}\Bigr)+C_2=0 \\[18pt]
& \dfrac{1}{u^{2}\cdot g}\cdot \mathtt{ln}(1)+C_2=0 \\[18pt]
& \Rightarrow (10)\quad C_2=0 \\[22pt]
& \mathtt{Sub.\ (10)\ into\ (8):} \\[12pt]
(8')\quad & y=\dfrac{1}{u^{2}\cdot g}\cdot \mathtt{ln}\Bigl((\mathtt{sec}(u g t))^{-1}\Bigr) \qquad (\mathtt{sub.\ back\ from\ (3)}) \\[18pt]
& y=\dfrac{m}{k}\cdot \mathtt{ln}\Bigl(\mathtt{cosh}\bigl(\sqrt{\dfrac{k g}{m}}\cdot t\bigr)\Bigr)
\end{aligned}
$$
## Question 2:
Find the formula for the terminal velocity
### Interpretation 1:
$$
\begin{aligned}
& \mathtt{From\ eq.\ (7)\ in\ question\ one:} \\[22pt]
(1)\quad & v=\dfrac{1}{u}\cdot \mathtt{tanh}(u g t) \qquad \Bigl(u:=\sqrt{\dfrac{k}{m g}}\Bigr) \\[22pt]
& v=\sqrt{\dfrac{m g}{k}}\cdot \mathtt{tanh}\Bigl(\sqrt{\dfrac{k}{m g}}\cdot g\cdot t\Bigr) \\[22pt]
& v=\sqrt{\dfrac{m g}{k}}\cdot \mathtt{tanh}\Bigl(\sqrt{\dfrac{k g}{m}}\cdot t\Bigr) \\[22pt]
& \mathtt{Terminal\ velocity:} \\[18pt]
(2)\quad & v_T=\lim_{t\to\infty} v(t) \\[22pt]
& v_T=\lim_{t\to\infty}\sqrt{\dfrac{m g}{k}}\cdot \mathtt{tanh}\Bigl(\sqrt{\dfrac{k g}{m}}\cdot t\Bigr) \\[22pt]
& v_T=\sqrt{\dfrac{m g}{k}}\cdot \lim_{t\to\infty}\mathtt{tanh}\Bigl(\sqrt{\dfrac{k g}{m}}\cdot t\Bigr) \\[22pt]
& v_T=\sqrt{\dfrac{m g}{k}} \qquad (\mathtt{for\ }k,m,g>0)
\end{aligned}
$$
### Interpretation 2: 
$$ \sum \vec{F}=m\vec{0} $$
## Question 3:
Time at which it would take the object to reach terminal velocity