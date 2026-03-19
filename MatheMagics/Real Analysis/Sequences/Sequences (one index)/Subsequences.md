---
down:
  - "[[Convergence (subsequences)]]"
  - "[[Divergence (subsequences)]]"
  - "[[Cauchy sequence, definition]]"
  - "[[Cauchy sequence with convergent subsequence]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
### Verbal definition:

A **subsequence** is formed by selecting certain elements of a sequence, **in order**, but not necessarily taking all of them.

- The **original order** of terms must be preserved.  
- Some terms may be **skipped**.  

From these conditions one concludes that a **subsequence** of ${s_n}$ is formed by selecting terms of ${s_n}$ according to an **increasing sequence of indices**, preserving their order but possibly skipping some.

---
### Formal definitions:
#### Formal definition 1:

Let $\{s_k\}_{k=1}^{\infty}$ be a sequence.

Let $\{k_n\}_{n=1}^{\infty}$ be a **strictly increasing sequence** of natural numbers:
$$
k_1 < k_2 < k_3 < \dotsb, \quad k_n \in \mathbb{N}.
$$

Then the sequence $\{t_n\}_{n=1}^{\infty}$ defined by  
$$
t_n := s_{k_n}
$$
is called a **subsequence** of $\{s_k\}$.
#### Formal definition 2:
$\exists\,\{k_n\}_{n\in\mathbb{N}}\subseteq\mathbb{N}\ \wedge \ \forall n\in\mathbb{N}\,[\,k_{n+1}>k_n\,].$ (i.e., there exists a strictly increasing index sequence $\{k_n\}$)
### Examples:
$$
\text{(1)}\quad 
\{s_k\}_{k=1}^{\infty}
= 
\Bigl\{\frac{1}{k^2}\Bigr\}_{k=1}^{\infty}
=
\Bigl\{1,\ \frac{1}{2^2},\ \frac{1}{3^2},\ \frac{1}{4^2},\ \ldots\Bigr\}
$$

Let's create a sequence with the even indices of eq.\,(1):  
$$
\text{(2)}\quad 
\{k_n\}_{n=1}^{\infty}
=
\{2n\}_{k=1}^{\infty}
=
\{2,4,6,\ldots\}
$$

Combining eqs.\,(1),(2) to define the subsequences:  
$$
\text{(3)}\quad 
\{t_n\}_{n=1}^{n}
=
\{s_{k_n}\}_{k=1}^{\infty}
=
\{s_{2n}\}_{n=1}^{\infty}
=
\Bigl\{\frac{1}{(2n)^2}\Bigr\}_{n=1}^{\infty}
=
\Bigl\{\frac{1}{2^2},\ \frac{1}{4^2},\ \ldots\Bigr\}
$$
