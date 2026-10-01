import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

pos_a = text_q.find('## 【 2교시')
pos_b = text_q.find('## 【 3교시')

a_lines = text_q[pos_a:pos_b].split('\n')
for i, line in enumerate(a_lines[:120]):
    print(f'{i:3d}: {line}')
