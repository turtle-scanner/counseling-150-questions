import sys, json

with open('scratch/final_55_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

found = [it for it in items if '단절' in it['kw'] or '단절' in it['q'] or '단절' in it['ans']]

with open('scratch/cutoff.txt', 'w', encoding='utf-8') as f:
    for it in found:
        f.write(f"{it['num']} | {it['kw']} | {it['ans']}\n")
