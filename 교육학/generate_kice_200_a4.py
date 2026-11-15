import json, re, subprocess, os, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/final_200_cleaned.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Loaded {len(items)} items.")

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
  <title>2027 KICE 교육학·전문상담 핵심 200제 A4 암기노트 (1장당 10문항 · 총 20장)</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 6mm 7mm 6mm 7mm;
    }
    html, body, div, table, thead, tbody, tr, th, td, p, h1, h2, span, button {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", "Noto Sans KR", sans-serif;
      background: #f8fafc;
      color: #000000;
      line-height: 1.28;
      padding: 8px;
      -webkit-font-smoothing: antialiased;
    }
    .no-print-bar {
      max-width: 980px;
      margin: 0 auto 14px auto;
      background: #000000;
      color: #ffffff;
      padding: 12px 18px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    }
    .btn-print {
      background: #2563eb;
      color: #ffffff;
      border: 1px solid #60a5fa;
      padding: 8px 18px;
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 800;
      cursor: pointer;
    }
    .btn-print:hover {
      background: #1d4ed8;
    }
    .page-sheet {
      width: 100%;
      max-width: 960px;
      height: 284mm;
      max-height: 284mm;
      margin: 0 auto 18px auto;
      background: #ffffff;
      padding: 9px 12px;
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
    }
    .page-header {
      border-bottom: 2px solid #000000;
      padding-bottom: 4px;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .page-title-main {
      font-size: 1.05rem;
      font-weight: 900;
      color: #000000;
      letter-spacing: -0.3px;
    }
    .page-sub-title {
      font-size: 0.82rem;
      color: #111111;
      font-weight: 800;
      margin-top: 1px;
    }
    .page-meta {
      font-size: 0.74rem;
      color: #000000;
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
      font-size: 0.81rem;
      table-layout: fixed;
    }
    th {
      background: #e5e5e5;
      border: 1.5px solid #000000;
      padding: 4px 4px;
      font-weight: 900;
      color: #000000;
      text-align: center;
      font-size: 0.80rem;
    }
    td {
      border: 1px solid #222222;
      padding: 3.5px 6px;
      vertical-align: middle;
      line-height: 1.28;
      word-break: keep-all;
      overflow-wrap: break-word;
      color: #000000;
    }
    tr:nth-child(even) td {
      background: #f7f7f7;
    }
    .td-num {
      text-align: center;
      font-weight: 600;
      color: #222222;
      width: 4.5%;
      font-size: 0.82rem;
    }
    .td-q {
      width: 34%;
      color: #111111;
      font-size: 0.80rem;
      font-weight: 400;
      line-height: 1.28;
    }
    .td-kw {
      width: 18.5%;
    }
    .kw-badge {
      display: inline-block;
      font-size: 0.68rem;
      font-weight: 800;
      color: #000000;
      background: #ffffff;
      border: 1px solid #000000;
      padding: 0px 4px;
      border-radius: 2px;
      margin-bottom: 2px;
    }
    .kw-name {
      font-weight: 800;
      color: #000000;
      font-size: 0.86rem;
      line-height: 1.24;
    }
    .td-ans {
      width: 35%;
      color: #111111;
    }
    .ans-box {
      font-weight: 400;
      color: #111111;
      font-size: 0.81rem;
      line-height: 1.30;
    }
    .td-write {
      width: 8%;
      text-align: center;
      vertical-align: middle;
    }
    .chk-box {
      display: inline-block;
      width: 14px;
      height: 14px;
      border: 1.5px solid #000000;
      border-radius: 1px;
      margin-bottom: 2px;
      background: #ffffff;
    }
    .write-guide {
      font-size: 0.66rem;
      color: #444444;
      font-weight: 400;
      display: block;
    }
    @media print {
      body {
        background: #ffffff !important;
        padding: 0 !important;
        color: #000000 !important;
      }
      .no-print-bar {
        display: none !important;
      }
      .page-sheet {
        border: 2px solid #000000 !important;
        box-shadow: none !important;
        padding: 8px 10px !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 284mm !important;
        max-height: 284mm !important;
      }
      tr:nth-child(even) td {
        background: #f7f7f7 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      th {
        background: #e5e5e5 !important;
        color: #000000 !important;
        border: 1.5px solid #000000 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      td {
        border: 1px solid #000000 !important;
        color: #000000 !important;
      }
      .kw-badge {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
      }
      .chk-box {
        border: 1.5px solid #000000 !important;
      }
    }
  </style>
</head>
<body>

  <div class="no-print-bar">
    <div>
      <h2 style="font-size: 1.1rem; margin-bottom: 3px;">📖 2027 KICE 교육학·전문상담 핵심 200제 암기노트 (1장당 10문항 · 총 20장)</h2>
      <p style="font-size: 0.8rem; color: #d1d5db;">교육학 30제 + 전공상담 170제 | 1장당 10개씩 글씨 확대 인쇄 | 2열 표제어만 굵게 강조</p>
    </div>
    <button class="btn-print" onclick="window.print()">🖨️ A4 20장 흑백 인쇄 / PDF 저장</button>
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
        <div class="page-title-main">🏛️ 2027 교육학·전문상담 임용고시 핵심 200제 암기노트 [ {p_num} / 20 ]</div>
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

    for it in page_items:
        html_parts.append(f"""
          <tr>
            <td class="td-num">{it['num']}</td>
            <td class="td-q">{it['q']}</td>
            <td class="td-kw">
              <span class="kw-badge">{it['badge']}</span>
              <div class="kw-name">{it['kw']}</div>
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

print('Saved kice_200_core_table_a4.html successfully!')
