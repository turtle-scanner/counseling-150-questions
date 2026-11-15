# -*- coding: utf-8 -*-
import json

with open('full_exam_dump.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for section, qlist in [("전공 A형", d['questions_a']), ("전공 B형", d['questions_b'])]:
    print(f"\n==================== {section} ====================")
    for q in qlist:
        print(f"\n[{q['id']}] {q['type']} ({q['score']}점) - {q['title']}")
        if q['instructions']:
            print(f"작성방법: {q['instructions'].replace(chr(10), ' ')}")
        print(f"정답/모범답안:\n{q['answer']}")
