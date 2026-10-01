import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_view = text.find('id="examView"')
print(text[pos_view:pos_view+2000])

# Find switchExamTab
pos_func = text.find('function switchExamTab')
print('switchExamTab function:')
print(text[pos_func:pos_func+1500])
