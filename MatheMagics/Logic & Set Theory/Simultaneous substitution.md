---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Motivation (why “one-at-a-time” can fail)
Let
$$
p \;:=\; x+y=0.
$$
Suppose we want to “swap” the variables so the result is $y+x=0$, i.e. we want
$$
p[x:=y,\ y:=x]\;=\;y+x=0.
$$

If we substitute **one-at-a-time**, the first substitution changes the expression in a way that affects the second:

$$
\begin{aligned}
(\,p[x:=y]\,)[y:=x] \quad &\Leftrightarrow \quad (y+y=0)[y:=x] \\
&\Leftrightarrow \quad x+x=0 \\[10pt]
(\,p[y:=x]\,)[x:=y] \quad &\Leftrightarrow \quad (x+x=0)[x:=y] \\
&\Leftrightarrow \quad y+y=0
\end{aligned}
$$

So “do $x:=y$ then $y:=x$” is **not** the same as “swap $x$ and $y$ simultaneously.”

## Procedure
A **simultaneous** substitution must prevent the first replacement from interfering with the later ones.

A standard way is to use **fresh variables** $u_0,\ldots,u_{n-1}$ as temporary placeholders:
1) rename $x_i$ to $u_i$ (so nothing collides),
2) then replace each $u_i$ by the desired term $t_i$.

## Definition (simultaneous substitution)

### Verbal definition
**Simultaneous substitution** replaces all free occurrences of
$$
x_0,\ldots,x_{n-1}
$$
in a formula $p$ by
$$
t_0,\ldots,t_{n-1}
$$
**at the same time** (so earlier replacements do not affect later ones).

### Formal definition

> [!note]+ **Simultaneous substitution $p[x_0:=t_0,\ldots,x_{n-1}:=t_{n-1}]$**
> > [!warning]+ **IF**
> > - Conditions in **parametrizing a formula by its FVs (free variables)** are met:
>>>  ◦ $p$ has an ordered, pairwise-distinct list of variables $x_0,\ldots,x_{n-1}$  
>>>  ◦ $\mathrm{FV}(p)\subseteq\{x_0,\ldots,x_{n-1}\}$  
> > - For each $i<n$, the term $t_i$ is **free for** $x_i$ in $p$ (so substitution does not cause variable capture).
> > - $u_0,\ldots,u_{n-1}$ are **fresh** variables (not occurring in $p$ or any $t_i$).
>
> > [!tip]+ **THEN**
> > $$
> > p[x_0:=t_0,\ldots,x_{n-1}:=t_{n-1}]
> > \;:=\;
> > \Big(p[x_0:=u_0,\ldots,x_{n-1}:=u_{n-1}]\Big)[u_0:=t_0]\cdots[u_{n-1}:=t_{n-1}].
> > $$
> > (Only free occurrences are replaced.)
> > 
> > **Note.** This definition builds simultaneity into the syntax: the first stage “protects” the variables by moving them to fresh placeholders.

## Motivating example revisited (swap)
Let $p:=x+y=0$. Choose fresh $u,v$.

$$
\begin{aligned}
p[x:=y,\ y:=x]
\;&:=\;
\big(p[x:=u,\ y:=v]\big)[u:=y][v:=x] \\[6pt]
&\Leftrightarrow\;
(u+v=0)[u:=y][v:=x] \\[6pt]
&\Leftrightarrow\;
y+x=0
\end{aligned}
$$

## Examples

### Example 1
Let $p \equiv R(x,y)\land Q(z)$. Then

$$
p(x,y,z) \Leftrightarrow R(x,y)\land Q(z).
$$

Simultaneous substitution via the argument list:

$$
p(a,\,f(b),\,b)
:= p[x:=a,\, y:=f(b),\, z:=b]
\Leftrightarrow R(a,f(b)) \land Q(b).
$$

Closed formula:

$$
\begin{aligned}
p[x:=a,\ y:=f(b),\ z:=b]
\quad &\Leftrightarrow \quad R(a,f(b))\land Q(b).
\end{aligned}
$$

### Example 2
$$
\begin{aligned}
& \text{Let } p := x \otimes (y \oplus z) \;=\; x \otimes y \;\oplus\; x \otimes z. \\[4pt]
& \text{Represent } p \text{ by } p(x,y,z,w). \\[6pt]
& \text{Find } p(1,x,y,2) \text{ by step-by-step substitution and by simultaneous substitution.} \\[10pt]

& \textbf{Step-by-step substitution (generic} \rightarrow \textbf{ specific):} \\[4pt]
& p(x,y,z,w)\ \mapsto\ p(u_1,u_2,u_3,u_4): \\[2pt]
& \qquad \big(\!\big(\!\big(p(x,y,z,w)[x:=u_1]\big)[y:=u_2]\big)[z:=u_3]\big)[w:=u_4] \\[3pt]
& \qquad \Leftrightarrow\ \big(\!\big(\!(\,u_1\otimes(y\oplus z)=u_1\otimes y\oplus u_1\otimes z\,)[y:=u_2]\big)[z:=u_3]\big)[w:=u_4] \\[3pt]
& \qquad \Leftrightarrow\ \big(\!(\,u_1\otimes(u_2\oplus z)=u_1\otimes u_2\oplus u_1\otimes z\,)[z:=u_3]\big)[w:=u_4] \\[3pt]
& \qquad \Leftrightarrow\ \big(\,u_1\otimes(u_2\oplus u_3)=u_1\otimes u_2\oplus u_1\otimes u_3\,\big)[w:=u_4] \\[3pt]
& \qquad \Leftrightarrow\ u_1\otimes(u_2\oplus u_3)=u_1\otimes u_2\oplus u_1\otimes u_3. \\[10pt]

& \textbf{Now plug in } (u_1,u_2,u_3,u_4)=(1,x,y,2): \\[4pt]
& \big(\!\big(\!\big(p(u_1,u_2,u_3,u_4)[u_1:=1]\big)[u_2:=x]\big)[u_3:=y]\big)[u_4:=2] \\[3pt]
& \qquad \Leftrightarrow\ \big(\!\big(\!(\,u_1\otimes(u_2\oplus u_3)=u_1\otimes u_2\oplus u_1\otimes u_3\,)[u_1:=1]\big)[u_2:=x]\big)[u_3:=y] \\[3pt]
& \qquad \Leftrightarrow\ \big(\!\big(\,1\otimes(u_2\oplus u_3)=1\otimes u_2\oplus 1\otimes u_3\,\big)[u_2:=x]\big)[u_3:=y] \\[3pt]
& \qquad \Leftrightarrow\ \big(\,1\otimes(x\oplus u_3)=1\otimes x\oplus 1\otimes u_3\,\big)[u_3:=y] \\[3pt]
& \qquad \Leftrightarrow\ 1\otimes(x\oplus y)=1\otimes x\oplus 1\otimes y. \\[12pt]

& \textbf{Simultaneous substitution:} \\[4pt]
& p(x,y,z,w)[\,x:=1,\ y:=x,\ z:=y,\ w:=2\,] \\[3pt]
& \qquad \Leftrightarrow\ (\,x\otimes(y\oplus z)=x\otimes y\oplus x\otimes z\,)[\,x:=1,\ y:=x,\ z:=y,\ w:=2\,] \\[3pt]
& \qquad \Leftrightarrow\ 1\otimes(x\oplus y)=1\otimes x\oplus 1\otimes y. \\[10pt]

& \boxed{\,p(1,x,y,2)=1\otimes(x\oplus y)=1\otimes x\oplus 1\otimes y\,}
\end{aligned}
$$
### Example 3
Let $S$ have constant symbols $5$ and $9$.  
Define the $S$-formula

$$
p(x,y) := \forall x \, \exists z \, [q(x,y) \wedge r(z)] \;\; \lor \;\; \exists y \,[\, r(y) \to s(x) \,].
$$
Therefore, it is the disjunction of two formulas.
- The *occurrence* of *y* in the first conjunctive formula is **free**, therefore, this formula will be represented terms of *y*, say *u(y)*.
- The *occurrence* of $x$ in the last conjunctive formula is **free**, therefore, this formula will be represented in terms of *x*.   

Therefore, $p(x,y)$ will be denoted thusly:

$$
\underbrace{\forall x \, \exists z \, [q(x,y) \wedge r(z)]}_{u(y)}
\;\; \lor \;\;
\underbrace{\exists y \,[\, r(y) \to s(x) \,]}_{v(x)}.
$$

Namely:

$$
p(x,y) \equiv u(y) \lor v(x).
$$

Now, performing the given substitution:

$$
p(9,5) \;\;\equiv\;\; u(5) \lor v(9)
\;\;\equiv\;\; \forall x \, \exists z \, [q(x,5) \wedge r(z)] \;\lor\; \exists y \,[\, r(y) \to s(9)\,].
$$

As in Example 2.2.11, computing $p(9,5)$ is simply replacing the free occurrences of  
$x$ with $9$ and the free occurrences of $y$ with $5$.
### Example 4

Consider the NT-formula:

$$
\forall x \forall y \forall z \; [(x+y)+z = x+(y+z)].
$$
Let's define the formula within the scope of the first, the first two and finally all of its variables:
#### In terms of *x*
Defining a formula within the scope of the first quantifier:

$$
p(x) := \forall y \forall z \; [(x+y)+z = x+(y+z)].
$$
Let's make the substitution $[x:=2]$:

$$
p(2) \;\;\equiv\;\; \forall y \forall z \; [(2+y)+z = 2+(y+z)].
$$
Notice:
 - The occurrences of $x$ are **free** in $p(x)$.  
 - The occurrences of $y$ and $z$ are **bound**.  

#### In terms of *x* and *y*
Defining a formula within the scope of the first two quantifiers:

$$
q(x,y) := \forall z \; [(x+y)+z = x+(y+z)],
$$

so that:

$$
p(x) \;\;\equiv\;\; \forall y \, q(x,y).
$$
#### In terms of *x*, *y* and *z*
Define:

$$
r(x,y,z) := (x+y)+z = x+(y+z),
$$

so that:

$$
q(x,y) \;\;\equiv\;\; \forall z \, r(x,y,z).
$$
#### Relating all of the above
Thus we can break apart the nested quantifiers into a sequence of formulas:

$$
p(x) \;\;\equiv\;\; \forall y \forall z \; [(x+y)+z = x+(y+z)]
\;\;\equiv\;\; \forall y \, q(x,y)
\;\;\equiv\;\; \forall y \forall z \, r(x,y,z).
$$

Finally, one conclude that:

- $\forall x \, p(x)$  
- $\forall x \forall y \, q(x,y)$  
- $\forall x \forall y \forall z \, r(x,y,z)$  

are all equivalent ways of expressing the same NT-formula.

## Summary
- One-at-a-time substitution can change later targets; simultaneous substitution prevents this.
- Formal simultaneous substitution is best defined using **fresh placeholder variables**.
- For formulas with quantifiers, require “$t_i$ is free for $x_i$ in $p$” to avoid variable capture.