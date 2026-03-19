---
down:
  - "[[Derivable]]"
  - "[[Not derivable]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition:

For **syntactic validity** (derivability), the “output” is not a truth value; it is the existence (and, when exhibited, the explicit data) of a **proof object**.

Concretely, given premises $\Gamma$ and conclusion $\varphi$:

## Derivability judgment
- The judgment $\Gamma \vdash \varphi$ holds **iff** there exists a **formal deduction** (derivation/proof) of $\varphi$ from $\Gamma$.

Equivalently:
- $\Gamma \vdash \varphi$ means **there exists** a finite derivation whose last line is $\varphi$.
- $\Gamma \nvdash \varphi$ means **no such** finite derivation exists.

## What a proof object is (typical presentation)
A formal deduction is a **finite sequence of wffs** (often displayed as numbered lines)
$$
\varphi_1,\varphi_2,\dots,\varphi_n,
\qquad\text{with }\varphi_n=\varphi,
$$
such that for each $i\in\{1,\dots,n\}$, the line $\varphi_i$ is justified by one of the allowed syntactic moves of the proof system, e.g.:
1. $\varphi_i\in\Gamma$ (a **premise**), or
2. $\varphi_i$ is an **axiom instance** (if the system is axiom-based), or
3. $\varphi_i$ follows from earlier lines by an **inference rule** (e.g., modus ponens), or
4. $\varphi_i$ is obtained from earlier lines by an allowed **replacement / equivalence / derived rule** (depending on the system’s rule set).

*(The exact allowed justifications depend on the chosen deductive system.)*

## Theorem (empty-premise case)
Special case: if $\Gamma=\varnothing$, then
$$
\vdash \varphi
$$
holds exactly when $\varphi$ is a **theorem** of the system, i.e., when there exists a derivation of $\varphi$ with no premises.

## Remarks on “output”
- In practice, one may treat the “output” of a derivability question as a boolean (“derivable / not derivable”).  
- Mathematically, the content is **existential**: either there **exists** a proof object (and you can exhibit it), or there does not.