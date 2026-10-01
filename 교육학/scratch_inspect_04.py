import sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

print('0906_04회 문제지 length:', len(text_q))
print('0906_04회 해설지 length:', len(text_a))

# Let's inspect the questions in 0906_04회
import re
q_headers = re.findall(r'### 문항.*', text_q)
print('Question headers found:', len(q_headers))
for qh in q_headers[:10]:
    print(' -', qh)
