---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
**Substitution** in propositional logic (PL) is the process of **==uniformly== replacing propositional variables in a propositional form by propositional forms**, producing a new propositional form.

This process is done uniformly, meaning the replacement is governed by a single substitution map $\sigma$ applied consistently throughout the formula. Concretely, you choose a rule such as
$$
\sigma(P)=(R\land S),\qquad \sigma(Q)=T,\qquad \sigma(\text{anything else})=\text{itself},
$$
and then you build the new formula $\sigma(\varphi)$ by replacing **every occurrence** of each variable $P$ by the same formula $\sigma(P)$, every occurrence of $Q$ by $\sigma(Q)$, and leaving all other variables unchanged. The key point is that the replacement does **not** depend on where the variable occurs (left/right of $\to$, inside a negation, nested deep in parentheses, etc.). If $P$ occurs five times, all five occurrences are replaced identically—otherwise you are not applying a well-defined substitution.

### Example
- Start with: $P\to Q$
- Substitute: $P := (R\wedge S)$
- Result: $(R\wedge S)\to Q$

*(If $P$ occurred more than once, each occurrence would be replaced.)*

## Symbolization (PL)
Let:
- $P :=$ “Squares are rectangles.”
- $Q :=$ “Squares are quadrilaterals.”

Then the sentence  
“If squares are rectangles, then squares are quadrilaterals”  
is symbolized by the propositional form $P\to Q.$