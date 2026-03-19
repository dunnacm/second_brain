---
down:
  - "[[Division, limits]]"
tags:
  - mathemagics/real_analysis
---
## Definition

> [!note]+ **Reciprocal (Inverse) Limit Rule**
>
> > [!warning]+ **IF**
> > $\displaystyle \lim_{n\to\infty}\{t_n\}=L\ne 0$.
>
> > [!tip]+ **THEN**
> > $$
> > \lim_{n\to\infty}\Big\{\frac{1}{t_n}\Big\}=\frac{1}{L}.
> > $$

## Proof:

> [!abstract]+ **Proof Outline**
> 1. **Goal:** Show that if $t_n \to L \ne 0$, then $\displaystyle \frac{1}{t_n} \to \frac{1}{L}$.
>
> 2. **Start from the definition:**  
>    Express the difference in reciprocal form:  
>    $$\Bigl|\frac{1}{t_n} - \frac{1}{L}\Bigr| = \frac{|t_n - L|}{|t_n||L|}.$$
>    To make this $<\varepsilon$, ensure both:
>    - $|t_n - L|$ is small (numerator control),  
>    - $|t_n|$ stays away from $0$ (denominator control).
>
> 3. **Half–modulus bound away from zero:**  
>    Since $t_n \to L \ne 0$, there exists $N_2$ such that  
>    $$n \ge N_2 \Rightarrow |t_n| > \frac{|L|}{2}.$$
>
> 4. **Bounding the numerator:**  
>    From the limit definition, there exists $N_1$ such that  
>    $$n \ge N_1 \Rightarrow |t_n - L| < \varepsilon \cdot \frac{|L|^{2}}{2}.$$
>
> 5. **Combine both bounds:**  
>    For $n \ge N_\varepsilon := \max\{N_1, N_2\}$,  
>    $$
>    \frac{|t_n - L|}{|t_n||L|}
>    < \frac{2}{|L|^{2}}\,|t_n - L|
>    < \varepsilon.
>    $$
>
> 6. **Quantifier closure:**  
>    Apply UG on $\varepsilon$, EG on $N$, and UG on $n$ to conclude  
>    $$\lim_{n\to\infty}\frac{1}{t_n} = \frac{1}{L}.$$
>
> 7. **Main idea:**  
>    The proof combines the definition of limit with a “bound-away-from-zero” argument to control the reciprocal’s denominator.

Assume $\displaystyle \lim_{n\to\infty}\{t_n\}=L\ne 0$.

$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty}\{t_n\}=L\ne 0
\ \Leftrightarrow\
\forall \varepsilon>0\ \exists N_1\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_1 \Rightarrow |t_n-L|<\varepsilon\cdot\frac{|L|^{2}}{2}\,].
\end{aligned}
$$

Applying **UI** on $\varepsilon$, **EI** on $N$, and **UI** on $n$ in (1), sequentially:

$$
\begin{aligned}
(2)\quad n\ge N_1\
&\Rightarrow\ |t_n-L|<\varepsilon\cdot\frac{|L|^{2}}{2}
&&\text{(from (1))}
\\
&\Rightarrow\ |t_n-L|\cdot\frac{2}{|L|^{2}}<\varepsilon
&&\text{(multiply both sides by $\,2/|L|^{2}$).}
\end{aligned}
$$

Applying **Half–modulus bound away from zero** to (1):

$$
\begin{aligned}
(3)\quad |t_n|>\frac{|L|}{2}\ (L\ne 0)\
&\Rightarrow\ \frac{1}{|t_n||L|}<\frac{2}{|L|^{2}}
&&\text{(invert and multiply)}
\\
&\Rightarrow\ \frac{|t_n-L|}{|t_n||L|}<\frac{2}{|L|^{2}}\;|t_n-L|
&&\text{(multiply by $|t_n-L|$)}
\\
&\Rightarrow\ \frac{|t_n-L|}{|t_n||L|}<\varepsilon
&&\text{(use the bound from (2)).}
\end{aligned}
$$

From (3) and the definition of limit, there exists $N_2$ such that

$$
\begin{aligned}
(4)\quad \exists N_2\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N_2 \Rightarrow |t_n-L|<\varepsilon\cdot|t_n||L|\,].
\end{aligned}
$$

Choose the common index $N_{\varepsilon}:=\max\{N_1,N_2\}$ and substitute it into (4):

$$
\begin{aligned}
(5)\quad n\ge N_{\varepsilon}\
&\Rightarrow\ |t_n-L|<\varepsilon\cdot|t_n||L|
&&\text{(from (4))}
\\
&\Rightarrow\ \frac{|t_n-L|}{|t_n||L|}<\varepsilon
&&\text{(divide by $|t_n||L|>0$)}
\\
&\Rightarrow\ \left|\frac{L-t_n}{t_n\,L}\right|<\varepsilon
&&\text{(rewrite numerator)}
\\
&\Rightarrow\ \left|\frac{1}{t_n}-\frac{1}{L}\right|<\varepsilon
&&\text{(algebra).}
\end{aligned}
$$

Applying **UG** on $n$, **EG** on $N$, and **UG** on $\varepsilon$ to (5), sequentially:

$$
\begin{aligned}
(6)\quad \forall \varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\in\mathbb{N}\,[\,n\ge N \Rightarrow \big|\tfrac{1}{t_n}-\tfrac{1}{L}\big|<\varepsilon\,]
\ \Leftrightarrow\
\lim_{n\to\infty}\Big\{\frac{1}{t_n}\Big\}=\frac{1}{L}.
\end{aligned}
$$