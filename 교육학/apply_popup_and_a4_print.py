import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

print('Loaded index.html, size:', len(html))

# 1. Add Popup Modal and KICE A4 Print Styles to CSS
modal_and_print_css = """
    /* ============================================================ */
    /* ✍️ KICE 실전 서술형 답안지 팝업 모달 & A4 실전 시험지 스타일   */
    /* ============================================================ */
    .exam-draft-bar {
      margin: 14px 0 16px 0;
    }
    .btn-open-draft-popup {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      padding: 13px 20px;
      background: linear-gradient(135deg, #1e293b, #0f172a);
      border: 1.5px solid #38bdf8;
      border-radius: 10px;
      color: #f8fafc;
      font-size: 1.02rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
      transition: all 0.2s ease;
    }
    .btn-open-draft-popup:hover {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border-color: #7dd3fc;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(56, 189, 248, 0.35);
    }
    .draft-status-pill {
      font-size: 0.82rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 999px;
      background: #334155;
      color: #94a3b8;
      border: 1px solid #475569;
    }
    .draft-status-pill.done {
      background: #065f46;
      color: #a7f3d0;
      border-color: #10b981;
    }

    /* Modal Overlay & Dialog */
    .draft-modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.78);
      backdrop-filter: blur(8px);
      z-index: 999999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      box-sizing: border-box;
    }
    .draft-modal-content {
      width: 100%;
      max-width: 860px;
      max-height: 92vh;
      background: #0b1120;
      border: 2px solid #38bdf8;
      border-radius: 16px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalFadeIn 0.22s ease-out;
    }
    @keyframes modalFadeIn {
      from { opacity: 0; transform: scale(0.96) translateY(10px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }
    .draft-modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 24px;
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
    }
    .draft-modal-title {
      font-size: 1.25rem;
      font-weight: 900;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .draft-modal-close {
      background: none;
      border: none;
      font-size: 1.5rem;
      color: #94a3b8;
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 6px;
      transition: all 0.15s;
    }
    .draft-modal-close:hover {
      background: #1e293b;
      color: #f8fafc;
    }

    /* Modal Reference Section */
    .draft-modal-reference {
      background: #0f172a;
      border-bottom: 1px solid #334155;
    }
    .modal-ref-toggle {
      padding: 12px 24px;
      font-size: 0.95rem;
      font-weight: 700;
      color: #f59e0b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(245, 158, 11, 0.08);
      user-select: none;
    }
    .modal-ref-toggle:hover {
      background: rgba(245, 158, 11, 0.15);
    }
    .modal-passage-content {
      padding: 16px 24px;
      max-height: 220px;
      overflow-y: auto;
      background: #080d1a;
      border-top: 1px solid #1e293b;
      font-size: 0.92rem;
      line-height: 1.65;
      color: #cbd5e1;
    }
    .modal-ref-lead {
      font-weight: 700;
      color: #e2e8f0;
      margin-bottom: 10px;
    }
    .modal-ref-passage {
      background: #131d31;
      padding: 12px 14px;
      border-radius: 6px;
      border-left: 3px solid #38bdf8;
      margin-bottom: 10px;
      white-space: pre-wrap;
      color: #f1f5f9;
    }
    .modal-ref-directions {
      background: rgba(180, 83, 9, 0.15);
      padding: 10px 14px;
      border-radius: 6px;
      border-left: 3px solid #f59e0b;
      white-space: pre-wrap;
      color: #fef08a;
    }

    /* Modal Ruled Writing Body */
    .draft-modal-body {
      padding: 20px 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }
    .draft-ruled-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .ruled-badge {
      font-size: 0.85rem;
      font-weight: 800;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid #0284c7;
    }
    .ruled-count {
      font-size: 0.88rem;
      color: #94a3b8;
    }
    .draft-ruled-textarea {
      flex: 1;
      width: 100%;
      min-height: 220px;
      box-sizing: border-box;
      background: #070d19;
      border: 1.5px solid #334155;
      border-radius: 10px;
      padding: 16px 18px;
      font-family: inherit;
      font-size: 1.05rem;
      line-height: 2rem;
      color: #f8fafc;
      resize: vertical;
      background-image: linear-gradient(transparent, transparent 1.95rem, rgba(51, 65, 85, 0.6) 2rem);
      background-size: 100% 2rem;
    }
    .draft-ruled-textarea:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25);
    }

    /* Modal Solution Peek */
    .modal-sol-box {
      margin: 0 24px 16px 24px;
      padding: 16px;
      background: #020617;
      border: 1.5px solid #10b981;
      border-radius: 10px;
      max-height: 200px;
      overflow-y: auto;
      animation: modalFadeIn 0.2s ease;
    }
    .modal-sol-title {
      font-size: 0.98rem;
      font-weight: 800;
      color: #34d399;
      margin-bottom: 8px;
    }
    .modal-sol-content {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #f1f5f9;
      white-space: pre-wrap;
    }

    /* Modal Footer Actions */
    .draft-modal-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 24px;
      background: #0f172a;
      border-top: 1px solid #1e293b;
      gap: 12px;
      flex-wrap: wrap;
    }
    .modal-footer-left {
      display: flex;
      gap: 10px;
    }
    .modal-btn-sol {
      padding: 9px 15px;
      background: #065f46;
      color: #a7f3d0;
      border: 1px solid #10b981;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.15s;
    }
    .modal-btn-sol:hover {
      background: #047857;
      color: #fff;
    }
    .modal-btn-clear {
      padding: 9px 14px;
      background: #334155;
      color: #cbd5e1;
      border: 1px solid #475569;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
    }
    .modal-btn-clear:hover {
      background: #475569;
      color: #fff;
    }
    .modal-btn-save {
      padding: 10px 22px;
      background: #0284c7;
      color: #fff;
      border: 1px solid #38bdf8;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.95rem;
      cursor: pointer;
      transition: all 0.15s;
    }
    .modal-btn-save:hover {
      background: #0369a1;
    }

    /* KICE A4 Exam Print Dedicated Container */
    #kicePrintExamContainer {
      display: none;
    }

    /* ============================================================ */
    /* 🖨️ KICE 중등임용 실전 문제지 A4 규격 인쇄 스타일             */
    /* ============================================================ */
    @media print {
      @page {
        size: A4 portrait;
        margin: 14mm 12mm 14mm 12mm;
      }
      body {
        background: #fff !important;
        color: #000 !important;
        font-family: 'Batang', 'Apple SD Gothic Neo', 'Malgun Gothic', serif !important;
      }

      /* Hide all web components */
      .sticky-tablet-font-bar, header, .filter-wrapper, .top-dashboard, .top-action-bar,
      .exam-header-banner, .period-subnav, .exam-toolbar, .btn-toggle-solution,
      .btn-flip-action, .cheer-box, footer, #rawExamBox, #draftModal,
      #flashcardView, #listView, #matrixView, #interactiveExamBox {
        display: none !important;
      }

      /* Mode 1: KICE Paper Print */
      body.printing-kice-paper #kicePrintExamContainer {
        display: block !important;
        position: static !important;
        width: 100% !important;
      }

      /* Mode 2: Core 150 Print */
      body.printing-core150 #printCore150Container {
        display: block !important;
        position: static !important;
        width: 100% !important;
      }

      /* Paper Header */
      .kice-paper-header {
        border-bottom: 2px solid #000;
        padding-bottom: 8px;
        margin-bottom: 16px;
        text-align: center;
      }
      .kice-paper-title-main {
        font-size: 1.4rem;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 4px;
      }
      .kice-paper-period-title {
        font-size: 1.15rem;
        font-weight: 800;
        margin-bottom: 8px;
      }
      .kice-paper-meta-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.95rem;
        padding-top: 4px;
        border-top: 1px solid #000;
      }

      /* Question Card in Paper */
      .kice-paper-qcard {
        border: 1px solid #000;
        padding: 14px;
        margin-bottom: 18px;
        page-break-inside: avoid;
        break-inside: avoid;
      }
      .kice-paper-qhead {
        font-size: 1.05rem;
        font-weight: 800;
        margin-bottom: 8px;
        line-height: 1.5;
      }
      .kice-paper-passage {
        border: 1.5px solid #000;
        padding: 10px 12px;
        margin-bottom: 10px;
        background: #fff;
        font-size: 0.95rem;
        line-height: 1.65;
        white-space: pre-wrap;
      }
      .kice-paper-directions {
        border: 1px solid #333;
        padding: 8px 12px;
        margin-bottom: 10px;
        background: #fdfdfd;
        font-size: 0.92rem;
        line-height: 1.55;
        white-space: pre-wrap;
      }
      .kice-paper-ans-box {
        border: 1px dashed #666;
        padding: 8px 12px;
        margin-top: 8px;
        background: #fafafa;
      }
      .kice-paper-ans-label {
        font-size: 0.85rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 6px;
      }
      .kice-paper-lines {
        min-height: 80px;
        background-image: repeating-linear-gradient(transparent, transparent 22px, #ccc 23px);
        background-size: 100% 23px;
      }

      /* Solution Mode Styling */
      .kice-paper-sol-box {
        border-top: 1.5px solid #000;
        margin-top: 10px;
        padding-top: 10px;
      }
      .kice-sol-step {
        margin-bottom: 8px;
        font-size: 0.9rem;
        line-height: 1.55;
      }
      .kice-sol-ans {
        border: 1.5px solid #000;
        padding: 8px;
        margin: 8px 0;
        background: #f8f8f8;
        font-size: 0.92rem;
        line-height: 1.6;
        white-space: pre-wrap;
      }
      .kice-sol-rubric {
        font-size: 0.88rem;
        color: #333;
        border-top: 1px solid #999;
        padding-top: 4px;
      }
    }
"""

# Inject this CSS before </style>
pos_style_end = html.find('</style>')
html = html[:pos_style_end] + modal_and_print_css + '\n' + html[pos_style_end:]
print('Injected Modal and A4 Print CSS.')

# 2. Add Modal Dialog HTML and kicePrintExamContainer before </body>
modal_and_print_html = """
  <!-- ✍️ KICE 실전 서술형 답안지 팝업 모달 -->
  <div id="draftModal" class="draft-modal-overlay" style="display: none;" onclick="onModalBackdropClick(event)">
    <div class="draft-modal-content" onclick="event.stopPropagation()">
      <div class="draft-modal-header">
        <div class="draft-modal-title" id="modalTitle">
          <span>✍️</span> [2교시 전공상담 A형] 1번 실전 답안지
        </div>
        <button class="draft-modal-close" onclick="closeDraftModal()">✕</button>
      </div>

      <div class="draft-modal-reference">
        <div class="modal-ref-toggle" onclick="toggleModalPassage()">
          <span>📋 [실전 문제 지문 및 작성 방법 확인하기]</span>
          <span id="modalPassageToggleIcon">▼ 열기</span>
        </div>
        <div id="modalPassageBox" class="modal-passage-content" style="display: none;">
          <div class="modal-ref-lead" id="modalLeadText"></div>
          <div class="modal-ref-passage" id="modalPassageText"></div>
          <div class="modal-ref-directions" id="modalDirectionsText"></div>
        </div>
      </div>

      <div class="draft-modal-body">
        <div class="draft-ruled-header">
          <span class="ruled-badge">KICE 실전 서술형 답안지 규격</span>
          <span class="ruled-count" id="modalCharCount">0자 / 권장 150~250자</span>
        </div>
        <textarea id="modalTextarea" class="draft-ruled-textarea" placeholder="이곳에 실전 시험처럼 정식 답안을 작성하세요... (자동 저장됩니다)" oninput="onModalInput()"></textarea>
      </div>

      <div id="modalSolutionBox" class="modal-sol-box" style="display: none;">
        <div class="modal-sol-title">🏆 [KICE 공식 정답 및 칼채점 루브릭]</div>
        <div id="modalSolutionContent" class="modal-sol-content"></div>
      </div>

      <div class="draft-modal-footer">
        <div class="modal-footer-left">
          <button class="modal-btn-sol" onclick="toggleModalSolution()">💡 이 문제 만점답안 확인</button>
          <button class="modal-btn-clear" onclick="clearModalDraft()">🧹 답안 비우기</button>
        </div>
        <button class="modal-btn-save" onclick="closeDraftModal()">💾 작성 완료 및 닫기</button>
      </div>
    </div>
  </div>

  <!-- KICE A4 Exam Print Container -->
  <div id="kicePrintExamContainer"></div>
"""

html = html.replace('</body>', modal_and_print_html + '\n</body>', 1)
print('Injected Modal and Print containers into HTML.')

# 3. Update Toolbar buttons in examView to highlight the A4 시험지 인쇄
old_toolbar_right = """          <div class="toolbar-right">
            <button class="tool-btn" onclick="printExamOnlyPaper()">🖨️ [문제지만] 실전 인쇄 (A4 시험지)</button>
            <button class="tool-btn highlight" onclick="printExamWithSolutions()">🖨️ [해설집] 풀이·정식답 포함 인쇄 (A4 해설서)</button>
          </div>"""

new_toolbar_right = """          <div class="toolbar-right">
            <button class="tool-btn" onclick="printKiceExamPaper(false)">🖨️ [실전 시험지] KICE 공식 A4 문제지 인쇄</button>
            <button class="tool-btn highlight" onclick="printKiceExamPaper(true)">🖨️ [공식 해설서] KICE 4점 만점 해설집 인쇄</button>
          </div>"""

html = html.replace(old_toolbar_right, new_toolbar_right, 1)
print('Updated exam toolbar print buttons.')

# 4. Update renderInteractiveExam to use popup button instead of plain textarea
old_draft_area = """            <div class="exam-draft-area">
              <div class="draft-header">
                <span class="draft-title">✍️ 수험생 실전 인출 답안지 (자동 저장)</span>
                <span class="draft-count" id="count_${q.id}">${charCount}자</span>
              </div>
              <textarea class="draft-textarea" id="draft_${q.id}" placeholder="시험장 실전 인출처럼 답안을 직접 작성해 보세요..." oninput="onDraftInput('${q.id}')">${savedDraft}</textarea>
            </div>"""

new_draft_area = """            <div class="exam-draft-bar">
              <button class="btn-open-draft-popup" onclick="openDraftPopup('${q.id}')">
                <span>✍️ [실전 답안 작성] KICE 서술형 답안지 팝업 열기</span>
                <span class="draft-status-pill ${savedDraft ? 'done' : ''}" id="pill_${q.id}">
                  ${savedDraft ? '작성 완료 (' + charCount + '자)' : '미작성 (클릭하여 작성)'}
                </span>
              </button>
            </div>"""

html = html.replace(old_draft_area, new_draft_area, 1)
print('Updated question cards to use popup trigger button.')

# 5. Add JavaScript functions for Popup Modal and KICE A4 Paper Generation
js_popup_and_print = """
    // ============================================================
    // ✍️ KICE 답안지 팝업 모달 & A4 실전 시험지 생성 스크립트
    // ============================================================
    let activeModalQuestionId = null;

    // Open Draft Popup Modal
    function openDraftPopup(qid) {
      if (typeof examQuestions04 === 'undefined') return;
      const q = examQuestions04.find(item => item.id === qid);
      if (!q) return;

      activeModalQuestionId = qid;
      const modal = document.getElementById('draftModal');
      const title = document.getElementById('modalTitle');
      const lead = document.getElementById('modalLeadText');
      const passage = document.getElementById('modalPassageText');
      const directions = document.getElementById('modalDirectionsText');
      const textarea = document.getElementById('modalTextarea');
      const countEl = document.getElementById('modalCharCount');
      const solBox = document.getElementById('modalSolutionBox');

      title.innerHTML = `<span>✍️</span> [${q.period}] 문항 ${q.qnum}번 (${q.score}점 / ${q.qtype}) 답안지`;
      lead.textContent = q.lead;
      passage.textContent = q.passage;
      directions.textContent = q.directions || '';
      directions.style.display = q.directions ? 'block' : 'none';

      const saved = localStorage.getItem('draft_04_' + qid) || '';
      textarea.value = saved;
      countEl.textContent = `${saved.length}자 / 권장 150~250자`;

      // Hide solution box on open
      solBox.style.display = 'none';

      // Hide passage box by default (compact)
      document.getElementById('modalPassageBox').style.display = 'none';
      document.getElementById('modalPassageToggleIcon').textContent = '▼ 열기';

      modal.style.display = 'flex';
      setTimeout(() => textarea.focus(), 100);
    }

    // Close Modal
    function closeDraftModal() {
      const modal = document.getElementById('draftModal');
      if (modal) modal.style.display = 'none';
      activeModalQuestionId = null;
    }

    // Modal backdrop click
    function onModalBackdropClick(event) {
      if (event.target.id === 'draftModal') {
        closeDraftModal();
      }
    }

    // Toggle Passage inside Modal
    function toggleModalPassage() {
      const box = document.getElementById('modalPassageBox');
      const icon = document.getElementById('modalPassageToggleIcon');
      if (!box) return;
      const isOpen = box.style.display === 'block';
      box.style.display = isOpen ? 'none' : 'block';
      icon.textContent = isOpen ? '▼ 열기' : '▲ 접기';
    }

    // Input in Modal
    function onModalInput() {
      if (!activeModalQuestionId) return;
      const textarea = document.getElementById('modalTextarea');
      const countEl = document.getElementById('modalCharCount');
      const text = textarea.value;
      countEl.textContent = `${text.length}자 / 권장 150~250자`;

      // Save to localStorage
      localStorage.setItem('draft_04_' + activeModalQuestionId, text);

      // Update card pill
      const pill = document.getElementById('pill_' + activeModalQuestionId);
      if (pill) {
        if (text.length > 0) {
          pill.className = 'draft-status-pill done';
          pill.textContent = `작성 완료 (${text.length}자)`;
        } else {
          pill.className = 'draft-status-pill';
          pill.textContent = '미작성 (클릭하여 작성)';
        }
      }
    }

    // Clear Modal Draft
    function clearModalDraft() {
      if (!activeModalQuestionId) return;
      if (!confirm('이 문항의 작성 답안을 비우시겠습니까?')) return;
      const textarea = document.getElementById('modalTextarea');
      textarea.value = '';
      onModalInput();
    }

    // Toggle Solution peek inside Modal
    function toggleModalSolution() {
      if (!activeModalQuestionId || typeof examQuestions04 === 'undefined') return;
      const q = examQuestions04.find(item => item.id === activeModalQuestionId);
      if (!q) return;

      const solBox = document.getElementById('modalSolutionBox');
      const solContent = document.getElementById('modalSolutionContent');
      if (solBox.style.display === 'block') {
        solBox.style.display = 'none';
      } else {
        solContent.innerHTML = `
          <div style="margin-bottom: 8px; font-weight: bold; color: #60a5fa;">📌 [현상학적 단서]: ${q.step1}</div>
          <div style="margin-bottom: 8px; font-weight: bold; color: #c084fc;">⚙️ [핵심 메커니즘]: ${q.step2}</div>
          <div style="margin-bottom: 8px; font-weight: bold; color: #fb7185;">⚠️ [오답 함정]: ${q.step3}</div>
          <div style="margin-bottom: 8px; padding: 8px; background: rgba(245,158,11,0.15); border-left: 3px solid #f59e0b; color: #fef08a; font-weight: bold;">
            🏆 [KICE 만점 정답]:\\n${q.answer}
          </div>
          <div style="color: #94a3b8; font-size: 0.85rem;">📊 [루브릭]: ${q.rubric}</div>
        `;
        solBox.style.display = 'block';
      }
    }

    // ESC key closes modal
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeDraftModal();
      }
    });

    // Generate and Print Authentic KICE A4 Exam Paper
    function printKiceExamPaper(isSolutionMode) {
      if (typeof examQuestions04 === 'undefined') return;
      const printBox = document.getElementById('kicePrintExamContainer');
      if (!printBox) return;

      const items = examQuestions04.filter(q => {
        if (currentExamPeriod === 'all') return true;
        return q.periodKey === currentExamPeriod;
      });

      let periodLabel = '3교시 풀세트 전체 (1교시 교육학 + 2교시 전공 A형 + 3교시 전공 B형)';
      if (currentExamPeriod === 'pedagogy') periodLabel = '1교시 : 교육학 논술';
      else if (currentExamPeriod === 'major_a') periodLabel = '2교시 : 전공상담 A형';
      else if (currentExamPeriod === 'major_b') periodLabel = '3교시 : 전공상담 B형';

      const modeTitle = isSolutionMode ? '만점 해설 및 칼채점기준표' : '실전 시험 문제지';

      let htmlContent = `
        <div class="kice-paper-sheet">
          <div class="kice-paper-header">
            <div class="kice-paper-title-main">2027학년도 중등교사 임용후보자 선정경쟁시험</div>
            <div class="kice-paper-period-title">[ ${periodLabel} ${modeTitle} ]</div>
            <div class="kice-paper-meta-row">
              <div>수험번호 : (                       )      성명 : (              )</div>
              <div>${isSolutionMode ? '한국교육과정평가원 공인 칼채점 규격' : '문제지의 각 문항을 확인하고 답안지에 작성하시오.'}</div>
            </div>
          </div>
      `;

      items.forEach((q, idx) => {
        htmlContent += `
          <div class="kice-paper-qcard">
            <div class="kice-paper-qhead">
              <strong>문항 ${q.qnum}번.</strong> [${q.domain} / ${q.score}점] ${q.lead}
            </div>

            <div class="kice-paper-passage">
              <div style="font-weight: bold; margin-bottom: 4px;">[ ${q.periodKey === 'pedagogy' ? '제시문' : '상담 사례 지문'} ]</div>
              ${q.passage}
            </div>

            ${q.directions ? `
            <div class="kice-paper-directions">
              <div style="font-weight: bold; margin-bottom: 4px;">[ 작성 방법 ]</div>
              ${q.directions}
            </div>
            ` : ''}

            ${!isSolutionMode ? `
            <!-- Blank writing space for paper exam -->
            <div class="kice-paper-ans-box">
              <div class="kice-paper-ans-label">【 답안 작성란 】</div>
              ${q.qtype === '기입형' ? `
                <div style="padding: 10px 0; font-size: 0.95rem;">
                  ( ㉠ ) : ________________________________________  /  ( ㉡ ) : ________________________________________
                </div>
              ` : `
                <div class="kice-paper-lines" style="${q.periodKey === 'pedagogy' ? 'min-height: 280px;' : 'min-height: 120px;'}"></div>
              `}
            </div>
            ` : `
            <!-- Solution and Rubric in solution booklet -->
            <div class="kice-paper-sol-box">
              <div class="kice-sol-step"><strong>📌 [현상학적 단서]:</strong> ${q.step1}</div>
              <div class="kice-sol-step"><strong>⚙️ [핵심 메커니즘]:</strong> ${q.step2}</div>
              <div class="kice-sol-step"><strong>⚠️ [오답 함정]:</strong> ${q.step3}</div>
              <div class="kice-sol-ans">
                <div style="font-weight: bold; color: #000; margin-bottom: 4px;">🏆 [KICE 공식 정답 & 만점 표준 서술문]</div>
                ${q.answer}
              </div>
              <div class="kice-sol-rubric">
                <strong>📊 [1:1 세부 채점 기준표]:</strong> ${q.rubric}
              </div>
            </div>
            `}
          </div>
        `;
      });

      htmlContent += `</div>`;

      printBox.innerHTML = htmlContent;

      document.body.classList.remove('printing-core150', 'printing-kice-paper');
      document.body.classList.add('printing-kice-paper');

      window.print();

      window.addEventListener('afterprint', function onAfterKicePrint() {
        document.body.classList.remove('printing-kice-paper');
        window.removeEventListener('afterprint', onAfterKicePrint);
      });
    }
"""

pos_js_end = html.rfind('</script>')
html = html[:pos_js_end] + js_popup_and_print + '\n' + html[pos_js_end:]
print('Injected Popup and KICE A4 Print JS functions.')

# Save to target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully with Popup Modal and KICE A4 Exam Print! File size:', len(html))
