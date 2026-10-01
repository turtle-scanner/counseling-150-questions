import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Star Mode button to controls
star_btn_html = '<button class="btn-control" id="btn-starmode" onclick="toggleStarMode()" style="background:#1e293b; color:#cbd5e1;">⭐ 별표 모드</button>'
html = html.replace('<button class="btn-control" style="background:#10b981;', star_btn_html + '\n      <button class="btn-control" style="background:#10b981;')

# 2. Modify the Anki Card layout to include the Star button
old_badge = '<div class="card-badge" id="c-badge">영역</div>'
new_badge = """<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <div class="card-badge" id="c-badge" style="margin-bottom:0;">영역</div>
            <div id="c-star" onclick="toggleCurrentStar()" style="cursor:pointer; font-size:1.8rem; color:#facc15; transition:0.2s;">☆</div>
          </div>"""
html = html.replace(old_badge, new_badge)

# 3. Add originalItems and Star Logic in JS
# Find where custom items are loaded and items array is finalized
init_logic = """
    let originalItems = [];
    let isStarMode = false;
    
    // Call this at the end of window.onload or script execution
    setTimeout(() => { originalItems = [...items]; }, 500);

    function getStars() {
      return JSON.parse(localStorage.getItem('kice_stars') || '[]');
    }
    
    function toggleCurrentStar() {
      if (!items[currentIndex]) return;
      const kw = items[currentIndex].kw;
      let stars = getStars();
      if (stars.includes(kw)) {
        stars = stars.filter(k => k !== kw);
      } else {
        stars.push(kw);
      }
      localStorage.setItem('kice_stars', JSON.stringify(stars));
      updateStarUI();
    }
    
    function updateStarUI() {
      if (!items[currentIndex]) return;
      const kw = items[currentIndex].kw;
      const stars = getStars();
      const starEl = document.getElementById('c-star');
      if (starEl) {
        starEl.innerText = stars.includes(kw) ? '⭐' : '☆';
        starEl.style.transform = stars.includes(kw) ? 'scale(1.2)' : 'scale(1)';
      }
    }
    
    function toggleStarMode() {
      isStarMode = !isStarMode;
      const btn = document.getElementById('btn-starmode');
      if (isStarMode) {
        const stars = getStars();
        const starredItems = originalItems.filter(item => stars.includes(item.kw));
        if (starredItems.length === 0) {
          alert('별표(⭐) 표시된 문제가 없습니다! 어려운 문제에 별표를 먼저 눌러주세요.');
          isStarMode = false;
          return;
        }
        items = starredItems;
        btn.style.background = '#facc15';
        btn.style.color = '#000';
        btn.innerText = '⭐ 별표 모드 (ON)';
      } else {
        items = [...originalItems];
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '⭐ 별표 모드 (OFF)';
      }
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
    }
"""

if "function toggleStarMode()" not in html:
    html = html.replace('function renderCard(index) {', init_logic + '\n    function renderCard(index) {')

# 4. Inject updateStarUI() inside renderCard()
html = html.replace("document.getElementById('c-q').innerHTML = item.q;", "document.getElementById('c-q').innerHTML = item.q;\n      updateStarUI();")

# 5. Fix custom item loading to ensure originalItems gets populated immediately
html = html.replace("let items = [", "let items = [") # placeholder to hook if needed, but the setTimeout does the trick.

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Star mode and logic injected.")
