import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS for Canvas, Highlighter, 90s Timer, and Stats Modal
premium_css = """
    /* --- ALL PREMIUM FEATURES CSS --- */
    /* 1. Keyword Highlighter in Answers */
    .kw-highlight {
      background: rgba(245, 158, 11, 0.22) !important;
      color: #fef08a !important;
      padding: 1px 4px !important;
      border-radius: 3px !important;
      font-weight: 700 !important;
      border-bottom: 2px solid #f59e0b !important;
      display: inline-block;
    }
    .tag-highlight {
      color: #38bdf8 !important;
      font-weight: 700 !important;
      margin-right: 2px;
    }
    
    /* 2. 90-Second Timer Bar */
    #timer90-container {
      display: none;
      width: 100%;
      background: #1e293b;
      border-radius: 6px;
      overflow: hidden;
      margin: 8px 0;
      height: 8px;
      position: relative;
    }
    #timer90-bar {
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444);
      transition: width 1s linear;
    }
    #timer90-badge {
      display: none;
      font-size: 0.88rem;
      font-weight: 800;
      color: #f59e0b;
      margin-left: 8px;
    }

    /* 3. Handwriting Canvas */
    #kice-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 160px;
      z-index: 5;
      touch-action: none;
      cursor: crosshair;
    }
    
    /* 4. Stats Modal */
    .stats-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.85);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 10000;
      padding: 15px;
    }
    .stats-modal {
      background: #111827;
      border: 1px solid #334155;
      border-radius: 12px;
      width: 100%;
      max-width: 520px;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.7);
      color: #f8fafc;
      font-family: 'Malgun Gothic', sans-serif;
    }
    .stats-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      gap: 10px;
    }
    .stats-bar-bg {
      flex: 1;
      height: 10px;
      background: #1e293b;
      border-radius: 5px;
      overflow: hidden;
    }
    .stats-bar-fill {
      height: 100%;
      border-radius: 5px;
      transition: width 0.4s ease;
    }
"""

if '/* --- ALL PREMIUM FEATURES CSS --- */' not in html:
    html = html.replace('</style>', premium_css.strip() + '\n  </style>')

# 2. Add Stats Button to Dashboard
dashboard_stats_btn = """<button onclick="openStatsModal()" style="background:#1e293b; color:#38bdf8; border:1px solid #3b82f6; border-radius:6px; padding:3px 10px; font-size:0.85rem; cursor:pointer; font-weight:bold; margin-left:8px;">📊 취약과목 진단</button>"""
if 'openStatsModal()' not in html:
    html = html.replace('🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>', '🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>\n      ' + dashboard_stats_btn)

# 3. Add 90s Timer button in controls and timer display above card
timer_btn_html = """<button class="btn-control" id="btn-timer90" onclick="toggleTimer90()" style="background:#1e293b; color:#cbd5e1;">⏱️ 90초 시험 (OFF)</button>"""
if 'id="btn-timer90"' not in html:
    html = html.replace('<button class="btn-control" id="btn-wrong"', timer_btn_html + '\n      <button class="btn-control" id="btn-wrong"')

# Add timer bar inside anki card right above card-q
timer_bar_html = """
        <div id="timer90-container"><div id="timer90-bar"></div></div>
"""
if 'id="timer90-container"' not in html:
    html = html.replace('<div class="card-q" id="c-q"', timer_bar_html + '        <div class="card-q" id="c-q"')

# 4. Add Handwriting Canvas & Buttons inside kice-sheet-right
canvas_buttons_html = """<button id="btn-toggle-pen" onclick="toggleHandwriting()" style="background:#0284c7; color:white; border:none; padding:4px 10px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; margin-right:5px; box-shadow:0 2px 4px rgba(0,0,0,0.2);">✏️ 펜 쓰기 (S펜/터치)</button>
              <button id="btn-clear-pen" onclick="clearCanvas()" style="display:none; background:#64748b; color:white; border:none; padding:4px 8px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; margin-right:5px;">🗑️ 지우기</button>"""

if 'id="btn-toggle-pen"' not in html:
    html = html.replace('<button onclick="showChosungHint()"', canvas_buttons_html + '\n              <button onclick="showChosungHint()"')

canvas_tag_html = """<canvas id="kice-canvas" width="800" height="160" style="display:none;"></canvas>"""
if 'id="kice-canvas"' not in html:
    html = html.replace('<textarea id="c-input"', canvas_tag_html + '\n            <textarea id="c-input"')

# 5. Add Stats Modal HTML before </body>
stats_modal_html = """
  <!-- SUBJECT DIAGNOSTIC RADAR MODAL -->
  <div class="stats-overlay" id="stats-modal" onclick="closeStatsModal(event)">
    <div class="stats-modal" onclick="event.stopPropagation()">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; border-bottom:1px solid #334155; padding-bottom:10px;">
        <h3 style="margin:0; font-size:1.2rem; color:#fbbf24;">📊 8대 과목별 학습 성취도 및 취약 영역 진단</h3>
        <button onclick="closeStatsModal()" style="background:none; border:none; color:#94a3b8; font-size:1.5rem; cursor:pointer;">&times;</button>
      </div>
      <div id="stats-content">
        <!-- Rendered by JS -->
      </div>
      <button onclick="closeStatsModal()" style="width:100%; background:#3b82f6; color:#fff; border:none; padding:10px; border-radius:8px; font-weight:bold; margin-top:15px; cursor:pointer;">닫기</button>
    </div>
  </div>
"""
if 'id="stats-modal"' not in html:
    html = html.replace('</body>', stats_modal_html.strip() + '\n</body>')

# 6. JavaScript Logic for All 4 Features
premium_js_logic = """
    // --- 1. KEYWORD HIGHLIGHTER IN FORMATTEXT ---
    function applyHighlighter(text) {
      if (!text) return '';
      // Highlight single quoted terms '...'
      let t = text.replace(/'([^']+)'/g, "'<span class=\\"kw-highlight\\">$1</span>'");
      // Highlight bracketed tags [핵심 장점], [2022 교육과정 효과] etc.
      t = t.replace(/\\[([^\\]]+)\\]/g, '<span class=\\"tag-highlight\\">[$1]</span>');
      return t;
    }

    // --- 2. 90-SECOND TIMED ATTACK MODE ---
    let isTimer90 = false;
    let timer90Interval = null;
    let timer90Seconds = 90;

    function toggleTimer90() {
      isTimer90 = !isTimer90;
      const btn = document.getElementById('btn-timer90');
      const barBox = document.getElementById('timer90-container');
      if (isTimer90) {
        btn.innerText = '⏱️ 90초 시험 (ON)';
        btn.style.background = '#f59e0b';
        btn.style.color = '#000';
        barBox.style.display = 'block';
        resetTimer90();
      } else {
        btn.innerText = '⏱️ 90초 시험 (OFF)';
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        barBox.style.display = 'none';
        clearInterval(timer90Interval);
      }
    }

    function resetTimer90() {
      clearInterval(timer90Interval);
      if (!isTimer90) return;
      
      timer90Seconds = 90;
      const bar = document.getElementById('timer90-bar');
      bar.style.width = '100%';
      
      timer90Interval = setInterval(() => {
        timer90Seconds--;
        const pct = (timer90Seconds / 90) * 100;
        bar.style.width = pct + '%';
        
        if (timer90Seconds <= 0) {
          clearInterval(timer90Interval);
          // Auto flip when time expires
          if (document.getElementById('c-back').style.display === 'none') {
            toggleFlip();
            alert('⏰ [90초 시간 종료!] 실전 권장 작성 시간이 종료되어 공식 정답을 공개합니다.');
          }
        }
      }, 1000);
    }

    // --- 3. APPLE PENCIL / S-PEN HANDWRITING CANVAS ---
    let isHandwriting = false;
    let canvas, ctx;
    let isDrawing = false;
    let lastX = 0, lastY = 0;

    function initCanvas() {
      canvas = document.getElementById('kice-canvas');
      if (!canvas) return;
      ctx = canvas.getContext('2d');
      
      // Auto resize canvas to wrapper width
      function resizeCanvas() {
        const wrapper = document.querySelector('.kice-sheet-right');
        if (wrapper) {
          canvas.width = wrapper.clientWidth;
          canvas.height = 160;
        }
      }
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);

      canvas.addEventListener('pointerdown', (e) => {
        isDrawing = true;
        const rect = canvas.getBoundingClientRect();
        lastX = e.clientX - rect.left;
        lastY = e.clientY - rect.top;
      });

      canvas.addEventListener('pointermove', (e) => {
        if (!isDrawing) return;
        const rect = canvas.getBoundingClientRect();
        const curX = e.clientX - rect.left;
        const curY = e.clientY - rect.top;

        ctx.strokeStyle = '#1e3a8a';
        ctx.lineWidth = e.pressure ? (e.pressure * 4 + 1.5) : 2.5; // Pressure sensitivity for S-Pen/Apple Pencil
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(curX, curY);
        ctx.stroke();

        lastX = curX;
        lastY = curY;
      });

      canvas.addEventListener('pointerup', () => isDrawing = false);
      canvas.addEventListener('pointercancel', () => isDrawing = false);
    }

    function toggleHandwriting() {
      isHandwriting = !isHandwriting;
      const cvs = document.getElementById('kice-canvas');
      const btn = document.getElementById('btn-toggle-pen');
      const clearBtn = document.getElementById('btn-clear-pen');
      const txt = document.getElementById('c-input');

      if (isHandwriting) {
        cvs.style.display = 'block';
        clearBtn.style.display = 'inline-block';
        btn.innerText = '⌨️ 키보드 입력 전환';
        btn.style.background = '#10b981';
        txt.style.pointerEvents = 'none'; // pass touch to canvas
      } else {
        cvs.style.display = 'none';
        clearBtn.style.display = 'none';
        btn.innerText = '✏️ 펜 쓰기 (S펜/터치)';
        btn.style.background = '#0284c7';
        txt.style.pointerEvents = 'auto';
      }
    }

    function clearCanvas() {
      if (!ctx || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    // --- 4. SUBJECT DIAGNOSTIC RADAR MODAL ---
    function openStatsModal() {
      const modal = document.getElementById('stats-modal');
      const content = document.getElementById('stats-content');
      const srsData = JSON.parse(localStorage.getItem('kice_srs_data') || '{}');
      
      const categories = [
        { key: '교육', name: '🎓 교육학' },
        { key: '진로', name: '🧭 진로상담' },
        { key: '심리검사', name: '📊 심리검사' },
        { key: '가족', name: '👨‍👩‍👧 가족치료' },
        { key: '정신병리', name: '🧠 이상심리/DSM-5' },
        { key: '이론', name: '💡 상담이론·치료' },
        { key: '위기', name: '🚨 위기·법령·윤리' }
      ];

      let html = '';
      categories.forEach(cat => {
        const catItems = originalItems.filter(it => (it.badge && it.badge.includes(cat.key)) || (it.kw && it.kw.includes(cat.key)));
        const total = catItems.length || 1;
        let mastered = 0;
        let weak = 0;

        catItems.forEach(it => {
          const rec = srsData[it.kw];
          if (rec && rec.interval >= 5) mastered++;
          else if (rec && rec.interval <= 1) weak++;
        });

        const pct = Math.round((mastered / total) * 100);
        let tag = pct >= 70 ? '👏 우수' : (weak > 0 ? '🔥 취약' : '🌱 학습중');
        let tagColor = pct >= 70 ? '#10b981' : (weak > 0 ? '#ef4444' : '#38bdf8');
        let barColor = pct >= 70 ? '#10b981' : (weak > 0 ? '#f59e0b' : '#3b82f6');

        html += `
          <div style="margin-bottom:14px;">
            <div style="display:flex; justify-content:space-between; font-size:0.95rem; margin-bottom:4px;">
              <span><b>${cat.name}</b> (${catItems.length}문항)</span>
              <span style="color:${tagColor}; font-weight:bold;">${pct}% 마스터 [${tag}]</span>
            </div>
            <div class="stats-bar-bg">
              <div class="stats-bar-fill" style="width:${pct}%; background:${barColor};"></div>
            </div>
          </div>
        `;
      });

      content.innerHTML = html;
      modal.style.display = 'flex';
    }

    function closeStatsModal(e) {
      document.getElementById('stats-modal').style.display = 'none';
    }
"""

if 'applyHighlighter' not in html:
    html = html.replace('// --- ADVANCED STUDY FEATURES', premium_js_logic.strip() + '\n\n    // --- ADVANCED STUDY FEATURES')

# Update formatText to call applyHighlighter
html = html.replace("elAns.innerHTML = formatText(item.ans);", "elAns.innerHTML = applyHighlighter(formatText(item.ans));")

# Call initCanvas on window load and resetTimer90 on renderCard
html = html.replace("renderCard(currentIndex);", "renderCard(currentIndex);\n    initCanvas();")
html = html.replace("warningCount = 0;", "warningCount = 0;\n        resetTimer90();\n        clearCanvas();")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected all 4 premium features!")
