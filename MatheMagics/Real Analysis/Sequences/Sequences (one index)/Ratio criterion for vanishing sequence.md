---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Ratio Criterion for Vanishing Sequence**
> > [!warning]+ **IF**
> > - $\{s_n\}\neq 0,\ \forall n\in\mathbb{N}$,  
> > - $\displaystyle \lim_{n\to\infty}\!\left\{\left|\frac{s_{n+1}}{s_n}\right|\right\}=L<1$,
>
> > [!tip]+ **THEN**
> > $$\displaystyle \lim_{n\to\infty}\{s_n\}=0.$$

## Proof:
$$
\begin{aligned}
(1)\quad 
&\lim_{n\to\infty}\left\{\left|\frac{s_{n+1}}{s_n}\right|\right\}=L
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,\big[\,n\ge N \Rightarrow \left|\ \left|\frac{s_{n+1}}{s_n}\right|-L\ \right|<\varepsilon\,\big]
\end{aligned}
$$

Applying **UI** on $\varepsilon$, with $\varepsilon=\dfrac{1-L}{2}$ as a witness; **EI** on $N$; and **UI** on $n$, sequentially:

$$
\begin{aligned}
(2)\quad 
&n\ge N \Rightarrow \left|\ \left|\frac{s_{n+1}}{s_n}\right|-L\ \right|<\frac{1-L}{2}\\[6pt]
&n\ge N \Rightarrow \frac{L-1}{2}<\left|\frac{s_{n+1}}{s_n}\right|-L<\frac{1-L}{2}\\[6pt]
&n\ge N \Rightarrow \frac{3L-1}{2}<\left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}\\[6pt]
&n\ge N \Rightarrow \frac{3L-1}{2}<\left|\frac{s_{n+1}}{s_n}\right|\ \wedge\ \left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}\\[6pt]
&n\ge N \Rightarrow \left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}\\[6pt]
&n\ge N \Rightarrow 0<\left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}\\[6pt]
&\big[\,n\ge N \Rightarrow 0<\left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}\,\big]\ \Rightarrow\ 0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\end{aligned}
$$


Take eq.\,(2)’s last consequent. An inductive argument [^1] therefore shows that:

$$
\begin{aligned}
(3)\quad 
&0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
0<|s_{N+k}|<\left(\frac{1+L}{2}\right)^{k}\,|s_N|,\ \forall k\in\mathbb{Z}^+\\[6pt]
&0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
\lim_{k\to\infty}0<\lim_{k\to\infty}|s_{N+k}|<\lim_{k\to\infty}\left(\frac{1+L}{2}\right)^{k}\,\lim_{k\to\infty}|s_N|\\[6pt]
&0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
0<\lim_{k\to\infty}|s_{N+k}|<0 \qquad\ \qquad\ \qquad\ \qquad\ \quad \text{(applying the squeeze thm.)}\\[6pt]
&0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
0<\lim_{k\to\infty}|s_{N+k}|<0\ \Rightarrow\ \lim_{k\to\infty}|s_{N+k}|=0\ \quad (\text{iff }\frac{1+L}{2}<1 \Rightarrow L<1)\\[6pt]
&0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
0<\lim_{k\to\infty}|s_{N+k}|<0\ \Rightarrow\ \lim_{k\to\infty}|s_{N+k}|=0\ \Rightarrow\ \lim_{n\to\infty}|s_n|=0,\ L<1
\end{aligned}
$$

$\qquad\ \therefore\ (4)\quad 0<|s_{n+1}|<\dfrac{1+L}{2}\cdot|s_n|\ \Rightarrow\ \lim_{n\to\infty}|s_n|=0,\ L<1$

Sub. eq.,(4) into (2):

$$
\begin{aligned}
(2')\quad 
&n\ge N \Rightarrow 0<\left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}
\ \Rightarrow\ 
0<|s_{n+1}|<\frac{1+L}{2}\cdot|s_n|
\ \Rightarrow\ 
\lim_{n\to\infty}|s_n|=0,\ L<1
\end{aligned}
$$

$$
\begin{aligned}
\therefore\ (5)\quad 
&n\ge N \Rightarrow 0<\left|\frac{s_{n+1}}{s_n}\right|<\frac{1+L}{2}
\ \Rightarrow\ 
\lim_{n\to\infty}|s_n|=0,\ L<1
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, **EG** on $L$, and **UG** on $\varepsilon$:

$$
\begin{aligned}
(5')\quad 
&\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\ \exists L<1\ \big[\,n\ge N \Rightarrow \left|\,\left|\frac{s_{n+1}}{s_n}\right|-L\right|<\varepsilon\,\big]\ \Rightarrow\ \lim_{n\to\infty}|s_n|=0\\[6pt]
&\lim_{n\to\infty}\left\{\left|\frac{s_{n+1}}{s_n}\right|\right\}=L<1
\ \Rightarrow\ 
\lim_{n\to\infty}|s_n|=0
\end{aligned}
$$
---
[^1]: **Proof**:
Take eq.\,(2)’s consequent:

$$
\begin{aligned}
(\mathrm{I})\quad 
&0<|s_{N+1}|<\frac{1+L}{2}\,|s_{N}|
\ \Rightarrow\
0<|s_{(N+k)+1}|<\frac{1+L}{2}\,|s_{(N+k)}|
\end{aligned}
$$

Assume the inductive hypothesis: $0<|s_{N+k}|<\left(\dfrac{1+L}{2}\right)^{k}\,|s_{N}|$

Base $(k=1)$:

$$
\begin{aligned}
(\mathrm{II})\quad 
0<|s_{N+1}|<\left(\frac{1+L}{2}\right)^{1}\,|s_{N}|
\end{aligned}
$$

Step $(k\to k+1)$:

$$
\begin{aligned}
(\mathrm{III})\quad 
&0<|s_{N+k}|<\left(\frac{1+L}{2}\right)^{k}\,|s_{N}|\\[4pt]
&0<\left(\frac{1+L}{2}\right)\!\cdot|s_{N+k}|
<\left(\frac{1+L}{2}\right)\!\cdot\left(\frac{1+L}{2}\right)^{k}\,|s_{N}|\\[4pt]
&0<\left(\frac{1+L}{2}\right)\!\cdot|s_{N+k}|
<\left(\frac{1+L}{2}\right)^{k+1}\,|s_{N}|
\end{aligned}
$$

Substitute eq., $(\mathrm{I})$’s consequent into eq.,$(\mathrm{III})$:

$$
\begin{aligned}
(\mathrm{III'})\quad 
&0<|s_{(N+k)+1}|<\left(\frac{1+L}{2}\right)\!\cdot|s_{N+k}|
<\left(\frac{1+L}{2}\right)^{k+1}\,|s_{N}|\\[4pt]
&0<|s_{N+(k+1)}|<\left(\frac{1+L}{2}\right)^{(k+1)}\,|s_{N}|
\end{aligned}
$$

IH holds for all $k$:

$$
\begin{aligned}
(\mathrm{IV})\quad 
0<|s_{N+k}|<\left(\frac{1+L}{2}\right)^{k}\,|s_{N}|,\ \forall k\in\mathbb{Z}^{+}
\end{aligned}
$$
