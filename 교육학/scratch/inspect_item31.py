import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Check in kice_55_core_compressed.html
path_comp = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(path_comp, 'r', encoding='utf-8') as f:
    text_comp = f.read()

idx = text_comp.find('계획된 우연 5대 기술')
print("In compressed html around index:", idx)
print(text_comp[idx:idx+600])
