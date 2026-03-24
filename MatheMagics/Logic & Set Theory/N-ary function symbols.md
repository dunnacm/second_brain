---
up:
down:
  - "[[Terms (S-Terms)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
An **$n$-ary function symbol** $f$ is a **theory symbol** in FOL intended to denote an operation that takes **$n$ elements from the domain** and returns **one subject in the domain**.

Formally, in a structure $\mathcal{M}$ with domain $D$, an $n$-ary function symbol is interpreted as a function
$$
f^{\mathcal{M}}:D^n\to D.
$$

## Formation rule (terms)
If $t_1,\dots,t_n$ are terms, then
$$
f(t_1,\dots,t_n)
$$
is a **term**.  
So function symbols are exactly what let us build **new terms** from existing ones.

## Examples (corrected)
- **Unary function symbol:** $\mathtt{succ}(x)$ (successor), or $\mathtt{neg}(x)$ (additive inverse).  
- **Binary function symbol:** $+(x,y)$ (addition), or $\times(x,y)$ (multiplication).  
- **Ternary function symbol:** $\mathtt{if}(p,q,r)$ (read: “if $p$ then $q$ else $r$”) *in a language where these are terms of the right sort.*

*(Note: $\cos$ is typically treated as a unary function symbol only if your language is built to talk about real analysis; otherwise it is not part of the default logical vocabulary.)*

## Important contrast: function symbols vs predicate symbols
- A **function symbol** produces a **term** (object-valued output).
- A **predicate symbol** produces a **formula** (truth-valued output).

## Summary
$n$-ary function symbols: interpreted as functions $D^n\to D$ → applied to $n$ terms → yield a term.