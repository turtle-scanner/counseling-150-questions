import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject missing JS logic (Pomodoro, Search, Confetti)
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
if "let pomoInterval;" not in html:
    html = html.replace('function getStars() {', js_upgrades + '\n    function getStars() {')

# 2. Tablet optimizations (Touch-friendly buttons, responsive gaps, no horizontal scrolling)
tablet_css = """
    /* TABLET OPTIMIZATIONS */
    @media (max-width: 900px) {
      .controls { flex-direction: row; flex-wrap: wrap; justify-content: center; gap: 8px !important; }
      .btn-control { min-width: 45%; padding: 12px 15px !important; font-size: 1.1rem !important; margin: 0 !important; }
      #search-input { width: 100% !important; margin: 5px 0 !important; font-size: 1.1rem !important; padding: 12px !important; }
      .btn-nav { padding: 15px !important; font-size: 1.2rem !important; }
      #pomodoro-bar { flex-wrap: wrap; }
      #pomodoro-bar button { padding: 10px 15px !important; font-size: 1.1rem !important; flex: 1; }
      #pomo-time { font-size: 1.6rem !important; }
      .kice-sheet-wrapper { padding: 5px !important; }
      .kice-sheet { padding: 10px 5px !important; }
      .answer-text { font-size: 1.5rem !important; line-height: 1.6 !important; }
      .card-q { font-size: 1.3rem !important; line-height: 1.5 !important; }
      .progress-container { margin: 10px 5px !important; }
      .progress-bar { height: 16px !important; }
      #p-text-container { font-size: 1.2rem !important; }
      .btn-mode { padding: 10px 5px !important; font-size: 1rem !important; }
    }
"""
if "/* TABLET OPTIMIZATIONS */" not in html:
    html = html.replace('</style>', tablet_css + '\n  </style>')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Missing JS and Tablet optimizations applied.")
