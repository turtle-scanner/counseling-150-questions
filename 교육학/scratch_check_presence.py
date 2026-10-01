import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('Has interactiveExamBox:', 'interactiveExamBox' in text)
print('Has draftModal:', 'draftModal' in text)
print('Has kicePrintExamContainer:', 'kicePrintExamContainer' in text)
