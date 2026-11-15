# -*- coding: utf-8 -*-
"""
삼국지 헥스 전장: 부대 선택·직접 공격 5대 혁신 종합 수정보완 스크립트
1. [아군 부대 원클릭 선택 퀵바] (우측 상단 상시 배치)
2. [전장 진입 및 매 턴 시작 시 첫 번째 아군 자동 선택] (선택 막힘 제로)
3. [행동 완료 시 다음 미행동 아군 자동 순차 선택] (연속 공격 보장)
4. [타일 기반 45px 정밀 히트테스트 및 빈 땅 클릭 시 선택 보호] (클릭 미스 완전 방지)
5. [원클릭 즉시 자동 공격 버튼] (마우스 조준 없이 가장 가까운 적 1초 만에 섬멸)
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. 우측 사이드 패널 상단에 [아군 부대 원클릭 선택 퀵바] HTML 주입
# ---------------------------------------------------------------------------
quick_bar_html = """      <!-- 🛡️ 아군 부대 원클릭 선택 퀵바 (클릭 미스 완전 박멸) -->
      <div class="koei-frame p-2 rounded-lg flex flex-col gap-1 border-2 border-yellow-600/70 shadow-lg">
        <div class="flex justify-between items-center text-[11px] text-yellow-300 font-black border-b border-yellow-700/50 pb-0.5">
          <span>⚡ 아군 부대 원클릭 선택</span>
          <span class="text-[9px] text-cyan-300">(클릭 시 즉시 선택)</span>
        </div>
        <div id="allyQuickSelectBar" class="grid grid-cols-2 gap-1 mt-0.5">
          <!-- JS로 동적 렌더링 -->
        </div>
      </div>
"""

# unitDetailBox 위에 퀵바를 삽입
target_panel_start = '<div class="lg:col-span-1 flex flex-col gap-2">'
if quick_bar_html not in content and target_panel_start in content:
    content = content.replace(target_panel_start, target_panel_start + "\n" + quick_bar_html, 1)
    print("SUCCESS: Added allyQuickSelectBar HTML.")

# ---------------------------------------------------------------------------
# 2. 전술 군령 패널에 [⚡ 원클릭 즉시 타격] 스마트 버튼 추가
# ---------------------------------------------------------------------------
old_btn_attack = '<button id="btnAttack" onclick="onCmdAttack()"'
new_btn_attack_combo = """<!-- ⚡ 원클릭 즉시 자동 공격 스마트 버튼 -->
            <button id="btnAutoSmartAttack" onclick="onCmdAutoSmartAttack()" class="col-span-2 py-2 px-3 rounded bg-gradient-to-r from-red-800 via-amber-600 to-red-800 hover:from-red-700 hover:to-amber-500 border-2 border-yellow-300 text-yellow-200 font-black text-xs shadow-xl flex items-center justify-center gap-1.5 transition transform hover:scale-[1.02] active:scale-95 animate-pulse">
              <span>⚡</span> <span>원클릭 즉시 공격 (최인접 적 자동 타격)</span>
            </button>
            <button id="btnAttack" onclick="onCmdAttack()" """

if "btnAutoSmartAttack" not in content and old_btn_attack in content:
    content = content.replace(old_btn_attack, new_btn_attack_combo, 1)
    print("SUCCESS: Added btnAutoSmartAttack HTML.")

# ---------------------------------------------------------------------------
# 3. 자바스크립트 전면 강화 (퀵바 렌더링, 자동 순차 선택, 선택 보호, 스마트 공격)
# ---------------------------------------------------------------------------
patch_js = """
    // ==========================================================================
    // 🛡️ 아군 부대 원클릭 선택 퀵바 실시간 렌더링 시스템
    // ==========================================================================
    function renderAllyQuickBar() {
      const container = document.getElementById("allyQuickSelectBar");
      if (!container) return;
      const allies = UNITS.filter(u => u.faction === 'ally' && u.troops > 0);
      const selected = sam5BattleState.selectedUnit;

      container.innerHTML = allies.map(u => {
        const isSel = selected && selected.id === u.id;
        const isActed = u.acted;
        
        let bgClass = "bg-slate-900 border-slate-700 text-slate-300 hover:bg-blue-900/60";
        if (isSel) {
          bgClass = "bg-amber-600 border-yellow-300 text-white font-black shadow-md ring-2 ring-yellow-400 animate-pulse";
        } else if (isActed) {
          bgClass = "bg-slate-950/70 border-slate-800 text-slate-500 opacity-60";
        }

        const actLabel = isActed ? '완료' : '대기';
        return `
          <button onclick="selectUnitById('${u.id}')" 
                  class="py-1 px-1.5 rounded border text-[11px] flex items-center justify-between transition ${bgClass}">
            <span class="flex items-center gap-1 font-bold">
              <span>${u.avatar}</span>
              <span class="truncate max-w-[65px]">${u.name}</span>
            </span>
            <span class="text-[9px] px-1 rounded ${isActed ? 'bg-slate-800 text-slate-400' : 'bg-cyan-900 text-cyan-200'}">
              ${actLabel}
            </span>
          </button>
        `;
      }).join('');
    }

    // ID로 부대 즉시 선택
    function selectUnitById(unitId) {
      if (sam5BattleState.battleOver || sam5BattleState.phase !== 'ally') return;
      const u = UNITS.find(unit => unit.id === unitId && unit.faction === 'ally' && unit.troops > 0);
      if (u) {
        selectUnit(u);
        playSound('fanfare');
        renderBattlefield();
      }
    }

    // ⚡ 원클릭 즉시 자동 공격: 현재 선택된 아군이 가장 가까운 적을 자동 타격!
    function onCmdAutoSmartAttack() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') {
        // 선택된 아군이 없으면 첫 번째 미행동 아군 자동 선택
        const firstAlly = UNITS.find(unit => unit.faction === 'ally' && unit.troops > 0 && !unit.acted);
        if (firstAlly) {
          selectUnit(firstAlly);
          onCmdAutoSmartAttack();
        } else {
          logBattle("행동 가능한 아군 부대가 없습니다. 턴을 종료하십시오.");
        }
        return;
      }

      // 살아있는 모든 적 중 가장 가까운 적 탐색
      const aliveEnemies = UNITS.filter(en => en.faction === 'enemy' && en.troops > 0);
      if (aliveEnemies.length === 0) {
        logBattle("전장에 생존한 적 부대가 없습니다!");
        return;
      }

      let closestEnemy = null;
      let minDistance = 999;
      aliveEnemies.forEach(en => {
        const d = getHexDistance(u.q, u.r, en.q, en.r);
        if (d < minDistance) {
          minDistance = d;
          closestEnemy = en;
        }
      });

      if (closestEnemy) {
        logBattle(`⚡ [자동 타격] ${u.name} 부대가 가장 인접한 적장 ${closestEnemy.name}을 정밀 조준하여 공격합니다!`);
        executeDirectAttack(u, closestEnemy);
        renderBattlefield();
      }
    }
"""

# selectUnit 전면 강화: 퀵바 연동 및 버튼 갱신
old_select_unit = r"function selectUnit\(unit\) \{[\s\S]*?updateActionCommands\(\);\s*\}"
new_select_unit = """function selectUnit(unit) {
      if (!unit || unit.troops <= 0) return;
      sam5BattleState.selectedUnit = unit;
      updateUnitDetailCard(unit);

      if (unit.faction === "ally" && !unit.moved && !unit.acted && sam5BattleState.phase === "ally") {
        computeMovementRange(unit);
      } else {
        sam5BattleState.reachableHexes = [];
      }

      sam5BattleState.attackableTargets = [];
      updateActionCommands();
      renderAllyQuickBar();
    }"""

content = re.sub(old_select_unit, new_select_unit, content, count=1)

# finishUnitAction 전면 강화: 다음 미행동 아군 자동 순차 선택 탑재
old_finish_action = r"function finishUnitAction\(u\) \{[\s\S]*?renderBattlefield\(\);[\s\S]*?\n\s*\}"
new_finish_action = """function finishUnitAction(u) {
      u.acted = true;
      u.moved = true;
      sam5BattleState.selectedUnit = null;
      sam5BattleState.reachableHexes = [];
      sam5BattleState.attackableTargets = [];
      clearSkillMode();

      // 다음 행동 가능한 아군 자동 순차 선택 (원활한 조작 보장)
      const nextAlly = UNITS.find(unit => unit.faction === 'ally' && unit.troops > 0 && !unit.acted);
      if (nextAlly && sam5BattleState.phase === 'ally' && !sam5BattleState.battleOver) {
        sam5BattleState.selectedUnit = nextAlly;
        updateUnitDetailCard(nextAlly);
        if (!nextAlly.moved) computeMovementRange(nextAlly);
        logBattle(`🗡️ 다음 아군 [${nextAlly.name}] 부대로 순차 전환되었습니다. 적을 클릭하여 공격하십시오!`);
      } else {
        deselectUnit();
      }

      updateActionCommands();
      renderAllyQuickBar();
      renderBattlefield();

      // 아군 모든 부대가 행동 완료했는지 검사
      const activeAllies = UNITS.filter(unit => unit.faction === 'ally' && unit.troops > 0);
      const allActed = activeAllies.every(unit => unit.acted);
      if (allActed && !sam5BattleState.battleOver) {
        logBattle("🚩 아군 전 부대가 행동을 마쳤습니다. 턴을 종료하고 적군 턴으로 넘어갑니다.");
        setTimeout(() => {
          if (sam5BattleState.phase === 'ally') endPlayerTurn();
        }, 600);
      }
    }"""

content = re.sub(old_finish_action, new_finish_action, content, count=1)

# 캔버스 클릭 리스너 전면 교체: 타일 기반 45px 정밀 히트테스트 및 선택 보호(Deselect Protection)
old_canvas_listener = r"canvas\.addEventListener\(\"click\", function\(e\) \{[\s\S]*?function handleHexClick"
new_canvas_listener = """canvas.addEventListener("click", function(e) {
      if (sam5BattleState.battleOver) return;
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      const mx = (e.clientX - rect.left) * scaleX;
      const my = (e.clientY - rect.top) * scaleY;

      // 1. 가장 가까운 헥스 타일 찾기
      let closestHex = null;
      let minTileDist = 9999;
      for (let r = 0; r < GRID_ROWS; r++) {
        for (let q = 0; q < GRID_COLS; q++) {
          const { x, y } = getHexPixel(q, r);
          const dist = Math.hypot(mx - x, my - y);
          if (dist < minTileDist) {
            minTileDist = dist;
            closestHex = { q, r };
          }
        }
      }

      // 2. 해당 헥스에 위치한 유닛 또는 반경 42px 내 유닛 감지 (초정밀 타겟팅)
      let clickedUnit = null;
      if (closestHex && minTileDist < HEX_RADIUS * 1.25) {
        clickedUnit = findUnitAt(closestHex.q, closestHex.r);
      }
      if (!clickedUnit) {
        for (const u of UNITS) {
          if (u.troops <= 0) continue;
          const { x, y } = getHexPixel(u.q, u.r);
          const d = Math.hypot(mx - x, my - y);
          if (d < 42) {
            clickedUnit = u;
            break;
          }
        }
      }

      // 🎯 유닛을 클릭한 경우
      if (clickedUnit) {
        handleUnitClick(clickedUnit);
        return;
      }

      // 🎯 빈 타일을 클릭한 경우 (이동 또는 조준)
      if (closestHex && minTileDist < HEX_RADIUS * 1.25) {
        handleTileClick(closestHex.q, closestHex.r);
      }
    });

    // 🎯 유닛 클릭 핸들러: 아군 선택 / 적군 원클릭 즉시 공격
    function handleUnitClick(unit) {
      const selected = sam5BattleState.selectedUnit;

      // 특기/명령 조준 모드(화계, 원거리 조준 등)인 경우
      if (sam5BattleState.skillMode) {
        executeSkillAction(sam5BattleState.skillMode, unit);
        clearSkillMode();
        renderBattlefield();
        return;
      }

      // 아군 턴이 아니면 단순 카드 조회
      if (sam5BattleState.phase !== "ally") {
        selectUnit(unit);
        renderBattlefield();
        return;
      }

      // A. 아군 부대를 클릭한 경우 -> 선택 및 이동범위 활성화
      if (unit.faction === "ally") {
        selectUnit(unit);
        logBattle(`🛡️ 아군 [${unit.name}] 부대를 선택했습니다. 적 부대를 클릭하거나 [원클릭 즉시 공격]을 누르십시오!`);
        renderBattlefield();
        return;
      }

      // B. 적군 부대를 클릭한 경우 -> 이미 선택된 아군이 있으면 100% 즉시 공격 감행!
      if (unit.faction === "enemy") {
        if (selected && selected.faction === "ally" && !selected.acted) {
          executeDirectAttack(selected, unit);
          renderBattlefield();
          return;
        } else {
          // 선택된 아군이 아직 없으면 첫 번째 미행동 아군을 즉시 골라주고 그 적을 타격!
          const firstAlly = UNITS.find(u => u.faction === 'ally' && u.troops > 0 && !u.acted);
          if (firstAlly) {
            selectUnit(firstAlly);
            executeDirectAttack(firstAlly, unit);
            renderBattlefield();
            return;
          } else {
            selectUnit(unit);
            renderBattlefield();
            return;
          }
        }
      }
    }

    // 🎯 빈 타일 클릭 핸들러: 이동 & 실수 클릭 보호(Deselect Protection)
    function handleTileClick(q, r) {
      // 1. 공격/특기 조준 발동 모드 (화계 등 타일 조준)
      if (sam5BattleState.skillMode) {
        const target = sam5BattleState.attackableTargets.find(t => t.q === q && t.r === r);
        if (target) {
          executeSkillAction(sam5BattleState.skillMode, target);
        } else {
          logBattle("명령 대상이 올바르지 않아 군령을 철회했습니다.");
        }
        clearSkillMode();
        renderBattlefield();
        return;
      }

      const selectedUnit = sam5BattleState.selectedUnit;

      // 2. 이동 가능 타일 클릭 시 부대 이동
      const canMove = sam5BattleState.reachableHexes.find(h => h.q === q && h.r === r);
      if (canMove && selectedUnit && !selectedUnit.moved) {
        selectedUnit.q = q;
        selectedUnit.r = r;
        selectedUnit.moved = true;
        sam5BattleState.reachableHexes = [];

        // 보급창 도달 검사
        const destTerrain = (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] !== undefined) ? MAP_TERRAIN[r][q] : 0;
        if (destTerrain === 4 && !sam5BattleState.supplyBurned) {
          triggerSupplyRaid(selectedUnit);
        } else if (destTerrain === 8 && !sam5BattleState.allySupplyBurned) {
          logBattle(`🌾 아군 ${selectedUnit.name} 부대가 본진 군량고를 경비하고 있습니다.`);
        } else {
          logBattle(`${selectedUnit.name} 부대가 진격했습니다. 이제 적을 클릭하여 공격하십시오!`);
        }

        playSound('fanfare');
        updateActionCommands();
        renderBattlefield();
        return;
      }

      // 3. 🛡️ 실수 클릭 보호: 빈 땅을 잘못 클릭해도 아군 부대 선택을 풀지 않음!
      if (selectedUnit && selectedUnit.faction === 'ally') {
        logBattle(`💡 이동할 수 없는 위치입니다. 녹색 이동 타일을 클릭하거나, 붉은 적군을 클릭하여 공격하십시오.`);
        return;
      }

      deselectUnit();
      renderBattlefield();
    }

    function handleHexClick"""

content = re.sub(old_canvas_listener, new_canvas_listener, content, count=1)

# 전장 시작 시 및 플레이어 턴 시작 시 첫 번째 아군 자동 선택 추가
old_reset = r"deselectUnit\(\);\s*\}"
new_reset = """const firstAlly = UNITS.find(u => u.faction === 'ally' && u.troops > 0 && !u.acted);
      if (firstAlly) {
        selectUnit(firstAlly);
      } else {
        deselectUnit();
      }
      renderAllyQuickBar();
      renderBattlefield();
    }"""
content = re.sub(old_reset, new_reset, content, count=1)

old_player_turn = r"function startPlayerTurn\(\) \{[\s\S]*?renderBattlefield\(\);\s*\}"
new_player_turn = """function startPlayerTurn() {
      sam5BattleState.phase = "ally";
      sam5BattleState.turn++;
      UNITS.forEach(u => {
        if (u.faction === "ally") {
          u.acted = false;
          u.moved = false;
        }
      });
      updateTurnBanner();
      logBattle(`🚩 제 ${sam5BattleState.turn} 턴 시작! 아군에게 명령을 내리십시오.`);

      // 턴 시작 시 첫 번째 아군 부대 자동 선택!
      const firstAlly = UNITS.find(u => u.faction === 'ally' && u.troops > 0 && !u.acted);
      if (firstAlly) {
        selectUnit(firstAlly);
      } else {
        deselectUnit();
      }

      renderAllyQuickBar();
      renderBattlefield();
    }"""
content = re.sub(old_player_turn, new_player_turn, content, count=1)

# 추가 JS 함수 주입 (renderAllyQuickBar, onCmdAutoSmartAttack 등)
content = content.replace("function selectUnit(unit) {", patch_js + "\n    function selectUnit(unit) {", 1)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Applied all 5 major upgrades to 삼국지 HTML.")

# 동기화
TARGETS = [
    r"C:\Users\LENOVO\Desktop\sam3_update.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
]

for t in TARGETS:
    shutil.copy2(TARGET_FILE, t)
    print(f"Synced -> {t}")
