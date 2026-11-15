# -*- coding: utf-8 -*-
import os
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
bm_path = os.path.join(base_dir, "build_master.js")

with open(bm_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Print CSS and Modal Styles
print_css = """
/* Print Modal Styles */
.print-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(4px);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.print-modal-overlay.active {
  display: flex;
}
.print-modal-card {
  background: #111827;
  border: 1px solid #334155;
  border-radius: 14px;
  width: 100%;
  max-width: 520px;
  padding: 24px;
  color: #f8fafc;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  animation: fadeIn 0.2s ease;
}
.print-modal-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
  border-bottom: 1px solid #1e293b;
  padding-bottom: 12px;
}
.print-modal-group {
  margin-bottom: 16px;
}
.print-modal-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: #94a3b8;
  margin-bottom: 8px;
  display: block;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.print-option-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 8px;
  margin-bottom: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.88rem;
}
.print-option-row:hover {
  background: #273549;
  border-color: #475569;
}
.print-option-row input[type="radio"],
.print-option-row input[type="checkbox"] {
  accent-color: #38bdf8;
  width: 18px;
  height: 18px;
  cursor: pointer;
}
.print-modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
  border-top: 1px solid #1e293b;
  padding-top: 16px;
}
.btn-print-confirm {
  background: #f59e0b;
  color: #000;
  font-weight: 800;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}
.btn-print-confirm:hover {
  background: #d97706;
}
.btn-print-cancel {
  background: #334155;
  color: #f8fafc;
  font-weight: 600;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
}
.btn-print-cancel:hover {
  background: #475569;
}

/* Screen hidden elements for print */
.print-page-header,
.print-paper-answer {
  display: none;
}

/* ================== A4 PRINT OPTIMIZATIONS ================== */
@media print {
  @page {
    size: A4 portrait;
    margin: 12mm 10mm 12mm 10mm;
  }
  
  *, *::before, *::after {
    box-shadow: none !important;
    text-shadow: none !important;
  }
  
  html, body {
    background: #ffffff !important;
    color: #0f172a !important;
    font-size: 9pt !important;
    line-height: 1.45 !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
  }

  .app-header,
  .control-bar,
  .progress-wrap,
  .tool-group,
  .timer-widget,
  .quick-nav,
  .notice-banner,
  .no-print,
  #blind-toggle-btn,
  .search-box,
  #top55-filters,
  .char-count-badge,
  .memorize-chk,
  .print-modal-overlay,
  .answer-box-header {
    display: none !important;
  }

  main.content-area {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Print Section Scopes */
  body.print-scope-full #sec-top55 {
    display: none !important;
  }
  body.print-scope-full #sec-pedagogy,
  body.print-scope-full #sec-qa,
  body.print-scope-full #sec-qb {
    display: block !important;
  }
  body.print-scope-full #sec-qa,
  body.print-scope-full #sec-qb {
    page-break-before: always !important;
    break-before: page !important;
  }

  body.print-scope-top55 #sec-top55 {
    display: block !important;
  }
  body.print-scope-top55 #sec-pedagogy,
  body.print-scope-top55 #sec-qa,
  body.print-scope-top55 #sec-qb {
    display: none !important;
  }

  body.print-scope-current .tab-section:not(.active) {
    display: none !important;
  }
  body.print-scope-current .tab-section.active {
    display: block !important;
  }

  /* Formal Print Page Header */
  .print-page-header {
    display: block !important;
    border-bottom: 2px solid #0f172a !important;
    padding-bottom: 6px !important;
    margin-bottom: 12px !important;
    page-break-after: avoid !important;
  }
  .print-page-header h2 {
    font-size: 13pt !important;
    font-weight: 900 !important;
    color: #0f172a !important;
    margin: 0 0 2px 0 !important;
  }
  .print-page-header p {
    font-size: 8.5pt !important;
    color: #475569 !important;
    margin: 0 !important;
  }

  /* Full Question Cards on Paper */
  .exam-full-card {
    background: #ffffff !important;
    border: 1px solid #94a3b8 !important;
    border-radius: 4px !important;
    padding: 10px 12px !important;
    margin-bottom: 12px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  .exam-split-grid {
    display: block !important;
  }
  .exam-left-col {
    width: 100% !important;
  }
  .exam-right-col {
    width: 100% !important;
    margin-top: 8px !important;
  }

  .exam-case-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-left: 3px solid #0284c7 !important;
    border-radius: 4px !important;
    padding: 8px 12px !important;
    font-size: 9pt !important;
    line-height: 1.5 !important;
    max-height: none !important;
    overflow: visible !important;
    white-space: pre-wrap !important;
  }

  .exam-instructions {
    background: #fefce8 !important;
    color: #713f12 !important;
    border: 1px solid #fde047 !important;
    border-left: 3px solid #ca8a04 !important;
    border-radius: 4px !important;
    padding: 6px 10px !important;
    margin-top: 6px !important;
    font-size: 8.5pt !important;
    line-height: 1.4 !important;
  }
  .exam-instructions strong {
    color: #713f12 !important;
  }

  .exam-textarea {
    display: none !important;
  }

  /* Print Paper Answer Layout */
  .print-paper-answer {
    display: block !important;
    margin-top: 6px !important;
  }
  
  .print-written-text {
    display: none;
    font-family: 'Nanum Myeongjo', serif;
    font-size: 9pt;
    line-height: 1.55;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 8px 12px;
    background: #fff;
    min-height: 50px;
    white-space: pre-wrap;
  }
  body.print-with-user .print-written-text {
    display: block !important;
  }
  
  .print-blank-lines {
    display: block;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 10px;
    background: #ffffff;
  }
  body.print-with-user .print-blank-lines {
    display: none !important;
  }
  .p-line {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    color: #94a3b8;
    line-height: 22px;
    border-bottom: 1px solid #e2e8f0;
    padding: 2px 0;
  }
  .p-line:last-child {
    border-bottom: none;
  }

  /* Model Answer on Paper */
  .model-answer-panel {
    display: none !important;
  }
  body.print-with-answers .model-answer-panel {
    display: block !important;
    background: #f0fdf4 !important;
    border: 1px solid #86efac !important;
    border-left: 3px solid #16a34a !important;
    border-radius: 4px !important;
    padding: 8px 12px !important;
    margin-top: 8px !important;
    color: #14532d !important;
    max-height: none !important;
    overflow: visible !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .model-answer-title {
    color: #15803d !important;
    font-size: 8.5pt !important;
    font-weight: 800 !important;
  }
  .model-answer-text {
    color: #14532d !important;
    font-size: 8.8pt !important;
    line-height: 1.5 !important;
  }
  .rubric-list {
    border-top: 1px dashed #86efac !important;
    color: #166534 !important;
    font-size: 8pt !important;
  }

  /* Badges */
  .badge {
    border: 1px solid #94a3b8 !important;
    color: #0f172a !important;
    background: #f1f5f9 !important;
    font-size: 7.5pt !important;
    padding: 1px 6px !important;
  }
  .badge-category, .badge-pedagogy {
    background: #e0f2fe !important;
    color: #0369a1 !important;
    border-color: #7dd3fc !important;
  }
  .badge-score {
    background: #fef3c7 !important;
    color: #b45309 !important;
    border-color: #fcd34d !important;
  }
  .kw-tag {
    background: #f8fafc !important;
    color: #0284c7 !important;
    border: 1px solid #cbd5e1 !important;
    font-size: 7.5pt !important;
    padding: 1px 5px !important;
  }

  /* TOP 55 Cards in Print */
  .card-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
  }
  .item-card {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 4px !important;
    padding: 8px 10px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    gap: 6px !important;
  }
  .card-question {
    color: #0f172a !important;
    font-size: 8.8pt !important;
  }
  .compact-answer-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 2px solid #10b981 !important;
    font-size: 8.3pt !important;
    padding: 6px 8px !important;
  }
}
"""

# Insert print_css before </style>
if "/* Print Modal Styles */" not in code:
    code = code.replace("</style>\n</head>", print_css + "\n</style>\n</head>")

# 2. Add print button in header .tool-group
btn_code = """      <button class="tool-btn" onclick="openPrintModal()" style="background: var(--gold); color: #000; font-weight: 800; border-color: var(--gold);">
        <span>🖨️</span> A4 인쇄 / PDF
      </button>"""
target_export = '<button class="tool-btn" onclick="exportAnswers()">'
if "openPrintModal()" not in code:
    code = code.replace(target_export, btn_code + "\n\n      " + target_export)

# 3. Add print modal HTML right after </header>
modal_html = """
<!-- ================== PRINT CONFIG MODAL ================== -->
<div class="print-modal-overlay" id="print-modal">
  <div class="print-modal-card">
    <div class="print-modal-title">
      <span>🖨️</span> A4 인쇄 및 PDF 저장 설정
    </div>

    <div class="print-modal-group">
      <span class="print-modal-label">인쇄 대상 선택</span>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="full" checked>
        <div>
          <strong>📑 1~3교시 실전 모의고사 풀세트 전체 (추천)</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">1교시 교육학 + 2교시 전공 A형 + 3교시 전공 B형 (각 교시별 페이지 자동 분할)</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="current">
        <div>
          <strong>📄 현재 열려 있는 탭만 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">현재 화면에서 선택된 특정 교시 또는 탭만 집중 인쇄</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="radio" name="print-scope" value="top55">
        <div>
          <strong>⚡ 2027 핵심 55선 콤팩트 암기장 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">교육학 20선 + 전공상담 35선 2열 인쇄용 카드 요약집</div>
        </div>
      </label>
    </div>

    <div class="print-modal-group">
      <span class="print-modal-label">출력 옵션 선택</span>
      <label class="print-option-row">
        <input type="checkbox" id="print-opt-answers" checked>
        <div>
          <strong>🏆 KICE 4점 만점 모범답안 및 채점기준표 포함</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">체크 해제 시 실제 시험장용 '빈 답안 작성란'으로 인쇄됩니다.</div>
        </div>
      </label>
      <label class="print-option-row">
        <input type="checkbox" id="print-opt-user">
        <div>
          <strong>✍️ 내가 웹에서 직접 작성한 답안 인쇄</strong>
          <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 2px;">웹페이지 답안란에 입력해 둔 내용을 그대로 종이에 인쇄합니다.</div>
        </div>
      </label>
    </div>

    <div class="print-modal-actions">
      <button class="btn-print-cancel" onclick="closePrintModal()">닫기</button>
      <button class="btn-print-confirm" onclick="executePrint()">
        <span>🖨️</span> A4 인쇄 시작 (미리보기)
      </button>
    </div>
  </div>
</div>
"""
if 'id="print-modal"' not in code:
    code = code.replace('</header>', '</header>\n' + modal_html)

# 4. Add print page headers in sections
if '<div class="print-page-header">' not in code:
    code = code.replace('<section class="tab-section active" id="sec-top55">', """<section class="tab-section active" id="sec-top55">
    <div class="print-page-header">
      <h2>2027 KICE 중등임용 전문상담 & 교육학 영구동결 핵심 55선 암기장</h2>
      <p>한국교육과정평가원(KICE) 7개년 기출 검증 공인 키워드 100% 수록 | 2열 콤팩트 스피드 암기</p>
    </div>""")

    code = code.replace('<section class="tab-section" id="sec-pedagogy">', """<section class="tab-section" id="sec-pedagogy">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>1교시 교육학 논술 [배점 20점 만점 / 시험시간 60분]</p>
    </div>""")

    code = code.replace('<section class="tab-section" id="sec-qa">', """<section class="tab-section" id="sec-qa">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>2교시 전공상담 A형 [12문항 40점 만점 / 시험시간 90분]</p>
    </div>""")

    code = code.replace('<section class="tab-section" id="sec-qb">', """<section class="tab-section" id="sec-qb">
    <div class="print-page-header">
      <h2>2027학년도 중등교사 임용후보자 선정경쟁시험</h2>
      <p>3교시 전공상담 B형 [11문항 40점 만점 / 시험시간 90분]</p>
    </div>""")

# 5. Populate ped-title and ped-case in renderPedagogy
ped_pop = """  const pedTitleEl = document.getElementById('ped-title');
  const pedCaseEl = document.getElementById('ped-case');
  if (pedTitleEl) pedTitleEl.innerText = ped.title || '2027학년도 중등교사 임용후보자 선정경쟁시험 1교시 교육학 논술';
  if (pedCaseEl) pedCaseEl.innerText = ped.case || '';
"""
if "pedTitleEl.innerText" not in code:
    code = code.replace("const container = document.getElementById('ped-domain-cards');\n  if (!container) return;\n  container.innerHTML = '';",
                        ped_pop + "\n  const container = document.getElementById('ped-domain-cards');\n  if (!container) return;\n  container.innerHTML = '';")

# 6. Add print paper answer in renderPedagogy
old_ped_card_html = """            '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)"></textarea>' +
            '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +"""

new_ped_card_html = """            '<textarea class="exam-textarea" id="ped-input-' + d.id + '" placeholder="여기에 답안을 직접 입력하세요. (B4 1줄당 38~45자 기준)"></textarea>' +
            '<div class="print-paper-answer">' +
              '<div class="print-written-text" id="ped-print-user-' + d.id + '"></div>' +
              '<div class="print-blank-lines">' +
                '<div class="p-line">1. ________________________________________________________________</div>' +
                '<div class="p-line">2. ________________________________________________________________</div>' +
                '<div class="p-line">3. ________________________________________________________________</div>' +
                '<div class="p-line">4. ________________________________________________________________</div>' +
              '</div>' +
            '</div>' +
            '<div class="model-answer-panel" id="ped-ans-' + d.id + '">' +"""

if "ped-print-user-" not in code:
    code = code.replace(old_ped_card_html, new_ped_card_html)

# 7. Add print paper answer in renderExamQuestions
old_exam_card_html = """            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)"></textarea>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +"""

new_exam_card_html = """            '<textarea class="exam-textarea" id="input-' + type + '-' + q.num + '" placeholder="여기에 답안을 직접 입력하세요. (3줄 컷: 줄당 38~45자 규격)"></textarea>' +
            '<div class="print-paper-answer">' +
              '<div class="print-written-text" id="print-user-' + type + '-' + q.num + '"></div>' +
              '<div class="print-blank-lines">' +
                '<div class="p-line">1. ________________________________________________________________</div>' +
                '<div class="p-line">2. ________________________________________________________________</div>' +
                '<div class="p-line">3. ________________________________________________________________</div>' +
                '<div class="p-line">4. ________________________________________________________________</div>' +
              '</div>' +
            '</div>' +
            '<div class="model-answer-panel" id="ansbox-' + type + '-' + q.num + '">' +"""

if "print-user-" not in code:
    code = code.replace(old_exam_card_html, new_exam_card_html)

# 8. Add Print Modal Functions at the end of script
print_js = """
// Print Functions
function openPrintModal() {
  const modal = document.getElementById('print-modal');
  if (modal) modal.classList.add('active');
}

function closePrintModal() {
  const modal = document.getElementById('print-modal');
  if (modal) modal.classList.remove('active');
}

function executePrint() {
  const scopeEl = document.querySelector('input[name="print-scope"]:checked');
  const scope = scopeEl ? scopeEl.value : 'full';
  const includeAnswers = document.getElementById('print-opt-answers').checked;
  const includeUser = document.getElementById('print-opt-user').checked;

  // Sync all user inputs to print-written-text boxes
  if (rawData.pedagogy && rawData.pedagogy.domains) {
    rawData.pedagogy.domains.forEach(d => {
      const ta = document.getElementById('ped-input-' + d.id);
      const pu = document.getElementById('ped-print-user-' + d.id);
      if (ta && pu) pu.innerText = ta.value || '';
    });
  }

  ['A', 'B'].forEach(type => {
    const list = (type === 'A') ? rawData.questions_a : rawData.questions_b;
    if (list) {
      list.forEach(q => {
        const ta = document.getElementById('input-' + type + '-' + q.num);
        const pu = document.getElementById('print-user-' + type + '-' + q.num);
        if (ta && pu) pu.innerText = ta.value || '';
      });
    }
  });

  // Apply print classes to body
  document.body.classList.remove('print-scope-full', 'print-scope-current', 'print-scope-top55', 'print-with-answers', 'print-with-user');

  document.body.classList.add('print-scope-' + scope);
  if (includeAnswers) document.body.classList.add('print-with-answers');
  if (includeUser) document.body.classList.add('print-with-user');

  closePrintModal();

  setTimeout(() => {
    window.print();
  }, 150);
}

// Reset print classes after printing
window.addEventListener('afterprint', () => {
  document.body.classList.remove('print-scope-full', 'print-scope-current', 'print-scope-top55', 'print-with-answers', 'print-with-user');
});
"""

if "function openPrintModal()" not in code:
    code = code.replace("</script>", print_js + "\n</script>")

with open(bm_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_master.js with A4 print feature successfully.")
