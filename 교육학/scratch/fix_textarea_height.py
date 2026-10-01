import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Force height of the specific KICE textarea to be 160px (4 lines) and override any global textarea styles
# Let's replace whatever height is there inside .kice-textarea
html = re.sub(r'\.kice-textarea\s*\{[^\}]*\}', 
    '''.kice-textarea {
      width: 100%;
      height: 160px !important;
      background-color: transparent;
      background-image: repeating-linear-gradient(transparent, transparent 39px, #fbcfe8 39px, #fbcfe8 40px);
      background-attachment: local;
      line-height: 40px !important;
      padding: 0 10px;
      color: #000;
      font-family: "Malgun Gothic", sans-serif;
      font-size: 1.15rem;
      font-weight: 600;
      border: none !important;
      outline: none !important;
      resize: none;
      box-sizing: border-box;
      display: block;
      overflow-y: auto;
    }''', html)

# Make sure the wrapper isn't restricted in height
html = re.sub(r'\.kice-sheet-wrapper\s*\{[^\}]*\}',
    '''.kice-sheet-wrapper {
      display: flex;
      width: 100%;
      min-height: 160px;
      border: 2px solid #ec4899;
      background-color: #fff;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 15px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }''', html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Forced textarea to 160px height.")
