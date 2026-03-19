---
down:
  - "[[Types of inductive logic]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Etymology
The adjective **inductive** traces back to **Late Latin** _**inductivus**_, meaning “serving to induce or infer,” built from **inducere** — _in_ (“into”) + _ducere_ (“to lead”).

## Core idea (ampliative inference)
**Inductive logic** studies inference patterns where one moves from **many observed instances** to a **more general claim**.

Unlike deductive validity, the conclusion is not guaranteed by the premises; it is supported to some **degree** (e.g., plausible, probable, well-confirmed).

## Canonical schema 
Let:
- $a_1,\dots,a_n$ be **names for particular observed cases** (individuals you actually examined),
- $W(x)$ be the **property** you checked (e.g., “$x$ is white”),
- $S(x)$ be the **target class** you want to generalize about (e.g., “$x$ is a swan”).

### Observations
From observed instances:
$$
W(a_1),\ W(a_2),\ \dots,\ W(a_n).
$$
This reads: “Each observed case $a_i$ has property $C$.”

*(Often it is also understood that the $a_i$ are in the target class, i.e. $S(a_i)$ holds for each $i$; this is usually suppressed for brevity.)*

### Inductive generalization (with uncertainty)
Infer a universal-looking claim **with an uncertainty marker**:
$$
\forall^{\operatorname{most}} x\,\bigl(S(x)\to W(x)\bigr) \quad (\text{e.g.,} \quad \forall^{\ge 0.95} x\,\bigl(S(x)\to W(x)\bigr))
$$

This reads: “Probably, every $S$ is $C$.”

The word “Probably” (or “Likely”, “With high confidence”, etc.) is essential:  from the observations alone one cannot *deductively* derive the universal statement, because an unobserved counterexample might exist.

## Example
Let $S(x)$ mean “$x$ is a swan” and $W(x)$ mean “$x$ is white.”

Observations:
- All observed swans are white.

Inductive conclusion:
- Therefore, **probably** all swans are white.

## Key contrast with deductive logic
- **Deduction:** truth-preserving. If the premises are true, the conclusion must be true.
- **Induction:** ampliative. The premises can be true while the general conclusion is false (one counterexample suffices).

## What makes an inductive inference stronger or weaker (typical background conditions)
Inductive support depends on assumptions that pure logical form doesn’t encode, such as:
- **Representativeness:** the observed $a_i$ are not a biased sample of the $S$’s.
- **Projectability/stability:** the property $W$ is expected to be stable across $S$’s (not a coincidence).
- **Amount/diversity of evidence:** larger and more varied samples usually give stronger support.
- **No known counterexamples:** known exceptions sharply reduce support.

## Typical “outputs”
Inductive reasoning is often represented as producing:
- a **probability / degree of support** for the generalization, or
- a **ranking of hypotheses** by plausibility,
rather than a proof object.