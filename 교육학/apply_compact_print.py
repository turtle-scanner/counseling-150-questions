# -*- coding: utf-8 -*-

compact_print_css = """@media print {
  @page {
    size: A4 portrait;
    margin: 8mm 7mm 8mm 7mm;
  }
  
  *, *::before, *::after {
    box-shadow: none !important;
    text-shadow: none !important;
  }
  
  html, body {
    background: #ffffff !important;
    color: #0f172a !important;
    font-size: 8pt !important;
    line-height: 1.32 !important;
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
    padding-bottom: 4px !important;
    margin-bottom: 6px !important;
    page-break-after: avoid !important;
  }
  .print-page-header h2 {
    font-size: 11pt !important;
    font-weight: 900 !important;
    color: #0f172a !important;
    margin: 0 0 2px 0 !important;
  }
  .print-page-header p {
    font-size: 7.5pt !important;
    color: #475569 !important;
    margin: 0 !important;
  }

  /* 2-Column Side-by-Side Exam Card (Paper Saving Layout) */
  .exam-full-card {
    background: #ffffff !important;
    border: 1px solid #94a3b8 !important;
    border-radius: 3px !important;
    padding: 6px 8px !important;
    margin-bottom: 6px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  .exam-split-grid {
    display: grid !important;
    grid-template-columns: 1.05fr 1fr !important;
    gap: 8px !important;
    align-items: start !important;
  }
  .exam-left-col {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
  }
  .exam-right-col {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
    margin-top: 0 !important;
  }

  .exam-case-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-left: 3px solid #0284c7 !important;
    border-radius: 3px !important;
    padding: 5px 8px !important;
    font-size: 7.8pt !important;
    line-height: 1.35 !important;
    max-height: none !important;
    overflow: visible !important;
    white-space: pre-wrap !important;
  }

  .exam-instructions {
    background: #fefce8 !important;
    color: #713f12 !important;
    border: 1px solid #fde047 !important;
    border-left: 3px solid #ca8a04 !important;
    border-radius: 3px !important;
    padding: 4px 6px !important;
    margin-top: 0 !important;
    font-size: 7.5pt !important;
    line-height: 1.28 !important;
  }
  .exam-instructions strong {
    color: #713f12 !important;
  }
  .exam-instructions ul {
    margin-left: 12px !important;
    margin-top: 2px !important;
    margin-bottom: 2px !important;
  }

  .exam-textarea {
    display: none !important;
  }

  /* Compact Print Paper Answer Layout */
  .print-paper-answer {
    display: block !important;
    margin-top: 4px !important;
  }
  
  .print-written-text {
    display: none;
    font-family: 'Nanum Myeongjo', serif;
    font-size: 7.8pt;
    line-height: 1.35;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 4px 6px;
    background: #fff;
    min-height: 40px;
    white-space: pre-wrap;
  }
  body.print-with-user .print-written-text {
    display: block !important;
  }
  
  .print-blank-lines {
    display: block;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 3px 6px;
    background: #ffffff;
  }
  body.print-with-user .print-blank-lines {
    display: none !important;
  }
  .p-line {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: #94a3b8;
    line-height: 16px;
    border-bottom: 1px solid #e2e8f0;
    padding: 1px 0;
  }
  .p-line:last-child {
    border-bottom: none;
  }

  /* Compact Model Answer on Paper */
  .model-answer-panel {
    display: none !important;
  }
  body.print-with-answers .model-answer-panel {
    display: block !important;
    background: #f0fdf4 !important;
    border: 1px solid #86efac !important;
    border-left: 3px solid #16a34a !important;
    border-radius: 3px !important;
    padding: 5px 7px !important;
    margin-top: 4px !important;
    color: #14532d !important;
    max-height: none !important;
    overflow: visible !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .model-answer-title {
    color: #15803d !important;
    font-size: 7.5pt !important;
    font-weight: 800 !important;
    margin-bottom: 2px !important;
  }
  .model-answer-text {
    color: #14532d !important;
    font-size: 7.6pt !important;
    line-height: 1.32 !important;
  }
  .rubric-list {
    border-top: 1px dashed #86efac !important;
    color: #166534 !important;
    font-size: 7.2pt !important;
    margin-top: 3px !important;
    padding-top: 3px !important;
  }

  /* Badges */
  .badge {
    border: 1px solid #94a3b8 !important;
    color: #0f172a !important;
    background: #f1f5f9 !important;
    font-size: 7pt !important;
    padding: 1px 4px !important;
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
    font-size: 7pt !important;
    padding: 1px 4px !important;
  }

  /* Pedagogy Domain 2x2 Grid on Paper */
  #ped-domain-cards {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 6px !important;
    margin-top: 6px !important;
  }

  /* Ultra-Compact TOP 55 Cards in Print (Paper Saver: 10-14 cards per A4 page) */
  .card-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 5px !important;
  }
  .item-card {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 3px !important;
    padding: 4px 6px !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    gap: 3px !important;
  }
  .card-header {
    margin-bottom: 2px !important;
  }
  .card-title {
    font-size: 7.6pt !important;
  }
  .card-question {
    color: #0f172a !important;
    font-size: 7.2pt !important;
    line-height: 1.25 !important;
    margin-bottom: 2px !important;
  }
  .compact-answer-box {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 2px solid #10b981 !important;
    font-size: 7.1pt !important;
    line-height: 1.26 !important;
    padding: 3px 5px !important;
  }
  .four-line-list li {
    margin-bottom: 2px !important;
  }
}"""

import re

target_files = [
    'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/exam_master_2027.html',
    'g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html'
]

for tf in target_files:
    with open(tf, 'r', encoding='utf-8') as f:
        content = f.read()

    # @media print { ... } 블록 찾기
    m = re.search(r'@media print\s*\{[\s\S]*?\n\}', content)
    if m:
        content = content[:m.start()] + compact_print_css + content[m.end():]
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated print CSS in {tf}")
    else:
        print(f"Could not find @media print in {tf}")

print("Compact print CSS deployment finished.")
