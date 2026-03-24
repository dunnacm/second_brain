---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core meaning
$$
\Gamma \nvdash \varphi
$$
means: **there does not exist** any formal proof (derivation) from premises $\Gamma$ whose last line is $\varphi$.

Equivalently: $\varphi$ is **not derivable from** $\Gamma$ in the chosen deductive system.

## What “not-derivable” claims
It is a **negative existential** statement:
- for every finite sequence of wffs you might present as a candidate derivation from $\Gamma$,
- at least one line will fail to be justified by the allowed syntactic moves,
- or the last line will not be $\varphi$.

## How one typically establishes $\Gamma \nvdash \varphi$
There are two common routes (depending on the metatheory available):

1) **Semantic countermodel route (soundness-based):**  
If the proof system is **sound** (i.e., $\Gamma\vdash\varphi \Rightarrow \Gamma\models\varphi$), then it is enough to show
$$
\Gamma \not\models \varphi,
$$
i.e., produce an interpretation/structure where all formulas in $\Gamma$ are true but $\varphi$ is false.  
Then $\Gamma \nvdash \varphi$ follows.

2) **Proof-theoretic route:**  
Argue directly that no derivation can reach $\varphi$ from $\Gamma$ under the permitted rules (often harder in practice unless you have a normal form theorem, cut-elimination, a derivation-height invariant, etc.).

## Empty-premise case
If $\Gamma=\varnothing$, then
$$
\nvdash \varphi
$$
means $\varphi$ is **not a theorem** of the system (no proof from no premises).

## What “not-derivable” is (and is not)
- **Syntactic**: it is about the nonexistence of proofs in the given calculus.
- It does **not** automatically mean “$\varphi$ is false” (truth is semantic, and depends on a structure/interpretation).
- It does **not** automatically mean “$\Gamma\models\varphi$ fails” unless you know the system is **complete** (i.e., $\Gamma\models\varphi \Rightarrow \Gamma\vdash\varphi$).