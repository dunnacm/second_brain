---
down:
tags:
  - mathemagics/real_analysis
---
## Example 1:
### Convergence:
$$
\begin{aligned}
& \quad \text{(1)}\quad \{s_n\}=\Bigl\{\frac{1}{n}\Bigr\},\quad \text{prove }\displaystyle\lim_{n\to\infty}s_n=0. \\[8pt]

& \quad \text{From definition: (2)}\quad
\forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]. \\[8pt]

& \quad \text{UI over }\varepsilon\ \text{(in eq.\,(2)): (3)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]. \\[8pt]

& \quad \text{EI over }N\ \text{(in eq.\,(3)): (4)}\quad
\forall n\in\mathbb{N}\,[\,n\ge N_{\varepsilon} \Rightarrow |s_n-L|<\varepsilon\,]. \\[10pt]

& \quad \text{(5)}\quad |s_n-L|<\varepsilon\ \ (\varepsilon>0) \\[2pt]
& \qquad \quad \, \, \Bigl|\frac{1}{n}-0\Bigr|<\varepsilon\ \ (\varepsilon>0) \\[2pt]
& \qquad \quad \, \, \frac{1}{n}-0<\varepsilon\ \\[2pt]
& \qquad \quad \, \, \frac{1}{n}<\varepsilon \\[2pt]
& \qquad \quad \, \, n>\frac{1}{\varepsilon} \\[8pt]

& \quad \text{Informed by (5), choose: (6)}\quad
N_{\varepsilon}:=\Bigl\lceil\frac{1}{\varepsilon}\Bigr\rceil+1. \\[10pt]

& \quad \text{From antecedent in (4):}\\
& \quad \text{(7)}\quad n\ge N_{\varepsilon}\ \ \text{(sub.\ from (6))} \\[2pt]
& \qquad \quad \, \, n\ge \Bigl\lceil\frac{1}{\varepsilon}\Bigr\rceil+1 \Rightarrow n>\frac{1}{\varepsilon}
\Rightarrow \frac{1}{n}<\varepsilon
\Rightarrow \Bigl|\frac{1}{n}-0\Bigr|<\varepsilon
\Rightarrow |s_n-0|<\varepsilon. \\[6pt]
& \qquad \quad \, \, \Rightarrow\ \text{(8)}\quad n\ge N_{\varepsilon} \Rightarrow |s_n-0|<\varepsilon. \\[10pt]

& \quad \text{UG over }n\ \text{(in eq.\,(8)): (9)}\quad
\forall n\in\mathbb{N}\,[\,n\ge N_{\varepsilon} \Rightarrow |s_n-0|<\varepsilon\,]. \\[8pt]

& \quad \text{EG over }N\ \text{(in eq.\,(9)): (10)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-0|<\varepsilon\,]. \\[8pt]

& \quad \text{UG over }\varepsilon\ \text{(in eq.\,(10)): (11)}\quad
\forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-0|<\varepsilon\,].\ \square
\end{aligned}
$$

## Example 2:
### Convergence:
$$
\begin{aligned}
& \quad \text{(1)}\quad \{s_n\}=\Bigl\{\frac{n}{n+1}\Bigr\},\quad \text{prove }\displaystyle\lim_{n\to\infty}s_n=1. \\[8pt]

& \quad \text{From definition: (2)}\quad
\forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-1|<\varepsilon\,]. \\[8pt]

& \quad \text{UI over }\varepsilon\ \text{(in eq.\,(2)): (3)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-1|<\varepsilon\,]. \\[8pt]

& \quad \text{EI over }N\ \text{(in eq.\,(3)): (4)}\quad
\forall n\in\mathbb{N}\,[\,n\ge N_{\varepsilon} \Rightarrow |s_n-1|<\varepsilon\,]. \\[10pt]

& \quad \text{(5)}\quad |s_n-1|<\varepsilon\ \ (\varepsilon>0) \\[2pt]
& \qquad \quad \, \, \Bigl|\frac{n}{n+1}-1\Bigr|<\varepsilon\ \ (\varepsilon>0) \\[2pt]
& \qquad \quad \, \, \Bigl|\frac{n-(n+1)}{n+1}\Bigr|<\varepsilon \\[2pt]
& \qquad \quad \, \, \Bigl|\frac{-1}{n+1}\Bigr|<\varepsilon \\[2pt]
& \qquad \quad \, \, \frac{1}{n+1}<\varepsilon \\[2pt]
& \qquad \quad \, \, n+1>\frac{1}{\varepsilon} \\[2pt]
& \qquad \quad \, \, n>\frac{1}{\varepsilon}-1. \\[8pt]

& \quad \text{Informed by (5), choose: (6)}\quad
N_{\varepsilon}:=\Bigl\lceil\frac{1}{\varepsilon}-1\Bigr\rceil+1. \\[10pt]

& \quad \text{From antecedent in (4):}\\
& \quad \text{(7)}\quad n\ge N_{\varepsilon}\ \ \text{(sub.\ from (6))} \\[2pt]
& \qquad \quad \, \, n\ge \Bigl\lceil\frac{1}{\varepsilon}-1\Bigr\rceil+1 \Rightarrow n>\frac{1}{\varepsilon}-1 \\[2pt]
& \qquad \quad \, \, \Rightarrow n+1>\frac{1}{\varepsilon}
\Rightarrow \frac{1}{n+1}<\varepsilon
\Rightarrow \Bigl|\frac{n}{n+1}-1\Bigr|<\varepsilon
\Rightarrow |s_n-1|<\varepsilon. \\[6pt]
& \qquad \quad \, \, \Rightarrow\ \text{(8)}\quad n\ge N_{\varepsilon} \Rightarrow |s_n-1|<\varepsilon. \\[10pt]

& \quad \text{UG over }n\ \text{(in eq.\,(8)): (9)}\quad
\forall n\in\mathbb{N}\,[\,n\ge N_{\varepsilon} \Rightarrow |s_n-1|<\varepsilon\,]. \\[8pt]

& \quad \text{EG over }N\ \text{(in eq.\,(9)): (10)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-1|<\varepsilon\,]. \\[8pt]

& \quad \text{UG over }\varepsilon\ \text{(in eq.\,(10)): (11)}\quad
\forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-1|<\varepsilon\,].\ \square
\end{aligned}
$$
## Example 3:
### Divergence, method 1
$$
\begin{aligned}
& \quad \text{(1)}\quad \{s_n\}=\{(-1)^n\},\quad \text{prove } \lim_{n\to\infty} s_n=\varnothing\ \text{(no limit).} \\[8pt]

& \quad \text{Suppose for contradiction: (2)}\quad
\exists L\in\mathbb{R}\ \forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]. \\[10pt]

& \quad \text{UI over }\varepsilon\ \text{ with }\varepsilon=\frac{1}{2}\ \text{(in eq.\,(2)): (3)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\tfrac{1}{2}\,]. \\[8pt]

& \quad \text{From antecedent in (3): choose }n_{\text{even}},n_{\text{odd}}\ge N\ \text{with }n_{\text{even}}\text{ even, }n_{\text{odd}}\text{ odd.} \\[2pt]
& \quad \text{(4)}\quad s_{n_{\text{even}}}=1,\ \ s_{n_{\text{odd}}}=-1. \\[2pt]
& \qquad \quad \, \, \Rightarrow\ \text{(5)}\quad |1-L|<\frac{1}{2}\ \ \text{and}\ \ |-1-L|<\frac{1}{2}. \\[10pt]

& \quad \text{(6)}\quad |1-L|<\frac{1}{2}\ \Leftrightarrow\ -\frac{1}{2}<1-L<\frac{1}{2}
\ \Leftrightarrow\ \frac{1}{2}<L<\frac{3}{2}. \\[4pt]
& \quad \text{(7)}\quad |-1-L|<\frac{1}{2}\ \Leftrightarrow\ -\frac{1}{2}<-1-L<\frac{1}{2}
\ \Leftrightarrow\ -\frac{3}{2}<L<-\frac{1}{2}. \\[8pt]

& \quad \text{(8)}\quad \text{Intervals } \bigl(\tfrac{1}{2},\tfrac{3}{2}\bigr) \text{ and } \bigl(-\tfrac{3}{2},-\tfrac{1}{2}\bigr) \text{ are disjoint}
\ \Rightarrow\ \text{(9)}\quad \bot\ \text{(contradiction).} \\[8pt]

& \quad \Rightarrow\ \text{(10)}\quad \neg\exists L\in\mathbb{R}\ \forall \varepsilon>0\,\exists N\,\forall n\ge N:\ |s_n-L|<\varepsilon \\[2pt]
& \qquad \quad \, \, \Rightarrow\ \text{(11)}\quad \{(-1)^n\}\ \text{diverges (has no limit).}\ \square
\end{aligned}
$$
### Divergence, method 2:
$$
\begin{aligned}
& \quad \text{(1)}\quad \{s_n\}=\{(-1)^n\},\quad \text{prove }\lim_{n\to\infty}s_n=\varnothing\ \text{(no limit).} \\[8pt]

& \quad \text{Assume for contradiction: (2)}\quad
\exists L\in\mathbb{R}\ \forall \varepsilon>0\,\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<\varepsilon\,]. \\[8pt]

& \quad \text{UI over }\varepsilon\text{ with }\varepsilon=1\ \text{(in eq.\,(2)): (3)}\quad
\exists N\in\mathbb{N}\,\forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow |s_n-L|<1\,]. \\[10pt]

& \quad \text{(4)}\quad \text{Choose }n_{\text{even}},n_{\text{odd}}\ge N\ \text{with }n_{\text{even}}\text{ even, }n_{\text{odd}}\text{ odd}. \\[2pt]
& \qquad \quad \, \, s_{n_{\text{even}}}=1,\qquad s_{n_{\text{odd}}}=-1 \\[2pt]
& \qquad \quad \, \, \Rightarrow\ |1-L|<1\ \text{ and }\ |-1-L|<1. \\[10pt]

& \quad \text{(5) Combine the two cases:}\quad |1-L| + |-1-L| < 2. \\[8pt]

& \quad \text{(6) Triangle inequality on the difference:} \\[2pt]
& \qquad \quad \, \, |(1-L)-(-1-L)| \le |1-L| + |-1-L| \\[2pt]
& \qquad \quad \, \, \Rightarrow\ |2| \le |1-L| + |-1-L| \\[2pt]
& \qquad \quad \, \, \Rightarrow\ 2 \le |1-L| + |-1-L|. \\[10pt]

& \quad \text{(7) Contradiction from (5) and (6):}\quad 2 \le |1-L|+|-1-L| < 2. \\[8pt]

& \quad \Rightarrow\ \text{(8)}\quad \neg\exists L\in\mathbb{R}\ \forall \varepsilon>0\,\exists N\,\forall n\ge N:\ |s_n-L|<\varepsilon \\[2pt]
& \qquad \quad \, \, \Rightarrow\ \text{(9)}\quad \{(-1)^n\}\ \text{diverges (has no limit).}\ \square
\end{aligned}
$$
