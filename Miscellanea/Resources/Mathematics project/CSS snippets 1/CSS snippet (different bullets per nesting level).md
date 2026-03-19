```css
/* Apply ONLY to the dataview MOC output wrapper */
.moc-tree ul { 
  margin: 0;
  padding-left: 1.35em;
}

/* Use custom markers by depth (matches “varying bullet shapes” look) */
.moc-tree ul > li::marker { content: "•  "; }
.moc-tree ul ul > li::marker { content: "○  "; }
.moc-tree ul ul ul > li::marker { content: "■  "; }
.moc-tree ul ul ul ul > li::marker { content: "□  "; }
.moc-tree ul ul ul ul ul > li::marker { content: "◆  "; }
.moc-tree ul ul ul ul ul ul > li::marker { content: "◇  "; }
.moc-tree ul ul ul ul ul ul ul > li::marker { content: "▶  "; }
.moc-tree ul ul ul ul ul ul ul ul > li::marker { content: "–  "; }

/* Optional: make markers slightly bolder/larger */
.moc-tree li::marker { 
  font-weight: 700;
  font-size: 1.05em;
}
```

