---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Verbal definition:
A propositional form p is a contradiction if v(p) always equals F for every valuation v
## Formal definition: 

> [!note]+ **Contradiction**
> > [!warning]+ **IFF**
> > - $p$ is a propositional form.
>
> > [!tip]+ **THEN**
> > $$
> > \vDash \neg p
> > \quad \Leftrightarrow \quad
> > (\forall \upnu)\,[\upnu(p)=\mathtt{F}]
> > \quad \Leftrightarrow \quad
> > \neg(\exists \upnu)\,[\upnu(p)=\mathtt{T}].
> > $$

## Related fact

$$
\not\vDash p \quad \Leftrightarrow \quad (\exists \upnu)\,[\upnu(p)=\mathtt{F}].
$$

This second statement is true, but it does **not** define contradiction. It says only that $p$ is **not a tautology**.

## Example
 $$
  \mathtt{P}\land\neg\mathtt{P}
$$