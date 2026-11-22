# -*- coding: utf-8 -*-
import json
import os
import re
import shutil

# Load real 2020-2026 PDF analysis data extracted from G:\내 드라이브\2. 전문상담
ANALYSIS_PATH = r"C:\Users\LENOVO\.gemini\antigravity\brain\b35672cb-40d5-428e-8945-cbb2b7b662e7\scratch\past_exam_analysis.json"
with open(ANALYSIS_PATH, "r", encoding="utf-8") as f:
    past_analysis = json.load(f)

# Load existing build_mobile_top55_webapp.py as base and enhance it cleanly
with open("build_mobile_top55_webapp.py", "r", encoding="utf-8") as f:
    base_code = f.read()

# Execute base script's data preparation by running it in a namespace or reading generated index.html
# Even cleaner: let's run build_mobile_top55_webapp.py first to ensure fresh index.html, then inject the
# 1) Analysis Dashboard Tab (real 2020-2026 PDF data)
# 2) Interactive Self-Grading Typing Box inside every 55-item card
# 3) Clean 3-tab navigation (📊 기출분석 | 🔥 55제 실전문제 | 📝 3교시 풀세트)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Verify required anchors exist
assert '<nav class="main-tabs">' in html, "main-tabs anchor missing"
assert '<section id="secTop55">' in html, "secTop55 anchor missing"
assert 'const TOP55 =' in html, "TOP55 data missing"

# Prepare Analysis JSON for injection
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
    "<title>2027 임용(11.28) 전문상담 기출분석 & 55제 실전 앱</title>"
)
html = html.replace(
    '<span class="brand-title">2027 임용 출제확률순 마스터</span>',
    '<span class="brand-title">2027 전문상담 기출분석·55제</span>'
)

# 2. Update CSS for 3-column main tabs, Analysis Dashboard, and Self-Grading box
EXTRA_CSS = """
  /* 3-tab main navigation */
  .main-tabs { grid-template-columns: repeat(3, 1fr) !important; gap: 6px !important; }
  .main-tab { padding: 9px 4px !important; font-size: 0.82rem !important; }

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
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin-bottom: 12px;
  }
  @media (min-width: 640px) { .kpi-grid { grid-template-columns: repeat(4, 1fr); } }
  .kpi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 10px;
    text-align: center;
  }
  .kpi-val { font-size: 1.25rem; font-weight: 900; color: var(--accent); line-height: 1.2; }
  .kpi-lbl { font-size: 0.74rem; color: var(--text-muted); margin-top: 4px; font-weight: 700; }
  .an-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
  }
  .an-card h3 {
    font-size: 0.94rem;
    font-weight: 900;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
  }
  .bar-row {
    display: grid;
    grid-template-columns: 112px 1fr 56px;
    align-items: center;
    gap: 8px;
    margin-bottom: 7px;
    font-size: 0.78rem;
  }
  .bar-row.yr-row { grid-template-columns: 52px 1fr 94px; }
  .bar-lbl { font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .bar-track {
    height: 12px;
    background: var(--surface-2);
    border-radius: 999px;
    overflow: hidden;
    border: 1px solid var(--border);
  }
  .bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #0284c7, #6366f1);
  }
  .bar-fill.hot { background: linear-gradient(90deg, #f43f5e, #fbbf24); }
  .bar-num { text-align: right; font-weight: 800; color: var(--text-muted); font-size: 0.74rem; }
  .kw-cloud { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 6px; }
  .kw-pill {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 3px 8px;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text);
  }
  .kw-pill.accent { background: rgba(56,189,248,0.16); border-color: var(--accent); color: var(--accent); }
  .top10-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    padding: 9px 10px;
    border-radius: 10px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    margin-bottom: 6px;
    cursor: pointer;
    transition: border-color 0.15s;
  }
  .top10-item:hover { border-color: var(--accent); }
  .top10-left { min-width: 0; }
  .top10-title { font-size: 0.84rem; font-weight: 800; color: var(--text); }
  .top10-sub { font-size: 0.73rem; color: var(--text-muted); margin-top: 2px; }
  .top10-go {
    flex-shrink: 0;
    background: var(--accent);
    color: #082f49;
    font-weight: 900;
    font-size: 0.74rem;
    padding: 4px 8px;
    border-radius: 8px;
  }
  .strat-grid { display: grid; grid-template-columns: 1fr; gap: 8px; }
  @media (min-width: 640px) { .strat-grid { grid-template-columns: 1fr 1fr; } }
  .strat-box {
    background: var(--surface-2);
    border-left: 3px solid var(--gold);
    border-radius: 8px;
    padding: 10px;
    font-size: 0.8rem;
    line-height: 1.55;
  }
  .strat-box strong { color: var(--gold); display: block; margin-bottom: 3px; }

  /* Interactive Self-Grading Answer Input inside 55 cards */
  .practice-box {
    margin-top: 10px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px;
  }
  .practice-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.78rem;
    font-weight: 800;
    color: var(--gold);
    margin-bottom: 6px;
  }
  .practice-ta {
    width: 100%;
    min-height: 76px;
    background: var(--pass-bg);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 8px 10px;
    font-family: inherit;
    font-size: 0.85rem;
    line-height: 1.5;
    resize: vertical;
  }
  .practice-ta:focus { outline: none; border-color: var(--accent); }
  .practice-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    margin-top: 6px;
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
    margin-top: 8px;
    display: none;
    padding: 8px;
    border-radius: 8px;
    background: var(--pass-bg);
    border: 1px solid var(--border);
    font-size: 0.78rem;
  }
  .grade-result.open { display: block; animation: fadeIn 0.2s ease; }
  .g-chip {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 800;
    margin: 2px 3px 2px 0;
  }
  .g-hit { background: rgba(16,185,129,0.22); color: var(--success); border: 1px solid var(--success); }
  .g-miss { background: rgba(244,63,94,0.18); color: var(--danger); border: 1px solid var(--danger); }
"""

html = html.replace("</style>", EXTRA_CSS + "\n</style>", 1)

# 3. Replace main-tabs with 3 tabs (Analysis + Top 55 + 3-Period Full Exam)
OLD_TABS = """<nav class="main-tabs">
  <button class="main-tab active" id="tabTop55" onclick="switchMode('top55')">🔥 출제확률 TOP 55</button>
  <button class="main-tab" id="tabExam" onclick="switchMode('exam')">📝 3교시 실전 풀세트</button>
</nav>"""

NEW_TABS = """<nav class="main-tabs">
  <button class="main-tab" id="tabAnalysis" onclick="switchMode('analysis')">📊 기출분석 (20~26)</button>
  <button class="main-tab active" id="tabTop55" onclick="switchMode('top55')">🔥 55제 실전문제</button>
  <button class="main-tab" id="tabExam" onclick="switchMode('exam')">📝 3교시 풀세트</button>
</nav>"""

assert OLD_TABS in html, "OLD_TABS not found"
html = html.replace(OLD_TABS, NEW_TABS, 1)

# 4. Add secAnalysis section right before secTop55
ANALYSIS_SECTION = """  <!-- MODE 0: 2020-2026 PAST EXAM ANALYSIS DASHBOARD -->
  <section id="secAnalysis" style="display:none;">
    <div id="analysisContainer"></div>
  </section>

"""
html = html.replace('  <!-- MODE 1: TOP 55 BY PROBABILITY -->', ANALYSIS_SECTION + '  <!-- MODE 1: TOP 55 BY PROBABILITY -->', 1)

# 5. Inject ANALYSIS_DATA constant right after TOP55
html = html.replace(
    "const TOP55 = ",
    f"const ANALYSIS_DATA = {ANALYSIS_JSON};\nconst TOP55 = ",
    1
)

# 6. Inject Practice Self-Grading UI into renderCardHtml right before TOGGLE BUTTONS
PRACTICE_SNIPPET = """      <!-- SELF-GRADING PRACTICE BOX -->
      <div class="practice-box">
        <div class="practice-head">
          <span>✍️ B4 답안지 실전 연습 (키워드 자동 자가채점)</span>
          <span id="charcnt-${item.id}" style="color:var(--text-muted);">0자</span>
        </div>
        <textarea class="practice-ta" id="ta-${item.id}" placeholder="핵심 KICE 공인 키워드를 포함해 직접 4줄 답안을 작성해 보세요..." oninput="onPracticeInput(${item.id})">${escHtml((state.drafts && state.drafts[item.id]) || '')}</textarea>
        <div class="practice-bar">
          <button class="grade-btn" onclick="gradeDraft(${item.id})">🎯 키워드 즉시 채점</button>
          <span style="font-size:0.73rem;color:var(--text-muted);">권장: 줄당 38~45자 · 4줄 약 160~180자</span>
        </div>
        <div class="grade-result" id="grade-res-${item.id}"></div>
      </div>

      <!-- TOGGLE BUTTONS -->"""

assert "<!-- TOGGLE BUTTONS -->" in html, "TOGGLE BUTTONS anchor missing"
html = html.replace("      <!-- TOGGLE BUTTONS -->", PRACTICE_SNIPPET, 1)

# 7. Update switchMode, saveState, and add renderAnalysis & gradeDraft functions
OLD_INIT = """// Init
updateDDay();
applyPrefs();
updateProgress();
renderTop55();"""

EXTRA_JS = """
if (!state.drafts) state.drafts = {};

function onPracticeInput(id) {
  const ta = document.getElementById('ta-' + id);
  const cnt = document.getElementById('charcnt-' + id);
  if (!ta) return;
  const val = ta.value;
  if (cnt) cnt.textContent = val.length + '자';
  if (!state.drafts) state.drafts = {};
  state.drafts[id] = val;
  try {
    const prev = JSON.parse(localStorage.getItem(STORE_KEY) || '{}');
    prev.drafts = state.drafts;
    localStorage.setItem(STORE_KEY, JSON.stringify(prev));
  } catch(e) {}
}

function gradeDraft(id) {
  const item = TOP55.find(x => x.id === id);
  const ta = document.getElementById('ta-' + id);
  const box = document.getElementById('grade-res-' + id);
  if (!item || !ta || !box) return;
  const text = (ta.value || '').replace(/\\s+/g, '').toLowerCase();
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
  const msg = pct === 100 ? '🏆 완벽! KICE 만점 키워드 100% 적중!' : (pct >= 60 ? '👍 우수! 누락된 빨강 키워드를 보완하세요.' : '📌 STEP 2 정답을 확인하고 핵심 키워드를 암기하세요.');
  box.innerHTML = `<div style="font-weight:900;margin-bottom:5px;">채점 결과: <span style="color:var(--accent);">${hits} / ${kws.length} (${pct}%)</span> — ${msg}</div><div>${chips}</div>`;
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
      <p><strong>G:/내 드라이브/2. 전문상담</strong> 실제 기출 PDF 20부(2020~2026 전공 A·B 14부 + 교육학 6부)를 전수 텍스트 추출하여 출제 패턴·지문 폭증 추이·공백기 순환 주기를 정밀 분석하고 <strong>55개 실전 문제</strong>로 압축했습니다.</p>
    </div>

    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-val">7개년</div>
        <div class="kpi-lbl">2020~2026 PDF 전수</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val" style="color:var(--danger);">+49.7%</div>
        <div class="kpi-lbl">지문 분량 폭증 (25년)</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val" style="color:var(--gold);">80%+</div>
        <div class="kpi-lbl">복합형(2~3이론 융합)</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-val" style="color:var(--success);">55문제</div>
        <div class="kpi-lbl">0순위 18 · 1순위 20 · 2순위 17</div>
      </div>
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
        <div class="strat-box"><strong>4. KICE 정식 용어 100% 고정</strong>탈숙고(Dereflection), 숀 셰이 (Shawn Shea), 사회적(실용적) 의사소통장애 등 한글 정식명(영어 약자) 필수!</div>
      </div>
    </div>
  `;
}

// Override switchMode to support 3 tabs: analysis | top55 | exam
const _origSwitchMode = switchMode;
switchMode = function(mode) {
  state.mode = mode;
  document.getElementById('tabAnalysis').classList.toggle('active', mode === 'analysis');
  document.getElementById('tabTop55').classList.toggle('active', mode === 'top55');
  document.getElementById('tabExam').classList.toggle('active', mode === 'exam');
  document.getElementById('secAnalysis').style.display = mode === 'analysis' ? 'block' : 'none';
  document.getElementById('secTop55').style.display = mode === 'top55' ? 'block' : 'none';
  document.getElementById('secExam').style.display = mode === 'exam' ? 'block' : 'none';
  document.getElementById('bottomBar').style.display = (mode === 'top55' && state.viewMode === 'card') ? 'block' : 'none';
  if (mode === 'analysis') renderAnalysis();
  else if (mode === 'exam') renderExam();
  else renderTop55();
};

// Init
updateDDay();
applyPrefs();
updateProgress();
renderAnalysis();
switchMode('analysis');
"""

assert OLD_INIT in html, "OLD_INIT not found"
html = html.replace(OLD_INIT, EXTRA_JS, 1)

# Write to both 교육학/index.html and repo root index.html
out_local = "index.html"
out_root = os.path.join("..", "index.html")
with open(out_local, "w", encoding="utf-8") as f:
    f.write(html)
with open(out_root, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Built & synced! Size: {len(html):,} chars")
print("Local:", os.path.abspath(out_local))
print("Root :", os.path.abspath(out_root))
