import sys, json, re, subprocess, os
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
    s = s.replace('~', '-')
    return s.strip()

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
output_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/kice_150_core_table_a4.html'
pdf_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/kice_150_core_table_a4.pdf'

def test_config(font_base, td_q_size, ans_size, kw_size, pad_y):
    html_parts = []
    html_parts.append(f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2027 KICE 전문상담 핵심 150제 A4 10장 암기노트 (가독성 확대판)</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 4.5mm 6mm 4.5mm 6mm;
    }}
    html, body, div, table, thead, tbody, tr, th, td, p, h1, h2, span, button {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", "Noto Sans KR", sans-serif;
      background: #f8fafc;
      color: #000000;
      line-height: 1.22;
      padding: 6px;
      -webkit-font-smoothing: antialiased;
    }}
    .no-print-bar {{
      max-width: 980px;
      margin: 0 auto 12px auto;
      background: #000000;
      color: #ffffff;
      padding: 10px 16px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    }}
    .btn-print {{
      background: #2563eb;
      color: #ffffff;
      border: 1px solid #60a5fa;
      padding: 7px 16px;
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 800;
      cursor: pointer;
    }}
    .btn-print:hover {{
      background: #1d4ed8;
    }}
    .page-sheet {{
      width: 100%;
      max-width: 960px;
      height: 287mm;
      max-height: 287mm;
      margin: 0 auto 16px auto;
      background: #ffffff;
      padding: 8px 10px;
      border: 2px solid #000000;
      border-radius: 0px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      page-break-inside: avoid;
      page-break-after: always;
      break-after: page;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }}
    .page-header {{
      border-bottom: 2px solid #000000;
      padding-bottom: 3px;
      margin-bottom: 3px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    .page-title-main {{
      font-size: 1.05rem;
      font-weight: 900;
      color: #000000;
      letter-spacing: -0.3px;
    }}
    .page-sub-title {{
      font-size: 0.82rem;
      color: #111111;
      font-weight: 800;
      margin-top: 1px;
    }}
    .page-meta {{
      font-size: 0.74rem;
      color: #000000;
      font-weight: 700;
      text-align: right;
    }}
    .table-container {{
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    table {{
      width: 100%;
      height: 100%;
      border-collapse: collapse;
      font-size: {font_base};
      table-layout: fixed;
    }}
    th {{
      background: #e5e5e5;
      border: 1.5px solid #000000;
      padding: 3px 3px;
      font-weight: 900;
      color: #000000;
      text-align: center;
      font-size: 0.78rem;
    }}
    td {{
      border: 1px solid #222222;
      padding: {pad_y} 4px;
      vertical-align: middle;
      line-height: 1.22;
      word-break: keep-all;
      overflow-wrap: break-word;
      color: #000000;
    }}
    tr:nth-child(even) td {{
      background: #f5f5f5;
    }}
    .td-num {{
      text-align: center;
      font-weight: 900;
      color: #000000;
      width: 4.5%;
      font-size: 0.82rem;
    }}
    .td-q {{
      width: 34%;
      color: #111111;
      font-size: {td_q_size};
      font-weight: 600;
    }}
    .td-kw {{
      width: 18.5%;
    }}
    .kw-badge {{
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 800;
      color: #000000;
      background: #ffffff;
      border: 1px solid #000000;
      padding: 0px 4px;
      border-radius: 2px;
      margin-bottom: 2px;
    }}
    .kw-name {{
      font-weight: 900;
      color: #000000;
      font-size: {kw_size};
      line-height: 1.2;
    }}
    .td-ans {{
      width: 35%;
      color: #000000;
    }}
    .ans-box {{
      font-weight: 800;
      color: #000000;
      font-size: {ans_size};
      line-height: 1.23;
    }}
    .td-write {{
      width: 8%;
      text-align: center;
      vertical-align: middle;
    }}
    .chk-box {{
      display: inline-block;
      width: 13px;
      height: 13px;
      border: 1.5px solid #000000;
      border-radius: 1px;
      margin-bottom: 2px;
      background: #ffffff;
    }}
    .write-guide {{
      font-size: 0.64rem;
      color: #000000;
      font-weight: 800;
      display: block;
    }}
    @media print {{
      body {{
        background: #ffffff !important;
        padding: 0 !important;
        color: #000000 !important;
      }}
      .no-print-bar {{
        display: none !important;
      }}
      .page-sheet {{
        border: 2px solid #000000 !important;
        box-shadow: none !important;
        padding: 6px 8px !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 287mm !important;
        max-height: 287mm !important;
      }}
      tr:nth-child(even) td {{
        background: #f5f5f5 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
      th {{
        background: #e5e5e5 !important;
        color: #000000 !important;
        border: 1.5px solid #000000 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
      td {{
        border: 1px solid #000000 !important;
        color: #000000 !important;
      }}
      .kw-badge {{
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
      }}
      .chk-box {{
        border: 1.5px solid #000000 !important;
      }}
    }}
  </style>
</head>
<body>

  <div class="no-print-bar">
    <div>
      <h2 style="font-size: 1.1rem; margin-bottom: 3px;">📖 2027 KICE 전문상담 핵심 150제 A4 10장 암기노트 (가독성 극대화판)</h2>
      <p style="font-size: 0.8rem; color: #d1d5db;">글씨 크기 확대 · 고대조 흑백 인쇄 최적화 (1페이지당 15문항 · 정확히 A4 10장)</p>
    </div>
    <button class="btn-print" onclick="window.print()">🖨️ A4 10장 흑백 인쇄 / PDF 저장</button>
  </div>
""")

    global_counter = 1
    for page in pages:
        p_num = page['pageNum']
        p_title = clean_no_stars(page['pageTitle'])
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
        <div>성명: _________ &nbsp; 날짜: 2026. __. __.</div>
        <div style="font-size: 0.68rem; color: #000000; margin-top: 1px;">KICE 만점 공인 표제어 & 38-45자 서술문 기준</div>
      </div>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width: 4.5%;">No.</th>
            <th style="width: 34%;">❓ KICE 실전 힌트 박멸 문제 (단서)</th>
            <th style="width: 18.5%;">영역 및 핵심 표제어</th>
            <th style="width: 35%;">🏆 KICE 4점 만점 공식 서술 정답</th>
            <th style="width: 8%;">암기</th>
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
            <td class="td-q">{clean_q}</td>
            <td class="td-kw">
              <span class="kw-badge">{clean_no_stars(it['domain'])}</span>
              <div class="kw-name">{clean_kw}</div>
            </td>
            <td class="td-ans">
              <div class="ans-box">{clean_a}</div>
            </td>
            <td class="td-write">
              <span class="chk-box"></span>
              <span class="write-guide">암기완료</span>
            </td>
          </tr>
""")
            global_counter += 1

        html_parts.append("""
        </tbody>
      </table>
    </div>
  </div>
""")

    html_parts.append("""
</body>
</html>
""")

    full_html = "".join(html_parts)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    cmd = [
        chrome,
        '--headless',
        '--disable-gpu',
        f'--print-to-pdf={pdf_path}',
        '--no-pdf-header-footer',
        output_path
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=25)
    with open(pdf_path, 'rb') as f:
        content = f.read()
    cnt = len(re.findall(b'/Type\\s*/Page[^s]', content))
    return cnt

# Test configurations
configs = [
    ('0.77rem', '0.76rem', '0.77rem', '0.80rem', '2px'),
    ('0.76rem', '0.75rem', '0.76rem', '0.79rem', '2px'),
    ('0.75rem', '0.74rem', '0.75rem', '0.78rem', '2.5px'),
]

for cfg in configs:
    cnt = test_config(*cfg)
    print(f'Config {cfg} -> PDF Pages: {cnt}')
    if cnt == 10:
        print('SUCCESS! Found optimal largest font configuration that fits EXACTLY 10 pages!')
        break
