---
down:
  - "[[Assignment operator]]"
  - "[[Equality symbol]]"
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
# Logic and Set Theory Symbol Glossary

Some symbols are context-dependent, so the same symbol may appear in more than one section with different meanings.

## 1. Logical connectives and quantifiers

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\lnot$ | Negation | “not”; reverses the truth value of a statement | $\lnot(2<1)$ | `\lnot` |
| $\land$ | Conjunction | “and”; true when both parts are true | $(2<3)\land(5\text{ is odd})$ | `\land` |
| $\lor$ | Disjunction | Inclusive “or”; true when at least one part is true | $(2<1)\lor(4\text{ is even})$ | `\lor` |
| $\to$ | Conditional | “if ... then ...” | $n\text{ is even}\to n^2\text{ is even}$ | `\to` |
| $\leftrightarrow$ | Biconditional | “if and only if” | $n\text{ is even}\leftrightarrow n^2\text{ is even}$ | `\leftrightarrow` |
| $\forall$ | Universal quantifier | “for all” | $\forall x\in\mathbb R\,(x+0=x)$ | `\forall` |
| $\exists$ | Existential quantifier | “there exists” | $\exists x\in\mathbb Z\,(x^2=9)$ | `\exists` |

## 2. Proof, consequence, and metalevel symbols

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\vdash$ | Syntactic derivability | “is provable from” in a formal proof system | $\{P\to Q,\ P\}\vdash Q$ | `\vdash` |
| $\vdash^{\ast}$ | Starred derivability | Provable in the starred / restricted proof system being used | $\vdash^{\ast}(P\to P)$ | `\vdash^{\ast}` |
| $\models$ | Semantic consequence | “entails”; true in every model / valuation satisfying the premises | $\{P\to Q,\ P\}\models Q$ | `\models` |
| $\not\models$ | Not semantic consequence | “does not entail” | $P\lor Q \not\models P$ | `\not\models` |
| $\nvdash,\ \not\vdash$ | Not derivable | “is not provable from” | $P\nvdash Q$ | `\nvdash`, `\not\vdash` |
| $\Rightarrow$ | Meta-level implication | Used in explanations or proof steps to mean “therefore / implies” | $n=2k \Rightarrow n^2=4k^2$ | `\Rightarrow` |
| $\Leftrightarrow$ | Meta-level equivalence | Used in proof chains to mean “equivalent to” | $x\in A\cap B \Leftrightarrow (x\in A\land x\in B)$ | `\Leftrightarrow` |

## 3. Sets: membership, inclusion, and construction

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\varnothing$ | Empty set | The set with no elements | $A\cap\varnothing=\varnothing$ | `\varnothing` |
| $\in$ | Membership | “is an element of” | $3\in\{1,2,3\}$ | `\in` |
| $\notin$ | Non-membership | “is not an element of” | $4\notin\{1,2,3\}$ | `\notin` |
| $\ni$ | Contains as element | Reverse-style notation for membership | $\{1,2,3\}\ni 2$ | `\ni` |
| $\subseteq$ | Subset | Every element of the left set is in the right set | $\{1,2\}\subseteq\{1,2,3\}$ | `\subseteq` |
| $\subset$ | Proper subset | Subset, but not equal | $\{1,2\}\subset\{1,2,3\}$ | `\subset` |
| $\supseteq$ | Superset | Reverse of subset | $\{1,2,3\}\supseteq\{1,2\}$ | `\supseteq` |
| $\supset$ | Proper superset | Reverse of proper subset | $\{1,2,3\}\supset\{1,2\}$ | `\supset` |
| $\nsubseteq$ | Not a subset | The left set is not contained in the right set | $\{1,4\}\nsubseteq\{1,2,3\}$ | `\nsubseteq` |
| $\nsupseteq$ | Not a superset | The left set does not contain the right set | $\{1,2\}\nsupseteq\{1,2,3\}$ | `\nsupseteq` |
| $\{x \mid \cdots\}$ | Set-builder notation (bar) | “the set of all $x$ such that ...” | $\{x\in\mathbb Z \mid x^2<10\}=\{-3,-2,-1,0,1,2,3\}$ | `\{x \mid \cdots\}` |
| $\{x : \cdots\}$ | Set-builder notation (colon) | Same idea as the bar version | $\{x\in\mathbb R : x^2=1\}=\{-1,1\}$ | `\{x : \cdots\}` |
| $\mathcal{P}(A)$ / $P(A)$ | Power set | The set of all subsets of $A$ | $\mathcal{P}(\{1,2\})=\{\varnothing,\{1\},\{2\},\{1,2\}\}$ | `\mathcal{P}(A)` |

## 4. Set operations and families of sets

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\cup$ | Union | Elements in at least one of the sets | $\{1,2\}\cup\{2,3\}=\{1,2,3\}$ | `\cup` |
| $\cap$ | Intersection | Elements common to both sets | $\{1,2\}\cap\{2,3\}=\{2\}$ | `\cap` |
| $\setminus$ | Set difference | Elements in the first set but not the second | $\{1,2,3\}\setminus\{2\}=\{1,3\}$ | `\setminus` |
| $\overline{A}$ | Complement | All elements in the fixed universe $U$ that are not in $A$ | If $U=\{1,2,3,4\}$ and $A=\{1,3\}$, then $\overline{A}=\{2,4\}$ | `\overline{A}` |
| $\times$ | Cartesian product | Set of ordered pairs from two sets | $\{1,2\}\times\{a,b\}=\{(1,a),(1,b),(2,a),(2,b)\}$ | `\times` |
| $\bigcup$ | Big union | Union of a family / indexed collection of sets | $\bigcup\{\{1\},\{2,3\}\}=\{1,2,3\}$ | `\bigcup` |
| $\bigcap$ | Big intersection | Intersection of a family / indexed collection of sets | $\bigcap\{\{1,2\},\{2,3\}\}=\{2\}$ | `\bigcap` |
| $\uplus$ | Disjoint union | Union of sets intended to be disjoint | $\{1,2\}\uplus\{3,4\}=\{1,2,3,4\}$ | `\uplus` |
| $\triangle,\ \Delta$ | Symmetric difference | Elements in exactly one of the two sets | $\{1,2\}\Delta\{2,3\}=\{1,3\}$ | `\triangle`, `\Delta` |

## 5. Relations, equivalence, order, and cardinal comparison

| Symbol         | Name                             | Meaning / how to read                                                              | Example                                                       | LaTeX         |
| -------------- | -------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------- |
| $aRb$          | Relation notation                | “$a$ is related to $b$ by $R$”; equivalent to $(a,b)\in R$                         | If $R$ is divisibility, then $2R6$                            | —             |
| $a\,\not R\,b$ | Negated relation                 | “$a$ is not related to $b$ by $R$”                                                 | If $R$ is divisibility, then $3\,\not R\,10$                  | —             |
| $R^{-1}$       | Inverse relation                 | Reverse all ordered pairs in the relation                                          | If $R=\{(1,2),(3,4)\}$, then $R^{-1}=\{(2,1),(4,3)\}$         | `R^{-1}`      |
| $\circ$        | Relation composition             | Chain two relations: first one, then the other                                     | If $R=\{(1,2)\}$ and $S=\{(2,3)\}$, then $S\circ R=\{(1,3)\}$ | `\circ`       |
| $\mid$         | Divides                          | $a\mid b$ means $a$ divides $b$                                                    | $4\mid 12$                                                    | `\mid`        |
| $\equiv$       | Congruence modulo                | Same remainder modulo a fixed integer                                              | $17\equiv 2\pmod{5}$                                          | `\equiv`      |
| $\preceq$      | Preorder / comparison            | “precedes or equals”; in cardinality, often means “injects into”                   | $\mathbb N\preceq\mathbb R$                                   | `\preceq`     |
| $\not\preceq$  | Negated preorder / comparison    | The left side does not precede / embed into the right side in the given comparison | $\mathbb R\not\preceq\mathbb N$                               | `\not\preceq` |
| $\prec$        | Strict order / strict comparison | Strict version of $\preceq$                                                        | $\mathbb N\prec\mathbb R$                                     | `\prec`       |
| $\approx$      | Equinumerous                     | Same cardinality; there is a bijection between the sets                            | $\mathbb N\approx 2\mathbb N$                                 | `\approx`     |
| $\not\approx$  | Not equinumerous                 | No bijection exists between the sets                                               | $\mathbb N\not\approx\mathbb R$                               | `\not\approx` |
| $\cong$        | Isomorphic / congruent           | Same structure or same geometric shape, depending on context                       | $(\mathbb Z,+)\cong(2\mathbb Z,+)$                            | `\cong`       |
| $\perp$        | Incompatible / perpendicular     | In order theory: incompatible; in geometry: perpendicular; read from context       | $a\perp b$ in a poset, or $\ell_1\perp\ell_2$ in geometry     | `\perp`       |

## 6. Functions and mappings

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\mapsto$ | Maps-to | Specifies the output rule for an input | $x\mapsto x^2+1$ | `\mapsto` |
| $f\colon A\to B$ | Function notation | $f$ is a function from domain $A$ to codomain $B$ | $f\colon\mathbb R\to\mathbb R,\ x\mapsto x^2$ | `\colon`, `\to` |
| $f\!\upharpoonright_{S}$ | Restriction | Same function rule, but only on the subset $S$ of the domain | If $f(x)=x^2$, then $f\!\upharpoonright_{[0,\infty)}$ is $x^2$ on $[0,\infty)$ | `\upharpoonright` |
| $f[S]$ | Image | Outputs of elements of $S$ under $f$ | If $f(x)=x^2$ and $S=\{-2,-1,1\}$, then $f[S]=\{1,4\}$ | — |
| $f^{-1}[T]$ | Preimage | All inputs whose outputs lie in $T$ | If $f(x)=x^2$ on $\mathbb Z$ and $T=\{1,4\}$, then $f^{-1}[T]=\{-2,-1,1,2\}$ | — |
| $\circ$ | Function composition | Apply one function, then the next | If $f(x)=x+1$ and $g(x)=x^2$, then $(g\circ f)(x)=(x+1)^2$ | `\circ` |
| $\mathrm{id}$ | Identity map | Sends every element to itself | $\mathrm{id}_{A}(x)=x$ | `\mathrm{id}` |

## 7. Very common logical constants and variants

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\top$ | Truth constant | Always true | $P\land\top\leftrightarrow P$ | `\top` |
| $\bot$ | Falsity constant | Always false | $P\lor\bot\leftrightarrow P$ | `\bot` |
| $\exists!$ | Unique existence | “There exists exactly one ...” | $\exists!x\in\mathbb R\,(2x+1=5)$ | `\exists!` |
| $\oplus,\ \veebar,\ \underline{\lor}$ | Exclusive-or | Exactly one of the two statements is true | $P\oplus Q$ | `\oplus`, `\veebar`, `\underline{\lor}` |
| $\uparrow$ | NAND | “not both” | $P\uparrow Q \leftrightarrow \lnot(P\land Q)$ | `\uparrow` |
| $\downarrow$ | NOR | “neither ... nor ...” | $P\downarrow Q \leftrightarrow \lnot(P\lor Q)$ | `\downarrow` |

## 8. Modal and temporal logic symbols

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\Box$ | Necessity | “necessarily” | $\Box p$ | `\Box` |
| $\Diamond$ | Possibility | “possibly” | $\Diamond p$ | `\Diamond` |
| $\mathsf{G}$ | Globally | “always in the future” | $\mathsf{G}\,p$ | `\mathsf{G}` |
| $\mathsf{F}$ | Eventually | “at some future time” | $\mathsf{F}\,p$ | `\mathsf{F}` |
| $\mathsf{X}$ | Next | “in the next state / next moment” | $\mathsf{X}\,p$ | `\mathsf{X}` |
| $\mathsf{U}$ | Until | $p$ holds until $q$ holds | $p\,\mathsf{U}\,q$ | `\mathsf{U}` |

## 9. Number systems and algebraic structure notation

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $\mathbb{N}$ | Natural numbers | The natural-number system | $2\in\mathbb N$ | `\mathbb{N}` |
| $\mathbb{Z}$ | Integers | Whole numbers, positive and negative, including $0$ | $-3\in\mathbb Z$ | `\mathbb{Z}` |
| $\mathbb{Q}$ | Rational numbers | Numbers of the form $\frac{a}{b}$ with $b\neq 0$ | $\frac{2}{3}\in\mathbb Q$ | `\mathbb{Q}` |
| $\mathbb{R}$ | Real numbers | The real-number line | $\pi\in\mathbb R$ | `\mathbb{R}` |
| $\mathbb{C}$ | Complex numbers | Numbers of the form $a+bi$ | $1+i\in\mathbb C$ | `\mathbb{C}` |
| $\mathbb{Z}_n,\ \mathbb{Z}/n\mathbb{Z}$ | Integers modulo $n$ | The quotient ring / set of congruence classes modulo $n$ | $\mathbb Z_5=\{[0],[1],[2],[3],[4]\}$ | `\mathbb{Z}_n`, `\mathbb{Z}/n\mathbb{Z}` |
| $\oplus$ | Direct sum | Combination of algebraic objects where components are tracked separately | $\mathbb Z\oplus\mathbb Z$ | `\oplus` |
| $\prod$ | Direct product | Indexed product of algebraic structures; same symbol as the big product operator, so read by context | $\prod_{i=1}^{3} G_i$ | `\prod` |

## 10. Arithmetic, comparison, and geometric / analytic notation

| Symbol | Name | Meaning / how to read | Example | LaTeX |
|---|---|---|---|---|
| $=$ | Equality | Both sides are exactly the same object / value | $2+3=5$ | `=` |
| $\neq$ | Not equal | The two sides are different | $2\neq 3$ | `\neq` |
| $<$ | Less than | Strict comparison | $2<5$ | `<` |
| $>$ | Greater than | Strict comparison | $5>2$ | `>` |
| $\le$ | Less than or equal | Non-strict comparison | $3\le 3$ | `\le` |
| $\ge$ | Greater than or equal | Non-strict comparison | $5\ge 2$ | `\ge` |
| $\ll$ | Much less than | Informal / asymptotic “far smaller than”; exact meaning depends on context | $1\ll 10^6$ | `\ll` |
| $\gg$ | Much greater than | Informal / asymptotic “far larger than”; exact meaning depends on context | $10^6\gg 1$ | `\gg` |
| $\approx,\ \sim,\ \simeq$ | Approximate / similar relation | Common comparison symbols; exact meaning depends on context | $\pi\approx 3.14159$, $f(n)\sim n^2$, $\sin x\simeq x$ for small $x$ | `\approx`, `\sim`, `\simeq` |
| $\lvert x\rvert$ | Absolute value | Distance of $x$ from $0$ on the real line | $\lvert -3\rvert=3$ | `\lvert x\rvert` |
| $\lVert x\rVert$ | Norm | Size / length of a vector or element in a normed space | $\lVert(3,4)\rVert=5$ | `\lVert x\rVert` |
| $\lfloor x\rfloor$ | Floor | Greatest integer less than or equal to $x$ | $\lfloor 3.7\rfloor=3$ | `\lfloor x\rfloor` |
| $\lceil x\rceil$ | Ceiling | Least integer greater than or equal to $x$ | $\lceil 3.1\rceil=4$ | `\lceil x\rceil` |
| $\langle x,y\rangle$ | Inner product | Standard pairing in inner-product spaces | $\langle(1,2),(3,4)\rangle=11$ | `\langle x,y\rangle` |
| $\pm$ | Plus/minus | Both sign choices are allowed | If $x^2=9$, then $x=\pm 3$ | `\pm` |

## 11. Summation, products, calculus, and definitions

| Symbol                         | Name                        | Meaning / how to read                                            | Example                                 | LaTeX                         |
| ------------------------------ | --------------------------- | ---------------------------------------------------------------- | --------------------------------------- | ----------------------------- |
| $\sum$                         | Summation                   | Add terms across an index set                                    | $\sum_{k=1}^{4} k = 10$                 | `\sum`                        |
| $\prod$                        | Product                     | Multiply terms across an index set                               | $\prod_{k=1}^{4} k = 24$                | `\prod`                       |
| $\lim$                         | Limit                       | Value approached by a sequence or function                       | $\lim_{x\to 0}\frac{\sin x}{x}=1$       | `\lim`                        |
| $\dfrac{d}{dx}$                | Derivative operator         | Differentiate with respect to $x$                                | $\frac{d}{dx}(x^2)=2x$                  | `\frac{d}{dx}`                |
| $\dfrac{\partial}{\partial x}$ | Partial derivative operator | Differentiate with respect to one variable, holding others fixed | $\frac{\partial}{\partial x}(x^2y)=2xy$ | `\frac{\partial}{\partial x}` |
| $\int$                         | Integral                    | Continuous accumulation / area operator                          | $\int_{0}^{1} x\,dx=\frac{1}{2}$        | `\int`                        |
| $:=$                           | Defined as                  | Introduces a definition                                          | $f(x):=x^2+1$                           | `:=`                          |