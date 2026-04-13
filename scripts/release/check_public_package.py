#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import zipfile

ARCHIVE = Path(__file__).resolve().parents[2] / 'dist' / 'auto-proteomics.skill'
def main() -> int:
    if not ARCHIVE.exists():
        print(f'Missing archive: {ARCHIVE}', file=sys.stderr)
        return 1
    names = []
    with zipfile.ZipFile(ARCHIVE) as zf:
        names = zf.namelist()
    bad = []
    for name in names:
        lowered = name.lower()
        if '/examples/' in lowered and '/results/' in lowered:
            bad.append(name)
            continue
        if 'mock' in lowered:
            bad.append(name)
    if bad:
        print('Forbidden packaged entries found:', file=sys.stderr)
        for name in bad:
            print(name, file=sys.stderr)
        return 1
    print(f'Archive check passed: {len(names)} entries')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
