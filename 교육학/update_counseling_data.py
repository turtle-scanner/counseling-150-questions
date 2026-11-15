# -*- coding: utf-8 -*-
import json
from validate_50_60 import topics_21_55_answers_50_60

data_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/counseling_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    topics = json.load(f)

updated_count = 0
for t in topics:
    num = t.get('num')
    if num in topics_21_55_answers_50_60:
        t['four_lines'] = topics_21_55_answers_50_60[num]
        updated_count += 1

with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} topics in counseling_data.json successfully.")
