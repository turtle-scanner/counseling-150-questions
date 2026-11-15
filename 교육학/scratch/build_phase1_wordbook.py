import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

# Read items from kice_55_core_compressed.html
source_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
target_html_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_d54_phase1_wordbook.html'

with open(source_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', text)
if not m:
    print("Could not find items array!")
    sys.exit(1)

items = json.loads(m.group(1))
print(f"Loaded {len(items)} items.")

# Format answer text with yellow highlighter, tags, and interactive blanks
def format_html_ans(ans_text, kw=''):
    if not ans_text:
        return ''
    # Tag badges [핵심 장점], [2022 효과] etc.
    t = re.sub(r'\[([^\]]+)\]', r'<span class="tag-badge">[\1]</span>', ans_text)

    # Extract terms to blank out from kw
    raw_kw = re.sub(r'\(.*?\)', '', kw).strip()
    terms_to_blank = []
    if raw_kw:
        for part in re.split(r'[,·/\s➔]+', raw_kw):
            part = part.strip()
            if len(part) >= 2 and part not in ['모형', '이론', '과정', '단계', '기법', '원리', '측면', '모델', '유형', '척도', '지표']:
                terms_to_blank.append(part)
    
    # Also terms inside parentheses
    inner = re.findall(r'\((.*?)\)', kw)
    for inn in inner:
        for part in re.split(r'[,·/\s➔]+', inn):
            part = part.strip()
            if len(part) >= 2 and part not in ['모형', '이론', '과정', '단계', '기법', '원리', '측면', '모델', '유형', '척도', '지표', '홀랜드', '수퍼', '보웬', '미누친', '사티어', '융', '설리반', '헤일리', '엘리스', '벡']:
                terms_to_blank.append(part)
                
    terms_to_blank = sorted(list(set(terms_to_blank)), key=lambda x: len(x), reverse=True)

    # Split into 4 lines
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    formatted_lines = []
    for l_idx, line in enumerate(lines):
        line_html = line
        # Blank out key concept in line 1 and line 2
        if l_idx in [0, 1]:
            for tm in terms_to_blank:
                if tm in line_html:
                    line_html = line_html.replace(
                        tm,
                        f'<span class="kw-blank" onclick="toggleKwBlank(this)"><span class="blank-text">{tm}</span></span>',
                        1
                    )
                    break
        formatted_lines.append(f'<div class="ans-line">{line_html}</div>')
    return ''.join(formatted_lines)

# Day allocation (18 Days)
def get_day_info(idx):
    day_num = (idx // 12) + 1
    if day_num > 18:
        day_num = 18
    from datetime import date, timedelta
    start_date = date(2026, 10, 5)
    cur_date = start_date + timedelta(days=(day_num - 1))
    weekdays_kr = ['월', '화', '수', '목', '금', '토', '일']
    w_str = weekdays_kr[cur_date.weekday()]
    return day_num, f"{cur_date.month:02d}/{cur_date.day:02d}({w_str})"

# Category mapping
def get_category_key(badge, kw):
    b = badge or ''
    k = kw or ''
    if '교육' in b or '교수' in b: return '교육'
    if '진로' in b: return '진로'
    if '검사' in b: return '심리검사'
    if '가족' in b: return '가족'
    if '병리' in b or '이상' in b or '장애' in k: return '정신병리'
    if '이론' in b or '행동' in b or '성격' in b or '대인' in b or '다문화' in b: return '이론'
    if '위기' in b or '법령' in b or '윤리' in b or '놀이' in b or '수퍼비전' in b: return '위기'
    return '기타'

cards_html = []
for idx, it in enumerate(items):
    day_num, date_str = get_day_info(idx)
    cat_key = get_category_key(it.get('badge', ''), it.get('kw', ''))
    ans_html = format_html_ans(it.get('ans', ''), it.get('kw', ''))
    q_text = it.get('q', '').replace('\n', '<br>')
    
    card = f"""
    <div class="word-card" id="card-{idx}" data-idx="{idx}" data-day="{day_num}" data-cat="{cat_key}">
      <div class="card-header">
        <div class="card-header-left">
          <span class="day-badge">Day {day_num:02d} ({date_str})</span>
          <span class="cat-badge">[{it.get('badge', '공통')}]</span>
          <span class="num-badge">No. {idx+1:03d}</span>
          <span class="card-title-badge blank-hidden" onclick="toggleTitleBadge(this)" title="클릭하여 표제어 확인">
            <span class="badge-text-hidden">빈칸</span>
            <span class="badge-text-revealed">{it.get('kw', '')}</span>
          </span>
        </div>
        <div class="check-group">
          <label class="check-label"><input type="checkbox" class="chk-box" data-idx="{idx}" data-round="1" onchange="handleCheckChange(this)"> 1회독</label>
          <label class="check-label"><input type="checkbox" class="chk-box" data-idx="{idx}" data-round="2" onchange="handleCheckChange(this)"> 2회독</label>
          <label class="check-label"><input type="checkbox" class="chk-box" data-idx="{idx}" data-round="3" onchange="handleCheckChange(this)"> 3회독</label>
        </div>
      </div>
      <div class="card-question">
        <span class="q-icon">Q.</span> {q_text}
      </div>
      <div class="card-answer">
        {ans_html}
      </div>
    </div>
    """
    cards_html.append(card)

full_cards_str = '\n'.join(cards_html)

html_template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>2027 KICE 임용시험 1단계(D-54~D-36) 55개 코어 203문항 만점 키워드 암기 단어장</title>
  <style>
    /* MALGUN GOTHIC GLOBAL TYPOGRAPHY */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Malgun Gothic', '맑은 고딕', sans-serif !important;
    }}
    body {{
      background-color: #0b0f19;
      color: #f8fafc;
      line-height: 1.6;
      padding: 16px;
      font-weight: 400;
      -webkit-font-smoothing: antialiased;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}

    /* HEADER & STATS BAR */
    header {{
      background: #111827;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 18px 24px;
      margin-bottom: 16px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }}
    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 12px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
    }}
    .main-title {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .dday-badge {{
      background: #ef4444;
      color: #fff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 20px;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.04); }}
    }}
    .header-links {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}
    .btn-link {{
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid #0284c7;
      border-radius: 6px;
      padding: 6px 12px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-link:hover {{
      background: #0284c7;
      color: #fff;
    }}

    /* 3-ROUND STATS DASHBOARD */
    .dashboard-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 10px;
    }}
    .dash-box {{
      background: #1e293b;
      border-radius: 8px;
      padding: 10px 14px;
      border: 1px solid #334155;
    }}
    .dash-title {{
      font-size: 0.8rem;
      color: #94a3b8;
      margin-bottom: 4px;
    }}
    .dash-val {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #34d399;
    }}
    .progress-bar-bg {{
      background: #0f172a;
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 6px;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #10b981, #38bdf8);
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* CONTROLS & FILTER TABS */
    .control-panel {{
      background: #111827;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .toolbar-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .btn-action {{
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #475569;
      border-radius: 6px;
      padding: 7px 14px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-action:hover {{
      background: #334155;
      border-color: #64748b;
    }}
    .btn-action.active {{
      background: #f59e0b;
      color: #000;
      border-color: #d97706;
    }}
    .pill-tabs {{
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      gap: 6px;
      padding-bottom: 4px;
      -webkit-overflow-scrolling: touch;
    }}
    .pill-tabs::-webkit-scrollbar {{
      height: 4px;
    }}
    .pill-tabs::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 2px;
    }}
    .tab-pill {{
      flex: 0 0 auto;
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
      border-radius: 20px;
      padding: 5px 12px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .tab-pill:hover {{
      background: #334155;
      color: #fff;
    }}
    .tab-pill.active {{
      background: #3b82f6;
      color: #fff;
      border-color: #60a5fa;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
    }}

    /* WORD CARDS LIST */
    .cards-container {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .word-card {{
      background: #111827;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 16px 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      transition: all 0.2s;
    }}
    .word-card:hover {{
      border-color: #3b82f6;
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
    }}
    .card-header-left {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .day-badge {{
      background: #0284c7;
      color: #fff;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .cat-badge {{
      color: #94a3b8;
      font-size: 0.85rem;
      font-weight: 700;
    }}
    .num-badge {{
      color: #64748b;
      font-size: 0.82rem;
      font-weight: 700;
    }}

    /* USER REQUESTED: [ 빈칸 ] TITLE BADGE */
    .card-title-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      border-radius: 6px;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
      padding: 3px 18px;
      margin-left: 6px;
      vertical-align: middle;
    }}
    .card-title-badge.blank-hidden {{
      background: #0284c7;
      color: #ffffff;
      font-size: 1.05rem;
      letter-spacing: 2px;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.5);
      border: 1px solid #38bdf8;
    }}
    .card-title-badge.blank-hidden:hover {{
      background: #0369a1;
      transform: translateY(-1px);
    }}
    .card-title-badge.blank-hidden .badge-text-hidden {{
      display: inline;
    }}
    .card-title-badge.blank-hidden .badge-text-revealed {{
      display: none;
    }}

    .card-title-badge.revealed {{
      background: #1e3a8a;
      color: #fbbf24;
      font-size: 1.02rem;
      border: 1.5px solid #3b82f6;
      box-shadow: 0 2px 8px rgba(30, 58, 138, 0.6);
    }}
    .card-title-badge.revealed:hover {{
      background: #1e40af;
    }}
    .card-title-badge.revealed .badge-text-hidden {{
      display: none;
    }}
    .card-title-badge.revealed .badge-text-revealed {{
      display: inline;
    }}

    /* CHECK GROUP */
    .check-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .check-label {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      user-select: none;
    }}
    .chk-box {{
      width: 17px;
      height: 17px;
      accent-color: #10b981;
      cursor: pointer;
    }}

    /* QUESTION BOX */
    .card-question {{
      background: #182234;
      border-left: 3px solid #38bdf8;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      font-size: 0.95rem;
      color: #e2e8f0;
      margin-bottom: 12px;
      line-height: 1.5;
    }}
    .q-icon {{
      color: #38bdf8;
      font-weight: 800;
      margin-right: 4px;
    }}

    /* ANSWER BOX */
    .card-answer {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 16px;
      font-size: 1.02rem;
      line-height: 1.85;
      color: #f8fafc;
    }}
    .ans-line {{
      margin-bottom: 8px;
    }}
    .ans-line:last-child {{
      margin-bottom: 0;
    }}

    /* TAG BADGES */
    .tag-badge {{
      background: rgba(56, 189, 248, 0.18) !important;
      color: #38bdf8 !important;
      font-weight: 700 !important;
      padding: 1px 6px !important;
      border-radius: 4px !important;
      margin-right: 4px !important;
      display: inline-block !important;
    }}

    /* INTERACTIVE ANSWER BLANKS */
    .kw-blank {{
      background: #1e293b;
      color: transparent;
      border-bottom: 2px dashed #f59e0b;
      padding: 1px 8px;
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
      display: inline-block;
      min-width: 50px;
      vertical-align: middle;
      transition: all 0.2s ease;
      text-align: center;
      margin: 0 2px;
    }}
    .kw-blank:hover {{
      background: #334155;
      border-color: #fbbf24;
    }}
    .kw-blank .blank-text {{
      visibility: hidden;
    }}
    .kw-blank.revealed {{
      background: #fef08a !important;
      color: #0f172a !important;
      border-bottom: 2px solid #eab308 !important;
      font-weight: 800 !important;
    }}
    .kw-blank.revealed .blank-text {{
      visibility: visible !important;
    }}

    /* PRINT STYLES */
    @media print {{
      body {{
        background: #fff !important;
        color: #000 !important;
        padding: 0 !important;
      }}
      header, .control-panel, .check-group, #btn-all-titles {{
        display: none !important;
      }}
      .word-card {{
        border: 1px solid #ccc !important;
        background: #fff !important;
        color: #000 !important;
        box-shadow: none !important;
        page-break-inside: avoid;
        margin-bottom: 16px !important;
      }}
      .card-question {{
        background: #f1f5f9 !important;
        color: #000 !important;
        border-left: 3px solid #000 !important;
      }}
      .card-answer {{
        background: #fafafa !important;
        color: #000 !important;
        border: 1px solid #ddd !important;
      }}
      .badge-text-hidden {{ display: none !important; }}
      .badge-text-revealed {{ display: inline !important; color: #000 !important; }}
      .kw-blank {{ background: none !important; color: #000 !important; border: none !important; }}
      .kw-blank .blank-text {{ visibility: visible !important; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- HEADER -->
    <header>
      <div class="header-top">
        <div class="main-title">
          <span>🏛️ 1단계(D-54~D-36) KICE 55개 코어 203문항 완벽 암기 단어장</span>
          <span class="dday-badge">D-54 (시험: 2026.11.28)</span>
        </div>
        <div class="header-links">
          <a href="kice_55_core_compressed.html" class="btn-link">🃏 앙키 플래시카드 앱</a>
          <button onclick="window.print()" class="btn-link" style="color:#a7f3d0; border-color:#10b981;">🖨️ A4 인쇄 / PDF 저장</button>
        </div>
      </div>
      
      <!-- DASHBOARD -->
      <div class="dashboard-grid">
        <div class="dash-box">
          <div class="dash-title">🎯 1회독 완수율 (초기 구조화)</div>
          <div class="dash-val" id="stat-r1">0 / 203 (0%)</div>
          <div class="progress-bar-bg"><div class="progress-bar-fill" id="fill-r1"></div></div>
        </div>
        <div class="dash-box">
          <div class="dash-title">🔥 2회독 완수율 (키워드 심화)</div>
          <div class="dash-val" id="stat-r2" style="color:#38bdf8;">0 / 203 (0%)</div>
          <div class="progress-bar-bg"><div class="progress-bar-fill" id="fill-r2" style="background:linear-gradient(90deg, #38bdf8, #818cf8);"></div></div>
        </div>
        <div class="dash-box">
          <div class="dash-title">🏆 3회독 완수율 (100% 완전 마스터)</div>
          <div class="dash-val" id="stat-r3" style="color:#fbbf24;">0 / 203 (0%)</div>
          <div class="progress-bar-bg"><div class="progress-bar-fill" id="fill-r3" style="background:linear-gradient(90deg, #f59e0b, #ef4444);"></div></div>
        </div>
      </div>
    </header>

    <!-- CONTROL PANEL -->
    <div class="control-panel">
      <div class="toolbar-row">
        <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
          <button class="btn-action" id="btn-all-titles" onclick="toggleAllTitleBadges()" style="background:#0284c7; color:#fff; border-color:#38bdf8; font-weight:800;">
            👁️ 전체 표제어 정답 보기
          </button>
          <button class="btn-action" id="btn-toggle-blind" onclick="toggleAllKwBlanks()">
            💡 본문 빈칸 정답 열기
          </button>
          <button class="btn-action" onclick="filterUnchecked()">
            🔥 미암기(0회독) 문항만 보기
          </button>
          <button class="btn-action" onclick="resetAllFilters()">
            🌟 전체 203문항 보기
          </button>
        </div>
        <div style="font-size:0.85rem; color:#94a3b8;">
          💡 팁: [빈칸] 배지를 클릭하면 해당 표제어가 열립니다!
        </div>
      </div>

      <!-- VIEW SELECTOR TABS -->
      <div style="display:flex; gap:10px; align-items:center; margin-top:4px;">
        <span style="font-size:0.82rem; font-weight:700; color:#38bdf8;">📅 18일 데일리 플랜:</span>
      </div>
      <div class="pill-tabs" id="day-pills">
        <button class="tab-pill active" onclick="filterByDay('all', this)">전체 Day</button>
      </div>

      <div style="display:flex; gap:10px; align-items:center; margin-top:2px;">
        <span style="font-size:0.82rem; font-weight:700; color:#f59e0b;">📚 8대 과목별 모아보기:</span>
      </div>
      <div class="pill-tabs" id="cat-pills">
        <button class="tab-pill active" onclick="filterByCat('all', this)">전체 과목 (203)</button>
        <button class="tab-pill" onclick="filterByCat('교육', this)">🎓 교육학 (33)</button>
        <button class="tab-pill" onclick="filterByCat('정신병리', this)">🧠 이상심리/DSM-5 (35)</button>
        <button class="tab-pill" onclick="filterByCat('가족', this)">👨‍👩‍👧 가족치료 (22)</button>
        <button class="tab-pill" onclick="filterByCat('심리검사', this)">📊 심리검사 (22)</button>
        <button class="tab-pill" onclick="filterByCat('진로', this)">🧭 진로상담 (18)</button>
        <button class="tab-pill" onclick="filterByCat('이론', this)">💡 상담이론·치료 (41)</button>
        <button class="tab-pill" onclick="filterByCat('위기', this)">🚨 위기·학폭·윤리 (22)</button>
      </div>
    </div>

    <!-- CARDS CONTAINER -->
    <div class="cards-container" id="cards-container">
      {full_cards_str}
    </div>
  </div>

  <script>
    const STORAGE_KEY = 'kice_phase1_checks';
    let checksData = {{}};

    // Populate Day Pills (1 to 18)
    const dayPillsContainer = document.getElementById('day-pills');
    for (let d = 1; d <= 18; d++) {{
      const b = document.createElement('button');
      b.className = 'tab-pill';
      b.innerText = `Day ${{String(d).padStart(2, '0')}}`;
      b.onclick = function() {{ filterByDay(d, this); }};
      dayPillsContainer.appendChild(b);
    }}

    // Title Blank Toggle
    function toggleTitleBadge(badge) {{
      badge.classList.toggle('blank-hidden');
      badge.classList.toggle('revealed');
    }}

    let isAllTitlesRevealed = false;
    function toggleAllTitleBadges() {{
      isAllTitlesRevealed = !isAllTitlesRevealed;
      const badges = document.querySelectorAll('.card-title-badge');
      badges.forEach(b => {{
        if (isAllTitlesRevealed) {{
          b.classList.remove('blank-hidden');
          b.classList.add('revealed');
        }} else {{
          b.classList.add('blank-hidden');
          b.classList.remove('revealed');
        }}
      }});
      const btn = document.getElementById('btn-all-titles');
      if (btn) {{
        btn.innerHTML = isAllTitlesRevealed ? '🔒 전체 빈칸으로 가리기' : '👁️ 전체 표제어 정답 보기';
      }}
    }}

    // Answer Blank Toggle
    function toggleKwBlank(el) {{
      el.classList.toggle('revealed');
    }}

    let isAllBlanksRevealed = false;
    function toggleAllKwBlanks() {{
      isAllBlanksRevealed = !isAllBlanksRevealed;
      const blanks = document.querySelectorAll('.kw-blank');
      blanks.forEach(b => {{
        if (isAllBlanksRevealed) {{
          b.classList.add('revealed');
        }} else {{
          b.classList.remove('revealed');
        }}
      }});
      const btn = document.getElementById('btn-toggle-blind');
      if (btn) {{
        btn.innerHTML = isAllBlanksRevealed ? '🔒 본문 빈칸 가리기' : '💡 본문 빈칸 정답 열기';
      }}
    }}

    // Checkbox & Round Persistence
    function loadSavedChecks() {{
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {{
        try {{
          checksData = JSON.parse(saved);
        }} catch(e) {{}}
      }}
      document.querySelectorAll('.chk-box').forEach(chk => {{
        const idx = chk.getAttribute('data-idx');
        const round = chk.getAttribute('data-round');
        if (checksData[idx] && checksData[idx]['r' + round]) {{
          chk.checked = true;
        }}
      }});
      updateDashboard();
    }}

    function handleCheckChange(chk) {{
      const idx = chk.getAttribute('data-idx');
      const round = chk.getAttribute('data-round');
      if (!checksData[idx]) checksData[idx] = {{}};
      checksData[idx]['r' + round] = chk.checked;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(checksData));
      updateDashboard();
    }}

    function updateDashboard() {{
      let r1Count = 0, r2Count = 0, r3Count = 0;
      const total = 203;
      for (let i = 0; i < total; i++) {{
        if (checksData[i]) {{
          if (checksData[i].r1) r1Count++;
          if (checksData[i].r2) r2Count++;
          if (checksData[i].r3) r3Count++;
        }}
      }}
      const pct1 = Math.round((r1Count / total) * 100);
      const pct2 = Math.round((r2Count / total) * 100);
      const pct3 = Math.round((r3Count / total) * 100);

      document.getElementById('stat-r1').innerText = `${{r1Count}} / ${{total}} (${{pct1}}%)`;
      document.getElementById('stat-r2').innerText = `${{r2Count}} / ${{total}} (${{pct2}}%)`;
      document.getElementById('stat-r3').innerText = `${{r3Count}} / ${{total}} (${{pct3}}%)`;

      document.getElementById('fill-r1').style.width = pct1 + '%';
      document.getElementById('fill-r2').style.width = pct2 + '%';
      document.getElementById('fill-r3').style.width = pct3 + '%';
    }}

    // Filtering Logic
    let curDay = 'all';
    let curCat = 'all';

    function filterByDay(day, btn) {{
      curDay = day;
      document.querySelectorAll('#day-pills .tab-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      applyCombinedFilter();
    }}

    function filterByCat(cat, btn) {{
      curCat = cat;
      document.querySelectorAll('#cat-pills .tab-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      applyCombinedFilter();
    }}

    function applyCombinedFilter() {{
      const cards = document.querySelectorAll('.word-card');
      cards.forEach(card => {{
        const cDay = card.getAttribute('data-day');
        const cCat = card.getAttribute('data-cat');
        const matchDay = (curDay === 'all' || String(cDay) === String(curDay));
        const matchCat = (curCat === 'all' || String(cCat) === String(curCat));
        if (matchDay && matchCat) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function filterUnchecked() {{
      const cards = document.querySelectorAll('.word-card');
      cards.forEach(card => {{
        const idx = card.getAttribute('data-idx');
        const isChecked = checksData[idx] && (checksData[idx].r1 || checksData[idx].r2 || checksData[idx].r3);
        if (!isChecked) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function resetAllFilters() {{
      curDay = 'all';
      curCat = 'all';
      document.querySelectorAll('.tab-pill').forEach(b => b.classList.remove('active'));
      document.querySelector('#day-pills .tab-pill').classList.add('active');
      document.querySelector('#cat-pills .tab-pill').classList.add('active');
      applyCombinedFilter();
    }}

    // Initialize
    loadSavedChecks();
  </script>
</body>
</html>
"""

with open(target_html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated Phase 1 Wordbook with USER-MATCHED [빈칸] BADGES at: {target_html_path}")
