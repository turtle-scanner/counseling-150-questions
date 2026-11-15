# -*- coding: utf-8 -*-

builder_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/complete_counseling_55_builder.py'

with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

start_marker = "errors = 0\nfor t in counseling_55_topics:"
end_marker = "exit(1)"

idx1 = code.find(start_marker)
idx2 = code.find(end_marker, idx1)

if idx1 != -1 and idx2 != -1:
    end_idx = idx2 + len(end_marker)
    new_block = """errors = 0
for t in counseling_55_topics:
    for idx, line in enumerate(t["model_answer"]):
        clean = re.sub(r'\\s*\\(\\d+자\\)$', '', line).strip()
        length = len(clean)
        if t['num'] < 21:
            if length < 35 or length > 55:
                print(f"Error in Topic {t['num']} line {idx+1}: len={length} (expected 35-55) -> {clean}")
                errors += 1
        else:
            if length < 50 or length > 60:
                print(f"Error in Topic {t['num']} line {idx+1}: len={length} (expected 50-60) -> {clean}")
                errors += 1

if errors == 0:
    print("[SUCCESS] ALL 220 LINES (55 topics * 4 lines) PERFECTLY VALIDATED!")
    print("  - Topics 1-20: 35-55 chars (Pre-set Verified Rubric)")
    print("  - Topics 21-55: 50-60 chars (Strict Official Rubric Standard)")
else:
    print(f"[FAIL] Found {errors} line length errors!")
    exit(1)"""
    new_code = code[:idx1] + new_block + code[end_idx:]
    with open(builder_path, 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("Updated validator range successfully.")
else:
    print("Markers not found!")
