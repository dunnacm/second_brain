---
down:
  - "[[Formulas (FOL S-Formulas)]]"
  - "[[Terms (S-Terms)]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Definition
In first-order logic, we work with a **first-order alphabet** $A$ that contains:
- **logic symbols** (variables, connectives, quantifiers, equality, grouping), and
- (optional) **theory symbols** (constants, $n$-ary function symbols, $n$-ary relation symbols),
chosen to fit a subject (set theory, number theory, etc.). 

A **string over $A$** is any finite sequence of characters drawn from $A$ (same “string over an alphabet” idea as in PL).

## Strings can be “about a theory,” but may still be nonsense
O’Leary explicitly points out that for a string to represent something from a particular theory, **each nonlogic symbol in it must be a theory symbol of that subject.** 
He gives examples of strings “for set theory” (i.e., using the set-theory theory symbols), but emphasizes that some strings are plausible and others are not. 

## Grammar is still needed (and is more complicated than in PL)
As with propositional logic, we need a **grammar** to determine which strings are *legal*—but in FOL the grammar is more complicated because predicates can involve variables. 

O’Leary then builds legality in stages:
- first define **S-terms** as certain strings over $A$ (Definition 2.1.7), 
- then define **S-formulas** as certain strings over $A$ (Definition 2.1.9).

## “Alphabet + grammar” = language
O’Leary states explicitly:
> **An alphabet combined with a grammar is called a language.**
So in FOL, “strings” are the raw material, and the grammar carves out the well-formed terms and formulas that constitute the language.