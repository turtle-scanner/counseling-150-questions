import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the whole KICE CSS block and replace it cleanly.
# The block starts near: "/* ACTUAL KICE EXAM ANSWER SHEET CSS */"

kice_css_full = """
    /* ACTUAL KICE EXAM ANSWER SHEET CSS */
    .kice-sheet-wrapper {
      display: flex;
      width: 100%;
      min-height: 160px;
      border: 2px solid #ec4899;
      background-color: #fff;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 15px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .kice-sheet-left {
      width: 70px;
      background-color: #fdf2f8;
      color: #be185d;
      font-weight: 800;
      font-size: 1.05rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-right: 1px solid #ec4899;
      text-align: center;
      line-height: 1.3;
      padding: 10px 5px;
    }
    .kice-sheet-right {
      flex: 1;
      position: relative;
      background-color: #fff;
    }
    .kice-textarea {
      width: 100% !important;
      height: 160px !important;
      background-color: transparent !important;
      background-image: repeating-linear-gradient(transparent, transparent 39px, #fbcfe8 39px, #fbcfe8 40px) !important;
      background-attachment: local !important;
      line-height: 40px !important;
      padding: 0 10px !important;
      color: #000 !important;
      font-family: "Malgun Gothic", sans-serif !important;
      font-size: 1.15rem !important;
      font-weight: 600 !important;
      border: none !important;
      outline: none !important;
      resize: none !important;
      box-sizing: border-box !important;
      display: block !important;
      margin: 0 !important;
    }
    .kice-textarea:focus { outline: none !important; border: none !important; }
    .kice-textarea::placeholder { color: #cbd5e1; font-weight: 400; line-height: 40px; }
"""

# Replace anything from /* ACTUAL KICE EXAM ANSWER SHEET CSS */ to the end of .kice-textarea::placeholder
# Regex dotall to match the whole block and replace it
html = re.sub(r'/\* ACTUAL KICE EXAM ANSWER SHEET CSS \*/.*\.kice-textarea::placeholder\s*\{[^\}]*\}', kice_css_full, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("CSS fixed.")
