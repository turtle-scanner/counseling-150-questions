import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

print('=== Periods in 0906_04회 문제지 ===')
for line in text_q.split('\n'):
    if line.startswith('## 【'):
        print(line)
    elif line.startswith('문항 '):
        print('  ', line[:60])

print('=== Headings in 0906_04회 해설지 ===')
for line in text_a.split('\n'):
    if line.startswith('## 【') or line.startswith('### 문항') or line.startswith('문항 '):
        print(line[:60])
