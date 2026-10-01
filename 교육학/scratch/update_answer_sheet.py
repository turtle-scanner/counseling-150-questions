import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace textarea css with realistic KICE B4 answer sheet
old_textarea_regex = r'textarea \{ width: 100%; height: 50px; background: #0f1117; border: 1\.5px solid #334155; border-radius: 6px; padding: 8px; color: #f8fafc; font-family: inherit; font-size: 0\.95rem; resize: none; box-sizing: border-box; line-height: 1\.4; \}'

real_paper_css = """textarea {
      width: 100%;
      height: 82px; /* 2 lines of 40px + 2px border */
      background-color: #f8fafc; /* White paper */
      background-image: repeating-linear-gradient(transparent, transparent 38px, #94a3b8 38px, #94a3b8 40px);
      background-attachment: local; /* Lines scroll with text */
      line-height: 40px;
      padding: 0 12px;
      color: #0f172a; /* Black ink */
      font-family: "Malgun Gothic", sans-serif;
      font-size: 1.15rem;
      font-weight: 600;
      border: 1px solid #64748b;
      border-radius: 4px;
      resize: none;
      box-sizing: border-box;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
    }
    textarea:focus { outline: none; border: 2px solid #d97706; }
    textarea::placeholder { color: #94a3b8; line-height: 40px; }"""

html = re.sub(old_textarea_regex, real_paper_css, html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Answer sheet styling applied successfully.")
