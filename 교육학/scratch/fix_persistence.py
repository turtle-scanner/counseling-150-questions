import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add persistent save logic to renderCard
html = html.replace('updateDashboard();', "updateDashboard();\n      localStorage.setItem('kice_last_kw', item.kw);")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Persistent logic added successfully.")
