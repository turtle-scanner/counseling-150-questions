# -*- coding: utf-8 -*-
import re

with open('complete_counseling_55_builder.py', 'r', encoding='utf-8') as f:
    code = f.read()

match = re.search(r'counseling_55_topics = (\[[\s\S]*?\])\n\n# Validation', code)
topics = eval(match.group(1))

for t in topics:
    if t['num'] in [1, 2, 3, 4, 7, 8, 10, 11, 12, 21, 22, 23, 37, 38]:
        print(f"--- Topic {t['num']} ---")
        for idx, line in enumerate(t['model_answer']):
            clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
            print(f"L{idx+1} len={len(clean)}: {repr(line)}")
