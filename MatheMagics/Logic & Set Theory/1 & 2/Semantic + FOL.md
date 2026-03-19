---
down:
  - "[[Assignment (FOL)]]"
  - "[[Proposition]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
By themselves, wffs are purely **syntactic** strings, so they do not have an (assignment-independent) truth value.  
Once an **interpretation/structure** $\mathcal{M}$ is given (a domain $D$ + meanings for the **theory symbols**), and—when needed—a **variable assignment** $s$ (mapping variables to elements of $D$), a wff can be understood as a formula about objects in the domain.

- If it has free variables $\to$ it can be evaluated as true/false **only relative to** an assignment $s$; equivalently, it denotes a *predicate/relation* on $D$ (an open formula).
- If all variables are bound $\to$ it denotes a *sentence* (closed formula), whose truth value is determined by $\mathcal{M}$ alone (true or false in $\mathcal{M}$).
