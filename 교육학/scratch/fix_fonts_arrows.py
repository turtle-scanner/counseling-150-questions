import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update font family and sizes
new_fonts = """
    /* FONT UPGRADES */
    body, .app-header, .table-container, .card-q, .answer-text {
      font-family: "Batang", "바탕", "KoPub Batang", "Nanum Myeongjo", serif !important;
    }
    .kice-textarea, #search-input, .btn-control {
      font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;
    }
    /* MASSIVE FONT SIZES FOR READABILITY */
    .card-q { font-size: 1.25rem !important; line-height: 1.6 !important; }
    .answer-text { font-size: 1.45rem !important; line-height: 1.7 !important; font-weight: 800 !important; }
    .card-kw { font-size: 1.5rem !important; font-weight: 900 !important; margin-bottom: 15px !important; }
    .kice-textarea { font-size: 1.25rem !important; }
"""
html = re.sub(r'/\* FONT UPGRADES \*/[\s\S]*?font-size: 1\.3rem !important; \}', new_fonts.strip(), html)


# 2. Add bulletproof arrow replacements including user typos (Wrightarrow instead of \rightarrow)
old_arrows = r"t = t\.split\('.*?\\Rightarrow.*?'\)\.join\('➔'\);" # just targeting the area
# Actually I'll just rewrite the formatText function
new_format_text = """
    function formatText(text) {
      if (!text) return '';
      let t = text.replace(/\\*\\*(.*?)\\*\\*/g, '<span style="color:#d97706; font-weight:bold;">$1</span>');
      // Replace LaTeX arrows safely (including Wrightarrow typo)
      t = t.split('$\\\\Rightarrow$').join('➔');
      t = t.split('\\\\Rightarrow').join('➔');
      t = t.split('$WRightarrow$').join('➔');
      t = t.split('WRightarrow').join('➔');
      
      t = t.split('$\\\\rightarrow$').join('→');
      t = t.split('\\\\rightarrow').join('→');
      t = t.split('$Wrightarrow$').join('→');
      t = t.split('Wrightarrow').join('→');
      
      t = t.split('$\\\\Leftrightarrow$').join('↔');
      t = t.split('\\\\Leftrightarrow').join('↔');
      return t;
    }
"""
html = re.sub(r'function formatText\(text\) \{[\s\S]*?return t;\s*\}', new_format_text.strip(), html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fonts updated and arrow typos fixed.")
