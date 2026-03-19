---
down:
tags:
  - mathemagics/real_analysis
---
## Catalog:
$$
\begin{aligned}
1.\quad & \sum_{n=1}^{\infty}\frac{1}{\,n+3^{n}\,} \\[4pt]
2.\quad & \sum_{n=1}^{\infty}\frac{(2n+1)^{n}}{n^{2n}} \\[4pt]
3.\quad & \sum_{n=1}^{\infty}(-1)^{n}\,\frac{n}{n+2} \\[4pt]
4.\quad & \sum_{n=1}^{\infty}(-1)^{n}\,\frac{n}{n^{2}+2} \\[4pt]
5.\quad & \sum_{n=1}^{\infty}\frac{n^{2}\,2^{\,n-1}}{(-5)^{n}} \\[4pt]
6.\quad & \sum_{n=1}^{\infty}\frac{1}{2n+1} \\[4pt]
7.\quad & \sum_{n=2}^{\infty}\frac{1}{n\sqrt{\ln n}} \\[4pt]
8.\quad & \sum_{k=1}^{\infty}\frac{2^{k}\,k!}{(k+2)!} \\[4pt]
9.\quad & \sum_{k=1}^{\infty}k^{2}e^{-k} \\[4pt]
10.\quad & \sum_{n=1}^{\infty}n^{2}e^{-n^{3}} \\[6pt]
11.\quad & \sum_{n=1}^{\infty}\!\left(\frac{1}{n^{3}}+\frac{1}{3^{n}}\right) \\[4pt]
12.\quad & \sum_{k=1}^{\infty}\frac{1}{k\sqrt{k^{2}+1}} \\[4pt]
13.\quad & \sum_{n=1}^{\infty}\frac{3^{n}n^{2}}{n!} \\[4pt]
14.\quad & \sum_{n=1}^{\infty}\frac{\sin(2n)}{1+2^{n}} \\[4pt]
15.\quad & \sum_{k=1}^{\infty}\frac{2^{\,k-1}\,3^{\,k+1}}{k^{k}} \\[4pt]
16.\quad & \sum_{n=1}^{\infty}\frac{n^{2}+1}{n^{3}+1} \\[4pt]
17.\quad & \sum_{n=1}^{\infty}\frac{1\cdot 3\cdot 5\cdots(2n-1)}{2\cdot 5\cdot 8\cdots(3n-1)} \\[4pt]
18.\quad & \sum_{n=2}^{\infty}\frac{(-1)^{n-1}}{\sqrt{n}-1} \\[6pt]
19.\quad & \sum_{n=1}^{\infty}(-1)^{n}\,\frac{\ln n}{\sqrt{n}} \\[4pt]
20.\quad & \sum_{k=1}^{\infty}\frac{\sqrt[3]{k}-1}{k(\sqrt{k}+1)} \\[4pt]
21.\quad & \sum_{n=1}^{\infty}(-1)^{n}\cos\!\left(\frac{1}{n^{2}}\right) \\[4pt]
22.\quad & \sum_{k=1}^{\infty}\frac{1}{2+\sin k} \\[4pt]
23.\quad & \sum_{n=1}^{\infty}\tan\!\left(\frac{1}{n}\right) \\[4pt]
24.\quad & \sum_{n=1}^{\infty} n\,\sin\!\left(\frac{1}{n}\right) \\[4pt]
25.\quad & \sum_{n=1}^{\infty}\frac{n!}{e^{n^{2}}} \\[4pt]
26.\quad & \sum_{n=1}^{\infty}\frac{n^{2}+1}{5^{n}} \\[4pt]
27.\quad & \sum_{k=1}^{\infty}\frac{k\ln k}{(k+1)^{3}} \\[4pt]
28.\quad & \sum_{n=1}^{\infty}\frac{e^{1/n}}{n^{2}} \\[6pt]
29.\quad & \sum_{n=1}^{\infty}\frac{(-1)^{n}}{\cosh n} \\[4pt]
30.\quad & \sum_{j=1}^{\infty}(-1)^{j}\,\frac{\sqrt{j}}{j+5} \\[4pt]
31.\quad & \sum_{k=1}^{\infty}\frac{5^{k}}{3^{k}+4^{k}} \\[4pt]
32.\quad & \sum_{n=1}^{\infty}\frac{(n!)^{n}}{n^{4n}} \\[4pt]
33.\quad & \sum_{n=1}^{\infty}\left(\frac{n}{n+1}\right)^{n^{2}} \\[4pt]
34.\quad & \sum_{n=1}^{\infty}\frac{1}{\,n+n\cos^{2}n\,} \\[4pt]
35.\quad & \sum_{n=1}^{\infty}\frac{1}{n^{\,1+1/n}} \\[4pt]
36.\quad & \sum_{n=2}^{\infty}\frac{1}{(\ln n)^{\ln n}} \\[4pt]
37.\quad & \sum_{n=1}^{\infty}\big(\sqrt[n]{2}-1\big)^{n} \\[4pt]
38.\quad & \sum_{n=1}^{\infty}\big(\sqrt[n]{2}-1\big)
\end{aligned}
$$
## Solutions: 
### Exercise 1:

$$
\begin{aligned}
(1)\quad 
& S^{(1)} := \sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty}\frac{1}{\,n+3^{n}\,}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& S^{(2)} := \sum_{n=1}^{\infty} t_n
=\sum_{n=1}^{\infty}\left(\frac{1}{3}\right)^{\!n}
=\sum_{n=1}^{\infty} r^{\,n}.
\end{aligned}
$$

Eq. (2) is a convergent geometric series ($|r|<1$).

$$s_n \le t_n: \dfrac{1}{\,n+3^{n}\,} \le \left(\dfrac{1}{3}\right)^{n}
\Longleftrightarrow 3^{n} \le n+3^{n}$$
Since $n\ge 0$ and $n\in\mathbb{N}$, the inequality holds.  
$\therefore\ \forall n\in\mathbb{N}\,[\,s_n\le t_n\,]$.

$$
\text{Eq. (1)}\quad \xRightarrow[\ \text{By comparison test}\ ]{}\quad
S^{(1)}\ \text{converges.}
$$

---

### Exercise 2:

$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty}\left(\frac{(2n+1)^{n}}{n^{2n}}\right)
=\sum_{n=1}^{\infty}\left(\frac{2n+1}{n^{2}}\right)^{\!n}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& \lim_{n\to\infty}\sqrt[n]{\lvert s_n\rvert}
=\lim_{n\to\infty}\sqrt[n]{\left\lvert\left(\frac{2n+1}{n^{2}}\right)^{\!n}\right\rvert}
=\lim_{n\to\infty}\left\lvert\frac{2n+1}{n^{2}}\right\rvert
\\
&=\lim_{n\to\infty}\frac{2n+1}{n^{2}}
\ \overset{\text{L'H}}{=}\ \lim_{n\to\infty}\frac{2}{2n}=0.
\end{aligned}
$$

$$
\text{Eq. (2)}\quad \xRightarrow[\ \text{By Root test}\ ]{}\quad
S\ \text{is convergent.}
$$
### Exercise 3:

$$
\begin{aligned}
(1)\quad 
& S:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty}(-1)^{n}\,\frac{n}{n+2}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& \lim_{n\to\infty} s_n
=\lim_{n\to\infty}(-1)^{n}\,\frac{n}{n+2}
\ \text{ does not exist (DNE).}
\end{aligned}
$$

By the **divergence test**, from eq. (2) the series in eq. (1) **diverges**.

---

### Exercise 4:

$$
\begin{aligned}
(1)\quad 
& S:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty}(-1)^{n}\,t_n
=\sum_{n=1}^{\infty}(-1)^{n}\,\frac{n}{n^{2}+2}.
\end{aligned}
$$

$$
(2)\quad \forall n\in\mathbb{N}\ \ [\ t_n\ge 0\ ].
$$

Decreasing tails:

$$
\begin{aligned}
(3)\quad 
& t_{n+1}\le t_n
\ \Longleftrightarrow\ 
\frac{n+1}{(n+1)^{2}+2}\ \le\ \frac{n}{n^{2}+2}
\\[6pt]
& \qquad\ \qquad \Longleftrightarrow\ (n+1)(n^{2}+2)\ \le\ n\big((n+1)^{2}+2\big)
\\[6pt]
& \qquad\ \qquad \Longleftrightarrow\ n^{3}+2n+n^{2}+2\ \le\ n^{3}+2n^{2}+3n
\\[6pt]
& \qquad\ \qquad \Longleftrightarrow\ n^{2}+n-2\ \ge\ 0
\\[6pt]
& \qquad\ \qquad \Longleftrightarrow\ (n+2)(n-1)\ \ge\ 0,\qquad n\in\mathbb{N}.
\end{aligned}
$$

Limit of terms:

$$
\begin{aligned}
(5)\quad 
& \lim_{n\to\infty} t_n
=\lim_{n\to\infty}\frac{n}{n^{2}+2}
\overset{\text{L'H}}{=}\lim_{n\to\infty}\frac{1}{2n}=0.
\end{aligned}
$$

From eqs. (2), (3), and (5), **by the alternating series test**, the series in eq. (1) **converges**.

### Exercise 5:

$$
\begin{aligned}
(1)\quad 
& S=\sum_{n=1}^{\infty}s_n
=\sum_{n=1}^{\infty}\frac{n^{2}\,2^{\,n-1}}{(-5)^{n}}
=\sum_{n=1}^{\infty}(-1)^{n}\,n^{2}\cdot\frac{1}{2}\left(\frac{2}{5}\right)^{\!n}.
\end{aligned}
$$

Ratio test:

$$
\begin{aligned}
(2)\quad 
& L:=\lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
=\lim_{n\to\infty}\left|
\frac{(n+1)^{2}\cdot \frac{1}{2}\left(\frac{2}{5}\right)^{n+1}}
{n^{2}\cdot \frac{1}{2}\left(\frac{2}{5}\right)^{n}}
\right|
=\lim_{n\to\infty}\left(\frac{2}{5}\right)\frac{(n+1)^{2}}{n^{2}}
=\frac{2}{5}<1.
\end{aligned}
$$

From eq. (2) (ratio test) $\Rightarrow\ S$ **converges**.

---

### Exercise 6:

$$
\begin{aligned}
(1)\quad 
& S^{(1)}:=\sum_{n=1}^{\infty}s_n
=\sum_{n=1}^{\infty}\frac{1}{2n+1}.
\end{aligned}
$$

Compare with the divergent $p$-series:

$$
\begin{aligned}
(2)\quad 
& S^{(2)}:=\sum_{n=1}^{\infty}t_n
=\sum_{n=1}^{\infty}\frac{1}{n}
\qquad(\text{harmonic series, divergent}).
\end{aligned}
$$

Limit comparison:

$$
\begin{aligned}
(3)\quad 
& \lim_{n\to\infty}\frac{s_n}{t_n}
=\lim_{n\to\infty}\frac{\frac{1}{2n+1}}{\frac{1}{n}}
=\lim_{n\to\infty}\frac{n}{2n+1}
=\frac{1}{2}>0.
\end{aligned}
$$

From eq. (3) (limit comparison with a divergent series) $\Rightarrow\ S^{(1)}$ **diverges**.

### Exercise 7:

$$
\begin{aligned}
(1)\quad 
& S=\sum_{n=2}^{\infty} s_n
=\sum_{n=2}^{\infty}\frac{1}{\,n\sqrt{\ln(n)}\,}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& f(x)=\frac{1}{\,x\sqrt{\ln(x)}\,}.
\end{aligned}
$$

$f(x)$ is positive, continuous, and decreasing on $[2,\infty)$, so the **integral test** applies.

$$
\begin{aligned}
(3)\quad 
& \lim_{t\to\infty}\int_{2}^{t}\frac{dx}{x\sqrt{\ln(x)}} 
\quad\Big[\ u=\ln(x),\ \ du=\frac{dx}{x}\ \Big]
\\[6pt]
&=\lim_{t\to\infty}\int_{\ln 2}^{\ln t} u^{-1/2}\,du
\\[6pt]
&=\lim_{t\to\infty}\Big[\,2\,u^{1/2}\,\Big]_{\,u=\ln 2}^{\,u=\ln t}
\\[6pt]
&=\lim_{t\to\infty}\Big[\,2\sqrt{\ln(x)}\,\Big]_{2}^{t}
=2\Big(\lim_{t\to\infty}\sqrt{\ln(t)}-\sqrt{\ln(2)}\Big)
=\infty.
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
& \therefore\ \lim_{t\to\infty}\int_{2}^{t}\frac{dx}{x\sqrt{\ln(x)}}=\infty
\ \ \xRightarrow{\ \text{by integral test}\ }\ 
S\ \text{diverges}.
\end{aligned}
$$
### Exercise 8:

$$
\begin{aligned}
(1)\quad 
& S:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty}\frac{2^{\,n}\,n!}{(n+2)!}.
\end{aligned}
$$

Ratio test:

$$
\begin{aligned}
(2)\quad 
& L:=\lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
=\lim_{n\to\infty}
\left|
\frac{2^{\,n+1}(n+1)!/(n+3)!}{2^{\,n}n!/(n+2)!}
\right|
=\lim_{n\to\infty}\frac{2(n+1)}{n+3}
=2\ (>1).
\end{aligned}
$$

From eq. (2) (ratio test) $\Rightarrow\ S$ **diverges**.  
*(Alternatively, $s_n=\dfrac{2^{\,n}}{(n+2)(n+1)}\not\to 0$, so the divergence test also applies.)*

---

### Exercise 9:

$$
\begin{aligned}
(1)\quad 
& S:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty} n^{2}e^{-n}.
\end{aligned}
$$

Ratio test:

$$
\begin{aligned}
(2)\quad 
& L:=\lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
=\lim_{n\to\infty}\frac{(n+1)^{2}e^{-(n+1)}}{n^{2}e^{-n}}
=\lim_{n\to\infty}\frac{(n+1)^{2}}{e\,n^{2}}
=\frac{1}{e}\ (<1).
\end{aligned}
$$

From eq. (2) (ratio test) $\Rightarrow\ S$ **converges**.
### Exercise 10:

$$
\begin{aligned}
(1)\quad 
& S:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty} n^{2}e^{-n^{3}}.
\end{aligned}
$$

$$
\begin{aligned}
(2)\quad 
& f(x)=\frac{x^{2}}{e^{x^{3}}}.
\end{aligned}
$$

$f(x)$ is positive, continuous, and decreasing on $[1,\infty)$, so the **integral test** applies.

$$
\begin{aligned}
(3)\quad 
& \lim_{t\to\infty}\int_{1}^{t}\frac{x^{2}}{e^{x^{3}}}\,dx
\qquad\Big[\,u=x^{3},\ \ du=3x^{2}dx\ \Rightarrow\ x^{2}dx=\frac{du}{3}\,\Big]
\\[6pt]
&=\lim_{t\to\infty}\int_{u=1}^{u=t^{3}}\frac{e^{-u}}{3}\,du
=\lim_{t\to\infty}\Big[-\frac{e^{-u}}{3}\Big]_{u=1}^{u=t^{3}}
\\[6pt]
&=\lim_{t\to\infty}\left(\frac{1}{3e}-\frac{e^{-t^{3}}}{3}\right)
=\frac{1}{3e}.
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
& \therefore\ \lim_{t\to\infty}\int_{1}^{t}\frac{x^{2}}{e^{x^{3}}}\,dx\ \text{converges}
\ \xRightarrow{\ \text{by integral test}\ }\ 
S\ \text{converges}.
\end{aligned}
$$

### Exercise 11:

$$
\begin{aligned}
(1)\quad 
& S^{(1)}:=\sum_{n=1}^{\infty} s_n
=\sum_{n=1}^{\infty}\!\left(\frac{1}{n^{3}}+\frac{1}{3^{n}}\right).
\end{aligned}
$$

Conclude by splitting into two standard convergent series:

$$
\begin{aligned}
(2)\quad 
& S^{(2)}:= \sum_{n=1}^{\infty}\frac{1}{n^{3}} \ \text{converges (}p\text{-series with }p=3>1\text{),}
\\[4pt]
(3) \quad & S^{(3)}:=  \sum_{n=1}^{\infty}\frac{1}{3^{n}} \ \text{converges (geometric, }r=\tfrac13<1\text{).}
\end{aligned}
$$

Therefore,
$$
S^{(1)}=\sum_{n=1}^{\infty}\!\left(\frac{1}{n^{3}}+\frac{1}{3^{n}}\right)
=\sum_{n=1}^{\infty}\frac{1}{n^{3}}
\;+\;
\sum_{n=1}^{\infty}\frac{1}{3^{n}} = S^{(2)} + S^{(3)}
\quad\Longrightarrow\quad
S^{(1)}\ \text{converges.}
$$

### Exercise 12

$$
\begin{aligned}
& (1)\;\; S^{(1)} \;:=\; \sum_{n=1}^{\infty} s_n \;=\; \sum_{n=1}^{\infty} \frac{1}{\,n\sqrt{n^{2}+1}\,} \\[10pt]

& (2)\;\; S^{(2)} \;:=\; \sum_{n=1}^{\infty} t_n \;=\; \sum_{n=1}^{\infty} \frac{1}{n^{2}}
\qquad (\text{$p$-series with } p=2,\ \text{convergent}) \\[12pt]

& (3)\;\; s_n \;\le\; t_n
\quad\Longleftrightarrow\quad
\frac{1}{n\sqrt{n^{2}+1}} \;\le\; \frac{1}{n^{2}}
\quad\Longleftrightarrow\quad
n^{2} \;\le\; n\sqrt{n^{2}+1} \\[6pt]
& \qquad\Longleftrightarrow\quad
n^{4} \;\le\; n^{2}(n^{2}+1)
\quad\Longleftrightarrow\quad
n^{4} \;\le\; n^{4}+n^{2}
\quad\Longleftrightarrow\quad
0 \;\le\; n^{2} \\[10pt]

& \therefore \quad (4)\;\; \forall n\in\mathbb{N}\;[\,s_n \le t_n\,].
\end{aligned}
$$

$$
\text{Eq.\ (4) + convergence of } S^{(2)}
\;\Longrightarrow\;
S^{(1)} \text{ convergent} \quad (\text{comparison test}).
$$

### Exercise 13

$$
\begin{aligned}
& (1)\;\; S \;:=\; \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} \frac{3^{\,n} n^{2}}{n!} \\[12pt]
& (2)\;\; L \;:=\; \lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
   \;=\; \lim_{n\to\infty}\left|\frac{\;\dfrac{3^{\,n+1}(n+1)^{2}}{(n+1)!}\;}{\;\dfrac{3^{\,n}n^{2}}{n!}\;}\right| \\[4pt]
& \qquad\qquad\qquad\qquad\qquad\quad
   =\; \lim_{n\to\infty}\left|\frac{3^{\,n}\cdot 3\cdot (n+1)^{2}\cdot n!}{(n+1)\cdot n!\cdot 3^{\,n}\cdot n^{2}}\right| \\[4pt]
& \qquad\qquad\qquad\qquad\qquad\quad
   =\; \lim_{n\to\infty}\left|\frac{3\,(n+1)^{2}}{(n+1)\,n^{2}}\right|
   =\; \lim_{n\to\infty}\left|\frac{3\,(n+1)}{n^{2}}\right|
   =\; 0\ (<1)
\end{aligned}
$$

$$
\begin{aligned}
(4)\quad 
& \therefore\ L=\lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|=0<1
\ \xRightarrow{\ \text{by ratio test}\ }\ 
S\ \text{converges}.
\end{aligned}
$$


### Exercise 14

$$
\begin{aligned}
& (1)\;\; S^{(1)} \;:=\; \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} \frac{\sin(2n)}{1+2^{\,n}} \\[12pt]
& (2)\;\; S^{(2)} \;:=\; \sum_{n=1}^{\infty} t_n 
   \;=\; \sum_{n=1}^{\infty} \!\left(\frac{1}{2}\right)^{\!n}
   \;=\; \sum_{n=1}^{\infty} r^{\,n}
   \qquad (\,|r|<1 \Rightarrow \text{ geometric, convergent}\,) \\[12pt]
& (3)\;\; \sin(2n)\ \le\ 1\ \le\ 1+\frac{1}{2^{\,n}}
   \;=\; \frac{2^{\,n}+1}{2^{\,n}} \\[4pt]
& \Rightarrow\ \ \sin(2n)\ \le\ \frac{2^{\,n}+1}{2^{\,n}}\\[4pt]
& \Rightarrow\ \ \frac{\sin(2n)}{1+2^{\,n}}\ \le\ \frac{1}{2^{\,n}}\\[4pt]
& \Rightarrow\ \ s_n \ \le\ t_n \\[12pt]
\end{aligned}
$$
Eq.(3) $\Rightarrow$ $S^{(1)}$ is **convergent**
### Exercise 15:

$$
\begin{aligned}
\textbf{(1)}\quad 
& S^{(1)} := \sum_{n=1}^{\infty} s_n 
\;=\; \sum_{n=1}^{\infty} \frac{2^{\,n-1}\,3^{\,n+1}}{n^{\,n}} \\[6pt]
& \qquad\;\; = \sum_{n=1}^{\infty} \frac{3}{2}\,\left(\frac{2\cdot 3}{n}\right)^{\!n}
\;=\; \frac{3}{2}\,\sum_{n=1}^{\infty} \left(\frac{6}{n}\right)^{\!n} \\[4pt]
& \qquad\;\; = \frac{3}{2}\,\sum_{n=1}^{\infty} t_n
\;=\; \frac{3}{2}\,S^{(2)} .
\end{aligned}
$$

$$
\begin{aligned}
\textbf{(2)}\quad 
& L \;:=\; \lim_{n\to\infty} \sqrt[n]{\,|t_n|\,}
\;=\; \lim_{n\to\infty} \sqrt[n]{\left|\left(\frac{6}{n}\right)^{\!n}\right|}
\;=\; \lim_{n\to\infty} \left|\frac{6}{n}\right|
\;=\; 0 \;(<1). \\[8pt]
& \text{Eq.\,(2)}\ \Rightarrow\ S^{(2)}\ \text{converges\ (by Root test).} \\[8pt]
& S^{(2)}\ \text{converges}\ \Rightarrow\ \frac{3}{2}\,S^{(2)} \;=\; S^{(1)}\ \text{converges.}
\end{aligned}
$$
### Exercise 16:

$$
\begin{aligned}
\textbf{(1)}\quad 
& S^{(1)} := \sum_{n=1}^{\infty} s_n 
\;=\; \sum_{n=1}^{\infty} \frac{n^{2}+1}{\,n^{3}+1\,}. \\[10pt]

\textbf{(2)}\quad 
& S^{(2)} := \sum_{n=1}^{\infty} t_n 
\;=\; \sum_{n=1}^{\infty} \frac{1}{n}
\qquad\text{(divergent $p$–series).} \\[10pt]

\textbf{(3)}\quad 
& n\ge 1 
\ \Rightarrow\ 
n^{3}+n \;\ge\; n^{3}+1
\ \Rightarrow\ 
n(n^{2}+1) \;\ge\; n^{3}+1 \\[3pt]
& \Rightarrow\ 
\frac{n^{2}+1}{n^{3}+1} \;\ge\; \frac{1}{n}
\qquad\Rightarrow\qquad s_n \;\ge\; t_n. \\[12pt]

\textbf{(4)}\quad 
& \therefore\ s_n\ge t_n\ \text{for all }n\ \text{and}\ \sum_{n=1}^{\infty} t_n\ \text{diverges}
\ \xRightarrow{\ \text{by comparison test}\ }\ 
S^{(1)}\ \text{diverges}.
\end{aligned}
$$
### Exercise 17:

$$
\begin{aligned}
\textbf{(1)}\quad 
& S := \sum_{n=1}^{\infty} s_n,\qquad 
s_n := \frac{1\cdot 3 \cdot 5 \cdots (2n-1)}{2\cdot 5 \cdot 8 \cdots (3n-1)}. \\[12pt]
\textbf{(2)}\quad 
& L := \lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
= \lim_{n\to\infty}
\left|
\frac{1\cdot 3\cdot 5\cdots(2n-1)\,\,(2n+1)}
     {2\cdot 5\cdot 8\cdots(3n-1)\,\,(3n+2)}
\cdot
\frac{2\cdot 5\cdot 8\cdots(3n-1)}
     {1\cdot 3\cdot 5\cdots(2n-1)}
\right| \\[6pt]
& \qquad = \lim_{n\to\infty} \frac{2n+1}{3n+2}
= \frac{2}{3}\ (<1). \\[12pt]
\textbf{(3)}\quad 
& \therefore\ L<1\ \xRightarrow{\ \text{by ratio test}\ }\ S\ \text{converges}.
\end{aligned}
$$
### Exercise 18:

$$
\begin{aligned}
(1)\quad 
& S \;:=\; \sum_{n=1}^{\infty} s_n 
 \;=\; \sum_{n=2}^{\infty} \frac{(-1)^{\,n-1}}{\sqrt{n}-1}
 \;=\; \sum_{n=1}^{\infty} (-1)^{\,n-1}\, t_n,
\end{aligned}
$$

where (for $n\ge 2$) $t_n := \dfrac{1}{\sqrt{n}-1}$.

$$
\begin{aligned}
(2)\quad 
& \sqrt{n}\ \le\ \sqrt{n+1}
\quad\Rightarrow\quad
\sqrt{n}-1\ \le\ \sqrt{n+1}-1 \\[4pt]
& \Rightarrow\quad
\frac{1}{\sqrt{n+1}-1}\ \le\ \frac{1}{\sqrt{n}-1}
\quad\Rightarrow\quad
t_{n+1}\ \le\ t_n \qquad (n\ge 2).
\end{aligned}
$$

$$
\begin{aligned}
(3)\quad 
& \lim_{n\to\infty} t_n
 \;=\; \lim_{n\to\infty} \frac{1}{\sqrt{n}-1}
 \;=\; 0.
\end{aligned}
$$

$$
\therefore\ t_{n+1}\le t_n\ \text{ and }\ \lim_{n\to\infty} t_n=0
\ \xRightarrow{\ \text{by alternating series test}\ }\ 
S\ \text{converges}.
$$
### Exercise 19:

$$
\begin{aligned}
(1)\quad 
& S \;:=\; \sum_{n=1}^{\infty} s_n 
 \;=\; \sum_{n=1}^{\infty} (-1)^n\,\frac{\ln n}{\sqrt{n}}
 \;=\; \sum_{n=1}^{\infty} (-1)^{\,n}\, t_n,
\end{aligned}
$$

where $t_n := \dfrac{\ln n}{\sqrt{n}}$.

$$
\begin{aligned}
(2)\quad 
& f(x):=t(x)=\frac{\ln x}{\sqrt{x}},\qquad x>0. \\[6pt]
(3)\quad 
& f'(x)
 =\frac{(1/x)\sqrt{x}-\ln(x)\,\frac{1}{2\sqrt{x}}}{(\sqrt{x})^{2}}
 =\frac{1-\tfrac{1}{2}\ln x}{x^{3/2}}. \\[6pt]
& \text{Hence } f'(x)\le 0 \text{ for } x\ge e^{2} 
\;\Rightarrow\; t_{n+1}\le t_n \text{ for all sufficiently large } n.
\end{aligned}
$$

$$
\begin{aligned}
(5)\quad 
& \lim_{n\to\infty} t_n
 = \lim_{n\to\infty} \frac{\ln n}{\sqrt{n}}
 = \lim_{x\to\infty} \frac{\ln x}{\sqrt{x}}
 \overset{\text{L'H}}{=}
 \lim_{x\to\infty} \frac{\frac{1}{x}}{\frac{1}{2\sqrt{x}}}
 = \lim_{x\to\infty} \frac{2\sqrt{x}}{x}
 = \lim_{x\to\infty} \frac{2}{\sqrt{x}} = 0.
\end{aligned}
$$

$$
\therefore\ t_{n+1}\le t_n\ \text{eventually and}\ \lim_{n\to\infty} t_n=0
\ \xRightarrow{\ \text{by alternating series test}\ }\ 
S\ \text{converges}.
$$
### Exercise 20:

$$
\begin{aligned}
(1)\quad 
& S^{(1)} \;:=\; \sum_{n=1}^{\infty} s_n
 \;=\; \sum_{n=1}^{\infty} \frac{n^{1/3}-1}{n^{3/2}+n}. \\[10pt]
(2)\quad 
& \text{Let } t_n := \frac{1}{n^{7/6}},\qquad 
S^{(2)} := \sum_{n=1}^{\infty} t_n \ \text{is a convergent $p$-series (since $p=\tfrac{7}{6}>1$).} \\[10pt]
(3)\quad 
& -\,n^{7/6} \;\le\; n \\[3pt]
 \Rightarrow\quad & n^{3/2}-n^{7/6} \;\le\; n^{3/2}+n \\[3pt]
 \Rightarrow\quad & n^{7/6}\big(n^{1/3}-1\big) \;\le\; n^{3/2}+n \\[3pt]
 \Rightarrow\quad &
\frac{n^{1/3}-1}{\,n^{3/2}+n\,} \;\le\; \frac{1}{n^{7/6}}. \\[6pt]
& \therefore\ s_n \le t_n\ \text{for all } n\ge1.
\end{aligned}
$$

$$
\therefore\ s_n\le t_n\ \text{and}\ \sum_{n=1}^{\infty} t_n\ \text{converges}
\ \xRightarrow{\ \text{by comparison test}\ }\ 
S^{(1)}\ \text{converges}.
$$
### Exercise 21

$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty} s_n
\qquad\text{with}\qquad
s_n := (-1)^n\,t_n,\ \ t_n := \cos\!\left(\frac{1}{n^{2}}\right). \\[10pt]

(2)\quad 
& \lim_{n\to\infty} t_n 
 = \lim_{n\to\infty} \cos\!\left(\frac{1}{n^{2}}\right) 
 = \cos(0)=1. \\[10pt]

(3)\quad 
& f(x):=\cos\!\left(\frac{1}{x^{2}}\right). \\[6pt]

(4)\quad 
& f'(x)= -\sin\!\left(\frac{1}{x^{2}}\right)\cdot(-2)\cdot\frac{1}{x^{3}}
 \;=\; 2\,\sin\!\left(\frac{1}{x^{2}}\right)\cdot\frac{1}{x^{3}}. \\[4pt]
& \text{From (4): } f'(x)\ \text{oscillates, hence}\ \sim\,(t_{n+1}\le t_n)\ \text{for large } n\in\mathbb{N}. \\[12pt]

(5)\quad 
& \lim_{n\to\infty} t_n = 1 \ \Rightarrow\ \lim_{n\to\infty} |s_n| = 1\ \Rightarrow\ \lim_{n\to\infty} s_n \neq 0. \\[10pt]

 
&  \therefore \quad (6)\quad \lim_{n\to\infty} s_n \neq 0
\ \xRightarrow{\ \text{by divergence test}\ }\ 
S\ \text{diverges}.
\end{aligned}
$$
**OR:**

$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} (-1)^n \cos\!\left(\frac{1}{n^{2}}\right). \\[12pt]

(2)\quad 
& \lim_{n\to\infty} s_n
   \;=\; \lim_{n\to\infty}\Big[\,(-1)^n \cdot \cos\!\left(\tfrac{1}{n^{2}}\right)\Big] \\[4pt]
& \qquad\ \quad \;=\; \Big(\lim_{n\to\infty}(-1)^n\Big)\cdot 
               \Big(\lim_{n\to\infty}\cos\!\left(\tfrac{1}{n^{2}}\right)\Big) \\[4pt]
& \qquad\ \quad \;=\; \Big(\lim_{n\to\infty}(-1)^n\Big)\cdot 1
   \;=\; \text{DNE}. \\[12pt]

& \therefore\ \lim_{n\to\infty} s_n\ \text{does not exist}
\ \xRightarrow{\ \text{by divergence test}\ }\ 
S\ \text{diverges}.
\end{aligned}
$$
### Exercise 22:

$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} \frac{1}{\,2+\sin n\,}. \\[10pt]

(2)\quad 
& 1 \le 2+\sin n \le 3 
\quad \Rightarrow \quad 
\frac{1}{3} \le s_n=\frac{1}{\,2+\sin n\,} \le 1
\ \text{ for all } n\in\mathbb{N}. \\[8pt]
& \therefore\ \lim_{n\to\infty}s_n \ne 0
\ \xRightarrow{\ \text{by divergence test}\ }\ 
S\ \text{diverges}.
\end{aligned}
$$
### Exercise 23:

$$
\begin{aligned}
(1)\quad 
& S^{(1)} := \sum_{n=1}^{\infty} s_n \;=\; \sum_{n=1}^{\infty} \tan\!\left(\frac{1}{n}\right). \\[10pt]

(2)\quad 
& S^{(2)} := \sum_{n=1}^{\infty} t_n \;=\; \sum_{n=1}^{\infty} \frac{1}{n} 
\qquad\text{(harmonic series, divergent).} \\[12pt]

(3)\quad 
& L := \lim_{n\to\infty}\frac{s_n}{t_n}
     \;=\; \lim_{n\to\infty}\frac{\tan(1/n)}{1/n}
     \;=\; \lim_{u\to 0^+}\frac{\tan u}{u} \\[4pt]
& \qquad\ \qquad\ \quad\ \overset{\text{L'H}}{=}\ \lim_{u\to 0^+}\frac{\sec^{2}u}{1}
     \;=\; 1. \\[10pt]

& \therefore\ L=1>0\ \xRightarrow{\ \text{by limit comparison test}\ }\ 
S^{(1)}\ \text{diverges}.
\end{aligned}
$$
### Exercise 24:

$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} n\,\sin\!\left(\frac{1}{n}\right). \\[10pt]

(2)\quad 
& \lim_{n\to\infty} s_n 
   \;=\; \lim_{n\to\infty} n\,\sin\!\left(\frac{1}{n}\right)
   \;=\; \lim_{n\to\infty} \frac{\sin(1/n)}{1/n}
   \;=\; \lim_{u\to 0^+} \frac{\sin u}{u} \\[2pt]
& \qquad \quad\  \overset{\text{L'H}}{=}\ \lim_{u\to 0^+} \frac{\cos u}{1}
   \;=\; 1. \\[10pt]

& \therefore\ \lim_{n\to\infty} s_n = 1\neq 0 
\ \xRightarrow{\ \text{by divergence test}\ }\ 
S\ \text{diverges}.
\end{aligned}
$$
### Exercise 25:


$$
\begin{aligned}
(1)\quad 
& S := \sum_{n=1}^{\infty} s_n 
   \;=\; \sum_{n=1}^{\infty} \frac{n!}{e^{\,n^2}}. \\[12pt]

(2)\quad 
& L := \lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
   \;=\; \lim_{n\to\infty}\left|
      \frac{(n+1)!/e^{(n+1)^2}}{n!/e^{n^2}}
   \right|
   \;=\; \lim_{n\to\infty} (n+1)\, e^{\,n^2-(n+1)^2} \\[4pt]
& \qquad\qquad\quad\ \qquad\
   =\; \lim_{n\to\infty} (n+1)\, e^{-(2n+1)}
   \;=\; 0 \;<\; 1. \\[10pt]

& \therefore\ L<1\ \xRightarrow{\ \text{by ratio test}\ }\ 
S\ \text{converges (absolutely)}.
\end{aligned}
$$
### Exercise 26:
$$
\begin{aligned}
& (1)\quad S := \sum_{n=1}^{\infty} s_n \;=\; \sum_{n=1}^{\infty} \frac{n^{2}+1}{5^{\,n}} \\[12pt]
& (2)\quad L := \lim_{n\to\infty}\left|\frac{s_{n+1}}{s_n}\right|
\;=\; \lim_{n\to\infty}\left|\frac{(n+1)^{2}+1}{5^{\,n+1}}\cdot\frac{5^{\,n}}{n^{2}+1}\right| \\[4pt]
& \qquad\qquad\qquad\qquad\ \quad\;\; =\; \lim_{n\to\infty} \frac{(n+1)^{2}+1}{5\,(n^{2}+1)}
\;=\; \lim_{n\to\infty} \frac{n^{2}+2n+2}{5\,(n^{2}+1)} \\[4pt]
& \qquad\qquad\qquad\qquad\ \quad\;\; =\; \lim_{n\to\infty}\!\left(\frac{1}{5}+\frac{2n+1}{5\,(n^{2}+1)}\right)
\;=\; \frac{1}{5}. \\[10pt]
& \therefore\ L<1\ \xRightarrow{\ \text{by ratio test}\ }\ S\ \text{converges}.
\end{aligned}
$$
### Exercise 27:

$$
\begin{aligned}
(1)\quad 
& S^{(1)} \;:=\; \sum_{n=1}^{\infty} s_n 
\;=\; \sum_{k=1}^{\infty} \frac{k\,\ln k}{(k+1)^{3}}. \\[10pt]
(2)\quad 
& S^{(2)} \;:=\; \sum_{n=1}^{\infty} t_n 
\;=\; \sum_{n=1}^{\infty} \frac{\ln n}{n^{2}}. \\[14pt]
(3)\quad 
& \text{Let } f(x):=\frac{\ln x}{x^{2}}\ \text{ and evaluate } \int_{1}^{\infty} f(x)\,dx: \\[2pt]
& \int_{1}^{\infty}\frac{\ln x}{x^{2}}\,dx
\;=\; \lim_{t\to\infty}\int_{1}^{t}\frac{\ln x}{x^{2}}\,dx \xRightarrow{\ u=\ln x,\; dv=\frac{1}{x^{2}}dx\ }\ 
\Big[\,du=\frac{1}{x}dx,\; v=-\frac{1}{x}\,\Big] \\[4pt]
& \qquad\ \qquad\ \quad\ =\; \lim_{t\to\infty}\Big(\ln x\cdot\!\left(-\frac{1}{x}\right)\Big)\Big|_{1}^{t}
\;+\; \lim_{t\to\infty}\int_{1}^{t}\frac{1}{x^{2}}\,dx \\[4pt]
& \qquad\ \qquad\ \quad\ =\; \lim_{t\to\infty}\Big(\frac{\ln 1-\ln t}{t}\Big)\;+\; \Big(1-\frac{1}{t}\Big)
\;=\; 0+1 \;=\; 1. \\[6pt]
& \therefore\ \int_{1}^{\infty}\frac{\ln x}{x^{2}}\,dx \text{ converges}
\ \xRightarrow{\ \text{by integral test}\ }\ 
S^{(2)} \text{ converges}. \\[16pt]
(4)\quad 
& \text{For } n\ge 1:\quad n\cdot n^{2}\le (n+1)^{3}
\ \Rightarrow\ \ln(n)\,n\,n^{2}\le \ln(n)\,(n+1)^{3} \\[4pt]
& \Rightarrow\ \frac{\ln(n)\,n}{(n+1)^{3}}\le \frac{\ln(n)}{n^{2}}
\ \Rightarrow\ s_n \le t_n. \\[10pt]
& \therefore\ s_n\le t_n\ \land\ S^{(2)}\ \text{convergent}
\ \xRightarrow{\ \text{by comparison test}\ }\ 
S^{(1)}\ \text{converges}.
\end{aligned}
$$
### Exercise 28:

$$
\begin{aligned}
(1)\quad 
& S^{(1)} \;:=\; \sum_{n=1}^{\infty} s_n 
\;=\; \sum_{n=1}^{\infty} \frac{e^{1/n}}{n^{2}}. \\[10pt]
(2)\quad 
& S^{(2)} \;:=\; \sum_{n=1}^{\infty} t_n 
\;=\; \sum_{n=1}^{\infty} \frac{1}{n^{2}}
\qquad (\text{convergent } p\text{-series}). \\[14pt]
(3)\quad 
& L \;:=\; \lim_{n\to\infty} \frac{s_n}{t_n}
\;=\; \lim_{n\to\infty} \frac{\dfrac{e^{1/n}}{n^{2}}}{\dfrac{1}{n^{2}}}
\;=\; \lim_{n\to\infty} e^{1/n}
\;=\; e^{\,0}
\;=\; 1 \;>\; 0. \\[10pt]
& \therefore\ L=1>0\ 
\xRightarrow{\ \text{by limit comparison test}\ }\ 
S^{(1)}\ \text{converges}.
\end{aligned}
$$
