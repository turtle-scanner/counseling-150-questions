# -*- coding: utf-8 -*-
with open('g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'@media print', content)]
print_funcs = [m.start() for m in re.finditer(r'function.*print|executePrint', content)]

with open('print_inspection_result.txt', 'w', encoding='utf-8') as out:
    out.write(f"File length: {len(content)}\n")
    for idx in matches:
        out.write("--- PRINT CSS SNIPPET ---\n")
        out.write(content[idx:idx+3500] + "\n\n")
    for idx in print_funcs:
        out.write("--- PRINT JS SNIPPET ---\n")
        out.write(content[idx:idx+3500] + "\n\n")

print("Inspection completed.")
