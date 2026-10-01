import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for hide-kw mode
table_css = """
    /* HIDE KEYWORDS IN TABLE MODE */
    #table-body.hide-kw td:nth-child(2) {
      position: relative;
      cursor: pointer;
      background-color: #1e293b;
    }
    #table-body.hide-kw td:nth-child(2)::after {
      content: "🔒 마우스 올려서 확인";
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #94a3b8;
      font-size: 0.9rem;
      font-weight: 700;
      pointer-events: none;
      opacity: 1;
      transition: 0.2s;
      width: 100%;
      text-align: center;
    }
    #table-body.hide-kw td:nth-child(2):hover::after {
      opacity: 0;
    }
    #table-body.hide-kw td:nth-child(2) > * {
      opacity: 0;
      filter: blur(4px);
      transition: 0.2s;
    }
    #table-body.hide-kw td:nth-child(2):hover > * {
      opacity: 1;
      filter: blur(0);
    }
    
    /* PRINT OVERRIDES FOR HIDE-KW */
    @media print {
      #table-body.hide-kw td:nth-child(2) { background-color: #fff !important; }
      #table-body.hide-kw td:nth-child(2)::after { display: none !important; }
      #table-body.hide-kw td:nth-child(2) > * { opacity: 1 !important; filter: blur(0) !important; }
    }
"""
if "/* HIDE KEYWORDS IN TABLE MODE */" not in html:
    html = html.replace('/* Reward Modal */', table_css + '\n    /* Reward Modal */')

# 2. Add Toggle Button in Table Mode
table_btn_html = """
      <div style="text-align: right; margin-bottom: 10px;">
        <button class="btn-control" id="btn-toggle-kw" onclick="toggleTableKw()" style="background:#475569; border-color:#334155; color:#fff; width:auto; display:inline-block; padding: 8px 15px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s;">👀 영역 및 표제어 가리기</button>
      </div>
"""
if "toggleTableKw()" not in html:
    html = html.replace('<div class="table-container">', table_btn_html + '        <div class="table-container">')

# 3. Add JS Logic for the Toggle Button
table_js = """
    let isKwHidden = false;
    function toggleTableKw() {
      isKwHidden = !isKwHidden;
      const tableBody = document.getElementById('table-body');
      const btn = document.getElementById('btn-toggle-kw');
      if (isKwHidden) {
        tableBody.classList.add('hide-kw');
        btn.innerText = '👀 영역 및 표제어 보이기';
        btn.style.background = '#facc15';
        btn.style.color = '#000';
      } else {
        tableBody.classList.remove('hide-kw');
        btn.innerText = '👀 영역 및 표제어 가리기';
        btn.style.background = '#475569';
        btn.style.color = '#fff';
      }
    }
"""
if "function toggleTableKw()" not in html:
    html = html.replace('function switchMode(mode) {', table_js + '\n    function switchMode(mode) {')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Table hide-keyword functionality added.")
