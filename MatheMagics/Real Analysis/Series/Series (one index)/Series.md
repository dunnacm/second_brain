---
down:
  - "[[Telescopic series]]"
  - "[[Divergence test]]"
  - "[[Geometric series test]]"
  - "[[Integral test]]"
  - "[[Comparison test]]"
  - "[[MatheMagics/Real Analysis/Series/Series (one index)/Limit comparison test]]"
  - "[[Alternating series]]"
  - "[[Absolute convergence test]]"
  - "[[Ratio test]]"
  - "[[Root test]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Finite:
$$
S_N \;=\; \sum_{n=1}^{N} s_n
$$
### Infinite:
$$
S \;=\; \lim_{n\to\infty}\sum_{k=1}^{n} s_k
\;=\; \sum_{n=1}^{\infty} s_n
$$
## Remainder:

>[!note] **Tail (remainder) of a series via index shift**
>>[!warning] **IF**
>>$$S_N \;=\; \sum_{n=1}^{N} s_n$$
>
>>[!tip] **THEN**
>>The remainder (tail) after the \(N\)-th partial sum is
>>$$
>>R_N \;=\; \sum_{n=N+1}^{\infty} s_n
>>\;=\; \sum_{\;n\;\textcolor{red}{+1}=N+1}^{\;\infty\;\textcolor{red}{-1}} s_{\,n+1}
>>\;=\; \sum_{n=N}^{\infty} s_{\,n+1}.
>>$$
## Convergence:

> [!note]+ **Series — tails and remainders**
>
> > [!warning]+ **IFF**
> > $S$ converges.
>
> > [!tip]+ **THEN**
> > - $\lim_{n\to\infty} R_n = 0 \ \Leftrightarrow\ \lim_{N\to\infty}\sum_{n=N}^{\infty} s_{n+1}=0.$
> > - $\lim_{n\to\infty}\big(S - S_n\big)=0.$

## Tail equivalence for series

$$
\begin{aligned}
(1)\quad 
& S_n \;=\; S_N + R_n \\[6pt]
& \lim_{n\to\infty}\sum_{k=1}^{n} s_k 
   \;=\; \sum_{k=1}^{N} s_k \;+\; \lim_{n\to\infty}\sum_{k=N+1}^{n} s_k
\end{aligned}
$$

$$
\begin{aligned}
(1')\quad 
& \sum_{k=1}^{n} s_k \;=\; \sum_{k=1}^{N} s_k \;+\; \sum_{k=N+1}^{n} s_k \\[8pt]
\Rightarrow\ & (2)\quad 
 \lim_{n\to\infty}\sum_{k=1}^{n} s_k 
   \;=\; \sum_{k=1}^{N} s_k \;+\; \lim_{n\to\infty}\sum_{k=N+1}^{n} s_k \\[8pt]
& \sum_{k=1}^{\infty} s_k 
   \;=\; \sum_{k=1}^{N} s_k \;+\; \sum_{k=N+1}^{\infty} s_k \\[6pt]
& S \;=\; S_N + R_N
\end{aligned}
$$

$$
\begin{aligned}
(3)\quad 
&\big(S_n \to S\big)
\;\Leftrightarrow\; \big(S = S + R_n \;\Leftrightarrow\; R_n \to 0\big)
\end{aligned}
$$

Therefore,
$$
\begin{aligned}
(4)\quad 
& \sum_{k=1}^{\infty} s_k \ \Leftrightarrow\  \sum_{k=N+1}^{\infty} s_k
\end{aligned}
$$

Changing indices in (4):
$$
\sum_{n=1}^{\infty} s_n \ \Leftrightarrow\  \sum_{n=N}^{\infty} s_n .
$$

---
***Mnemonic device***
**T**o**D**o **G**ira **I** **C**ome **L**a**C**aca, **A A R R**
- **T**elescopic
- **D**ivergence
- **G**eometric
- **I**ntegral
- **C**omparison
- **L**imit **C**omparison
- **A**lternating
- **A**bsolute convergence
- **R**ation test
- **R**oot test
![[Pasted image 20251105220820.png]]