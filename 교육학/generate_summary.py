import json

topics = json.load(open('topics_21_55_dump.json', encoding='utf-8'))
with open('topics_21_55_summary.txt', 'w', encoding='utf-8') as f:
    for t in topics:
        f.write(f"[{t['num']}] {t.get('title', '')}\n")
        for i, q in enumerate(t.get('sub_questions', []), 1):
            f.write(f"  Q{i}: {q}\n")
        for i, a in enumerate(t.get('four_lines', []), 1):
            f.write(f"  A{i} ({len(a)}자): {a}\n")
        f.write("\n")
print("Done")
