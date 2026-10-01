import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'interactiveExamBox', text)]
print('Matches for interactiveExamBox:', matches)
for pos in matches:
    print('At pos:', pos, text[pos-50:pos+80])
