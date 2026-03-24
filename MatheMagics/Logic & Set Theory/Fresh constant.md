---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
> [!note] **Definition — Fresh constant symbol**
>
> > [!warning] **IF**
> > - $p(x)$ is an $\mathcal{S}$-**formula**.
> > - A constant symbol $a$ **does not occur earlier** anywhere in the proof (not in premises, prior lines, or undischarged assumptions).
> > - $a$ is introduced **at this step** solely to instantiate a quantified claim (e.g., by **EI**: $\exists x\,p(x)\;\Rightarrow\;p(\hat a)$).
>
> > [!tip] **THEN**
> > - $a$ is a **fresh** (i.e., **particular**) constant symbol — often written $\hat a$.
>
>- A “fresh” constant serves as a temporary **witness** for an existential claim. 
> - Its freshness (= no prior occurrence) prevents 
>> - illegitimate generalization and 
>> - preserves soundness of **EI**.

> [!warning] **Restriciton**:
>  No **UG** may be applied to formulas containing particular/fresh constants.

