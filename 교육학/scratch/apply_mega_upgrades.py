import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. PWA Meta Tags
pwa_meta = """
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#161a23">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <link rel="apple-touch-icon" href="images/go1.png">
"""
if "manifest.json" not in html:
    html = html.replace('<meta name="viewport"', pwa_meta + '    <meta name="viewport"')

# 2. PWA Service Worker Registration
sw_script = """
      // PWA Service Worker
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('sw.js').catch(err => console.log('SW Reg Failed', err));
        });
      }
"""
if "navigator.serviceWorker.register" not in html:
    html = html.replace('// INIT\n      renderCard(currentIndex);', sw_script + '\n      // INIT\n      renderCard(currentIndex);')


# 3. Dashboard UI
dashboard_html = """
    <div id="dashboard" style="display:flex; justify-content:center; gap:20px; background:#1e293b; padding:12px; margin: 10px 10px; border-radius:8px; font-weight:800; font-size:1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
      <span style="color:#94a3b8;">🌱 미학습 <span id="stat-new" style="color:#f8fafc;">0</span></span>
      <span style="color:#ef4444;">🔥 복습요망 <span id="stat-due" style="color:#fca5a5;">0</span></span>
      <span style="color:#10b981;">🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>
    </div>
"""
if "id=\"dashboard\"" not in html:
    html = html.replace('<div class="controls">', dashboard_html + '    <div class="controls">')

# Dashboard JS Logic
dashboard_js = """
    function updateDashboard() {
      let srsData = JSON.parse(localStorage.getItem('kice_srs') || '{}');
      const now = new Date().getTime();
      let countNew = 0, countDue = 0, countDone = 0;
      items.forEach(item => {
        if (!srsData[item.kw]) countNew++;
        else if (srsData[item.kw] <= now) countDue++;
        else countDone++;
      });
      document.getElementById('stat-new').innerText = countNew;
      document.getElementById('stat-due').innerText = countDue;
      document.getElementById('stat-done').innerText = countDone;
    }
"""
if "function updateDashboard()" not in html:
    html = html.replace('function renderCard(index) {', dashboard_js + '\n    function renderCard(index) {')

# Hook updateDashboard into renderCard and handleSRS
html = html.replace("elAns.innerText = item.ans;", "elAns.innerText = item.ans;\n        updateDashboard();")
html = html.replace("showRewardUI('right');\n      }", "showRewardUI('right');\n      }\n      updateDashboard();")


# 4. Voice Input (STT) UI and Logic
mic_btn = """
            <div style="text-align:right; margin-bottom:4px; padding-right:5px;">
              <button onclick="startDictation()" style="background:#ef4444; color:white; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; box-shadow:0 2px 4px rgba(0,0,0,0.2);">🎤 음성 답안 작성</button>
            </div>
"""
if "startDictation()" not in html:
    html = html.replace('<textarea id="c-input"', mic_btn + '            <textarea id="c-input"')

mic_js = """
    function startDictation() {
      if (window.hasOwnProperty('webkitSpeechRecognition') || window.hasOwnProperty('SpeechRecognition')) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.lang = 'ko-KR';
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.onstart = function() {
          document.getElementById('c-input').placeholder = '듣고 있습니다... 말씀해 주세요!';
        };
        recognition.onresult = function(e) {
          const t = e.results[0][0].transcript;
          const input = document.getElementById('c-input');
          input.value += (input.value ? ' ' : '') + t;
          input.placeholder = '실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요...';
        };
        recognition.onerror = function(e) { 
          alert('음성 인식 오류: ' + e.error); 
          document.getElementById('c-input').placeholder = '실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요...';
        };
        recognition.start();
      } else {
        alert('이 브라우저에서는 음성 인식을 지원하지 않습니다. (최신 크롬/사파리 브라우저를 이용해주세요)');
      }
    }
"""
if "function startDictation()" not in html:
    html = html.replace('function switchMode(mode) {', mic_js + '\n    function switchMode(mode) {')


# 5. Table Mode Answer Blind
ans_blind_css = """
    #table-body.hide-ans td:nth-child(4) {
      position: relative;
      cursor: pointer;
      background-color: #1e293b;
    }
    #table-body.hide-ans td:nth-child(4)::after {
      content: "🔒 마우스 올려서 공식 정답 확인";
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
    #table-body.hide-ans td:nth-child(4):hover::after { opacity: 0; }
    #table-body.hide-ans td:nth-child(4) > * { opacity: 0; filter: blur(4px); transition: 0.2s; }
    #table-body.hide-ans td:nth-child(4):hover > * { opacity: 1; filter: blur(0); }
    @media print {
      #table-body.hide-ans td:nth-child(4) { background-color: #fff !important; }
      #table-body.hide-ans td:nth-child(4)::after { display: none !important; }
      #table-body.hide-ans td:nth-child(4) > * { opacity: 1 !important; filter: blur(0) !important; }
    }
"""
if "#table-body.hide-ans" not in html:
    html = html.replace('/* PRINT OVERRIDES FOR HIDE-KW */', ans_blind_css + '\n    /* PRINT OVERRIDES FOR HIDE-KW */')

ans_btn_html = """
        <button class="btn-control" id="btn-toggle-ans" onclick="toggleTableAns()" style="background:#475569; border-color:#334155; color:#fff; width:auto; display:inline-block; padding: 8px 15px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-left:8px;">👀 공식 정답 가리기</button>
"""
if "toggleTableAns()" not in html:
    html = html.replace('👀 영역 및 표제어 가리기</button>', '👀 영역 및 표제어 가리기</button>' + ans_btn_html)

ans_js = """
    let isAnsHidden = false;
    function toggleTableAns() {
      isAnsHidden = !isAnsHidden;
      const tableBody = document.getElementById('table-body');
      const btn = document.getElementById('btn-toggle-ans');
      if (isAnsHidden) {
        tableBody.classList.add('hide-ans');
        btn.innerText = '👀 공식 정답 보이기';
        btn.style.background = '#facc15';
        btn.style.color = '#000';
      } else {
        tableBody.classList.remove('hide-ans');
        btn.innerText = '👀 공식 정답 가리기';
        btn.style.background = '#475569';
        btn.style.color = '#fff';
      }
    }
"""
if "function toggleTableAns()" not in html:
    html = html.replace('function toggleTableKw() {', ans_js + '\n    function toggleTableKw() {')


with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("All mega upgrades injected into HTML.")
