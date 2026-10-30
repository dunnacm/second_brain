# Archived project resources

Historical visualization workflows for **Logic & Set Theory**, grouped by application. These records are retained for reference; use the [current EdrawMind protocol](<../Mathematics & Linguistics Projects/Node visualization/Obsidian to EdrawMind/Protocol Creation and Upkeep Protocol.md>) for ongoing mapping work.

## Contents

| Folder | Preserved materials |
| --- | --- |
| `Canvas/` | [Canvas protocol](<Canvas/Obsidian Canvas - Graph Protocol.md>), [matching historical manifest](<Canvas/Logic & Set Theory.manifest.json>), and `_tools/build_canvas.py`. |
| `yEd/` | [yEd protocol](<yEd/Obsidian to yEd - Graph Protocol.md>) and `_tools/build_yed_graph.py`. |
| `EdrawMind/` | Earlier [Graph Export Protocol V.1](<EdrawMind/Graph Export Protocol V.1.md>) and [V.2 drafting brief](<EdrawMind/Graph Export Protocol V.2.md>). |

The archived documents retain their original wording and metadata, including historical `current` or `draft` labels, instructions, and paths. Those labels describe their former role. They do not make these workflows current. The helper scripts are preserved historical tools.

The Canvas manifest names `Logic & Set Theory.canvas`, but that Canvas file was absent from the materials consolidated here. No native Canvas or yEd graph was included in this move; the archive is a collection of protocols, tools, and the existing Canvas record.

## Consolidation record — 2026-10-10

Seven source files and one generated Python cache were consolidated from `Mathematics & Linguistics Projects/Node visualization/Obsidian to EdrawMind/Archived`, including its nested `Archived/Canvas` and `Archived/yEd` folders. The cache remains local and is excluded from Git by `.gitignore`. Empty nested folders, including the empty `Canvas & yEd/Lexicon` placeholder, were removed after verification.

[Archive moves - 2026-10-10.csv](<Archive moves - 2026-10-10.csv>) records each original vault-relative path, its new path, size, and SHA-256 hash. Every file was verified against its original contents before the old copy was removed.

To undo this consolidation, use the CSV's `OriginalPath` and `ArchivedPath` columns to restore each file to its former location. Verify its hash and check for existing files before moving it back.
