import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New HTML structure for the input area
old_input_regex = r'<div class="input-area".*?>\s*<textarea id="c-input".*?</textarea>\s*</div>'

new_input_html = """<div class="kice-sheet-wrapper">
          <div class="kice-sheet-left">
            문항 <span id="kice-q-num">1</span><br>(4점)
          </div>
          <div class="kice-sheet-right">
            <textarea id="c-input" class="kice-textarea" placeholder="실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요..."></textarea>
          </div>
        </div>"""

html = re.sub(old_input_regex, new_input_html, html, flags=re.DOTALL)

# 2. CSS for the actual KICE sheet
kice_css = """
    /* ACTUAL KICE EXAM ANSWER SHEET CSS */
    .kice-sheet-wrapper {
      display: flex;
      width: 100%;
      border: 2px solid #ec4899; /* Strong Pink border */
      background-color: #fff;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 15px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .kice-sheet-left {
      width: 70px;
      background-color: #fdf2f8; /* Very light pink */
      color: #be185d; /* Deep pink text */
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
      width: 100%;
      height: 120px; /* 3 lines of 40px */
      background-color: transparent;
      background-image: repeating-linear-gradient(transparent, transparent 39px, #fbcfe8 39px, #fbcfe8 40px); /* Dotted-like pink lines */
      background-attachment: local;
      line-height: 40px;
      padding: 0 10px;
      color: #000; /* Black ink */
      font-family: "Malgun Gothic", sans-serif;
      font-size: 1.15rem;
      font-weight: 600;
      border: none;
      resize: none;
      box-sizing: border-box;
    }
    .kice-textarea:focus { outline: none; }
    .kice-textarea::placeholder { color: #cbd5e1; font-weight: 400; line-height: 40px; }
"""

# Insert CSS before the closing style tag
html = html.replace('  </style>', kice_css + '\n  </style>')

# Remove old textarea CSS to avoid conflicts
html = re.sub(r'textarea \{.*?\}', '', html, flags=re.DOTALL)
html = re.sub(r'\.input-area \{.*?\}', '', html, flags=re.DOTALL)

# 3. Update JS to modify the question number
js_update = """elInput.value = '';
      if(document.getElementById('kice-q-num')) {
        document.getElementById('kice-q-num').innerText = index + 1;
      }"""
html = html.replace("elInput.value = '';", js_update)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("KICE Answer Sheet design applied.")
