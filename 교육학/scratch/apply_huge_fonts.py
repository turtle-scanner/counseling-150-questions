import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the previous font upgrades with even BIGGER sizes
bigger_fonts = """
    /* FONT UPGRADES */
    body, .app-header, .table-container, .card-q {
      font-family: "Batang", "바탕", "KoPub Batang", "Nanum Myeongjo", serif !important;
    }
    .kice-textarea, .answer-text, #search-input, .btn-control {
      font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;
    }
    /* MASSIVE FONT SIZES FOR READABILITY */
    .card-q { font-size: 1.45rem !important; line-height: 1.8 !important; }
    .answer-text { font-size: 1.7rem !important; line-height: 1.8 !important; font-weight: 800 !important; }
    .card-kw { font-size: 1.8rem !important; font-weight: 900 !important; margin-bottom: 15px !important; }
    .kice-textarea { font-size: 1.3rem !important; }
"""

# Extract the old font CSS block and replace
html = re.sub(r'/\* FONT UPGRADES \*/[\s\S]*?margin-bottom: 15px !important; \}', bigger_fonts.strip(), html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Extra HUGE font sizes applied.")
