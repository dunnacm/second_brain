---
down:
tags:
  - mathemagics/real_analysis
---
> [!note]+ **Definition — $\varepsilon$-neighborhood**
>
> > [!warning]+ **IF**
> > - $x_0 \in \mathbb{R}$, and  
> > - $\varepsilon > 0$ is **fixed**.
>
> > [!tip]+ **THEN**
> > - The **$\varepsilon$-neighborhood** of $x_0$ is  
> >   $$
> >   V_{\varepsilon}(x_0) = \{\,x \in \mathbb{R} : \lvert x - x_0\rvert < \varepsilon\,\}.
> >   $$
> > - Equivalently,  
> >   $$
> >   (\varepsilon > 0)\ \wedge\ \forall x \in \mathbb{R}\,[\,x \in V_{\varepsilon}(x_0)\ \Leftrightarrow\ \lvert x - x_0\rvert < \varepsilon\,].
> >   $$
> ---
> > [!note]+ **Notes**
> > - In $\mathbb{R}$, one also writes  
> >   $$
> >   B_{\varepsilon}(x_0) = (x_0 - \varepsilon,\ x_0 + \varepsilon).
> >   $$
> > - $B_{\varepsilon}(x_0)$ is called the **open ball** of radius $\varepsilon$ centered at $x_0$.  
> >   It represents **all points within distance $\varepsilon$ of $x_0$**, excluding the boundary.  
> > - Thus, in $\mathbb{R}$:  
> >   $$
> >   B_{\varepsilon}(x_0) = V_{\varepsilon}(x_0).
> >   $$



```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathreplacing}

\begin{document}
\begin{tikzpicture}[scale=1.2, baseline={(current bounding box.center)}]
  % real line
  \draw[-, thick] (-3,0) -- (3,0);

  % tick marks
  \draw[thick] (-1.5,0.08) -- (-1.5,-0.08);
  \draw[thick] ( 1.5,0.08) -- ( 1.5,-0.08);

  % labels
  \node[below=3pt] at ( 0,0)   {$x_0$};
  \node[below=3pt] at (-1.5,0) {$x_0-\varepsilon$};
  \node[below=3pt] at ( 1.5,0) {$x_0+\varepsilon$};

  % brace: concave DOWN (overbrace style)
  % Option A: no mirror, path left->right
  \draw[decorate, decoration={brace, amplitude=5pt, raise=4pt}]
       (-1.5,0.0) -- (1.5,0.0)
       node[midway, above=10pt] {$V_{\varepsilon}(x_0)$};

  % (Alternative: keep 'mirror' but reverse the endpoints)
  % \draw[decorate, decoration={brace, amplitude=5pt, mirror, raise=4pt}]
  %      (1.5,0.0) -- (-1.5,0.0)
  %      node[midway, above=10pt] {$V_{\varepsilon}(x_0)$};
\end{tikzpicture}
\end{document}

```
