import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Backup / Restore Buttons to Controls
backup_html = """
      <button class="btn-control" style="background:#4b5563; border-color:#374151; color:#fff;" onclick="exportData()">📥 백업</button>
      <button class="btn-control" style="background:#4b5563; border-color:#374151; color:#fff;" onclick="document.getElementById('import-file').click()">📤 복원</button>
      <input type="file" id="import-file" style="display:none" accept=".json" onchange="importData(event)">
"""
if "exportData()" not in html:
    html = html.replace('<button class="btn-control btn-print" onclick="window.print()">🖨️ 인쇄하기 (전체)</button>',
                        '<button class="btn-control btn-print" onclick="window.print()">🖨️ 인쇄하기 (전체)</button>' + backup_html)

# 2. Add Export/Import JS
backup_js = """
    function exportData() {
      const customItems = localStorage.getItem('kice_custom_items');
      if (!customItems) {
        alert('저장된 나만의 문제가 없습니다.');
        return;
      }
      const blob = new Blob([customItems], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'kice_custom_cards_backup.json';
      a.click();
      URL.revokeObjectURL(url);
    }
    
    function importData(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          if (Array.isArray(data)) {
            localStorage.setItem('kice_custom_items', JSON.stringify(data));
            alert('성공적으로 복원되었습니다! 페이지를 새로고침합니다.');
            location.reload();
          } else {
            alert('잘못된 파일 형식입니다.');
          }
        } catch (err) {
          alert('파일을 읽는 중 오류가 발생했습니다.');
        }
      };
      reader.readAsText(file);
    }
"""
if "function exportData()" not in html:
    html = html.replace('function shuffleCards() {', backup_js + '\n    function shuffleCards() {')

# 3. Update toggleFlip() to include Auto-Grader Logic
# We need to find the existing toggleFlip and replace it entirely.
old_toggleFlip_regex = r'function toggleFlip\(\)\s*\{[\s\S]*?\}[\s\n]*(?=function showReward)'

new_toggleFlip = """function toggleFlip() {
      const elBack = document.getElementById('c-back');
      const btn = document.getElementById('btn-flip');
      const isHidden = (elBack.style.display === 'none' || elBack.style.display === '');
      
      if (isHidden) {
        elBack.style.display = 'block';
        btn.innerText = '🙈 다시 숨기기';
        btn.classList.add('flipped');
        
        // --- AUTO GRADER LOGIC ---
        const userAnswer = document.getElementById('c-input').value.trim();
        const officialAnswer = items[currentIndex].ans;
        
        if (userAnswer.length > 0) {
          const words = officialAnswer.split(' ');
          let highlightedAns = '';
          words.forEach(word => {
            const cleanWord = word.replace(/[.,!?()]/g, '');
            if (cleanWord.length > 1 && userAnswer.includes(cleanWord)) {
              highlightedAns += `<span style="color:#4ade80; font-weight:800;">${word}</span> `;
            } else if (cleanWord.length <= 1) {
              highlightedAns += `${word} `;
            } else {
              highlightedAns += `<span style="color:#f87171; text-decoration:underline;">${word}</span> `;
            }
          });
          document.getElementById('c-ans').innerHTML = highlightedAns + '<br><span style="font-size:0.8rem; color:#94a3b8; display:block; margin-top:8px;">(초록: 키워드 적중 / 빨강: 누락)</span>';
        } else {
          document.getElementById('c-ans').innerText = officialAnswer;
        }
        // -------------------------
        
      } else {
        elBack.style.display = 'none';
        btn.innerText = '💡 정답 확인하기 (뒤집기)';
        btn.classList.remove('flipped');
      }
    }"""

html = re.sub(old_toggleFlip_regex, new_toggleFlip + '\n    ', html)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Auto-grader and backup features injected.")
