---
down:
  - "[[Prenex normal form]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:
### **Verbal**:
- #### *Negation of universal quantifier*: 
	- Proposition: *all P are Q*
	- QN: *some P are not Q*
		**Example**:
		- **Proposition:**  *All rectangles are squares.*
			 This sentence is false because there exists a rectangle where one side is twice the length of the adjacent side.
		- **Quantifier Negation:**  *Some rectangle is not a square.*
- #### *Negation of of existential quantifier*:
	- Proposition: *some P are Q*
	- QN: *all P are not Q*
		**Example**:
		- **Proposition:**  *Some rectangles are round*
			 This sentence is false because there are no round rectangles
		- **Quantifier Negation:**  *all rectangles are not round*
### **Formal**:

>[!note] **Quantifier Negation Laws**
>
>>[!warning] **IF**
>> - $\mathbf{S}$ (theory symbols)
>> - *p* is an $\mathbf{S}$-**formula** 
>
>>[!tip] **THEN**
>> - $\lnot \forall x \, p \;\;\Leftrightarrow\;\; \exists x \, \lnot p$
>> - $\lnot \exists x \, p \;\;\Leftrightarrow\;\; \forall x \, \lnot p$

> [!quote]+ **Note**:
> - **Positive form**: Whenever a formula of the form $\forall x \, p$ or $\exists x \, p$ is negated (to make it easier to read), the final form should:
> 	◦ not have a negation immediately to the left of any quantifier (i.e., $\lnot \forall x \, p$ and $\lnot \exists x \, p$)
>	◦ After using the replacement rules, the negation should be as far into the formula *p* as possible

---
## Illustrations:
### Example 1:
The original statement:  
$$(1) \quad \ \forall x \,(p \land q)$$

Negation of (1) in *positive form*:

$$
\begin{aligned}
(2) \quad & \lnot \forall x \,(p \land q) &\Leftrightarrow&\; \exists x \,\lnot (p \land q) \\[6pt]
&&\Leftrightarrow&\; \exists x \,(\lnot p \lor \lnot q)
\end{aligned}
$$
### Example 2:
Original statement:
$$
\begin{aligned}
(1) \quad & \forall x\, \exists y\;[\, p(x) \to q(y) \,]
\end{aligned}
$$


Negation in positive form
$$
\begin{aligned}
(2) \quad & \neg\, \forall x\, \exists y\;[\, p(x) \to q(y) \,] 
&\Leftrightarrow&\; \exists x\, \neg\, \exists y\;[\, p(x) \to q(y) \,] \\\\[6pt]
&&\Leftrightarrow&\; \exists x\, \forall y\, \neg\,[\, p(x) \to q(y) \,] \\\\[6pt]
&&\Leftrightarrow&\; \exists x\, \forall y\, \neg\,[\, \neg p(x) \lor q(y) \,] \\\\[6pt]
&&\Leftrightarrow&\; \exists x\, \forall y\, [\, p(x) \land \neg q(y) \,]
\end{aligned}
$$


