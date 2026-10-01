import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

print('문제지 길이:', len(text_q))
print('해설지 길이:', len(text_a))

# Let's see how 1교시, 2교시, 3교시 are partitioned in 문제지
p1_start = text_q.find('## 【 1교시')
p2_start = text_q.find('## 【 2교시')
p3_start = text_q.find('## 【 3교시')

pedagogy_q = text_q[p1_start:p2_start]
major_a_q = text_q[p2_start:p3_start]
major_b_q = text_q[p3_start:]

print('1교시 문제 길이:', len(pedagogy_q))
print('2교시 A형 문제 길이:', len(major_a_q))
print('3교시 B형 문제 길이:', len(major_b_q))

# Answers partitioned
ap1_start = text_a.find('## 【 1교시')
ap2_start = text_a.find('## 【 2교시')
ap3_start = text_a.find('## 【 3교시')

pedagogy_a = text_a[ap1_start:ap2_start]
major_a_a = text_a[ap2_start:ap3_start]
major_b_a = text_a[ap3_start:]

print('1교시 해설 길이:', len(pedagogy_a))
print('2교시 A형 해설 길이:', len(major_a_a))
print('3교시 B형 해설 길이:', len(major_b_a))
