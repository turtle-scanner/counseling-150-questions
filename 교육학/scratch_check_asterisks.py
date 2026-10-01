import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the questions and build the dataset
with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

# Check for any asterisks or forbidden terms in raw files
print('Raw text_q asterisks:', text_q.count('*'))
print('Raw text_a asterisks:', text_a.count('*'))
