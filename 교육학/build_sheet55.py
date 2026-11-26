# -*- coding: utf-8 -*-
import json, html, shutil

data = json.load(open('kice_55_4lines_master.json', encoding='utf-8'))

# 대표님 실전 채점에서 실제로 걸렸던 오답/함정 주의 18선
TRAP_IDS = {1, 7, 9, 11, 12, 13, 16, 18, 19, 23, 26, 27, 29, 30, 31, 41, 42, 43, 45, 47, 51, 53, 54}

def highlight(line, kws):
    out = html.escape(line)
    # 긴 키워드부터 치환
    for kw in sorted(set(kws), key=len, reverse=True):
        ekw = html.escape(kw)
        if ekw and ekw in out:
            out = out.replace(ekw, f'<span class="kw">{ekw}</span>')
    return out

cards_html = []
for it in data:
    tid = it['id']
    part = it['part'] # PED10 or COUNSEL45
    domain = html.escape(it.get('domain', ''))
    title = html.escape(it.get('title', ''))
    kws = it.get('keywords', [])
    lines = it.get('lines', [])
    is_trap = tid in TRAP_IDS
    trap_badge = '<span class="trap-badge">🚨 오답주의</span>' if is_trap else ''
    part_cls = 'ped' if part == 'PED10' else 'csl'
    part_label = '교육학 6줄' if part == 'PED10' else '전공 4줄'

    lines_html = '\n'.join(
        f'<div class="ans-line"><span class="ln-no">{idx+1}</span><span class="ln-txt">{highlight(ln, kws)}</span></div>'
        for idx, ln in enumerate(lines)
    )
    cards_html.append(f'''
    <article class="card {part_cls} {'trap' if is_trap else ''}" data-part="{part}" data-trap="{'1' if is_trap else '0'}">
      <div class="card-head">
        <div class="card-title-wrap">
          <span class="num-badge">#{tid:02d}</span>
          <span class="part-badge {part_cls}">{part_label}</span>
          <span class="dom-badge">{domain}</span>
          {trap_badge}
        </div>
        <h2 class="card-title">{title}</h2>
      </div>
      <div class="card-lines">
        {lines_html}
      </div>
    </article>''')

page = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2027학년도(11.28) KICE 핵심키워드 55제 공식 4줄(교육학 6줄) 요약 답안지</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Noto Sans KR', sans-serif;
    background: #0b1120;
    color: #f1f5f9;
    padding: 14px 12px 60px;
    line-height: 1.5;
  }}
  .toolbar {{
    position: sticky; top: 6px; z-index: 100;
    max-width: 1120px; margin: 0 auto 16px;
    background: rgba(15, 23, 42, 0.96);
    backdrop-filter: blur(8px);
    border: 1.5px solid #38bdf8;
    border-radius: 10px;
    padding: 10px 14px;
    display: flex; flex-wrap: wrap; gap: 8px;
    align-items: center; justify-content: space-between;
    box-shadow: 0 8px 24px rgba(0,0,0,0.45);
  }}
  .btn-group {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }}
  .btn {{
    border: 1px solid #334155; background: #1e293b; color: #e2e8f0;
    padding: 6px 11px; border-radius: 6px; font-size: 0.82rem; font-weight: 700;
    cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 4px;
  }}
  .btn.active {{ background: #fbbf24; color: #451a03; border-color: #f59e0b; }}
  .btn.rose {{ background: #e11d48; color: #fff; border-color: #f43f5e; }}
  .btn.sky {{ background: #0284c7; color: #fff; border-color: #38bdf8; }}
  .header-banner {{
    max-width: 1120px; margin: 0 auto 14px;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 1px solid #334155; border-radius: 10px;
    padding: 14px 18px;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
  }}
  .header-banner h1 {{ font-size: 1.15rem; color: #fbbf24; font-weight: 900; }}
  .header-banner p {{ font-size: 0.84rem; color: #94a3b8; }}
  .grid {{
    max-width: 1120px; margin: 0 auto;
    display: grid; grid-template-columns: repeat(auto-fill, minmax(480px, 1fr));
    gap: 10px;
  }}
  @media (max-width: 560px) {{
    .grid {{ grid-template-columns: 1fr; }}
    .toolbar {{ position: static; }}
  }}
  .card {{
    background: #111827;
    border: 1.5px solid #334155;
    border-radius: 8px;
    padding: 10px 12px;
    break-inside: avoid;
  }}
  .card.ped {{ border-left: 4px solid #38bdf8; }}
  .card.csl {{ border-left: 4px solid #fbbf24; }}
  .card.trap {{ border-color: #f43f5e; }}
  .card-head {{ margin-bottom: 7px; border-bottom: 1px solid #1f2937; padding-bottom: 6px; }}
  .card-title-wrap {{ display: flex; flex-wrap: wrap; gap: 5px; align-items: center; margin-bottom: 4px; }}
  .num-badge {{ background: #0f172a; color: #fbbf24; font-weight: 900; font-size: 0.78rem; padding: 1px 6px; border-radius: 4px; border: 1px solid #475569; }}
  .part-badge {{ font-size: 0.72rem; font-weight: 800; padding: 1px 6px; border-radius: 4px; }}
  .part-badge.ped {{ background: rgba(56,189,248,0.18); color: #38bdf8; }}
  .part-badge.csl {{ background: rgba(251,191,36,0.18); color: #fbbf24; }}
  .dom-badge {{ font-size: 0.72rem; color: #94a3b8; }}
  .trap-badge {{ background: rgba(244,63,94,0.2); color: #fda4af; border: 1px solid #f43f5e; font-size: 0.72rem; font-weight: 800; padding: 1px 6px; border-radius: 4px; }}
  .card-title {{ font-size: 0.92rem; font-weight: 800; color: #f8fafc; }}
  .card-lines {{ display: flex; flex-direction: column; gap: 4px; }}
  .ans-line {{ display: flex; gap: 6px; font-size: 0.86rem; color: #e2e8f0; align-items: baseline; }}
  .ln-no {{
    flex-shrink: 0; width: 18px; height: 18px; line-height: 18px; text-align: center;
    font-size: 0.72rem; font-weight: 800; border-radius: 50%;
    background: #1e293b; color: #94a3b8;
  }}
  .kw {{
    color: #fde047; background: rgba(250, 204, 21, 0.16);
    font-weight: 800; padding: 0 3px; border-radius: 3px;
    transition: all 0.15s;
  }}
  body.hide-kw .kw {{
    color: transparent; background: #334155; border-radius: 3px; user-select: none; cursor: pointer;
  }}
  body.hide-kw .kw.revealed {{
    color: #fde047; background: rgba(250, 204, 21, 0.16);
  }}
  @media print {{
    body {{ background: #fff; color: #111; padding: 0; }}
    .toolbar {{ display: none !important; }}
    .header-banner {{ background: #fff; border: 1.5px solid #111; color: #111; padding: 8px 12px; margin-bottom: 8px; }}
    .header-banner h1 {{ color: #111; font-size: 1rem; }}
    .header-banner p {{ color: #333; font-size: 0.75rem; }}
    .grid {{ grid-template-columns: 1fr 1fr; gap: 6px; }}
    .card {{ background: #fff; border: 1px solid #999; padding: 6px 8px; }}
    .card.ped {{ border-left: 3px solid #1d4ed8; }}
    .card.csl {{ border-left: 3px solid #b45309; }}
    .card-head {{ border-bottom: 1px solid #ddd; margin-bottom: 4px; padding-bottom: 3px; }}
    .card-title {{ color: #000; font-size: 0.78rem; }}
    .ans-line {{ color: #111; font-size: 0.74rem; line-height: 1.38; }}
    .ln-no {{ background: #eee; color: #333; width: 15px; height: 15px; line-height: 15px; font-size: 0.65rem; }}
    .num-badge {{ background: #eee; color: #000; border-color: #999; }}
    .part-badge.ped {{ background: #dbeafe; color: #1e40af; }}
    .part-badge.csl {{ background: #fef3c7; color: #92400e; }}
    .trap-badge {{ background: #ffe4e6; color: #9f1239; border-color: #f43f5e; }}
    .kw {{ color: #1e3a8a !important; background: #fef08a !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  }}
</style>
</head>
<body>

<div class="toolbar">
  <div class="btn-group">
    <button class="btn active" onclick="filterCards('ALL', this)">📚 전체 (55제)</button>
    <button class="btn" onclick="filterCards('PED10', this)">📘 교육학 10선 (6줄)</button>
    <button class="btn" onclick="filterCards('COUNSEL45', this)">📗 전공 45선 (4줄)</button>
    <button class="btn" onclick="filterCards('TRAP', this)">🚨 오답주의 ({len(TRAP_IDS)}선)</button>
  </div>
  <div class="btn-group">
    <button class="btn rose" id="btn-kw" onclick="toggleKw()">🙈 키워드 가리기</button>
    <button class="btn sky" onclick="window.print()">🖨️ A4 인쇄</button>
    <a class="btn" href="master55.html">⌨️ 55제 타이핑</a>
    <a class="btn" href="index.html">📝 AB 시험지</a>
  </div>
</div>

<div class="header-banner">
  <div>
    <h1>🏆 2027학년도(11.28) KICE 핵심키워드 55제 공식 4줄(교육학 6줄) 요약 답안지</h1>
    <p>수험자: 변귀섭 대표님 | 택시·시험장 직전 3분 컷 초압축 암기 & A4 인쇄 전용 (키워드 가리기 후 클릭 시 1초 확인)</p>
  </div>
</div>

<main class="grid" id="card-grid">
  {''.join(cards_html)}
</main>

<script>
function filterCards(mode, btn) {{
  document.querySelectorAll('.toolbar .btn-group:first-child .btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.card').forEach(c => {{
    let show = true;
    if (mode === 'PED10') show = c.dataset.part === 'PED10';
    else if (mode === 'COUNSEL45') show = c.dataset.part === 'COUNSEL45';
    else if (mode === 'TRAP') show = c.dataset.trap === '1';
    c.style.display = show ? 'block' : 'none';
  }});
}}
function toggleKw() {{
  const on = document.body.classList.toggle('hide-kw');
  document.querySelectorAll('.kw.revealed').forEach(k => k.classList.remove('revealed'));
  document.getElementById('btn-kw').textContent = on ? '👀 키워드 모두 보기' : '🙈 키워드 가리기';
}}
document.addEventListener('click', e => {{
  if (document.body.classList.contains('hide-kw') && e.target.classList.contains('kw')) {{
    e.target.classList.toggle('revealed');
  }}
}});
</script>
</body>
</html>
'''

open('sheet55.html', 'w', encoding='utf-8').write(page)
shutil.copyfile('sheet55.html', '../sheet55.html')
print('Generated sheet55.html and ../sheet55.html cleanly! bytes:', len(page.encode('utf-8')))
