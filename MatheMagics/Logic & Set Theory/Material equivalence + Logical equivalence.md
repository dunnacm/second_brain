---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Material equivalence vs. logical equivalence

### Material equivalence is connective-level (inside one formula)

In propositional logic, the biconditional connective $p\leftrightarrow q$ is interpreted as **material equivalence**.

- **Truth-condition**:  
  $p\leftrightarrow q$ is **true exactly when** $p$ and $q$ have the same truth value (both true or both false).

- **Equivalent forms**:
	$p\leftrightarrow q\ \Leftrightarrow\ (p\to q)\land(q\to p).$

	$p\leftrightarrow q\ \Leftrightarrow\ (p\land q)\ \lor\ (\neg p\land \neg q).$

So **material equivalence** is about how the truth value of the *single* compound formula $p\leftrightarrow q$ depends on the truth values of $p$ and $q$.

---

### Logical equivalence is meta-level (an equivalence relation between formulas)

**Logical equivalence** is defined using the semantic consequence relation $\models$:

$$p\Leftrightarrow\ q \quad \text{means} \quad \models\,(p\leftrightarrow q).$$

Interpretation: $p$ and $q$ are logically equivalent iff, under **every** valuation, $p$ and $q$ have the same truth value.

Equivalently:
- $p\models q$ and $q\models p$ (mutual consequence),
- the truth tables for $p$ and $q$ have identical final columns.

So **logical equivalence** is a statement about two formulas being interchangeable **in all valuations**, not about a single valuation or a single evaluation.

## The relationship

Logical equivalence is defined **using** material equivalence **plus** tautology:

1. Form the biconditional
   $$p\leftrightarrow q,$$
   where $\leftrightarrow$ is the **material equivalence** connective (truth-functional).

2. Require that biconditional to be a **tautology**:
   $$\models\,(p\leftrightarrow q).$$

So:

- **material equivalence** = an *object-language connective* ($\leftrightarrow$) inside formulas,
- **logical equivalence** = a *meta-language claim* that a particular biconditional is always true (a tautology).

## Common pitfall to avoid

It’s tempting to blur these and say:

> “$p$ is logically equivalent to $q$”  $\stackrel{?}{=}$  “$p\leftrightarrow q$”.

That’s wrong in general.

- $p\leftrightarrow q$ is just a formula; it can be true under some valuations and false under others.
- $p\equiv q$ means $\models(p\leftrightarrow q)$, i.e. the biconditional is true **under every valuation**.

Equivalently:
$$p\equiv q \quad \Leftrightarrow \quad p\models q \ \text{and}\ q\models p.$$

So:
- $\leftrightarrow$ is evaluated *within* a valuation;
- $\models$ (and logical equivalence) quantify over *all* valuations.