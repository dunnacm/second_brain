---
down:
  - "[[Tail-bound criterion]]"
  - "[[Cauchy ⇒ Bounded]]"
  - "[[Cauchy sequence with convergent subsequence]]"
  - "[[Convergent ⇒ Cauchy]]"
tags:
  - mathemagics/real_analysis
---
## Introduction
### Need for the definition of a Cauchy sequence
Sometimes it is possible to establish that a sequence is convergent without actually finding its limit. 
It will be shown that a sequence is convergent **iff** its terms are ultimately close to one another, even if they're not consecutive

## Definition:
### Verbal:
A sequence is **Cauchy** if, no matter how tiny a tolerance ε\varepsilonε you choose, you can go far enough out in the sequence (past some index NNN) so that **every pair of later terms** lies within ε\varepsilonε of each other. In other words: in the tail, the terms crowd together as tightly as you wish; the sequence “stabilizes internally,” even before you know what (if anything) it converges to.
### Formal:

> [!note]+ **Cauchy Sequence — Characterization**
> > [!warning]+ **IF**
> > $$\forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall m,n\in\mathbb{N}\ \big[\, (m\ge N \land n\ge N)\ \Rightarrow\ |s_m-s_n|<\varepsilon \,\big],$$
>
> > [!tip]+ **THEN**
> > $$\{s_n\}\ \text{is Cauchy.}$$

