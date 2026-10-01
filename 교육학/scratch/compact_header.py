import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS to heavily compress the top header heights
compact_css = """
    /* COMPACT HEADER HEIGHTS */
    .app-header { padding: 5px 10px !important; margin-bottom: 0 !important; }
    .app-title { font-size: 1.2rem !important; margin-bottom: 2px !important; }
    .app-sub { font-size: 0.8rem !important; }
    #pomodoro-bar { padding: 3px !important; gap: 8px !important; }
    #pomo-time { font-size: 1rem !important; }
    #dashboard { padding: 5px !important; margin: 5px 10px !important; font-size: 0.9rem !important; }
    .controls { margin-bottom: 5px !important; gap: 5px !important; }
    .btn-control { padding: 6px 10px !important; font-size: 0.85rem !important; }
    #search-input { padding: 6px !important; }
"""
if "/* COMPACT HEADER HEIGHTS */" not in html:
    html = html.replace('</style>', compact_css + '\n  </style>')
else:
    # Update it if it exists
    html = re.sub(r'/\* COMPACT HEADER HEIGHTS \*/[\s\S]*?#search-input \{ padding: 6px !important; \}', compact_css.strip(), html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Header heights compacted.")
