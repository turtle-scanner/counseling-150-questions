import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<button class="btn-control" id="btn-table" onclick="switchMode(\'table\')">📑 4개씩 표 모드</button>'
replacement = '<button class="btn-control" id="btn-table" onclick="switchMode(\'table\')">📑 4개씩 표 모드</button>\n      <a href="kice_d54_phase1_wordbook.html" class="btn-control" style="text-decoration:none; display:inline-flex; align-items:center; background:#0284c7; color:#fff; font-weight:bold;">📖 1단계(D-54) 암기 단어장</a>'

if target in html and 'kice_d54_phase1_wordbook.html' not in html:
    html = html.replace(target, replacement)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added 1단계 암기 단어장 button to compressed html!")
else:
    print("Already added or target not found.")
