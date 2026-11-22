# -*- coding: utf-8 -*-
import json
import os
import re

# Load real 2020-2026 PDF analysis data extracted from G:\내 드라이브\2. 전문상담
ANALYSIS_PATH = r"C:\Users\LENOVO\.gemini\antigravity\brain\b35672cb-40d5-428e-8945-cbb2b7b662e7\scratch\past_exam_analysis.json"
with open(ANALYSIS_PATH, "r", encoding="utf-8") as f:
    past_analysis = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Safety normalization for KICE official terminology
html = html.replace("자아 동질적", "자아 동조적").replace("자아동질적", "자아동조적")

assert '<nav class="main-tabs">' in html, "main-tabs anchor missing"
assert '<section id="secTop55">' in html, "secTop55 anchor missing"
assert 'const TOP55 =' in html, "TOP55 data missing"

# Prepare Analysis JSON
yearly_chart = []
for yr in sorted(past_analysis["counsel_by_year"].keys()):
    d = past_analysis["counsel_by_year"][yr]
    yearly_chart.append({
        "year": yr,
        "aChars": d["A"]["chars"],
        "bChars": d["B"]["chars"],
        "totalChars": d["A"]["chars"] + d["B"]["chars"],
        "asks": d["A"]["ask_boxes"] + d["B"]["ask_boxes"],
    })

domain_chart = [
    {"name": k, "count": v}
    for k, v in sorted(past_analysis["counsel_domain_totals"].items(), key=lambda x: -x[1])
]

analysis_payload = {
    "yearly": yearly_chart,
    "domains": domain_chart,
    "kw2026": past_analysis["counsel_kw_by_year"]["2026"][:24],
    "kw2025": past_analysis["counsel_kw_by_year"]["2025"][:24],
    "edu2026": past_analysis["edu_by_year"]["2026"]["hits"],
}
ANALYSIS_JSON = json.dumps(analysis_payload, ensure_ascii=False)

# 1. Update title & brand
html = html.replace(
    "<title>2027 임용(11.28) 출제확률순 모바일 합격 마스터</title>",
    "<title>2027 임용(11.28) 전문상담 기출분석 · 55제 · KICE 공식 답안지</title>"
)
html = html.replace(
    '<span class="brand-title">2027 임용 출제확률순 마스터</span>',
    '<span class="brand-title">2027 전문상담 · KICE 답안지</span>'
)

# 2. Inject CSS for 4-tab nav, Analysis Dashboard, and Authentic KICE Official B4 Answer Sheet
EXTRA_CSS = """
  /* 4-tab main navigation */
  .main-tabs { grid-template-columns: repeat(4, 1fr) !important; gap: 5px !important; }
  .main-tab { padding: 8px 3px !important; font-size: 0.76rem !important; line-height: 1.25; }

  /* Analysis Dashboard Styles */
  .an-hero {
    background: linear-gradient(135deg, rgba(2,132,199,0.22), rgba(79,70,229,0.22));
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
  }
  .an-hero h2 { font-size: 1.05rem; font-weight: 900; margin-bottom: 6px; color: var(--text); }
  .an-hero p { font-size: 0.84rem; color: var(--text-muted); line-height: 1.55; }
  .kpi-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-bottom: 12px; }
  @media (min-width: 640px) { .kpi-grid { grid-template-columns: repeat(4, 1fr); } }
  .kpi-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 12px 10px; text-align: center; }
  .kpi-val { font-size: 1.25rem; font-weight: 900; color: var(--accent); line-height: 1.2; }
  .kpi-lbl { font-size: 0.74rem; color: var(--text-muted); margin-top: 4px; font-weight: 700; }
  .an-card { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 14px; margin-bottom: 12px; }
  .an-card h3 { font-size: 0.94rem; font-weight: 900; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between; gap: 6px; }
  .bar-row { display: grid; grid-template-columns: 112px 1fr 56px; align-items: center; gap: 8px; margin-bottom: 7px; font-size: 0.78rem; }
  .bar-row.yr-row { grid-template-columns: 52px 1fr 94px; }
  .bar-lbl { font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .bar-track { height: 12px; background: var(--surface-2); border-radius: 999px; overflow: hidden; border: 1px solid var(--border); }
  .bar-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, #0284c7, #6366f1); }
  .bar-fill.hot { background: linear-gradient(90deg, #f43f5e, #fbbf24); }
  .bar-num { text-align: right; font-weight: 800; color: var(--text-muted); font-size: 0.74rem; }
  .kw-cloud { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 6px; }
  .kw-pill { background: var(--surface-2); border: 1px solid var(--border); border-radius: 999px; padding: 3px 8px; font-size: 0.75rem; font-weight: 700; color: var(--text); }
  .kw-pill.accent { background: rgba(56,189,248,0.16); border-color: var(--accent); color: var(--accent); }
  .top10-item { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 9px 10px; border-radius: 10px; background: var(--surface-2); border: 1px solid var(--border); margin-bottom: 6px; cursor: pointer; transition: border-color 0.15s; }
  .top10-item:hover { border-color: var(--accent); }
  .top10-left { min-width: 0; }
  .top10-title { font-size: 0.84rem; font-weight: 800; color: var(--text); }
  .top10-sub { font-size: 0.73rem; color: var(--text-muted); margin-top: 2px; }
  .top10-go { flex-shrink: 0; background: var(--accent); color: #082f49; font-weight: 900; font-size: 0.74rem; padding: 4px 8px; border-radius: 8px; }
  .strat-grid { display: grid; grid-template-columns: 1fr; gap: 8px; }
  @media (min-width: 640px) { .strat-grid { grid-template-columns: 1fr 1fr; } }
  .strat-box { background: var(--surface-2); border-left: 3px solid var(--gold); border-radius: 8px; padding: 10px; font-size: 0.8rem; line-height: 1.55; }
  .strat-box strong { color: var(--gold); display: block; margin-bottom: 3px; }

  /* ===== AUTHENTIC KICE OFFICIAL B4 ANSWER SHEET ===== */
  .kice-paper {
    background: #ffffff;
    color: #111827;
    border-radius: 8px;
    padding: 14px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.35);
    margin-bottom: 16px;
    font-family: 'Noto Sans KR', sans-serif;
    --kc-main: #d81b60;
    --kc-soft: #fce4ec;
    --kc-dash: #f48fb1;
  }
  .kice-paper.p1 { --kc-main: #008a4b; --kc-soft: #e8f5e9; --kc-dash: #81c784; }
  .kice-paper.p2 { --kc-main: #d81b60; --kc-soft: #fce4ec; --kc-dash: #f48fb1; }
  .kice-paper.p3 { --kc-main: #d84315; --kc-soft: #fbe9e7; --kc-dash: #ffab91; }

  .kice-omr-marks {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 6px;
    padding: 0 20px;
  }
  .kice-omr-marks span {
    display: inline-block;
    width: 6px;
    height: 11px;
    background: #1f2937;
  }
  .kice-frame {
    border: 2px solid var(--kc-main);
    background: #fff;
  }
  .kice-banner {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 8px 10px;
    border-bottom: 1.5px solid var(--kc-main);
    color: var(--kc-main);
    font-weight: 900;
    font-size: 0.96rem;
    flex-wrap: wrap;
    text-align: center;
  }
  .kice-period-pill {
    border: 2px solid var(--kc-main);
    border-radius: 999px;
    padding: 1px 11px;
    font-size: 0.88rem;
    font-weight: 900;
    background: #fff;
  }
  .kice-meta-grid {
    display: grid;
    grid-template-columns: 1.15fr 1.35fr 1.2fr;
    border-bottom: 1.5px solid var(--kc-main);
    font-size: 0.72rem;
    color: var(--kc-main);
  }
  @media (max-width: 600px) {
    .kice-meta-grid { grid-template-columns: 1fr; }
    .kice-meta-col { border-right: none !important; border-bottom: 1px solid var(--kc-dash); }
  }
  .kice-meta-col {
    border-right: 1px solid var(--kc-main);
    display: flex;
    flex-direction: column;
  }
  .kice-meta-col:last-child { border-right: none; }
  .kice-cell-head {
    background: var(--kc-soft);
    text-align: center;
    font-weight: 800;
    padding: 4px 6px;
    border-bottom: 1px solid var(--kc-dash);
  }
  .kice-cell-body {
    padding: 6px 8px;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .kice-input-inline {
    width: 100%;
    border: none;
    border-bottom: 1px dashed var(--kc-dash);
    text-align: center;
    font-size: 0.88rem;
    font-weight: 800;
    color: #111827;
    background: transparent;
    padding: 2px 4px;
    font-family: inherit;
  }
  .kice-input-inline:focus { outline: none; border-bottom-color: var(--kc-main); background: #fefce8; }
  .kice-subject-row {
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    border-top: 1px solid var(--kc-main);
    flex: 1;
  }
  .kice-subject-box {
    background: var(--kc-soft);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 0.85rem;
    padding: 6px;
    border-right: 1px solid var(--kc-main);
  }
  .kice-page-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 4px;
    gap: 3px;
  }
  .kice-omr-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 2px 6px;
    border-bottom: 1px solid var(--kc-soft);
    font-size: 0.66rem;
    letter-spacing: 1px;
  }
  .kice-notice {
    padding: 6px 10px;
    border-bottom: 1.5px solid var(--kc-main);
    color: #dc2626;
    font-size: 0.7rem;
    line-height: 1.5;
    font-weight: 600;
  }

  /* Answer Rows (Authentic KICE Table) */
  .kice-q-row {
    display: grid;
    grid-template-columns: 62px 1fr;
    border-bottom: 1.5px solid var(--kc-main);
  }
  .kice-q-row:last-child { border-bottom: none; }
  .kice-q-num {
    background: var(--kc-soft);
    color: var(--kc-main);
    border-right: 1.5px solid var(--kc-main);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 0.78rem;
    text-align: center;
    padding: 6px 2px;
    line-height: 1.3;
  }
  .kice-lines-wrap {
    display: flex;
    flex-direction: column;
  }
  .kice-line-item {
    display: flex;
    align-items: center;
    border-bottom: 1px dashed var(--kc-dash);
    min-height: 33px;
    padding: 2px 8px;
    gap: 6px;
    background: #fff;
  }
  .kice-line-item:last-child { border-bottom: none; }
  .kice-line-item.solid-5 { border-bottom: 1.5px solid var(--kc-main); }
  .kice-line-idx {
    font-size: 0.68rem;
    color: var(--kc-dash);
    font-weight: 800;
    width: 18px;
    flex-shrink: 0;
    text-align: right;
  }
  .kice-line-input {
    flex: 1;
    border: none;
    background: transparent;
    color: #111827;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.86rem;
    font-weight: 500;
    padding: 4px 2px;
    min-width: 0;
  }
  .kice-line-input:focus { outline: none; background: #fefce8; }
  .kice-char-badge {
    font-size: 0.68rem;
    font-weight: 800;
    padding: 1px 5px;
    border-radius: 4px;
    flex-shrink: 0;
    color: #64748b;
    background: #f1f5f9;
  }
  .kice-char-badge.ok { color: #047857; background: #d1fae5; }
  .kice-char-badge.over { color: #be123c; background: #ffe4e6; }

  /* Toolbar above KICE sheet */
  .kice-toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 10px;
    align-items: center;
    justify-content: space-between;
  }
  .kice-tool-btn {
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 7px 10px;
    font-size: 0.78rem;
    font-weight: 800;
    cursor: pointer;
  }
  .kice-tool-btn.primary { background: linear-gradient(135deg, #10b981, #0284c7); color: #fff; border: none; }
  .kice-tool-btn.danger { color: var(--danger); border-color: var(--danger); }

  /* Inline KICE 4-Line Practice Sheet inside 55-question cards */
  .kice-mini-wrap {
    margin-top: 10px;
    border-radius: 10px;
    overflow: hidden;
    border: 2px solid var(--kc-main, #d81b60);
    background: #ffffff;
    color: #111827;
    --kc-main: #d81b60;
    --kc-soft: #fce4ec;
    --kc-dash: #f48fb1;
  }
  .kice-mini-wrap.p1 { --kc-main: #008a4b; --kc-soft: #e8f5e9; --kc-dash: #81c784; }
  .kice-mini-head {
    background: var(--kc-soft);
    color: var(--kc-main);
    border-bottom: 1.5px solid var(--kc-main);
    padding: 6px 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.76rem;
    font-weight: 900;
  }
  .kice-mini-foot {
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
    padding: 7px 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    flex-wrap: wrap;
  }
  .grade-btn {
    background: linear-gradient(135deg, #10b981, #0284c7);
    color: #fff;
    border: none;
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 0.78rem;
    font-weight: 800;
    cursor: pointer;
  }
  .grade-result {
    display: none;
    padding: 8px 10px;
    background: #f8fafc;
    border-top: 1px dashed #cbd5e1;
    color: #0f172a;
    font-size: 0.78rem;
  }
  .grade-result.open { display: block; animation: fadeIn 0.2s ease; }
  .g-chip { display: inline-block; padding: 2px 7px; border-radius: 999px; font-size: 0.74rem; font-weight: 800; margin: 2px 3px 2px 0; }
  .g-hit { background: #d1fae5; color: #047857; border: 1px solid #10b981; }
  .g-miss { background: #ffe4e6; color: #be123c; border: 1px solid #f43f5e; }

  /* Authentic Print CSS for B4/A4 KICE Answer Sheet */
  @media print {
    body { background: #fff !important; padding: 0 !important; color: #000 !important; }
    .top-header, .main-tabs, .bottom-bar, .sub-tabs, .kice-toolbar, .kice-char-badge { display: none !important; }
    .container { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
    .kice-paper { box-shadow: none !important; padding: 0 !important; margin: 0 !important; border-radius: 0 !important; }
    .kice-line-input { font-size: 11pt !important; }
    @page { size: B4 portrait; margin: 10mm; }
  }
"""

html = html.replace("</style>", EXTRA_CSS + "\n</style>", 1)

# 3. Replace main-tabs with 4 tabs
OLD_TABS = """<nav class="main-tabs">
  <button class="main-tab active" id="tabTop55" onclick="switchMode('top55')">🔥 출제확률 TOP 55</button>
  <button class="main-tab" id="tabExam" onclick="switchMode('exam')">📝 3교시 실전 풀세트</button>
</nav>"""

NEW_TABS = """<nav class="main-tabs">
  <button class="main-tab" id="tabAnalysis" onclick="switchMode('analysis')">📊 기출분석<br><small>20~26</small></button>
  <button class="main-tab active" id="tabTop55" onclick="switchMode('top55')">🔥 55제 실전<br><small>확률순</small></button>
  <button class="main-tab" id="tabExam" onclick="switchMode('exam')">📝 3교시 시험<br><small>문제지</small></button>
  <button class="main-tab" id="tabSheet" onclick="switchMode('sheet')">📄 KICE 답안지<br><small>공식B4</small></button>
</nav>"""

assert OLD_TABS in html, "OLD_TABS not found"
html = html.replace(OLD_TABS, NEW_TABS, 1)

# 4. Add secAnalysis before secTop55, and secSheet after secExam
ANALYSIS_SECTION = """  <!-- MODE 0: 2020-2026 PAST EXAM ANALYSIS DASHBOARD -->
  <section id="secAnalysis" style="display:none;">
    <div id="analysisContainer"></div>
  </section>

"""
html = html.replace('  <!-- MODE 1: TOP 55 BY PROBABILITY -->', ANALYSIS_SECTION + '  <!-- MODE 1: TOP 55 BY PROBABILITY -->', 1)

SHEET_SECTION = """
  <!-- MODE 3: AUTHENTIC KICE OFFICIAL B4 ANSWER SHEET -->
  <section id="secSheet" style="display:none;">
    <div class="sub-tabs">
      <button class="sub-tab active" id="shPed" onclick="switchSheetPeriod('ped')">1교시 교육학<br><small>초록 · 논술</small></button>
      <button class="sub-tab" id="shA" onclick="switchSheetPeriod('A')">2교시 전공 A<br><small>분홍 · 12문항</small></button>
      <button class="sub-tab" id="shB" onclick="switchSheetPeriod('B')">3교시 전공 B<br><small>주황 · 11문항</small></button>
    </div>
    <div class="kice-toolbar">
      <div style="display:flex;gap:6px;flex-wrap:wrap;">
        <button class="kice-tool-btn primary" onclick="fillSheetModelAnswers()">✨ 만점 모범답안 채우기</button>
        <button class="kice-tool-btn danger" onclick="clearSheetAnswers()">🧹 백지 초기화</button>
      </div>
      <button class="kice-tool-btn" onclick="window.print()">🖨️ KICE 공식 답안지 인쇄 / PDF</button>
    </div>
    <div id="sheetContainer"></div>
  </section>
"""
html = html.replace('  </section>\n</main>', '  </section>\n' + SHEET_SECTION + '</main>', 1)

# 5. Inject ANALYSIS_DATA constant right after TOP55
html = html.replace(
    "const TOP55 = ",
    f"const ANALYSIS_DATA = {ANALYSIS_JSON};\nconst TOP55 = ",
    1
)

# 6. Inject Authentic KICE Practice Sheet inside every 55-question card (Education=6 lines / 60 chars, Counseling=4 lines / 45 chars)
KICE_MINI_SNIPPET = """      <!-- AUTHENTIC KICE PRACTICE SHEET -->
      <div class="kice-mini-wrap ${item.part === '교육학' ? 'p1' : 'p2'}">
        <div class="kice-mini-head">
          <span>📄 KICE 공식 B4 답안지 실전 작성 (${item.part === '교육학' ? '1교시 초록 · 6줄 양식' : '2·3교시 전공 · 4줄 양식'})</span>
          <span>${item.part === '교육학' ? '권장 50~60자/줄' : '권장 38~45자/줄'}</span>
        </div>
        <div class="kice-q-row">
          <div class="kice-q-num">문항 ${item.rank}<br>(4점)</div>
          <div class="kice-lines-wrap">
            ${(item.part === '교육학' ? [0,1,2,3,4,5] : [0,1,2,3]).map(li => {
              const limit = item.part === '교육학' ? 60 : 45;
              const ph = item.part === '교육학'
                ? (li === 5 ? '6번째 줄 (마무리: 이처럼 교사가 ~한다면 ~이 실현될 것이다.)' : `${li+1}번째 줄 (50~60자 이내 논술 핵심 서술)`)
                : `${li+1}번째 줄 (38~45자 이내 핵심 서술)`;
              const savedVal = (state.lineDrafts && state.lineDrafts[item.id] && state.lineDrafts[item.id][li]) || '';
              const len = savedVal.length;
              const cls = len === 0 ? '' : (len <= limit ? 'ok' : 'over');
              return `
                <div class="kice-line-item">
                  <span class="kice-line-idx">${li+1}</span>
                  <input type="text" class="kice-line-input" id="kline-${item.id}-${li}" value="${escHtml(savedVal)}" placeholder="${ph}" oninput="onKiceLineInput(${item.id}, ${li}, ${limit})">
                  <span class="kice-char-badge ${cls}" id="kcnt-${item.id}-${li}">${len}/${limit}</span>
                </div>
              `;
            }).join('')}
          </div>
        </div>
        <div class="kice-mini-foot">
          <button class="grade-btn" onclick="gradeDraft(${item.id})">🎯 KICE 키워드 즉시 채점</button>
          <span style="font-size:0.72rem;color:#475569;font-weight:700;">※ ${item.part === '교육학' ? '60자 초과 시 빨간 경고 (교육학 6줄 규격)' : '45자 초과 시 빨간 경고 (B4 1줄 이탈 방지)'}</span>
        </div>
        <div class="grade-result" id="grade-res-${item.id}"></div>
      </div>

      <!-- TOGGLE BUTTONS -->"""

assert "<!-- TOGGLE BUTTONS -->" in html, "TOGGLE BUTTONS anchor missing"
html = html.replace("      <!-- TOGGLE BUTTONS -->", KICE_MINI_SNIPPET, 1)

# 7. Add full JS logic for KICE Official B4 Answer Sheet (1st/2nd/3rd Period) + Analysis + Self-Grading
OLD_INIT = """// Init
updateDDay();
applyPrefs();
updateProgress();
renderTop55();"""

EXTRA_JS = """
if (!state.lineDrafts) state.lineDrafts = {};
if (!state.sheetData) state.sheetData = { ped: {}, A: {}, B: {}, name: '', examNo: '' };
if (!state.sheetPeriod) state.sheetPeriod = 'A';

function persistExtra() {
  try {
    const prev = JSON.parse(localStorage.getItem(STORE_KEY) || '{}');
    prev.lineDrafts = state.lineDrafts;
    prev.sheetData = state.sheetData;
    localStorage.setItem(STORE_KEY, JSON.stringify(prev));
  } catch(e) {}
}

function onKiceLineInput(id, lineIdx, limit) {
  const maxC = limit || 45;
  const inp = document.getElementById(`kline-${id}-${lineIdx}`);
  const badge = document.getElementById(`kcnt-${id}-${lineIdx}`);
  if (!inp) return;
  const val = inp.value;
  if (!state.lineDrafts[id]) state.lineDrafts[id] = ['', '', '', '', '', ''];
  state.lineDrafts[id][lineIdx] = val;
  if (badge) {
    badge.textContent = `${val.length}/${maxC}`;
    badge.className = 'kice-char-badge ' + (val.length === 0 ? '' : (val.length <= maxC ? 'ok' : 'over'));
  }
  persistExtra();
}

function gradeDraft(id) {
  const item = TOP55.find(x => x.id === id);
  const box = document.getElementById('grade-res-' + id);
  if (!item || !box) return;
  const lineCnt = item.part === '교육학' ? 6 : 4;
  const lines = Array.from({length: lineCnt}, (_, li) => {
    const el = document.getElementById(`kline-${id}-${li}`);
    return el ? el.value : '';
  });
  const text = lines.join(' ').replace(/\\s+/g, '').toLowerCase();
  const kws = item.keywords || [];
  let hits = 0;
  const chips = kws.map(kw => {
    const norm = kw.replace(/\\([^)]*\\)/g, '').replace(/\\s+/g, '').toLowerCase();
    const parts = norm.split(/[·,/]/).filter(p => p.length >= 2);
    const matched = text.includes(norm) || (parts.length > 0 && parts.some(p => text.includes(p)));
    if (matched) hits++;
    return `<span class="g-chip ${matched ? 'g-hit' : 'g-miss'}">${matched ? '✔ ' : '✘ '}${escHtml(kw)}</span>`;
  }).join('');
  const pct = kws.length ? Math.round((hits / kws.length) * 100) : 0;
  const msg = pct === 100 ? '🏆 완벽! KICE 만점 키워드 100% 적중!' : (pct >= 60 ? '👍 우수! 누락된 빨강 키워드를 보완하세요.' : '📌 STEP 2 정답을 확인하고 핵심 키워드를 채워보세요.');
  box.innerHTML = `<div style="font-weight:900;margin-bottom:5px;">채점 결과: <span style="color:#0284c7;">${hits} / ${kws.length} (${pct}%)</span> — ${msg}</div><div>${chips}</div>`;
  box.classList.add('open');
}

function jumpToQuestionById(id) {
  state.filter = 'all';
  state.search = '';
  const si = document.getElementById('searchInput');
  if (si) si.value = '';
  document.querySelectorAll('#filterBar .chip').forEach(c => c.classList.toggle('active', c.dataset.f === 'all'));
  const idx = TOP55.findIndex(x => x.id === id);
  state.cardIdx = idx >= 0 ? idx : 0;
  state.viewMode = 'card';
  applyPrefs();
  switchMode('top55');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderAnalysis() {
  const el = document.getElementById('analysisContainer');
  if (!el) return;
  const maxChars = Math.max(...ANALYSIS_DATA.yearly.map(y => y.totalChars));
  const maxDom = Math.max(...ANALYSIS_DATA.domains.map(d => d.count));

  const yrBars = ANALYSIS_DATA.yearly.map(y => {
    const w = Math.round((y.totalChars / maxChars) * 100);
    const isHot = Number(y.year) >= 2025;
    return `
      <div class="bar-row yr-row">
        <div class="bar-lbl">${y.year}년</div>
        <div class="bar-track"><div class="bar-fill ${isHot ? 'hot' : ''}" style="width:${w}%"></div></div>
        <div class="bar-num">${y.totalChars.toLocaleString()}자 · ${y.asks}발문</div>
      </div>
    `;
  }).join('');

  const domBars = ANALYSIS_DATA.domains.map((d, i) => {
    const w = Math.round((d.count / maxDom) * 100);
    return `
      <div class="bar-row">
        <div class="bar-lbl" title="${escHtml(d.name)}">${escHtml(d.name)}</div>
        <div class="bar-track"><div class="bar-fill ${i < 3 ? 'hot' : ''}" style="width:${w}%"></div></div>
        <div class="bar-num">${d.count}회 출제</div>
      </div>
    `;
  }).join('');

  const kw26Html = ANALYSIS_DATA.kw2026.map(k => `<span class="kw-pill accent">${escHtml(k)}</span>`).join('');
  const kw25Html = ANALYSIS_DATA.kw2025.map(k => `<span class="kw-pill">${escHtml(k)}</span>`).join('');

  const top10Html = TOP55.slice(0, 10).map(item => `
    <div class="top10-item" onclick="jumpToQuestionById(${item.id})">
      <div class="top10-left">
        <div class="top10-title">#${item.rank}위 [${item.prob}%] ${escHtml(item.title)}</div>
        <div class="top10-sub">${escHtml(item.part)} · ${escHtml(item.domain)} · ${item.past_years.length ? '기출 ' + item.past_years.join('·') : '2027 공백 적중'}</div>
      </div>
      <span class="top10-go">풀기 ▶</span>
    </div>
  `).join('');

  el.innerHTML = `
    <div class="an-hero">
      <h2>📊 2027(11.28) 임용 전문상담 7개년 기출 전수 분석</h2>
      <p><strong>G:/내 드라이브/2. 전문상담</strong> 실제 기출 PDF 20부(2020~2026 전공 A·B 14부 + 교육학 6부)를 전수 텍스트 추출하여 출제 패턴·지문 폭증 추이·공백기 순환 주기를 정밀 분석하고 <strong>55개 실전 문제 & KICE 공식 B4 답안지</strong>로 구현했습니다.</p>
    </div>

    <div class="kpi-grid">
      <div class="kpi-card"><div class="kpi-val">7개년</div><div class="kpi-lbl">2020~2026 PDF 전수</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:var(--danger);">+49.7%</div><div class="kpi-lbl">지문 분량 폭증 (25년)</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:var(--gold);">80%+</div><div class="kpi-lbl">복합형(2~3이론 융합)</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:var(--success);">55문제</div><div class="kpi-lbl">0순위 18 · 1순위 20 · 2순위 17</div></div>
    </div>

    <div class="an-card">
      <h3>📈 연도별 지문 분량 & &lt;작성 방법&gt; 발문 수 폭증 추이</h3>
      ${yrBars}
      <p style="font-size:0.76rem;color:var(--text-muted);margin-top:8px;">※ 2020년 16,598자(32발문) ➔ 2025년 24,851자 / 2026년 23,851자(역대 최다 40발문). 초장문 사례 독해 속도와 핵심 단서 추출 훈련이 당락을 가릅니다.</p>
    </div>

    <div class="an-card">
      <h3>🎯 2020~2026 7대 영역별 출제 빈도 (실제 PDF 집계)</h3>
      ${domBars}
    </div>

    <div class="an-card">
      <h3>🔥 2027(11.28) 0순위 최유력 적중 예측 TOP 10 <span style="font-size:0.74rem;color:var(--accent);">클릭 시 바로 풀기</span></h3>
      ${top10Html}
    </div>

    <div class="an-card">
      <h3>🔍 직전 2026학년도 실제 기출 핵심 키워드</h3>
      <div class="kw-cloud">${kw26Html}</div>
      <h3 style="margin-top:14px;">📌 2025학년도 실제 기출 핵심 키워드</h3>
      <div class="kw-cloud">${kw25Html}</div>
    </div>

    <div class="an-card">
      <h3>🏆 11월 28일 시험장 만점 4대 절대 전략</h3>
      <div class="strat-grid">
        <div class="strat-box"><strong>1. 복합형(80%+) 융합 사고</strong>단일 이론 암기 금지! [DSM-5-TR 감별 + MMPI-2-RF 척도 + 상담기법] 3단 융합 사례로 훈련하세요.</div>
        <div class="strat-box"><strong>2. 힌트 ZERO 현상학적 인출</strong>발문에 학자명·이론명이 주어지지 않습니다. 내담자 증상과 상담 대화 단서만으로 정식 명칭을 인출하세요.</div>
        <div class="strat-box"><strong>3. B4 답안지 줄당 38~45자 압축</strong>군더더기 수식어를 제거하고 1줄당 1개 KICE 채점 포인트를 38~45자 이내로 정확히 배치하세요.</div>
        <div class="strat-box"><strong>4. KICE 정식 용어 100% 고정</strong>탈숙고(Dereflection), 숀 셰이 (Shawn Shea), 자아동조적/자아이질적, 사회적(실용적) 의사소통장애 등 정식명 필수!</div>
      </div>
    </div>
  `;
}

/* ===== KICE OFFICIAL B4 ANSWER SHEET RENDERER ===== */
function onSheetInput(period, key, limit) {
  const inp = document.getElementById(`sh-${period}-${key}`);
  const badge = document.getElementById(`shcnt-${period}-${key}`);
  if (!inp) return;
  if (!state.sheetData[period]) state.sheetData[period] = {};
  state.sheetData[period][key] = inp.value;
  if (badge) {
    const len = inp.value.length;
    badge.textContent = `${len}/${limit}`;
    badge.className = 'kice-char-badge ' + (len === 0 ? '' : (len <= limit ? 'ok' : 'over'));
  }
  persistExtra();
}

function onSheetMeta(field, val) {
  state.sheetData[field] = val;
  persistExtra();
}

function buildKiceHeader(periodCode, periodNum, subjectLabel) {
  const omrBars = Array(10).fill('<span></span>').join('');
  return `
    <div class="kice-omr-marks">${omrBars}</div>
    <div class="kice-banner">
      <span class="kice-period-pill">${periodNum}교시</span>
      <span>2027학년도 중등학교교사 임용후보자 선정경쟁시험 제1차 시험 답안지</span>
    </div>
    <div class="kice-meta-grid">
      <div class="kice-meta-col">
        <div style="padding:5px 7px;font-size:0.68rem;line-height:1.35;border-bottom:1px solid var(--kc-dash);">
          본인은 응시자 유의 사항을 숙지하였으며 이를 지키지 않아 발생하는 모든 불이익을 감수할 것을 서약합니다.
        </div>
        <div class="kice-cell-head">성 명</div>
        <div class="kice-cell-body">
          <input type="text" class="kice-input-inline" placeholder="성명 입력" value="${escHtml(state.sheetData.name || '')}" oninput="onSheetMeta('name', this.value)">
        </div>
        <div class="kice-subject-row">
          <div class="kice-subject-box">${subjectLabel}<br><small style="font-weight:700;">전용 답안지</small></div>
          <div class="kice-page-box">
            <div style="font-weight:800;font-size:0.7rem;">쪽 번호</div>
            <div style="font-size:0.85rem;">❶ &nbsp; ②</div>
          </div>
        </div>
      </div>
      <div class="kice-meta-col">
        <div class="kice-cell-head">수 험 번 호 (전문상담)</div>
        <div class="kice-cell-body" style="flex-direction:column;gap:4px;">
          <input type="text" class="kice-input-inline" placeholder="수험번호 8자리 (예: 20271128)" value="${escHtml(state.sheetData.examNo || '')}" oninput="onSheetMeta('examNo', this.value)">
          <div class="kice-omr-row"><span>① ②</span><span>⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨</span></div>
          <div class="kice-omr-row"><span>① ②</span><span>⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨</span></div>
          <div class="kice-omr-row"><span>&nbsp;</span><span>⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨</span></div>
        </div>
      </div>
      <div class="kice-meta-col">
        <div class="kice-cell-head">※ 결시자 확인란(응시자는 표기하지 말 것)</div>
        <div style="padding:5px 7px;font-size:0.66rem;line-height:1.4;border-bottom:1px solid var(--kc-main);">
          - 결시자 성명과 수험 번호 기재<br>
          - 검은색 필기구로 '●' 표기
        </div>
        <div class="kice-cell-head">※ 감독관 확인란(응시자는 표기하지 말 것)</div>
        <div style="padding:5px 7px;font-size:0.66rem;line-height:1.4;">
          - 본인 여부, 성명, 수험 번호 기록 확인 후 서명/날인 (서명 또는 날인)
        </div>
      </div>
    </div>
    <div class="kice-notice">
      1. 수험 번호와 쪽 번호는 검은색 필기구를 사용하여 '●'로 표기하시오.<br>
      2. 답안은 지워지거나 번지지 않는 동일한 종류의 검은색 필기구를 사용하여 작성하시오(연필, 번지거나 지워지는 펜, 수정테이프 또는 수정액 등 사용 불가).<br>
      3. 응시자 유의 사항을 위반하여 작성한 답안은 채점 시 불이익을 받을 수 있으니 유의하시오.
    </div>
  `;
}

function renderKiceSheet() {
  const el = document.getElementById('sheetContainer');
  if (!el) return;
  const p = state.sheetPeriod || 'A';
  document.getElementById('shPed').classList.toggle('active', p === 'ped');
  document.getElementById('shA').classList.toggle('active', p === 'A');
  document.getElementById('shB').classList.toggle('active', p === 'B');

  const store = state.sheetData[p] || {};

  if (p === 'ped') {
    const rows = Array.from({length: 25}, (_, i) => {
      const key = `L${i+1}`;
      const val = store[key] || '';
      const len = val.length;
      const cls = len === 0 ? '' : (len <= 60 ? 'ok' : 'over');
      const solidCls = (i + 1) % 5 === 0 ? 'solid-5' : '';
      return `
        <div class="kice-line-item ${solidCls}">
          <span class="kice-line-idx">${i+1}</span>
          <input type="text" class="kice-line-input" id="sh-ped-${key}" value="${escHtml(val)}" placeholder="${i===0?'서론 1줄 (최근 급변하는 미래 교육환경 속에서...)':''}" oninput="onSheetInput('ped','${key}',60)">
          <span class="kice-char-badge ${cls}" id="shcnt-ped-${key}">${len}/60</span>
        </div>
      `;
    }).join('');

    el.innerHTML = `
      <div class="kice-paper p1">
        <div class="kice-frame">
          ${buildKiceHeader('p1', '1', '교육학 논술')}
          <div class="kice-lines-wrap">${rows}</div>
        </div>
      </div>
    `;
    return;
  }

  const examArr = p === 'A' ? EXAM_A : EXAM_B;
  const pClass = p === 'A' ? 'p2' : 'p3';
  const pNum = p === 'A' ? '2' : '3';
  const subj = p === 'A' ? '전공 A' : '전공 B';

  const qRows = examArr.map(q => {
    const isGiip = q.score === 2 || q.type === '기입형';
    const lineCount = isGiip ? 1 : 4;
    const limit = isGiip ? 40 : 45;
    const linesHtml = Array.from({length: lineCount}, (_, li) => {
      const key = `Q${q.no}_L${li+1}`;
      const val = store[key] || '';
      const len = val.length;
      const cls = len === 0 ? '' : (len <= limit ? 'ok' : 'over');
      const ph = isGiip ? '㉠ ____________ ,  ㉡ ____________' : `${li+1}줄 (38~45자 이내 핵심 키워드 서술)`;
      return `
        <div class="kice-line-item">
          <span class="kice-line-idx">${isGiip ? '답' : (li+1)}</span>
          <input type="text" class="kice-line-input" id="sh-${p}-${key}" value="${escHtml(val)}" placeholder="${ph}" oninput="onSheetInput('${p}','${key}',${limit})">
          <span class="kice-char-badge ${cls}" id="shcnt-${p}-${key}">${len}/${limit}</span>
        </div>
      `;
    }).join('');

    return `
      <div class="kice-q-row">
        <div class="kice-q-num">문항 ${q.no}<br>(${q.score}점)</div>
        <div class="kice-lines-wrap">${linesHtml}</div>
      </div>
    `;
  }).join('');

  el.innerHTML = `
    <div class="kice-paper ${pClass}">
      <div class="kice-frame">
        ${buildKiceHeader(pClass, pNum, subj)}
        ${qRows}
      </div>
    </div>
  `;
}

function switchSheetPeriod(p) {
  state.sheetPeriod = p;
  renderKiceSheet();
}

function fillSheetModelAnswers() {
  const p = state.sheetPeriod || 'A';
  if (!state.sheetData[p]) state.sheetData[p] = {};
  if (p === 'ped') {
    const tmp = document.createElement('div');
    tmp.innerHTML = PED_EXAM.answerHtml || '';
    const paras = Array.from(tmp.querySelectorAll('p, .essay-sec')).map(x => x.textContent.trim()).filter(Boolean);
    const sentences = paras.join(' ').split(/(?<=[.!?])\\s+/).filter(Boolean);
    for (let i = 0; i < 25; i++) {
      state.sheetData.ped[`L${i+1}`] = sentences[i] || '';
    }
  } else {
    const examArr = p === 'A' ? EXAM_A : EXAM_B;
    examArr.forEach(q => {
      const isGiip = q.score === 2 || q.type === '기입형';
      const ansLines = q.model || [];
      if (isGiip) {
        state.sheetData[p][`Q${q.no}_L1`] = ansLines.join(' / ');
      } else {
        for (let li = 0; li < 4; li++) {
          state.sheetData[p][`Q${q.no}_L${li+1}`] = ansLines[li] || '';
        }
      }
    });
  }
  persistExtra();
  renderKiceSheet();
}

function clearSheetAnswers() {
  const p = state.sheetPeriod || 'A';
  state.sheetData[p] = {};
  persistExtra();
  renderKiceSheet();
}

// Override switchMode to support 4 tabs: analysis | top55 | exam | sheet
const _origSwitchMode = switchMode;
switchMode = function(mode) {
  state.mode = mode;
  document.getElementById('tabAnalysis').classList.toggle('active', mode === 'analysis');
  document.getElementById('tabTop55').classList.toggle('active', mode === 'top55');
  document.getElementById('tabExam').classList.toggle('active', mode === 'exam');
  document.getElementById('tabSheet').classList.toggle('active', mode === 'sheet');
  document.getElementById('secAnalysis').style.display = mode === 'analysis' ? 'block' : 'none';
  document.getElementById('secTop55').style.display = mode === 'top55' ? 'block' : 'none';
  document.getElementById('secExam').style.display = mode === 'exam' ? 'block' : 'none';
  document.getElementById('secSheet').style.display = mode === 'sheet' ? 'block' : 'none';
  document.getElementById('bottomBar').style.display = (mode === 'top55' && state.viewMode === 'card') ? 'block' : 'none';
  if (mode === 'analysis') renderAnalysis();
  else if (mode === 'exam') renderExam();
  else if (mode === 'sheet') renderKiceSheet();
  else renderTop55();
};

// Init
updateDDay();
applyPrefs();
updateProgress();
renderAnalysis();
renderKiceSheet();
switchMode('sheet');
"""

assert OLD_INIT in html, "OLD_INIT not found"
html = html.replace(OLD_INIT, EXTRA_JS, 1)

out_local = "index.html"
out_root = os.path.join("..", "index.html")
with open(out_local, "w", encoding="utf-8") as f:
    f.write(html)
with open(out_root, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Built & synced KICE Official Sheet App! Size: {len(html):,} chars")
