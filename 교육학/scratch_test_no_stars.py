import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('0906_04회_초고난도_KICE_실전모의고사_문제지.md', 'r', encoding='utf-8') as f:
    text_q = f.read()

with open('0906_04회_초고난도_KICE_실전모의고사_해설_및_칼채점기준표.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

def no_stars(text):
    if not text:
        return ''
    # Convert **bold** to <strong>bold</strong>
    s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Remove any remaining single asterisks
    s = s.replace('*', '')
    return s

# Test on a small snippet
sample = "**1번 (2점)** : ㉠ **수용형** [1점], ㉡ **과보호형** [1점]"
print('Sample converted:', no_stars(sample))
assert '*' not in no_stars(sample)
print('Zero asterisks verified!')
