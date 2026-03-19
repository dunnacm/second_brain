---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
$$
\begin{aligned}& \text{From Example, it was concluded that:} \\[5pt]& (1) \; \vdash p \to p \\[15pt]& \text{The following theorem is to be proved:} \\[5pt]& (2) \; \vdash \lnot q \to (p \land \lnot p) \to q \\[15pt]& \text{Combining (1), (2) (All theorems agree with each other. They won't affect one another)} \\[5pt]& (3) \; p \to p,\; \lnot q \to (p \land \lnot p) \; \vdash q \\\\[15pt]\end{aligned}
$$

$$
\begin{array}{lll}1. & p \to p & \text{Given} \\[5pt]2. & \lnot q \to (p \land \lnot p) & \text{Given} \\[5pt]3. & \lnot (p \land \lnot p) \to q & 2 \; \text{Contra} \\[5pt]4. & \lnot p \lor p \to q & 3 \; \text{DeM} \\[5pt]5. & (p \to p) \to q & 4 \; \text{Impl} \\[5pt]6. & q & 1,5 \; \text{MP}\end{array}
$$

---

[[Examples (indirect proof)]]