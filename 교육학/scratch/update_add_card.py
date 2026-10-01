import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add the "Add Card" button to the controls
add_btn_html = '<button class="btn-control" style="background:#8b5cf6; border-color:#7c3aed; color:#fff;" onclick="openAddCardModal()">➕ 새 문제 추가</button>'
html = html.replace('<button class="btn-control btn-print"', add_btn_html + '\n    <button class="btn-control btn-print"')

# 2. Add the Modal HTML right before <script>
modal_html = """
  <!-- Add Card Modal -->
  <div class="modal-overlay" id="add-modal">
    <div class="modal-content" style="text-align: left; max-width: 500px;">
      <div class="modal-title" style="margin-bottom:15px; color:#fbbf24;">📝 나만의 문제 추가하기</div>
      <p style="color:#94a3b8; font-size:0.9rem; margin-bottom:15px; line-height:1.4;">추가된 문제는 현재 사용 중인 브라우저(기기)에만 안전하게 저장됩니다.</p>
      
      <div style="margin-bottom: 12px;">
        <label style="color:#94a3b8; font-size:0.9rem; font-weight:bold;">영역 (예: 가족치료)</label>
        <input type="text" id="new-badge" style="width:100%; padding:12px; background:#0f1117; color:#fff; border:1px solid #334155; border-radius:6px; margin-top:5px; box-sizing:border-box;" placeholder="영역을 입력하세요">
      </div>
      <div style="margin-bottom: 12px;">
        <label style="color:#94a3b8; font-size:0.9rem; font-weight:bold;">표제어 (핵심 정답)</label>
        <input type="text" id="new-kw" style="width:100%; padding:12px; background:#0f1117; color:#fff; border:1px solid #334155; border-radius:6px; margin-top:5px; box-sizing:border-box;" placeholder="예: 가장기법">
      </div>
      <div style="margin-bottom: 12px;">
        <label style="color:#94a3b8; font-size:0.9rem; font-weight:bold;">문제 단서 (현상학적 단서)</label>
        <textarea id="new-q" style="width:100%; height:80px; padding:12px; background:#0f1117; color:#fff; border:1px solid #334155; border-radius:6px; margin-top:5px; box-sizing:border-box; resize:none;" placeholder="내담자의 증상이나 지문 내용을 적어주세요"></textarea>
      </div>
      <div style="margin-bottom: 20px;">
        <label style="color:#94a3b8; font-size:0.9rem; font-weight:bold;">공식 정답 (서술형 해설)</label>
        <textarea id="new-ans" style="width:100%; height:80px; padding:12px; background:#0f1117; color:#fff; border:1px solid #334155; border-radius:6px; margin-top:5px; box-sizing:border-box; resize:none;" placeholder="모범 답안을 적어주세요"></textarea>
      </div>
      
      <div style="display:flex; gap:10px;">
        <button style="flex:1; background:#8b5cf6; color:#fff; border:none; padding:14px; border-radius:8px; cursor:pointer; font-weight:800; font-size:1.05rem;" onclick="saveNewCard()">💾 저장하기</button>
        <button style="flex:1; background:#475569; color:#fff; border:none; padding:14px; border-radius:8px; cursor:pointer; font-weight:800; font-size:1.05rem;" onclick="closeAddCardModal()">취소</button>
      </div>
    </div>
  </div>
"""
html = html.replace('  <script>', modal_html + '\n  <script>')

# 3. Modify JS to use `let items` and load from localStorage
# Replace "const items = [{" with "let items = [{"
html = re.sub(r'const items = \[', 'let items = [', html)

js_addition = """
    // Load custom items from local storage
    const customItems = JSON.parse(localStorage.getItem('kice_custom_items') || '[]');
    items = items.concat(customItems);

    function openAddCardModal() {
      document.getElementById('add-modal').style.display = 'flex';
    }
    
    function closeAddCardModal() {
      document.getElementById('add-modal').style.display = 'none';
    }

    function saveNewCard() {
      const badge = document.getElementById('new-badge').value.trim() || '추가문제';
      const kw = document.getElementById('new-kw').value.trim();
      const q = document.getElementById('new-q').value.trim();
      const ans = document.getElementById('new-ans').value.trim();
      
      if(!kw || !q) {
        alert('표제어와 문제 단서는 필수 입력입니다!');
        return;
      }
      
      const newItem = { badge, kw, q, ans };
      
      // Save to local storage
      const saved = JSON.parse(localStorage.getItem('kice_custom_items') || '[]');
      saved.push(newItem);
      localStorage.setItem('kice_custom_items', JSON.stringify(saved));
      
      // Update running memory
      items.push(newItem);
      
      // Clear form
      document.getElementById('new-badge').value = '';
      document.getElementById('new-kw').value = '';
      document.getElementById('new-q').value = '';
      document.getElementById('new-ans').value = '';
      
      closeAddCardModal();
      alert('문제가 성공적으로 추가되었습니다!');
      
      // Refresh UI
      totalPages = Math.ceil(items.length / itemsPerPage);
      initTable();
      renderCard(currentIndex);
    }
"""

# Insert JS logic right after the items array is declared.
# Find the end of items array declaration: "];\n"
html = re.sub(r'(let items = \[.*?\];)', r'\1' + js_addition, html, flags=re.DOTALL)

# Re-evaluate totalPages dynamically in initTable / render logic
html = html.replace('const totalPages = Math.ceil(items.length / itemsPerPage);', 'let totalPages = Math.ceil(items.length / itemsPerPage);')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Add Card feature implemented successfully.")
