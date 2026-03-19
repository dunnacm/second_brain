---
down:
  - "[[Completeness ⇒ Supremum]]"
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Preface:
### Motivating example:
$$
\begin{aligned}
S \,:=\, \{\, x\in\mathbb{Q} : x^{2}<2 \,\}
\quad \Leftrightarrow \quad
S = \{\, x\in\mathbb{Q} : (x-\sqrt{2})\cdot(x+\sqrt{2})<0 \,\}.
\end{aligned}
$$

From proof $\sqrt{2}\notin\mathbb{Q}$ ([[√2 ∉ ℚ]]), it can be concluded that $\exists x\in(-\sqrt{2},\sqrt{2})$ with $x\notin\mathbb{Q}$.
This means that there are gaps between rational numbers in this interval.

![[image_white_bg_v2.png]]

---
## Significance:
$S$ is nonempty and bounded above *inside $\mathbb{Q}$*, yet $\sup_{\mathbb{Q}} S$ does *not* exist. This failure of the “least upper bound” property is exactly the *incompleteness* of $\mathbb{Q}$. By adjoining limits like $\sqrt{2}$ (and all other “missing” limits) we obtain $\mathbb{R}$, where the *completeness property* holds: every nonempty, bounded‐above set has a supremum (here, $\sqrt{2}$).
This is why the **completeness property** implies the ****supremum property***.





