import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def extract_model_answer(ans_str):
    if not ans_str:
        return ''
    pos_trophy = ans_str.find('🏆 [KICE 4점 만점 서술문]')
    if pos_trophy != -1:
        part = ans_str[pos_trophy + len('🏆 [KICE 4점 만점 서술문]'):].strip()
        pos_next = part.find('🔍')
        if pos_next != -1:
            part = part[:pos_next].strip()
        return part
    lines = ans_str.strip().split('\n')
    return lines[0].strip()

def clean_no_stars(s):
    if not s:
        return ''
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    s = s.replace('*', '')
    return s.strip()

# Build HTML content without any universal selector *
html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2027 KICE 전문상담 핵심 150제 A4 10장 암기노트 (ADHD 고대조 쓰기노트)</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 10mm 12mm 10mm;
    }
    html, body, div, table, thead, tbody, tr, th, td, p, h1, h2, span, button {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif;
      background: #f1f5f9;
      color: #0f172a;
      line-height: 1.4;
      padding: 20px;
    }
    .no-print-bar {
      max-width: 1000px;
      margin: 0 auto 20px auto;
      background: #0f172a;
      color: #fff;
      padding: 14px 20px;
      border-radius: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    }
    .btn-print {
      background: #0284c7;
      color: #fff;
      border: 1px solid #38bdf8;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 800;
      cursor: pointer;
    }
    .btn-print:hover {
      background: #0369a1;
    }
    .page-sheet {
      width: 100%;
      max-width: 960px;
      margin: 0 auto 25px auto;
      background: #ffffff;
      padding: 22px 26px;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
      page-break-after: always;
      break-after: page;
    }
    .page-header {
      border-bottom: 2px solid #0f172a;
      padding-bottom: 8px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .page-title-main {
      font-size: 1.15rem;
      font-weight: 900;
      color: #0f172a;
    }
    .page-sub-title {
      font-size: 0.88rem;
      color: #475569;
      font-weight: 600;
      margin-top: 2px;
    }
    .page-meta {
      font-size: 0.82rem;
      color: #334155;
      text-align: right;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.81rem;
    }
    th {
      background: #f1f5f9;
      border: 1px solid #94a3b8;
      padding: 6px 8px;
      font-weight: 800;
      color: #0f172a;
      text-align: center;
    }
    td {
      border: 1px solid #cbd5e1;
      padding: 6px 8px;
      vertical-align: top;
      line-height: 1.45;
    }
    tr:nth-child(even) {
      background: #f8fafc;
    }
    .td-num {
      text-align: center;
      font-weight: 900;
      color: #0284c7;
      width: 5%;
    }
    .td-kw {
      width: 18%;
    }
    .kw-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      color: #1e3a8a;
      background: #dbeafe;
      padding: 1px 5px;
      border-radius: 4px;
      margin-bottom: 2px;
    }
    .kw-name {
      font-weight: 800;
      color: #0f172a;
      font-size: 0.84rem;
    }
    .td-q {
      width: 32%;
      color: #334155;
    }
    .td-ans {
      width: 35%;
      color: #0f172a;
    }
    .ans-box {
      font-weight: 600;
      color: #0f172a;
    }
    .td-write {
      width: 10%;
      text-align: center;
    }
    .write-line {
      display: block;
      border-bottom: 1px dashed #94a3b8;
      margin-top: 14px;
      height: 12px;
    }
    @media print {
      body {
        background: #fff !important;
        padding: 0 !important;
      }
      .no-print-bar {
        display: none !important;
      }
      .page-sheet {
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }
      tr:nth-child(even) {
        background: #f9f9f9 !important;
      }
    }
  </style>
</head>
<body>

  <div class="no-print-bar">
    <div>
      <h2 style="font-size: 1.15rem; margin-bottom: 4px;">🟡 2027 KICE 전문상담 핵심 150제 A4 10장 암기노트</h2>
      <p style="font-size: 0.85rem; color: #94a3b8;">ADHD 맞춤형 고대조 10페이지 조판 · 1페이지당 15문항 정밀 배치 (인쇄 시 정확히 10장 출력)</p>
    </div>
    <button class="btn-print" onclick="window.print()">🖨️ A4 10장 바로 인쇄 / PDF 저장</button>
  </div>
""")

global_counter = 1

for page in pages:
    p_num = page['pageNum']
    p_title = page['pageTitle']
    items = page['items']

    html_parts.append(f"""
  <!-- Page {p_num} / 10 -->
  <div class="page-sheet">
    <div class="page-header">
      <div>
        <div class="page-title-main">🏛️ 2027 전문상담 임용고시 핵심 150제 암기노트 [ {p_num} / 10 ]</div>
        <div class="page-sub-title">{p_title}</div>
      </div>
      <div class="page-meta">
        <div>수험번호: _________________ &nbsp; 성명: _________</div>
        <div style="font-size: 0.75rem; color: #64748b; margin-top: 2px;">KICE 만점 공인 표제어 & 서술문 기준</div>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th>영역 및 핵심 표제어</th>
          <th>❓ KICE 실전 힌트 박멸 문제 (단서)</th>
          <th>🏆 KICE 4점 만점 공식 서술 정답</th>
          <th>✍️ 인출체크</th>
        </tr>
      </thead>
      <tbody>
""")

    for it in items:
        clean_kw = clean_no_stars(it['keywords'])
        clean_q = clean_no_stars(it['question'])
        clean_a = clean_no_stars(extract_model_answer(it['answer']))

        html_parts.append(f"""
        <tr>
          <td class="td-num">{global_counter}</td>
          <td class="td-kw">
            <span class="kw-badge">{it['domain']}</span>
            <div class="kw-name">{clean_kw}</div>
          </td>
          <td class="td-q">{clean_q}</td>
          <td class="td-ans">
            <div class="ans-box">{clean_a}</div>
          </td>
          <td class="td-write">
            <span style="font-size: 0.75rem; color: #64748b;">[ ] 완벽</span>
            <span class="write-line"></span>
          </td>
        </tr>
""")
        global_counter += 1

    html_parts.append("""
      </tbody>
    </table>
  </div>
""")

html_parts.append("""
</body>
</html>
""")

full_html = "".join(html_parts)

# Verify zero asterisks in generated HTML
star_count = full_html.count('*')
print('Asterisks count in generated HTML:', star_count)
assert star_count == 0, f"Asterisks found ({star_count}) in generated 150 HTML!"

output_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/kice_150_core_table_a4.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Generated kice_150_core_table_a4.html successfully! Size:', len(full_html))
