---
down:
  - "[[Proposition]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
# Standard FOL semantics: $\mathcal{M},s\models\varphi$ + translation to $\mathfrak{A},I$-notation

## Purpose
A **structure** is the semantic object that tells you:
- what the **nonlogical symbols** mean, and
- what objects the **variables range over**,

so that formulas can be evaluated as true or false.

> Caution (terminology): different texts use “structure / interpretation / model” differently.  
> In this note, “structure” is the underlying domain + symbol-meanings; “assignment” is for variables; “model” may mean either the structure alone or the structure together with an assignment, depending on context.

---

## 1) Standard structure $\mathcal{M}$
Fix a first-order language with nonlogical (theory) symbols:
- constant symbols $c,d,\dots$
- $n$-ary function symbols $f,g,\dots$
- $n$-ary predicate/relation symbols $P,Q,R,\dots$

A **structure** is typically written as
$$
\mathcal{M}=\bigl(D,\ (c^{\mathcal{M}})_{c},\ (f^{\mathcal{M}})_{f},\ (P^{\mathcal{M}})_{P}\bigr),
$$
where:
- $D\neq\varnothing$ is the **domain**.
- each constant symbol $c$ is interpreted as an element $c^{\mathcal{M}}\in D$,
- each $n$-ary function symbol $f$ is interpreted as a function $f^{\mathcal{M}}:D^n\to D$,
- each $n$-ary predicate symbol $P$ is interpreted as a relation $P^{\mathcal{M}}\subseteq D^n$.

Logical symbols ($\lnot,\land,\lor,\to,\leftrightarrow,\forall,\exists$) are **not** interpreted this way; their meanings are fixed by logic.

---

## 2) Variable assignment (for open formulas)
To evaluate formulas with free variables, choose a **variable assignment**
$$
s:\mathtt{VAR}\to D.
$$

If $x$ is a variable and $d\in D$, write $s[x\mapsto d]$ for the assignment that agrees with $s$ on all variables except it sends $x$ to $d$.

---

## 3) Interpretation of terms
Given $\mathcal{M}$ and $s$, each term $t$ denotes an element of $D$, written $t^{\mathcal{M},s}$, defined recursively:
- if $t$ is a variable $x$, then $x^{\mathcal{M},s}=s(x)$;
- if $t$ is a constant $c$, then $c^{\mathcal{M},s}=c^{\mathcal{M}}$;
- if $t=f(t_1,\dots,t_n)$, then
$$
f(t_1,\dots,t_n)^{\mathcal{M},s}
=
f^{\mathcal{M}}\bigl(t_1^{\mathcal{M},s},\dots,t_n^{\mathcal{M},s}\bigr).
$$

---

## 4) Truth / satisfaction
Truth is defined by the **satisfaction relation**
$$
\mathcal{M},s\models \varphi
$$
meaning “$\varphi$ is true in $\mathcal{M}$ under assignment $s$.”

### Atomic cases
- **Atomic predicate:**
$$
\mathcal{M},s\models P(t_1,\dots,t_n)
\ \Leftrightarrow\
\bigl(t_1^{\mathcal{M},s},\dots,t_n^{\mathcal{M},s}\bigr)\in P^{\mathcal{M}}.
$$
- **Equality (if included):**
$$
\mathcal{M},s\models (t_1=t_2)
\ \Leftrightarrow\
t_1^{\mathcal{M},s}=t_2^{\mathcal{M},s}.
$$

### Connectives
Evaluated by the usual truth-conditions for $\lnot,\land,\lor,\to,\leftrightarrow$.

### Quantifiers
Quantifiers range over the domain $D$:
$$
\mathcal{M},s\models \forall x\,\varphi
\ \Leftrightarrow\
\text{for all }d\in D,\ \mathcal{M},s[x\mapsto d]\models \varphi,
$$
$$
\mathcal{M},s\models \exists x\,\varphi
\ \Leftrightarrow\
\text{for some }d\in D,\ \mathcal{M},s[x\mapsto d]\models \varphi.
$$

---

## 5) Sentences (closed formulas)
If $\varphi$ is a **sentence** (no free variables), its truth in $\mathcal{M}$ does **not** depend on $s$. One writes:
$$
\mathcal{M}\models \varphi.
$$

---

## Summary (standard notation)
- $\mathcal{M}$ fixes the domain $D$ and interprets all theory symbols.
- $s$ assigns domain elements to variables.
- Terms denote elements of $D$ via $(\mathcal{M},s)$.
- Formulas are evaluated via $\mathcal{M},s\models\varphi$; sentences via $\mathcal{M}\models\varphi$.

---

# Translation dictionary to $\mathfrak{A}=(A,a)$ and $I$ notation (same semantics, different packaging)

## Objects
- Structure:
$$
\mathcal{M}\ \leftrightarrow\ \mathfrak{A}=(A,a)
\qquad\text{with }A=D.
$$
- Variable assignment vs interpretation:
  - $s:\mathtt{VAR}\to D$ corresponds to the values of variables inside an interpretation $I$,
  - with $I:\mathrm{TERMS}(\mathfrak{A})\to A$ extending variable values to all terms by recursion.
- “Model” (in the sense structure + assignment/interpretation):
$$
(\mathcal{M},s)\ \leftrightarrow\ (\mathfrak{A},I).
$$

## Symbol interpretation
- Constant:
$$
c^{\mathcal{M}} \ \leftrightarrow\ a(c).
$$
- Relation symbol:
$$
P^{\mathcal{M}} \ \leftrightarrow\ a(P).
$$
- Function symbol:
$$
f^{\mathcal{M}} \ \leftrightarrow\ a(f).
$$

## Term denotation
Standard term value $t^{\mathcal{M},s}$ corresponds to $I(t)$:
$$
t^{\mathcal{M},s}\ \leftrightarrow\ I(t).
$$
(Choosing $s$ determines $I$ uniquely by recursion; conversely, $I$ restricted to variables is $s$.)

## Satisfaction notation
$$
\mathcal{M},s\models\varphi
\ \leftrightarrow\
\mathfrak{A}\vDash \varphi[I].
$$

For sentences $\varphi$:
$$
\mathcal{M}\models\varphi
\ \leftrightarrow\
\mathfrak{A}\vDash \varphi
\quad\text{(i.e., }\mathfrak{A}\vDash \varphi[I]\text{ for all }I\text{).}
$$