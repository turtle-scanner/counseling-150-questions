import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    if '생활양식' in it['kw'] or '아들러' in it['kw'] or '생활양식' in it['ans']:
        print(f"Item {it['num']}: {it['kw']}")
        print(it['ans'])
        print('-'*40)
