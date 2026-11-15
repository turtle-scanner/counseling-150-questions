# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1. troop-promotion-modal 에 배경/박스 어디든 클릭 시 닫힘 + 1.8초 후 자동 닫힘 적용
old_promo_div = '<div id="troop-promotion-modal" class="fixed inset-0 modal-backdrop z-[9999999] hidden flex items-center justify-center p-3 bg-black/90">'
new_promo_div = '<div id="troop-promotion-modal" onclick="closeModal(\'troop-promotion-modal\')" class="fixed inset-0 modal-backdrop z-[9999999] hidden flex items-center justify-center p-3 bg-black/90 cursor-pointer">'
if old_promo_div in html:
    html = html.replace(old_promo_div, new_promo_div)
    print('Updated troop-promotion-modal backdrop onclick')

# 2. openModal('troop-promotion-modal') 호출 시 1.8초 뒤 자동 닫힘 보장 (openModal 함수 업그레이드)
auto_close_patch = '''
    // Override openModal & closeModal so troop-promotion-modal auto-dismisses after 1.8s and never blocks UI
    let _promoAutoCloseTimer = null;
    function openModal(id) {
      const el = document.getElementById(id);
      if (!el) return;
      el.classList.remove('hidden');
      el.style.display = 'flex';
      el.style.pointerEvents = 'auto';
      if (id === 'troop-promotion-modal') {
        if (_promoAutoCloseTimer) clearTimeout(_promoAutoCloseTimer);
        _promoAutoCloseTimer = setTimeout(() => {
          closeModal('troop-promotion-modal');
        }, 1800);
      }
    }
    function closeModal(id) {
      try {
        if (id === 'troop-promotion-modal' && _promoAutoCloseTimer) {
          clearTimeout(_promoAutoCloseTimer);
          _promoAutoCloseTimer = null;
        }
        const el = document.getElementById(id);
        if (el) {
          el.classList.add('hidden');
          el.style.display = 'none';
          el.style.pointerEvents = 'none';
        }
      } catch (err) {
        console.error('Error closing modal:', err);
      }
    }
'''

last_script_idx = html.rfind('</script>')
html = html[:last_script_idx] + '\n' + auto_close_patch + '\n' + html[last_script_idx:]

open(target_html_path, 'w', encoding='utf-8').write(html)
print('Saved sam3_update.html with auto-closing troop-promotion-modal')

# Check syntax
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp = f'temp_verify_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        print(f'SYNTAX ERROR in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:500])
        sys.exit(1)
print('All scripts valid JS!')

# Copy to all 5 target files immediately!
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
    print('Synced:', tgt)
