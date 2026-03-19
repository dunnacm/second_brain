---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Material implication vs. logical implication

### Material implication is connective-level (inside one formula)

In propositional logic, the conditional connective $p\to q$ is interpreted as **material implication**.

- **Truth-condition**:
	$p\to q$ is **false exactly when** $p$ is true and $q$ is false.

- **Equivalent form**:
	$p\to q\ \Leftrightarrow\ \neg(p\land \neg q).$

So **material implication** is about how the truth value of the *single* compound formula $p\to q$ depends on the truth values of $p$ and $q$. 

### Logical implication is meta-level (a consequence relation between formulas)

**Logical implication / semantic consequence** is defined using the consequence symbol $\models$:

$$p_0,p_1,\dots,p_{n-1}\ \models\ q
\quad \Leftrightarrow \quad
\models\ \bigl((p_0\land p_1\land\cdots\land p_{n-1})\to q\bigr).$$

Interpretation: $p_0,\dots,p_{n-1}\models q$ means:

> In **every** valuation where all premises $p_0,\dots,p_{n-1}$ are true, the conclusion $q$ is also true.

So **logical implication** is a statement about an **argument form** (premises ⟹ conclusion), not about the truth table of a single connective.

## The relationship 

Logical implication is defined **using** material implication **plus** tautology:

1. Form the conditional
   $$\bigl(p_0\land\cdots\land p_{n-1}\bigr)\to q,$$
   where $\to$ is the **material implication** connective (truth-functional).

2. Require that conditional to be a **tautology**:
   $$\models\ \bigl((p_0\land\cdots\land p_{n-1})\to q\bigr).$$

So:

- **material implication** = an *object-language connective* ($\to$) inside formulas,
- **logical implication** = a *meta-language consequence relation* ($\models$) defined by saying a certain material implication is always true (a tautology). 

## Common pitfall to avoid

It’s tempting to identify these:

> “$p$ logically implies $q$”  $\stackrel{?}{=}$  “$p\to q$”.

That is **not** correct in general.

- $p\to q$ is just a formula; it can be true under some valuations and false under others.
- $p\models q$ is a stronger claim: there is **no** valuation with $v(p)=T$ and $v(q)=F$.

Equivalently:
$$p\models q \quad \Leftrightarrow \quad \models\,(p\to q).$$

So: 
- $\models$ talks about *all valuations*; 
- $\to$ talks about the truth value *under one valuation*. 