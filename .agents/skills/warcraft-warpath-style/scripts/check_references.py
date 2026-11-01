"""Read-only check of the original corpus and local skill links. Standard library only."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote


def check(skill_root: Path) -> list[str]:
    issues: list[str] = []
    manifest = json.loads((skill_root / 'references' / 'manifest.json').read_text(encoding='utf-8'))
    references = manifest['images']
    expected_ids = [f'{i:03d}' for i in range(1, 44)]
    actual_ids = [entry['id'] for entry in references]
    if actual_ids != expected_ids:
        issues.append('Manifest must list IDs 001 through 043 exactly once and in order.')
    atlas_text = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((skill_root / 'references').glob('atlas-*.md')))
    atlas_ids = re.findall(r'^## (\d{3}) ·', atlas_text, flags=re.MULTILINE)
    if atlas_ids != expected_ids:
        issues.append('Atlas must cover IDs 001 through 043 exactly once and in order.')
    for entry in references:
        source = (skill_root / entry['skill_relative_path']).resolve()
        if not source.is_relative_to(skill_root):
            issues.append(f"Reference escapes skill: {entry['id']}")
            continue
        if not source.is_file():
            issues.append(f'Missing original: {source}')
            continue
        data = source.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n':
            issues.append(f'Not a PNG: {source.name}')
            continue
        width, height = struct.unpack('>II', data[16:24])
        if (width, height) != (entry['width'], entry['height']):
            issues.append(f'Dimensions changed: {source.name}')
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            issues.append(f'Original bytes changed: {source.name}')
        if entry['filename'] not in atlas_text:
            issues.append(f"Original is not linked from atlas: {entry['id']}")

    # Relative links resolve from their document, not from the working directory.
    for doc in skill_root.rglob('*.md'):
        text = doc.read_text(encoding='utf-8')
        for raw in re.findall(r'\]\(([^)]+)\)', text):
            raw = raw.strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', raw) or raw.startswith('#'):
                continue
            raw = unquote(raw.split('#', 1)[0])
            target = (doc.parent / raw).resolve()
            if not target.is_relative_to(skill_root):
                issues.append(f'Local link escapes skill: {doc.name}: {raw}')
            elif not target.exists():
                issues.append(f'Broken local link: {doc.name}: {raw}')
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    issues = check(skill_root)
    if issues:
        for issue in issues:
            print(f'FAIL: {issue}')
        return 1
    print('PASS: 43 original PNGs match SHA-256 and dimensions; 43 atlas entries and local skill links are valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
