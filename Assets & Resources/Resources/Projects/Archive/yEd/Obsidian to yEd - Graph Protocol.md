---
type: protocol
project: MatheMagics
status: current
---

# Obsidian to yEd — Graph Protocol

## Purpose and present decisions

Use **yEd Graph Editor for desktop** to study the relationships in `MatheMagics/Logic & Set Theory`, including all its subfolders, in the `second_brain` Obsidian vault. Every note appears once. Several parents can connect to the same child, and cycles remain visible. This is a directed graph; do not reduce it to a duplicated branching outline.

The user chose a **Neighborhood panel that follows the clicked concept and shows its immediate incoming and outgoing neighbors**. Hierarchical layout is the starting arrangement; Organic is an alternative for exploring densely connected concepts.

**Evaluation status:** the user is still assessing whether this yEd workflow meets their needs. They explicitly chose to leave the current arrangement unsaved for now. Treat the desktop setup as a trial, not an accepted workflow. Resume with the user's assessment before further setup or upkeep. Do not prompt them to save again unless they decide to retain the arrangement; do not regenerate or reopen a graph over their current unsaved trial.

The Supply Chain and Layout Styles demonstrations belong to the separate **yFiles programming library**. Supply Chain highlights a product's flow. Its behavior is not a promise that desktop yEd automatically highlights an entire connected component in the main drawing. The agreed desktop substitute is the selection-driven Neighborhood panel. No yFiles license, custom application, or paid product is necessary for this workflow. [Supply Chain demo](https://live.yworks.com/demos/showcase/supply-chain/), [Layout Styles showcase](https://www.yworks.com/pages/interactive-showcase-of-graph-layouts)

### What changed in the visualization section

The user moved Canvas and the earlier EdrawMind protocol into `Node visualization/Archived`. The old `Logic - Linked Map.emmx`, `.mm`, and `Logic & Set Theory Outline.md` remain in the parent folder. They are historical references. The outline is a tree projection and must not become the relationship source for this graph. Leave these files and the archives intact unless the user requests cleanup.

## Working files and locations

This manual belongs in:

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\Systems and Resources\Resources\Projects\Mathematics Project\Node visualization\yEd`

Keep these four essential files, with these responsibilities and locations:

- `Obsidian to yEd - Graph Protocol.md`: this governing manual, setup instructions, upkeep, and future prompt.
- `Logic & Set Theory.graphml`: the working graph, opened directly in desktop yEd; save in `C:\Users\dunnc\OneDrive\Desktop\Obsidian to yEd`.
- `Logic & Set Theory.manifest.json`: source hashes, stable identities, relationship evidence, body-link decisions, unresolved destinations, and changes; keep beside the working graph in that same Desktop folder.
- `_tools/build_yed_graph.py`: the self-contained helper that scans the notes and produces GraphML. It does not depend on `Archived` or on a community plugin.

Use **GraphML** for the working file. It retains relationships, presentation, and custom properties when opened and saved in yEd. A PDF, SVG, or picture is a viewing export and does not replace the working graph. Keep the manifest paired with its graph. [yEd file formats](https://yed.yworks.com/support/manual/fileformat.html)

The user chose **`C:\Users\dunnc\OneDrive\Desktop\Obsidian to yEd`** for working graphs and their manifests. This replaces the earlier Academic destination for the new yEd workflow. Keep protocols and the helper in this vault folder. The helper defaults to the chosen Desktop destination; do not create competing working copies in the vault. Candidates and dated backups also belong beside the working graph.

## First use in desktop yEd

If yEd is not installed, download **yEd Graph Editor**, the desktop application, from the [official yEd page](https://www.yworks.com/products/yed). The user completes any license agreement. Do not install yFiles as a substitute.

When guiding the user in chat, give **one step at a time** and wait for their result. Group all relevant settings within the same tab into that step; do not ask for a separate confirmation after every checkbox. The list below is the complete reference sequence.

1. Open yEd and choose **File → Open**. Select `C:\Users\dunnc\OneDrive\Desktop\Obsidian to yEd\Logic & Set Theory.graphml`. GraphML needs no mind-map import conversion.
2. If the graph opens as a grid, apply **Layout → Hierarchical** using the settings below. The grid only provides nonidentical starting positions; it is not the proposed finished arrangement.
3. Open **Window → Context Views → Neighborhood**. Keep this panel beside the main drawing.
4. In **File → Preferences → Display**, set **Context Views Update Trigger** to selection. Enable **Hierarchy Aware Context Views** if you later collapse groups, so the panel can still show actual neighboring concepts. If a busy concept makes the panel empty, check its maximum-node and maximum-edge limits. These are application preferences, not embedded GraphML settings. [Display preferences](https://yed.yworks.com/support/manual/yed_file_preferences.html)
5. Select `Constituent parts (material implication)`. The Neighborhood panel should include `Antecedent` and `Consequent`. Select a node in that panel to center and select its counterpart in the main drawing. Both incoming and outgoing neighbors appear; green reference connections are also neighbors and do not mean parenthood. The panel can include connections among those neighbors too. [Context views](https://yed.yworks.com/support/manual/localviews.html)
6. Select `Types of validity`. Confirm that both `Propositional logic (PL)` and `First-order logic (FOL)` connect to the same single node. This is the acceptance check for shared children.
7. Select a real note, right-click it, and choose **Go to URL** to open it in Obsidian. The graph stores an encoded `obsidian://open` link using the vault name `second_brain` and the complete vault-relative path. If Windows does not open Obsidian, test the registered Obsidian handler; the note is not missing merely because the handler fails. [URLs and node properties](https://yed.yworks.com/support/manual/properties.html)
8. Save in **GraphML** at the working location. Save layout and presentation changes before asking for an update, then close the graph during regeneration so an unsaved yEd session cannot overwrite the new file.

### Highlight the connecting lines in the main graph

Desktop yEd's Neighborhood panel follows the selected concept, but selecting a node does not automatically highlight its incident lines in the main drawing. For temporary main-graph highlighting, select the concept and open **Tools → Select Elements**. On **General**, enable only **Clear Selection First**. Enable **Use These Criteria** only on **Edges**, and set **Select** to **Selected Nodes**. Apply the command. This selects the incoming and outgoing lines and replaces the node selection; rerun the command for each new concept. It does not recolor the underlying evidence or remain active as a click listener. [yWorks explanation of desktop edge highlighting](https://yed.yworks.com/support/qa/29786/ability-highlight-edges-when-selecting-node-desktop-version?show=29802)

This selection includes references as well as hierarchy connections. Follow the evidence legend when interpreting them. If automatic highlighting in the main drawing remains essential, treat it as an unmet interaction requirement and revisit a suitable viewer; do not promise that changing the GraphML or layout settings will add it.

### Layout choices

For the first **Hierarchical** arrangement, use **Top to Bottom**, consider node labels, arrange components separately, and try **Orthogonal** edge routing with **Backloop Routing**. Start with automatic edge grouping disabled so separate parent connections are easy to inspect; enable it later if the drawing becomes too wide. Suggested starting distances are 35 between adjacent nodes and 70 between layers. These numbers are preferences, not mathematical constraints. Cycles remain in the data even when their arrows curve back against the overall direction. [Hierarchical layout](https://yed.yworks.com/support/manual/layout/layout_hierarchic_incremental.html)

Try **Layout → Organic** when you want to discover clusters and hubs. Use no preferred direction, disallow overlapping nodes, consider labels, and start with a moderate quality setting. Natural clustering is worth trying as a visual aid; its clusters are not mathematical categories. Undo an unsatisfactory result. Save the preferred arrangement in the existing GraphML rather than accumulating alternative full maps. [Organic layout](https://yed.yworks.com/support/manual/layout/layout_smartorganic.html)

Tree and balloon layouts can be useful for a genuinely tree-shaped local selection. They are not the default for this project because several concepts have multiple parents. Layout changes must never remove a connection, reverse its meaning, or duplicate a shared child.

## Further capabilities worth using

| Capability | Use in these notes | Protocol |
|---|---|---|
| Neighborhood | Immediate parents, children, and lateral links of the selected concept | Default navigation panel. Read arrow direction and evidence color. |
| Predecessors / Successors | Follow longer paths backward or forward | Optional context views. Reference edges also participate, so a reachable node is not necessarily a conceptual ancestor. |
| Convert to Document | Study a local cluster without the complete graph | Context-panel command. A derived view is a snapshot; rebuild it after source changes. Avoid maintaining a second authoritative graph. |
| Structure View and Find | Locate a concept in a large map | Use the Structure View's prefix search, or **Edit → Find** for more choices. Double-click an entry to center its node. [Structure View](https://yed.yworks.com/support/manual/structure.html) |
| Overview | Keep your bearings while zoomed in | Keep the overview visible and move its viewport rectangle. [Overview](https://yed.yworks.com/support/manual/overview.html) |
| Expandable groups | Temporarily fold a topic region | Use groups for presentation only. A shared child still has one node and can belong to only one containment group; its cross-group edges remain meaningful. Start without groups, then add them only where they help. [Grouping](https://yed.yworks.com/support/manual/hierarchy.html) |
| Partial / incremental layout | Fit added concepts into a familiar drawing | Rearrange the changed selection rather than laying out everything afresh. [Partial layout](https://yed.yworks.com/support/manual/layout/layout_partial.html) |
| Edge routing and label placement | Improve clutter without moving all nodes | Use the corresponding Layout tools on a saved graph. Check that every endpoint stays correct. [Layout tools](https://yed.yworks.com/support/manual/layout.html) |
| Properties Mapper | Show a chosen graph property through color or style | Useful for `sb_status` or `sb_kind`; keep the evidence legend meaningful. Applying a mapping changes the drawing at that moment, not an ongoing Obsidian synchronization. [Properties Mapper](https://yed.yworks.com/support/manual/properties_mapper.html) |
| Graph analysis | Detect cycles, components, and structural hubs | Useful diagnostics. Centrality measures graph connectivity, not a concept's mathematical importance. [Analysis tools](https://yed.yworks.com/support/manual/yed_tools.html) |

I also examined the **Neighborhood View**, **Flow Filtering**, **Graph Viewer**, and **Interactive Aggregation** demos. Neighborhood View closely matches the agreed navigation goal. Flow Filtering is useful inspiration for future upstream/downstream exploration; Graph Viewer demonstrates hover emphasis and search; aggregation can simplify very large diagrams. Their exact scripted interactions belong to yFiles and are not installed by importing a GraphML file into desktop yEd. Start with desktop context views and ordinary grouping; revisit a custom viewer only if those prove insufficient. [Neighborhood demo](https://www.yfiles.com/demos/showcase/neighborhood/), [Flow Filtering](https://live.yworks.com/demos/application-features/flow-filtering/), [Graph Viewer](https://live.yworks.com/demos/view/graphviewer/), [Interactive Aggregation](https://live.yworks.com/demos/application-features/interactiveaggregation/index.html)

## Connection legend and source authority

| Appearance | Meaning |
|---|---|
| Blue arrow | Explicit YAML hierarchy, possibly also supported by body links |
| Purple arrow | Hierarchy established by reviewed body context |
| Green arrow labelled `reference` | Background, comparison, citation, or other lateral relation |
| Dashed orange arrow labelled `uncertain` | New or changed body evidence awaiting review |
| Red or amber warning node / dashed red connection | Missing or ambiguous destination; not an actual source note |
| Green-bordered node | Real note outside the selected source folder; its project is not recursively expanded |

Hierarchy arrows run **parent → child**. References run **linking note → destination**. Preserve reciprocal connections and cycles. Never attach an orphan to `Logic & Set Theory` or `LOGIC` simply to tidy the drawing. Disconnected notes remain disconnected until source evidence supports a link.

The notes govern content and relationships. yEd governs the saved arrangement, optional presentation groups, and personal annotations. Moving or linking nodes in yEd does not update Obsidian. Source relationship changes belong in the notes unless the user expressly intends a graph-only annotation. Source-note properties and contents are not rewritten during map upkeep.

Only a few graph properties are added: stable identity, note path, source/external/warning status, relation kind, and origin of evidence. The full audit stays in the manifest, not on the visible labels. Do not delete or edit properties beginning with `sb_`.

## Instructions for the AI assistant

### 1. Establish scope and scan every source

Read this manual, the saved GraphML, and its matching manifest. Inventory all Markdown notes recursively in the agreed source folder and hash their bytes. Use current notes as the source; the earlier outline, mind map, and Canvas are historical references.

Read each note's **YAML properties and entire body**. `down` means current note → child; `up` means parent → current note. Empty values add no connection. Inspect other properties for note links and retain them as references unless their hierarchy meaning is established.

Scan wikilinks, display aliases, heading/block links, note embeds, ordinary Markdown note links, and reference-style links. Include headings, paragraphs, lists, tables, callouts, quotations, footnotes, and inline fields. Literal code and comments are not relationships. Non-note media and internet URLs are excluded from the note graph. Same-note heading navigation is audited without redundant self-loops. The helper handles the vault's present scalar/list YAML syntax; stop and extend it carefully if new relationship syntax cannot be parsed. Do not silently skip unsupported YAML.

### 2. Resolve and classify evidence

Resolve paths relative to the vault or linking note, unique path suffixes, unique names, and declared aliases. Retain the original link, source line, context, and surrounding heading. Do not choose between ambiguous names or guess from approximate spelling. Show unresolved targets as warning nodes. External real notes appear once as boundary nodes.

Classify body links from context as **hierarchy**, **reference**, or **uncertain**. A mention alone does not make a child. Merge repeated evidence supporting the same directed connection into one edge. YAML hierarchy remains explicit; conflicting body evidence must be reported rather than silently reversed.

The initial build reused prior reviewed body decisions only when the exact owner/link/context/heading signature still matched a fresh scan. Every future assistant must review new or changed body evidence. An old signature cannot authorize a new context. The single known corrupted XOR destination has an explicit reviewed correction in the helper; other encoding or path changes require an evidence-backed decision.

Run the helper with `--inspect` to see unresolved destinations and new body evidence. Review the actual surrounding notes. Add reviewed body decisions to the accepted manifest, with a reason, before generating the candidate. For a hierarchy stated in the opposite direction, such as “parent: [[X]]”, set `direction` to `target_to_owner`; otherwise it is `owner_to_target`. References always keep the linking-note direction. If classification remains uncertain, retain that visible status and explain it. Do not edit the source notes merely to eliminate warnings.

### 3. Build and preserve the graph

Use one node per source note, direct edges, meaningful Unicode labels, and encoded Obsidian URLs. Preserve all parents of shared children, cycles, and isolates. No artificial root edges or duplicated branch projections.

The helper preserves existing node positions, sizes, styles, containment groups, user-created nodes, and user-created edges. Managed labels and source metadata are refreshed. Existing managed edge presentation is retained when its classification is unchanged. New nodes begin to the right of the existing drawing for selection and incremental placement. A uniquely matched unchanged-content rename retains its stable identity; a rename combined with editing needs explicit review rather than a guessed identity match.

yEd may change its XML node numbers on save. Match the stable `sb_id` property, not XML numbers. If identities are missing, duplicate, or incompatible with the manifest, stop and repair the pair. If a removed source note has a user-created connection, the helper stops so that annotation can be resolved explicitly.

The helper generates a **Candidate** graph and manifest whenever an accepted graph already exists. It does not overwrite the accepted graph and will not overwrite an existing unreviewed candidate. Running the helper does not invoke yEd's layout engine or change its application preferences.

From the vault root, the assistant can run:

```powershell
python 'Systems and Resources\Resources\Projects\Mathematics Project\Node visualization\yEd\_tools\build_yed_graph.py' --inspect
python 'Systems and Resources\Resources\Projects\Mathematics Project\Node visualization\yEd\_tools\build_yed_graph.py'
```

The first command only reads; the second writes to the chosen Desktop folder. Obtain filesystem permission if that folder is outside the assistant's writable roots. For a different explicitly requested source, use `--source` with its vault-relative folder, `--name` for the graph filename, and `--output-dir` for the working destination. Do not alter the established Logic map's source when building another project.

### 4. Verify before replacing the working pair

Check all of the following:

- Source files have identical hashes before and after work.
- Every source note appears exactly once, including isolates.
- Node identities are unique and every edge endpoint exists.
- Every connection has source evidence and the correct direction and classification.
- Added, removed, changed, and renamed notes and connections are reported.
- `Constituent parts (material implication)` points to both `Antecedent` and `Consequent` from its body evidence.
- Both PL and FOL point to the same `Types of validity` node.
- Reciprocal relationships such as `Atoms` and `Compound propositions` remain reciprocal.
- Existing arrangement, groups, and personal annotations survive updates.

Open the candidate in desktop yEd when available. Inspect Unicode labels, arrow direction, the two local acceptance examples above, warning nodes, and one **Go to URL** action. Selection-driven Neighborhood behavior must be tested in the user's desktop application; a successful browser rendering check is not equivalent.

For changed/new nodes, select them and use Hierarchical's **Selected Elements Incrementally** and, where useful, **Use Drawing As Sketch**. For a strictly fixed surrounding layout, try **Layout → Selection**. Save as GraphML after arranging. Major rearrangement of the whole graph is a user preference, not the default upkeep action.

After verification, preserve one dated backup of the previous graph/manifest pair under `_backups`, then promote the candidate pair to the working filenames and correct its manifest's `graph_file` field. If application checks remain unavailable, say so and leave the candidate for review. Never describe an untested import or navigation behavior as verified.

## Regular upkeep for the user

1. Edit and link your notes normally in Obsidian.
2. Save your current yEd arrangement and close it before an update.
3. Ask the assistant to update the graph using the prompt below.
4. Review the reported changes and unresolved links, then test the candidate's Neighborhood panel.
5. Accept the candidate when the graph is accurate and readable. Continue saving arrangement changes to that same working GraphML.

The graph is a snapshot: titles and edges are refreshed by an update run. Opening a note through its URL shows the live Obsidian note. A freshly opened graph does not automatically detect new notes.

Before the next upkeep run, check warnings and decide whether to correct the notes, supply a missing note, or leave the issue open. Do not invent parents for isolates. Review cycles as recorded relationships rather than assuming all cycles are mistakes. App preferences, layout settings, and panel placement may need restoration when moving to another computer; GraphML alone does not transport all of those settings.

To revert a graph update, restore its dated GraphML and manifest together. Source notes remain unaffected. Do not restore the graph from an old screenshot or the EdrawMind outline. Use the existing version-control workflow if the user requests a Git backup; do not commit or push automatically.

## Reusable update prompt

> Read `Systems and Resources/Resources/Projects/Mathematics Project/Node visualization/yEd/Obsidian to yEd - Graph Protocol.md` in my `second_brain` vault. Update the desktop yEd graph of the complete `MatheMagics/Logic & Set Theory` folder. Scan every note's YAML properties and entire body, including all supported internal link forms. Review new or changed body-link context, preserve shared children and cycles, keep one node per note, and do not invent orphan-parent connections. Preserve my saved arrangement, groups, and annotations. Produce and verify a candidate GraphML and matching manifest, report additions/removals/renames, uncertainty and missing targets, and use incremental layout where possible. Preserve a rollback copy before promoting the verified pair. The Neighborhood panel should follow a clicked concept and show its immediate incoming and outgoing neighbors. Do not modify source notes during visualization upkeep. If you need me to operate yEd, guide me one step at a time.

## Handoff to a new chat or project

Start with this manual and the current graph/manifest pair. Confirm the source and working destinations from the files rather than relying on old conversation paths. The helper is self-contained and uses Python's standard library; no archived file, cloud account, Obsidian community plugin, or yFiles SDK is required for regeneration.

Earlier EdrawMind exports duplicated shared branches; Canvas was also tried and rejected. The current choice is desktop yEd, automatic layout, one node per note, and the immediate-neighbor panel. The user prefers clear explanations and one operational step per chat turn, with all relevant settings in a tab grouped together. The user also wants the connecting lines highlighted in the main drawing; desktop yEd requires a separate selection command for this, as explained above. Preserve the established full-YAML/full-body scan and explicit evidence classification.

Initial source baseline, 2026-09-26: **285 source notes, 2 external nodes, 7 unresolved destinations, 385 directed connections, 76 shared children, 5 cyclic hierarchy components, and 5 isolates** on the resolved note graph. Body evidence supplies 29 internal hierarchy connections additional to YAML. The five isolates include `Logical and Mathematical symbols` (its outgoing destinations are missing) and four pending notes. The manifest is the detailed issue list. Counts are a baseline, not a future target; recalculate them after every change.

Structural checks and update-preservation checks passed, including shared children, body-only parents, cycles, a rename, application-style XML renumbering, retained groups/positions/styles/annotations, and protection of an unreviewed candidate. Source hashes remained unchanged. The attempted browser file-opening check did not load the graph.

The user subsequently downloaded and opened desktop yEd, opened the GraphML successfully, applied Hierarchical layout (Top to Bottom, separate components, Orthogonal routing, Backloop Routing, node labels considered, Hierarchic edge labeling), and configured selection-driven, hierarchy-aware context views. The user confirmed that selecting `Constituent parts (material implication)` displays both `Antecedent` and `Consequent` in Neighborhood. These are user-reported application checks.

Direct desktop inspection also verified the edge-selection command: with `Constituent parts (Logic)` selected, the configured selector produced gold/yellow highlighting and small selection handles on its incoming and outgoing lines. The underlying evidence color remained blue in Properties View. The selection settings were correct; applying the command again produced the visible result. The user subsequently confirmed seeing the highlighted lines after rerunning the command. Clicking another concept clears that edge selection, so rerun the selector for each concept. This is temporary selection emphasis, not a saved change to evidence colors.

### Session checkpoint — 2026-09-26

The user ended the session after confirming that manual edge highlighting works. Final direct desktop inspection showed an asterisk on the graph tab, and the working GraphML on disk retained its generated grid coordinates. The user then clarified that leaving the arrangement unsaved is intentional while they assess the workflow. Respect this choice. The new Hierarchical arrangement remains an unsaved trial; do not assume it has been adopted or stored. Do not regenerate or reopen another graph over that trial. If the user later chooses to retain it, save and verify it at the established Desktop working location.

The working file on disk remains structurally valid: 294 unique managed nodes, 385 unique managed edges, and valid endpoints, matching the manifest identities. A fresh comparison with the manifest found changed source hashes for `Existential generalization (EG).md`, `Existential instantiation (EI).md`, `Universal generalization (UG).md`, and `Universal instantiation (UI).md`. These changes were not incorporated into a new graph during wrap-up; review their current contents on the next requested update. No source notes were edited during this checkpoint.

Resume with the user's assessment of the workflow. If they choose to continue, remaining checks include the shared `Types of validity` node and an Obsidian **Go to URL** action. If they choose to retain the arrangement, save and confirm the working file and update the matching manifest's application-validation record, distinguishing user-reported results from direct file or desktop verification. Its initial flags still describe preparation; it was left unchanged during wrap-up. The user has requested no further setup steps today.
