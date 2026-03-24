---
down: "[[Consistency]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---

$$
{\large
\begin{aligned}
& \textbf{IFF: } \{ p_i \}_{i=0}^{N-1} \text{ are propositional forms} \\[10pt]

& \textbf{THEN:} \\[5pt]

& \qquad 1.\; \mathrm{Con}\!\left(\{ p_i \}_{i=0}^{N-1}\right) \\[5pt]

& \qquad 2.\; \mathrm{Con}\!\left(\{ p_{i_k} \}_{k=0}^{n-1}\right) \\[5pt]

& \qquad 3.\; (\exists p)\ \Big[\, \{ p_i \}_{i=0}^{N-1} \ \nvdash\ p \,\Big]
\end{aligned}
}
$$

>[!Explanation]
>
>1. The (main) sequence of propositional forms is consistent (no contradiction is a thm.)
>2. Every finite subsequence of the (main) sequence is consistent.
>3. There's a propositional form _p_ that can't be proven with the (main) sequence of propositional forms[^1]

---
[^1]: [Pending proof](M/Pending/Proof thm. 1.5.2.md)
