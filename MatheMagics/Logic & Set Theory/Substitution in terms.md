---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
>[!important] **Preconditions**
> - Let $S$ be the set of theory symbols from a first-order alphabet $A$.  
> - Let $x$ be a variable symbol from $A$ and let $t$ be an $S$-term.  
> - The notation $u[x:=t]$ means: **replace every occurrence of $x$ in $u$ by $t$**.
>
>
## Rules:
Defined by structural induction on terms:
### Variables:

>[!Quote]+ **Rule 1/3**
>$$
>y[x:=t]=
>\begin{cases}
>t, & \text{if } x=y,\\
>y, & \text{if } x\neq y.
>\end{cases}
>$$
>

### Constants

>[!quote]+ **Rule 2/3**
>$$
>c[x:=t]=c.
>$$
>

### Function Symbols:

>[!quote]+ **Function symbols**
>$$
>f(s_0,\ldots,s_{n-1})[x:=t]
>=f\big(s_0[x:=t],\ldots,s_{n-1}[x:=t]\big).
>$$


## Examples:
Let:
- *x, y, z* be distinct symbols
- *c, d* be constant symbols
- *f* be a binary function symbol
$$
\begin{aligned}
 & (1) \qquad x[x:=y] \;\Leftrightarrow\; y \\[6pt]
 & (2) \qquad x[x:=c] \;\Leftrightarrow\; c \\[6pt]
 & (3) \qquad y[x:=f(x,z)] \;\Leftrightarrow\; y \\[6pt]
 & (4) \qquad c[x:=x] \;\Leftrightarrow\; c \\[6pt]
 & (5) \qquad d[x:=c] \;\Leftrightarrow\; d \\[6pt]
 & (6) \qquad c[x:=g(x)] \;\Leftrightarrow\; c \\[6pt]
 & (7) \qquad f(x,y)[y:=c] \;\Leftrightarrow\; f(x,c) \\[10pt]
 & (8) \qquad \big(f(y,z)[y:=h(c)]\big)[x:=g(y)] \;\Leftrightarrow\; f(h(c),z)[x:=g(y)] \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \ \Leftrightarrow\; f(h(c),z) \\[10pt]
 & (9) \qquad ((((z[x:=c])[y:=d])[z:=c])[x:=d]) \;\Leftrightarrow\; (((z[y:=d])[z:=c])[x:=d]) \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \, \, \, \, \, \,\Leftrightarrow\; ((z[z:=c])[x:=d]) \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \, \, \, \, \, \, \Leftrightarrow\; (c[x:=d]) \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \, \, \, \, \, \, \Leftrightarrow\; c \\[10pt]
 & (10) \qquad (\,[f(x,y)[x:=c]][y:=g(x)]\,)[z:=x][x:=g(d)] \;\Leftrightarrow\; (\,[f(c,y)[y:=g(x)]][z:=x]\,)[x:=g(d)] \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \, \Leftrightarrow\; (f(c,g(x))[z:=x])[x:=g(d)] \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \, \Leftrightarrow\; f(c,g(x))[x:=g(d)] \\[3pt]
 & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \, \Leftrightarrow\; f(c, g(g(d)))
\end{aligned}
$$