---
down:
  - "[[Exercises, series convergence test]]"
tags:
  - mathemagics/real_analysis
---
## Definitions:
### Verbal definition:
The **divergence test** (nth-term test) says: for a series **S = ∑ sₙ**, if the terms don’t go to zero—i.e., **lim sₙ ≠ 0**, or the limit of **sₙ** does not exist (including **±∞**)—then the series **diverges**. Equivalently, **if a series converges, its terms must approach 0** (but the converse need not hold).
### Formal definition:

> [!note]+ **Divergence (nth-term) test — minimalist**
>
> > [!warning]+ **IF**:
> > - A series $S=\sum_{n=1}^{\infty}s_n.$
> > - $\lim_{n\to\infty}s_n\neq 0$   **or**   $\lim_{n\to\infty}s_n$ *DNE* (either finitely $\emptyset$ or infinitely $\textpm \infty$)
>
> > [!tip]+ **THEN**
> > Series **S** **diverges**
> 
> > ---
> 
>  **Equivalently (necessary condition for convergence):**  
> $$\sum s_n\ \text{converges} \;\Rightarrow\; \lim_{n\to\infty}s_n=0.$$
## Proofs:
### Proof 1:

Assume the sequence of partial sums $(S_n)$ converges to a finite limit $S$, where
$$
\begin{aligned}
(1)\quad 
& S_n \;=\; \sum_{k=0}^{n} s_k 
\;=\; \underbrace{s_0+s_1+\cdots+s_{n-1}}_{S_{n-1}} \;+\; s_n .
\end{aligned}
$$

From eq. (1) we isolate the $n$-th term:
$$
\begin{aligned}
(2)\quad 
& s_n \;=\; S_n - S_{n-1}\, .
\end{aligned}
$$

Taking limits as $n\to\infty$ and using $\lim_{n\to\infty}S_n=\lim_{n\to\infty}S_{n-1}=S$:
$$
\begin{aligned}
(3)\quad 
& \lim_{n\to\infty} s_n
\;=\; \lim_{n\to\infty}\big(S_n-S_{n-1}\big)
\;=\; \lim_{n\to\infty} S_n \;-\; \lim_{n\to\infty} S_{n-1}
\;=\; S-S \;=\; 0 .
\end{aligned}
$$

$\therefore$ $s_n \to 0$ whenever the series $\sum_{k=0}^{\infty} s_k$ converges.

### Proof 2:
## Examples:
### Example 1:
$$
\begin{aligned}
(1)\quad 
& S=\sum_{n=1}^{\infty}s_n
=\sum_{n=1}^{\infty}\dfrac{2^{\,n}}{n^{2}}.
\end{aligned}
$$

From eq. (1):

$$
\begin{aligned}
(2)\quad 
&\lim_{n\to\infty}s_n
=\lim_{n\to\infty}\dfrac{2^{\,n}}{n^{2}}\\[6pt]
&\overset{\text{L'H}}{=} \lim_{n\to\infty}\dfrac{2^{\,n}\ln(2)}{2\cdot n}\\[6pt]
&\overset{\text{L'H}}{=} \lim_{n\to\infty}\dfrac{2^{\,n}(\ln 2)^{2}}{2}\\[6pt]
&= \dfrac{(\ln 2)^{2}}{2}\cdot\lim_{n\to\infty}2^{\,n}\\[6pt]
&=\infty.
\end{aligned}
$$

$\therefore$ $S$ diverges by the divergence test (since $\lim_{n\to\infty}s_n$ does not exist).
### Example 2:
$$
\begin{aligned}
(1)\quad 
& S=\sum_{n=1}^{\infty}s_n
=\sum_{n=1}^{\infty}(-1)^{n}.
\end{aligned}
$$

From eq. (1):

$$
\begin{aligned}
(2)\quad 
&\lim_{n\to\infty}s_n
=\lim_{n\to\infty}(-1)^{n}.
\end{aligned}
$$

Since $(-1)^{n}$ oscillates between $1$ and $-1$, the limit does **not exist**.

$$
\lim_{n\to\infty}s_n\ \text{DNE},
\quad\therefore\quad
S\ \text{diverges by the divergence test.}
$$
