# -*- coding: utf-8 -*-
import json

with open('counseling_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('topics_21_to_55_info.txt', 'w', encoding='utf-8') as out:
    for t in data:
        if t['num'] >= 21:
            out.write(f"=== TOPIC {t['num']}: {t['title']} ({t['domain']}) ===\n")
            out.write(f"Concept: {t.get('concept', '')}\n")
            out.write("Sub-questions:\n")
            for idx, q in enumerate(t.get('sub_questions', [])):
                out.write(f"  Q{idx+1}: {q}\n")
            out.write("Keywords: " + ", ".join(t.get('keywords', [])) + "\n")
            out.write("Current answers:\n")
            for idx, a in enumerate(t.get('model_answer', [])):
                out.write(f"  Line {idx+1}: {a}\n")
            out.write("\n")

print("Wrote topics_21_to_55_info.txt")
