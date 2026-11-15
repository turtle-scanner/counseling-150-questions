# -*- coding: utf-8 -*-
import json
import re

html_path = 'g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/counseling_55_topics.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

m = re.search(r'const topics = (\[[\s\S]*?\]);', html_content)
topics = json.loads(m.group(1))

mismatches = []
for t in topics:
    num = t['num']
    for idx, line in enumerate(t.get('model_answer', [])):
        clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
        actual_len = len(clean)
        m_len = re.search(r'\((\d+)자\)$', line)
        if m_len:
            declared_len = int(m_len.group(1))
            if declared_len != actual_len:
                mismatches.append((num, idx+1, actual_len, declared_len, clean))

print(f"Total mismatches: {len(mismatches)}")
for num, row, actual, declared, text in mismatches[:20]:
    print(f"T{num} R{row}: actual={actual}, declared={declared} -> {text}")
