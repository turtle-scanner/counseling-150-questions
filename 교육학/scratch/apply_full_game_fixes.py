# -*- coding: utf-8 -*-
"""
삼국지 웹게임: 종합 무결성 전수 수리 패치
1. updateTroopLevelUI() HTML ID 완벽 매핑 (troop-tier-name, troop-tier-badge, troop-tier-mod 등)
2. nextTurn(), refundActionPoint() 함수 완전 정의
3. reorganize-modal (8. 재편성) 모달 HTML 마크업 추가
4. 미정의 요소들 안전 보강
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. nextTurn() 및 refundActionPoint() 함수 추가
# ---------------------------------------------------------------------------
helper_funcs = """
    function nextTurn() {
      executeRest();
    }

    function refundActionPoint() {
      if (gameState.actionPoints !== undefined && gameState.actionPoints < 5) {
        gameState.actionPoints++;
        updateActionPointUI();
      }
    }
"""

if "function refundActionPoint" not in content:
    content = content.replace("function executeRest() {", helper_funcs + "\n    function executeRest() {")
    print("SUCCESS: Added nextTurn and refundActionPoint functions.")

# ---------------------------------------------------------------------------
# 2. updateTroopLevelUI()를 실제 HTML ID와 100% 일치하도록 전면 개편
# ---------------------------------------------------------------------------
old_troop_ui_pattern = r"function updateTroopLevelUI\(\)\s*\{[\s\S]*?if \(multEl\) multEl\.innerText = `공방 \$\{mult\}배`;\s*\}"

new_troop_ui_code = """function updateTroopLevelUI() {
      const lvl = gameState.troopLevel || 1;
      const exp = gameState.troopExp || 0;
      const typeName = gameState.troopTypeName || '보병 (기본)';
      const mult = (1.0 + (lvl - 1) * 0.15).toFixed(2);

      // 우측 패널의 실제 엘리먼트 ID들 매핑
      const tName = document.getElementById('troop-tier-name');
      const tBadge = document.getElementById('troop-tier-badge');
      const tMod = document.getElementById('troop-tier-mod');
      const tBar = document.getElementById('troop-exp-bar');
      const tText = document.getElementById('troop-exp-text');
      const tIcon = document.getElementById('troop-tier-icon');

      const icons = {
        '보병': '🛡️', '숙련보병': '🛡️', '기마병': '🐎', '강궁병': '🏹',
        '연노병': '🎯', '전차병': '🛡️', '돌격기병': '⚡', '서량철기병': '🏔️', '천하무적군': '👑'
      };
      const curIcon = icons[typeName.split(' ')[0]] || '🛡️';

      if (tName) tName.innerText = typeName;
      if (tBadge) tBadge.innerText = `Lv. ${lvl}`;
      if (tMod) tMod.innerText = `공방 ${mult}배`;
      if (tBar) tBar.style.width = `${Math.min(100, (exp / (lvl * 100)) * 100)}%`;
      if (tText) tText.innerText = `경험치: ${exp} / ${lvl * 100} EXP`;
      if (tIcon) tIcon.innerText = curIcon;

      // 하위 호환 매핑
      const pType = document.getElementById('panel-troop-type');
      const pLvl = document.getElementById('panel-troop-lvl');
      const pMult = document.getElementById('panel-troop-mult');
      if (pType) pType.innerText = typeName;
      if (pLvl) pLvl.innerText = `Lv. ${lvl}`;
      if (pMult) pMult.innerText = `공방 ${mult}배`;
    }"""

if re.search(old_troop_ui_pattern, content):
    content = re.sub(old_troop_ui_pattern, new_troop_ui_code, content, count=1)
    print("SUCCESS: Updated updateTroopLevelUI with exact HTML IDs.")
else:
    print("WARNING: Could not find old updateTroopLevelUI pattern.")

# ---------------------------------------------------------------------------
# 3. reorganize-modal (8. 재편성) 모달 HTML 마크업 주입
# ---------------------------------------------------------------------------
reorganize_modal_html = """
  <!-- ==================== ⚖️ 병력 재편성 모달 ==================== -->
  <div id="reorganize-modal" class="fixed inset-0 modal-backdrop z-[99999] hidden flex items-center justify-center p-3 bg-black/90">
    <div class="koei-box w-full max-w-lg p-5 rounded-lg shadow-2xl border-4 border-blue-500 flex flex-col justify-between">
      <div class="flex items-center justify-between border-b-2 border-blue-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-2xl">⚖️</span>
          <h2 class="text-base font-black text-cyan-300 text-pixel">군사 재편성 (병종 승급 & 병력 배분)</h2>
        </div>
        <button onclick="closeModal('reorganize-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <!-- 병종 상태 박스 -->
      <div class="bg-slate-900/90 p-3 rounded-lg border border-blue-500/50 mb-3 text-xs space-y-2">
        <div class="flex justify-between items-center">
          <span class="text-slate-300">현재 주력 병종:</span>
          <div class="flex items-center gap-1.5 font-bold">
            <span id="reorg-tier-icon">🛡️</span>
            <span id="reorg-tier-name" class="text-yellow-300">보병 (기본)</span>
            <span id="reorg-tier-lvl" class="px-1.5 py-0.5 rounded bg-blue-950 text-cyan-200 border border-cyan-500 text-[10px]">Lv. 1</span>
          </div>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-slate-300">전투 공방 보정:</span>
          <span id="reorg-tier-mult" class="text-emerald-400 font-black">공방 1.0배</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-slate-300">다음 목표 승급:</span>
          <span id="reorg-next-promo" class="text-amber-300 font-bold">Lv.3 기마병</span>
        </div>
        <div class="w-full bg-slate-950 h-2 rounded-full overflow-hidden border border-slate-700">
          <div id="reorg-exp-bar" class="h-full bg-gradient-to-r from-blue-500 to-amber-400" style="width: 10%;"></div>
        </div>
        <div class="flex justify-between text-[10px] text-slate-400">
          <span id="reorg-exp-text">경험치: 10 / 100 EXP</span>
          <span id="reorg-total-soldiers">영지 총 병력: -</span>
        </div>
      </div>

      <!-- 재편성 버튼들 -->
      <div class="grid grid-cols-2 gap-2 text-xs">
        <button onclick="reorganizeSoldiers('even')" class="p-2.5 rounded bg-blue-900 hover:bg-blue-800 border border-cyan-400 text-white font-bold shadow flex flex-col items-center gap-1">
          <span>⚖️ 균등 분배</span>
          <span class="text-[10px] text-cyan-200">전 장수에게 병력 균등 배분</span>
        </button>
        <button onclick="reorganizeSoldiers('front')" class="p-2.5 rounded bg-amber-900 hover:bg-amber-800 border border-yellow-400 text-yellow-200 font-bold shadow flex flex-col items-center gap-1">
          <span>⚔️ 맹장 집중 분배</span>
          <span class="text-[10px] text-yellow-100">무력 최상위 장수에게 병력 집중</span>
        </button>
      </div>

      <div class="mt-4 pt-2 border-t border-slate-700 flex justify-end">
        <button onclick="closeModal('reorganize-modal')" class="px-4 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold border border-slate-600">
          닫기
        </button>
      </div>
    </div>
  </div>
"""

if "id=\"reorganize-modal\"" not in content:
    content = content.replace("<!-- ==================== ⚔️ 출전 장수 편성 & 피로도 선택 모달 ==================== -->", reorganize_modal_html + "\n  <!-- ==================== ⚔️ 출전 장수 편성 & 피로도 선택 모달 ==================== -->")
    print("SUCCESS: Added reorganize-modal HTML markup.")

# ---------------------------------------------------------------------------
# 4. 파일 저장 및 동기화
# ---------------------------------------------------------------------------
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Saved clean HTML to Desktop.")

TARGETS = [
    r"C:\Users\LENOVO\Desktop\sam3_update.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
]

for t in TARGETS:
    try:
        shutil.copy2(TARGET_FILE, t)
        print(f"Synced successfully -> {t}")
    except Exception as e:
        print(f"Error copying to {t}: {e}")
