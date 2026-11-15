# -*- coding: utf-8 -*-
import re

builder_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/complete_counseling_55_builder.py'

with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 기존 유효성 검사 블록 찾기
old_block_pattern = r'errors = 0\s*for t in counseling_55_topics:[\s\S]*?if errors == 0:[\s\S]*?exit\(1\)'

new_block = """errors = 0
for t in counseling_55_topics:
    for idx, line in enumerate(t["model_answer"]):
        clean = re.sub(r'\\s*\\(\\d+자\\)$', '', line).strip()
        length = len(clean)
        if t['num'] < 21:
            if length < 38 or length > 48:
                print(f"Error in Topic {t['num']} line {idx+1}: len={length} (expected 38-48) -> {clean}")
                errors += 1
        else:
            if length < 50 or length > 60:
                print(f"Error in Topic {t['num']} line {idx+1}: len={length} (expected 50-60) -> {clean}")
                errors += 1

if errors == 0:
    print("[SUCCESS] ALL 220 LINES (55 topics * 4 lines) PERFECTLY VALIDATED!")
    print("  - Topics 1-20: 38-48 chars")
    print("  - Topics 21-55: 50-60 chars (Strict Official Rubric Standard)")
else:
    print(f"[FAIL] Found {errors} line length errors!")
    exit(1)"""

new_code, count = re.subn(old_block_pattern, new_block, code, count=1)
if count == 0:
    print("Warning: could not find old validator block with regex!")
    # 수동 교체 시도
    start_str = "errors = 0\nfor t in counseling_55_topics:"
    end_str = "exit(1)"
    idx1 = code.find(start_str)
    idx2 = code.find(end_str, idx1)
    if idx1 != -1 and idx2 != -1:
        new_code = code[:idx1] + new_block + code[idx2+len(end_str):]
        print("Replaced validator block manually.")
    else:
        print("Could not find start/end markers!")
else:
    print("Replaced validator block with regex.")

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Builder validation logic updated successfully.")
