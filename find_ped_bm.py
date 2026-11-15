# -*- coding: utf-8 -*-
with open('build_master.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('bm_ped_lines.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if 'pedagogy' in line.lower() or 'ped_03' in line.lower():
            out.write(f"{i+1}: {line}")

print("Wrote bm_ped_lines.txt")
