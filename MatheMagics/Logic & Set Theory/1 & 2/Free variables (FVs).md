---
down:
  - "[[(S-Sentence) or (Closed Formula) or (Sentence)]]"
  - "[[Set of FVs]]"
  - "[[Parametrizing a formula by its FVs]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
> [!note]+ **2.2.5**
> > [!warning]+ **IF**
> > - $p$ is an **S-formula**.
> > - $p$ has a variable with a **free occurrence**.
>
> > [!tip]+ **THEN**
> > That variable is **free**.

### Example:
$R(x,y,c) \;\to\; \exists x (f(y) = c)$  

- $x$ has a **free occurrence** in $R(x,y,c)$  
- $x$ has a **bound occurrence** in $\exists x (f(y) = c)$  
- $y$ has a **free occurrence** in $R(x,y,c)$  
- $y$ has a **free occurrence** in $\exists x (f(y) = c)$  
- $x$ and $y$ are **free variables** of the formula $R(x,y,c) \to \exists x (f(y) = c)$  
