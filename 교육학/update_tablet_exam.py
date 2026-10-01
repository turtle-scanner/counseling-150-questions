import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the examView block in HTML
pos_exam_start = text.find('<div id="examView"')
pos_main_end = text.find('</main>', pos_exam_start)
pos_exam_end = text.rfind('</div>', pos_exam_start, pos_main_end) + len('</div>')

exam_view_html = """    <!-- ============================================================ -->
    <!-- 📝 2027 KICE 실전 모의고사 풀이관 (태블릿 & 시험지 최적화 뷰어) -->
    <!-- ============================================================ -->
    <div id="examView" style="display: none;">
      <!-- KICE Official Exam Paper Banner -->
      <div class="kice-screen-exam-header" id="kiceScreenHeader">
        <div class="kice-paper-emblem">🏛️ 2027학년도 중등교사 임용후보자 선정경쟁시험</div>
        <div class="kice-paper-main-title" id="kiceScreenPeriodTitle">【 3교시 풀세트 : 1교시 교육학 + 2교시 전공 A + 3교시 전공 B 】</div>
        <div class="kice-paper-meta-box">
          <div class="kice-meta-student">수험번호 : ____________________ &nbsp;&nbsp;&nbsp; 성명 : ____________________</div>
          <div class="kice-meta-count">총 24문항 / 100점 만점 / KICE 4점 만점 칼채점 규격</div>
        </div>
      </div>

      <!-- Navigation Bar: Switch Rounds & Switch Periods & Themes -->
      <div class="exam-control-bar">
        <!-- Top Row: Round Switcher & Theme Toggle -->
        <div class="exam-control-row">
          <div class="exam-control-group">
            <span class="exam-control-label">📑 회차 선택:</span>
            <button class="exam-round-btn active" id="btnRound04" onclick="selectExamRound(4)">🔥 0906_04회 인터랙티브 실전 풀이관</button>
            <button class="exam-round-btn secondary" id="btnRoundRaw" onclick="toggleRawExamViewer()">📂 1~4회 & 10회 전체 원문 뷰어</button>
          </div>
          <div class="exam-control-group">
            <button class="theme-toggle-btn" id="btnExamTheme" onclick="toggleExamPaperTheme()">📄 백색 시험지 테마 전환</button>
          </div>
        </div>

        <!-- Middle Row: Period Navigation (Strict 3-Period Sequence: Rule 2) -->
        <div class="exam-period-nav" id="examPeriodNavRow">
          <button class="exam-period-pill active" id="btnSubAll" onclick="setExamPeriod('all')">📄 전체 24문항 풀세트 연속 보기</button>
          <button class="exam-period-pill" id="btnSubPed" onclick="setExamPeriod('pedagogy')">🏛️ 1교시 교육학 논술 (1문항 / 20점)</button>
          <button class="exam-period-pill" id="btnSubA" onclick="setExamPeriod('major_a')">🛋️ 2교시 전공상담 A형 (12문항 / 40점)</button>
          <button class="exam-period-pill" id="btnSubB" onclick="setExamPeriod('major_b')">🏥 3교시 전공상담 B형 (11문항 / 40점)</button>
        </div>

        <!-- Bottom Row: Tools & A4 Print -->
        <div class="exam-action-row" id="examActionRow">
          <div class="action-left">
            <button class="tool-action-btn" onclick="toggleAllSolutions(true)">📖 풀이과정 & 만점답안 전체 열기</button>
            <button class="tool-action-btn" onclick="toggleAllSolutions(false)">🔒 전체 접기</button>
            <button class="tool-action-btn" onclick="clearMyAnswers()">🧹 작성 답안 비우기</button>
          </div>
          <div class="action-right">
            <button class="print-action-btn paper" onclick="printKiceExamPaper(false)">🖨️ [실전 시험지] KICE 공식 A4 문제지 인쇄</button>
            <button class="print-action-btn solution" onclick="printKiceExamPaper(true)">🖨️ [공식 해설서] KICE 4점 만점 해설집 인쇄</button>
          </div>
        </div>
      </div>

      <!-- Interactive Exam Dynamic Question Container -->
      <div id="interactiveExamBox">
        <div id="examQuestionsContainer"></div>
      </div>

      <!-- Raw Markdown Viewer (Rounds 01~04, 10) -->
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

text = text[:pos_exam_start] + exam_view_html + text[pos_exam_end:]
print('Updated examView in HTML.')

# 2. Add Tablet and Paper Theme CSS to style section
tablet_css = """
    /* ============================================================ */
    /* 📱 태블릿 & KICE 실전 시험지 테마 스타일                     */
    /* ============================================================ */
    .kice-screen-exam-header {
      background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
      border: 2px solid #38bdf8;
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 20px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .kice-paper-emblem {
      font-size: 1.05rem;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }
    .kice-paper-main-title {
      font-size: 1.45rem;
      font-weight: 900;
      color: #38bdf8;
      margin-bottom: 12px;
      letter-spacing: 0.5px;
    }
    .kice-paper-meta-box {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      padding-top: 10px;
      border-top: 1px solid #334155;
      font-size: 0.95rem;
      color: #cbd5e1;
    }
    .kice-meta-student {
      font-weight: 700;
      color: #f1f5f9;
    }
    .kice-meta-count {
      font-weight: 600;
      color: #38bdf8;
    }

    .exam-control-bar {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 24px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }
    .exam-control-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding-bottom: 14px;
      border-bottom: 1px solid #1e293b;
      margin-bottom: 14px;
    }
    .exam-control-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .exam-control-label {
      font-size: 0.95rem;
      font-weight: 700;
      color: #94a3b8;
    }
    .theme-toggle-btn {
      padding: 8px 16px;
      background: #1e293b;
      border: 1.5px solid #e2e8f0;
      color: #f8fafc;
      border-radius: 8px;
      font-size: 0.92rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.2s;
    }
    .theme-toggle-btn:hover {
      background: #334155;
      border-color: #38bdf8;
    }

    .exam-period-nav {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }
    .exam-period-pill {
      padding: 9px 18px;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      color: #cbd5e1;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .exam-period-pill:hover {
      background: #334155;
      color: #fff;
    }
    .exam-period-pill.active {
      background: #0284c7;
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }

    .exam-action-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .exam-action-row .action-left, .exam-action-row .action-right {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tool-action-btn {
      padding: 8px 14px;
      border-radius: 6px;
      border: 1px solid #475569;
      background: #1e293b;
      color: #e2e8f0;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
    }
    .tool-action-btn:hover {
      background: #334155;
    }
    .print-action-btn {
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.92rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s;
    }
    .print-action-btn.paper {
      background: #1e293b;
      border: 1px solid #94a3b8;
      color: #f8fafc;
    }
    .print-action-btn.paper:hover {
      background: #334155;
    }
    .print-action-btn.solution {
      background: #d97706;
      border: 1px solid #f59e0b;
      color: #fff;
    }
    .print-action-btn.solution:hover {
      background: #b45309;
    }

    /* ============================================================ */
    /* 📄 백색 시험지 테마 (Paper White Theme)                      */
    /* ============================================================ */
    .kice-paper-theme #interactiveExamBox {
      background: #f8fafc;
      padding: 20px;
      border-radius: 12px;
      border: 2px solid #cbd5e1;
    }
    .kice-paper-theme .exam-qcard {
      background: #ffffff !important;
      border: 2px solid #1e293b !important;
      color: #0f172a !important;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    }
    .kice-paper-theme .exam-qcard-lead {
      color: #0f172a !important;
      font-weight: 700 !important;
    }
    .kice-paper-theme .exam-passage-box {
      background: #f8fafc !important;
      border: 1.5px solid #334155 !important;
      border-left: 5px solid #0284c7 !important;
    }
    .kice-paper-theme .passage-label {
      color: #0369a1 !important;
    }
    .kice-paper-theme .passage-text {
      color: #0f172a !important;
    }
    .kice-paper-theme .exam-directions-box {
      background: #fffbeb !important;
      border: 1.5px solid #d97706 !important;
      border-left: 5px solid #f59e0b !important;
    }
    .kice-paper-theme .directions-label {
      color: #b45309 !important;
    }
    .kice-paper-theme .directions-text {
      color: #78350f !important;
    }
    .kice-paper-theme .btn-open-draft-popup {
      background: linear-gradient(135deg, #0284c7, #0369a1) !important;
      border-color: #38bdf8 !important;
      color: #ffffff !important;
    }
    .kice-paper-theme .btn-toggle-solution {
      background: linear-gradient(135deg, #059669, #047857) !important;
      color: #ffffff !important;
    }

    /* Tablet Touch Optimizations */
    @media (min-width: 768px) and (max-width: 1366px) {
      .exam-qcard {
        padding: 22px;
      }
      .exam-passage-box {
        padding: 18px 22px;
      }
      .passage-text {
        font-size: 1.05rem;
        line-height: 1.8;
      }
      .btn-open-draft-popup {
        padding: 16px 22px;
        font-size: 1.1rem;
      }
      .draft-modal-content {
        max-height: 94vh;
      }
      .draft-ruled-textarea {
        font-size: 1.15rem;
        line-height: 2.2rem;
        min-height: 260px;
      }
    }
"""

pos_css_insert = text.find('/* ============================================================ */\n    /* ✍️ KICE 실전 서술형 답안지 팝업 모달')
if pos_css_insert != -1:
    text = text[:pos_css_insert] + tablet_css + '\n' + text[pos_css_insert:]
else:
    pos_style_close = text.find('</style>')
    text = text[:pos_style_close] + tablet_css + '\n' + text[pos_style_close:]

print('Added Tablet and Paper Theme CSS.')

# 3. Add toggleExamPaperTheme JS function
js_theme = """
    // Toggle Paper White vs Focus Dark Theme for Exam
    let isPaperTheme = false;
    function toggleExamPaperTheme() {
      isPaperTheme = !isPaperTheme;
      const view = document.getElementById('examView');
      const btn = document.getElementById('btnExamTheme');
      if (view) {
        view.classList.toggle('kice-paper-theme', isPaperTheme);
      }
      if (btn) {
        btn.textContent = isPaperTheme ? '🌙 다크 시험지 테마' : '📄 백색 시험지 테마';
        btn.style.background = isPaperTheme ? '#0284c7' : '#1e293b';
        btn.style.color = '#ffffff';
      }
    }
"""

pos_js_end = text.rfind('</script>')
text = text[:pos_js_end] + js_theme + '\n' + text[pos_js_end:]
print('Added toggleExamPaperTheme JS function.')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Saved index.html with tablet exam features! Size:', len(text))
