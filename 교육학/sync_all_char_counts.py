# -*- coding: utf-8 -*-
import json
import re

builder_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/complete_counseling_55_builder.py'

with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# complete_counseling_55_builder.py의 model_answer 안의 각 줄마다 실제 글자수를 계산하여 (XX자) 동기화
# 정규식으로 "(.*)" 안의 문자열에서 (\d+자) 부분을 실제 글자수로 교체

def fix_line(m):
    full_str = m.group(1)
    # 뒤의 (XX자) 제거
    clean = re.sub(r'\s*\(\d+자\)$', '', full_str).strip()
    actual_len = len(clean)
    return f'"{clean} ({actual_len}자)"'

# builder_code 내의 model_answer 리스트 내부 행들을 보정
# counseling_55_topics 데이터 블록 내에서 교체
fixed_code = re.sub(r'"([^"\n]+?\(\d+자\))"', fix_line, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(fixed_code)

print("Synchronized all (XX자) labels with actual char lengths in builder!")
