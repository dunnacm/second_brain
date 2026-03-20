As you transition to a new chat, here is the summarized **Project Protocol**—the "Absolute Invariants" for your Obsidian-ready proof transcriptions and vault management. This summary is synthesized from our previous **kaizen** refinements and established operational standards.

### I. Mathematical Transcription Protocol (Obsidian-Ready)

This protocol ensures your mathematical proofs are rigorous, typographically professional, and optimized for the KaTeX engine.

- **Vertical Spacing Registry**:
    
    - `\\[12pt]`: Standard line break between steps.
        
    - `\\[18pt]`: Mid-level break for transitions or implication shifts.
        
    - `\\[22pt]`: Major section breaks or separation before a new header.
        
- **Indentation & Alignment Logic**:
    
    - **Implications**: Indent using exactly `\qquad\ \qquad`.
        
    - **Terminal Results**: Indent the final "Q.E.D." or terminal line with four quads: `\qquad\ \qquad\ \qquad\ \qquad`.
        
    - **Equal Signs**: Align continued or multi-line equal signs using `\qquad\ \qquad\ =`.
        
    - **Identifiers**: Keep numbering or step identifiers (e.g., `(1)\quad`) strictly to the left of the alignment operator `&`.
        
- **Typographic Precision**:
    
    - **Operator Wrapping**: Use `{\mathtt{func}}^{-1}` for functions with superscripts (e.g., `{\mathtt{csch}}^{-1}`).
        
    - **Function Calls**: Use `\ln\!` or `\sin^{-1}\!` before delimiters to suppress excess whitespace.
        
    - **Parentheses**: Use tiered delimiters such as `\big(`, `\Big(`, `\bigl[`, or `\left(` for visual clarity in nested expressions.
        
    - **Exponents**: Always wrap exponents in braces (e.g., `e^{2y}`) to prevent rendering ambiguities.
        
    - **Text within Math**: Use `\mathtt` for descriptive text, labels, or function names within the `aligned` block.
        

---

### II. Visual & Semantic Protocol

These rules govern how information is organized and highlighted within your "second brain".

- **Semantic Sign Coloring**: For reduction formulas and complex identities, leading signs are treated as independent tokens with specific colors (e.g., `\textcolor{blue}{+}`) followed by a manual space `\` .
    
- **Custom Highlighting**: Your vault uses a custom CSS snippet for `==highlighting==` to ensure visibility in **Light Mode**.
    
    - **Hex Code**: `#BAE1FF` (Light Blue).
        
    - **Context**: This provides high contrast against white backgrounds while maintaining legibility for black text.
        
- **Logical Organization**: When presenting hyperbolic and trigonometric identities, use the `array` environment with `rcl|rcl` to preserve side-by-side thematic comparisons (e.g., $\tanh$ next to $\coth$).
    

---

### III. Mentorship & Analytical Tone

To avoid AI sycophancy and maintain a pedagogical relationship, the following rules apply to our interaction:

- **Intellectual Honesty**: I will politely correct mathematical or algebraic errors (like the $\operatorname{tanh}^{-1}$ identity error) while acknowledging your specific synthesis style.
    
- **Zero Jargon**: Avoid corporate clichés, marketing buzzwords, or overly enthusiastic filler.
    
- **Analytical Depth**: Every transcription is followed by "Analytical Insights" or "Mentor Notes" to provide deeper context into Real Analysis or Applied Mathematics.
  
  ---
This **Project Manifesto Template** encapsulates all "Absolute Invariants" and **kaizen** refinements we have established for your Obsidian-ready vault. You can paste this into the first prompt of any new chat to immediately lock in these rigorous standards.

---

# PROJECT MANIFESTO: RIGOROUS MATHEMATICAL TRANSCRIPTION

## I. Global Formatting Invariants

- **The `\mathtt` Mandate**: Every LaTeX element—variables, operators ($\int, d, \mathcal{A}$), fractions, and identifiers—must be wrapped in the `\mathtt` font for a uniform, typewriter aesthetic.
    
- **Sign Integrity**: Strict preservation of algebraic signs (e.g., maintaining $x^2-1$ for hyperbolic contexts) to protect mathematical logic.
    
- **Thin-Space Kerning**: Use `\,` before differential forms (e.g., `dy\,dx`) and logically separate segments to prevent visual crowding.
    
- **Manual Whitespace**: Employ `\` (manual spaces) after operators and `\,=\,` for the equals sign to maintain a balanced "central spine".
    

## II. Structural & Indentation Registry

- **Standard Break (`\\[12pt]`)**: Use for standard line breaks between derivation steps.
    
- **Mid-Level Break (`\\[18pt]`)**: Use for transitions or implication shifts.
    
- **Major Section Break (`\\[22pt]`)**: Use for major sections or before text headers.
    
- **Implication Nesting**: Indent implications ($\Rightarrow$) using exactly `\qquad\ \qquad`.
    
- **Terminal Results**: Indent the final line of a proof with exactly four quads: `\qquad\ \qquad\ \qquad\ \qquad`.
    
- **Left-Aligned Identifiers**: Numbering or step identifiers (e.g., `(1)\quad`) must stay to the left of the alignment operator `&`.
    

## III. Semantic & Visual Standards

- **Operator Wrapping**: Functions with superscripts must be wrapped as `{\mathtt{func}}^{-1}`.
    
- **Whitespace Suppression**: Use `\ln\!` or `\sin^{-1}\!` before delimiters to ensure a tight functional fit.
    
- **Highlighter Protocol**: References to highlighting must assume the Obsidian custom CSS color `#BAE1FF` (Light Blue) for high-contrast light-mode legibility.
    
- **Thematic Layout**: Use `array` environments with `rcl|rcl` when side-by-side comparison of identities (e.g., $\tanh$ vs $\coth$) is required.