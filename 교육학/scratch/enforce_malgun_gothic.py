target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Explicitly enforce Malgun Gothic directly on card-q and all text containers
enforce_css = """
    /* ULTRA-STRICT MALGUN GOTHIC ENFORCEMENT */
    .card-q, #c-q, .answer-text, #c-ans, .td-q, .td-ans, .kice-textarea, body, * {
      font-family: 'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', sans-serif !important;
    }
    .card-q, #c-q {
      font-weight: 600 !important;
      color: #f8fafc !important;
      letter-spacing: -0.3px !important;
      line-height: 1.65 !important;
    }
    .answer-text, #c-ans {
      font-weight: 600 !important;
      color: #fef08a !important;
      letter-spacing: -0.2px !important;
      line-height: 1.75 !important;
    }
"""

if '/* ULTRA-STRICT MALGUN GOTHIC ENFORCEMENT */' not in html:
    html = html.replace('</style>', enforce_css.strip() + '\n  </style>')

# Also inject style attribute directly into <div class="card-q" id="c-q">
html = html.replace(
    '<div class="card-q" id="c-q">',
    '<div class="card-q" id="c-q" style="font-family:\'Malgun Gothic\', \'맑은 고딕\', sans-serif !important;">'
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Enforced Malgun Gothic on #c-q and CSS!")
