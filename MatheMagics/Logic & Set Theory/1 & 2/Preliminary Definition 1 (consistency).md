---
down: "[[Compactness thm.]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Consistency (definition 1.5.1)


### Verbal definition:
A logical system is consistent if no contraction is a theorem

---
### Formal definition:
 $$
\begin{aligned}
 & \textbf{IF:} \quad \{p_n\}_{n=0}^N \;\not\vdash\; (q \land \lnot q) \\[10pt]
 & \textbf{THEN:} \quad \operatorname{Con}\!\big(\{p_n\}_{n=0}^N\big) \\[10pt]
 & \textbf{ELSE:} \quad \{p_n\}_{n=0}^N \;\; \text{is inconsistent}
 \end{aligned}
$$

---

We have two goals:

- To show that propositional logic is consistent. 
- To discover properties of sequences of consistent propostional forms that will aid in proving other properties of propositional logic. 