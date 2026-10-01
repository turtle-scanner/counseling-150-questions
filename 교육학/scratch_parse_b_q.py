import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

p3_start = text_q.find('## 【 3교시')
major_b_text = text_q[p3_start:]

lines = major_b_text.split('\n')
q_indices = []
for i, line in enumerate(lines):
    if re.match(r'^\*{0,2}\d+\.\*{0,2}\s+', line.strip()) or re.match(r'^문항\s+\d+번', line.strip()):
        q_indices.append((i, line.strip()))

print('Found question markers in B형:', len(q_indices))
for idx, text in q_indices:
    print(f'Line {idx}: {text[:70]}')
