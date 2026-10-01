import os, json

with open('scratch/final_55_compressed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

ped_items = [it for it in items if it['badge'] in ['교육과정', '교육방법', '교육평가', '교육행정']]
coun_items = [it for it in items if it['badge'] not in ['교육과정', '교육방법', '교육평가', '교육행정']]

html = []
html.append('<!DOCTYPE html>')
html.append('<html lang="ko">')
html.append('<head>')
html.append('  <meta charset="UTF-8">')
html.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">')
html.append('  <title>2027 KICE 초압축 55제 암기장</title>')
html.append('  <style>')
html.append('    html, body { margin: 0; padding: 0; background: #0f1117; color: #e2e8f0; font-family: "Malgun Gothic", "맑은 고딕", sans-serif; -webkit-font-smoothing: antialiased; }')
html.append('    .app-header { max-width: 1000px; margin: 0 auto; background: #161a23; padding: 16px 20px; border-bottom: 2px solid #d97706; text-align: center; }')
html.append('    .app-title { font-size: 1.25rem; font-weight: 800; color: #fbbf24; margin-bottom: 5px; }')
html.append('    .app-sub { font-size: 0.9rem; color: #94a3b8; }')
html.append('    .main-container { max-width: 1000px; margin: 20px auto; padding: 0 10px; }')
html.append('    .section-title { font-size: 1.15rem; font-weight: 800; color: #38bdf8; margin: 30px 0 10px 0; border-left: 4px solid #38bdf8; padding-left: 10px; }')
html.append('    .table-container { background: #11141d; border: 1.5px solid #2d3748; border-radius: 8px; overflow-x: auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }')
html.append('    table { width: 100%; border-collapse: collapse; font-size: 10pt; min-width: 600px; }')
html.append('    th { background: #161a24; color: #fbbf24; border: 1px solid #283042; padding: 10px; font-weight: 800; text-align: center; word-break: keep-all; overflow-wrap: break-word; }')
html.append('    td { border: 1px solid #222938; padding: 10px; line-height: 1.6; word-break: keep-all; overflow-wrap: break-word; vertical-align: top; }')
html.append('    tr:nth-child(even) { background: #141822; }')
html.append('    tr:nth-child(odd) { background: #10131b; }')
html.append('    .td-num { text-align: center; color: #fbbf24; font-weight: 800; }')
html.append('    .td-badge { color: #38bdf8; font-size: 8.5pt; font-weight: 700; display: block; margin-bottom: 4px; }')
html.append('    .td-kw { font-weight: 800; color: #fde047; }')
html.append('    .td-q { color: #f1f5f9; }')
html.append('    .td-ans { color: #fef08a; font-weight: 600; }')
html.append('    @media (max-width: 768px) {')
html.append('      th, td { font-size: 9.5pt; padding: 8px; }')
html.append('      .app-title { font-size: 1.1rem; }')
html.append('    }')
html.append('  </style>')
html.append('</head>')
html.append('<body>')
html.append('  <div class="app-header">')
html.append('    <div class="app-title">🚨 2027 KICE 출제확률 99% 초압축 55제</div>')
html.append('    <div class="app-sub">현상학적 단서 문맥 교정 완료 · 모바일 최적화 웜다크 배색</div>')
html.append('  </div>')
html.append('  <div class="main-container">')

# Pedagogy
html.append('    <div class="section-title">🎯 1교시: 교육학 논술 핵심 20선</div>')
html.append('    <div class="table-container">')
html.append('      <table>')
html.append('        <thead><tr><th width="5%">No</th><th width="20%">영역 및 표제어</th><th width="40%">실전 단서 (핵심 키워드)</th><th width="35%">공식 정답</th></tr></thead>')
html.append('        <tbody>')
for i, it in enumerate(ped_items):
    html.append('<tr>')
    html.append(f'<td class="td-num">{i+1}</td>')
    html.append(f'<td><span class="td-badge">{it["badge"]}</span><span class="td-kw">{it["kw"]}</span></td>')
    html.append(f'<td class="td-q">{it["q"]}</td>')
    html.append(f'<td class="td-ans">{it["ans"]}</td>')
    html.append('</tr>')
html.append('        </tbody></table>')
html.append('    </div>')

# Counseling
html.append('    <div class="section-title">🎯 2~3교시: 전공상담 복합형 킬러 35선</div>')
html.append('    <div class="table-container">')
html.append('      <table>')
html.append('        <thead><tr><th width="5%">No</th><th width="20%">영역 및 표제어</th><th width="40%">실전 단서 (핵심 키워드)</th><th width="35%">공식 정답</th></tr></thead>')
html.append('        <tbody>')
for i, it in enumerate(coun_items):
    html.append('<tr>')
    html.append(f'<td class="td-num">{i+1}</td>')
    html.append(f'<td><span class="td-badge">{it["badge"]}</span><span class="td-kw">{it["kw"]}</span></td>')
    html.append(f'<td class="td-q">{it["q"]}</td>')
    html.append(f'<td class="td-ans">{it["ans"]}</td>')
    html.append('</tr>')
html.append('        </tbody></table>')
html.append('    </div>')

html.append('  </div>')
html.append('</body>')
html.append('</html>')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))

print(f'Successfully generated HTML at {target_path}')
