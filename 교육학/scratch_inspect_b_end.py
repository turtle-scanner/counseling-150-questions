import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

lines = text_a.split('\n')
for i, line in enumerate(lines[95:]):
    print(f'{i+95:3d}: {line}')
