import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('>🎓 교육학 (18)<', '>🎓 교육학 (33)<'),
    ('>💡 상담이론·치료 (25)<', '>💡 상담이론·치료 (41)<'),
    ('>🚨 위기·법령·윤리 (25)<', '>🚨 위기·법령·윤리 (22)<'),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"Updated pill {old} -> {new}")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
