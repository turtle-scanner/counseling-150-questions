import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update ULTRA-STRICT CSS to use normal font-weight: 400
old_ultra = r"""    /* ULTRA-STRICT MALGUN GOTHIC ENFORCEMENT */[\s\S]*?(?=</style>)"""
new_ultra = """    /* ULTRA-STRICT MALGUN GOTHIC & SLIM COMFORTABLE FONT WEIGHT (400) */
    *, html, body, .app-header, .table-container, table, th, td, .td-kw, .td-q, .td-ans, .card-q, #c-q, .answer-text, #c-ans, .kice-textarea, #search-input, .btn-control, .pill-btn, .answer-kw, .card-badge, .trap-box {
      font-family: 'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', sans-serif !important;
    }
    .card-q, #c-q {
      font-weight: 400 !important;
      color: #f1f5f9 !important;
      letter-spacing: -0.2px !important;
      line-height: 1.7 !important;
      font-size: 1.2rem !important;
    }
    .answer-text, #c-ans {
      font-weight: 400 !important;
      color: #fef08a !important;
      letter-spacing: -0.2px !important;
      line-height: 1.75 !important;
      font-size: 1.25rem !important;
    }
    .td-q {
      font-weight: 400 !important;
      color: #f1f5f9 !important;
    }
    .td-ans {
      font-weight: 400 !important;
      color: #fef08a !important;
    }
"""

html = re.sub(old_ultra, new_ultra.strip() + '\n  ', html)

# Also remove any dangling heavy weights on card-q and answer-text in the stylesheet
html = html.replace('.card-q { font-size: 1.1rem; font-weight: 700;', '.card-q { font-size: 1.1rem; font-weight: 400;')
html = html.replace('.answer-text { font-size: 0.95rem; color: #fef08a; line-height: 1.4; font-weight: 600;', '.answer-text { font-size: 0.95rem; color: #fef08a; line-height: 1.4; font-weight: 400;')
html = html.replace('.answer-text { font-size: 1.45rem !important; line-height: 1.7 !important; font-weight: 800 !important; }', '.answer-text { font-size: 1.25rem !important; line-height: 1.7 !important; font-weight: 400 !important; }')
html = html.replace('.card-q { font-size: 1.25rem !important; line-height: 1.6 !important; }', '.card-q { font-size: 1.2rem !important; line-height: 1.65 !important; font-weight: 400 !important; }')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Adjusted font-weight to 400 (Comfortable Regular)!")
