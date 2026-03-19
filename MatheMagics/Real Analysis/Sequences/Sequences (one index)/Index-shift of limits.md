---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:

> [!note]+ **Index-shift of limits theorem**
>
> > [!warning]+ **IF**
> > $\{s_n]\}$ is a real sequence
>
> > [!tip]+ **THEN**
> > $$
> >   \lim_{n\to\infty} s_n = L \quad \Leftrightarrow \quad \lim_{n\to\infty} s_{n+k} = L, k\in\mathbb{N}
> >   $$
## Proof:
$$
\begin{aligned}
& (1)\quad 
\lim_{n\to\infty}s_n=L_1 
\Leftrightarrow 
\forall \varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N\,[\,n\ge N \Rightarrow |s_n-L_1|<\varepsilon\,].\\[10pt]
& (2)\quad 
\lim_{n\to\infty}s_{n+k}=L_2 
\Leftrightarrow 
\forall \varepsilon>0\ \exists N\in\mathbb N\ \forall n,k\in\mathbb N\,[\,n+k\ge N \Rightarrow |s_{n+k}-L_2|<\varepsilon\,].
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$ and UI on $n$ to (1) sequentially:

$$
\begin{aligned}
& (3)\quad n\ge N \Rightarrow |s_n-L_1|<\varepsilon \\[10pt]
& \qquad (n\ge N \Rightarrow n+k\ge N \wedge n\ge N) \Rightarrow |s_n-L_1|<\varepsilon.
\end{aligned}
$$

Applying UI on $\varepsilon$, EI on $N$ and UI on $n$ to (2) sequentially:

$$
\begin{aligned}
& (4)\quad n+k\ge N \Rightarrow |s_{n+k}-L_2|<\varepsilon \\[10pt]
& \qquad (n+k\ge N \Rightarrow n+k\ge N \wedge n\ge N) \Rightarrow |s_{n+k}-L_2|<\varepsilon.
\end{aligned}
$$

Translate to propositional variables:
let 
$a:=(n\ge N)$, 
$b:=\big(|s_n-L_1|<\varepsilon\big)$, 
$c:=(n+k\ge N)$, 
$d:=\big(|s_{n+k}-L_2|<\varepsilon\big)$.

From (3), first line:
$$
\begin{aligned}
& (5)\quad a \to b
\end{aligned}
$$

From (4), first line:
$$
\begin{aligned}
& (6)\quad c \to d
\end{aligned}
$$

From (3), second line:
$$
\begin{aligned}
& (7)\quad (a\to [\,c\wedge a\,]) \to b
\end{aligned}
$$

From (4), second line:
$$
\begin{aligned}
& (8)\quad (c\to [\,c\wedge a\,]) \to d
\end{aligned}
$$

From (5)–(8), we can derive (in propositional logic):
$$
\begin{aligned}
& (9)\quad a\to b,\ c\to d,\ (a\to[c\wedge a])\to b,\ (c\to[c\wedge a])\to d\ \vdash\ (a\to d)\ \Leftrightarrow\ (c\to b).
\end{aligned}
$$

Translate (9) back:

$$
\begin{aligned}
& (10)\quad (a\to d)\Leftrightarrow(c\to b):
\ [\,n\ge N \Rightarrow |s_{n+k}-L_2|<\varepsilon\,]
\ \Leftrightarrow\
[\,n+k\ge N \Rightarrow |s_n-L_1|<\varepsilon\,].
\end{aligned}
$$

Applying UG on $n$ and $k$, EG on $N$, and UG on $\varepsilon$ to (10):

$$
\begin{aligned}
& (11)\quad 
\forall \varepsilon>0\ \exists N\in\mathbb N\ \forall n,k\in\mathbb N\,
\Big( [\,n\ge N \Rightarrow |s_{n+k}-L_2|<\varepsilon\,]
\Leftrightarrow
[\,n+k\ge N \Rightarrow |s_n-L_1|<\varepsilon\,] \Big)
\\
& \qquad \Leftrightarrow\ 
\left[
\left(\lim_{n\to\infty}s_n = L_2\right)
\Leftrightarrow
\left(\lim_{n\to\infty}s_{n+k}=L_1\right)
\right].
\end{aligned}
$$

Therefore,
$$
\begin{aligned}
& (12)\quad \lim_{n\to\infty}s_n = L_1 = \lim_{n\to\infty}s_{n+k} = L_2 = L.
\end{aligned}
$$

