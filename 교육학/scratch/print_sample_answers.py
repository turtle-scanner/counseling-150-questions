import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in [0, 1, 2, 20, 50, 100, 150, 200]:
    it = items[i]
    print(f"=== Item {it['num']}: {it['kw']} ===")
    print(it['ans'])
    print()
