import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_buttons = """<button class="btn-control" id="btn-table" onclick="switchMode('table')">📑 4개씩 표 모드</button>
      <button class="btn-control" id="btn-wrong" onclick="toggleWrongMode()" style="background:#dc2626; border-color:#b91c1c; color:#fff;">🔥 오답 집중 모드</button>
      <button class="btn-control" id="btn-mock20" onclick="startMockTest20()" style="background:#0284c7; border-color:#0369a1; color:#fff;">🎲 실전 20제 모의고사</button>
      <div style="display:inline-flex; align-items:center; gap:3px; margin-left:5px;">
        <button class="btn-control" onclick="adjustFontSize(-0.1)" title="글자 축소" style="padding:4px 8px; font-weight:900;">A-</button>
        <button class="btn-control" onclick="adjustFontSize(0.1)" title="글자 확대" style="padding:4px 8px; font-weight:900;">A+</button>
      </div>"""

html = re.sub(r'<button class="btn-control" id="btn-table"[^>]*>[\s\S]*?</button>', new_buttons, html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Buttons injected successfully!')
