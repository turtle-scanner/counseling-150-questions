import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_print = text.find('@media print')
if pos_print != -1:
    print('Current @media print:')
    print(text[pos_print:pos_print+1200])
else:
    print('No @media print found')
