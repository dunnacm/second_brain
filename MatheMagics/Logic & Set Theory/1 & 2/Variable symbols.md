---
down:
  - "[[Variable symbols (what they do)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Variable symbols (FOL)

In **first-order logic (FOL)** we assume a stock of **variable symbols**, such as
$$x,\ y,\ z,\ x_0,\ x_1,\ x_2,\dots$$

Let the set of all variable symbols be denoted by $\mathtt{VAR}$.

A variable symbol is a **placeholder**: it may occur in **terms** and **formulas**, but it does not denote any fixed object by itself.  
(Assignments are what associate variables with elements of the domain.)

To evaluate a formula that contains variables we use:

- a **structure** (interpretation) $\mathcal{M}$, which has a **domain** $D$ and assigns meanings to the *nonlogical* symbols (predicate symbols, function symbols, constant symbols), and
- a **variable assignment** (often written $s$), which is a function
  $$s:\mathtt{VAR}\to D$$
  telling us which element of $D$ each variable is currently standing for.

### Example (assignment and an atomic formula)

Let the domain be
$$D=\{1,2,3\}.$$

Define an assignment $s:\mathtt{VAR}\to D$ by
$$
\begin{aligned}
s(x)&=2,\\
s(y)&=1,\\
s(z)&=3,\\
s(x_0)&=1,\\
s(x_1)&=3,\\
&\ \vdots
\end{aligned}
$$

Suppose the language contains a unary predicate symbol $P$, and $\mathcal{M}$ interprets $P$ as the subset
$$P^{\mathcal{M}}=\{2,3\}\subseteq D.$$

Then (with respect to $\mathcal{M}$ and the assignment $s$):
- $P(x)$ is **true**, because $s(x)=2\in P^{\mathcal{M}}$,
- $P(y)$ is **false**, because $s(y)=1\notin P^{\mathcal{M}}$.

### Free and bound occurrences

Quantifiers **bind** variables.

- In $\forall x\,\varphi$, the occurrences of $x$ inside the scope of $\forall x$ are **bound**.
- Any occurrence of a variable that is not bound by a quantifier is **free**.

A formula with **no free variables** is called a **sentence** (or **closed formula**).  
A sentence has a truth-value in a structure $\mathcal{M}$ that is **independent of the assignment** $s$ (that is, it has the same truth-value for every assignment).

### Contrast with propositional logic

Do not confuse **first-order variables** with **propositional variables**.

- In **propositional logic**, symbols like $\mathtt{p},\mathtt{q},\mathtt{r}$ stand for whole statements, and a valuation assigns truth-values:
  $$v:\mathtt{PropVar}\to\{\top,\bot\}.$$

- In **FOL**, symbols like $x,y,z$ stand for objects of the domain (via $s:\mathtt{VAR}\to D$).  
  Variables are not assigned truth-values.

### Variables vs constants (one more contrast)

A **constant symbol** (say $c$) is not a variable.  
Once a structure $\mathcal{M}$ assigns an element $c^{\mathcal{M}}\in D$, that element is what $c$ denotes throughout the structure.  
Variables can be reassigned by changing $s$.