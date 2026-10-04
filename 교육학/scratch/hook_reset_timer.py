import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

target = '        updateDashboard();\n      localStorage.setItem(\'kice_last_kw\', item.kw);'
replacement = '        updateDashboard();\n        if (typeof resetTimer90 === "function") resetTimer90();\n        if (typeof clearCanvas === "function") clearCanvas();\n      localStorage.setItem(\'kice_last_kw\', item.kw);'

if target in html:
    html = html.replace(target, replacement)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully hooked resetTimer90 & clearCanvas in renderCard!")
else:
    print("Target not found!")
