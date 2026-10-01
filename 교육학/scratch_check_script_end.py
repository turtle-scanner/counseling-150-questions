import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_end = text.rfind('</script>')
print('Last 60 lines of script in index.html:')
print(text[pos_end-2000:pos_end])
