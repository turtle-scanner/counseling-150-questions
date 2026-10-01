import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Select Option
html = html.replace('<option value="천개의문">👑 천개의문</option>', '<option value="1000">👑 1000</option>')

# 2. Update the USERS mapping
html = html.replace('"1000개의 문": "371400", "천개의문": "371400",', '"1000": "371400",')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated Master ID to 1000.")
