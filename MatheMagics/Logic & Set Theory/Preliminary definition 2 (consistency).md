---
down: "[[Consistency]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---

## Maximal consistency (definition 1.5.3)


### Introduction:

A sequence of propositional forms, such as **P -> Q**, **P**, **Q**, although consistent, has the property that there are propositional forms that can be added to the sequence so that the resulting list remains consistent. 

When the sequence can no longer take new forms and remain consistent, one has arrived at a sequence that satisfies the next definition.

---

### Verbal definition:

A set of propositional forms is **maximally consistent** iff:

- It is consistent (no contradictions)
- Every **p** in propositional form is an element of this set

---

### Formal definition:

$$
{\large
\begin{aligned}
& \textbf{IFF:} \\[5pt]

& \qquad \bullet\; \mathrm{Con}\!\left(\{ p_n \}_{n=0}^{N-1}\right) \\[5pt]

& \qquad \bullet\; \forall p \;\Big( p \in \{ p_n \}_{n=0}^{N-1} \;\lor\; \lnot p \in \{ p_n \}_{n=0}^{N-1} \Big) \\[10pt]

& \textbf{THEN:}\; \{ p_n \}_{n=0}^{N-1} \;\; \text{is} \; \textbf{maximally consistent.}
\end{aligned}
}
$$

