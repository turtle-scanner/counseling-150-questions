import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make table base font larger
html = html.replace('table { width: 100%; border-collapse: collapse; font-size: 10pt; min-width: 600px; }', 'table { width: 100%; border-collapse: collapse; font-size: 1.05rem; min-width: 600px; }')

# Make specific cells more readable
html = html.replace('.td-kw { font-weight: 800; color: #fde047; }', '.td-kw { font-weight: 800; color: #fde047; font-size: 1.15rem; display: block; margin-top: 5px; }')
html = html.replace('.td-q { color: #f1f5f9; }', '.td-q { color: #ffffff; font-size: 1.1rem; font-weight: 700; line-height: 1.7; }')
html = html.replace('.td-ans { color: #fef08a; font-weight: 600; }', '.td-ans { color: #fef08a; font-weight: 700; font-size: 1.05rem; line-height: 1.7; }')

# Tablet specific table tweaks
html = html.replace('th, td { font-size: 11pt; padding: 15px; }', 'th, td { font-size: 1.15rem; padding: 18px; line-height: 1.7; }')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Table visibility improved.")
