---
down:
  - "[[Constituent parts (S-Formulas)]]"
  - "[[Substitution in Formulas]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definitions:

### Verbal:
An **S-formula** is a ==*string*== that denotes a *statement* (truth-valued once interpreted). It's the grammar used to represent propositional forms and predicates

### Formal (inductive definition):

> [!note]+ **Rule 1 (Equality formulas)**
> > [!warning]+ **IF**
> > - $t_0,\,t_1$ are terms (S-terms).
> 
> > [!tip]+ **THEN**
> > - $t_0=t_1$ is a formula (the equality symbol is an element of the ==logic symbols==).
> 
> > [!example]+ **Example**
> > - $x=y$ is a formula.

> [!note]+ **Rule 2 (Atomic S-formulas from relation symbols)**
> > [!warning]+ **IF**
> > - $t_0,\,t_1,\,\ldots,\,t_{n-1}$ are S-terms.
> > - $R$ is an $n$-ary relation symbol (an element of the ==theory symbols==).
> 
> > [!tip]+ **THEN**
> > - $R(t_0,\,t_1,\,\ldots,\,t_{n-1})$ is an S-formula.
> 
> > [!example]+ **Example**
> > - If $R$ is binary and $t_0=x$, $t_1=f(y)$, then $R(x,f(y))$ is an S-formula.

> [!note]+ **Rule 3 (S-formulas under propositional connectives)**
> > [!warning]+ **IF**
> > - $\varphi,\,\psi$ are formulas.
 >
> > [!tip]+ **THEN**
> > - The following are **S-formulas**:
> >   - $(\lnot\varphi)$
> >   - $(\varphi\land\psi)$
> >   - $(\varphi\lor\psi)$
> >   - $(\varphi\to\psi)$
> >   - $(\varphi\leftrightarrow\psi)$
 >
> > [!example]+ **Example**
> > - If $\varphi$ is $P(x)$ and $\psi$ is $Q(y)$, then $(P(x)\lor Q(y))$ is an S-formula.

> [!note]+ **Rule 4 (Quantified formulas)**
> > [!warning]+ **IF**
> > - $x$ is a variable.
> > - $\varphi$ is a formula.
 >
> > [!tip]+ **THEN**
> > - The following are formulas:
> >   - $\exists x\,\varphi$ (existential formula)
> >   - $\forall x\,\varphi$ (universal formula)
 >
> > [!example]+ **Example**
> > - $\forall x\,(P(x)\to Q(x))$ is a formula.

>[!quote]+ **Rule 5**  
>Nothing else is an **S-formula**.  

## Examples:
- *x* = *y* (atomic formula with equality)
- <(x,y) (binary relation)
- ∀x∃y (x+y=y+x)

Let $\mathtt{x}$ and $\mathtt{y}$ be variable symbols. Let $\mathtt{c}$ be a constant symbol.  
Let $\mathtt{f},\mathtt{g},\mathtt{h}$ be unary function symbols, and let $\mathtt{R}$ be a binary relation symbol from $\mathtt{S}$.

- $\mathtt{x=c}$
- $\mathtt{R\,c\,f\,y}\ \Leftrightarrow\ \mathtt{R(c,f(y))}$
- $\mathtt{\lnot(y=g\,c)}\ \Leftrightarrow\ \mathtt{\lnot\bigl(y=g(c)\bigr)}$
- $\mathtt{R\,x\,f\,x\to R\,f\,x\,x}\ \Leftrightarrow\ \mathtt{R(x,f(x))\to R(f(x),x)}$
- $\mathtt{\forall x\,\lnot(fx=f\,c)}\ \Leftrightarrow\ \mathtt{(\forall )\bigl[\,\lnot\bigl(f(x)=f(c)\bigr)\,\bigr]}$
- $\mathtt{\exists x\,\forall y\,\bigl(R\,f\,x\,g\,y\land R\,f\,x\,h\,y\bigr)}\ \Leftrightarrow\ \mathtt{(\exists x)\bigl[(\forall y)\bigl[\,R\bigl(f(x),g(y)\bigr)\land R\bigl(f(x),h(y)\bigr)\,\bigr]\bigr]}$

Some ST-formulas with their standard translations

- $\mathtt{\lnot\,\in x\{\}}\ \Leftrightarrow\ \mathtt{\sim(x\in\{\})}\ \Leftrightarrow\ \mathtt{x\notin\{\}}$
- $\mathtt{\forall x\,(\in x A\to \in x B)}\ \Leftrightarrow\ \mathtt{\forall x\,(x\in A\to x\in B)}$
- $\mathtt{\lnot\,\exists x\,\forall y\,(\in y x)}\ \Leftrightarrow\ \mathtt{\sim(\exists x)(\forall y)(y\in x)}$
- $\mathtt{x=y \ \ \lor \in y x \ \ \lor \in x y}\ \Leftrightarrow\ \mathtt{(x=y)\lor(y\in x)\lor(x\in y)}$ 
## Representation:
### Designation:
All of the formulas of the **first-order language** with **theory symbols S** is denoted by ***L(S)***.

### Notation:
 - The string $Rt_0, \, t_1, \, . . . , t_{n-1}$ is often written as $R(t_0, \, t_1, \, . . . , t_{n-1})$.
 - The string +*xy* is typically written as x + y and the string ∘*xy* is typically written x ∘ y

### Summary:
S-formulas are syntactic objects denoting *statements* about elements of the domain