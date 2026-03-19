---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
A **telescoping series** is a sum whose terms are arranged so that most of them cancel when you form partial sums—typically they look like **bₙ − bₙ₊₁** (or a finite shift of this), so the **N**-th partial sum reduces to just a few boundary terms (e.g., **b₁ − bₙ₊₁**). The series **S** converges exactly when the surviving boundary term has a limit (e.g., **bₙ → L**), and then the sum equals that boundary difference (e.g., **S = b₁ − L**).
## Exercises:
### Exercise 1:
$$
\begin{aligned}
S
&=\sum_{n=1}^{\infty}\big(\arctan(n)-\arctan(n+2)\big)\\[6pt]
&=\arctan(1)-\bcancel{\arctan(3)}
\;+\;\arctan(2)-\bcancel{\arctan(4)}
\;+\;\arctan(3)-\arctan(5)
\;+\;\arctan(4)-\arctan(6)\;+\;\cdots\\[6pt]
&=\arctan(1)+\arctan(2)\;-\;\lim_{n\to\infty}\arctan(n-1)\;-\;\lim_{n\to\infty}\arctan(n)\\[6pt]
&=\frac{\pi}{4}+\arctan(2)-\frac{\pi}{2}-\frac{\pi}{2}\\[6pt]
&=\frac{\pi}{4}+\arctan(2)-\pi\\[6pt]
&=-\frac{3\pi}{4}+\arctan(2).
\end{aligned}
$$
### Exercise 2:
$$
\begin{aligned}
S
&=\sum_{n=1}^{\infty}\frac{6n+3}{n^2(n+1)^2}
=\sum_{n=1}^{\infty}\left(\frac{3}{n^2}-\frac{3}{(n+1)^2}\right)\\[6pt]
&=\frac{3}{1^2}-\frac{3}{2^2}
+\bcancel{\frac{3}{2^2}}-\frac{3}{3^2}
+\bcancel{\frac{3}{3^2}}-\frac{3}{4^2}
+\cdots\\[6pt]
&=3-3\lim_{n\to\infty}\frac{1}{(n+1)^2}\\[6pt]
&=3.
\end{aligned}
$$
