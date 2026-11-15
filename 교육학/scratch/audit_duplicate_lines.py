import json, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

all_lines = []
for it in items:
    lines = [l.strip() for l in it['ans'].split('\n') if l.strip()]
    for l in lines:
        # strip line numbers like "1. ", "2. "
        clean_l = l
        if len(l) > 3 and l[0].isdigit() and l[1] == '.':
            clean_l = l[3:].strip()
        all_lines.append(clean_l)

counts = Counter(all_lines)
print("=== MOST FREQUENT LINES IN DECK ===")
for line, cnt in counts.most_common(15):
    if cnt > 1:
        print(f"[{cnt} times] {line[:60]}...")
