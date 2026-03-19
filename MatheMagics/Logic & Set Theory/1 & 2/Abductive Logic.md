---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea (inference to the best explanation)
**Abductive logic** studies inference patterns where one moves from an observed fact to a **hypothesis that would explain it**.

Abduction is **not** truth-preserving: even if the premises are true, the explanatory hypothesis can still be false.

## Canonical schema
Given:
- an observation (often “surprising”) $E$, and
- background knowledge that $H \to E$,

infer (defeasibly):
- $H$.

In words:  
“If $H$ were true, $E$ would be expected; $E$ occurred; so $H$ is a plausible explanation.”

## Example
Observation: the lawn is wet ($E$).  
Background: if it rained, the lawn would be wet ($H\to E$).  
Abductive conclusion: therefore, it (probably) rained ($H$).

## What makes an abductive inference good or bad
Typical evaluation criteria:
- **Explanatory power:** does $H$ make $E$ likely/expected?
- **Simplicity / parsimony:** does $H$ avoid unnecessary complexity?
- **Consistency:** is $H$ compatible with other accepted information?
- **Rival explanations:** are there alternative hypotheses $H_1,H_2,\dots$ that explain $E$ as well or better?

## Contrast with deduction and induction
- **Deduction:** $H\to E$, $H$ ⟹ $E$ (guaranteed).
- **Induction:** many $S$ are $W$ ⟹ (probably/most) all $S$ are $W$ (generalization).
- **Abduction:** $H\to E$, $E$ ⟹ (plausibly) $H$ (explanation).