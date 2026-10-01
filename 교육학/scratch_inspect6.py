import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# search for 150 in index.html
matches = re.findall(r'.{0,50}150.{0,50}', text)
print('Occurrences of 150 in index.html:', len(matches))
for m in matches[:10]:
    print(' -', m.strip())

# Check filter pills and mode buttons in index.html
pos_mode = text.find('class="mode-selector"')
if pos_mode != -1:
    print('Mode selector snippet:')
    print(text[pos_mode:pos_mode+800])

pos_filter = text.find('id="periodFilters"')
if pos_filter != -1:
    print('Period filters snippet:')
    print(text[pos_filter:pos_filter+800])
