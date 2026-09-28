---
down:
  - "[[POS (Part of Speech)|POS (Part of Speech)]]"
  - "[[WORDS]]"
  - "[[ROOTS]]"
  - "[[CONCEPTS]]"
tags:
  - lexicon
---
# Lexicon Study Project

## Purpose
Build a personal lexicon by mapping each target word or expression to:
- ROOTS
- word family
- parts of speech
- CONCEPTS

## Default source policy
- **Merriam-Webster** controls the core family inventory, POS labeling, and standard lemma handling.
- **Merriam-Webster browse pages** may be used to catch adjacent attested family members.
- **Etymonline** controls etymology and root caution.
- If Merriam-Webster alone is too narrow for the family inventory, the secondary source must be named explicitly.

## Meaning of "exhaustive"
- **Exhaustive** means exhaustive **within the declared source scope** for that entry.
- Include direct family members:
  - headwords
  - derivatives
  - inflections
  - spelling variants
  - attested historical / rare / technical forms
- Do **not** automatically include every open compound or phrase built from the word unless I specifically ask for compounds.

## Normalization rules
- Keep my original form visible.
- Normalize to the lemma when useful.
- Correct obvious spelling errors, but note the correction.
- Treat multiword expressions as **expressions first**, then analyze their lexical heads.
- Separate distinct senses when they change root analysis, family grouping, or concept placement.

## Root analysis
- Check whether the word matches any root in my ROOT inventory.
- Transcribe the matching root tag **exactly**.
- Separate:
  - **Secure** matches
  - **Possible** matches
- Do not assign a root from mere spelling resemblance.
- If no root securely fits, write:  
  **"no secure match from current ROOT inventory."**

## Word-family inventory
For each family member, record:
- form
- lemma
- POS
- status
- note when needed

### Status labels
- headword
- derivative
- inflection
- variant
- historical
- rare
- technical
- doubtful

## Concept placement
- Give **1 primary concept** and up to **2 secondary concepts**.
- Transcribe the **full concept code** and **full concept label** exactly.
- Do not force weak concept matches.

## Output format

### Target word
- Original form:
- Lemma:
- Source scope:

### Root match
- Secure:
- Possible:

### Word-family inventory
| Form | Lemma | POS | Status | Note |

### Concept placement
- Primary:
- Secondary:

### Uncertain / needs review

## Multiword batches
- If a daily list is long, process it in micro-batches so the family inventories stay readable.
- Single words and multiword expressions may be separated into different sections.

## Reusable instruction snippet
When I give you a word or expression, do the following:
1. Check for secure and possible ROOT matches from my ROOT inventory.
2. Build the exhaustive direct word family within the declared source scope.
3. Tag every family member for POS.
4. Suggest 1 primary concept and up to 2 secondary concepts from my CONCEPT inventory.
5. Separate senses when needed.
6. Mark uncertainty explicitly.
7. Keep my original form visible even when you normalize to a lemma.