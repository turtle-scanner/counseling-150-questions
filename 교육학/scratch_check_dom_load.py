import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('document.addEventListener(\'DOMContentLoaded\'')
print('DOMContentLoaded snippet:')
print(text[pos:pos+700])
