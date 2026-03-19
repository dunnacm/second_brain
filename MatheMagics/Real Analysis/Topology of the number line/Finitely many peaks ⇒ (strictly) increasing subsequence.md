---
down:
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:
If a real sequence $\,\{s_n\}\,$ has **only finitely many peaks**—that is, there is a last peak index—then beyond that index we can choose terms that keep getting larger, yielding a **strictly increasing subsequence** $\,s_{n_1}<s_{n_2}<s_{n_3}<\cdots$.

![[bb28cfa1-e068-4252-a19d-10c7345d5467_white.png]]
### Formal definition:

> [!note]+ **Finitely many peaks ⇒ (strictly) increasing subsequence**
> > [!warning]+ **IF**
> > - $\exists P\in\mathbb{N}\ \ \forall n\in\mathbb{N}\,[\,n\ge P \Rightarrow \neg(\forall m\in\mathbb{N}\,[\,m\ge n \Rightarrow s_n\ge s_m\,])\,]$  
> >   (i.e., there is a last peak; equivalently, $\forall n\ge P\ \exists m>n\ (s_m>s_n)$).
> 
> 
> > [!tip]+ **THEN**
> > $$
> > \exists\,(n_j)_{j\in\mathbb{N}}\subseteq\mathbb{N}\ \ \big[\,n_{j+1}>n_j\ \land\ s_{n_{j+1}}>s_{n_j}\ \text{ for all }j\,\big]
> > \quad\text{(hence $(s_{n_j})$ is strictly increasing).}
> > $$
## Proof:
**Assumptions**
- There are finitely many peaks (so there is a **last** peak index \(N\)).
- $\{k_n\}_{n\in\mathbb{N}}\subseteq\mathbb{N}$ and $\forall n\in\mathbb{N}\,[\,k_n\le k_{n+1}\,]$.

Applying **UI** on \(n\) in the second assumption:
$$
\begin{aligned}
(1)\quad 
& k_n\le k_{n+1}
\Rightarrow\ k_n+N\le k_{n+1}+N .
\end{aligned}
$$

From the first assumption (definition of **last peak**):
$$
\begin{aligned}
(2)\quad 
& s_N \text{ is the last peak}
\ \Leftrightarrow\
\forall n\in\mathbb{N}\,[\,N\le n \Rightarrow s_N\ge s_n\,].
\end{aligned}
$$

Applying **UI** on $n$ in (2) with $n:=N+1$:
$$
\begin{aligned}
(2')\quad 
& s_N \text{ is the last peak}
\ \Leftrightarrow\
N\le N+1 \Rightarrow s_N\ge s_{N+1}.
\end{aligned}
$$

Now derive the stepwise increase for the tail chosen by $\{k_n\}$:
$$
\begin{aligned}
(3)\quad 
& s_{N+k_n}\ \text{is NOT the last peak}
\\
& \Leftrightarrow\ 
\neg\big[\,N+k_n\le N+k_{n+1} \Rightarrow s_{N+k_n}\ge s_{N+k_{n+1}}\,\big]
\\[6pt]
& \Rightarrow\ 
\neg\Big(\neg[\,N+k_n\le N+k_{n+1}\,]\ \vee\ [\,s_{N+k_n}\ge s_{N+k_{n+1}}\,]\Big)
\\[6pt]
& \Rightarrow\ 
N+k_n\le N+k_{n+1}\ \land\ \neg[\,s_{N+k_n}\ge s_{N+k_{n+1}}\,]\qquad\text{(note that antecedent aligns with (1))}
\\[6pt]
& \Rightarrow\ 
N+k_n\le N+k_{n+1}\ \land\ s_{N+k_n}\le s_{N+k_{n+1}} \qquad (\text{cancel }N)
\\[6pt]
& \Rightarrow\ 
k_n\le k_{n+1}\ \land\ s_{N+k_n}\le s_{N+k_{n+1}}\qquad (\text{simpl.})
\\[6pt]
& \Rightarrow\ s_{N+k_n}\le s_{N+k_{n+1}}. 
\end{aligned}
$$
$\therefore$ ${s_{N+k_n}}$ is nondecreasing (a monotone subsequence).