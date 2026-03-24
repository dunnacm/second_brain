---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
### Verbal:
Consider the sentence *all multiples of 4 are even*. 
This implies, for instance, that 8, 100 and -16 are even. 
To generalize this reasoning to **S-formulas** means that whenever one has $\forall x p(x)$, one also has
- $p(a)$, where *a* might be:
	◦ a **constant** symbol (such as 8, 100 and -16) or
	◦ a **randomly chosen constant** symbol
### Formal:
> [!note] **Inference Rule 2.3.4 (Universal Instantiation)**
>
> > [!warning] **IF**
> > $p(x)$ is an $\mathcal{S}$-formula
>
> > [!tip] **THEN**
> > $(\forall a \in \overline{S})\,[\,(\forall x\, p(x)) \Rightarrow p(a)\,]$

>[!quote] Notes:
>Two observations about UI
>> - Since the resulting formula is to be part of a proof, the substitution must yield a sentence, so *a* must be a **constant symbol**. 
>> - The notation *p(x)* is used to represent the formula instead of *p* because $(\forall x\, p(x))$ will be part of a proof, which means, again, that it must be a sentence. If the formula *p* had free variables other than x, then $\forall x\, p$ would not be a **sentence** and not suitable for a proof

## Examples:
- $\forall x\,[\, p(x)\!\to\! q(x)\,] \Rightarrow p(a)\!\to\! q(a)$
- $\forall x\,[\, p(x)\lor \forall y\, q(y)\,] \Rightarrow p(a)\lor \forall y\, q(y)$
- $\forall x\,\forall y\,[\, q(x)\lor r(y)\,] \Rightarrow \forall y\,[\, q(a)\lor r(y)\,]$
- $\forall y\,[\, q(a)\lor r(y)\,] \Rightarrow q(a)\land r(a)$
- $\forall y\,[\, q(a)\lor r(y)\,] \Rightarrow q(a)\land r(b)$
