---
down:
  - "[[Mathematical Logic]]"
  - "[[Other types of deductive logic]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Core idea
**Deductive logic** is about inferences where the premises _guarantee_ the conclusion: **if the premises are true, the conclusion cannot be false**.

## Validities
### Validity (semantic)
An argument is **valid** if there is no case in which all premises are true and the conclusion is false.

Using semantic consequence:
$$
\Gamma \models \varphi
$$
means: in every interpretation/structure in which all formulas in $\Gamma$ are true, $\varphi$ is also true.

### Derivability (syntactic)
A conclusion is **derivable** from premises when there exists a formal proof:
$$
\Gamma \vdash \varphi.
$$
Here the “output” is a **proof object** (a finite derivation), or the fact that such a derivation exists.

## Soundness and completeness (linking $\vdash$ and $\models$)
For a given deductive system:
- **Soundness:**  
  $$\Gamma\vdash\varphi\ \Rightarrow\ \Gamma\models\varphi.$$
- **Completeness:**  
  $$\Gamma\models\varphi\ \Rightarrow\ \Gamma\vdash\varphi.$$

When both hold, syntactic provability matches semantic validity.

## Example:
$$
$$
$$ 
\begin{aligned}
& \textbf{Assignments:}\\[18pt]
\mathtt{(1)} \quad & \mathtt{G}(\mathtt{x})\;:=\;\text{``}x\ \text{is a geometer''}.\\[12pt]
\mathtt{(2)} \quad & \mathtt{M}(\mathtt{x})\;:=\;\text{``}x\ \text{is a mathematician''}.\\[22pt]
& \textbf{From English to FOL Formulas:}\\[18pt]
& \text{``All geometers are mathematicians''}\; \mapsto \;\forall \mathtt{x}\,\bigl(\mathtt{G}(\mathtt{x})\to \mathtt{M}(\mathtt{x})\bigr).\\[12pt]
& \text{``Euclid is a geometer''}\; \mapsto \;\mathtt{G}(\hat{\mathtt{x}}).\\[22pt]
& \textbf{Reasoning:}\\[18pt]
& \text{Given:}\quad \mathtt{(3)}\quad \forall \mathtt{x}\,\bigl(\mathtt{G}(\mathtt{x})\to \mathtt{M}(\mathtt{x})\bigr).\\[12pt]
& \phantom{\text{Given:}\quad \mathtt{(3)}\quad}\Rightarrow \mathtt{(4)}\quad \mathtt{G}(\hat{\mathtt{x}})\to \mathtt{M}(\hat{\mathtt{x}}).\\[18pt]
& \text{Given:}\quad \mathtt{(5)}\quad \mathtt{G}(\hat{\mathtt{x}}).\\[18pt]
& \text{From (4), (5) by MP:}\quad \mathtt{(6)}\quad
\begin{array}{c}
\mathtt{G}(\hat{\mathtt{x}})\to \mathtt{M}(\hat{\mathtt{x}})\\
\mathtt{G}(\hat{\mathtt{x}})\\
\hline
\therefore\ \mathtt{M}(\hat{\mathtt{x}})
\end{array}
\end{aligned}
$$


## Contrast with inductive logic
- **Deductive:** ampliation-free; conclusions are guaranteed by premises (given correct rules).
- **Inductive:** ampliative; conclusions go beyond premises and are supported only to a degree (e.g., “probably”).
  
