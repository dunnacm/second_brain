---
down:
  - "[[Propositional form or ((wffs) or (PL-formula))]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition

Let $p$ be a **finite sequence of characters** from a given collection of symbols (an **alphabet**).  
Then $p$ is called a **string over the alphabet**. 

In propositional logic, the alphabet chosen so that strings can represent propositions is called the **proposition alphabet**, consisting of: propositional variables, connectives, and grouping symbols. 

## Examples of strings (not all are well-formed)
Many sequences are strings over the proposition alphabet—including “bad” ones—and even the **empty string** counts as a string. 

## Grammar vs “just a string”
Only certain strings are selected for study—those that can represent propositions.  
This selection is made by a **grammar**, given recursively (base case + rules to build longer strings). 
Concretely, a **propositional form (PL-formula)** is a **nonempty string** over the proposition alphabet that satisfies the recursive formation rules (Definition 1.1.2). 