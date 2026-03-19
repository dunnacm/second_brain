---
down:
  - "[[Examples (limit of a sequence)]]"
  - "[[Proof (limit of sequences properties)]]"
  - "[[Properties (convergent sequences)]]"
tags:
  - mathemagics/real_analysis
---
## Definition:
>[!note] **Definition 2.2.1 (Limit of a sequence)**
> Let $\{s_n\}$ be a sequence in $\mathbb{R}$ (or $\mathbb{C}$) and let $L\in\mathbb{R}$ (or $\mathbb{C}$).
>
>>[!important] **Formal (FOL) definition**
>> $$
>> \lim_{n\to\infty} s_n = L
>> \quad \Leftrightarrow \quad
>> \forall \varepsilon>0\;\exists N\in\mathbb{N}\;\forall n\in\mathbb{N}\;
>> \bigl(n\ge N \;\Rightarrow\; \lvert s_n - L\rvert < \varepsilon \bigr).
>> $$
>
>>[!tip] **Notation (equivalents)**
>> $$
>> s_n \to L \ \text{ as } n\to\infty
>> \qquad\text{or}\qquad
>> \lim_{n\to\infty}s_n = L.
>> $$
>
>>[!tip] **Divergence as negation**
>> $$
>> \text{$\{s_n\}$ diverges}
>> \;\Leftrightarrow\;
>> \neg\exists L\ \forall \varepsilon>0\;\exists N\;\forall n\ge N:\ \lvert s_n-L\rvert<\varepsilon
>> $$
>> $$
>> \text{equivalently: }\ 
>> \forall L\ \exists\,\varepsilon_0>0\ \forall N\in\mathbb{N}\ \exists n\ge N:\ \lvert s_n-L\rvert\ge \varepsilon_0.
>> $$
## Properties