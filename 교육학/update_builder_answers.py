# -*- coding: utf-8 -*-
import json
import re
from validate_50_60 import topics_21_55_answers_50_60

builder_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/complete_counseling_55_builder.py'

with open(builder_path, 'r', encoding='utf-8') as f:
    builder_code = f.read()

# complete_counseling_55_builder.py에서 counseling_55_topics 부분 교체
# 먼저 Python의 ast나 파싱을 쓰거나, json / 정규식으로 안전하게 업데이트

# 각 topic num별로 model_answer를 교체
for num, lines in sorted(topics_21_55_answers_50_60.items()):
    formatted_lines = [f"{line} ({len(line)}자)" for line in lines]
    
    # 해당 num의 model_answer 블록을 찾기
    # "num": <num>, ... "model_answer": [ ... ]
    pattern = rf'("num":\s*{num}\b[\s\S]*?"model_answer":\s*\[)([\s\S]*?)(\])'
    
    def repl(m):
        prefix = m.group(1)
        suffix = m.group(3)
        indent = "            "
        lines_str = "\n" + ",\n".join([f'{indent}"{fl}"' for fl in formatted_lines]) + "\n        "
        return prefix + lines_str + suffix

    builder_code, count = re.subn(pattern, repl, builder_code, count=1)
    if count == 0:
        print(f"Warning: could not update topic {num} in builder!")
    else:
        print(f"Topic {num} updated in builder.")

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(builder_code)

print("Builder code updated successfully with 50-60 char answers!")
