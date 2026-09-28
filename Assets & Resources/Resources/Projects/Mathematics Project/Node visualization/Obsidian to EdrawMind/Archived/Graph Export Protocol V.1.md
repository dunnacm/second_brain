---
type: protocol
project: MatheMagics
status: current
---
## Purpose

Use this protocol to create or update an EdrawMind map from an Obsidian project whose notes form a nonlinear hierarchy.

The protocol reproduces the method used to create **Logic - Linked Map**. It presents every note once as a complete branch and represents additional parentage with clickable reference topics. This preserves lattice-like relationships without duplicating entire branches or filling the map with relationship lines.

This document is also a prompt template for an AI assistant. Supply the project information below, then ask the assistant to follow the complete protocol.

## Project information

- **Operation:** Create or update
    
- **Obsidian source folder:** `[enter the folder containing the source notes]`
    
- **Map name:** `[Project Name] - Linked Map`
    
- **Existing map, if updating:** `[enter its path or write none]`
    
- **Preferred starting note:** `[enter the principal index note, if one exists]`
    

For **Logic - Linked Map**, the source folder is:

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\MatheMagics\Logic & Set Theory`

## Required output location

Save every newly created or updated mind-map file here:

`C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic`

This applies to mind maps produced from any Obsidian project.

Keep the Obsidian vault as the source of truth. Do not modify the source notes while producing a map unless the user separately requests those changes.

Do not place generated map files inside the Obsidian vault. The protocol note itself may remain in the vault.

### Preserved Logic reference files

The following known-good files are retained beside this protocol as historical references for the workflow that produced **Logic - Linked Map**:

- `Logic - Linked Map.mm` — the validated FreeMind import source, including its internal topic links.
- `Logic - Linked Map.emmx` — the corresponding native EdrawMind map.

These are reference copies rather than the destination for future work. Save every newly created or updated map in the Academic output folder specified above.

## Minimal deliverables

Normally create only:

1. `[Map Name].mm` — the importable FreeMind source.
    
2. `[Map Name].emmx` — the native EdrawMind document.
    
3. `[Map Name] Manifest.json` — a compact verification record, when an audit record is useful.
    

Do not create pilot files, duplicate exports, GraphML files, audit documents, or alternate maps unless the user asks for them.

If an existing map will be replaced, preserve it until the regenerated map passes verification. Do not delete an earlier version without the user’s instruction.

## Conceptual model

An Obsidian project may form a lattice rather than a strict tree. A note can have multiple parents, and a chain of notes can eventually return to an earlier note.

EdrawMind requires a tree for its visible topic structure. Therefore:

- Expand each internal Obsidian note as a complete topic exactly once.
    
- Treat that occurrence as the note’s **canonical topic**.
    
- When the same note occurs under another parent, create a terminal reference topic instead of duplicating its descendants.
    
- Link the reference topic to the canonical topic inside the EdrawMind document.
    
- Represent a cycle with a terminal return reference linked to the already expanded topic.
    
- Do not enumerate every possible spanning tree.
    
- Do not use large numbers of visible relationship lines unless the user specifically requests them.
    

This creates a readable tree projection while retaining the source hierarchy’s nonlinear connections.

## Reading the Obsidian relationship graph

Recursively examine every Markdown note in the selected source folder and its subfolders. Parse both the YAML properties and the complete note body. A note is not fully analysed until both sources have been scanned.

### YAML relationships

Treat YAML as the primary source for explicitly declared hierarchy:

- A note listed in `down` is a child of the current note.
- A note listed in `up` is a parent of the current note. Reverse the direction when constructing the hierarchy: the listed parent points to the current note.
- Preserve the listed order of `down` relationships when arranging children.
- Accept scalar values and YAML lists.
- Ignore empty `up` or `down` properties.
- Remove duplicate instances of the same relationship.

Record each resulting edge as an explicit YAML relationship.

### Note-body relationships

Scan the complete body of every note for:

- Obsidian wikilinks such as `[[Note]]`;
- aliased wikilinks such as `[[Note|label]]`;
- heading and block links such as `[[Note#Heading]]` and `[[Note^block]]`;
- embedded Markdown notes such as `![[Note]]`;
- ordinary Markdown links whose destination is another note in the vault;
- links contained in lists, tables, callouts, quotations, and inline fields outside the YAML block.

Ignore links inside fenced code blocks, inline code, HTML comments, and literal examples. Omit embedded images, audio, PDFs, and other non-note media unless the user requests them.

For each resolved body link from note A to note B:

1. Record the source note, target note, raw link, surrounding heading, containing sentence or list item, and source order.
2. Treat A → B as a candidate parent-child relationship.
3. Classify the link from its local context:
   - **Body hierarchy:** B is presented as a constituent, subtype, example, step, member, result, or narrower concept of A.
   - **Body reference:** B is cited for comparison, background, contrast, further reading, or another lateral purpose.
   - **Uncertain:** the context does not establish the relationship confidently.
4. Use a body-hierarchy edge to place B beneath A when no higher-priority YAML placement conflicts with it.
5. Represent an additional body-hierarchy parent with a terminal internal-link reference to B's canonical topic.
6. Represent a body-reference relationship as a terminal internal-link reference when it is useful to navigation, without changing B's canonical parent.
7. Report uncertain body links rather than silently treating them as hierarchy.

YAML hierarchy has priority over body-derived placement. When YAML and the body express the same edge, keep one edge and mark it as supported by both sources.

Example: if the body of `Constituent parts (material implication)` contains `[[Antecedent]]` and `[[Consequent]]` as its displayed constituent parts, both linked notes are children of that note even when their own YAML properties are empty.
    

## Resolving Obsidian links

Resolve each linked note conservatively.

Use this order:

1. Exact vault-relative path.
    
2. Exact path relative to the source note.
    
3. A unique matching path suffix or filename.
    

Remove aliases, headings, and block references for resolution while retaining the original link text as evidence.

Never guess when more than one note is a possible match. Represent unresolved cases as terminal topics:

- `[Title] — external note`
    
- `[Title] — missing note`
    
- `[Title] — ambiguous note`
    

External, missing, and ambiguous topics do not receive internal hyperlinks unless a valid destination is later established.

## Building the visible map

Create one synthetic central topic named after the project. It is a presentation container and does not represent an additional Obsidian note.

Under it:

1. Place the principal index or designated starting note first.
    
2. Add the remaining natural roots in a stable order only after the orphan audit described below.
    
3. Add any disconnected or cyclic components that have not yet appeared.
    
4. Expand every internal note exactly once.
    

For the Logic project, use the main `LOGIC` note as the preferred starting point when available.

The parent under which a shared note is first expanded becomes its presentation parent. This placement does not imply that it has only one conceptual parent.

Use these reference labels:

- Shared child: `[Title] — go to topic`
    
- Cycle returning to an ancestor: `[Title] — return to topic`
    

Reference topics must remain terminal leaves. Do not copy the canonical topic’s children beneath them.

### Orphan and synthetic-root audit

Before placing any source note directly beneath the synthetic central topic:

1. Check all resolved incoming YAML relationships.
2. Check all resolved incoming body-hierarchy relationships.
3. Check the note's outgoing body links and backlinks for contextual evidence of a parent.
4. Check aliases and path variants that may have prevented link resolution.
5. Attach the note beneath a real parent when the evidence supports one.
6. If more than one real parent is supported, choose one canonical placement using the precedence rules above and create linked reference occurrences under the others.
7. Place the note directly beneath the synthetic root only when no supported parent can be found.

List every remaining synthetic-root-only note in the completion report with the reason it could not be placed more specifically.

## Creating internal hyperlinks

Generate a unique document identifier for every topic occurrence in the FreeMind file.

Maintain a table connecting each Obsidian note’s stable identity to the identifier of its canonical expanded topic.

For every shared-child or cycle reference, add an internal FreeMind link to that canonical identifier. In the generated `.mm` file, the reference node should contain a link equivalent to:

`LINK="#canonical-topic-ID"`

The machine identifier belongs in the file structure only. Do not display it as part of the visible topic title.

This is the mechanism that produced the clickable references in **Logic - Linked Map**.

## Presentation

Use a restrained and consistent hierarchy:

- Central topic: large and bold.
    
- First-level topics: bold and clearly distinguished.
    
- Deeper topics: smaller but readable.
    
- Use a limited blue and purple branch palette when no existing project style is supplied.
    
- Use a common font such as Arial.
    
- Keep note titles intact, including Unicode and mathematical symbols.
    
- Keep reference labels visibly distinct through their wording rather than excessive decoration.
    

A user may restyle the native `.emmx` map afterward without changing the hierarchy.

## Importing into EdrawMind

1. Generate the `.mm` file in the required Academic output folder.
    
2. In EdrawMind, select **Import**.
    
3. Select the generated `.mm` file.
    
4. Confirm that the central topic, branches, and reference topics appear.
    
5. Test several reference topics by activating their hyperlink icons.
    
6. Save the imported map as `[Map Name].emmx` in the same Academic folder.
    

Use EdrawMind’s import function for the `.mm` file. Do not rely on opening it as an ordinary document.

## Mind-map upkeep

Use this procedure whenever the user asks the AI assistant to update an existing map after changes in Obsidian. The Obsidian notes remain authoritative, and the mind map remains a generated snapshot.

### Establish the baseline

1. Read the current Obsidian source folder recursively.
2. Locate the current `.mm` and `.emmx` files in the Academic output folder. Use the preserved Logic reference files only if the current files are missing.
3. Parse the current `.mm` file before generating its replacement. Record its canonical note identities, topic identifiers, reference links, topic count, and hyperlink count.
4. Reconstruct the current Obsidian relationship graph from the `up` and `down` properties and from a complete scan of every note body.
5. Compare the reconstructed hierarchy with the existing map and identify:
   - added, removed, and renamed notes;
   - added, removed, and reordered YAML hierarchy edges;
   - added, removed, and reclassified body-derived relationships;
   - newly shared children;
   - cycles that appeared or disappeared;
   - links that became missing, external, or ambiguous.
6. Do not modify the Obsidian source notes during this comparison unless the user separately asks for corrections.

### Generate the update

1. Preserve the existing canonical topic identifier for every unchanged note whenever practical.
2. Generate new identifiers only for new topic occurrences and references.
3. Remove a topic only when its source note or hierarchy edge is absent from the current source. Report uncertain rename matches instead of guessing.
4. Preserve the order of explicit `down` entries and the source order of body-derived child links. Apply the protocol's stable ordering rules to roots and disconnected components.
5. Run the orphan and synthetic-root audit again using the current YAML properties, body links, and backlinks.
6. Recalculate every shared-child, body-reference, and cycle occurrence so that its hyperlink points to the current canonical topic.
7. Regenerate the complete `.mm` file. Do not directly edit the native `.emmx` file as the primary update method.

### Protect the working map

1. Write the regenerated import file as `[Map Name] - Candidate.mm` in the Academic output folder.
2. Keep the current `.mm` and `.emmx` files until the candidate passes structural and EdrawMind verification.
3. Import the candidate into EdrawMind and save it as `[Map Name] - Candidate.emmx`.
4. Check whether user-applied layout or styling from the previous native map needs to be restored.
5. After verification, replace the canonical `[Map Name].mm` and `[Map Name].emmx` files with the accepted candidate.
6. Delete candidates or earlier versions only when the user asks for that cleanup.

### Verify and report the change

Run every check in **Verification requirements** against the candidate. Compare the new totals with the baseline and report the differences. Test hyperlinks involving at least one newly added or changed relationship, one shared child, and one cycle when those cases exist.

The completion report must state:

- which notes and hierarchy relationships changed;
- which changes came from YAML and which came from note bodies;
- which body links were classified as hierarchy, references, or uncertain;
- which notes remain directly under the synthetic root and why;
- whether stable topic identifiers were preserved;
- the old and new topic and hyperlink totals;
- where the candidate and accepted files were saved;
- whether EdrawMind import, layout review, and hyperlink testing passed.

### Reusable upkeep prompt

> Update **[Map Name]** from the current Obsidian notes in **[source folder]**. Follow the **Mind-map upkeep** section of this protocol. Parse the YAML `up` and `down` properties and scan the complete body of every note for internal links. Classify body links as hierarchy, reference, or uncertain; run the orphan and synthetic-root audit; compare the result with the existing `.mm` map; preserve stable topic identifiers where practical; and rebuild all canonical and reference topics. Save candidate files in `C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic`. Do not alter the source notes or overwrite the accepted map until the candidate passes structural checks and EdrawMind import testing. Report every added, removed, renamed, unresolved, or synthetic-root-only note and every material relationship change.

## Verification requirements

Before reporting completion, verify that:

- Every source note is represented.
    
- Every YAML hierarchy edge appears either as ordinary parent-child placement or as a clickable reference.

- Every note body was scanned and every resolvable internal note link was recorded.

- Every body-derived link has a recorded classification: hierarchy, reference, or uncertain.

- Every body-hierarchy edge appears either as ordinary parent-child placement or as a clickable reference.

- Every note placed directly beneath the synthetic root passed the orphan audit.
    
- Every internal note has exactly one complete canonical expansion.
    
- Reference topics have no copied descendants.
    
- All topic identifiers are unique.
    
- Every internal hyperlink points to an existing canonical topic.
    
- Titles and mathematical symbols survived XML generation.
    
- The `.mm` file is valid XML.
    
- EdrawMind successfully imports the full map.
    
- The EdrawMind outline count agrees with the generated topic count.
    
- Several shared-child links and at least one cycle link work when applicable.
    
- The original Obsidian source files remain unchanged.
    

Separate structural validation from application validation. A syntactically valid `.mm` file is not considered complete until it imports and its hyperlinks work in EdrawMind.

## Legacy reference snapshot: Logic - Linked Map

The validated generation of **Logic - Linked Map** produced:

- 286 source notes
    
- 345 hierarchy edges
    
- 394 visible topics, including the synthetic central topic
    
- 98 internal hyperlinks
    
- One complete expansion for each internal note
    

These figures describe the source at the time of generation. If the source notes have changed, report the new figures and explain the differences rather than forcing the old totals.

This snapshot was generated before complete note-body scanning became mandatory. It is retained as a technical reference for the working hyperlink format, but its hierarchy is not a compliant baseline for a future Logic map. A rebuilt Logic map must scan every note body and is expected to produce different placement and relationship totals.

## Completion report

When finished, report:

- Source folder examined
    
- Map name
    
- Number of source notes
    
- Number of YAML hierarchy edges

- Number of body-hierarchy relationships

- Number of body-reference relationships

- Number of uncertain body links
    
- Number of visible topics
    
- Number of shared-child references
    
- Number of cycle references
    
- Missing or ambiguous links

- Notes placed directly beneath the synthetic root, with reasons
    
- Files created or updated
    
- Results of the EdrawMind import and hyperlink tests
    

Keep the report concise. Do not produce additional protocol or audit documents unless requested.

## Prompt for the AI assistant

Follow the complete protocol in this document.

Create or update the specified EdrawMind linked map from the specified Obsidian source folder. Parse the YAML `up` and `down` properties, then scan the complete body of every note for wikilinks, embedded note links, and Markdown links to other notes. Classify body-derived links as hierarchy, reference, or uncertain. Use supported body-hierarchy links to place notes that would otherwise appear as orphans, and represent additional parentage, lateral references, or cycles with terminal topics that hyperlink to the canonical topic.

Do not place a note directly beneath the synthetic root until its YAML relationships, body links, backlinks, aliases, and path variants have been audited.

Save all generated or updated mind-map files in:

`C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic`

Keep the deliverables minimal. Do not alter the Obsidian source notes, delete existing maps, or create additional export formats unless I explicitly request it. Validate the generated structure, import it into EdrawMind when application access is available, test representative internal hyperlinks, and provide the concise completion report defined above.
