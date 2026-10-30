"""Build or audit a native Obsidian Canvas. Python standard library only.

Read the governing manual before use. Unknown body links remain uncertain.
Source notes are never written. No execution of note content or plugins.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
from datetime import datetime, timezone
import hashlib
import json
import math
import posixpath
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote


HERE = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = "MatheMagics/Logic & Set Theory"
DEFAULT_NAME = "Logic & Set Theory"
WIKI = re.compile(r"!?\[\[([^\]\n]+)\]\]")
MEDIA = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".pdf", ".mp3", ".mp4", ".wav", ".canvas"}
# Reviewed encoding corruption from the earlier Logic mapping; exact target exists.
REVIEWED_TARGET_CORRECTIONS = {
    "Exclusive disjunction Ã¢â€¡â€ XOR": "Exclusive disjunction ⇔ XOR",
}


def ident(kind, value):
    return hashlib.sha256((kind + ":" + value).encode("utf-8")).hexdigest()[:16]


def scalar(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def frontmatter(text):
    """Accept the vault's scalar/list YAML subset; fail on unsupported relations."""
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match:
        return {}, text, 0
    result, key = {}, None
    for line in match[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        top = re.match(r"^([\w-]+):\s*(.*?)\s*$", line)
        if top:
            key, value = top.groups()
            if key in {"up", "down", "aliases"}:
                result[key] = []
                if value and value not in {"null", "~", "[]"}:
                    if value.startswith("[") and not value.startswith("[["):
                        try:
                            result[key] = json.loads(value)
                        except json.JSONDecodeError:
                            raise ValueError("Unsupported YAML flow list: " + line)
                    else:
                        result[key] = [scalar(value)]
            continue
        if key in {"up", "down", "aliases"}:
            item = re.match(r"^\s*-\s+(.+?)\s*$", line)
            if item:
                result[key].append(scalar(item[1]))
            else:
                raise ValueError("Unsupported YAML relationship syntax: " + line)
    return result, text[match.end():], text[:match.end()].count("\n")


def visible_body(body):
    """Mask literal regions without changing line numbering."""
    blank = lambda m: re.sub(r"[^\n]", " ", m[0])
    body = re.sub(r"<!--[\s\S]*?-->", blank, body)
    lines, fence = [], None
    for line in body.splitlines(keepends=True):
        m = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            lines.append(re.sub(r"[^\n]", " ", line))
            if m and m[1][0] == fence[0] and len(m[1]) >= len(fence):
                fence = None
        elif m:
            fence = m[1]
            lines.append(re.sub(r"[^\n]", " ", line))
        else:
            lines.append(line)
    return re.sub(r"(`+)([^\n]*?)\1", blank, "".join(lines))


def body_links(body, offset):
    body = visible_body(body)
    heading = ""
    reference_defs = {}
    for line in body.splitlines():
        definition = re.match(r"^\s{0,3}\[([^\]^]+)\]:\s*(<[^>]+>|\S+)", line)
        if definition:
            reference_defs[definition[1].strip().casefold()] = definition[2].strip("<>")
    for i, line in enumerate(body.splitlines(), offset + 1):
        if re.match(r"^\s{4}(?![-*>])", line):
            continue
        h = re.match(r"^\s{0,3}#{1,6}\s+(.+)", line)
        if h:
            heading = h[1]
        records = [(m.start(), m[0], m[1], "wikilink") for m in WIKI.finditer(line)]
        if not re.match(r"^\s{0,3}\[[^\]]+\]:", line):
            for m in re.finditer(r"(?<!!)\[([^\[\]^]+)\](?:\[([^\]\n]*)\])?(?!\(|\])", line):
                ref = (m[2] if m[2] else m[1]).strip().casefold()
                if ref in reference_defs:
                    records.append((m.start(), m[0], reference_defs[ref], "markdown"))
        # Balanced parentheses allow ordinary Markdown links to mathematical titles.
        for m in re.finditer(r"(?<!!)\[[^\[\]]*\]\(", line):
            start, end, depth, quote = m.end(), m.end(), 1, False
            while end < len(line) and depth:
                c = line[end]
                if c == "<":
                    quote = True
                elif c == ">":
                    quote = False
                elif not quote and c == "(":
                    depth += 1
                elif not quote and c == ")":
                    depth -= 1
                end += 1
            if depth == 0:
                dest = line[start:end - 1].strip()
                if dest.startswith("<"):
                    dest = dest[1:dest.find(">")]
                else:
                    dest = re.split(r'\s+[\"\']', dest, maxsplit=1)[0]
                records.append((m.start(), line[m.start():end], dest, "markdown"))
        for position, raw, target, syntax in sorted(records):
            yield {"raw": raw, "target": target, "syntax": syntax, "line": i,
                   "position": position, "heading": heading, "context": line.strip()}


def vault_root():
    for path in HERE.parents:
        if (path / ".obsidian").is_dir():
            return path
    raise RuntimeError("Cannot find the containing Obsidian vault")


def scan(vault, source):
    paths = sorted(source.rglob("*.md"), key=lambda p: p.as_posix().casefold())
    notes, contents = {}, {}
    for p in paths:
        key = p.relative_to(vault).as_posix()
        contents[key] = p.read_bytes()
        text = contents[key].decode("utf-8-sig")
        props, body, offset = frontmatter(text)
        notes[key] = {"title": p.stem, "properties": props, "body": body, "offset": offset,
                      "sha256": hashlib.sha256(contents[key]).hexdigest()}
    all_paths = [p.relative_to(vault).as_posix() for p in vault.rglob("*.md")
                 if not any(x.startswith(".") for x in p.relative_to(vault).parts)]
    exact = {unicodedata.normalize("NFC", k).casefold(): k for k in all_paths}
    names, aliases = defaultdict(list), defaultdict(list)
    for p in all_paths:
        names[unicodedata.normalize("NFC", Path(p).stem).casefold()].append(p)
    for key, data in notes.items():
        for alias in data["properties"].get("aliases", []):
            aliases[str(alias).casefold()].append(key)

    def resolve(raw, owner, syntax="wikilink"):
        raw = str(raw).strip()
        w = WIKI.fullmatch(raw)
        if w:
            raw = w[1]
        raw = unquote(raw.split("|", 1)[0]).replace("\\", "/")
        raw = re.split(r"[#^]", raw, maxsplit=1)[0].strip()
        if not raw:
            return owner, "internal", "same-note subpath"
        if re.match(r"^[\w+.-]+:", raw):
            return None, "url", "URL is not a note"
        suffix = Path(raw).suffix.casefold()
        if suffix in MEDIA:
            return None, "media", "non-note attachment"
        value = raw if raw.endswith(".md") else raw + ".md"
        direct = [value.lstrip("/"), posixpath.normpath(posixpath.join(posixpath.dirname(owner), value))]
        if syntax == "markdown":
            direct.reverse()
        for item in direct:
            k = exact.get(unicodedata.normalize("NFC", item).casefold())
            if k:
                return k, "internal" if k in notes else "external", "exact path"
        candidates = [p for p in all_paths if p.casefold().endswith("/" + value.casefold())]
        if not candidates:
            candidates = names.get(unicodedata.normalize("NFC", Path(raw).stem).casefold(), [])
        if not candidates:
            candidates = aliases.get(raw.casefold(), [])
        if len(candidates) == 1:
            k = candidates[0]
            return k, "internal" if k in notes else "external", "unique name/path/alias"
        if len(candidates) > 1:
            return None, "ambiguous", candidates
        if raw in REVIEWED_TARGET_CORRECTIONS:
            fixed = REVIEWED_TARGET_CORRECTIONS[raw]
            candidates = names.get(fixed.casefold(), [])
            if len(candidates) == 1:
                k = candidates[0]
                return k, "internal" if k in notes else "external", "reviewed encoding correction: " + fixed
        return None, "missing", "no exact unique match"

    evidence, ignored = [], []
    for owner, note in notes.items():
        for prop in ["down", "up"]:
            for order, raw in enumerate(note["properties"].get(prop, [])):
                target, status, method = resolve(raw, owner)
                evidence.append({"owner": owner, "target": target, "status": status, "resolution": method,
                                 "raw": raw, "origin": "yaml", "property": prop, "order": order})
        text = contents[owner].decode("utf-8-sig")
        fm = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
        if fm:
            prop = ""
            for line_no, line in enumerate(fm[1].splitlines(), 2):
                top = re.match(r"^([\w-]+):", line)
                if top:
                    prop = top[1]
                if prop not in {"up", "down", "aliases"}:
                    for item in WIKI.finditer(line):
                        target, status, method = resolve(item[0], owner)
                        evidence.append({"owner": owner, "target": target, "status": status, "resolution": method,
                                         "raw": item[0], "origin": "yaml_reference", "property": prop,
                                         "line": line_no, "context": line.strip()})
        for item in body_links(note["body"], note["offset"]):
            target, status, method = resolve(item["target"], owner, item["syntax"])
            record = dict(item, owner=owner, target=target, status=status, resolution=method, origin="body")
            if status in {"media", "url"}:
                ignored.append(record)
            else:
                evidence.append(record)
    return notes, evidence, ignored


def signature(record):
    return ident("body-evidence", "\n".join(str(record.get(k, "")) for k in
                                         ["owner", "raw", "context", "heading"]))


def graph(notes, evidence, previous):
    decisions = {e["signature"]: e for e in previous.get("body_decisions", [])}
    edges, problems, self_links = {}, [], []
    for record in evidence:
        owner, target = record["owner"], record["target"]
        if record["origin"] == "yaml_reference":
            record["classification"] = "reference"
            record["reason"] = "note link in a property without declared hierarchy semantics"
        elif record["origin"] == "yaml":
            record["classification"] = "hierarchy"
            record["reason"] = "explicit " + record["property"] + " property"
        else:
            record["signature"] = signature(record)
            decision = decisions.get(record["signature"], {})
            record["classification"] = decision.get("classification", "uncertain")
            record["reason"] = decision.get("reason", "new or changed body evidence needs contextual review")
        if record["status"] in {"media", "url"}:
            continue
        if record["status"] in {"missing", "ambiguous"}:
            label = str(record["raw"])
            wiki = WIKI.fullmatch(label)
            label = (wiki[1] if wiki else label).split("|", 1)[0]
            target = "warning:" + record["status"] + ":" + label
            record["warning_key"] = target
            problems.append(record)
        elif target == owner and record["origin"] != "yaml":
            self_links.append(record)
            continue
        a, b = (target, owner) if record.get("property") == "up" else (owner, target)
        pair = (a, b)
        if pair not in edges:
            edges[pair] = {"source": a, "target": b, "evidence": [], "classification": record["classification"]}
        edge = edges[pair]
        edge["evidence"].append(record)
        order = {"uncertain": 0, "reference": 1, "hierarchy": 2}
        if order[record["classification"]] > order[edge["classification"]]:
            edge["classification"] = record["classification"]
    return list(edges.values()), problems, self_links


def strongly_connected(keys, directed):
    adjacency = defaultdict(list)
    for a, b in directed:
        adjacency[a].append(b)
    index, low, stack, onstack, components = {}, {}, [], set(), []

    def visit(a):
        index[a] = low[a] = len(index)
        stack.append(a)
        onstack.add(a)
        for b in adjacency[a]:
            if b not in index:
                visit(b)
                low[a] = min(low[a], low[b])
            elif b in onstack:
                low[a] = min(low[a], index[b])
        if low[a] == index[a]:
            part = []
            while True:
                b = stack.pop()
                onstack.remove(b)
                part.append(b)
                if b == a:
                    break
            components.append(sorted(part, key=str.casefold))

    for a in sorted(keys, key=str.casefold):
        if a not in index:
            visit(a)
    return components


def positions(keys, edges):
    hierarchy = [(e["source"], e["target"]) for e in edges
                 if e["classification"] == "hierarchy" and e["source"] in keys and e["target"] in keys]
    scc = strongly_connected(keys, hierarchy)
    component_id = {a: i for i, part in enumerate(scc) for a in part}
    dag, incoming = defaultdict(set), defaultdict(set)
    for a, b in hierarchy:
        u, v = component_id[a], component_id[b]
        if u != v:
            dag[u].add(v)
            incoming[v].add(u)
    degree = {i: len(incoming[i]) for i in range(len(scc))}
    queue = deque(i for i in range(len(scc)) if not degree[i])
    rank = defaultdict(int)
    while queue:
        i = queue.popleft()
        for j in sorted(dag[i]):
            rank[j] = max(rank[j], rank[i] + 1)
            degree[j] -= 1
            if degree[j] == 0:
                queue.append(j)
    connected = defaultdict(set)
    parents, children = defaultdict(list), defaultdict(list)
    for e in edges:
        a, b = e["source"], e["target"]
        if a in keys and b in keys:
            connected[a].add(b)
            connected[b].add(a)
    for a, b in hierarchy:
        parents[b].append(a)
        children[a].append(b)
    remaining, weak = set(keys), []
    while remaining:
        start = min(remaining, key=str.casefold)
        queue, part = [start], set()
        while queue:
            a = queue.pop()
            if a in part:
                continue
            part.add(a)
            queue.extend(connected[a] - part)
        remaining -= part
        weak.append(part)
    weak.sort(key=lambda part: (-len(part), min(part).casefold()))
    result, sections, ybase, maxwidth, isolated = {}, [], 0, 0, []
    for part in weak:
        if len(part) == 1 and not connected[next(iter(part))]:
            isolated.extend(part)
            continue
        layers = defaultdict(list)
        minrank = min(rank[component_id[a]] for a in part)
        for a in sorted(part, key=lambda k: (Path(k).stem != "LOGIC", k.casefold())):
            layers[rank[component_id[a]] - minrank].append(a)
        # Barycentre ordering reduces edge crossings; explicit source order breaks ties.
        for _ in range(5):
            for reverse in [False, True]:
                slots = {a: i for layer in layers.values() for i, a in enumerate(layer)}
                neighbours = children if reverse else parents
                for r in sorted(layers, reverse=reverse):
                    original = {a: i for i, a in enumerate(layers[r])}
                    layers[r].sort(key=lambda a: (
                        sum(slots[b] for b in neighbours[a]) / len(neighbours[a])
                        if neighbours[a] else original[a], original[a]))
        columns = min(12, max(map(len, layers.values())))
        width = columns * 520 - 120
        rowbase = 0
        for r, layer in layers.items():
            for start in range(0, len(layer), columns):
                row = layer[start:start + columns]
                xstart = (width - (len(row) * 520 - 120)) // 2
                for i, a in enumerate(row):
                    result[a] = (xstart + i * 520, ybase + rowbase * 380)
                rowbase += 1
        height = (rowbase - 1) * 380 + 200
        roots = [a for a in part if not parents[a]]
        label = "Connected concepts" if not sections else "Component: " + Path(min(roots or part)).stem
        sections.append({"label": label, "x": -60, "y": ybase - 70, "width": width + 120,
                         "height": height + 130, "members": sorted(part)})
        ybase += height + 400
        maxwidth = max(maxwidth, width)
    if isolated:
        columns = min(8, len(isolated))
        for i, a in enumerate(sorted(isolated, key=str.casefold)):
            result[a] = ((i % columns) * 520, ybase + (i // columns) * 300)
        sections.append({"label": "No recorded connections — review placement", "x": -60, "y": ybase - 70,
                         "width": columns * 520, "height": math.ceil(len(isolated) / columns) * 300 + 70,
                         "members": sorted(isolated)})
        ybase += math.ceil(len(isolated) / columns) * 300 + 400
    return result, sections, scc, isolated, maxwidth, ybase


def overlaps(a, b):
    return (a["x"] < b["x"] + b["width"] and b["x"] < a["x"] + a["width"]
            and a["y"] < b["y"] + b["height"] and b["y"] < a["y"] + a["height"])


def generate(vault, source, name, notes, evidence, ignored, relayout):
    if any(c in name for c in '\\/:*?"<>|'):
        raise ValueError("Map name must be a filename without reserved characters")
    path = HERE / (name + ".canvas")
    manifest_path = HERE / (name + ".manifest.json")
    previous = json.loads(manifest_path.read_text(encoding="utf-8-sig")) if manifest_path.exists() else {}
    old = json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else {"nodes": [], "edges": []}
    old_nodes = {n.get("file"): n for n in old["nodes"] if n["type"] == "file"}
    previous_notes = set(previous.get("notes", {}))
    removed, added = previous_notes - set(notes), set(notes) - previous_notes
    renames = {}
    for new in added:
        candidates = [k for k in removed if previous["notes"][k]["sha256"] == notes[new]["sha256"]]
        if len(candidates) == 1 and sum(notes[k]["sha256"] == notes[new]["sha256"] for k in added) == 1:
            renames[new] = candidates[0]
    relationships, unresolved, self_links = graph(notes, evidence, previous)
    external = sorted({e["target"] for e in evidence if e["status"] == "external"})
    keys = set(notes) | set(external)
    xy, sections, scc, isolated, graphwidth, bottom = positions(keys, relationships)
    pilots = [p for p in HERE.glob("*Pilot.canvas") if p != path]
    pilot_ids = {}
    for p in pilots:
        pilot_ids.update({n["file"]: n["id"] for n in json.loads(p.read_text(encoding="utf-8-sig"))["nodes"]
                          if n["type"] == "file"})
    nodes, groups = [], []
    for i, section in enumerate(sections):
        group = {k: v for k, v in section.items() if k != "members"}
        group.update(id=ident("group", str(i)), type="group", color="5" if i == 0 else "6")
        groups.append(group)
    for key in sorted(keys, key=str.casefold):
        old_node = old_nodes.get(key, old_nodes.get(renames.get(key), {}))
        x, y = xy[key]
        node = dict(id=old_node.get("id", pilot_ids.get(key, ident("note", key))), type="file", file=key,
                    x=x, y=y, width=400, height=200)
        if key in external:
            node["color"] = "4"
        if old_node and not relayout:
            for attr in ["x", "y", "width", "height", "color"]:
                if attr in old_node:
                    node[attr] = old_node[attr]
        nodes.append(node)
    warning_keys = sorted({r["warning_key"] for r in unresolved})
    for i, key in enumerate(warning_keys):
        _, status, title = key.split(":", 2)
        nodes.append(dict(id=ident("warning", key), type="text", x=graphwidth + 600,
                          y=i * 320, width=500, height=220, color="1",
                          text="### " + status.capitalize() + " target\n\n" + title +
                          "\n\nThis destination could not be resolved. Its source link is recorded in the manifest."))
    if warning_keys:
        groups.append(dict(id=ident("group", "unresolved"), type="group", x=graphwidth + 540,
                           y=-70, width=620, height=len(warning_keys) * 320 + 70,
                           label="Unresolved destinations", color="1"))
    if not relayout:
        old_groups = {n["id"]: n for n in old["nodes"] if n["type"] == "group"}
        for group in groups:
            for attr in ["x", "y", "width", "height", "color", "label"]:
                if attr in old_groups.get(group["id"], {}):
                    group[attr] = old_groups[group["id"]][attr]
    no_parent = sorted(k for k in notes if not any(e["target"] == k and e["classification"] == "hierarchy"
                                                for e in relationships))
    manual = (HERE / "Obsidian Canvas - Graph Protocol.md").relative_to(vault).as_posix()
    legend_text = ("# " + name + "\n\n" + str(len(notes)) + " source notes · one card per note\n\n"
                   "**Cyan arrows:** YAML hierarchy. **Purple arrows:** body hierarchy. "
                   "**Green arrows:** references. **Orange arrows:** uncertain links.\n\n"
                   "Shared children receive several arrows. Cycles remain direct connections. "
                   "Groups are layout containers, not conceptual parents.\n\n"
                   "Green-bordered cards are outside the source folder. Red cards mark unresolved targets.\n\n"
                   "Zoom in to navigate the live cards. Note content is live; arrows update when the Canvas is rebuilt.\n\n"
                   "[[" + manual + "|Governing manual and upkeep prompt]]")
    nodes.append(dict(id=ident("legend", name), type="text", text=legend_text,
                      x=0, y=-620, width=1050, height=450))
    lookup = {n.get("file", ""): n for n in nodes if n["type"] == "file"}
    lookup.update({key: next(n for n in nodes if n["id"] == ident("warning", key)) for key in warning_keys})
    cyclic = {a: i for i, part in enumerate(scc) if len(part) > 1 for a in part}
    edges, edge_audit = [], []
    for relationship in relationships:
        a, b = lookup[relationship["source"]], lookup[relationship["target"]]
        ev, kind = relationship["evidence"], relationship["classification"]
        warning = relationship["source"].startswith("warning:") or relationship["target"].startswith("warning:")
        has_yaml = any(e["origin"] == "yaml" for e in ev)
        color = "1" if warning else ("5" if kind == "hierarchy" and has_yaml else
                                      "6" if kind == "hierarchy" else "4" if kind == "reference" else "2")
        if b["y"] >= a["y"] + a["height"]:
            fromside, toside = "bottom", "top"
        elif a["y"] >= b["y"] + b["height"]:
            fromside, toside = "top", "bottom"
        else:
            fromside, toside = ("right", "left") if b["x"] > a["x"] else ("left", "right")
        edge = dict(id=ident("edge", relationship["source"] + "\n" + relationship["target"]),
                    fromNode=a["id"], toNode=b["id"], fromSide=fromside, toSide=toside,
                    fromEnd="none", toEnd="arrow", color=color)
        if warning:
            edge["label"] = "unresolved"
        elif kind != "hierarchy":
            edge["label"] = kind
        elif relationship["source"] in cyclic and cyclic.get(relationship["source"]) == cyclic.get(relationship["target"]):
            edge["label"] = "cycle"
        edges.append(edge)
        edge_audit.append(dict(relationship, canvas_edge_id=edge["id"]))
    generated_ids = [n["id"] for n in groups + nodes]
    # Preserve user-created annotations not managed by the previous generation.
    old_managed = set(previous.get("generated_node_ids", []))
    extras = [n for n in old["nodes"] if n["id"] not in old_managed and n.get("file") not in old_nodes]
    if old and old_managed:
        extras = [n for n in old["nodes"] if n["id"] not in old_managed and n["id"] not in generated_ids]
    all_nodes = groups + nodes + extras
    ids = [n["id"] for n in all_nodes]
    assert len(set(ids)) == len(ids), "Duplicate node identifier"
    edge_ids = {e["id"] for e in edges}
    old_edge_ids = set(previous.get("generated_edge_ids", []))
    extras_edges = [e for e in old["edges"] if e["id"] not in old_edge_ids and e["id"] not in edge_ids
                    and e["fromNode"] in ids and e["toNode"] in ids]
    edges += extras_edges
    assert len({e["id"] for e in edges}) == len(edges), "Duplicate edge identifier"
    assert all(e["fromNode"] in ids and e["toNode"] in ids for e in edges)
    file_paths = [n["file"] for n in all_nodes if n["type"] == "file"]
    assert all(file_paths.count(k) == 1 for k in notes), "Each source note must have one file card"
    assert all((vault / k).is_file() for k in file_paths), "Broken file card"
    assert all(hashlib.sha256((vault / k).read_bytes()).hexdigest() == notes[k]["sha256"] for k in notes)
    cards = [n for n in all_nodes if n["type"] != "group"]
    collisions = [[a["id"], b["id"]] for i, a in enumerate(cards) for b in cards[i + 1:] if overlaps(a, b)]
    if not old and collisions:
        raise ValueError("Initial layout has overlapping cards")
    canvas = {"nodes": all_nodes, "edges": edges}
    old_relationships = {e["canvas_edge_id"]: e for e in previous.get("relationships", [])}
    changed_relationships = [dict(id=e["canvas_edge_id"], before=old_relationships[e["canvas_edge_id"]]["classification"],
                                  after=e["classification"])
                             for e in edge_audit if e["canvas_edge_id"] in old_relationships and
                             old_relationships[e["canvas_edge_id"]]["classification"] != e["classification"]]
    incoming = defaultdict(set)
    for e in relationships:
        if e["classification"] == "hierarchy" and e["source"] in notes and e["target"] in notes:
            incoming[e["target"]].add(e["source"])
    yaml_pairs = {(e["source"], e["target"]) for e in relationships if any(r["origin"] == "yaml" for r in e["evidence"])
                  and e["source"] in notes and e["target"] in notes}
    body_pairs = {(e["source"], e["target"]) for e in relationships if e["source"] in notes and e["target"] in notes
                  and any(r["origin"] == "body" and r["classification"] == "hierarchy" for r in e["evidence"])}
    totals = {"source_notes": len(notes), "external_note_cards": len(external), "unresolved_target_cards": len(warning_keys),
              "canvas_nodes_including_groups_and_legend": len(all_nodes), "canvas_edges": len(edges),
              "yaml_internal_hierarchy_edges": len(yaml_pairs), "body_hierarchy_edges": len(body_pairs),
              "body_hierarchy_edges_additional_to_yaml": len(body_pairs - yaml_pairs),
              "body_link_occurrences_scanned": sum(e["origin"] == "body" for e in evidence),
              "uncertain_body_link_occurrences": sum(e.get("origin") == "body" and e["classification"] == "uncertain" for e in evidence),
              "shared_child_notes": sum(len(v) > 1 for v in incoming.values()),
              "cyclic_hierarchy_components": sum(len(p) > 1 for p in scc), "isolated_source_notes": len(set(isolated) & set(notes))}
    manifest = {"generated_at": datetime.now(timezone.utc).isoformat(), "source": source.relative_to(vault).as_posix(),
                "canvas_file": path.name, "totals": totals,
                "notes": {k: {"node_id": lookup[k]["id"], "sha256": v["sha256"]} for k, v in notes.items()},
                "generated_node_ids": generated_ids, "generated_edge_ids": [e["canvas_edge_id"] for e in edge_audit],
                "relationships": edge_audit, "unresolved_links": unresolved,
                "body_decisions": [e for e in evidence if e["origin"] == "body"],
                "same_note_links_without_canvas_loops": self_links,
                "ignored_media_and_urls": len(ignored), "hierarchy_roots": no_parent,
                "isolated_notes": sorted(set(isolated) & set(notes)),
                "cyclic_components": [p for p in scc if len(p) > 1],
                "changes": {"added_notes": sorted(added - set(renames)),
                            "removed_notes": sorted(removed - set(renames.values())) if previous_notes else [],
                            "renamed_notes": [{"from": old, "to": new, "evidence": "unique unchanged content hash"}
                                              for new, old in sorted(renames.items())],
                            "changed_notes": sorted(k for k in set(notes) & previous_notes
                                                    if notes[k]["sha256"] != previous["notes"][k]["sha256"]),
                            "changed_relationship_classifications": changed_relationships,
                            "new_relationships": sorted([e["canvas_edge_id"] for e in edge_audit
                                                         if e["canvas_edge_id"] not in set(previous.get("generated_edge_ids", []))]),
                            "removed_relationships": sorted(set(previous.get("generated_edge_ids", [])) -
                                                            {e["canvas_edge_id"] for e in edge_audit})},
                "validation": {"valid_json_canvas": True, "source_unchanged": True,
                               "source_notes_represented_once": True, "broken_file_cards": 0, "broken_edge_endpoints": 0,
                               "overlapping_cards": collisions, "obsidian_open_tested": False,
                               "existing_positions_preserved": bool(old["nodes"]) and not relayout}}
    if old["nodes"]:
        path = HERE / (name + " - Candidate.canvas")
        manifest_path = HERE / (name + " - Candidate.manifest.json")
        manifest["canvas_file"] = path.name
    path.write_text(json.dumps(canvas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Verify serialization round trip, including mathematical symbols and evidence.
    assert json.loads(path.read_text(encoding="utf-8")) == canvas
    assert json.loads(manifest_path.read_text(encoding="utf-8")) == manifest
    print(json.dumps({"canvas": str(path), "manifest": str(manifest_path), "totals": totals}, ensure_ascii=False, indent=2))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--name", default=DEFAULT_NAME)
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--relayout", action="store_true")
    args = parser.parse_args()
    vault = vault_root()
    source = (vault / args.source).resolve()
    if not source.is_relative_to(vault) or not source.is_dir():
        raise ValueError("Source must be a folder inside the vault")
    notes, evidence, ignored = scan(vault, source)
    if args.inspect:
        print(json.dumps({"source_notes": len(notes), "body_links": [e for e in evidence if e["origin"] == "body"],
                          "unresolved_yaml": [e for e in evidence if e["origin"] == "yaml" and e["status"] != "internal"]},
                         ensure_ascii=False, indent=2))
        return
    generate(vault, source, args.name, notes, evidence, ignored, args.relayout)


if __name__ == "__main__":
    main()
