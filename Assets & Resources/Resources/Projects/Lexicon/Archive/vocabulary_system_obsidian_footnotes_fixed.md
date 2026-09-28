

## Requirements that drive the design

Your system has to do three things at once, and each one pulls the design in a different direction.

First, it must behave like a **lexicon**: consistent fields per entry, easy filtering, and a structure that remains usable when the collection gets large. In Obsidian, the natural place for that structured data is **Properties**, which are stored as YAML at the top of the note.[^properties]

Second, it must behave like a **knowledge graph**: you want relationships such as word ↔ family ↔ root ↔ concept category to be navigable and visually explorable. Obsidian supports this with **internal links**, **Graph view**, **local graph**, and **Canvas**.[^internal-links] [^graph] [^canvas]

Third, you want **automation**: a workflow where you can feed in today’s words and have the system propose structure, metadata, relationships, and draft notes. That means the schema must be easy for scripts to write, easy for you to review, and robust enough that errors do not silently spread.

A practical design is one where the **notes are durable and human-readable**, while most tables, indexes, and relationship views are generated from metadata rather than maintained by hand.

## Tool choice: Obsidian and database options

### What Obsidian is especially good at for this project

Obsidian stores notes as Markdown-formatted plain text files inside a local vault, and it automatically refreshes when files change externally.[^storage] That is a strong fit for a system you may want to automate later, because your notes remain ordinary files rather than being trapped inside a proprietary database.

Obsidian also has several native features that matter here:

- **Properties** for structured metadata.[^properties]
- **Bases** for database-like views over notes and their properties, while keeping the underlying data in Markdown files.[^bases]
- **Graph view** and **Canvas** for visual exploration.[^graph] [^canvas]

### What a database-first tool still does better

A database-first tool is better when your highest priority is **strict schema enforcement** and **relational integrity**. For example, if you want to guarantee that every word has exactly one primary concept, every root is chosen from a canonical list, and every synonym points to an existing entry, a database system is naturally better at enforcing those constraints.

That said, database-centric systems are often less comfortable for text-heavy knowledge work. Definitions, etymology notes, sense distinctions, usage examples, and conceptual commentary fit more naturally inside notes than inside rows.

### Recommendation

For your stated goals, Obsidian is a strong primary home **if you commit to a schema and a small set of note types**. Bases makes it much more practical to treat the vault like a lightweight database without giving up file durability.[^bases]

A database tool becomes the better primary home only if your top priority is strict relational control and table-driven work more than note-driven work.

A hybrid is also reasonable: ==Obsidian as the canonical store, with occasional export to a spreadsheet or database for analysis, spaced repetition, or reporting.==

## Scalable note architecture inside Obsidian

The main scaling mistake in a system like this is choosing a unit of organization that is either too large or too fragmented.

- If your notes are too large, you end up with giant root notes that are hard to maintain.
- If your notes are too fragmented, you drown in link maintenance.

A durable structure is a **three-note-type model**, with an optional fourth.

### Primary note types

**Word note**  
One note per lemma or headword form. This is the core unit you will search, revise, and revisit.

**Root note**  
One note per root or morpheme anchor. Each root note explains the root and links to the words that use it.

**Concept category note**  
One note per concept node in your taxonomy. These notes define the category and collect the words assigned to it.

### Optional note type

**Word-family note**  
Only add this if you want family-specific commentary, curated comparison, or a dedicated visual map. In many cases, a `family_key` property is enough to generate the family automatically.

### Folder structure that scales

A clean baseline:

- `Lexicon/Words/`
- `Lexicon/Roots/`
- `Lexicon/Concepts/`
- `Lexicon/Inbox/`
- `Lexicon/Templates/`
- `Lexicon/Canvases/`

This separates **note types** rather than pretending that your content fits a single hierarchy. It also stays friendly to external tooling because everything is still just files.[^storage]

## Linking model and metadata design

The linking model should answer one question:

**When I am on a word note, how do I reach everything I care about with minimal manual upkeep?**

### Use Properties as the canonical relations layer

Obsidian Properties can store text, lists, dates, tags, and internal links. Internal links inside text properties must be quoted.[^properties]

That leads to a strong working pattern:

- Put **relations** in Properties.
- Put **explanation, nuance, and commentary** in the note body.

### Recommended fields for a word note

Think in terms of identity, relations, and workflow state:

- `type`
- `lemma`
- `pos`
- `aliases`
- `roots`
- `morpheme_breakdown`
- `concepts`
- `synonyms`
- `antonyms`
- `near_synonyms`
- `contrast_words`
- `family_key`
- `family_head`
- `definition`
- `register`
- `added`
- `status`
- `sources`

### Example of outward links for a word such as “benevolent”

A word note should be able to point outward like this:

- `roots`: `["[[Lexicon/Roots/BENE]]"]`
- `concepts`: `["[[Lexicon/Concepts/Affect and values/Virtue]]"]`
- `synonyms`: links to other word notes if they exist
- `antonyms`: links to contrast notes if they exist
- `family_key`: something like `benevol`

This works well because Obsidian supports internal links directly, and it can automatically update internal links when you rename files.[^internal-links]

### How to reduce manual link upkeep

Two core tools matter here:

- **Backlinks**, which show linked mentions and unlinked mentions for the active note.[^backlinks]
- **Search**, which supports operators such as `path:` and `tag:`, as well as property queries like `[property]`, `[property:value]`, and `[property:null]`.[^search]

The more you move “lists of related things” into generated views, the less manual upkeep you have to do.

## Visual representations that stay useful past a few hundred words

### Graph view

Graph view is useful for understanding the relationship structure of your vault, and local graph is especially useful because it lets you inspect the neighborhood around the active note and adjust depth.[^graph]

Graph view is best for:

- seeing what connects directly to a word or root
- identifying hubs
- discovering unexpected clusters

It is weaker for:

- side-by-side comparison
- typed relationship analysis
- detailed editing

### Canvas

Canvas gives you an infinite visual workspace and stores its data as `.canvas` files in the JSON Canvas format.[^canvas]

Canvas is best when you want a deliberately designed visual representation, such as:

- a root map for `BENE`
- a concept map for a semantic field
- a comparison map such as benevolent vs beneficent vs kind vs altruistic

### Bases

Bases is the best native option for routine browsing, filtering, grouping, and editing of structured note metadata.[^bases]

In everyday use, Bases is likely to become your main “database view” of the lexicon.

### Dataview

Dataview remains useful when you want dynamic computed sections inside notes. Its own documentation describes it as a live index and query engine over your vault, and it is designed for large collections.[^dataview]

A practical combination is:

- **Bases** for interactive browsing and editing
- **Dataview** for generated sections and custom query views

### Typed relationships

If you eventually want different relation types—such as “is antonym of” versus “derived from root” versus “belongs to family”—you may want a typed-link layer. Breadcrumbs is a community plugin built for that purpose.[^breadcrumbs]

That is a reasonable phase-two enhancement, not something you need on day one.

## A practical template for new word notes

Obsidian’s Templates core plugin can insert predefined snippets into the active note, and it supports variables such as `{{title}}` and `{{date}}`.[^templates]

Below is a template that is both human-readable and automation-friendly:

```markdown
---
type: word
lemma: "{{title}}"
pos: []
roots: []
family_key: ""
concepts: []
synonyms: []
antonyms: []
definition: ""
register: ""
added: "{{date}}"
status: draft
sources: []
---

# {{title}}

## Definition
- {{definition}}

## Senses and nuance
### Sense 1
Concise description of the sense, constraints, and typical context.

**Synonyms (Sense 1):**  
**Antonyms (Sense 1):**

### Sense 2 (if needed)
...

## Word family
<!-- Prefer an auto-generated list driven by family_key; keep this section for commentary. -->

## Etymology and morphology
Morpheme breakdown, notes about Latin/Greek origins, any uncertainty, and what needs verification.

## Concept category
Primary concept + optional secondary concepts. Explain why it belongs there.

## Examples
One or two sentences you write yourself, or careful paraphrases, aiming for natural usage.

## Related links
- Compare/contrast: [[...]]
```

Two implementation details matter:

1. Internal links in text properties must be quoted.[^properties]
2. Keep `definition` short in Properties so it works well in Bases, and put richer nuance in the note body.[^bases]

## Concept categories that will not collapse under their own weight

A useful concept taxonomy should be:

- broad enough that every word fits somewhere
- specific enough to mean something
- stable enough that you do not keep renaming everything
- simple enough that automation can work with it

A good working rule is:

**Assign one primary concept, plus optional secondary concepts.**

If you let every word accumulate too many concept assignments, the system stops behaving like a taxonomy and starts behaving like a tag cloud.

### A proposed top-level taxonomy

This is a practical working taxonomy, not a claim that it is the only correct one:

- **Abstract relations**  
  existence, identity, similarity/difference, quantity, order, cause, possibility, necessity

- **Space and time**  
  location, direction, motion, boundaries, duration, chronology, cycles

- **Physical world**  
  matter, energy, weather, heat, light, sound, structure, tools

- **Life and body**  
  biology, anatomy, health, disease, growth, decay, nutrition

- **Mind and cognition**  
  perception, attention, memory, belief, reasoning, imagination, learning

- **Affect and values**  
  emotion, desire, virtues, vices, moral evaluation, aesthetics

- **Society and institutions**  
  relationships, hierarchy, politics, law, economics, religion, education

- **Language and communication**  
  speech, writing, rhetoric, symbols, information, media

### How to implement categories in Obsidian

Treat categories as **notes**, not just tags.

For example:

- concept note path: `Lexicon/Concepts/Society and institutions/Social hierarchy.md`
- word note property: `concepts: ["[[Lexicon/Concepts/Society and institutions/Social hierarchy]]"]`

This gives you concept pages, graph structure, and searchable structured metadata.[^properties] [^search]

## Tagging and indexing without tag bloat

Obsidian tags are useful, but they should not carry the whole classification system. Use Properties for most structured classification and tags mainly for workflow state.[^tags] [^properties]

### Recommended split

Use **Properties** for:

- `pos`
- `roots`
- `concepts`
- other structured lexical fields

Use **tags** for:

- `#vocab/inbox`
- `#vocab/to-verify`
- `#vocab/verified`
- `#vocab/needs-example`
- `#vocab/needs-root-review`

This keeps tags sparse and meaningful.

### Navigating POS and roots without tag overload

- Use a Base or Dataview view to group word notes by `pos`.[^bases] [^dataview]
- Let root notes collect their associated words through backlinks or generated queries.[^backlinks]

## Automation workflow using Codex and lexical resources

You want something close to this:

> Give the system today’s words, and have it create draft notes, suggest roots, suggest concept placement, and propose family and semantic relations.

There are really two automation problems here:

1. **Vault editing and organization**
2. **Lexical knowledge acquisition**

### How Codex can help with the vault side

OpenAI’s Codex CLI is a local coding agent that can read, modify, and run code in a selected directory.[^codex-cli]

Since an Obsidian vault is just a local folder of files, that makes the vault a good automation target.[^storage]

A robust pattern looks like this:

- **Input**: a daily list of new lemmas
- **Automation**:
  - create word notes from a template
  - populate draft properties
  - create or flag missing root notes
  - create or flag missing concept notes
  - move reviewed notes from `Inbox` to `Words`
- **Review loop**:
  - verify roots
  - verify concepts
  - verify family grouping
  - verify semantic relations
  - change `status` from `draft` to `verified`

### How to make the system consult your existing notes

If you want a model to classify new words partly by looking at your existing lexicon, OpenAI’s **file search** tool in the Responses API is relevant. It lets models search uploaded files or vector stores using semantic and keyword retrieval.[^file-search]

That is useful if you want a hosted retrieval layer over your vocabulary notes.

### Where synonyms, antonyms, and family candidates should come from

This is where hallucinations become a real risk.

Do **not** rely only on a model to invent synonyms, antonyms, or etymologies. Use lexical resources and let the model assist with integration and drafting.

Two useful resources are:

- **WordNet**, which organizes English words into synsets and explicitly represents lexical and semantic relations such as antonymy.[^wordnet]
- **Datamuse**, which is a word-finding API that supports constraints on meaning, spelling, sound, and related-word queries.[^datamuse]

A sound workflow is:

- generate candidates
- write them into draft notes
- keep the note marked as `draft`
- verify before promoting it to `verified`

That review step matters because semantic relations are often **sense-dependent**, and WordNet itself is structured around distinct senses rather than undifferentiated word lists.[^wordnet]

### Control properties that make automation easier

A small number of control properties will help a lot:

- `type: word | root | concept`
- `status: draft | verified`
- `family_key: ...`
- `roots: [...]`
- `concepts: [...]`

These make it easy to search for incomplete notes, group entries, and generate maintenance views.[^search] [^bases]

## Bottom line

The strongest version of this system is:

- **file-based**
- **schema-driven**
- **note-centered**
- **query-assisted**
- **reviewed by you before promotion from draft to verified**

That gives you the durability of plain-text notes, the structure of metadata, the navigability of links, and a realistic path to automation without letting automation silently degrade the quality of the lexicon.

## Footnotes

[^properties]: [Obsidian Help — Properties](https://help.obsidian.md/properties). Properties are stored in YAML at the top of the note; internal links in text properties must be quoted.
[^storage]: [Obsidian Help — How Obsidian stores data](https://help.obsidian.md/data-storage). Obsidian stores notes as Markdown-formatted plain text files in a vault and refreshes when files change externally.
[^bases]: [Obsidian Help — Introduction to Bases](https://help.obsidian.md/bases) and [Core plugins](https://help.obsidian.md/plugins). Bases is a core plugin for database-like views over notes and their properties.
[^internal-links]: [Obsidian Help — Internal links](https://help.obsidian.md/Linking%20notes%20and%20files/Internal%20links) and [Settings](https://help.obsidian.md/settings). Obsidian supports internal links and can automatically update them when files are renamed.
[^graph]: [Obsidian Help — Graph view](https://help.obsidian.md/plugins/graph). Graph view includes a local graph mode with adjustable depth.
[^canvas]: [Obsidian Help — Canvas](https://help.obsidian.md/plugins/canvas). Canvas is a core plugin with an infinite visual workspace and `.canvas` files stored in JSON Canvas format.
[^backlinks]: [Obsidian Help — Backlinks](https://help.obsidian.md/plugins/backlinks). The Backlinks plugin shows linked mentions and unlinked mentions.
[^search]: [Obsidian Help — Search](https://help.obsidian.md/plugins/search). Search supports operators such as `path:` and `tag:` and also supports property queries like `[property:value]` and `[property:null]`.
[^templates]: [Obsidian Help — Templates](https://help.obsidian.md/Plugins/Templates). The Templates core plugin supports variables such as `{{title}}` and `{{date}}`.
[^tags]: [Obsidian Help — Tags](https://help.obsidian.md/tags). Tags can be created inline or through the `tags` property.
[^dataview]: [Dataview documentation](https://blacksmithgu.github.io/obsidian-dataview/). Dataview describes itself as a live index and query engine over an Obsidian vault.
[^breadcrumbs]: [Breadcrumbs documentation](https://publish.obsidian.md/breadcrumbs-docs/) and [GitHub repository](https://github.com/SkepticMystic/breadcrumbs). Breadcrumbs adds typed links to Obsidian notes.
[^codex-cli]: [OpenAI Help Center — Codex CLI getting started](https://help.openai.com/en/articles/11096431). Codex CLI is a local command-line coding agent that can read, modify, and run code.
[^file-search]: [OpenAI API — File search guide](https://platform.openai.com/docs/guides/tools-file-search) and [Responses API reference](https://platform.openai.com/docs/api-reference/responses/create?api-mode=responses). File search is available as a tool in the Responses API.
[^wordnet]: [Princeton WordNet](https://wordnet.princeton.edu/) and [WordNet glossary / database organization](https://wordnet.princeton.edu/node/28). WordNet organizes words into synsets and encodes semantic and lexical relations including antonymy.
[^datamuse]: [Datamuse API](https://www.datamuse.com/api/). Datamuse supports constraints on meaning, spelling, sound, and related-word queries.
