import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the block from /* FONT UPGRADES */ up to /* MASSIVE FONT SIZES
new_font_block = """      /* FONT UPGRADES: 100% MALGUN GOTHIC FOR CRISP READABILITY */
      *, html, body, .app-header, .table-container, table, th, td, .td-kw, .td-q, .td-ans, .card-q, .answer-text, .kice-textarea, #search-input, .btn-control, .pill-btn, .answer-kw, .card-badge, .trap-box {
        font-family: "Malgun Gothic", "맑은 고딕", -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Segoe UI", sans-serif !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
      }
      
      /* TABLE HIGH-CONTRAST MALGUN GOTHIC ENHANCEMENTS */
      .table-container table th {
        font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;
        font-weight: 800 !important;
        color: #fbbf24 !important;
        background: #0f172a !important;
        border-bottom: 2px solid #334155 !important;
      }
      .table-container table td {
        font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;
        line-height: 1.65 !important;
        font-size: 1.05rem !important;
        vertical-align: top !important;
      }
      .td-kw {
        color: #38bdf8 !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        line-height: 1.4 !important;
        display: block !important;
        margin-top: 4px !important;
      }
      .td-q {
        color: #f1f5f9 !important;
        font-size: 1.05rem !important;
        line-height: 1.65 !important;
        font-weight: 500 !important;
      }
      .td-ans {
        color: #fef08a !important;
        font-size: 1.05rem !important;
        line-height: 1.7 !important;
        font-weight: 600 !important;
        background: #111827 !important;
        padding: 10px !important;
        border-radius: 6px !important;
        border-left: 3px solid #facc15 !important;
      }"""

# Use regex to find and replace the entire Batang/serif section
html = re.sub(
    r'/\*\s*FONT UPGRADES\s*\*/[\s\S]*?(?=/\*\s*MASSIVE FONT SIZES)',
    new_font_block.strip() + '\n      ',
    html
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced font block cleanly with regex!")
