---
down:
tags:
  - mathemagics/real_analysis
---
> [!note]+ **Definition — Deleted $\varepsilon$-neighborhood**
>
> > [!warning]+ **IF**
> > - $x_0 \in \mathbb{R}$, and  
> > - $\varepsilon > 0$ is **fixed**.
>
> > [!tip]+ **THEN**
> > - The **deleted $\varepsilon$-neighborhood** of $x_0$ is  
> >   $$
> >   V'_{\varepsilon}(x_0) = \{\,x \in \mathbb{R} : 0 < \lvert x - x_0\rvert < \varepsilon\,\}.
> >   $$
> > - Equivalently,  
> >   $$
> >   (\varepsilon > 0)\ \wedge\ \forall x \in \mathbb{R}\,[\,x \in V'_{\varepsilon}(x_0)\ \Leftrightarrow\ 0 < \lvert x - x_0\rvert < \varepsilon\,].
> >   $$
>---
> > [!note]+ **Notes**
> > - $V'_{\varepsilon}(x_0)$ is obtained by **removing the center** $x_0$ from the ordinary $\varepsilon$-neighborhood:  
> >   $$
> >   V'_{\varepsilon}(x_0) = V_{\varepsilon}(x_0)\setminus\{x_0\}.
> >   $$
> > - In $\mathbb{R}$, one may also write  
> >   $$
> >   B'_{\varepsilon}(x_0) = (x_0 - \varepsilon,\ x_0 + \varepsilon)\setminus\{x_0\}.
> >   $$
> > - It represents **all points within distance $\varepsilon$ of $x_0$ except $x_0$ itself** — i.e., an open interval “punctured” at its center.


