---
down:
tags:
  - mathemagics/geometry/euclidean
---
## Sine & Cosine:
### General forms:
For **sine** and **cosine**:

$$
y(x) = A\sin\big(B(x-C)\big)+D
\qquad\text{or}\qquad
y(x) = A\cos\big(B(x-C)\big)+D
$$
### Key parameters & their effects:
- **Amplitude**:
  $$
  \text{Amplitude} = |A|
  $$
  If $A<0$, the graph is reflected across its midline.

- **Period**:
  $$
  T = \frac{2\pi}{|B|}
  $$

- **Horizontal (phase) shift**

  The graph is shifted **$C$ units** horizontally:

  - $C>0$ → shift **right** $C$ units  
  - $C<0$ → shift **left** $|C|$ units

- **Vertical shift**

  The entire graph is shifted **up** or **down** by $D$.

  The **midline** is
  $$
  y = D.
  $$
### Examples:
#### Sine:
Let
$$
y(x) = -3\sin(2x+\pi/2)+1
$$

Rewriting the inside:
$$
y(x) = -3\sin\big(2(x+\tfrac{\pi}{4})\big)+1.
$$
so it is in $A\sin(B(x-C))+D$ form with

- $A = -3$
- $B = 2$
- $C = -\dfrac{\pi}{4}$
- $D = 1$

Then:

- **Amplitude**: $|A| = 3$.  
- **Period**: $T = \dfrac{2\pi}{|2|} = \pi$.  
- **Horizontal shift**: $C=-\dfrac{\pi}{4}$ → shift **left** $\dfrac{\pi}{4}$.  
- **Vertical shift**: $D=1$ → midline $y=1$.  
- Because $A<0$, the sine wave is reflected across the line $y=1$.

```desmos-graph
left=-pi; right=pi;
top=4.5; bottom=-2.5;
height=380; width=520;
---
y=-3\sin(2(x+\pi/4))+1|magenta|solid

```
#### Cosine:
Let
$$
y(x) = \dfrac12\cos\Big(\frac{x-\pi}{3}\Big) - 2.
$$
Rewriting the inside:
$$
y(x) = \frac{1}{2} \cos\left( \frac{1}{3}(x - \pi) \right)
$$


- $A = \dfrac12$
- $B = \dfrac13$
- $C = \pi$
- $D = -2$

Hence:

- **Amplitude**: $|A| = \dfrac12$.  
- **Period**: $T = \dfrac{2\pi}{|1/3|} = 6\pi$.  
- **Horizontal shift**: $C=\pi$ → shift **right** $\pi$.  
- **Vertical shift**: $D=-2$ → midline $y=-2$.  
- Since $A>0$, we keep the standard cosine shape (starting at a maximum) but centered on the line $y=-2$.
```desmos-graph
left=-2*pi; right=4*pi;
top=1; bottom=-5;
height=380; width=520;
---
y=\frac12\cos\left(\frac{x-\pi}{3}\right)-2|blue|solid
```

## Tangent:
### General form:
For the **tangent** function:

$$
y(x) = A\tan\big(B(x-C)\big)+D
$$

### Key parameters & their effects:
- **Vertical stretch / reflection**:
	  **-** There is *no amplitude* (tangent is unbounded).
	  **-** $|A|$ controls **vertical stretch**.
	  **-** If $A<0$, the graph is reflected across its midline.

- **Period**:
  $$
  T = \frac{\pi}{|B|}
  $$

- **Horizontal (phase) shift**:

  The graph is shifted **$C$ units** horizontally:

  - $C>0$ → shift **right** $C$ units  
  - $C<0$ → shift **left** $|C|$ units

- **Vertical shift / midline**:

  The entire graph is shifted **up** or **down** by $D$.

  The **midline** is
  $$
  y = D.
  $$

- **Vertical asymptotes**:

  For $y(x) = A\tan\big(B(x-C)\big)+D$, vertical asymptotes occur at
  $$
  B(x-C) = \frac{\pi}{2} + k\pi,\quad k\in\mathbb{Z},
  $$
  i.e.
  $$
  x = C + \dfrac{\dfrac{\pi}{2} + k\pi}{B},\quad k\in\mathbb{Z}.
  $$

### Example:
Let
$$
y(x) = -2\tan\big(x+\dfrac{\pi}{4}\big)+1.
$$

This is already in $A\tan(B(x-C))+D$ form with

- $A = -2$
- $B = 1$
- $C = -\dfrac{\pi}{4}$
- $D = 1$

Then:

- **Vertical stretch / reflection**: factor $|A|=2$ and reflection across $y=1$ (since $A<0$).  
- **Period**: 
  $$
  T = \frac{\pi}{|1|} = \pi.
  $$
- **Horizontal shift**: $C=-\dfrac{\pi}{4}$ → shift **left** $\dfrac{\pi}{4}$.  
- **Vertical shift**: $D=1$ → midline $y=1$.  
- **Vertical asymptotes**:

  Solve
  $$
  x+\frac{\pi}{4} = \frac{\pi}{2} + k\pi
  \quad\Rightarrow\quad
  x = \frac{\pi}{4} + k\pi,\quad k\in\mathbb{Z}.
  $$

So one period between two consecutive asymptotes is, for example, from $x=-\dfrac{3\pi}{4}$ to $x=\dfrac{\pi}{4}$, with the “center” of that branch at $x=-\dfrac{\pi}{4}$ on the midline $y=1$.

```desmos-graph
left=-pi; right=pi;
top=4; bottom=-4;
height=380; width=520;
---
y=-2\tan(x+\pi/4)+1|blue|solid

x=-3\pi/4|red|dotted
x=\pi/4|red|dotted
```


- The dotted lines mark two consecutive vertical asymptotes 
  $x = -\dfrac{3\pi}{4}$ and $x = \dfrac{\pi}{4}$.
- The tangent branch between them shows the effect of the shift, stretch, 
  and vertical translation, just like your sine and cosine examples.

## Summary:

> [!summary]+
> For transformed trigonometric functions of the form  
> $y(x) = A\sin(B(x-C))+D$, $y(x) = A\cos(B(x-C))+D$, or $y(x) = A\tan(B(x-C))+D$:
> 
> - **Sine & Cosine (wave-shaped, bounded):**
>   - **Amplitude:** the “height” of the wave is $|A|$. If $A<0$, the graph is reflected across its midline.
>   - **Period:** one full cycle has length $T = \dfrac{2\pi}{|B|}$.
>   - **Horizontal (phase) shift:** the basic graph ($\sin x$ or $\cos x$) is shifted left/right by $C$ units.
>   - **Vertical shift / midline:** the graph is moved up/down by $D$; the midline is the horizontal line $y = D$.
> 
> - **Tangent (unbounded, with asymptotes):**
>   - There is **no amplitude** (tangent is unbounded). The factor $|A|$ controls vertical stretch, and $A<0$ reflects the graph across the midline.
>   - **Period:** one repeating pattern has length $T = \dfrac{\pi}{|B|}$.
>   - **Horizontal shift:** the basic graph $\tan x$ is shifted left/right by $C$ units.
>   - **Vertical shift / midline:** the graph is moved up/down by $D$; the midline is $y = D$.
>   - **Vertical asymptotes:** occur where $B(x-C) = \dfrac{\pi}{2} + k\pi$ (for $k\in\mathbb{Z}$), i.e. at  
>     $x = C + \dfrac{\frac{\pi}{2} + k\pi}{B}$.
>   - In example graphs, the dotted lines mark two consecutive vertical asymptotes (e.g. $x = -\tfrac{3\pi}{4}$ and $x = \tfrac{\pi}{4}$), and the tangent branch between them shows the effect of the shift, stretch, and vertical translation.
