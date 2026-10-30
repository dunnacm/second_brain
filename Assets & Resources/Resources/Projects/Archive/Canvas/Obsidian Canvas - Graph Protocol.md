---
type: protocol
project: MatheMagics
status: current
---

## Purpose and present project

Create and maintain a native Obsidian Canvas from a project's notes. The preferred design is the existing [[Logic - Shared Concept Pilot.canvas|shared-concept pilot]]: one live file card per note, with direct arrows between related concepts.

If A connects to B and C, and both B and C connect to D, display D once and draw both incoming arrows. Preserve cycles as direct connections. Every source note belongs in the full Canvas, including disconnected notes.

This is the governing manual for the Canvas workflow. It replaces the EdrawMind method for current visualization work. The earlier maps remain historical references.

The current project is [[Logic & Set Theory.canvas|Logic & Set Theory]]. Its source is `MatheMagics/Logic & Set Theory`, including subfolders, in the `second_brain` vault. A note's YAML properties and its complete body both supply relationship evidence.

## Location and essential files

Keep the governing manual, Canvas, and maintenance record together in:

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\Systems and Resources\Resources\Projects\Mathematics Project\Node visualization\Canvas`

The essential working files are:

- `Obsidian Canvas - Graph Protocol.md`: this manual, including the reusable prompt below.
- `Logic & Set Theory.canvas`: the complete native Canvas.
- `Logic & Set Theory.manifest.json`: source identities, relationship evidence, reviewed body-link classifications, unresolved destinations, and verification results.
- `_tools/build_canvas.py`: the repeatable scanning and layout helper. Keep it with the workflow.

The shared-concept pilot remains the visual reference. Avoid additional export formats, duplicate maps, or separate audit notes unless requested. Native Canvas files belong inside the vault so their file cards can resolve to the notes; the earlier Academic export destination applies to the historical EdrawMind workflow.

## How the user navigates and maintains the Canvas

1. Open `Logic & Set Theory.canvas` in Obsidian. No import is necessary.
2. Press **Shift+1** to see the whole Canvas. The full graph is an overview; zoom in to read individual cards.
3. Hold **Space** and drag to pan. Hold **Ctrl** and use the mouse wheel to zoom.
4. Select a card and press **Shift+2** to focus on it. To follow a distant connection, right-click the line and choose **Go to target** or **Go to source**.
5. Move or resize cards to improve their arrangement. The next upkeep run should preserve the positions and sizes of unchanged cards.
6. Edit relationships in the notes when they should become part of the project's source structure. A line drawn manually on the Canvas does not add an `up`, `down`, or body link to either note.
7. Ask the assistant to update the Canvas after adding, renaming, removing, or relinking notes. The cards display live note content, but the connections and placement require an upkeep run.

File cards display the original notes. Editing a note's content through its Canvas card edits that note. Moving a card changes only its position on the Canvas.

### Connection legend

| Appearance | Meaning |
|---|---|
| Cyan arrow | Explicit YAML hierarchy, possibly also supported by the body |
| Purple arrow | Reviewed hierarchy established by a note's body |
| Green arrow, labelled `reference` | A background, comparison, citation, or other lateral link |
| Orange arrow, labelled `uncertain` | A body link whose relationship needs contextual review |
| Red card or connection | A missing or ambiguous destination |
| Green-bordered file card | A real note outside the selected source folder |

Hierarchy arrows run from parent to child. Reference arrows run from the note containing the link to its destination; they do not assert parenthood. A group is a layout container. Do not add connections merely to make every card look connected.

## Instructions for the AI assistant

### 1. Establish scope and baseline

Read this manual, the supplied visual example, the current `.canvas`, and its matching manifest. Confirm the source folder and recursively inventory every Markdown note. Record hashes of the source files before work.

For this project, use the `second_brain` vault and the complete `MatheMagics/Logic & Set Theory` folder. Preserve all source notes while building the visualization. Correct a source note only when the user requests that correction separately.

### 2. Read YAML properties and every note body

- `down` declares children: current note → listed note.
- `up` declares parents: listed note → current note.
- Accept scalar and list values; ignore empty values. Preserve explicit source order when practical.
- Scan the complete body for wikilinks, aliases, heading and block links, note embeds, ordinary Markdown links, and reference-style Markdown links. Include links in headings, lists, tables, callouts, quotations, footnotes, and inline fields.
- If other YAML properties contain note links, record them as references unless the property has an explicitly established hierarchy meaning.
- Ignore fenced and inline code, comments, literal examples, and non-note media. Retain same-note heading links in the maintenance record without drawing redundant note-to-itself loops.

For each body link, record the source, raw link, destination, surrounding heading, containing line, and source order. Classify it as **hierarchy**, **reference**, or **uncertain** from its actual context. A link alone does not establish hierarchy. Review new or changed evidence; do not silently infer a parent from a title or reuse a classification after its supporting context has changed.

If YAML and a body link support the same directed hierarchy relationship, draw one arrow and keep both sources of evidence. If a lateral link coincides with an explicit YAML hierarchy, preserve that hierarchy and record the lateral evidence in the manifest.

The helper's saved body decisions apply only to matching evidence signatures. New or changed body evidence defaults to `uncertain`. Inspect the surrounding notes, enter the reviewed classification and reason in the matching manifest record, and rebuild before declaring the update complete.

### 3. Resolve destinations conservatively

Resolve vault-relative paths, paths relative to the linking note, unique path suffixes or filenames, and established note aliases. Remove display aliases, headings, and block suffixes only for file resolution; retain the original link in the evidence.

Never choose between ambiguous destinations. Display a labelled warning card for a missing or ambiguous target. A resolved note outside the source folder may appear once as a green-bordered boundary card; do not recursively expand its own project.

Any approved path or encoding correction must be explicit in the helper and recorded in the manifest. Do not silently use approximate title matching. The known corrupted XOR link is resolved through a reviewed correction without changing the original note.

### 4. Construct the actual graph

Create exactly one native `file` card for each source note, using its vault-relative path. Retain a stable card identifier wherever possible. Draw every resolved relationship directly between the appropriate cards.

Preserve all supported parents of a shared child, and all source-defined cycles. There are no duplicate branch expansions, terminal “go to topic” cards, or artificial central-parent connections. Keep titles and mathematical symbols intact.

Arrange connected concepts from top to bottom where the hierarchy allows it. Keep cyclic concepts near each other. Use consistent card dimensions, restrained colours, adequate spacing, and as few line crossings as practical. Audit incoming YAML links, incoming and outgoing body links, aliases, and path variants before treating a note as disconnected. Group genuinely disconnected notes for review without inventing connections.

### 5. Update while preserving the user's arrangement

Rebuild from the current notes each time. Compare the new inventory and directed relationships with the previous manifest. Report additions, removals, changed classifications, and unresolved destinations.

Preserve unchanged file-card IDs, positions, sizes, colours, and user annotations. Confirm renames from explicit user information or unique evidence before transferring an identity; report uncertain matches. Do not infer a rename solely from a similar filename.

Write an update as `[Map Name] - Candidate.canvas` with its corresponding candidate manifest. Keep the accepted Canvas available while verifying the candidate. Review new-card placement and group boundaries if preserved positions conflict with the generated layout. Use a complete relayout only when the user requests it or accepts that arrangement change.

After verification, update the accepted Canvas and its matching manifest together. Retain a recoverable previous version or existing version-control history. Do not delete historical maps or candidates as incidental cleanup.

### 6. Verify structure and the Obsidian display

Before reporting completion, confirm:

- Every source note appears exactly once and every file card resolves.
- Every explicit YAML relationship and every resolved body link is accounted for by a direct connection, a documented same-note link, or a labelled unresolved destination.
- Every body link has a classification and supporting evidence.
- All card and connection identifiers are unique, and all connection endpoints exist.
- JSON serialization preserves paths, Unicode, and mathematical symbols.
- No source note changed during generation.
- The initial layout has no overlapping cards; preserved-layout conflicts are reported and reviewed.
- Obsidian opens the Canvas, file cards render, shared-child connections appear, and a representative body-derived relationship and cycle remain visible.

Keep structural validation separate from application validation. Record any unperformed check rather than claiming it passed. Report the actual current totals, rather than forcing the numbers from an older map.

## Repeatable helper

The helper uses Python's standard library. From the vault root, an assistant may inspect the current evidence with:

```powershell
python "Systems and Resources/Resources/Projects/Mathematics Project/Node visualization/Canvas/_tools/build_canvas.py" --inspect
```

To build or refresh this project's Canvas:

```powershell
python "Systems and Resources/Resources/Projects/Mathematics Project/Node visualization/Canvas/_tools/build_canvas.py"
```

The first build creates the working Canvas; subsequent runs create candidates. `--source` and `--name` select another project. `--relayout` replaces the computed card arrangement and should be used only within the layout authority described above.

The helper handles the current vault's simple scalar/list YAML properties, ordinary and reference-style Markdown links, and wikilinks in other YAML properties. It stops if a hierarchy property uses unsupported YAML syntax. Extend the helper or use an appropriate YAML parser before completing such a refresh. Unchanged cards retain their IDs and placement; a uniquely matched unchanged content hash can establish a rename. Other rename cases require review. The helper is an implementation aid; these protocols and contextual review govern the result.

## Reusable prompt for upkeep or a new chat

> Create or update the Obsidian Canvas for **[project name]** from all Markdown notes in **[source folder]**. Follow `Obsidian Canvas - Graph Protocol.md` in the Mathematics Project's `Node visualization/Canvas` folder. Read the current Canvas and manifest, parse YAML properties, and scan the complete body of every note. Review new or changed body links as hierarchy, reference, or uncertain. Represent each source note once as a live file card; draw all supported relationships directly, including multiple parents and cycles. Audit disconnected notes without inventing parents. Preserve my existing card IDs, positions, sizes, colours, and annotations where practical. Save the Canvas, matching manifest, and any necessary helper changes in that Canvas folder. Verify file paths, connections, source integrity, and the Obsidian display. For an update, verify a candidate before replacing the working Canvas and manifest together. Report the changes and remaining unresolved cases concisely.

For the current Logic project, replace the placeholders with **Logic & Set Theory** and **MatheMagics/Logic & Set Theory**.

## Technical references

Native file structure: [JSON Canvas specification](https://jsoncanvas.org/spec/1.0/). Navigation and card behaviour: [Obsidian Canvas documentation](https://obsidian.md/help/plugins/canvas).
