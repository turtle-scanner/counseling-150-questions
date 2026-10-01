import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

# find question patterns in A형
pos_a = text_q.find('## 【 2교시')
pos_b = text_q.find('## 【 3교시')

print('--- Question headings in A형 ---')
for line in text_q[pos_a:pos_b].split('\n'):
    if re.match(r'^(문항|\d+번|###|\[문항|\*\*문항)', line):
        print(line[:80])

print('--- Question headings in B형 ---')
for line in text_q[pos_b:].split('\n'):
    if re.match(r'^(문항|\d+번|###|\[문항|\*\*문항)', line):
        print(line[:80])
