import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the corrupted regex
html = re.sub(r"elQ\.innerHTML = item\.q\.replace\(/[^/]*?/g, '<span style=\"color:#d97706; font-weight:bold;\">[^<]*?</span>'\);", "elQ.innerHTML = formatText(item.q);", html)
html = html.replace("elQ.innerHTML = item.q.replace(/??g, '<span style=\"color:#d97706; font-weight:bold;\">??/span>');", "elQ.innerHTML = formatText(item.q);")
html = html.replace("??g", "") # just in case

# Make sure it's correct
if "formatText(item.q)" not in html:
    html = html.replace("elKw.innerHTML = formatText(item.kw);", "elQ.innerHTML = formatText(item.q);\n        elKw.innerHTML = formatText(item.kw);")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Regex syntax error fixed.")
