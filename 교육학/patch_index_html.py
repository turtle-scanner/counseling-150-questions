import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open('test_progress_html.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS rules right before </style>
css_additions = """
    /* ============================================================ */
    /* 🌟 핵심 150선 카드 뒤집기 및 인터랙티브 모의고사 전용 스타일 */
    /* ============================================================ */
    .btn-flip-action {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      margin: 14px 0 6px 0;
      padding: 12px 18px;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #fff;
      border: 1px solid #60a5fa;
      border-radius: 10px;
      font-size: 1.05rem;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
      transition: all 0.2s ease;
    }
    .btn-flip-action:hover {
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.6);
    }
    .btn-flip-action .flip-icon {
      font-size: 1.2rem;
    }

    /* Interactive Exam Layout */
    .exam-header-banner {
      background: linear-gradient(135deg, #0f172a, #1e293b);
      border: 2px solid #38bdf8;
      border-radius: 14px;
      padding: 22px 26px;
      margin-bottom: 22px;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.5);
    }
    .exam-header-title {
      font-size: 1.45rem;
      font-weight: 900;
      color: #38bdf8;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .exam-header-desc {
      font-size: 0.98rem;
      line-height: 1.65;
      color: #cbd5e1;
      margin-bottom: 18px;
    }
    .exam-round-tabs {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    .exam-round-btn {
      padding: 10px 18px;
      border-radius: 8px;
      border: 1px solid #38bdf8;
      background: #0369a1;
      color: #fff;
      font-size: 0.96rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .exam-round-btn:hover {
      background: #0284c7;
    }
    .exam-round-btn.secondary {
      background: #1e293b;
      border-color: #475569;
      color: #94a3b8;
    }
    .exam-round-btn.secondary:hover {
      background: #334155;
      color: #f1f5f9;
    }

    .period-subnav {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }
    .period-sub-btn {
      padding: 9px 16px;
      border-radius: 8px;
      border: 1px solid #334155;
      background: #1e293b;
      color: #cbd5e1;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .period-sub-btn:hover {
      background: #334155;
      color: #fff;
    }
    .period-sub-btn.active {
      background: #0284c7;
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }

    .exam-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 22px;
      padding: 14px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid #334155;
      border-radius: 10px;
    }
    .exam-toolbar .toolbar-left, .exam-toolbar .toolbar-right {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tool-btn {
      padding: 8px 14px;
      border-radius: 6px;
      border: 1px solid #475569;
      background: #1e293b;
      color: #e2e8f0;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tool-btn:hover {
      background: #334155;
    }
    .tool-btn.highlight {
      background: #d97706;
      border-color: #f59e0b;
      color: #fff;
    }
    .tool-btn.highlight:hover {
      background: #b45309;
    }

    .exam-qcard {
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 26px;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4);
      transition: border-color 0.2s;
    }
    .exam-qcard:hover {
      border-color: #475569;
    }
    .exam-qcard-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .exam-qcard-badges {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .qbadge-period {
      background: #1e3a8a;
      color: #93c5fd;
      border: 1px solid #3b82f6;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.85rem;
      font-weight: 700;
    }
    .qbadge-num {
      background: #047857;
      color: #a7f3d0;
      border: 1px solid #10b981;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.85rem;
      font-weight: 700;
    }
    .qbadge-type {
      background: #7c2d12;
      color: #fed7aa;
      border: 1px solid #f97316;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.85rem;
      font-weight: 700;
    }
    .qbadge-score {
      background: #701a75;
      color: #f5d0fe;
      border: 1px solid #c026d3;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.85rem;
      font-weight: 700;
    }
    .qbadge-domain {
      background: #1f2937;
      color: #e5e7eb;
      border: 1px solid #6b7280;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.85rem;
      font-weight: 700;
    }
    .exam-qcard-lead {
      font-size: 1.05rem;
      font-weight: 600;
      line-height: 1.65;
      color: #e2e8f0;
      margin-bottom: 16px;
    }
    .exam-passage-box {
      background: #1e293b;
      border-left: 4px solid #38bdf8;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 16px;
    }
    .passage-label {
      font-size: 0.95rem;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 10px;
    }
    .passage-text {
      font-size: 1rem;
      line-height: 1.75;
      color: #f1f5f9;
      white-space: pre-wrap;
    }
    .exam-directions-box {
      background: rgba(180, 83, 9, 0.15);
      border-left: 4px solid #f59e0b;
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 16px;
    }
    .directions-label {
      font-size: 0.95rem;
      font-weight: 800;
      color: #fbbf24;
      margin-bottom: 8px;
    }
    .directions-text {
      font-size: 0.95rem;
      line-height: 1.65;
      color: #fef3c7;
      white-space: pre-wrap;
    }
    .exam-draft-area {
      margin-bottom: 16px;
    }
    .draft-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .draft-title {
      font-size: 0.9rem;
      font-weight: 700;
      color: #94a3b8;
    }
    .draft-count {
      font-size: 0.85rem;
      color: #64748b;
    }
    .draft-textarea {
      width: 100%;
      min-height: 90px;
      background: #090e17;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 12px;
      color: #f8fafc;
      font-family: inherit;
      font-size: 0.95rem;
      line-height: 1.6;
      resize: vertical;
      box-sizing: border-box;
    }
    .draft-textarea:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
    }
    .btn-toggle-solution {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      padding: 12px 18px;
      background: linear-gradient(135deg, #059669, #047857);
      color: #fff;
      border: 1px solid #34d399;
      border-radius: 8px;
      font-size: 1.02rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.2s;
      margin-bottom: 12px;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
    }
    .btn-toggle-solution:hover {
      background: linear-gradient(135deg, #047857, #065f46);
      box-shadow: 0 6px 16px rgba(5, 150, 105, 0.5);
    }
    .exam-solution-card {
      background: #020617;
      border: 2px solid #10b981;
      border-radius: 10px;
      padding: 20px;
      margin-top: 12px;
    }
    .sol-step {
      border-radius: 8px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }
    .sol-step.step-1 {
      background: rgba(37, 99, 235, 0.12);
      border-left: 4px solid #3b82f6;
    }
    .sol-step.step-2 {
      background: rgba(147, 51, 234, 0.12);
      border-left: 4px solid #a855f7;
    }
    .sol-step.step-3 {
      background: rgba(225, 29, 72, 0.12);
      border-left: 4px solid #f43f5e;
    }
    .sol-step-title {
      font-size: 0.95rem;
      font-weight: 800;
      margin-bottom: 6px;
    }
    .sol-step.step-1 .sol-step-title { color: #60a5fa; }
    .sol-step.step-2 .sol-step-title { color: #c084fc; }
    .sol-step.step-3 .sol-step-title { color: #fb7185; }
    .sol-step-body {
      font-size: 0.95rem;
      line-height: 1.65;
      color: #f1f5f9;
    }
    .sol-model-answer {
      background: rgba(245, 158, 11, 0.12);
      border-left: 4px solid #fbbf24;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 14px;
    }
    .sol-model-title {
      font-size: 1.05rem;
      font-weight: 900;
      color: #f59e0b;
      margin-bottom: 8px;
    }
    .sol-model-body {
      font-size: 1rem;
      line-height: 1.7;
      color: #fef08a;
      white-space: pre-wrap;
    }
    .sol-rubric-box {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 14px 16px;
    }
    .sol-rubric-title {
      font-size: 0.92rem;
      font-weight: 800;
      color: #94a3b8;
      margin-bottom: 6px;
    }
    .sol-rubric-body {
      font-size: 0.9rem;
      line-height: 1.6;
      color: #cbd5e1;
    }

    /* Print View Container */
    #printCore150Container {
      display: none;
    }
"""

pos_style_close = html.find('</style>')
html = html[:pos_style_close] + css_additions + html[pos_style_close:]
print('Injected CSS additions.')

# 2. Update Header buttons
header_buttons_find = '<button class="btn active" id="btnModeCard" onclick="setMode(\'card\')">🎯 1장씩 실전 시험</button>'
header_buttons_replace = """<button class="btn active" id="btnModeCard" onclick="setMode('card')">🎯 1장씩 실전 시험</button>
      <button class="btn" id="btnModeCore150" onclick="openCore150Mode()">🌟 핵심 150선 플립카드</button>
      <button class="btn" onclick="printCore150PDF()">🖨️ 핵심 150선 PDF 인쇄</button>"""
html = html.replace(header_buttons_find, header_buttons_replace, 1)

# Update Exam Button label in header
html = html.replace("📝 0906 실전 모의고사 뷰어 (1~4회)", "📝 2027 모의고사 풀이관 (1~4회)", 1)
print('Updated header buttons.')

# 3. Update Filter Section pills
filter_pill_find = '<button class="pill active" onclick="setPeriodFilter(\'all\')">전체 (250)</button>'
filter_pill_replace = """<button class="pill active" onclick="setPeriodFilter('all')">전체 (250)</button>
        <button class="pill" id="pillCore150" onclick="setPeriodFilter('core150')">🌟 핵심키워드 150선 플립카드</button>"""
html = html.replace(filter_pill_find, filter_pill_replace, 1)
print('Updated filter pills.')

# 4. Update Flashcard front & back with flip buttons and core150 badge
card_badges_find = '<span class="tag-badge tag-freeze" id="cardBadgeFreeze" style="display:none;">🔥 2027 1순위 킬러</span>'
card_badges_replace = """<span class="tag-badge tag-freeze" id="cardBadgeFreeze" style="display:none;">🔥 2027 1순위 킬러</span>
              <span class="tag-badge tag-core150" id="cardBadgeCore150" style="display:none; background:#b45309; color:#fef3c7; border:1px solid #f59e0b;">🌟 핵심 150선</span>"""
html = html.replace(card_badges_find, card_badges_replace, 1)

# Add flip action button to cardFront
front_flip_find = '<div class="front-flip-hint">👉 화면을 클릭하거나 Spacebar를 누르면 3단 만점 루브릭이 열립니다</div>'
front_flip_replace = """<button class="btn-flip-action" onclick="event.stopPropagation(); flipCard()">
                <span class="flip-icon">🔄</span> 문제 뒤집기 (KICE 만점답안 확인)
              </button>
              <div class="front-flip-hint">👉 위 버튼을 누르거나 카드를 클릭하면 3단 만점 루브릭이 열립니다</div>"""
html = html.replace(front_flip_find, front_flip_replace, 1)

# Add flip back button to cardBack
back_title_find = '<div class="front-title" style="font-size: 1.4rem; margin-bottom: 16px;" id="cardTitleBack">백워드 설계 모형</div>'
back_title_replace = """<div class="front-title" style="font-size: 1.4rem; margin-bottom: 12px;" id="cardTitleBack">백워드 설계 모형</div>
              <button class="btn-flip-action" style="background: linear-gradient(135deg, #059669, #047857); border-color: #34d399; margin-bottom: 16px;" onclick="event.stopPropagation(); flipCard()">
                <span class="flip-icon">🔄</span> 문제로 다시 뒤집기
              </button>"""
html = html.replace(back_title_find, back_title_replace, 1)
print('Updated flashcard with flip action buttons.')

# 5. Replace examView content with the new interactive exam layout + raw exam box
exam_view_old = """    <!-- Exam Mode View -->
    <div id="examView" style="display: none;">
      <div class="matrix-title">📝 2027 KICE 실전 모의고사 전문 뷰어 (시험지 & 3단계 칼채점 해설지)</div>
      <p class="matrix-desc">
        2027 KICE 중등임용 실전 규격으로 제작된 0905_10회 및 0905_07회 3교시 풀세트 전문을 웹에서 바로 확인하고 답안을 인출하세요.
      </p>

      <div class="exam-nav">
        <button class="exam-tab-btn active" onclick="switchExamTab(0)">🔥 [NEW] 0906_04회 실전 문제지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(1)">🏆 [NEW] 0906_04회 칼채점 해설지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(2)">✨ 0906_03회 실전 문제지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(3)">🎯 0906_03회 칼채점 해설지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(4)">0906_02회 실전 문제지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(5)">0906_02회 칼채점 해설지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(6)">0906_01회 실전 문제지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(7)">0906_01회 칼채점 해설지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(8)">0905_10회 실전 문제지</button>
        <button class="exam-tab-btn" onclick="switchExamTab(9)">0905_10회 칼채점 해설지</button>
      </div>

      <div class="exam-content-box" id="examDisplayBox"></div>
    </div>"""

exam_view_new = """    <!-- Exam Mode View -->
    <div id="examView" style="display: none;">
      <!-- Exam Header Banner -->
      <div class="exam-header-banner">
        <div class="exam-header-title">
          <span>📝</span> 2027 KICE 중등임용 전문상담 실전 모의고사 풀이관
        </div>
        <p class="exam-header-desc">
          2027 KICE 실전 시험 시간표와 100% 동일한 3교시 풀세트 [1교시 교육학 논술 ➔ 2교시 전공상담 A형 ➔ 3교시 전공상담 B형] 인터랙티브 풀이관입니다.<br>
          800자 이상 실전 지문 분석부터 3단계 핵심 풀이과정(지문단서·핵심메커니즘·오답함정)과 🏆 KICE 4점 만점 공식 서술문 및 칼채점 루브릭을 웹에서 실시간 학습하세요.
        </p>

        <div class="exam-round-tabs">
          <button class="exam-round-btn" id="btnRound04" onclick="selectExamRound(4)">🔥 [최신] 0906_04회 인터랙티브 풀이관 (24문항 풀세트)</button>
          <button class="exam-round-btn secondary" id="btnRoundRaw" onclick="toggleRawExamViewer()">📑 1~4회 및 10회 전체 모의고사 원문 뷰어</button>
        </div>
      </div>

      <!-- Interactive Exam Container -->
      <div id="interactiveExamBox">
        <!-- Period Subnav (Strict 3-Period Rule: 1교시 ➔ 2교시 ➔ 3교시) -->
        <div class="period-subnav">
          <button class="period-sub-btn active" id="btnSubAll" onclick="setExamPeriod('all')">📄 전체 24문항 풀세트 연속 보기</button>
          <button class="period-sub-btn" id="btnSubPed" onclick="setExamPeriod('pedagogy')">🏛️ 1교시 교육학 논술 (1문항 / 20점)</button>
          <button class="period-sub-btn" id="btnSubA" onclick="setExamPeriod('major_a')">🛋️ 2교시 전공상담 A형 (12문항 / 40점)</button>
          <button class="period-sub-btn" id="btnSubB" onclick="setExamPeriod('major_b')">🏥 3교시 전공상담 B형 (11문항 / 40점)</button>
        </div>

        <!-- Exam Toolbar -->
        <div class="exam-toolbar">
          <div class="toolbar-left">
            <button class="tool-btn" onclick="toggleAllSolutions(true)">📖 풀이과정·정답 전체 열기</button>
            <button class="tool-btn" onclick="toggleAllSolutions(false)">🔒 전체 접기</button>
            <button class="tool-btn" onclick="clearMyAnswers()">🧹 작성 답안 초기화</button>
          </div>
          <div class="toolbar-right">
            <button class="tool-btn" onclick="printExamOnlyPaper()">🖨️ [문제지만] 실전 인쇄 (A4 시험지)</button>
            <button class="tool-btn highlight" onclick="printExamWithSolutions()">🖨️ [해설집] 풀이·정식답 포함 인쇄 (A4 해설서)</button>
          </div>
        </div>

        <!-- Dynamic Questions Render Area -->
        <div id="examQuestionsContainer"></div>
      </div>

      <!-- Raw Markdown Viewer (Round 01~04, 10) -->
      <div id="rawExamBox" style="display: none;">
        <div class="exam-nav">
          <button class="exam-tab-btn active" onclick="switchExamTab(0)">0906_04회 문제지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(1)">0906_04회 해설지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(2)">0906_03회 문제지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(3)">0906_03회 해설지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(4)">0906_02회 문제지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(5)">0906_02회 해설지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(6)">0906_01회 문제지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(7)">0906_01회 해설지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(8)">0905_10회 문제지</button>
          <button class="exam-tab-btn" onclick="switchExamTab(9)">0905_10회 해설지</button>
        </div>

        <div class="exam-content-box" id="examDisplayBox"></div>
      </div>
    </div>"""

html = html.replace(exam_view_old, exam_view_new, 1)
print('Replaced examView with interactive exam solver.')

# 6. Add Print Container for 150 Core Keywords before </body>
print_container = """
  <!-- Print Container for 150 Core Keywords -->
  <div id="printCore150Container"></div>
"""
html = html.replace('</body>', print_container + '\n</body>', 1)

# 7. JavaScript updates
js_functions = """
    // ============================================================
    // 🌟 핵심키워드 150선 및 인터랙티브 실전 모의고사 제어 함수
    // ============================================================
    let currentExamPeriod = 'all';
    let currentExamRound = 4;
    let isRawExamOpen = false;

    // 150 Core Keywords Mode
    function openCore150Mode() {
      setMode('card');
      setPeriodFilter('core150');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Print 150 Core Keywords as A4 Booklet
    function printCore150PDF() {
      const coreItems = allData.filter(item => Boolean(item.isCore150));
      const printBox = document.getElementById('printCore150Container');
      if (!printBox) return;

      let htmlContent = `
        <div style="padding: 20px; font-family: sans-serif;">
          <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 12px; margin-bottom: 18px;">
            <h1 style="font-size: 1.6rem; margin: 0 0 6px 0;">🟡 2027 KICE 전문상담 핵심키워드 150선 A4 암기장</h1>
            <div style="font-size: 0.95rem; color: #444;">1교시 교육학 핵심 38선 + 2교시 전공 A형 72선 + 3교시 전공 B형 40선 | KICE 만점 출제 기준 영구 동결</div>
          </div>
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem;">
            <thead>
              <tr style="background: #f1f5f9; border-top: 1.5px solid #000; border-bottom: 1.5px solid #000;">
                <th style="width: 8%; padding: 8px; border: 1px solid #cbd5e1; text-align: center;">No.</th>
                <th style="width: 15%; padding: 8px; border: 1px solid #cbd5e1; text-align: center;">교시/영역</th>
                <th style="width: 37%; padding: 8px; border: 1px solid #cbd5e1; text-align: left;">❓ KICE 실전 힌트 박멸 발문</th>
                <th style="width: 40%; padding: 8px; border: 1px solid #cbd5e1; text-align: left;">🏆 KICE 4점 만점 표준 서술문 & 핵심 메커니즘</th>
              </tr>
            </thead>
            <tbody>
      `;

      coreItems.forEach((item, idx) => {
        htmlContent += `
          <tr style="border-bottom: 1px solid #e2e8f0; page-break-inside: avoid; break-inside: avoid;">
            <td style="padding: 8px; border: 1px solid #e2e8f0; text-align: center; font-weight: bold;">${idx + 1}</td>
            <td style="padding: 8px; border: 1px solid #e2e8f0; text-align: center;">
              <div style="font-weight: bold; color: #1e3a8a;">${item.period}</div>
              <div style="color: #64748b; font-size: 0.8rem;">${item.domain}</div>
            </td>
            <td style="padding: 8px; border: 1px solid #e2e8f0;">
              <div style="font-weight: 800; color: #0f172a; margin-bottom: 4px;">${item.keywords}</div>
              <div style="line-height: 1.5; color: #334155;">${item.question}</div>
            </td>
            <td style="padding: 8px; border: 1px solid #e2e8f0; line-height: 1.55; color: #1e293b; white-space: pre-wrap;">${item.answer}</td>
          </tr>
        `;
      });

      htmlContent += `
            </tbody>
          </table>
        </div>
      `;

      printBox.innerHTML = htmlContent;
      document.body.classList.add('printing-core150');

      window.print();

      window.addEventListener('afterprint', function onAfterPrint() {
        document.body.classList.remove('printing-core150');
        window.removeEventListener('afterprint', onAfterPrint);
      });
    }

    // Render 2027 KICE Mock Exam 0906_04회 Interactive Solver
    function renderInteractiveExam() {
      const container = document.getElementById('examQuestionsContainer');
      if (!container || !window.examQuestions04) return;

      const items = examQuestions04.filter(q => {
        if (currentExamPeriod === 'all') return true;
        return q.periodKey === currentExamPeriod;
      });

      let html = '';
      items.forEach(q => {
        const savedDraft = localStorage.getItem('draft_04_' + q.id) || '';
        const charCount = savedDraft.length;

        html += `
          <div class="exam-qcard" id="qcard_${q.id}">
            <div class="exam-qcard-header">
              <div class="exam-qcard-badges">
                <span class="qbadge-period">${q.period}</span>
                <span class="qbadge-num">문항 ${q.qnum}번</span>
                <span class="qbadge-type">${q.qtype}</span>
                <span class="qbadge-score">${q.score}점</span>
                <span class="qbadge-domain">${q.domain}</span>
              </div>
            </div>

            <div class="exam-qcard-lead">${q.lead}</div>

            <div class="exam-passage-box">
              <div class="passage-label">📋 [실전 사례 지문 / 제시문]</div>
              <div class="passage-text">${q.passage}</div>
            </div>

            ${q.directions ? `
            <div class="exam-directions-box">
              <div class="directions-label">📝 [작성 방법]</div>
              <div class="directions-text">${q.directions}</div>
            </div>
            ` : ''}

            <div class="exam-draft-area">
              <div class="draft-header">
                <span class="draft-title">✍️ 수험생 실전 인출 답안지 (자동 저장)</span>
                <span class="draft-count" id="count_${q.id}">${charCount}자</span>
              </div>
              <textarea class="draft-textarea" id="draft_${q.id}" placeholder="시험장 실전 인출처럼 답안을 직접 작성해 보세요..." oninput="onDraftInput('${q.id}')">${savedDraft}</textarea>
            </div>

            <button class="btn-toggle-solution" onclick="toggleExamSolution('${q.id}')">
              <span>🔍</span> 3단계 풀이과정 & 🏆 KICE 만점 정식답안 보기 (열기/닫기)
            </button>

            <div class="exam-solution-card" id="sol_${q.id}" style="display: none;">
              <div class="sol-step step-1">
                <div class="sol-step-title">📌 [1단계 : 현상학적 지문 단서 분석]</div>
                <div class="sol-step-body">${q.step1}</div>
              </div>

              <div class="sol-step step-2">
                <div class="sol-step-title">⚙️ [2단계 : 핵심 이론 메커니즘 & 학술 원리]</div>
                <div class="sol-step-body">${q.step2}</div>
              </div>

              <div class="sol-step step-3">
                <div class="sol-step-title">⚠️ [3단계 : 오답 함정 피하기 (채점관 칼채점 포인트)]</div>
                <div class="sol-step-body">${q.step3}</div>
              </div>

              <div class="sol-model-answer">
                <div class="sol-model-title">🏆 [KICE 공식 정답 & 만점 표준 서술문]</div>
                <div class="sol-model-body">${q.answer}</div>
              </div>

              <div class="sol-rubric-box">
                <div class="sol-rubric-title">📊 [1:1 세부 채점 기준표 (Rubric)]</div>
                <div class="sol-rubric-body">${q.rubric}</div>
              </div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Toggle specific exam question solution
    function toggleExamSolution(id) {
      const el = document.getElementById('sol_' + id);
      if (!el) return;
      el.style.display = (el.style.display === 'none') ? 'block' : 'none';
    }

    // Toggle all solutions
    function toggleAllSolutions(open) {
      const cards = document.querySelectorAll('.exam-solution-card');
      cards.forEach(c => {
        c.style.display = open ? 'block' : 'none';
      });
    }

    // Real-time draft input and auto-save
    function onDraftInput(id) {
      const textarea = document.getElementById('draft_' + id);
      const countEl = document.getElementById('count_' + id);
      if (!textarea) return;
      const text = textarea.value;
      if (countEl) countEl.textContent = `${text.length}자`;
      localStorage.setItem('draft_04_' + id, text);
    }

    // Clear student answers
    function clearMyAnswers() {
      if (!confirm('작성하신 모의고사 답안을 모두 초기화하시겠습니까?')) return;
      if (window.examQuestions04) {
        examQuestions04.forEach(q => {
          localStorage.removeItem('draft_04_' + q.id);
          const ta = document.getElementById('draft_' + q.id);
          if (ta) ta.value = '';
          const countEl = document.getElementById('count_' + q.id);
          if (countEl) countEl.textContent = '0자';
        });
      }
    }

    // Filter Exam Period (Strict 3-Period Sequence)
    function setExamPeriod(period) {
      currentExamPeriod = period;
      document.getElementById('btnSubAll').classList.toggle('active', period === 'all');
      document.getElementById('btnSubPed').classList.toggle('active', period === 'pedagogy');
      document.getElementById('btnSubA').classList.toggle('active', period === 'major_a');
      document.getElementById('btnSubB').classList.toggle('active', period === 'major_b');
      renderInteractiveExam();
    }

    // Print Exam Paper Only Mode (for offline test)
    function printExamOnlyPaper() {
      document.body.classList.remove('printing-exam-solution', 'printing-core150');
      document.body.classList.add('printing-exam-paper');
      window.print();
      window.addEventListener('afterprint', function onAfter() {
        document.body.classList.remove('printing-exam-paper');
        window.removeEventListener('afterprint', onAfter);
      });
    }

    // Print Exam With Complete Solutions Mode
    function printExamWithSolutions() {
      toggleAllSolutions(true);
      document.body.classList.remove('printing-exam-paper', 'printing-core150');
      document.body.classList.add('printing-exam-solution');
      window.print();
      window.addEventListener('afterprint', function onAfter() {
        document.body.classList.remove('printing-exam-solution');
        window.removeEventListener('afterprint', onAfter);
      });
    }

    // Switch Exam Round / Viewer Mode
    function selectExamRound(round) {
      currentExamRound = round;
      isRawExamOpen = false;
      document.getElementById('interactiveExamBox').style.display = 'block';
      document.getElementById('rawExamBox').style.display = 'none';
      document.getElementById('btnRound04').classList.remove('secondary');
      document.getElementById('btnRoundRaw').classList.add('secondary');
      renderInteractiveExam();
    }

    function toggleRawExamViewer() {
      isRawExamOpen = true;
      document.getElementById('interactiveExamBox').style.display = 'none';
      document.getElementById('rawExamBox').style.display = 'block';
      document.getElementById('btnRound04').classList.add('secondary');
      document.getElementById('btnRoundRaw').classList.remove('secondary');
      switchExamTab(0);
    }
"""

# In setPeriodFilter, add core150 support
set_period_old = """    function setPeriodFilter(period) {
      currentPeriod = period;
      const pills = document.querySelectorAll('#periodFilters .pill');
      pills.forEach(p => {
        if (
          (period === 'all' && p.textContent.includes('전체')) ||
          (period === 'pedagogy' && p.textContent.includes('교육학')) ||
          (period === 'major_a' && p.textContent.includes('전공 A')) ||
          (period === 'major_b' && p.textContent.includes('전공 B')) ||
          (period === 'starred' && p.textContent.includes('북마크')) ||
          (period === 'freeze55' && p.textContent.includes('55선')) ||
          (period === 'unknown' && p.textContent.includes('몰라요')) ||
          (period === 'confused' && p.textContent.includes('헷갈려요')) ||
          (period === 'known' && p.textContent.includes('완벽암기'))
        ) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });
      applyFilter();
    }"""

set_period_new = """    function setPeriodFilter(period) {
      currentPeriod = period;
      const pills = document.querySelectorAll('#periodFilters .pill');
      pills.forEach(p => {
        if (
          (period === 'all' && p.textContent.includes('전체')) ||
          (period === 'core150' && p.textContent.includes('150선')) ||
          (period === 'pedagogy' && p.textContent.includes('교육학')) ||
          (period === 'major_a' && p.textContent.includes('전공 A')) ||
          (period === 'major_b' && p.textContent.includes('전공 B')) ||
          (period === 'starred' && p.textContent.includes('북마크')) ||
          (period === 'freeze55' && p.textContent.includes('55선')) ||
          (period === 'unknown' && p.textContent.includes('몰라요')) ||
          (period === 'confused' && p.textContent.includes('헷갈려요')) ||
          (period === 'known' && p.textContent.includes('완벽암기'))
        ) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });
      applyFilter();
    }"""

html = html.replace(set_period_old, set_period_new, 1)

# In applyFilter, add core150 logic
apply_filter_old = """      filteredItems = allData.filter(item => {
        let matches = true;
        if (currentPeriod === 'pedagogy') matches = item.period.includes('교육학');
        else if (currentPeriod === 'major_a') matches = item.period.includes('전공 A');
        else if (currentPeriod === 'major_b') matches = item.period.includes('전공 B');
        else if (currentPeriod === 'starred') matches = starred.has(item.id);
        else if (currentPeriod === 'freeze55') matches = isFreezeItem(item);
        else if (currentPeriod === 'unknown') matches = (mastery[item.id] === 'unknown');
        else if (currentPeriod === 'confused') matches = (mastery[item.id] === 'confused');
        else if (currentPeriod === 'known') matches = (mastery[item.id] === 'known');"""

apply_filter_new = """      filteredItems = allData.filter(item => {
        let matches = true;
        if (currentPeriod === 'core150') matches = Boolean(item.isCore150);
        else if (currentPeriod === 'pedagogy') matches = item.period.includes('교육학');
        else if (currentPeriod === 'major_a') matches = item.period.includes('전공 A');
        else if (currentPeriod === 'major_b') matches = item.period.includes('전공 B');
        else if (currentPeriod === 'starred') matches = starred.has(item.id);
        else if (currentPeriod === 'freeze55') matches = isFreezeItem(item);
        else if (currentPeriod === 'unknown') matches = (mastery[item.id] === 'unknown');
        else if (currentPeriod === 'confused') matches = (mastery[item.id] === 'confused');
        else if (currentPeriod === 'known') matches = (mastery[item.id] === 'known');"""

html = html.replace(apply_filter_old, apply_filter_new, 1)

# In renderCardView, update badge display for core150
render_card_old = """      document.getElementById('cardBadgeId').textContent = `#${String(item.id).padStart(3, '0')} / 300`;
      document.getElementById('cardBadgePeriod').textContent = item.period;
      document.getElementById('cardBadgeDomain').textContent = item.domain;
      document.getElementById('cardBadgeFreeze').style.display = isFreezeItem(item) ? 'inline-block' : 'none';"""

render_card_new = """      if (currentPeriod === 'core150') {
        document.getElementById('cardBadgeId').textContent = `🌟 핵심 150선: #${currentIndex + 1} / ${filteredItems.length}`;
      } else {
        document.getElementById('cardBadgeId').textContent = `#${String(item.id).padStart(3, '0')} / 300`;
      }
      document.getElementById('cardBadgePeriod').textContent = item.period;
      document.getElementById('cardBadgeDomain').textContent = item.domain;
      document.getElementById('cardBadgeFreeze').style.display = isFreezeItem(item) ? 'inline-block' : 'none';
      const badgeCore = document.getElementById('cardBadgeCore150');
      if (badgeCore) badgeCore.style.display = item.isCore150 ? 'inline-block' : 'none';"""

html = html.replace(render_card_old, render_card_new, 1)

# In setMode, when switching to exam, render interactive exam
set_mode_old = "document.getElementById('examView').style.display = (mode === 'exam') ? 'block' : 'none';"
set_mode_new = """document.getElementById('examView').style.display = (mode === 'exam') ? 'block' : 'none';
      if (mode === 'exam') {
        renderInteractiveExam();
      }"""
html = html.replace(set_mode_old, set_mode_new, 1)

# Inject the new JS functions right before DOMContentLoaded or end of script
pos_doc_load = html.find('document.addEventListener(\'DOMContentLoaded\'')
if pos_doc_load != -1:
    html = html[:pos_doc_load] + js_functions + '\n' + html[pos_doc_load:]
else:
    pos_script_end = html.rfind('</script>')
    html = html[:pos_script_end] + js_functions + '\n' + html[pos_script_end:]

print('Injected JS functions.')

# Save to target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully written updated index.html! Final size:', len(html))
