import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Read 문제지 and 해설지 for 0906_04회
with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

# Let's inspect how to parse each question
# 1교시: 교육학
p1_q = text_q[text_q.find('## 【 1교시'):text_q.find('## 【 2교시')]
p1_a = text_a[text_a.find('## 【 1교시'):text_a.find('## 【 2교시')]

# 2교시: 전공상담 A형
p2_q = text_q[text_q.find('## 【 2교시'):text_q.find('## 【 3교시')]
p2_a = text_a[text_a.find('## 【 2교시'):text_a.find('## 【 3교시')]

# 3교시: 전공상담 B형
p3_q = text_q[text_q.find('## 【 3교시'):]
p3_a = text_a[text_a.find('## 【 3교시'):]

print('Partitions successfully read.')
