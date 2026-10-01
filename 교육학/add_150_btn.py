import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_btn = '<button class="btn" onclick="printCore150PDF()">🖨️ 핵심 150선 PDF 인쇄</button>'
new_btn = """<button class="btn" onclick="printCore150PDF()">🖨️ 핵심 150선 PDF 인쇄</button>
      <button class="btn" id="btnMode150Sheet" style="background: linear-gradient(135deg, #7c3aed, #6d28d9); border-color: #a78bfa; color: #fff;" onclick="window.open('kice_150_core_table_a4.html', '_blank')">📑 [ADHD 맞춤] 핵심 150제 A4 10장 표</button>"""

text = text.replace(old_btn, new_btn, 1)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Added 10-page A4 table button to index.html.')
