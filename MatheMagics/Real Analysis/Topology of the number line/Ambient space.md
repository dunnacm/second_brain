---
down:
  - "[[Point classifications (relative to an ambient set 𝑋)]]"
tags:
  - mathemagics/real_analysis
  - mathemagics/topology
---
## Definitions:
### Verbal definition 

The **ambient space** is the “big set” (together with its notion of distance or neighborhoods) in which all the sets we study live. In real analysis, we usually take the ambient space to be $\mathbb{R}$ with the usual metric $d(x,y)=|x-y|$. When we write objects like
$$
\operatorname{int}_{\mathbb{R}}(A),\quad \overline{A}^{\,\mathbb{R}},\quad \partial_{\mathbb{R}} A,
$$
the subscript $\mathbb{R}$ indicates that interior, closure, and boundary are being computed **relative to $\mathbb{R}$ as the ambient space**.

---
## Conventions and notation:
### Ambient space convention in these notes

The *ambient space* is **always** $\mathbb{R}$ with the standard metric, unless explicitly stated otherwise. Therefore:
$$
\operatorname{int}(X)\ \text{or}\ X^\circ \quad\text{instead of}\quad \operatorname{int}_{\mathbb{R}}(X),
$$
and similarly
$$
\overline{U}\ \text{instead of}\ \overline{U}^{\,\mathbb{R}}, 
\quad
\partial U\ \text{instead of}\ \partial_{\mathbb{R}} U.
$$
Whenever a different ambient space is used (for example, $\mathbb{Q}$ with the subspace topology), I will make that explicit by writing subscripts such as $\operatorname{int}_{\mathbb{Q}}(U)$.

**Convention**:  
Many authors prefer **$X$** for ambient spaces. $x$ for a generic point of $\mathbb{R}$ 
