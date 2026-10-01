import sys
import os

sys.path.insert(0, 'scratch')
from generate_continuous_200 import all_200

artifact_dir = r'C:\Users\LENOVO\.gemini\antigravity\brain\022db66e-d9b4-4946-a17a-1330d1eea034'
if not os.path.exists(artifact_dir):
    os.makedirs(artifact_dir)

out_path = os.path.join(artifact_dir, '2027_전문상담_200제_영역별_암기장.md')

grouped = {}
for item in all_200:
    b = item['badge']
    if b not in grouped:
        grouped[b] = []
    grouped[b].append(item)

md = []
md.append('# 🏛️ 2027 KICE 전문상담 200제 영역별 핵심 암기장\n')
md.append('> [!TIP]')
md.append('> KICE 4점 만점 공식 서술 정답 및 핵심 표제어입니다. 학자명 힌트를 배제한 실전형 현상학적 문제로 구성되어 있습니다.\n')

for b, items in grouped.items():
    md.append(f'## 🎯 {b} 영역')
    md.append('<table>')
    md.append('<thead><tr><th width="5%">No</th><th width="20%">핵심 표제어</th><th width="35%">실전 단서 (문제)</th><th width="40%">공식 정답</th></tr></thead>')
    md.append('<tbody>')
    for it in items:
        md.append('<tr>')
        md.append(f'<td>{it["num"]}</td>')
        md.append(f'<td><b>{it["kw"]}</b></td>')
        md.append(f'<td>{it["q"]}</td>')
        md.append(f'<td>{it["ans"]}</td>')
        md.append('</tr>')
    md.append('</tbody>')
    md.append('</table>\n')

full_md = '\n'.join(md)
if '*' in full_md:
    full_md = full_md.replace('*', '★')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_md)
print("Artifact successfully created at", out_path)
