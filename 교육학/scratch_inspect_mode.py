import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_mode = text.find('function setMode(')
print('setMode function:')
print(text[pos_mode:pos_mode+800])

# inspect header / nav HTML
pos_header = text.find('<header>')
if pos_header == -1:
    pos_header = text.find('<header')
print('Header HTML:')
print(text[pos_header:pos_header+1200])
