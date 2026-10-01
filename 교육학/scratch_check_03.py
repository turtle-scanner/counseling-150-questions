import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_03회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q3 = f.read()

with open('0906_03회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a3 = f.read()

print('03회 문제지 길이:', len(text_q3))
print('03회 해설지 길이:', len(text_a3))
