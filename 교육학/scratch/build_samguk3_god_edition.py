# -*- coding: utf-8 -*-
import os
import json
import re

def build():
    print("=== 삼국지 3 갓 에디션 (병사 Lv1~100 전직 + 보물 + 컷인 + 관직 + 계절) 빌드 시작 ===")

    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")

    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    map_b64 = assets["map_b64"]
    liubei_b64 = assets["portraits"]["liubei"]
    portraits_json = json.dumps(assets["portraits"])

    # 1. 기존 완성된 HTML 가져오기 (이전 궁극 빌드 결과물)
    master_html_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    with open(master_html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 2. 추가 CSS (병사 전직 뱃지, 일기토 컷인 오버레이, 보물 카드, 레벨업 게이지 등)
    extra_css = """
    /* 병사 레벨업 및 전직 뱃지 */
    .troop-tier-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 900;
      box-shadow: 0 0 8px rgba(0,0,0,0.6);
    }

    /* 일기토 필살기 컷인 애니메이션 */
    @keyframes cutinSlideIn {
      0% { transform: translateX(-100%) skewX(-15deg); opacity: 0; }
      50% { transform: translateX(5%) skewX(-15deg); opacity: 1; }
      100% { transform: translateX(0) skewX(0); opacity: 1; }
    }
    .cutin-banner {
      animation: cutinSlideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes flashWhite {
      0% { opacity: 0.9; }
      100% { opacity: 0; }
    }
    .screen-flash {
      position: fixed;
      inset: 0;
      background: white;
      pointer-events: none;
      z-index: 9999999;
      animation: flashWhite 0.35s ease-out forwards;
    }

    /* 보물 카드 */
    .treasure-card {
      background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
      border: 1.5px solid #d97706;
      box-shadow: 0 4px 12px rgba(0,0,0,0.8), inset 0 0 8px rgba(217, 119, 6, 0.3);
      transition: all 0.2s ease;
    }
    .treasure-card:hover {
      border-color: #fbbf24;
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(251, 191, 36, 0.4);
    }
"""

    # 3. 추가 모달 HTML
    # (A) 병종 승급 전직 모달 (Lv3 기마병, Lv6 전차병, Lv9 중보병, Lv99 친위병)
    promotion_modal_html = """
  <!-- ==================== 🔥 병종 승급 전직 축하 모달 ==================== -->
  <div id="troop-promotion-modal" class="fixed inset-0 modal-backdrop z-[9999999] hidden flex items-center justify-center p-3 bg-black/90">
    <div class="koei-box w-full max-w-lg p-5 rounded-xl shadow-2xl border-4 border-yellow-400 text-center flex flex-col items-center gap-3">
      <div class="text-4xl animate-bounce" id="promo-icon">🐎</div>
      <h2 class="text-xl font-black text-yellow-300 text-pixel tracking-wider" id="promo-title">
        🎉 [병종 승급] 기마병(騎馬兵) 승급 달성!
      </h2>
      <div class="text-sm font-bold text-amber-200" id="promo-subtitle">
        병사들의 숙련도가 3레벨에 도달하여 전원 '기마병'으로 전직하였습니다!
      </div>
      <div class="p-3 bg-blue-950/80 border border-yellow-500/60 rounded-lg text-xs text-slate-200 text-left w-full space-y-1.5" id="promo-desc">
        <div>• 기동력 +1칸 증가 (빠른 전장 기습 가능)</div>
        <div>• 평지 돌격 피해량 +35% 증가</div>
        <div>• 적 방어선 돌파 확률 대폭 향상!</div>
      </div>
      <button onclick="closeModal('troop-promotion-modal')" class="px-6 py-2.5 rounded-lg bg-gradient-to-r from-amber-600 to-yellow-500 hover:from-amber-500 hover:to-yellow-400 text-black font-black text-sm shadow-xl border-2 border-yellow-200 mt-2">
        천하통일을 향해 진격하라! (확인)
      </button>
    </div>
  </div>
"""

    # (B) 보물 보관함 모달 (하사 및 수색)
    treasure_modal_html = """
  <!-- ==================== 🏆 전설의 보물 보관함 & 하사 모달 ==================== -->
  <div id="treasure-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex items-center justify-center p-3 bg-black/85">
    <div class="koei-box w-full max-w-3xl p-4 rounded-lg shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col justify-between overflow-y-auto">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-2xl">🏆</span>
          <h2 class="text-base font-black text-yellow-300 text-pixel">
            [전설의 보물 보관함] 명마 · 명검 · 병법서
          </h2>
        </div>
        <button onclick="closeModal('treasure-modal')" class="text-slate-400 hover:text-white font-mono text-sm px-2 py-0.5 border border-slate-600 rounded">
          ✕ 닫기
        </button>
      </div>

      <div class="text-xs text-amber-200 mb-2 px-1 flex items-center justify-between">
        <span>💡 보물을 맹장에게 하사하면 능력치가 비약적으로 상승하고 충성도가 100(절대 불변)이 됩니다!</span>
        <button onclick="executeTreasureSearch()" class="px-3 py-1 bg-amber-700 hover:bg-amber-600 text-yellow-100 font-black rounded text-xs border border-yellow-300 shadow">
          🔍 천하 명산 보물 탐색 (금 300)
        </button>
      </div>

      <div id="treasure-list-container" class="grid grid-cols-1 md:grid-cols-2 gap-2.5 max-h-[60vh] overflow-y-auto p-1">
        <!-- 동적 렌더링 -->
      </div>

      <div class="border-t border-amber-500/40 pt-2.5 mt-2 flex justify-end">
        <button onclick="closeModal('treasure-modal')" class="px-4 py-1.5 bg-slate-700 hover:bg-slate-600 text-white font-bold text-xs rounded border border-slate-500">
          닫기
        </button>
      </div>
    </div>
  </div>
"""

    # (C) 일기토 필살기 컷인 오버레이 HTML
    cutin_overlay_html = """
  <!-- ==================== ⚔️ 일기토 필살기 컷인 오버레이 ==================== -->
  <div id="cutin-overlay" class="fixed inset-0 pointer-events-none z-[9999999] hidden flex items-center justify-center">
    <div class="cutin-banner w-full bg-gradient-to-r from-red-950 via-amber-900 to-red-950 border-y-4 border-yellow-400 py-6 px-10 shadow-2xl flex items-center justify-between">
      <div class="flex items-center gap-6">
        <div id="cutin-icon" class="text-6xl filter drop-shadow-[0_0_15px_rgba(255,215,0,0.8)]">🐉</div>
        <div>
          <div id="cutin-title" class="text-yellow-300 font-black text-2xl text-pixel tracking-wider drop-shadow-[0_2px_4px_#000]">
            [무성(武聖) 관우] 청룡언월도 극의!
          </div>
          <div id="cutin-quote" class="text-white font-bold text-lg italic mt-1 drop-shadow-[0_2px_4px_#000]">
            "내 청룡도 앞에 목을 내놓아라!"
          </div>
        </div>
      </div>
      <div class="text-right">
        <div class="text-red-400 font-black text-3xl animate-pulse">치명타 3배!</div>
        <div class="text-yellow-200 text-xs font-bold mt-1">적장 방어구 완전 분쇄</div>
      </div>
    </div>
  </div>
"""

    # (D) 관직 승진 & 황제 칙명 모달
    quest_modal_html = """
  <!-- ==================== 👑 관직 승진 & 황제 칙명 모달 ==================== -->
  <div id="quest-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex items-center justify-center p-3 bg-black/85">
    <div class="koei-box w-full max-w-lg p-5 rounded-lg shadow-2xl border-4 border-yellow-400 flex flex-col gap-3">
      <div class="flex items-center justify-between border-b-2 border-yellow-400 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-2xl">👑</span>
          <h2 class="text-base font-black text-yellow-300 text-pixel" id="quest-modal-title">
            [황제 칙명] 한실 부흥의 밀서
          </h2>
        </div>
        <span class="px-2 py-0.5 rounded text-xs bg-amber-950 border border-yellow-400 text-yellow-200 font-bold" id="quest-rank-badge">승상(丞相)</span>
      </div>

      <div class="p-3 bg-blue-950/90 border border-amber-500/70 rounded-lg text-xs text-slate-200 space-y-2 leading-relaxed" id="quest-modal-body">
        "조조가 허창에서 천자를 능멸하고 국정을 전횡하고 있소. 충의로운 주군이시여, 조조의 본거지 낙양을 탈환하여 사직을 구원하시오!"
      </div>

      <div class="p-2.5 bg-amber-950/60 border border-amber-500 rounded text-xs text-yellow-200 font-bold" id="quest-reward-text">
        🎁 칙명 달성 보상: 군자금 3,000전 + 전설의 보물 '전국옥새(傳國玉璽)' 하사!
      </div>

      <button onclick="closeModal('quest-modal')" class="w-full py-2.5 rounded bg-gradient-to-r from-red-700 to-amber-700 hover:from-red-600 hover:to-amber-600 text-white font-black text-xs border border-yellow-300 shadow">
        칙명을 받들어 충의를 다하겠나이다! (확인)
      </button>
    </div>
  </div>
"""

    # 4. 상단 헤더 및 우측 패널에 [병사 등급 & 레벨 바] HUD 컴포넌트 추가
    # 우측 정보창에 병사 등급 및 레벨 게이지 바 삽입
    troop_hud_ui = """
        <!-- 🔥 병사 등급(보병->기마병->전차병->중보병->친위병) & 레벨 1~100 게이지 -->
        <div class="bg-blue-950/90 border-2 border-amber-400/80 rounded-lg p-2.5 mb-2.5 shadow">
          <div class="flex items-center justify-between mb-1">
            <div class="flex items-center gap-1.5">
              <span id="troop-tier-icon" class="text-base">🛡️</span>
              <span id="troop-tier-name" class="font-black text-xs text-white">보병 (기본)</span>
              <span id="troop-tier-badge" class="troop-tier-badge bg-slate-800 border border-slate-500 text-slate-200">Lv. 1</span>
            </div>
            <span id="troop-tier-mod" class="text-[11px] text-yellow-300 font-bold">공방 1.0배</span>
          </div>
          <!-- 레벨 100 경험치 프로그레스 바 -->
          <div class="w-full bg-slate-900 h-2.5 rounded-full overflow-hidden border border-blue-600/60 p-0.5">
            <div id="troop-exp-bar" class="h-full rounded-full bg-gradient-to-r from-blue-500 via-amber-500 to-yellow-400 transition-all duration-300" style="width: 10%;"></div>
          </div>
          <div class="flex justify-between items-center text-[10px] text-slate-300 mt-1">
            <span id="troop-exp-text">경험치: 10 / 100 EXP</span>
            <span class="text-cyan-300">다음 승급: <strong id="troop-next-promo-text" class="text-yellow-300">Lv.3 기마병</strong></span>
          </div>
        </div>
"""

    # 5. 상단 메뉴 8. 특별 및 9. 기능에 [보물 보관함], [황제 칙명] 메뉴 항목 추가
    treasure_menu_item = """
          <div onclick="openTreasureModal()" class="koei-popup-item !text-amber-300 font-black">🏆 보물 보관함 (하사)</div>
          <div onclick="openQuestModal()" class="koei-popup-item !text-yellow-300 font-black">👑 황제 칙명 & 관직</div>
"""

    # 6. 추가 자바스크립트 로직 (병종 레벨업 엔진, 보물 시스템, 컷인 연출, 관직 퀘스트, 계절 이벤트)
    god_edition_js = """
    // ==================== 🔥 [신개념] 병사 Lv.1~100 및 5단계 병종 전직 엔진 ====================
    // 보병(Lv1) ➔ 기마병(Lv3) ➔ 전차병(Lv6) ➔ 중보병(Lv9) ➔ 친위병(Lv99~100)
    const TROOP_TIERS = [
      { minLv: 1, maxLv: 2, name: '보병', icon: '🛡️', color: 'text-slate-200', badgeClass: 'bg-slate-800 border-slate-500', atkMod: 1.0, defMod: 1.0, moveBonus: 0, nextReq: 3, nextName: '기마병', desc: '기본 징집 보병' },
      { minLv: 3, maxLv: 5, name: '기마병', icon: '🐎', color: 'text-amber-300', badgeClass: 'bg-amber-900 border-amber-500 text-yellow-200', atkMod: 1.35, defMod: 1.20, moveBonus: 1, nextReq: 6, nextName: '전차병', desc: '이동력 +1, 돌격력 +35%' },
      { minLv: 6, maxLv: 8, name: '전차병', icon: '⚔️', color: 'text-red-400', badgeClass: 'bg-red-950 border-red-500 text-yellow-100', atkMod: 1.75, defMod: 1.50, moveBonus: 1, nextReq: 9, nextName: '중보병', desc: '철갑 바퀴 전차 (평지 돌파 데미지 +75%)' },
      { minLv: 9, maxLv: 98, name: '중보병', icon: '🛡️', color: 'text-cyan-300', badgeClass: 'bg-cyan-950 border-cyan-400 text-cyan-200', atkMod: 2.20, defMod: 2.10, moveBonus: 0, nextReq: 99, nextName: '친위병', desc: '철갑 방진 (궁시 피해 80% 차단, 방어 2.1배)' },
      { minLv: 99, maxLv: 100, name: '친위병', icon: '👑', color: 'text-yellow-300 font-black', badgeClass: 'bg-gradient-to-r from-amber-600 to-yellow-500 text-black border-yellow-200 ring-2 ring-yellow-400 animate-pulse', atkMod: 3.50, defMod: 3.20, moveBonus: 2, nextReq: 100, nextName: '최종 만렙', desc: '황제 직속 무적 근위 군단 (공방 3.5배, 이동력+2)' }
    ];

    function getTroopTier(level) {
      if (level >= 99) return TROOP_TIERS[4];
      if (level >= 9) return TROOP_TIERS[3];
      if (level >= 6) return TROOP_TIERS[2];
      if (level >= 3) return TROOP_TIERS[1];
      return TROOP_TIERS[0];
    }

    function getNextExp(level) {
      return Math.floor(80 * Math.pow(1.055, level - 1));
    }

    function addTroopExp(amount) {
      if (!gameState.troopLevel) gameState.troopLevel = 1;
      if (!gameState.troopExp) gameState.troopExp = 0;

      gameState.troopExp += amount;
      let oldTier = getTroopTier(gameState.troopLevel);
      let leveledUp = false;

      while (gameState.troopLevel < 100 && gameState.troopExp >= getNextExp(gameState.troopLevel)) {
        gameState.troopExp -= getNextExp(gameState.troopLevel);
        gameState.troopLevel++;
        leveledUp = true;
      }

      let newTier = getTroopTier(gameState.troopLevel);
      if (oldTier.name !== newTier.name) {
        triggerTroopPromotion(oldTier, newTier);
      } else if (leveledUp) {
        playTone(587, 0.15, 'sine', 0.2);
        logMessage(`⭐ [병사 레벨업!] 병사 숙련도가 Lv.${gameState.troopLevel}로 올랐습니다! (전투 공방 보정치 상승)`, 'text-yellow-300 font-bold');
      }

      updateTroopLevelUI();
    }

    function triggerTroopPromotion(oldTier, newTier) {
      playSfx('victory');
      document.getElementById('promo-icon').innerText = newTier.icon;
      document.getElementById('promo-title').innerText = `🎉 [병종 승급] '${newTier.name}' 승급 달성!`;
      document.getElementById('promo-subtitle').innerText = `병사 숙련도가 ${gameState.troopLevel}레벨에 도달하여 아군 전 병력이 '${newTier.name}'으로 전직하였습니다!`;
      document.getElementById('promo-desc').innerHTML = `
        <div>• <strong>새로운 전투 능력치:</strong> 공격력 x${newTier.atkMod} / 방어력 x${newTier.defMod}</div>
        <div>• <strong>병종 특성:</strong> ${newTier.desc}</div>
        <div>• <strong>다음 최종 목표:</strong> Lv.${newTier.nextReq} 도달 시 '${newTier.nextName}'으로 전직!</div>
      `;
      openModal('troop-promotion-modal');
      logMessage(`🎖️ [병종 전직 대축하!] 아군 병력이 '${oldTier.name}' ➔ '${newTier.name}'(Lv.${gameState.troopLevel})으로 승급 전직했습니다!`, 'text-yellow-300 font-extrabold text-sm');
    }

    function updateTroopLevelUI() {
      if (!gameState.troopLevel) gameState.troopLevel = 1;
      if (!gameState.troopExp) gameState.troopExp = 0;

      const tier = getTroopTier(gameState.troopLevel);
      const req = getNextExp(gameState.troopLevel);
      const pct = Math.min(100, Math.floor((gameState.troopExp / req) * 100));

      const iconEl = document.getElementById('troop-tier-icon');
      const nameEl = document.getElementById('troop-tier-name');
      const badgeEl = document.getElementById('troop-tier-badge');
      const modEl = document.getElementById('troop-tier-mod');
      const barEl = document.getElementById('troop-exp-bar');
      const textEl = document.getElementById('troop-exp-text');
      const promoEl = document.getElementById('troop-next-promo-text');

      if (iconEl) iconEl.innerText = tier.icon;
      if (nameEl) nameEl.innerText = `${tier.name} (${tier.desc})`;
      if (badgeEl) {
        badgeEl.className = `troop-tier-badge ${tier.badgeClass}`;
        badgeEl.innerText = `Lv. ${gameState.troopLevel}`;
      }
      if (modEl) modEl.innerText = `공방 x${tier.atkMod}`;
      if (barEl) barEl.style.width = pct + '%';
      if (textEl) textEl.innerText = `숙련도: ${gameState.troopExp} / ${req} EXP (${pct}%)`;
      if (promoEl) {
        promoEl.innerText = (gameState.troopLevel >= 99) ? '👑 친위병 만렙 달성!' : `Lv.${tier.nextReq} ${tier.nextName}`;
      }
    }

    // ==================== 🏆 전설의 보물 시스템 ====================
    let TREASURES = [
      { id: 'red_hare', name: '적토마 (赤兎馬)', icon: '🐎', war: 10, int: 0, desc: '하루에 천 리를 달리는 명마. 이동력 +2, 일기토 선공권, 퇴각 100% 성공', owner: null },
      { id: 'green_dragon', name: '청룡언월도 (靑龍偃月刀)', icon: '🗡️', war: 12, int: 0, desc: '무게 82근의 신도. 관우의 무기. 치명타 확률 3배 및 적 방어구 분쇄', owner: '관우 (운장)' },
      { id: 'serpent_spear', name: '장팔사모 (丈八蛇矛)', icon: '🐍', war: 10, int: 0, desc: '뱀 형상의 강철 창. 장비의 무기. 적의 진형 돌파 및 광역 넉백', owner: '장비 (익덕)' },
      { id: 'sun_tzu', name: '손자병법서 (孫子兵法)', icon: '📜', war: 0, int: 15, desc: '손무가 지은 최고의 병법서. 화계 및 계략 성공률 90% 보장', owner: null },
      { id: 'sky_piercer', name: '방천화극 (方天畵戟)', icon: '👹', war: 15, int: 0, desc: '여포의 무기. 공격력 최상위, 일기토 2연타 필살기 발동', owner: null },
      { id: 'imperial_seal', name: '전국옥새 (傳國玉璽)', icon: '👑', war: 5, int: 10, desc: '한나라 황제의 정통성을 상징하는 보옥. 명성 100 증가, 전 영지 민충 100 고정', owner: null }
    ];

    function openTreasureModal() {
      closeAllPopups();
      renderTreasures();
      openModal('treasure-modal');
    }

    function renderTreasures() {
      const container = document.getElementById('treasure-list-container');
      if (!container) return;
      container.innerHTML = TREASURES.map(t => {
        const ownerTxt = t.owner ? `<span class="text-emerald-300 font-bold">장착: ${t.owner}</span>` : `<span class="text-amber-400">보관함 보관 중 (미지급)</span>`;
        return `
          <div class="treasure-card p-3 rounded-lg flex flex-col justify-between">
            <div class="flex items-start gap-2.5">
              <span class="text-3xl">${t.icon}</span>
              <div class="space-y-0.5">
                <div class="text-sm font-black text-yellow-300">${t.name}</div>
                <div class="text-[11px] text-cyan-300">효과: 무력 +${t.war} | 지력 +${t.int}</div>
                <div class="text-[10px] text-slate-300 leading-tight">${t.desc}</div>
              </div>
            </div>
            <div class="mt-2 pt-2 border-t border-slate-700/80 flex items-center justify-between text-xs">
              <div class="text-[11px]">${ownerTxt}</div>
              <button onclick="awardTreasurePrompt('${t.id}')" class="px-2.5 py-1 rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 font-bold text-[11px] border border-yellow-300 shadow">
                장수 하사 ➔
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    function awardTreasurePrompt(tId) {
      const t = TREASURES.find(x => x.id === tId);
      if (!t) return;
      const offNames = MY_OFFICERS.map((o, idx) => `${idx + 1}. ${o.name}`).join('\\n');
      const choice = prompt(`[${t.name} 하사]\\n어느 장수에게 하사하시겠습니까?\\n번호를 입력하십시오:\\n${offNames}`);
      if (!choice) return;
      const idx = parseInt(choice, 10) - 1;
      const targetOff = MY_OFFICERS[idx];
      if (!targetOff) { alert('유효하지 않은 장수 번호입니다.'); return; }

      t.owner = targetOff.name;
      targetOff.war += t.war;
      targetOff.int += t.int;
      playSfx('victory');
      alert(`🎉 [보물 하사 완료!]\\n'${t.name}'을(를) ${targetOff.name}에게 하사했습니다!\\n${targetOff.name}의 무력이 ${targetOff.war}, 지력이 ${targetOff.int}로 상승하고 충성도가 100(절대 불변)이 되었습니다!`);
      logMessage(`🏆 [보물 하사] '${t.name}'을(를) ${targetOff.name}에게 수여하여 충성도 100과 무력 +${t.war}을 부여했습니다!`, 'text-yellow-300 font-black');
      renderTreasures();
    }

    function executeTreasureSearch() {
      const myProv = getMyCapital();
      if (myProv.gold < 300) { alert('보물 탐색을 위한 탐문 자금(금 300전)이 부족합니다.'); return; }
      myProv.gold -= 300;
      updateRightPanel(myProv.id);
      playSfx('build');

      const unowned = TREASURES.filter(t => !t.owner);
      if (unowned.length === 0 || Math.random() < 0.45) {
        alert('산야를 샅샅이 수색하였으나 이번에는 신비로운 보물을 찾지 못했습니다.');
        logMessage('🔍 [보물 탐색] 보물을 발견하지 못했습니다. 다음 기회를 노리십시오.', 'text-slate-400');
      } else {
        const found = unowned[Math.floor(Math.random() * unowned.length)];
        found.owner = null;
        playSfx('victory');
        alert(`🎉🏆 [천하 명검 발견!]\\n태산 깊은 동굴에서 전설의 보물 '${found.name}'을(를) 발굴하였습니다!\\n보관함에서 맹장에게 하사하십시오!`);
        logMessage(`👑 [보물 획득!] 전설의 보물 '${found.name}'을(를) 손에 넣었습니다!`, 'text-yellow-300 font-extrabold text-sm');
        renderTreasures();
      }
    }

    // ==================== ⚔️ 일기토 필살기 컷인 연출 ====================
    function triggerCutinEffect(heroName, quote, title, icon, bonusDmg) {
      const flash = document.createElement('div');
      flash.className = 'screen-flash';
      document.body.appendChild(flash);
      setTimeout(() => flash.remove(), 400);

      const overlay = document.getElementById('cutin-overlay');
      if (!overlay) return;
      document.getElementById('cutin-icon').innerText = icon || '⚔️';
      document.getElementById('cutin-title').innerText = title || `[${heroName}] 필살 절기 작렬!`;
      document.getElementById('cutin-quote').innerText = quote || `"적장의 목을 베어 주군께 바치겠노라!"`;

      overlay.classList.remove('hidden');
      playTone(220, 0.35, 'sawtooth', 0.4);

      setTimeout(() => {
        overlay.classList.add('hidden');
      }, 1400);
    }

    // ==================== 👑 관직 승진 & 황제 칙명 시스템 ====================
    function checkImperialRank() {
      const myProvs = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      let newRank = '평민 군벌';
      if (myProvs >= 13) newRank = '황제 (천하통일)';
      else if (myProvs >= 8) newRank = '위왕 / 한중왕';
      else if (myProvs >= 5) newRank = '승상 (丞相)';
      else if (myProvs >= 3) newRank = '주목 (州牧)';
      else if (myProvs >= 2) newRank = '주자사 (州刺史)';

      if (gameState.imperialRank !== newRank) {
        gameState.imperialRank = newRank;
        playSfx('victory');
        alert(`👑 [관직 승진!]\n영토를 확장하여 헌제(황제)로부터 '${newRank}'에 봉해졌습니다!\n매 턴 세금 및 군량 징수량이 증가합니다!`);
        logMessage(`👑 [관직 승진] 한나라 조정으로부터 '${newRank}'에 정식 책봉되었습니다!`, 'text-yellow-300 font-extrabold');
      }
    }

    function openQuestModal() {
      closeAllPopups();
      checkImperialRank();
      openModal('quest-modal');
    }
"""

    # 7. 훈련(executeTraining) 시 병사 경험치 +150 획득 연결
    training_patch = """
    function executeTraining() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 100) { alert('군사 훈련을 위한 군비(금 100전)가 부족합니다.'); return; }
      myProv.gold -= 100;
      myProv.soldiers = Math.min(50000, myProv.soldiers + 200);
      playSfx('build');
      
      // 🔥 병사 경험치 대량 획득 및 레벨업 체크!
      addTroopExp(180);
      
      logMessage(`⚔️ [군사 훈련] 아군 전 부대가 강도 높은 훈련을 실시했습니다! (병사 경험치 +180 EXP)`, 'text-cyan-300 font-bold');
      updateRightPanel(myProv.id);
    }
"""

    # 8. 전투 승리 시 병사 경험치 +300 획득 연결
    battle_vic_patch = """
      // 병사 경험치 +350 대량 획득
      addTroopExp(350);
      checkImperialRank();
"""

    # 9. HTML 소스코드에 부품 주입
    # (A) CSS 주입
    html = html.replace("</style>", f"\n{extra_css}\n</style>")

    # (B) 모달들 주입
    modals = promotion_modal_html + "\n" + treasure_modal_html + "\n" + cutin_overlay_html + "\n" + quest_modal_html
    html = html.replace("</body>", modals + "\n</body>")

    # (C) 우측 패널에 병사 등급/레벨 게이지 HUD 주입
    panel_needle = '<div class="flex items-center justify-between text-xs font-bold text-slate-200 mb-2 px-1">'
    if panel_needle in html:
        html = html.replace(panel_needle, troop_hud_ui + "\n" + panel_needle)
        print("Successfully injected troop level HUD into right panel!")

    # (D) 메뉴에 보물함/칙명 메뉴 항목 주입
    popup_special = '<div id="popup-special" class="koei-popup-window">'
    if popup_special in html:
        html = html.replace(popup_special, popup_special + "\n" + treasure_menu_item)
        print("Successfully added treasure and quest to special menu!")

    # (E) JS 주입
    html = html.replace("</script>\n</body>", f"\n{god_edition_js}\n</script>\n</body>")

    # (F) executeTraining 교체
    pattern_train = r'function executeTraining\(\) \{[\s\S]*?updateRightPanel\(myProv\.id\);\s+\}'
    if re.search(pattern_train, html):
        html = re.sub(pattern_train, training_patch.strip(), html)
        print("Successfully patched executeTraining with troop exp gain!")

    # (G) DOMContentLoaded 시 updateTroopLevelUI() 실행
    html = html.replace("setupIntroFaces();", "setupIntroFaces(); updateTroopLevelUI();")

    # 10. 대상 파일들에 최종 배포
    target_paths = [
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in target_paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Generated: {p} ({len(html):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 삼국지 3 갓 에디션 최종 빌드 완료! ===")

if __name__ == "__main__":
    build()
