# second_brain

An Obsidian-based knowledge vault for building, organizing, and refining a long-form personal knowledge system.

This repository is not a generic notes dump. It is a structured vault with a strong emphasis on mathematical note-making, formal definitions, theorem-style writeups, symbolic glossaries, workflow protocols, and durable cross-linking.

The center of gravity of the vault is **MatheMagics**: a growing body of notes in logic, set theory, real analysis, geometry, computation, and operations research. Around that core are supporting resources, idea capture, notation references, and project protocols.

## What this vault is for

This repository serves several purposes at once:

- a **second brain** for durable knowledge capture
- an **Obsidian vault** with tracked settings, theme choices, and plugins
- a **mathematics notebook system** for definitions, examples, proofs, and symbol references
- a **protocol repository** for writing, formatting, and refining notes over time
- a **linked knowledge graph** built through `[[wikilinks]]`, frontmatter metadata, and topic hierarchies

## Repository character

A few traits define the vault:

- **Obsidian-native**: the repo includes `.obsidian` configuration, appearance settings, theme selection, CSS snippets, and community plugin configuration
- **Frontmatter-driven structure**: many notes begin with YAML frontmatter using fields such as `down:` and `tags:`
- **Cross-link first**: notes are designed to point to parent, child, and sibling notes through wikilinks rather than relying only on folders
- **Math-heavy formatting**: many notes combine Markdown with LaTeX, structured callouts, and tightly controlled proof formatting
- **Protocol-aware**: the vault contains explicit style and workflow notes that govern how content should be written and maintained

## High-level structure

The exact contents will evolve, but the current repository visibly organizes around patterns like these:

### `MatheMagics/`
The main subject-matter corpus. This is the most developed area of the vault.

Representative subareas include:

- `Geometry/`
- `Logic & Set Theory/`
- `Real Analysis/`
- `Operations research/`
- `Computation/Software/`

Within these folders, notes are often granular and atomic. A single concept, theorem, symbol family, example, or proof pattern may live in its own file.

### `Miscellanea/`
Supporting resources, reference materials, and process documents. This includes project protocols and notes about writing systems, formatting rules, and workflow conventions.

### `Ideas/`
A lighter capture area for open-ended ideas and future development.

### Root-level notes
The vault also contains standalone notes at the root, including glossary-like or reference-style notes such as `Notation.md` and concept notes such as `Assignment operator.md`.

## Note conventions

A typical note in this vault often uses YAML frontmatter like this:

```yaml
---
down:
tags:
  - some/topic
---
```

Common conventions include:

- `down:` to indicate downstream or child links in the note graph
- `tags:` for topical classification
- descriptive file names, often close to the mathematical concept itself
- direct topic pages alongside umbrella pages such as `GEOMETRY.md` or `CALCULUS.md`

## Writing style inside the vault

The vault mixes several note styles depending on purpose.

### 1. Minimal structural notes
Some notes are intentionally light and serve mostly as graph nodes, indices, or category anchors.

### 2. Expository concept notes
Other notes define and explain a concept in clear prose, often with lists and staged explanations.

### 3. Formal theorem-definition notes
Many mathematics notes use nested Obsidian callouts with a stable pattern such as:

- theorem/definition title
- an `IFF` or hypothesis block
- a `THEN` block
- display math for the formal statement

### 4. Reference tables and glossaries
Some notes are built as structured tables for symbols, notation, and comparative definitions.

## Obsidian setup tracked in the repo

This vault tracks part of its Obsidian environment directly in version control.

Notable repository-level configuration currently includes:

- **Theme**: `Minimal`
- **CSS snippets**: several enabled snippets, including custom visual tweaks
- **Community plugins** such as Dataview, Omnisearch, Excalidraw, Excalibrain, TikZJax, Desmos, and others
- **Link-updating enabled** in Obsidian settings

Because `.obsidian` is versioned, this repository preserves not only note content but also part of the reading and authoring environment.

## What makes this vault distinctive

This is not only a storage repository. It is a repository of **method**.

The vault contains explicit protocols for:

- how mathematical notes should be formatted
- how proofs should be transcribed
- how Obsidian-ready Markdown + LaTeX should be structured
- how topic hierarchies and MOCs should be maintained
- how writing conventions are refined over time

That makes the repo both a knowledge base and a meta-knowledge base about how that knowledge should be represented.

## Recommended way to use this repository

### In Obsidian
1. Clone the repository locally.
2. Open the folder as an Obsidian vault.
3. Allow Obsidian to load the tracked configuration.
4. Install any missing community plugins if your local environment does not already have them.

### As a GitHub repository
Use GitHub primarily for:

- backup
- version history
- synchronization between machines
- safe experimentation through commits

## Suggested maintenance workflow

A stable workflow for this vault is:

1. Work locally in Obsidian.
2. Review changes before syncing.
3. Commit meaningful note batches.
4. Push local changes to GitHub.
5. Pull before starting work on a different machine.

For a vault like this, frequent small commits are usually better than infrequent large ones. They preserve the evolution of note structure, formatting standards, and content decisions.

## Audience

This repository is most useful to someone interested in one or more of the following:

- Obsidian-based knowledge management
- mathematical note systems
- formalized personal study workflows
- long-term knowledge graph building
- version-controlling a personal vault

## Status

This is an actively developing personal vault. Structure, conventions, and scope are expected to keep evolving as the system matures.
