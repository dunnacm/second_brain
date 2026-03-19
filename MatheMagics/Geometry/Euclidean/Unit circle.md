---
down:
  - "[[Primary trigonometric functions]]"
  - "[[Inverse trigonometric functions]]"
tags:
  - mathemagics/geometry/euclidean
---
## Diagram:
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc}

\begin{document}
\begin{tikzpicture}[scale=1.05,
    dot/.style={circle,inner sep=1.6pt,draw,fill=blue!80,draw opacity=0,fill opacity=1},
    axis/.style={-Latex,thick},
    ray/.style={gray!55,thin},
    deg/.style={font=\footnotesize, text=black!70},
    rad/.style={font=\footnotesize, text=red!70!black},
    coord/.style={font=\small, text=blue!80!black}
]

% ----- helpers -----
\newcommand{\R}{3.6} % radius

% Map index -> coordinate string (cos, sin)
\newcommand{\coordlabel}[1]{%
\ifcase#1
(1,0)\or (\frac{\sqrt{3}}{2},\frac{1}{2})\or (\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2})\or (\frac{1}{2},\frac{\sqrt{3}}{2})\or
(0,1)\or (-\frac{1}{2},\frac{\sqrt{3}}{2})\or (-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2})\or (-\frac{\sqrt{3}}{2},\frac{1}{2})\or
(-1,0)\or (-\frac{\sqrt{3}}{2},-\frac{1}{2})\or (-\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2})\or (-\frac{1}{2},-\frac{\sqrt{3}}{2})\or
(0,-1)\or (\frac{1}{2},-\frac{\sqrt{3}}{2})\or (\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2})\or (\frac{\sqrt{3}}{2},-\frac{1}{2})
\fi}

% Map index -> radian string
\newcommand{\radlabel}[1]{%
\ifcase#1 0 \or \frac{\pi}{6} \or \frac{\pi}{4} \or \frac{\pi}{3} \or \frac{\pi}{2} \or
\frac{2\pi}{3} \or \frac{3\pi}{4} \or \frac{5\pi}{6} \or \pi \or
\frac{7\pi}{6} \or \frac{5\pi}{4} \or \frac{4\pi}{3} \or \frac{3\pi}{2} \or
\frac{5\pi}{3} \or \frac{7\pi}{4} \or \frac{11\pi}{6} \fi}

% Map index -> degree string
\newcommand{\deglabel}[1]{%
\ifcase#1 0^\circ \or 30^\circ \or 45^\circ \or 60^\circ \or 90^\circ \or
120^\circ \or 135^\circ \or 150^\circ \or 180^\circ \or 210^\circ \or
225^\circ \or 240^\circ \or 270^\circ \or 300^\circ \or 315^\circ \or 330^\circ \fi}

% ----- axes -----
\draw[axis] (-4.6,0) -- (4.9,0) node[below right=1pt] {$x$};
\draw[axis] (0,-4.6) -- (0,4.9) node[above left=1pt] {$y$};

% unit circle
\draw[line width=0.9pt] (0,0) circle (\R);

% angles to draw (degrees)
\def\angles{0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330}

% Rays + dots + labels
\foreach [count=\i from 0] \a in \angles {
  % light ray
  \draw[ray] (0,0) -- (\a:\R*0.92);

  % dot on circle
  \path (\a:\R) node[dot] {};

  % radian label (inside arc)
  \node[rad] at (\a:\R*0.76) {$\radlabel{\i}$};

  % degree label (outside arc)
  \node[deg] at (\a:\R*1.05) {$\deglabel{\i}$};

  % coordinate pair label (farther out)
  \node[coord] at (\a:\R*1.24) {$\coordlabel{\i}$};
}

\end{tikzpicture}
\end{document}

```

## Quadrant signs:
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}[scale=0.9]

% --- grid (background) ---
\draw[step=1,help lines,gray!55] (-4.6,-3.6) grid (4.6,3.6);

% --- axes with arrows (blue) ---
\draw[blue!70!black, line width=2.2pt, -{Latex[length=4mm]}] (-4.6,0) -- (4.8,0);
\draw[blue!70!black, line width=2.2pt, -{Latex[length=4mm]}] (0,-3.6) -- (0,3.8);
\node[below right] at (4.8,0) {$x$};
\node[above left]  at (0,3.8) {$y$};

% --- tick marks & numbers (skip origin) ---
\foreach \x in {-4,-3,-2,-1,1,2,3,4}{
  \draw[blue!70!black, line width=1.4pt] (\x,0.09) -- (\x,-0.09);
  \node[below, yshift=-1pt] at (\x,0) {\small \x};
}
\foreach \y in {-3,-2,-1,1,2,3}{
  \draw[blue!70!black, line width=1.4pt] (0.09,\y) -- (-0.09,\y);
  \node[left, xshift=-1pt] at (0,\y) {\small \y};
}
\node[below right] at (0.04,-0.04) {\small 0};

% --- quadrant words (Spanish mnemonic) ---
% QII: SENtimos^2
\node[anchor=east] at (-0.3,2.1)
  {\bfseries\Large \textcolor{red!80!black}{SEN}\textcolor{green!50!black}{timos$^{2}$}};
% QI: TODOS
\node[anchor=west] at (0.3,2.1)
  {\bfseries\Large \textcolor{red!80!black}{TODOS}};
% QIII: TANtas
\node[anchor=east] at (-0.3,-2.1)
  {\bfseries\Large \textcolor{red!80!black}{TAN}\textcolor{green!50!black}{tas}};
% QIV: COSas
\node[anchor=west] at (0.3,-2.1)
  {\bfseries\Large \textcolor{red!80!black}{COS}\textcolor{green!50!black}{as}};

\end{tikzpicture}
\end{document}

```
