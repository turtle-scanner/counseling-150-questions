with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('originalItems')
print("originalItems index:", idx)
if idx != -1:
    print(text[idx:idx+200])
