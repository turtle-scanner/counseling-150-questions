# -*- coding: utf-8 -*-
import re

with open('complete_counseling_55_builder.py', 'r', encoding='utf-8') as f:
    code = f.read()

match = re.search(r'counseling_55_topics = (\[[\s\S]*?\])\n\n# Validation', code)
topics = eval(match.group(1))

with open('counseling_line_errors.txt', 'w', encoding='utf-8') as out:
    for t in topics:
        for idx, line in enumerate(t['model_answer']):
            clean = re.sub(r'\s*\(\d+자\)$', '', line).strip()
            l = len(clean)
            if l < 38 or l > 45:
                num = t['num']
                out.write(f"Topic {num} line {idx+1} len={l}: {clean}\n")

print("Done writing errors.")
