import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'(\b[a-zA-Z0-9_]+\s*=\s*\[\s*\{\s*\"num\")', text)
if m:
    print('Found array definition:', m.group(0))
else:
    # search where "num" appears
    pos = text.find('"num"')
    print('Context around "num":')
    print(text[max(0, pos-50):pos+150])
