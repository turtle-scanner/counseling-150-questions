import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS Injection
css_to_add = """
    /* --- PREMIUM SUITE CSS (NO ASTERISKS) --- */
    .kw-highlight {
      background: rgba(245, 158, 11, 0.22) !important;
      color: #fef08a !important;
      padding: 1px 5px !important;
      border-radius: 4px !important;
      font-weight: 700 !important;
      border-bottom: 2px solid #f59e0b !important;
      display: inline !important;
    }
    .tag-highlight {
      color: #38bdf8 !important;
      font-weight: 700 !important;
      background: rgba(56, 189, 248, 0.15) !important;
      padding: 1px 5px !important;
      border-radius: 4px !important;
      margin-right: 4px !important;
      display: inline-block !important;
    }

    #timer90-container {
      display: none;
      width: 100%;
      background: #1e293b;
      border-radius: 6px;
      overflow: hidden;
      margin: 8px 0;
      height: 22px;
      position: relative;
      border: 1px solid #334155;
    }
    #timer90-bar {
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444);
      transition: width 1s linear;
    }
    #timer90-text {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.82rem;
      font-weight: 800;
      color: #ffffff;
      text-shadow: 0 1px 2px rgba(0,0,0,0.8);
      pointer-events: none;
    }

    .kice-canvas-wrapper {
      position: relative;
      width: 100%;
      height: 160px;
    }
    #kice-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10;
      touch-action: none;
      cursor: crosshair;
      background: transparent;
      display: none;
    }

    .stats-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 10000;
      padding: 15px;
    }
    .stats-modal {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 12px;
      width: 100%;
      max-width: 580px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 22px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.8);
      color: #f8fafc;
      font-family: 'Malgun Gothic', sans-serif;
    }
    .stats-bar-bg {
      flex: 1;
      height: 10px;
      background: #1e293b;
      border-radius: 5px;
      overflow: hidden;
      margin: 0 10px;
    }
    .stats-bar-fill {
      height: 100%;
      border-radius: 5px;
      transition: width 0.4s ease;
    }
"""

if '/* --- PREMIUM SUITE CSS (NO ASTERISKS) --- */' not in html:
    html = html.replace('</style>', css_to_add.strip() + '\n  </style>')
    print("[1] CSS injected successfully.")

# 2. Add Stats Button to Dashboard
stats_btn = """<button onclick="openStatsModal()" style="background:#1e293b; color:#38bdf8; border:1px solid #3b82f6; border-radius:6px; padding:3px 10px; font-size:0.85rem; cursor:pointer; font-weight:bold; margin-left:8px;">📊 8대 과목 진단</button>"""
if 'openStatsModal()' not in html:
    html = html.replace('🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>', '🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>\n      ' + stats_btn)
    print("[2] Stats Modal Button injected.")

# 3. Add 90s Timer Button in Controls
timer_btn = """<button class="btn-control" id="btn-timer90" onclick="toggleTimer90()" style="background:#1e293b; color:#cbd5e1;">⏱️ 90초 시험 (OFF)</button>"""
if 'id="btn-timer90"' not in html:
    html = html.replace('<button class="btn-control" id="btn-wrong"', timer_btn + '\n      <button class="btn-control" id="btn-wrong"')
    print("[3] 90s Timer Control Button injected.")

# 4. Add Timer Bar inside Card
timer_bar_markup = """
        <div id="timer90-container"><div id="timer90-bar"></div><div id="timer90-text">90초 남음</div></div>
"""
if 'id="timer90-container"' not in html:
    html = html.replace('<div class="card-q" id="c-q"', timer_bar_markup + '        <div class="card-q" id="c-q"')
    print("[4] Timer Bar markup injected.")

# 5. Add Canvas & Pen Buttons in Sheet Right
canvas_buttons = """<button id="btn-toggle-pen" onclick="toggleHandwriting()" style="background:#0284c7; color:white; border:none; padding:4px 10px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; margin-right:5px; box-shadow:0 2px 4px rgba(0,0,0,0.2);">✏️ 펜 쓰기 (S펜/터치)</button>
              <button id="btn-clear-pen" onclick="clearCanvas()" style="display:none; background:#64748b; color:white; border:none; padding:4px 8px; border-radius:4px; cursor:pointer; font-size:0.85rem; font-weight:800; margin-right:5px;">🗑️ 획 지우기</button>"""
if 'id="btn-toggle-pen"' not in html:
    html = html.replace('<button onclick="showChosungHint()"', canvas_buttons + '\n              <button onclick="showChosungHint()"')
    print("[5] Pen Buttons injected.")

# Wrap textarea with canvas
old_textarea = '<textarea id="c-input" class="kice-textarea" placeholder="실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요..."></textarea>'
new_wrapper = """<div class="kice-canvas-wrapper">
              <textarea id="c-input" class="kice-textarea" placeholder="실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하거나 상단 [✏️ 펜 쓰기] 버튼을 눌러 필기하세요..."></textarea>
              <canvas id="kice-canvas"></canvas>
            </div>"""
if 'class="kice-canvas-wrapper"' not in html and old_textarea in html:
    html = html.replace(old_textarea, new_wrapper)
    print("[6] Canvas wrapper & textarea injected.")

# 6. Add Stats Modal before </body>
stats_modal_markup = """
  <!-- 8대 과목별 학습 성취도 진단 모달 -->
  <div class="stats-overlay" id="stats-modal" onclick="closeStatsModal(event)">
    <div class="stats-modal" onclick="event.stopPropagation()">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; border-bottom:1px solid #334155; padding-bottom:10px;">
        <h3 style="margin:0; font-size:1.15rem; color:#fbbf24;">📊 8대 영역별 성취도 및 취약 과목 진단</h3>
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
    html = html.replace('</body>', stats_modal_markup.strip() + '\n</body>')
    print("[7] Stats Modal markup injected.")

# 7. JavaScript Logic
premium_js = """
    // --- 1. KEYWORD & TAG HIGHLIGHTER ---
    function applyHighlighter(text) {
      if (!text) return '';
      // Bracket tags like [핵심 장점], [2022 교육과정 효과], [상담 효과]
      let t = text.replace(/\\[([^\\]]+)\\]/g, '<span class="tag-highlight">[$1]</span>');
      // Single quotes like '영속적 이해', '빅 아이디어'
      t = t.replace(/'([^']+)'/g, "'<span class=\\"kw-highlight\\">$1</span>'");
      return t;
    }

    // --- 2. 90-SECOND COUNTDOWN EXAM TIMER ---
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
        btn.style.fontWeight = 'bold';
        barBox.style.display = 'block';
        resetTimer90();
      } else {
        btn.innerText = '⏱️ 90초 시험 (OFF)';
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.style.fontWeight = 'normal';
        barBox.style.display = 'none';
        clearInterval(timer90Interval);
      }
    }

    function resetTimer90() {
      clearInterval(timer90Interval);
      if (!isTimer90) return;
      
      timer90Seconds = 90;
      const bar = document.getElementById('timer90-bar');
      const txt = document.getElementById('timer90-text');
      if (bar) bar.style.width = '100%';
      if (txt) txt.innerText = '⏱️ 남은 시간: 90초 (권장 작성 시간)';
      
      timer90Interval = setInterval(() => {
        timer90Seconds--;
        const pct = (timer90Seconds / 90) * 100;
        if (bar) bar.style.width = pct + '%';
        if (txt) txt.innerText = '⏱️ 남은 시간: ' + timer90Seconds + '초';
        
        if (timer90Seconds <= 0) {
          clearInterval(timer90Interval);
          if (!isFlipped) {
            toggleFlip();
            alert('⏰ [90초 실전 제한시간 종료!]\\n실전 권장 작성 시간이 종료되어 KICE 공식 모범답안을 공개합니다.');
          }
        }
      }, 1000);
    }

    // --- 3. APPLE PENCIL / S-PEN HANDWRITING CANVAS ---
    let isHandwriting = false;
    let canvas = null, ctx = null;
    let isDrawing = false;
    let lastX = 0, lastY = 0;

    function initCanvas() {
      canvas = document.getElementById('kice-canvas');
      if (!canvas) return;
      ctx = canvas.getContext('2d');
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);

      canvas.addEventListener('pointerdown', (e) => {
        isDrawing = true;
        const rect = canvas.getBoundingClientRect();
        lastX = e.clientX - rect.left;
        lastY = e.clientY - rect.top;
        ctx.beginPath();
        ctx.arc(lastX, lastY, 1.2, 0, Math.PI * 2);
        ctx.fillStyle = '#1e3a8a';
        ctx.fill();
      });

      canvas.addEventListener('pointermove', (e) => {
        if (!isDrawing) return;
        e.preventDefault();
        const rect = canvas.getBoundingClientRect();
        const curX = e.clientX - rect.left;
        const curY = e.clientY - rect.top;

        ctx.strokeStyle = '#1e3a8a';
        let width = 2.5;
        if (e.pressure && e.pressure > 0) {
          width = e.pressure * 3.5 + 1.2;
        }
        ctx.lineWidth = width;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(curX, curY);
        ctx.stroke();

        lastX = curX;
        lastY = curY;
      });

      canvas.addEventListener('pointerup', () => { isDrawing = false; });
      canvas.addEventListener('pointercancel', () => { isDrawing = false; });
    }

    function resizeCanvas() {
      if (!canvas) return;
      const wrapper = canvas.parentElement;
      if (wrapper) {
        const dpr = window.devicePixelRatio || 1;
        const w = wrapper.clientWidth || 600;
        const h = 160;
        canvas.width = Math.round(w * dpr);
        canvas.height = Math.round(h * dpr);
        canvas.style.width = w + 'px';
        canvas.style.height = h + 'px';
        ctx = canvas.getContext('2d');
        ctx.scale(dpr, dpr);
      }
    }

    function toggleHandwriting() {
      isHandwriting = !isHandwriting;
      const cvs = document.getElementById('kice-canvas');
      const btn = document.getElementById('btn-toggle-pen');
      const clearBtn = document.getElementById('btn-clear-pen');

      if (isHandwriting) {
        resizeCanvas();
        cvs.style.display = 'block';
        clearBtn.style.display = 'inline-block';
        btn.innerText = '⌨️ 키보드 전환';
        btn.style.background = '#10b981';
      } else {
        cvs.style.display = 'none';
        clearBtn.style.display = 'none';
        btn.innerText = '✏️ 펜 쓰기 (S펜/터치)';
        btn.style.background = '#0284c7';
      }
    }

    function clearCanvas() {
      if (!ctx || !canvas) return;
      const dpr = window.devicePixelRatio || 1;
      ctx.clearRect(0, 0, canvas.width / dpr, canvas.height / dpr);
    }

    // --- 4. 8-SUBJECT DIAGNOSTIC RADAR MODAL ---
    function openStatsModal() {
      const modal = document.getElementById('stats-modal');
      const content = document.getElementById('stats-content');
      const srsData = JSON.parse(localStorage.getItem('kice_srs_data') || '{}');
      
      const categories = [
        { key: '교육', name: '🎓 교육학 (과정·방법·평가·행정)' },
        { key: '정신병리', name: '🧠 이상심리/DSM-5-TR' },
        { key: '가족', name: '👨‍👩‍👧 가족치료' },
        { key: '심리검사', name: '📊 심리검사/평가' },
        { key: '진로', name: '🧭 진로상담' },
        { key: '이론', name: '💡 상담이론·기법·치료' },
        { key: '위기', name: '🚨 위기·학폭법령·윤리' }
      ];

      const allItemsList = (typeof originalItems !== 'undefined' && originalItems.length > 0) ? originalItems : items;
      
      let overallMastered = 0;
      allItemsList.forEach(it => {
        const rec = srsData[it.kw];
        if (rec && rec.interval >= 5) overallMastered++;
      });
      const overallPct = Math.round((overallMastered / (allItemsList.length || 1)) * 100);

      let html = `
        <div style="background:#1e293b; padding:14px; border-radius:8px; border:1px solid #3b82f6; margin-bottom:18px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <span style="font-weight:bold; font-size:1.05rem; color:#60a5fa;">전체 학습 달성도</span>
            <span style="font-size:1.15rem; font-weight:800; color:#34d399;">${overallMastered} / ${allItemsList.length}문항 (${overallPct}%)</span>
          </div>
          <div class="stats-bar-bg" style="margin:0; height:12px;">
            <div class="stats-bar-fill" style="width:${overallPct}%; background:#10b981;"></div>
          </div>
        </div>
      `;

      categories.forEach(cat => {
        const catItems = allItemsList.filter(item => {
          const badge = item.badge || '';
          const kw = item.kw || '';
          if (cat.key === '교육') return badge.includes('교육') || badge.includes('교수');
          if (cat.key === '진로') return badge.includes('진로');
          if (cat.key === '심리검사') return badge.includes('검사');
          if (cat.key === '가족') return badge.includes('가족');
          if (cat.key === '정신병리') return badge.includes('병리') || badge.includes('이상') || kw.includes('장애');
          if (cat.key === '이론') return badge.includes('이론') || badge.includes('행동') || badge.includes('성격') || badge.includes('대인') || badge.includes('다문화');
          if (cat.key === '위기') return badge.includes('위기') || badge.includes('법령') || badge.includes('윤리') || badge.includes('놀이') || badge.includes('수퍼비전');
          return false;
        });

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
          <div style="background:#131d31; border:1px solid #1e293b; padding:12px 14px; border-radius:8px; margin-bottom:10px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span style="font-weight:bold; font-size:0.95rem;">${cat.name} (${catItems.length}문항)</span>
              <span style="color:${tagColor}; font-weight:800; font-size:0.9rem;">${pct}% 마스터 [${tag}]</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <div class="stats-bar-bg" style="margin:0;">
                <div class="stats-bar-fill" style="width:${pct}%; background:${barColor};"></div>
              </div>
              <button onclick="filterByCategory('${cat.key}'); closeStatsModal();" style="background:#334155; color:#38bdf8; border:1px solid #475569; border-radius:4px; padding:3px 8px; font-size:0.8rem; font-weight:bold; cursor:pointer; white-space:nowrap;">집중학습 ➔</button>
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

if 'function applyHighlighter' not in html:
    html = html.replace('// --- ADVANCED STUDY FEATURES', premium_js.strip() + '\n\n    // --- ADVANCED STUDY FEATURES')
    print("[8] JavaScript logic injected.")

# Connect applyHighlighter to renderCard
html = html.replace('elAns.innerHTML = formatText(item.ans);', 'elAns.innerHTML = applyHighlighter(formatText(item.ans));')

# Connect resetTimer90 and clearCanvas inside renderCard
if 'resetTimer90();' not in html:
    html = html.replace('updateDashboard();', 'updateDashboard();\n      resetTimer90();\n      clearCanvas();')
    print("[9] renderCard connected with resetTimer90 and clearCanvas.")

# Call initCanvas on window load
if 'initCanvas();' not in html:
    html = html.replace('renderCard(currentIndex);\n    initTable();', 'renderCard(currentIndex);\n    initTable();\n    initCanvas();')
    print("[10] initCanvas called at startup.")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("ALL PREMIUM FEATURES INJECTED 100% SUCCESSFULLY!")
