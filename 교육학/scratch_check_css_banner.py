import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_banner = text.find('.exam-header-banner')
print('.exam-header-banner pos:', pos_banner)
if pos_banner != -1:
    print(text[pos_banner:pos_banner+600])
