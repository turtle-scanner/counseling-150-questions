# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1) Update subtitle dynamically in gainTroopExp and auto-hide troop-promotion-modal after 1.2s
old_promo_block = """          const tIcon = document.getElementById('promo-icon');
          const tTitle = document.getElementById('promo-title');
          const tDesc = document.getElementById('promo-desc');
          if (tIcon) tIcon.innerText = info.icon;
          if (tTitle) tTitle.innerText = `🎉 [병종 승급] ${info.typeName} 승급 달성!`;
          if (tDesc) tDesc.innerText = `병사들이 Lv.${gameState.troopLevel}에 도달하여 ${info.typeName}(으)로 전직했습니다! 공방 ${info.mult}배 대폭 강화!`;
          openModal('troop-promotion-modal');"""

new_promo_block = """          const tIcon = document.getElementById('promo-icon');
          const tTitle = document.getElementById('promo-title');
          const tSub = document.getElementById('promo-subtitle');
          const tDesc = document.getElementById('promo-desc');
          if (tIcon) tIcon.innerText = info.icon;
          if (tTitle) tTitle.innerText = `🎉 [병종 승급] ${info.typeName} 승급 달성!`;
          if (tSub) tSub.innerText = `병사들의 숙련도가 ${gameState.troopLevel}레벨에 도달하여 전원 '${info.typeName}'(으)로 전직하였습니다!`;
          if (tDesc) tDesc.innerText = `병사들이 Lv.${gameState.troopLevel}에 도달하여 ${info.typeName}(으)로 전직했습니다! 공방 ${info.mult}배 대폭 강화!`;
          showTransientPromotionBanner();"""

if old_promo_block in html:
    html = html.replace(old_promo_block, new_promo_block)
    print('Replaced gainTroopExp promo block successfully!')
else:
    print('WARNING: old_promo_block not exact match, using regex...')
    html = re.sub(r"openModal\(['\"]troop-promotion-modal['\"]\);", "showTransientPromotionBanner();", html)

# 2) Define showTransientPromotionBanner() so it pops up for 1.3 seconds and ALWAYS disappears automatically (and also closes immediately on any click or key press)
banner_fn = '''
    let _promoHideTimer = null;
    function showTransientPromotionBanner() {
      const el = document.getElementById('troop-promotion-modal');
      if (!el) return;
      el.classList.remove('hidden');
      el.style.display = 'flex';
      el.style.pointerEvents = 'auto';
      el.onclick = () => hidePromotionBannerNow();
      const btn = el.querySelector('button');
      if (btn) btn.onclick = (e) => { e.stopPropagation(); hidePromotionBannerNow(); };
      if (_promoHideTimer) clearTimeout(_promoHideTimer);
      _promoHideTimer = setTimeout(() => {
        hidePromotionBannerNow();
      }, 1300);
    }
    function hidePromotionBannerNow() {
      if (_promoHideTimer) {
        clearTimeout(_promoHideTimer);
        _promoHideTimer = null;
      }
      const el = document.getElementById('troop-promotion-modal');
      if (el) {
        el.classList.add('hidden');
        el.style.setProperty('display', 'none', 'important');
        el.style.setProperty('pointer-events', 'none', 'important');
      }
    }
'''

last_script_idx = html.rfind('</script>')
html = html[:last_script_idx] + '\n' + banner_fn + '\n' + html[last_script_idx:]

open(target_html_path, 'w', encoding='utf-8').write(html)

# Sync to all 5 files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
print('All 6 files updated and synced!')
