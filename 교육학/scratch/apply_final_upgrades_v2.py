import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Pomodoro Timer UI
pomodoro_html = """
    <div id="pomodoro-bar" style="display:flex; justify-content:center; align-items:center; gap:12px; padding:8px; background:#020617; border-bottom:1px solid #1e293b;">
      <span id="pomo-time" style="font-size:1.3rem; font-weight:900; color:#ef4444; font-family:monospace; letter-spacing:1px;">25:00</span>
      <button onclick="startPomodoro(25)" style="background:#ef4444; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-weight:bold; cursor:pointer;">🍅 25분 집중</button>
      <button onclick="startPomodoro(5)" style="background:#3b82f6; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-weight:bold; cursor:pointer;">☕ 5분 휴식</button>
    </div>
"""
if "pomodoro-bar" not in html:
    html = html.replace('<div class="app-header">', pomodoro_html + '    <div class="app-header">')

# 2. Add Search Bar UI
search_html = """
      <input type="text" id="search-input" placeholder="🔍 키워드 검색..." oninput="handleSearch()" style="padding:8px; border-radius:6px; border:1px solid #334155; background:#1e293b; color:#f8fafc; font-weight:bold; width:140px; margin-right:5px; transition:0.3s; font-family:'Malgun Gothic', sans-serif;">
"""
if "search-input" not in html:
    html = html.replace('<div class="controls">', '<div class="controls">\n' + search_html)

# 3. Add JS Logic for Pomodoro, Search, and Confetti
js_upgrades = """
    // --- POMODORO LOGIC ---
    let pomoInterval;
    function startPomodoro(minutes) {
      clearInterval(pomoInterval);
      let time = minutes * 60;
      const el = document.getElementById('pomo-time');
      el.style.color = minutes === 25 ? '#ef4444' : '#3b82f6';
      
      pomoInterval = setInterval(() => {
        time--;
        let m = Math.floor(time / 60).toString().padStart(2, '0');
        let s = (time % 60).toString().padStart(2, '0');
        el.innerText = `${m}:${s}`;
        
        if (time <= 0) {
          clearInterval(pomoInterval);
          if (minutes === 25) {
            alert('🍅 집중 시간이 끝났습니다! 5분 휴식을 취하세요.');
            speakTextClean('집중 시간이 끝났습니다. 정말 고생하셨어요. 5분만 쉴까요?');
          } else {
            alert('☕ 휴식이 끝났습니다! 다시 집중해볼까요?');
            speakTextClean('휴식이 끝났습니다. 다시 힘내서 시작해봐요, 화이팅!');
          }
        }
      }, 1000);
    }
    
    // --- SEARCH LOGIC ---
    let searchQuery = '';
    function handleSearch() {
      searchQuery = document.getElementById('search-input').value.trim().toLowerCase();
      let baseItems = originalItems;
      
      if (isStarMode) {
        const stars = getStars();
        baseItems = originalItems.filter(item => stars.includes(item.kw));
      }
      
      if (searchQuery === '') {
        items = baseItems;
      } else {
        items = baseItems.filter(item => 
          (item.q && item.q.toLowerCase().includes(searchQuery)) || 
          (item.ans && item.ans.toLowerCase().includes(searchQuery)) || 
          (item.kw && item.kw.toLowerCase().includes(searchQuery))
        );
      }
      
      if (items.length === 0) {
        document.getElementById('c-q').innerHTML = '<span style="color:#f87171;">검색 결과가 없습니다.</span>';
        document.getElementById('c-input').value = '';
        document.getElementById('c-back').style.display = 'none';
        return;
      }
      
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
    }
    
    // --- CONFETTI & DASHBOARD UPGRADE ---
    let lastDueCount = -1;
    function fireConfetti() {
      speakTextClean('오늘 예정된 복습을 모두 완료하셨습니다. 완벽해요!');
      for (let i = 0; i < 70; i++) {
        let conf = document.createElement('div');
        conf.style.position = 'fixed';
        conf.style.width = (Math.random() * 10 + 5) + 'px';
        conf.style.height = (Math.random() * 10 + 5) + 'px';
        conf.style.backgroundColor = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6'][Math.floor(Math.random() * 6)];
        conf.style.left = Math.random() * 100 + 'vw';
        conf.style.top = '-20px';
        conf.style.zIndex = '99999';
        conf.style.opacity = '0.9';
        conf.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
        conf.style.pointerEvents = 'none';
        conf.style.transition = 'top 3s ease-in, transform 3s ease-out, opacity 3s';
        document.body.appendChild(conf);
        
        setTimeout(() => {
          conf.style.top = '100vh';
          conf.style.transform = `rotate(${Math.random() * 1080}deg) translateX(${Math.random() * 200 - 100}px)`;
          conf.style.opacity = '0';
        }, 50);
        
        setTimeout(() => conf.remove(), 3000);
      }
    }
"""
if "startPomodoro" not in html:
    html = html.replace('function getStars() {', js_upgrades + '\n    function getStars() {')

# Hook Confetti into updateDashboard
new_dashboard_logic = """
      document.getElementById('stat-new').innerText = countNew;
      document.getElementById('stat-due').innerText = countDue;
      document.getElementById('stat-done').innerText = countDone;
      
      if (lastDueCount > 0 && countDue === 0 && countDone > 0) {
        fireConfetti();
      }
      lastDueCount = countDue;
"""
old_dashboard_logic = """
      document.getElementById('stat-new').innerText = countNew;
      document.getElementById('stat-due').innerText = countDue;
      document.getElementById('stat-done').innerText = countDone;
"""
if "fireConfetti()" not in html:
    html = html.replace(old_dashboard_logic.strip(), new_dashboard_logic.strip())

# 4. Font Fixes (KICE Batang for body, Malgun Gothic for Answers)
font_css = """
    /* FONT UPGRADES */
    body, .app-header, .table-container, .card-q {
      font-family: "Batang", "바탕", "KoPub Batang", "Nanum Myeongjo", serif !important;
    }
    .kice-textarea, .answer-text, #search-input, .btn-control {
      font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;
    }
    .card-q { font-size: 1.15rem; line-height: 1.6; }
    .answer-text { font-size: 1.15rem; line-height: 1.6; font-weight: bold; }
"""
if "/* FONT UPGRADES */" not in html:
    html = html.replace('</style>', font_css + '\n  </style>')


with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("All final features and fonts applied.")
