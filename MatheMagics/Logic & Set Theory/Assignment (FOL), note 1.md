---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## The big picture

In first-order logic, truth does **not** come from the formula alone.

A first-order formula gets a truth value only relative to:

1. a **structure**, and
2. an **assignment** (when free variables are present).

So first-order logic follows the same general idea as propositional logic:

$$
\text{syntax first, semantics second.}
$$

## Parallel with propositional logic

### Propositional logic
- symbols: $\mathtt{P},\mathtt{Q},\mathtt{R},\dots$
- assign propositions to them
- apply the truth valuation $\upnu$

### First-order logic
- formulas contain variables, constants, function symbols, and relation symbols
- a **structure** tells you what the nonlogical symbols mean
- an **assignment** tells you which objects the free variables currently denote
- then you evaluate truth by **satisfaction**

So the analogy is:

$$
\text{assignment of atoms} + \upnu
\quad\longleftrightarrow\quad
\text{structure} + \text{assignment} + \vDash
$$

## What each semantic ingredient does

### 1. Structure
A structure is the **world of discourse** in which the formula is being interpreted.

It supplies:
- a **domain** of objects;
- meanings for the nonlogical symbols.

So the structure answers questions like:
- What objects are we talking about?
- What does the constant symbol name?
- What function does this function symbol denote?
- What relation does this relation symbol denote?

A good informal slogan is:

$$
\text{The structure fixes what the language is about.}
$$

### 2. Assignment
An assignment chooses values for the **free variables**.

So if a formula contains a free variable such as $x$, the assignment tells you:

$$
x \mapsto \text{which object in the domain?}
$$

A good informal slogan is:

$$
\text{The assignment fixes the current placeholders.}
$$


### 3. Satisfaction
Once the structure has fixed the meanings of the nonlogical symbols, and the assignment has fixed the values of the free variables, the satisfaction relation tells you whether the formula is **true in that setup**.

So:

- **structure** = semantic background
- **assignment** = current variable-values
- **satisfaction** = truth in that semantic setup


## Why this is needed

Consider the formula
$$
x=y.
$$

By itself, this is not yet true or false in any absolute sense.

To evaluate it, you need to know:
- what object $x$ denotes,
- what object $y$ denotes.

That is exactly what the assignment provides.

Now consider
$$
R(x,f(c)).
$$

To evaluate this, you need to know:
- what $c$ denotes,
- what function $f$ denotes,
- what relation $R$ denotes,
- what object $x$ denotes.

So:
- the **structure** interprets $c$, $f$, and $R$,
- the **assignment** interprets $x$.

Only then can the formula be evaluated.

## Terms first, formulas second

A good way to think about the semantics is:

1. evaluate **terms** as objects of the domain;
2. then evaluate **formulas** as true or false statements about those objects.

So the flow is:

$$
\text{terms} \to \text{objects in the domain},
\qquad
\text{formulas} \to \text{truth values}.
$$

This is why your note first defines the interpretation of terms and only then defines satisfaction for formulas.

## Why quantifiers force variable-changing

Suppose the formula is
$$
\forall x\,\varphi.
$$

To say this is true means:

- no matter which object of the domain is chosen for $x$,
- the formula $\varphi$ comes out true.

That is why the semantics uses a modified assignment such as $I_x^b$:
it means “use the same assignment as before, except now let $x$ denote $b$.”

Similarly,
$$
\exists x\,\varphi
$$
means:

- there is **some** object $b$ in the domain
- such that $\varphi$ is true when $x$ is assigned that object.

So quantifiers do not merely decorate formulas.  
They tell you to **vary the assignment**.

## The most important conceptual distinction

Do not merge these two roles:

- **the structure interprets symbols**
- **the assignment interprets free variables**

That distinction is the heart of first-order semantics.

A constant symbol does **not** get its meaning from the assignment.  
It gets its meaning from the structure.

A free variable does **not** get its value from the structure alone.  
It gets its value from the assignment.

## Sentences vs formulas with free variables

If a formula has **no free variables**, it is a **sentence**.

A sentence can be true or false in a structure **without needing a separate variable assignment** in any essential way.

If a formula **does** have free variables, then its truth depends on the current assignment.

So:

$$
\text{sentence} \Rightarrow \text{truth depends only on the structure},
$$

whereas

$$
\text{open formula} \Rightarrow \text{truth depends on the structure and the assignment}.
$$

## Final bridge back to propositional logic

In propositional logic, the question is:

$$
\text{Which proposition does }\mathtt{P}\text{ stand for, and is it true or false?}
$$

In first-order logic, the question becomes:

$$
\text{Which structure are we in, what do the symbols mean there, and what do the free variables denote?}
$$

So the first-order case is not a different idea.  
It is the **same semantic idea made richer**.