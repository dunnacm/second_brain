---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core meaning
$$
\Gamma \vdash \varphi
$$
means: **there exists** a formal proof (derivation/deduction) whose premises are drawn from $\Gamma$ and whose final line is $\varphi$.

Equivalently: $\varphi$ is **derivable from** $\Gamma$ in the chosen deductive system.

## Proof object (what one must be able to exhibit)
A derivation is typically a **finite sequence of wffs**
$$
\varphi_1,\varphi_2,\dots,\varphi_n,
\qquad\text{with }\varphi_n=\varphi,
$$
such that each line $\varphi_i$ is justified by an allowed syntactic move, e.g.:
- $\varphi_i\in\Gamma$ (premise), or
- $\varphi_i$ is an axiom instance (if axioms are used), or
- $\varphi_i$ follows from earlier lines by an inference rule, or
- $\varphi_i$ comes from earlier lines by an allowed replacement / equivalence / derived rule (if the system permits these).

## Empty-premise case (theorem)
If $\Gamma=\varnothing$, then
$$
\vdash \varphi
$$
means $\varphi$ is a **theorem**: it has a derivation with no premises.

## What “derivable” is (and is not)
- **Syntactic**: it depends only on the proof rules/axioms, not on meaning or truth in a structure.
- **Existential**: the mathematical content is “a proof object exists” (and can, in principle, be written down).

## Useful comparison (semantic consequence)
Do not conflate $\Gamma\vdash\varphi$ with $\Gamma\models\varphi$:
- $\vdash$ is **provability/derivability** (syntax).
- $\models$ is **semantic consequence** (truth in all relevant interpretations/structures).