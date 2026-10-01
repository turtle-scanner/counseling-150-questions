import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update save/load logic for persistent card state
persistent_logic = """
      // PERSISTENT INDEX
      const lastKw = localStorage.getItem('kice_last_kw');
      if (lastKw) {
        const foundIdx = items.findIndex(item => item.kw === lastKw);
        if (foundIdx !== -1) currentIndex = foundIdx;
      }
"""
if "const lastKw = localStorage.getItem('kice_last_kw');" not in html:
    html = html.replace('renderCard(currentIndex);', persistent_logic + '\n      renderCard(currentIndex);', 1)

# Ensure currentIndex saves on every render
render_save_logic = """
        elAns.innerText = item.ans;
        updateDashboard();
        
        // Save current card so user can resume after refresh
        localStorage.setItem('kice_last_kw', item.kw);
"""
html = html.replace("elAns.innerText = item.ans;\n        updateDashboard();", render_save_logic)


# 2. Add a tiny UI hint about keyboard shortcuts for the Textarea
hint_ui = """
              <div style="font-size:0.75rem; color:#94a3b8; text-align:right; margin-top:3px;">
                💡 <b>단축키 팁</b>: 답안 작성 중엔 <b>[ESC]</b>를 눌러 커서를 뺀 후, <b>스페이스바</b>(정답확인), <b>➔</b>(다음카드)를 누르세요.
              </div>
"""
if "단축키 팁" not in html:
    html = html.replace('</textarea>', '</textarea>\n' + hint_ui)


with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Persistent index and UI hints applied.")
