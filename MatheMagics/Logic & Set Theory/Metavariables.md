---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Introduction

A **metavariable** is a symbol of the **meta-language** used to stand for an arbitrary expression of the object language.

Thus, in propositional logic:

- $\mathtt{P},\mathtt{Q},\mathtt{R},\dots$ are object-language propositional variables;
- $p,q,r,\dots$ and $\varphi,\psi,\chi,\dots$ are meta-language symbols standing for arbitrary propositional forms;
- $\Gamma,\Delta,\Sigma,\dots$ are meta-language symbols standing for collections of propositional forms.

## Single-formula metavariables

The symbols
$$
p,q,r,\dots
$$
are commonly used as metavariables for individual propositional forms.

Likewise, the symbols
$$
\varphi,\psi,\chi,\dots
$$
are also commonly used as metavariables for individual formulas.

So, for example, either of the following may be used:

$p\to q$ or $\varphi\to\psi$

In both cases, the symbols stand for arbitrary propositional forms.

## Collection metavariables

The symbol
$$
\Gamma
$$
is a metavariable for a **set** or **sequence** of propositional forms.

So, rigorously, one may write:

- as a set: $\Gamma=\{p_0,p_1,\dots,p_{n-1}\}$
- as a sequence: $\Gamma=\langle p_0,p_1,\dots,p_{n-1}\rangle$

If one uses Greek-letter metavariables for single formulas, then one may likewise write:

- as a set:$\Gamma=\{\varphi_0,\varphi_1,\dots,\varphi_{n-1}\}$
- as a sequence: $\Gamma=\langle \varphi_0,\varphi_1,\dots,\varphi_{n-1}\rangle$

### Important distinction

The symbol $\Gamma$ does **not** itself mean a conjunction.

So $\Gamma=\{p_0,p_1,\dots,p_{n-1}\}$

is not the same as $p_0\land p_1\land\cdots\land p_{n-1}.$

The first is a **collection of formulas**.  
The second is **one formula**.

If one wants to pass from a finite collection of formulas to a single formula, one may form their conjunction explicitly.

## When each is appropriate

- Use $p,q,r,\dots$ for individual propositional forms in elementary propositional logic.
- Use $\varphi,\psi,\chi,\dots$ for individual formulas when using broader or more general logical notation.
- Use $\Gamma$ for a set or sequence of formulas, especially a set or list of premises.

