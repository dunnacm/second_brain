---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
To prove a **string** is a **propositional form**, one decomposes it to form a parsing tree and ensures the formation sequence of the propositional form 

## Examples
### Example 1:
#### Problem:
Identify if the following **string** is a propositional form:
$$\bigl(\mathtt{P}\to \mathtt{Q}\bigr)\land \bigl(\mathtt{R}\leftrightarrow \neg \mathtt{P}\bigr)$$
#### Solution:

- **Parsing tree**:
![[Pasted image 20260309173907.png|250]]
- The parsing tree yield the **formation sequence** of the propositional form:
$$\mathtt{P},\ \mathtt{Q},\ \mathtt{R},\ \neg \mathtt{P},\ \mathtt{P}\to \mathtt{Q},\ \mathtt{R}\leftrightarrow \neg \mathtt{P},\ \bigl(\mathtt{P}\to \mathtt{Q}\bigr)\land \bigl(\mathtt{R}\leftrightarrow \neg \mathtt{P}\bigr).$$
### Example 2
#### Problem:
Identify if the following **string** is a propositional form:
$$
\begin{aligned}
& \bigl[\mathtt{R}\leftrightarrow \bigl(\mathtt{P}\land \mathtt{Q}\bigr)\bigr]\land \bigl[\bigl(\mathtt{R}\leftrightarrow \mathtt{P}\bigr)\land \mathtt{Q}\bigr]
\end{aligned}
$$
#### Solution:
- **Parsing tree**:
![[Pasted image 20260309192858.png|500]]
- **Formation sequence**: $$
\mathtt{P},\ \mathtt{Q},\ \mathtt{R},\ (\mathtt{P}\land \mathtt{Q}),\ (\mathtt{R}\leftrightarrow \mathtt{P}),\ (\mathtt{R}\leftrightarrow (\mathtt{P}\land \mathtt{Q})),\ ((\mathtt{R}\leftrightarrow \mathtt{P})\land \mathtt{Q}),\ [\mathtt{R}\leftrightarrow (\mathtt{P}\land \mathtt{Q})]\land [(\mathtt{R}\leftrightarrow \mathtt{P})\land \mathtt{Q}].
$$