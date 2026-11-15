import json, re, subprocess, os, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/final_200_verb_enriched.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

page_titles = [
    "1교시 교육학 핵심 10선 [Part 1: 교육과정 설계 모형] (위긴스·맥타이, 스킬벡, 타바, 워커, 아이즈너)",
    "1교시 교육학 핵심 10선 [Part 2: 교육과정 조직 및 교수학습] (메타인지, 융합, 나선형, 쿠레레, 라이겔루스, 가네, 플립드러닝, 켈러)",
    "1교시 교육학 핵심 10선 [Part 3: 교육평가 및 교육행정·교사론] (변혁적 학습, 성장참조평가, 역동적 평가, 루브릭, 도덕적 리더십, 분산적 리더십, 임상장학, 동료장학, 겟젤스-구바, 자기결정성)",
    "2교시 전공 A형 [진로상담 핵심 10선 ①] - 홀랜드 성격이론 5대 가정 & 수퍼 생애 진로발달 5단계 & 갓프레드슨",
    "2교시 전공 A형 [진로상담 핵심 10선 ②] - SCCT 3대 인지변인, 진로장벽, 사비카스 진로적응도 4C, 크롬볼츠 우연기술",
    "2교시 전공 A형 [심리검사 핵심 10선 ①] - MMPI-2-RF 타당도 척도 전수 (VRIN-r, TRIN-r, F-r, Fp-r, L-r, K-r, Fs, FBS-r) & RCd, RC1",
    "2교시 전공 A형 [심리검사 핵심 10선 ②] - MMPI-2-RF 재구성 임상 척도 & 외현적 위기척도 (SUI, BXD, THD)",
    "2교시 전공 A형 [심리검사 ③ & 집단상담] - K-WISC-V 5대 지표 & 집단상담 얄롬 치료적 요인 및 집단상담 기법",
    "2교시 전공 A형 [대인관계 및 성격심리] - 조하리의 창 4영역, 설리반 자아상, 머레이 압착, 만족지연, 빅파이브 5대 특질",
    "2교시 전공 A형 [분석심리 및 개인심리학] - 융 원형 (페르소나, 그림자, 아니마, 자기), 아들러 생활양식 및 주요 상담기법",
    "2교시 전공 A형 [인지행동치료 (CBT & REBT)] - 벡 인지삼제, 하향화살표, 행동실험 & 엘리스 3대 당위 및 3대 논박",
    "3교시 전공 B형 [게슈탈트, 실존, 현실, ACT] - 접촉경계혼란, 역설적 의도, 탈숙고, WDEP, 인지적 탈융합, 심리적 유연성",
    "3교시 전공 B형 [가족치료 핵심 10선 ①] - 보웬 다세대 가족치료 8대 핵심 개념 (자기분화, 삼각관계, 투사, 가계도, 탈삼각화)",
    "3교시 전공 B형 [가족치료 핵심 10선 ②] - 미누친 구조적 경계선, 실연, 균형깨기 & 사티어 의사소통, 빙산, 가족조각 & 전략적 가족치료",
    "3교시 전공 B형 [이상심리 DSM-5-TR ①] - 강박장애, 자폐스펙트럼, 신체증상, 질병불안, 공황장애, 광장공포, 기분조절부전, 주요우울",
    "3교시 전공 B형 [이상심리 DSM-5-TR ②] - 양극성 장애 1형·2형, 반응성 애착장애, 탈억제 사회관여, 반항장애, 품행장애, PTSD, 급성스트레스",
    "3교시 전공 B형 [성격장애 10종 & 기타 임상] - A·B·C군 성격장애 (경계선, 자기애성 등), 섭식장애 (거식·폭식), 신체변형, 조현병 음성증상",
    "3교시 전공 B형 [행동수정 & 특수아상담] - 차별강화 (DRI, DRA, DRO), 체계적 둔감법, 홍수법, 토큰경제, 행동조성, 자기교시, SIT",
    "3교시 전공 B형 [위기상담, 놀이치료, 다문화] - SLAP, CASE, 안전계획서, ACT 제한설정, 훈습, 수 다문화 역량, 미세공격",
    "3교시 전공 B형 [수퍼비전, 윤리, 학교폭력예방법] - 버나드 판별모델, 다중관계, 사전동의, 아동학대 신고, 학폭법 16조·17조 조치, 전담기구"
]

html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2027 KICE 교육학·전문상담 핵심 200제 동사형 암기노트 (안티그래비티 다크모드)</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 5mm 6mm 5mm 6mm;
    }
    html, body, div, table, thead, tbody, tr, th, td, p, h1, h2, span, button {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", "Noto Sans KR", sans-serif;
      background: #090a0f;
      color: #f3f4f6;
      line-height: 1.25;
      padding: 6px;
      -webkit-font-smoothing: antialiased;
    }
    .no-print-bar {
      max-width: 980px;
      margin: 0 auto 12px auto;
      background: #14161f;
      border: 1px solid #2d313f;
      color: #ffffff;
      padding: 12px 18px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 18px rgba(0,0,0,0.6);
    }
    .btn-group {
      display: flex;
      gap: 10px;
    }
    .btn-print {
      background: #2563eb;
      color: #ffffff;
      border: 1px solid #3b82f6;
      padding: 7px 16px;
      border-radius: 6px;
      font-size: 0.90rem;
      font-weight: 800;
      cursor: pointer;
      transition: background 0.15s ease;
    }
    .btn-print:hover {
      background: #1d4ed8;
    }
    .btn-theme {
      background: #27272a;
      color: #e4e4e7;
      border: 1px solid #3f3f46;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
    }
    .btn-theme:hover {
      background: #3f3f46;
    }
    .page-sheet {
      width: 100%;
      max-width: 960px;
      height: 285mm;
      max-height: 285mm;
      margin: 0 auto 16px auto;
      background: #0e0f15;
      padding: 7px 10px;
      border: 2px solid #2d313f;
      border-radius: 0px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      page-break-inside: avoid;
      page-break-after: always;
      break-after: page;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }
    .page-header {
      border-bottom: 2px solid #2d313f;
      padding-bottom: 3px;
      margin-bottom: 3px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .page-title-main {
      font-size: 1.02rem;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.3px;
    }
    .page-sub-title {
      font-size: 0.79rem;
      color: #38bdf8;
      font-weight: 800;
      margin-top: 1px;
    }
    .page-meta {
      font-size: 0.72rem;
      color: #9ca3af;
      font-weight: 700;
      text-align: right;
    }
    .table-container {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    table {
      width: 100%;
      height: 100%;
      border-collapse: collapse;
      font-size: 0.79rem;
      table-layout: fixed;
    }
    th {
      background: #181a24;
      border: 1.5px solid #2d313f;
      padding: 3px 4px;
      font-weight: 900;
      color: #ffffff;
      text-align: center;
      font-size: 0.78rem;
    }
    td {
      border: 1px solid #232634;
      padding: 3px 5px;
      vertical-align: middle;
      line-height: 1.25;
      word-break: keep-all;
      overflow-wrap: break-word;
      color: #f3f4f6;
    }
    tr:nth-child(even) td {
      background: #13141d;
    }
    tr:nth-child(odd) td {
      background: #0e0f15;
    }
    .td-num {
      text-align: center;
      font-weight: 600;
      color: #9ca3af;
      width: 4%;
      font-size: 0.80rem;
    }
    .td-q {
      width: 32%;
      color: #d1d5db;
      font-size: 0.78rem;
      font-weight: 400;
      line-height: 1.25;
    }
    .td-kw {
      width: 23%;
    }
    .kw-badge {
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 800;
      color: #38bdf8;
      background: #0f2438;
      border: 1px solid #0284c7;
      padding: 0px 4px;
      border-radius: 2px;
      margin-bottom: 2px;
    }
    .kw-name {
      font-weight: 800;
      color: #ffffff;
      font-size: 0.83rem;
      line-height: 1.2;
    }
    .kw-verb {
      font-weight: 800;
      color: #fde047;
      font-size: 0.77rem;
      line-height: 1.22;
      margin-top: 2.5px;
      padding-top: 2px;
      border-top: 1px dashed #3f4458;
    }
    .verb-tag {
      display: inline-block;
      background: #38bdf8;
      color: #000000;
      font-size: 0.62rem;
      font-weight: 900;
      padding: 0px 3px;
      border-radius: 2px;
      margin-right: 2px;
      vertical-align: 1px;
    }
    .td-ans {
      width: 34%;
      color: #e5e7eb;
    }
    .ans-box {
      font-weight: 400;
      color: #e5e7eb;
      font-size: 0.78rem;
      line-height: 1.27;
    }
    .td-write {
      width: 7%;
      text-align: center;
      vertical-align: middle;
    }
    .chk-box {
      display: inline-block;
      width: 13px;
      height: 13px;
      border: 1.5px solid #6b7280;
      border-radius: 1px;
      margin-bottom: 2px;
      background: #181a24;
    }
    .write-guide {
      font-size: 0.64rem;
      color: #9ca3af;
      font-weight: 400;
      display: block;
    }

    body.light-theme {
      background: #f8fafc !important;
      color: #000000 !important;
    }
    body.light-theme .page-sheet {
      background: #ffffff !important;
      border: 2px solid #000000 !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }
    body.light-theme .page-header {
      border-bottom: 2px solid #000000 !important;
    }
    body.light-theme .page-title-main {
      color: #000000 !important;
    }
    body.light-theme .page-sub-title {
      color: #111111 !important;
    }
    body.light-theme .page-meta {
      color: #000000 !important;
    }
    body.light-theme th {
      background: #e5e5e5 !important;
      color: #000000 !important;
      border: 1.5px solid #000000 !important;
    }
    body.light-theme td {
      border: 1px solid #222222 !important;
      color: #000000 !important;
    }
    body.light-theme tr:nth-child(even) td {
      background: #f7f7f7 !important;
    }
    body.light-theme tr:nth-child(odd) td {
      background: #ffffff !important;
    }
    body.light-theme .td-num {
      color: #222222 !important;
    }
    body.light-theme .td-q {
      color: #111111 !important;
    }
    body.light-theme .kw-badge {
      background: #ffffff !important;
      color: #000000 !important;
      border: 1px solid #000000 !important;
    }
    body.light-theme .kw-name {
      color: #000000 !important;
    }
    body.light-theme .kw-verb {
      color: #000000 !important;
      border-top: 1px dashed #555555 !important;
    }
    body.light-theme .verb-tag {
      background: #000000 !important;
      color: #ffffff !important;
    }
    body.light-theme .ans-box {
      color: #111111 !important;
    }
    body.light-theme .chk-box {
      border: 1.5px solid #000000 !important;
      background: #ffffff !important;
    }
    body.light-theme .write-guide {
      color: #444444 !important;
    }

    @media print {
      body {
        background: #000000 !important;
        padding: 0 !important;
        color: #ffffff !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .no-print-bar {
        display: none !important;
      }
      .page-sheet {
        border: 2px solid #333333 !important;
        background: #000000 !important;
        box-shadow: none !important;
        padding: 6px 8px !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 285mm !important;
        max-height: 285mm !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      tr:nth-child(even) td {
        background: #111115 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      tr:nth-child(odd) td {
        background: #050508 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      th {
        background: #1c1d24 !important;
        color: #ffffff !important;
        border: 1.5px solid #333333 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      td {
        border: 1px solid #282a36 !important;
        color: #f3f4f6 !important;
      }
      .kw-badge {
        background: #0f2438 !important;
        color: #38bdf8 !important;
        border: 1px solid #0284c7 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .verb-tag {
        background: #38bdf8 !important;
        color: #000000 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .kw-verb {
        color: #fde047 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .chk-box {
        border: 1.5px solid #6b7280 !important;
        background: #181a24 !important;
      }
    }
  </style>
  <script>
    function toggleTheme() {
      document.body.classList.toggle('light-theme');
      var btn = document.getElementById('themeBtn');
      if (document.body.classList.contains('light-theme')) {
        btn.innerText = '🌙 안티그래비티 다크모드로 전환';
      } else {
        btn.innerText = '☀️ 화이트 모드로 전환 (인쇄용)';
      }
    }
  </script>
</head>
<body>

  <div class="no-print-bar">
    <div>
      <h2 style="font-size: 1.1rem; margin-bottom: 3px;">🌌 2027 KICE 교육학·전문상담 핵심 200제 암기노트 (안티그래비티 다크모드)</h2>
      <p style="font-size: 0.8rem; color: #94a3b8;">눈이 편안한 OLED 다크 테마 | 동사형 핵심키워드(굵게) + 4점 만점 모범답안 | 1장당 10문항 · 총 20장</p>
    </div>
    <div class="btn-group">
      <button id="themeBtn" class="btn-theme" onclick="toggleTheme()">☀️ 화이트 모드로 전환 (인쇄용)</button>
      <button class="btn-print" onclick="window.print()">🖨️ A4 20장 PDF 저장 / 인쇄</button>
    </div>
  </div>
""")

for page_idx in range(20):
    p_num = page_idx + 1
    p_title = page_titles[page_idx]
    page_items = items[page_idx * 10 : (page_idx + 1) * 10]

    html_parts.append(f"""
  <!-- Page {p_num} / 20 -->
  <div class="page-sheet">
    <div class="page-header">
      <div>
        <div class="page-title-main">🌌 2027 교육학·전문상담 임용고시 핵심 200제 암기노트 [ {p_num} / 20 ]</div>
        <div class="page-sub-title">{p_title}</div>
      </div>
      <div class="page-meta">
        <div>성명: _________ &nbsp; 날짜: 2026. __. __.</div>
        <div style="font-size: 0.68rem; color: #9ca3af; margin-top: 1px;">KICE 만점 공인 동사형 술어 & 38-45자 서술문 기준</div>
      </div>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width: 4%;">No.</th>
            <th style="width: 32%;">❓ KICE 실전 힌트 박멸 문제 (단서)</th>
            <th style="width: 23%;">영역 및 동사형 핵심 표제어</th>
            <th style="width: 34%;">🏆 KICE 4점 만점 공식 서술 정답</th>
            <th style="width: 7%;">암기</th>
          </tr>
        </thead>
        <tbody>
""")

    for it in page_items:
        html_parts.append(f"""
          <tr>
            <td class="td-num">{it['num']}</td>
            <td class="td-q">{it['q']}</td>
            <td class="td-kw">
              <span class="kw-badge">{it['badge']}</span>
              <div class="kw-name">{it['kw']}</div>
              <div class="kw-verb"><span class="verb-tag">서술동사</span>{it['verb_kw']}</div>
            </td>
            <td class="td-ans">
              <div class="ans-box">{it['ans']}</div>
            </td>
            <td class="td-write">
              <span class="chk-box"></span>
              <span class="write-guide">암기완료</span>
            </td>
          </tr>
""")

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

# Verify zero asterisks in generated HTML
star_count = full_html.count('*')
assert star_count == 0, f"Asterisks found ({star_count}) in generated 200 HTML!"

output_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_200_core_table_a4.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

workspace_path = 'kice_200_core_table_a4.html'
with open(workspace_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Saved kice_200_core_table_a4.html with Antigravity Dark Mode successfully!')
