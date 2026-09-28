---
type: protocol
project: MatheMagics
status: draft
---

# Obsidian to EdrawMind — Graph Export Protocol V.2

## Status and purpose

This is the drafting brief for an improved EdrawMind workflow. The user will supply the parameters, protocols, constraints, and proposed visualization method in the next session. Do not treat this draft as a completed export specification or begin generating a new map from it.

The user is returning to EdrawMind after evaluating Canvas and yEd. The yEd arrangement was intentionally left unsaved while the workflow was assessed. Continuing or saving that trial is not a prerequisite for the EdrawMind work.

The earlier protocol is now in this folder's `Archived` subfolder. It documents historical methods; its hyperlink strategy must not govern the new version.

## Decisions already established

1. **Do not use EdrawMind hyperlinks.** The user has a different idea for representing and navigating the notes and will explain it next session. Do not assume that additional parents or cycles will be represented by linked reference topics.
2. **Review the inappropriate connections to `LOGIC`.** Some ideas were connected to that topic when they should not have been. Ask the user how to handle these cases next session, before deciding their placement or generating a replacement map.
3. **Keep reading YAML and complete note bodies.** The prohibition on EdrawMind hyperlinks does not remove the requirement to scan Obsidian links as relationship evidence. A note's properties alone do not establish its full set of connections.
4. **Keep source notes authoritative.** Visualization work does not authorize rewriting the notes, inventing parents, or removing source relationships merely to obtain a convenient arrangement.
5. **Guide app operations one step at a time.** Group relevant settings within the same dialog or tab into one step.

## Source and locations

**Vault:**

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain`

**Source notes, including all subfolders:**

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\MatheMagics\Logic & Set Theory`

**Governing protocol folder:**

`C:\Users\dunnc\My Drive (cardonadunn@gmail.com)\PRESENT\Η βιβλιοθήκη\second_brain\Systems and Resources\Resources\Projects\Mathematics Project\Node visualization\Obsidian to EdrawMind`

**Map folder to inspect before future work:**

`C:\Users\dunnc\OneDrive\Desktop\mind_map\Academic\Logic and Set Theory`

### Structure inspected on 2026-09-26

The map folder contains:

```text
Logic and Set Theory/
├── Current/                         [empty at inspection]
└── Archived/
    ├── Logic - Linked Map - Candidate.emmx
    ├── Logic - Linked Map - Candidate.mm
    └── Logic - Linked Map - Candidate Manifest.json
```

Treat the archived set as historical reference, not an accepted current map. Confirm the responsibilities of `Current` and `Archived` when specifying the new workflow; do not move, replace, or delete these files now.

In the vault's `Node visualization` section, the old EdrawMind map, its `.mm` import source, and an outline remain in the parent folder. Canvas and yEd materials are archived. The user also moved `Graph Export Protocol V.1.md` into `Obsidian to EdrawMind/Archived` during this session.

## Findings useful for the next session

- The archived candidate `.mm` contains 406 topics, including 286 canonical note topics and 109 internal links. Its IDs are unique and the internal link targets exist. These are historical format checks, not an endorsement of its presentation or the method for V.2.
- That file places `Antecedent` and `Consequent` under `Constituent parts (material implication)`. This is a useful relationship example to retain when checking a new map against the current source.
- It represents shared `Types of validity` parentage and an `Atoms` / `Compound propositions` cycle through hyperlinks. The new representation of these cases remains undecided because the user has ruled out EdrawMind hyperlinks.
- The archived manifest records an earlier successful EdrawMind import and representative hyperlink test. The native `.emmx` has since been saved and its current hash differs from the recorded hash. Do not claim that those historical tests verify the present native file or a future export.
- The current source inventory contained 280 Markdown notes. It differs from the older map's inventory, including older accompanying-note labels versus the current `Assignment (FOL), note 1` and `Assignment (FOL), note 2` filenames. Rescan before building and verify identity before declaring renames.
- No new map was created, no Desktop map files were changed, and no source notes were edited during this protocol preparation.

## Start the next session here

Invite the user to explain the proposed EdrawMind method and supply the promised parameters and constraints. Then ask:

> Which ideas were incorrectly connected to `LOGIC`, and how would you like those cases represented in the new map?

For each disputed connection, inspect and show the relevant evidence before applying the user's decision. Distinguish an actual YAML/body relationship from a placement introduced only by the export. Also distinguish the real `LOGIC` note from a synthetic central topic used as a presentation container. Do not automatically put unplaced concepts under either one and describe that as conceptual parenthood.

Questions about layout preservation, shared concepts, cycles, disconnected notes, import format, and upkeep remain open. Resolve them in the context of the user's proposed method rather than carrying over the old hyperlink-based answers. Do not ask these questions today; the user has deferred the specification to the next session.

Once the method is established, complete this same document with:

- The agreed visual representation and scope.
- YAML/body parsing, resolution, relationship classification, and direction rules.
- Explicit treatment of the disputed `LOGIC` placements and other unplaced notes.
- Generation/import steps and the chosen file format, verified in EdrawMind.
- Creation, update, preservation of user presentation, review, acceptance, and rollback procedures.
- Minimal deliverables and the final `Current` / `Archived` conventions.
- Structural and application checks appropriate to the new representation.
- A reusable user prompt and AI handoff instructions.

Change `status` to `current` only after the governing decisions are specified. This draft records the next-session starting point and does not substitute for those decisions.
