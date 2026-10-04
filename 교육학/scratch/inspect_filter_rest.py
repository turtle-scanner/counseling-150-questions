import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function filterByCategory')
print(text[idx:idx+1200])
