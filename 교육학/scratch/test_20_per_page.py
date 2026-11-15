import subprocess, pypdf

# Let's test 20 items per page in test HTML
with open('scratch/test_20_per_page.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page { size: A4 portrait; margin: 4mm 5mm; }
body { margin: 0; padding: 0; font-family: sans-serif; font-size: 0.72rem; line-height: 1.15; }
.page { width: 100%; height: 288mm; max-height: 288mm; page-break-after: always; break-after: page; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; padding: 4px; border: 1px solid black; box-sizing: border-box; }
table { width: 100%; height: 100%; border-collapse: collapse; font-size: 0.70rem; table-layout: fixed; }
th, td { border: 1px solid black; padding: 1.5px 3px; vertical-align: middle; }
th { background: #eee; font-weight: bold; }
.kw { font-weight: bold; }
</style>
</head>
<body>
''')
    for p in range(10):
        f.write(f'''<div class="page">
<div style="font-weight:bold; font-size:0.85rem; border-bottom:1px solid black; margin-bottom:2px;">KICE 200제 암기장 [Page {p+1} / 10]</div>
<table>
<thead><tr><th style="width:5%;">No</th><th style="width:34%;">문제(단서)</th><th style="width:18%;">핵심 표제어</th><th style="width:35%;">모범 정답</th><th style="width:8%;">암기</th></tr></thead>
<tbody>''')
        for i in range(20):
            num = p * 20 + i + 1
            f.write(f'''<tr>
<td style="text-align:center;">{num}</td>
<td>평가 계획을 수업 활동 설계보다 앞서 수립하여 목표와 평가의 일관성을 극대화하는 역방향 설계 모형의 공식 명칭을 쓸 것.</td>
<td class="kw">백워드 설계 모형<br><span style="font-size:0.6rem; font-weight:normal;">(영속적 이해)</span></td>
<td>원하는 결과 확인 ➔ 수용 가능한 증거 결정 ➔ 학습 경험 및 교수 계획의 3단계를 거치는 백워드 설계 모형이다.</td>
<td style="text-align:center;">□</td>
</tr>''')
        f.write('</tbody></table></div>')
    f.write('</body></html>')

print("Created test HTML.")
