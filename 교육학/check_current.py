import json

topics = json.load(open('topics_21_55_dump.json', encoding='utf-8'))
with open('current_answers_21_55.txt', 'w', encoding='utf-8') as f:
    for t in topics:
        f.write(f"[{t['num']}] {t['title']}\n")
        for i, a in enumerate(t.get('four_lines', []), 1):
            f.write(f"  L{i} ({len(a)}자): {a}\n")
        f.write("\n")
print("Done")
