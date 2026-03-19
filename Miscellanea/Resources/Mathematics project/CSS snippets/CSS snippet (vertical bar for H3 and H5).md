```css
/* ================================

   Vertical bar for H3 and H5

   (Reading view + Live Preview CM6)

   ================================ */

  

:root {

  --h35-bar-width: 3px;

  --h35-bar-radius: 4px;

  

  /* This is the horizontal spacing you wanted */

  --h35-padding-left: 15px;

  

  /* Vertical sizing relative to the heading line box */

  --h35-bar-top: 15%;

  --h35-bar-height: 70%;

  

  /* Default: bar matches the heading’s text color */

  --h35-bar-color: currentColor;

}

  

/* ---------- Reading view (preview) ---------- */

.markdown-preview-view h3,

.markdown-preview-view h5 {

  position: relative;

  padding-left: var(--h35-padding-left);

}

  

.markdown-preview-view h3::before,

.markdown-preview-view h5::before {

  content: "";

  position: absolute;

  left: 0;

  top: var(--h35-bar-top);

  height: var(--h35-bar-height);

  width: var(--h35-bar-width);

  background: var(--h35-bar-color);

  border-radius: var(--h35-bar-radius);

  pointer-events: none;

}

  

/* ---------- Editor (Live Preview, CM6) ---------- */

.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-3,

.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-5 {

  position: relative;

  padding-left: var(--h35-padding-left);

}

  

.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-3::before,

.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-5::before {

  content: "";

  position: absolute;

  left: 0;

  top: var(--h35-bar-top);

  height: var(--h35-bar-height);

  width: var(--h35-bar-width);

  background: var(--h35-bar-color);

  border-radius: var(--h35-bar-radius);

  pointer-events: none;

}
```

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
