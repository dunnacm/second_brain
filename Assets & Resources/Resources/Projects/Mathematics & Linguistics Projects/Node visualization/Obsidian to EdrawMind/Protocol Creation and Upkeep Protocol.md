---
type: protocol
project: MatheMagics
status: current
---

## Purpose

Produce an EdrawMind map of the complete **Logic & Set Theory** Obsidian project. Show shared concepts explicitly wherever they belong, use native **Relationship** arrows to close cycles, and integrate related supplementary concepts into their relevant branches under the provisional reciprocal-link rule below.

The notes govern conceptual content. This protocol governs its presentation, including the explicitly recorded provisional reciprocal-link assumption in rule 3. The map is a generated snapshot; changes in Obsidian require an update. Use no EdrawMind hyperlinks for navigation or as substitutes for visible topics.

## Project locations

**Obsidian source, including all subfolders:**

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\MatheMagics\Logic & Set Theory`

**Output folder for the protocol, completed maps, and their upkeep records:**

`C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic\Logic and Set Theory\Current`

**Visual reference:**

`C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic\Logic and Set Theory\logic.emmx`

Use the example to understand the desired presentation, not to infer missing source relationships. It contains more than one page; inspect relevant pages before choosing a layout. The explicit rules below govern where the example is incomplete or inconsistent with them. Preserve the example file.

## The three presentation rules

### 1. Show a shared concept in every applicable branch

If a concept belongs beneath several parents, display its real title beneath each of them. For example, **Conclusions** must be visible in every supported argument or validity branch where it occurs.

Repeat its supported descendant branch at each occurrence, applying the cycle rule independently within that branch. Do not replace an occurrence with “go to topic,” a hyperlink icon, a machine ID, or a reference-only label. Repetition across different branches is intentional, even when the titles and descendants are identical.

Every visible occurrence has its own internal topic ID, while the upkeep record identifies the one source note it represents. Deduplicate repeated evidence for a source relationship; do not globally deduplicate visible topics.

Example: for A → B, A → C, B → D, and C → D, show D under B and also under C. If D has children, show those children under both occurrences, stopping only when expansion would return to an ancestor in that particular branch.

### 2. Close a cycle with a Relationship arrow

If expansion would repeat a note already in the **current ancestor chain**, stop before creating that repeated ancestor. Add an actual EdrawMind Relationship from the current topic to the matching ancestor occurrence.

For A → B, A → C, and C → A:

- Show A with B and C as ordinary children.
- Draw a directed Relationship **C → A**.
- Do not create a second A beneath C and continue indefinitely.

A topic appearing elsewhere in the map is not, by itself, a cycle. Test source-note identities on the current branch, not titles alone and not a global “already displayed” list. When the same source concept has several visible copies, a cycle arrow targets the matching ancestor in its own branch.

Use a curved, dashed gray Relationship with its arrowhead at the destination, as in the supplied cycle illustration. Here, dashes distinguish a Relationship from an ordinary branch; they do not mean that the evidence is uncertain. Add a short label only when it clarifies the relationship's meaning. Preserve the source direction for evidenced arrows and distinguish any rule-3 assumed direction in the upkeep record.

### 3. Integrate supplementary notes through an assumed reciprocal link

**Provisional rule adopted 2026-09-29.** This replaces the previous default of showing a related supplementary note as a detached floating topic with a long Relationship to the main hierarchy. It applies to both mathematics and Linguistics maps using this protocol, until the user changes it.

When a supplementary note B would otherwise float, but its actual note links establish a clear connection to an already placed A, treat A and B as reciprocally linked for presentation. Prefer an established hierarchy placement first. Where the source has only B → A, add an assumed A → B to the mapping model and display B as a normal child of the relevant A occurrence. Retain B's supported descendants. This makes B accessible within the branch without giving it the visual prominence of the presentation center.

**Concrete example:** the source currently contains Grammar → Alphabet + Grammar. Assume Alphabet + Grammar → Grammar for presentation, place **Grammar beneath Alphabet + Grammar**, and render Grammar → Alphabet + Grammar as a native directed cycle-closing Relationship to that same ancestor occurrence. Do not create another Alphabet + Grammar beneath Grammar or leave Grammar in a detached box.

This is a user-authorized presentation assumption, not a claim that the reverse wikilink has been found in the vault or that the connection proves a semantic parent-child relation. Record the actual evidence and direction separately from the added reverse edge, with the rule date, source-note identities, chosen anchor, and affected occurrences. Do not edit the source notes to insert reciprocal wikilinks during visualization work.

Apply this exception only to otherwise floating supplementary notes with an identifiable linked anchor. Do not make every reference, source citation, synonym, external boundary link, or existing hierarchy edge reciprocal. If the anchor appears in several applicable branches, show B beneath each applicable occurrence and apply cycle detection independently within each ancestor chain. A local cycle arrow must target the matching local ancestor.

If several anchors are plausible and the evidence does not determine placement, ask about that specific choice while continuing other work. If no related anchor can be identified at all, retain the note provisionally as an unresolved floating topic and report it for placement. Never attach an unrelated note to the center merely to eliminate floating topics, and never omit an unresolved note. Floating placement is a fallback for genuinely unresolved cases, not the default for an identifiable related note.

**Logic and Set Theory scope approved 2026-09-29:** repeat eligible supplementary notes beneath every directly linked placed anchor, including the sources of the previously reviewed detached sub-branch connections. The user explicitly selected the broader, approximately 40,015-topic expansion after reviewing its size. Do not choose only one of the four inference-rule anchors for Examples (UI, UG, EI, EG).

For this update, eligible notes are the prior detached source roots and the supplementary source endpoints of the previously reviewed floating-to-main hierarchy connections. Reassess these roots as their directly linked anchors become placed. Keep internal descendant hierarchy directed; this authorization does not reverse every edge inside a detached component. Expand every selected branch completely, using local cycle closure. Record the exact eligible notes and assumed edges in the manifest so later runs can reproduce and reassess this scope. Components without a direct placed anchor remain reported fallbacks; a multi-step path alone does not authorize inventing an additional parent. Other projects still resolve their own anchor choices and expansion size before applying this project-specific scope.

## Main topic, placement, and relationship meaning

Use **Logic and Set Theory** as the presentation center. Distinguish this container from the source note **LOGIC**. A connection to a presentation container is not automatically a conceptual parent-child relationship.

Choose main branches from an explicit project index, supported source structure, or a user-approved presentation decision. Do not promote all roots or disconnected components into main branches automatically. Record the reason for each direct main-topic placement. Use rule 3 to integrate an otherwise floating related component under its identifiable anchor. Retain floating components only when placement remains unresolved.

Use ordinary branches for established parent-child expansion and the explicitly authorized supplementary placement in rule 3. Use Relationships for cycle closure and labelled lateral associations where useful. A hyperlink mention alone does not establish semantic parenthood; record a rule-3 placement as an assumption rather than reclassifying its source evidence.

If a Relationship target has several visible occurrences, prefer the occurrence in the relevant local branch. For a cycle, the ancestor rule determines the destination. For a floating or lateral connection with no clear local occurrence, record the proposed destination and ask about any material ambiguity; do not connect indiscriminately to every copy or select one solely because it has the same title.

Keep Relationship endpoints on the same page. If page splitting is necessary, agree on the partition with the user and repeat the necessary concepts so relationships remain visible locally. Do not conceal a required connection through a cross-page hyperlink.

## Parse every note's properties and body

Recursively inventory every Markdown note in the source folder and record its path and content hash. Read **both YAML and the entire note body** before deciding that a note has no relationships.

### YAML

- `down`: current note → listed child.
- `up`: listed parent → current note.
- Accept scalars and lists; ignore empty values.
- Preserve explicit `down` order where it does not conflict with a user-approved arrangement.
- Inspect other properties containing note links. Classify them by their established meaning; do not assume they are hierarchy.
- Merge duplicate support for the same directed relationship and retain the evidence from each source.

### Body

Scan wikilinks, aliased links, links with heading or block suffixes, embedded Markdown notes, ordinary Markdown note links, and reference-style links. Include paragraphs, lists, tables, callouts, quotations, footnotes, and inline fields.

Ignore literal code and comments as conceptual connections. Distinguish a syntax example from a real link. Exclude internet URLs and non-note attachments from the concept graph. Same-note heading navigation is not automatically a genuine conceptual self-loop.

For each extracted note-link occurrence, retain the source note, raw target, resolved destination or resolution failure, source order/line, heading, and surrounding context. Classify it as:

- **Hierarchy:** the context establishes a constituent, subtype, example, member, step, or another narrower concept.
- **Reference:** comparison, background, contrast, citation, further reading, or another lateral association.
- **Uncertain:** meaning or direction is not sufficiently established.

Body hierarchy can point in either direction. “Parent: [[A]]” inside B supports **A → B**, not B → A. Review the actual context instead of applying keyword rules blindly. Explicit YAML and contradictory body evidence must be reported together, not silently reconciled by changing the notes.

For example, constituent links in the body of **Constituent parts (material implication)** can establish **Antecedent** and **Consequent** as its children even if those children's properties are empty.

Never claim complete scanning if the parser skipped an unsupported relationship-bearing syntax. Repair the parser or identify the unparsed evidence before declaring the map complete.

## Resolve and audit links

Resolve exact vault-relative paths, exact paths relative to the linking note, unique path suffixes or filenames, and unique declared aliases. Strip display aliases and heading/block suffixes for note resolution while retaining the original link as evidence. Decode Markdown destinations as necessary.

Do not guess from similar names, damaged symbols, or ambiguous filenames. Distinguish a real note outside the selected project from a missing note. External notes remain boundary topics without recursively expanding another project. Missing or ambiguous destinations remain explicitly identified in the upkeep record and, where represented visibly, carry a qualified terminal label.

Before assigning a main-topic parent or declaring a note disconnected, audit incoming YAML and body hierarchy, its outgoing links, relevant backlinks, aliases, and path variants. A backlink is context to inspect; it is not automatic proof of parenthood. It may establish the real connection used by rule 3, whose added reverse edge must remain separately identified.

For disputed placements, present the note, proposed target, direction, and evidence to the user. Record the user's presentation decision separately from source relationships. Visualization upkeep does not authorize modifying the notes to enforce that decision.

## Instructions for constructing the map

1. Build and classify the complete source relationship network before rendering branches. Keep the observed network separate from the mapping model containing rule-3 assumed reverse edges.
2. Determine the supported main hierarchy, integrate eligible supplementary notes using rule 3, and record any unresolved floating components. Give the evidence and presentation rationale for each anchor choice; do not guess an unrelated parent.
3. Expand each hierarchy branch with a fresh ancestor chain. Shared notes outside that chain receive another visible occurrence and descendant expansion.
4. When an observed or rule-3 assumed edge returns to an ancestor, add a directed native Relationship to that ancestor occurrence and stop that recursive step. In the Grammar example, the ordinary branch is the assumed forward edge and the return Relationship preserves the actual source edge.
5. Connect lateral and remaining unresolved floating topics through evidenced Relationships where applicable, recording exact source and target occurrences. Do not substitute a distant floating box for an eligible rule-3 branch placement.
6. Retain all source notes, including disconnected ones. A separate coverage audit may track which source notes are represented; it must not suppress legitimate repeated occurrences.
7. Estimate topic and Relationship counts before building a very large map. Repetition can produce a large finite result even after cycles are stopped. If it becomes impractical, show the estimate and discuss layout, folding, or an explicit scope/page decision. Do not silently truncate branches, omit notes, or substitute hyperlinks.

Identify a source note independently of its title. Give each occurrence its own ID and identify it by source identity plus its branch context. Record Relationship endpoints by occurrence ID. A rename must not cause connections to land on a different note with a similar title.

The method must create actual native Relationships and, where unresolved fallback placement requires them, native floating topics in the saved EdrawMind document. A tree outline, an imported arrow that behaves differently, or a line baked into a picture does not satisfy these rules.

Before relying on any export/import method, verify that it retains repeated topics, directed Relationships, floating topics, and Unicode titles in EdrawMind after saving and reopening. Do not assume a `.mm` import carries every required feature. An intermediate import file is useful only if its conversion is demonstrated. Do not rename an XML file to `.emmx` or modify an unverified native binary payload and claim a functioning map.

If a method produces only the branching structure, finish the native Relationships and any required unresolved floating placements through a verified EdrawMind operation and report that step. A map with missing cycle arrows or flattened floating topics remains incomplete. Do not make large amounts of manual reconstruction the default without explaining the upkeep burden.

## Presentation

Use the supplied `logic.emmx` and diagrams as visual guidance. Prefer a clearly distinguished dark central topic, readable titles, and restrained purple/blue branches. Integrated supplementary concepts use ordinary branch-topic styling at their local depth. Reserve detached boxes for unresolved fallback topics and avoid styling them with the center's prominence. Preserve mathematical symbols, Unicode, and source title capitalization.

Keep repeated titles identical when they represent the same source note. Do not add visible IDs or repetitive “duplicate” labels. Use spacing and folding to keep repeated branches navigable. Place eligible supplementary topics beneath their relevant anchors as ordinary branch topics. Keep unresolved fallback topics near useful context without suggesting equality with the center.

Use curved gray dashed Relationships with unambiguous arrowheads. Route them around text and keep their endpoints attached to the intended occurrences. Their labels must describe supported meanings; use a distinct label for uncertainty instead of treating all dashed arrows as uncertain.

## User procedure

1. Edit and link the notes normally in Obsidian.
2. Before requesting an update, save any EdrawMind presentation changes you want retained and identify the working file.
3. Ask the assistant to follow the reusable prompt below.
4. Review the proposed changes, disputed placements, and completed map in EdrawMind.
5. Confirm that repeated concepts are visible, cycle arrows close locally, and related supplementary topics appear beneath their anchors under rule 3. Check that Grammar is beneath Alphabet + Grammar; unresolved fallback topics must be reported.

During interactive app guidance, give **one operational step at a time** and wait for the user's result. Group settings belonging to the same tab or dialog into one step.

## Upkeep for the AI assistant

Read this protocol, the current native map, its matching upkeep record, and the current source notes. Rescan every note's YAML and entire body on every update. Compare additions, removals, confirmed renames, changed ordering, hierarchy/reference changes, uncertain links, new cycles, and changed supplementary-anchor or unresolved floating placements. Reassess prior assumed edges: retain their provenance while the rule applies, replace them with actual evidence if the source now contains the reverse link, and flag assumptions whose real supporting connection has disappeared.

Retain the user's layout and formatting where a verified method permits. Reimporting a whole map may lose native-only presentation changes; stable source identities alone do not preserve the layout. Identify what can be retained before choosing an update method and explain any reconstruction that needs review.

Apply each source-note or relationship change to **all relevant occurrences**, not just the first matching title. Recalculate ancestor chains and cycle Relationships in each affected branch. Preserve unaffected occurrence identities where practical, and recalculate Relationship endpoints when branches move.

Reuse a reviewed body classification only while the source identity, raw link, heading, and context still match. Review new or changed context. Confirm rename identity through explicit evidence or a unique unchanged-content match; do not guess a rename combined with editing.

Keep user annotations distinct from generated concepts. Resolve the handling of annotations before removing their associated source occurrences. Never silently remove a floating concept simply because it is unreachable from the main topic.

Prepare a candidate under a clearly marked filename in `Current`, preserving the accepted map until checks pass. All new working deliverables go in `Current`. Before replacement, copy the accepted native map and its matching record together into one dated backup under `Archived` beside `Current`; this rollback storage is the only exception to the working output location. Do not delete existing files or create extra export formats without a request.

## Minimal working files

- `Obsidian to EdrawMind - Protocol.md`: these rules.
- `Logic and Set Theory.emmx`: the completed native map.
- `Logic and Set Theory Manifest.json`: a compact upkeep record.
- An import source only when the chosen, verified method requires it.

The upkeep record must include source paths/hashes and stable note identities; occurrence IDs and branch contexts; Relationship endpoints, kinds, and evidence; root/anchor/fallback-placement decisions; actual source edges separately from assumed reciprocal edges, including rule date and evidence; unresolved and uncertain links; material changes; native/import file hashes; and separate structural and application-check results. Record changes to the native file after a later save so validation remains tied to the actual file tested.

Source notes and `logic.emmx` are not overwritten during map generation. To roll back an accepted update, restore the matching native map and upkeep record together. Version-control work is a separate user request.

## Verification requirements

### Source and structure

- Every source note is represented, including floating and disconnected notes.
- Every note's YAML and complete body were scanned; extracted note links have a classification and resolution result.
- Every supported hierarchy edge and approved rule-3 placement is visible through branching or a cycle-closing Relationship; any unresolved fallback remains explicitly recorded.
- Shared concepts appear explicitly in every required branch, with their supported descendants and local cycle closures.
- No global uniqueness rule suppresses shared topic occurrences; occurrence IDs themselves are unique.
- Cycle Relationships point to the correct ancestor occurrence. Source directions remain intact, and assumed directions are identified separately in the upkeep record.
- Direct main-topic placements, supplementary anchors, and unresolved fallback targets are justified. The only added reciprocal edges are those authorized by rule 3; they are never represented as observed source links.
- Source files remain unchanged by visualization work.

### Inside EdrawMind, after saving and reopening

- **Conclusions** appears explicitly in all applicable argument and validity branches.
- Shared **Types of validity** branches are visible under both PL and FOL when the current source supports them.
- A cycle such as **Atoms** / **Compound propositions**, when supported, closes with a native Relationship instead of repeated infinite expansion.
- **Antecedent** and **Consequent** appear under **Constituent parts (material implication)** when supported by the current notes.
- **Grammar** appears as an ordinary child of **Alphabet + Grammar**, with a local directed return Relationship to that ancestor. Other supplementary concepts, including **Arbitrary constant** and **Closed formula**, use rule 3 only when an identifiable related anchor exists; unresolved cases remain reported.
- Integrated supplementary topics remain attached to their intended anchors after saving and reopening. Any unresolved fallback topics remain represented; local cycle arrowheads and endpoints survive.
- No navigation hyperlinks were generated; native Relationships are not hyperlink substitutes.
- Topic/Relationship counts, Unicode titles, readability, and retained personal presentation agree with the upkeep record.

Distinguish structural checks from direct or user-reported application checks. An intact file package or syntactically valid import source is not proof that its Relationships and floating topics behave correctly in EdrawMind. If a check cannot be performed, mark it untested rather than reporting completion.

## Reusable request and handoff

> Create or update my EdrawMind map of the complete `MatheMagics/Logic & Set Theory` folder in the `second_brain` vault. Follow **Obsidian to EdrawMind - Protocol.md**. Read every note's YAML and entire body, resolve internal links, and classify hierarchy, references, and uncertainty with the correct direction. Show shared topics explicitly in every applicable branch, including their supported descendants. When a branch returns to one of its own ancestors, stop the expansion and draw a native directed Relationship to that ancestor occurrence. Do not use EdrawMind hyperlinks. Apply provisional rule 3 to otherwise floating related notes: assume the missing reciprocal link for presentation, place the supplementary note beneath its identifiable anchor, and close the return edge locally. In particular, place Grammar beneath Alphabet + Grammar. Record observed and assumed edges separately and leave source notes unchanged. Ask about ambiguous anchors; retain genuinely unplaced notes as reported fallback topics rather than attaching them arbitrarily to the center. Use `C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic\Logic and Set Theory\logic.emmx` for visual guidance while following these rules and the current source notes. Save outputs in `C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic\Logic and Set Theory\Current`. Preserve my presentation where possible, update all occurrences consistently, retain a rollback copy before replacement, and leave source notes unchanged. Verify the saved native Relationships, integrated supplementary branches, unresolved fallback topics, repeated branches, and readability in EdrawMind. Report material changes, counts, uncertain or missing evidence, exact files, and which checks actually passed. Guide any app steps one at a time, grouping settings within the same dialog or tab.

A new assistant should begin with this protocol, the current working map and upkeep record, and a fresh source inventory. Confirm the source and destination paths from current files. Resolve concrete placement uncertainties with the user while continuing independent work. Keep the final report concise and avoid generating extra audit documents.

## Application references

### Application record: 2026-09-29

The approved broader reciprocal-placement model contains 280 source notes, 40 assumed reverse edges, 40,015 visible topics, and 18,129 generated Relationships. The two remaining source-root fallbacks are **Logical and Mathematical symbols** (missing linked destinations) and **Occurrences** (only an indirect path to a placed sub-branch within this scope). Eight unresolved source-link occurrences remain recorded. The source notes were preserved.

Use **File → Import** for the XMind source, then save as native EMMX. Ordinary Open is for the native working file. This full import took roughly twelve minutes; native reopening was much quicker. The large navigation/search panel caused delays, while canvas controls were more responsive with it closed. Keep deep branches folded; the primary Alphabet + Grammar / Grammar branch may remain open for review.

The primary Grammar return curve was adjusted in the native map to avoid crossing its parent's label. Its manifest entry identifies the affected occurrence and records this native presentation change, which a future full reimport must preserve or reapply. Consult the matching manifest for the actual verified native hash, save/reopen results, rollback location, and unperformed checks. Complete structural coverage does not mean every native arrow route was individually inspected.

### Feature documentation

EdrawMind provides native Relationship lines with configurable curvature, dashes, labels, and arrowheads, and supports floating topics. These features must be verified in the chosen generation/import workflow.

- [Relationship lines and their formatting](https://edrawmind.wondershare.com/guide/add-relationship-lines.html)
- [Topics, including floating topics](https://edrawmind.wondershare.com/guide/add-topics.html)
- [Copying a branch as a floating topic](https://edrawmind.wondershare.com/guide/cut-copy-paste-topics.html)
