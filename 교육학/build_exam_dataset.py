import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

# Let's inspect the domains and questions of 04회
# Major A questions (1..12)
# Major B questions (1..11)
# Pedagogy question (1)

def clean_stars(s):
    # Replace **text** with <strong>text</strong>, and * with empty or bullet
    s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
    s = s.replace('*', '')
    return s

print('clean_stars test done.')
