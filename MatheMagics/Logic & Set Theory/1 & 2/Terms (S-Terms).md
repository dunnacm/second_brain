---
down:
  - "[[Constituent parts (S-terms)]]"
  - "[[Substitution in terms]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definitions:

### Verbal:
An **S-term** is a *string* built from the *alphabet* of a *FOL* that denotes an _object_ in the *domain*. 
S-term is to be understood as "string term". One often simply, by convention, write using the word *term* without the S.

### Formal (inductive definition):

> [!note]+ **S-term formation (function application)**
> > [!warning]+ **IF**
> > - $t_0,\,t_1,\,\ldots,\,t_{n-1}$ are S-terms.
> > 	- Every **variable symbol(s)** (element of ==logic symbols==) is an **S-term**.
> > 	- Every **constant symbol(s)** (element of ==theory symbols==) is an **S-term**.
> > - $f$ is an $n$-ary function symbol (element of ==theory symbols==).
>
> > [!tip]+ **THEN**
> > $$
> > f(t_0,\,t_1,\,\ldots,\,t_{n-1}) \ \text{is an S-term}.
> > $$


## Representation:
### Designation:
Denote the collection of strings over **A** that are **S-terms** by ***TERMS (A)***

### Notation  
- The string $f\,t_0\,t_1\,\dots\,t_{n-1}$ is commonly written as $f(t_0,\,t_1,\,\dots,\,t_{n-1})$  (function-notation).  
- If $+$ is a binary function symbol, the string $+(x,y)$ is typically written as $x+y$.  
- If $\circ$ is a binary function symbol, the string $\circ(x,y)$ is typically written as $x\circ y$.
### Summary  
**Terms (S-terms)** are syntactic objects; under an interpretation (and assignment), they designate elements of the domain.


