---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
Find the truth tables of the following propositional forms

## Example 1: $(\mathtt{P}\leftrightarrow \mathtt{Q})\lor(\mathtt{R}\to \mathtt{P})$

### Step 1 (Decompose through parsing tree)

$$
(\mathtt{P}\leftrightarrow \mathtt{Q})\lor(\mathtt{R}\to \mathtt{P})
$$

![[Pasted image 20260323045654.png|280]]

### Step 2 (Formation sequence)

$$
\mathtt{P},\ \mathtt{Q},\ \mathtt{R},\ \mathtt{P}\leftrightarrow\mathtt{Q},\ \mathtt{R}\to\mathtt{P},\ (\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P})
$$

### Step 3 (Valuation of propositional forms in formation sequence through truth tables)

| $\upnu(\mathtt{P})$ | $\upnu(\mathtt{Q})$ | $\upnu(\mathtt{R})$ | $\upnu(\mathtt{P}\leftrightarrow\mathtt{Q})$ | $\upnu(\mathtt{R}\to\mathtt{P})$ | $\upnu\bigl((\mathtt{P}\leftrightarrow\mathtt{Q})\lor(\mathtt{R}\to\mathtt{P})\bigr)$ |
|---|---|---|---|---|---|
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ |
| $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{F}$ | $\mathtt{T}$ |
| $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{F}$ | $\mathtt{T}$ | $\mathtt{T}$ | $\mathtt{T}$ |

## Example 2: $\mathtt{P}\to\mathtt{Q}\land\neg\mathtt{P}$

### Step 1 (Decompose through parsing tree)

$$
\mathtt{P}\to\mathtt{Q}\land\neg\mathtt{P}
$$

![[Pasted image 20260323045748.png|180]]

### Step 2 (Formation sequence)

$$
\mathtt{P},\ \mathtt{Q},\ \neg\mathtt{P},\ \mathtt{Q}\land\neg\mathtt{P},\ \mathtt{P}\to(\mathtt{Q}\land\neg\mathtt{P})
$$

### Step 3 (Valuation of propositional forms in formation sequence through truth tables)

| $\upnu(\mathtt{P})$ | $\upnu(\mathtt{Q})$ | $\upnu(\neg\mathtt{P})$ | $\upnu(\mathtt{Q}\land\neg\mathtt{P})$ | $\upnu\bigl(\mathtt{P}\to(\mathtt{Q}\land\neg\mathtt{P})\bigr)$ |
| ------------------- | ------------------- | ----------------------- | -------------------------------------- | --------------------------------------------------------------- |
| $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$            | $\mathtt{F}$                           | $\mathtt{F}$                                                    |
| $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$            | $\mathtt{F}$                           | $\mathtt{F}$                                                    |
| $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$            | $\mathtt{T}$                           | $\mathtt{T}$                                                    |
| $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$            | $\mathtt{F}$                           | $\mathtt{T}$                                                    |
## Example 3: $([\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}]) \to (\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])])$

### Step 1 (Decompose through parsing tree)

![[Pasted image 20260323172337.png|500]]

### Step 2 (Formation sequence)
$$
\begin{aligned}
&\mathtt{P},\ \mathtt{Q},\ \mathtt{R},\ \mathtt{S},\ \neg\mathtt{P},\ \neg\neg\mathtt{P},\ \mathtt{P}\land\mathtt{S},\ [\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}],\\[6pt]
&\mathtt{Q}\lor\mathtt{R},\ \neg[\mathtt{Q}\lor\mathtt{R}],\ \neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}],\\[6pt]
&\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}]),\ (\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])]),\\[6pt]
&([\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}]) \to (\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])]).
\end{aligned}
$$

### Step 3 (Valuation of propositional forms in formation sequence through truth tables)
  
| $\upnu(\mathtt{P})$ | $\upnu(\mathtt{Q})$ | $\upnu(\mathtt{R})$ | $\upnu(\mathtt{S})$ | $\upnu(\neg\mathtt{P})$ | $\upnu(\neg\neg\mathtt{P})$ | $\upnu(\mathtt{P}\land\mathtt{S})$ | $\upnu([\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}])$ | $\upnu(\mathtt{Q}\lor\mathtt{R})$ | $\upnu(\neg[\mathtt{Q}\lor\mathtt{R}])$ | $\upnu(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])$ | $\upnu(\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}]))$ | $\upnu(\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])])$ | $\upnu\bigl(([\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}]) \to (\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])])\bigr)$ |
| ------------------- | ------------------- | ------------------- | ------------------- | ----------------------- | --------------------------- | ---------------------------------- | -------------------------------------------------------------- | --------------------------------- | --------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{T}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{F}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{T}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{F}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{T}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{F}$                       | $\mathtt{T}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{T}$                       | $\mathtt{T}$                                                   | $\mathtt{F}$                      | $\mathtt{T}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$            | $\mathtt{T}$                | $\mathtt{F}$                       | $\mathtt{T}$                                                   | $\mathtt{F}$                      | $\mathtt{T}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{F}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{F}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{F}$                                                            | $\mathtt{F}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{F}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{T}$                      | $\mathtt{F}$                            | $\mathtt{F}$                                             | $\mathtt{F}$                                                            | $\mathtt{F}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{F}$                      | $\mathtt{T}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
| $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{F}$        | $\mathtt{T}$            | $\mathtt{F}$                | $\mathtt{F}$                       | $\mathtt{F}$                                                   | $\mathtt{F}$                      | $\mathtt{T}$                            | $\mathtt{T}$                                             | $\mathtt{T}$                                                            | $\mathtt{T}$                                                                            | $\mathtt{T}$                                                                                                                                                    |
  
#### Conclusion  
  
The final column is always $\mathtt{T}$. Therefore,  
  
$$  
([\neg\neg\mathtt{P}] \lor [\mathtt{P}\land\mathtt{S}]) \to (\mathtt{Q}\lor[\mathtt{R}\to(\neg\mathtt{P}\to\neg[\mathtt{Q}\lor\mathtt{R}])])  
$$  
  
is a tautology.