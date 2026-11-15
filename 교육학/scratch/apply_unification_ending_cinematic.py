# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. renderMapPins 내 checkUnification() 자동 호출 주입 (13주 점령 즉시 100% 발동)
# ==============================================================================
print("1. Wiring checkUnification() to renderMapPins()...")

if 'checkUnification();' not in text[text.find('function renderMapPins'):text.find('function renderMapPins')+1500]:
    text = text.replace(
        "document.getElementById('unify-progress').innerText = `${myCount} / 13주 (${percent}%)`;",
        "document.getElementById('unify-progress').innerText = `${myCount} / 13주 (${percent}%)`;\n      if (myCount === 13) { checkUnification(); }"
    )
    print("  -> checkUnification() auto-trigger wired into renderMapPins()!")

# ==============================================================================
# 2. checkUnification() 함수 고도화 (웅장한 팡파레 사운드 & 즉위식 연출)
# ==============================================================================
print("2. Enhancing checkUnification() & openUnificationEnding()...")

unification_engine = """    function checkUnification() {
      const myCount = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      if (myCount === 13) {
        openUnificationEnding();
      }
    }

    function openUnificationEnding() {
      closeAllPopups();
      try {
        playSfx('fanfare');
        if (typeof playSound === 'function') playSound('fanfare');
      } catch (e) {}

      logMessage(`👑🏆✨ [천하통일 대위업 달성!] ${gameState.rulerName} 주군께서 천하 13주를 100% 완전 통일하여 한나라 황제에 즉위하셨습니다!`, 'text-yellow-300 font-black text-base animate-pulse');

      const rNameEl = document.getElementById('ending-ruler-name');
      if (rNameEl) rNameEl.innerText = `한나라 제2의 건국 황제: ${gameState.rulerName}`;

      openModal('unification-ending-modal');
    }
"""

pattern_check_unify = r"function checkUnification\(\)\s*\{[\s\S]*?openModal\('unification-ending-modal'\);\s*\}\s*\}"
match_check_unify = re.search(pattern_check_unify, text)
if match_check_unify:
    text = text[:match_check_unify.start()] + unification_engine.strip() + text[match_check_unify.end():]
    print("  -> checkUnification() & openUnificationEnding() successfully upgraded!")

# ==============================================================================
# 3. 천하통일 진행률 배너 클릭 시 즉위식 엔딩 바로보기 버튼 연결
# ==============================================================================
print("3. Making Unification progress banner clickable to view ending...")

progress_banner_clickable = """<div onclick="checkUnification()" class="text-amber-300 text-xs hidden sm:inline-block cursor-pointer hover:text-yellow-200 hover:underline bg-slate-900/80 px-2 py-0.5 rounded border border-yellow-500/50 shadow">
            천하통일: <strong id="unify-progress" class="text-yellow-300">1 / 13주 (8%)</strong> <span class="text-[10px] text-cyan-300">👑 [엔딩보기]</span>
          </div>"""

pattern_banner = r'<div class="text-amber-300 text-xs hidden sm:inline-block">\s*천하통일:\s*<strong id="unify-progress"[^>]*?>[^<]*?</strong>\s*</div>'
text = re.sub(pattern_banner, progress_banner_clickable, text)

# ==============================================================================
# 4. 엔딩 모달 하단 버튼: '새로운 난세 환생(새 게임)' & '통치 계속하기' 완비
# ==============================================================================
print("4. Upgrading Unification Ending Modal buttons...")

ending_modal_buttons = """        <div class="flex items-center justify-between gap-3 w-full mt-3 pt-3 border-t border-yellow-500/40">
          <button onclick="location.reload()" class="px-5 py-2.5 bg-gradient-to-r from-red-800 to-amber-700 hover:from-red-700 hover:to-amber-600 text-yellow-200 font-black text-xs rounded-lg border-2 border-yellow-400 shadow-xl flex items-center gap-1.5 transition">
            <span>👑 새로운 난세로 환생 (새 게임 시작)</span>
          </button>
          <button onclick="closeModal('unification-ending-modal')" class="px-5 py-2.5 bg-gradient-to-r from-blue-900 to-indigo-800 hover:from-blue-800 hover:to-indigo-700 text-cyan-200 font-black text-xs rounded-lg border border-cyan-400 shadow-lg flex items-center gap-1.5 transition">
            <span>🏰 천하 태평성대 자유 통치 계속하기</span>
          </button>
        </div>"""

pattern_ending_buttons = r'<button onclick="closeModal\(\'unification-ending-modal\'\)" class="px-5 py-2\.5 bg-blue-900[\s\S]*?<\/button>'
text = re.sub(pattern_ending_buttons, ending_modal_buttons, text)

# ==============================================================================
# 파일 저장 및 전역 동기화
# ==============================================================================
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)
print(f"Main Desktop file saved: {len(text):,} bytes")

update_desktop_path = r'C:/Users/LENOVO/Desktop/sam3_update.html'
with open(update_desktop_path, 'w', encoding='utf-8') as f:
    f.write(text)

git_edu_path = r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/교육학/samgukji.html'
with open(git_edu_path, 'w', encoding='utf-8') as f:
    f.write(text)

git_root_path = r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/samgukji.html'
with open(git_root_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("UNIFICATION ENDING CINEMATIC UPGRADE COMPLETE!")
