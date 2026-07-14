from pathlib import Path
root = Path('frontend/src')
modified = []
for path in sorted(root.rglob('*.vue')):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    in_style = False
    changed = False
    out = []
    for line in lines:
        stripped = line.lstrip()
        if not in_style and '<style' in line:
            in_style = True
        if in_style and stripped.startswith('//'):
            changed = True
            continue
        out.append(line)
        if in_style and '</style>' in line:
            in_style = False
    if changed:
        path.write_text('\n'.join(out) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
        modified.append(str(path))
print('modified files:', len(modified))
for m in modified:
    print(m)
