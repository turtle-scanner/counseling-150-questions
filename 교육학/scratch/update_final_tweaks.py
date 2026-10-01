import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Height adjustment for kice-textarea to exactly 4 lines
# 4 lines * 40px = 160px
html = html.replace('.kice-textarea {\n      width: 100%;\n      height: 120px;', '.kice-textarea {\n      width: 100%;\n      height: 160px;')

# 2. Add Shuffle Button
shuffle_btn_html = '<button class="btn-control" style="background:#10b981; border-color:#059669; color:#fff;" onclick="shuffleCards()">🔀 카드 섞기</button>'
# Insert it after the Add Card button
html = html.replace('<button class="btn-control btn-print"', shuffle_btn_html + '\n    <button class="btn-control btn-print"')

# 3. Add Shuffle JS
shuffle_js = """
    function shuffleCards() {
      // Fisher-Yates shuffle
      for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
      }
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
      alert('카드가 무작위로 섞였습니다!');
    }
"""
html = html.replace('function openAddCardModal()', shuffle_js + '\n    function openAddCardModal()')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Added 4-line textarea and Shuffle button.")
