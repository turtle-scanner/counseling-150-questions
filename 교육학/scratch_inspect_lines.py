import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

lines = text_q.split('\n')
print('First 40 lines of 0906_04회 문제지:')
for line in lines[:40]:
    print(line)
