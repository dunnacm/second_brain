"""Build or audit a native yEd GraphML graph. Python standard library only.

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
from urllib.parse import urlencode, quote
import copy
import textwrap
import xml.etree.ElementTree as ET


HERE = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = "MatheMagics/Logic & Set Theory"
DEFAULT_NAME = "Logic & Set Theory"
DEFAULT_OUTPUT = Path(r'C:\Users\dunnc\OneDrive\Desktop\Obsidian to yEd')
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
        h = re.match(r"^\s{0,3}#{1,6}\s+(.+)", line)
        if h:
            heading = h[1]
        records = [(m.start(), m[0], m[1], "wikilink") for m in WIKI.finditer(line)]
        if not re.match(r"^\s{0,3}\[[^\]]+\]:", line):
            for m in re.finditer(r"\[([^\[\]^]+)\](?:\[([^\]\n]*)\])?(?!\(|\])", line):
                ref = (m[2] if m[2] else m[1]).strip().casefold()
                if ref in reference_defs:
                    records.append((m.start(), m[0], reference_defs[ref], "markdown"))
        # Balanced parentheses allow ordinary Markdown links to mathematical titles.
        for m in re.finditer(r"\[[^\[\]]*\]\(", line):
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
    for key in all_paths:
        props = notes[key]['properties'] if key in notes else frontmatter((vault / key).read_text(encoding='utf-8-sig'))[0]
        for alias in props.get("aliases", []):
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
                    for item in body_links(line, line_no - 1):
                        target, status, method = resolve(item['target'], owner, item['syntax'])
                        evidence.append({"owner": owner, "target": target, "status": status, "resolution": method,
                                         "raw": item['raw'], "origin": "yaml_reference", "property": prop,
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
            record['direction'] = decision.get('direction', 'owner_to_target')
            if record['direction'] not in {'owner_to_target', 'target_to_owner'}:
                raise ValueError('Unrecognized reviewed body direction')
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
        reverse = record.get('property') == 'up' or (record['origin'] == 'body' and
                   record['classification'] == 'hierarchy' and record.get('direction') == 'target_to_owner')
        a, b = (target, owner) if reverse else (owner, target)
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


G = 'http://graphml.graphdrawing.org/xmlns'
Y = 'http://www.yworks.com/xml/graphml'
ET.register_namespace('', G)
ET.register_namespace('y', Y)
NS = {'g': G, 'y': Y}


def el(parent, namespace, name, **attrs):
    return ET.SubElement(parent, '{' + namespace + '}' + name,
                         {k: str(v) for k, v in attrs.items()})


def keys(root):
    existing = list(root.findall('g:key', NS))
    ids = {k.get('id') for k in existing}
    result = {}
    for scope, names in [('node', ['sb_id', 'sb_path', 'sb_status', 'url', 'description']),
                         ('edge', ['sb_id', 'sb_kind', 'sb_evidence'])]:
        for name in names + ['graphics']:
            special = ('nodegraphics' if scope == 'node' else 'edgegraphics') if name == 'graphics' else None
            found = next((k for k in existing if k.get('for') == scope and
                          (k.get('yfiles.type') == special if special else k.get('attr.name') == name)), None)
            if found is None:
                candidate = 'sb_' + scope + '_' + name
                while candidate in ids:
                    candidate += '_'
                attrs = {'id': candidate, 'for': scope}
                if special:
                    attrs['yfiles.type'] = special
                else:
                    attrs.update({'attr.name': name, 'attr.type': 'string'})
                    if name in {'url', 'description'}:
                        attrs['yfiles.type'] = 'node' + name
                found = ET.Element('{' + G + '}key', attrs)
                root.insert(len(root.findall('g:key', NS)), found)
                ids.add(candidate)
                existing.append(found)
            result[(scope, name)] = found.get('id')
    return result


def value(element, key):
    data = element.find("g:data[@key='" + key + "']", NS)
    return data.text if data is not None else None


def set_value(element, key, text):
    data = element.find("g:data[@key='" + key + "']", NS)
    if data is None:
        data = el(element, G, 'data', key=key)
    data.text = str(text)


def label_for(title):
    return '\n'.join(textwrap.wrap(title, width=36, break_long_words=False, break_on_hyphens=False))


def make_node(graph_element, node_id, title, status, index, keymap, xbase=0):
    node = el(graph_element, G, 'node', id=node_id)
    graphic = el(node, G, 'data', key=keymap[('node', 'graphics')])
    shape = el(graphic, Y, 'ShapeNode')
    label = label_for(title)
    width = max(150, min(320, max(map(len, label.splitlines()), default=1) * 7.4 + 28))
    height = max(44, len(label.splitlines()) * 17 + 22)
    el(shape, Y, 'Geometry', x=xbase + (index % 12) * 360, y=(index // 12) * 120,
       width=width, height=height)
    colors = {'source': ('#F3F6FA', '#46566B'), 'external': ('#ECF9F0', '#388251'),
              'missing': ('#FFF0EE', '#B43D36'), 'ambiguous': ('#FFF5DF', '#B77421')}
    fill, border = colors[status]
    el(shape, Y, 'Fill', color=fill, transparent='false')
    el(shape, Y, 'BorderStyle', color=border, type='line', width='1.2')
    node_label = el(shape, Y, 'NodeLabel', alignment='center', autoSizePolicy='content',
                    fontFamily='Dialog', fontSize='13', fontStyle='plain', hasBackgroundColor='false',
                    hasLineColor='false', modelName='internal', modelPosition='c', textColor='#172334',
                    visible='true')
    node_label.text = label
    el(shape, Y, 'Shape', type='roundrectangle')
    return node


def style_edge(edge, relationship, keymap, fresh):
    records, kind = relationship['evidence'], relationship['classification']
    warning = any(relationship[x].startswith('warning:') for x in ['source', 'target'])
    color = '#B43D36' if warning else '#338DB5' if kind == 'hierarchy' and any(
        e['origin'] == 'yaml' for e in records) else '#8660B4' if kind == 'hierarchy' else (
        '#398553' if kind == 'reference' else '#C7841D')
    graphic = edge.find("g:data[@key='" + keymap[('edge', 'graphics')] + "']", NS)
    if graphic is None:
        graphic = el(edge, G, 'data', key=keymap[('edge', 'graphics')])
    poly = graphic.find('y:PolyLineEdge', NS)
    if poly is None:
        if len(graphic) and not fresh:
            # Preserve unsupported yEd routing styles, including curved edges.
            return
        graphic.clear()
        graphic.set('key', keymap[('edge', 'graphics')])
        poly = el(graphic, Y, 'PolyLineEdge')
        el(poly, Y, 'Path', sx=0, sy=0, tx=0, ty=0)
        el(poly, Y, 'BendStyle', smoothed='false')
    for name in ['LineStyle', 'Arrows', 'EdgeLabel']:
        for item in list(poly.findall('y:' + name, NS)):
            poly.remove(item)
    el(poly, Y, 'LineStyle', color=color, type='dashed' if kind == 'uncertain' or warning else 'line', width=1.3)
    el(poly, Y, 'Arrows', source='none', target='standard')
    text = 'unresolved' if warning else kind if kind != 'hierarchy' else ''
    if text:
        edge_label = el(poly, Y, 'EdgeLabel', alignment='center', fontFamily='Dialog', fontSize=10,
                        modelName='six_pos', modelPosition='tail', textColor=color, visible='true')
        edge_label.text = text


def build(vault, source, name, inspect=False, output_dir=None):
    if any(c in name for c in '\\/:*?"<>|'):
        raise ValueError('Name must be a filename without reserved characters')
    output_dir = Path(output_dir or DEFAULT_OUTPUT).resolve()
    accepted = output_dir / (name + '.graphml')
    audit_path = output_dir / (name + '.manifest.json')
    previous = json.loads(audit_path.read_text(encoding='utf-8-sig')) if audit_path.exists() else {}
    notes, evidence, ignored = scan(vault, source)
    relationships, unresolved, self_links = graph(notes, evidence, previous)
    if inspect:
        print(json.dumps({'notes': len(notes), 'new_body_evidence': [e for e in evidence if
                          e['origin'] == 'body' and e['classification'] == 'uncertain'],
                          'unresolved_links': unresolved}, ensure_ascii=False, indent=2))
        return
    old_root = ET.parse(accepted).getroot() if accepted.exists() else None
    root = copy.deepcopy(old_root) if old_root is not None else ET.Element('{' + G + '}graphml')
    if old_root is not None and not previous.get('notes'):
        raise ValueError('An existing graph requires its matching manifest before it can be updated')
    keymap = keys(root)
    graph_element = root.find('g:graph', NS)
    if graph_element is None:
        graph_element = el(root, G, 'graph', id='G', edgedefault='directed')
    all_old_nodes = list(root.findall('.//g:node', NS))
    all_old_edges = list(root.findall('.//g:edge', NS))
    managed_nodes = set(previous.get('generated_node_ids', []))
    managed_edges = set(previous.get('generated_edge_ids', []))
    old_nodes = {value(n, keymap[('node', 'sb_id')]): n for n in all_old_nodes
                 if value(n, keymap[('node', 'sb_id')]) in managed_nodes}
    old_edges = {value(e, keymap[('edge', 'sb_id')]): e for e in all_old_edges
                 if value(e, keymap[('edge', 'sb_id')]) in managed_edges}
    if old_root is not None and set(old_nodes) != managed_nodes:
        raise ValueError('Managed node identities are missing/duplicated. Restore the accepted graph and manifest pair.')
    if len(old_nodes) != sum(value(n, keymap[('node', 'sb_id')]) in managed_nodes for n in all_old_nodes):
        raise ValueError('Duplicate managed node identity')
    if old_root is not None and set(old_edges) != managed_edges:
        raise ValueError('Managed edge identities are missing. Do not delete source relationships in the graph.')
    if len(old_edges) != sum(value(e, keymap[('edge', 'sb_id')]) in managed_edges for e in all_old_edges):
        raise ValueError('Duplicate managed edge identity')
    old_paths = set(previous.get('notes', {}))
    added, removed = set(notes) - old_paths, old_paths - set(notes)
    renames = {}
    for new in added:
        matches = [old for old in removed if previous['notes'][old]['sha256'] == notes[new]['sha256']]
        if len(matches) == 1 and sum(notes[p]['sha256'] == notes[new]['sha256'] for p in added) == 1:
            renames[new] = matches[0]
    external = sorted({e['target'] for e in evidence if e['status'] == 'external'})
    warning_keys = sorted({r['warning_key'] for r in unresolved})
    logical = {}
    used_xml_ids = {e.get('id') for e in root.iter() if e.get('id')}
    xbase = max([float(g.get('x', 0)) + float(g.get('width', 0)) for n in all_old_nodes
                 for g in n.findall('.//y:Geometry', NS)] or [0]) + (120 if old_root is not None else 0)
    generated_nodes = []
    new_ids = []
    for i, path in enumerate(sorted(set(notes) | set(external) | set(warning_keys), key=str.casefold)):
        old_path = renames.get(path, path)
        stable = previous.get('notes', {}).get(old_path, {}).get('node_id', 'n_' + ident('note', old_path))
        status = 'source' if path in notes else 'external' if path in external else path.split(':', 2)[1]
        title = Path(path).stem if not path.startswith('warning:') else status.upper() + ': ' + path.split(':', 2)[2]
        node = old_nodes.get(stable)
        if node is None:
            xml_id = stable
            while xml_id in used_xml_ids:
                xml_id += '_'
            used_xml_ids.add(xml_id)
            node = make_node(graph_element, xml_id, title, status, len(new_ids), keymap, xbase)
            new_ids.append(stable)
        for field, text in [('sb_id', stable), ('sb_path', path), ('sb_status', status),
                            ('url', 'obsidian://open?' + urlencode({'vault': vault.name, 'file': path}, safe='', quote_via=quote)
                             if not path.startswith('warning:') else ''),
                            ('description', status + ' | ' + path)]:
            set_value(node, keymap[('node', field)], text)
        node_label = node.find('.//y:NodeLabel', NS)
        if node_label is not None:
            node_label.text = label_for(title)
        logical[path] = node
        generated_nodes.append(stable)
    parents = {child: parent for parent in root.iter() for child in parent}
    obsolete_xml = {n.get('id') for stable, n in old_nodes.items() if stable not in generated_nodes}
    manual_edges = [e for e in all_old_edges if value(e, keymap[('edge', 'sb_id')]) not in managed_edges]
    if any(e.get('source') in obsolete_xml or e.get('target') in obsolete_xml for e in manual_edges):
        raise ValueError('A removed source note has a user-created graph connection. Resolve that annotation before updating.')
    for stable, node in old_nodes.items():
        if stable not in generated_nodes:
            parents[node].remove(node)
    edge_audit, changed_styles = [], []
    old_relation = {e['graph_edge_id']: e for e in previous.get('relationships', [])}
    generated_edges = []
    for relationship in relationships:
        a, b = logical[relationship['source']], logical[relationship['target']]
        stable = 'e_' + ident('edge', value(a, keymap[('node', 'sb_id')]) + '\n' + value(b, keymap[('node', 'sb_id')]))
        edge = old_edges.get(stable)
        fresh = edge is None
        if fresh:
            xml_id = stable
            while xml_id in used_xml_ids:
                xml_id += '_'
            used_xml_ids.add(xml_id)
            edge = el(graph_element, G, 'edge', id=xml_id, source=a.get('id'), target=b.get('id'))
        edge.set('source', a.get('id'))
        edge.set('target', b.get('id'))
        before = old_relation.get(stable, {}).get('classification')
        if fresh or before != relationship['classification']:
            style_edge(edge, relationship, keymap, fresh)
            if not fresh:
                changed_styles.append({'id': stable, 'before': before, 'after': relationship['classification']})
        set_value(edge, keymap[('edge', 'sb_id')], stable)
        set_value(edge, keymap[('edge', 'sb_kind')], relationship['classification'])
        set_value(edge, keymap[('edge', 'sb_evidence')], '; '.join(sorted({r['origin'] for r in relationship['evidence']})))
        generated_edges.append(stable)
        edge_audit.append(dict(relationship, graph_edge_id=stable))
    for stable, edge in old_edges.items():
        if stable not in generated_edges:
            parents[edge].remove(edge)
    all_nodes = root.findall('.//g:node', NS)
    all_edges = root.findall('.//g:edge', NS)
    ids = [n.get('id') for n in all_nodes]
    assert len(ids) == len(set(ids)), 'Duplicate XML node ID'
    assert len({e.get('id') for e in all_edges}) == len(all_edges), 'Duplicate XML edge ID'
    assert all(e.get('source') in ids and e.get('target') in ids for e in all_edges), 'Invalid edge endpoint'
    for path in notes:
        assert sum(value(n, keymap[('node', 'sb_path')]) == path for n in all_nodes) == 1, 'Source represented more than once'
        assert hashlib.sha256((vault / path).read_bytes()).hexdigest() == notes[path]['sha256'], 'Source changed during scan'
    h_pairs = [(e['source'], e['target']) for e in relationships if e['classification'] == 'hierarchy'
               and e['source'] in notes and e['target'] in notes]
    scc = strongly_connected(set(notes), h_pairs)
    incoming = defaultdict(set)
    degree = defaultdict(int)
    for a, b in h_pairs:
        incoming[b].add(a)
    for e in relationships:
        if not e['source'].startswith('warning:') and not e['target'].startswith('warning:'):
            degree[e['source']] += 1
            degree[e['target']] += 1
    yaml_pairs = {(e['source'], e['target']) for e in relationships if any(r['origin'] == 'yaml' for r in e['evidence'])
                  and e['source'] in notes and e['target'] in notes}
    body_pairs = {(e['source'], e['target']) for e in relationships if any(r['origin'] == 'body' and
                  r['classification'] == 'hierarchy' for r in e['evidence']) and e['source'] in notes and e['target'] in notes}
    target = output_dir / (name + (' - Candidate' if accepted.exists() else '') + '.graphml')
    target_audit = target.with_suffix('.manifest.json')
    if target != accepted and target.exists():
        raise ValueError('A candidate already exists; review or archive it before another generation')
    totals = {'source_notes': len(notes), 'external_nodes': len(external), 'unresolved_nodes': len(warning_keys),
              'managed_nodes': len(generated_nodes), 'managed_edges': len(generated_edges),
              'manual_nodes_including_groups': len(all_nodes) - len(generated_nodes), 'manual_edges': len(manual_edges),
              'yaml_internal_hierarchy_edges': len(yaml_pairs), 'body_hierarchy_edges': len(body_pairs),
              'body_hierarchy_edges_additional_to_yaml': len(body_pairs - yaml_pairs),
              'body_link_occurrences_scanned': sum(e['origin'] == 'body' for e in evidence),
              'uncertain_body_links': sum(e['origin'] == 'body' and e['classification'] == 'uncertain' for e in evidence),
              'shared_children': sum(len(v) > 1 for v in incoming.values()),
              'cyclic_hierarchy_components': sum(len(part) > 1 for part in scc),
              'isolated_source_notes': sum(degree[k] == 0 for k in notes)}
    manifest = {'version': 1, 'generated_at': datetime.now(timezone.utc).isoformat(),
                'source': source.relative_to(vault).as_posix(), 'graph_file': target.name, 'totals': totals,
                'notes': {k: {'node_id': value(logical[k], keymap[('node', 'sb_id')]), 'sha256': v['sha256']} for k, v in notes.items()},
                'generated_node_ids': generated_nodes, 'generated_edge_ids': generated_edges,
                'relationships': edge_audit, 'unresolved_links': unresolved,
                'body_decisions': [e for e in evidence if e['origin'] == 'body'],
                'same_note_links_without_loops': self_links, 'ignored_media_and_urls': len(ignored),
                'isolated_notes': sorted(k for k in notes if degree[k] == 0),
                'cyclic_components': [p for p in scc if len(p) > 1],
                'changes': {'added_notes': sorted(added - set(renames)),
                            'removed_notes': sorted(removed - set(renames.values())),
                            'renamed_notes': [{'from': old, 'to': new, 'basis': 'unique unchanged content hash'} for new, old in renames.items()],
                            'changed_notes': sorted(k for k in set(notes) & old_paths if notes[k]['sha256'] != previous['notes'][k]['sha256']),
                            'new_node_ids': new_ids,
                            'new_edge_ids': sorted(set(generated_edges) - managed_edges),
                            'removed_edge_ids': sorted(managed_edges - set(generated_edges)),
                            'changed_classifications': changed_styles},
                'validation': {'xml_roundtrip': True, 'source_unchanged': True, 'each_source_once': True,
                               'valid_endpoints': True, 'existing_visual_data_preserved': old_root is not None,
                               'yEd_desktop_open_tested': False, 'initial_layout': 'seed grid; apply yEd Layout > Hierarchical'}}
    output_dir.mkdir(parents=True, exist_ok=True)
    ET.indent(root)
    ET.ElementTree(root).write(target, encoding='utf-8', xml_declaration=True)
    target_audit.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert len(ET.parse(target).getroot().findall('.//g:node', NS)) == len(all_nodes)
    print(json.dumps({'graph': str(target), 'manifest': str(target_audit), 'totals': totals}, ensure_ascii=False, indent=2))


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=DEFAULT_SOURCE)
    parser.add_argument('--name', default=DEFAULT_NAME)
    parser.add_argument('--inspect', action='store_true')
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    vault = vault_root()
    source = (vault / args.source).resolve()
    if not source.is_relative_to(vault) or not source.is_dir():
        raise ValueError('Source must be a folder inside the vault')
    build(vault, source, args.name, args.inspect, args.output_dir)


if __name__ == '__main__':
    main()
