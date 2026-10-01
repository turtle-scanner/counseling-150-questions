import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_media = text.find('Media Print Styles')
print('Media Print Styles found at:', pos_media)
if pos_media != -1:
    print(text[pos_media:pos_media+800])
