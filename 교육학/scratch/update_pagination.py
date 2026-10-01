import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change pagination
html = html.replace('const itemsPerPage = 6;', 'const itemsPerPage = 4;')
html = html.replace('◀ 이전 6개', '◀ 이전 4개')
html = html.replace('다음 6개 ▶', '다음 4개 ▶')
html = html.replace('📋 6개씩 표 모드', '📋 4개씩 표 모드')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Pagination updated to 4 items.")
