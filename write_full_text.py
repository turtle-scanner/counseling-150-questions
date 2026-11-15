# -*- coding: utf-8 -*-
import json

with open('full_exam_dump.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('all_qa_qb_text.txt', 'w', encoding='utf-8') as out:
    for section, qlist in [("전공 A형", d['questions_a']), ("전공 B형", d['questions_b'])]:
        out.write(f"\n==================== {section} (총 {len(qlist)}문항 / 40점) ====================\n\n")
        for q in qlist:
            out.write(f"[{section} {q['num']}번] {q['type']} ({q['score']}점)\n")
            out.write(f"제목: {q['title']}\n\n")
            out.write(f"[지문]\n{q['content']}\n\n")
            if q['instructions']:
                out.write(f"{q['instructions']}\n\n")
            out.write(f"{q['answer']}\n\n")
            out.write("-" * 60 + "\n\n")

print("Finished writing all_qa_qb_text.txt")
