# -*- coding: utf-8 -*-
"""
삼국지 헥스 전장: 전 부대 궁시 사격 지원, 이동력 상향(기본 3칸, 추행/기마 5칸),
원클릭 자동 사격/돌격/근접 공격 100% 보장 패치
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. 이동력 상향: 기본 3칸, 추행/기마병 5칸으로 대폭 상향하여 대형 전장에서 1턴부터 시원한 진격 보장!
# ---------------------------------------------------------------------------
old_move_calc = r"const maxMove = Math\.max\(1, 2 \+ \(form \? form\.moveBonus : 0\)\);"
new_move_calc = """// 대형 13x8 전장 맞춤 기동력 상향 (기본 3칸, 추행/기마 5칸)
      const baseMove = (unit.faction === 'ally' && gameState.troopLevel >= 3) ? 4 : 3;
      const maxMove = Math.max(2, baseMove + (form ? form.moveBonus : 0));"""

if re.search(old_move_calc, content):
    content = re.sub(old_move_calc, new_move_calc, content, count=1)
    print("SUCCESS: Upgraded unit movement range (base 3, cavalry 5).")

# ---------------------------------------------------------------------------
# 2. handleHexClick(q, r) 혁신:
#    - 아군 부대 선택 후 전장의 적 클릭 시:
#      1) 인접(거리 1) -> 근접 공격 / 3면 포위 합공!
#      2) 거리 2~4칸 -> 모든 장수 화살(궁시) 사격 100% 발사! (명궁은 맹화시/신궁 극딜)
#      3) 거리 5칸 이상 -> 적 방향으로 최대 사거리 급속 진격 돌격!
# ---------------------------------------------------------------------------
old_hex_click_pattern = r"function handleHexClick\(q, r\)\s*\{[\s\S]*?renderBattlefield\(\);\s*\}"

new_hex_click_code = """function handleHexClick(q, r) {
      // 1. 공격/특기 조준 발동 모드 (화계, 원거리 궁시, 일격필살 등)
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

      const clickedUnit = findUnitAt(q, r);
      const selectedUnit = sam5BattleState.selectedUnit;

      // 2. [★원클릭 공격 완전 자동화★] 아군 부대가 선택된 상태에서 적 부대를 직접 클릭했을 때!
      if (selectedUnit && selectedUnit.faction === "ally" && !selectedUnit.acted && sam5BattleState.phase === "ally" && clickedUnit && clickedUnit.faction === "enemy") {
        const dist = getHexDistance(selectedUnit.q, selectedUnit.r, clickedUnit.q, clickedUnit.r);
        const isArcher = isMasterArcher(selectedUnit);

        // A. 인접 1칸 적 -> 즉시 칼을 뽑아 근접 공격 또는 3면 포위 일제합공!
        if (dist === 1) {
          executeSkillAction('attack', clickedUnit);
          clearSkillMode();
          renderBattlefield();
          return;
        }

        // B. 사거리 2~4칸 적 -> 모든 장수 궁시(화살) 사격 즉각 100% 발사!
        if (dist <= 4) {
          executeSkillAction('archery', clickedUnit);
          clearSkillMode();
          renderBattlefield();
          return;
        }

        // C. 거리 4칸 초과인 적 -> 적에게 닿을 수 있는 이동 가능 타일 중 가장 가까운 곳으로 전속력 돌격 진격!
        if (!selectedUnit.moved) {
          computeMovementRange(selectedUnit);
          if (sam5BattleState.reachableHexes.length > 0) {
            let bestHex = null;
            let bestDist = 999;
            sam5BattleState.reachableHexes.forEach(h => {
              const d = getHexDistance(h.q, h.r, clickedUnit.q, clickedUnit.r);
              if (d < bestDist) {
                bestDist = d;
                bestHex = h;
              }
            });

            if (bestHex) {
              selectedUnit.q = bestHex.q;
              selectedUnit.r = bestHex.r;
              selectedUnit.moved = true;
              sam5BattleState.reachableHexes = [];
              playSound('fanfare');

              const newDist = getHexDistance(selectedUnit.q, selectedUnit.r, clickedUnit.q, clickedUnit.r);
              if (newDist === 1) {
                logBattle(`🏇 [질풍 돌격!] ${selectedUnit.name} 부대가 적장 ${clickedUnit.name}에게 쇄도하여 통렬한 돌격을 가합니다!`);
                executeSkillAction('attack', clickedUnit);
              } else if (newDist <= 4) {
                logBattle(`🏇🏹 [돌격 사격!] ${selectedUnit.name} 부대가 진격 후 적장 ${clickedUnit.name}에게 화살비를 쏟아붓습니다!`);
                executeSkillAction('archery', clickedUnit);
              } else {
                logBattle(`🏇 ${selectedUnit.name} 부대가 적장 ${clickedUnit.name}을 향해 급속 돌격 진격했습니다!`);
                updateActionCommands();
              }
              renderBattlefield();
              return;
            }
          }
        }
      }

      // 3. 이동 타일 클릭 시 (이동 실행)
      const canMove = sam5BattleState.reachableHexes.find(h => h.q === q && h.r === r);
      if (canMove && selectedUnit && !selectedUnit.moved) {
        selectedUnit.q = q;
        selectedUnit.r = r;
        selectedUnit.moved = true;
        sam5BattleState.reachableHexes = [];

        // 특수 기믹: 보급창 도달 검사
        const destTerrain = (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] !== undefined) ? MAP_TERRAIN[r][q] : 0;
        if (destTerrain === 4 && !sam5BattleState.supplyBurned) {
          triggerSupplyRaid(selectedUnit);
        } else if (destTerrain === 8 && !sam5BattleState.allySupplyBurned) {
          logBattle(`🌾 아군 ${selectedUnit.name} 부대가 본진 군량고를 경비하고 있습니다.`);
        } else {
          logBattle(`${selectedUnit.name} 부대가 진격하여 진형을 잡았습니다.`);
        }

        playSound('fanfare');
        updateActionCommands();
        renderBattlefield();
        return;
      }

      // 4. 부대 선택 (아군 및 적군 자유 클릭)
      if (clickedUnit) {
        selectUnit(clickedUnit);
      } else {
        deselectUnit();
      }
      renderBattlefield();
    }"""

content = re.sub(old_hex_click_pattern, new_hex_click_code, content, count=1)
print("SUCCESS: Applied all-unit archery and auto-charge logic to handleHexClick.")

# ---------------------------------------------------------------------------
# 3. updateActionCommands() 버튼 상태 개선:
#    - 모든 아군 부대 선택 시 근접공격 & 궁시사격 버튼 100% 항시 활성화
# ---------------------------------------------------------------------------
old_update_pattern = r"function updateActionCommands\(\)\s*\{[\s\S]*?if \(btnDuel\)[\s\S]*?\}"

new_update_code = """function updateActionCommands() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.faction !== "ally" || u.acted || sam5BattleState.phase !== "ally") {
        disableAllCommands();
        return;
      }

      const isArcher = isMasterArcher(u);
      const adjEnemies = getEnemiesInRange(u, 1);
      const allEnemies = UNITS.filter(en => en.faction === "enemy" && en.troops > 0);

      const btnAtk = document.getElementById("btnAttack");
      const btnArc = document.getElementById("btnArchery");
      const btnFire = document.getElementById("btnFireSkill");
      const btnChaos = document.getElementById("btnChaosSkill");
      const btnFlurry = document.getElementById("btnFlurry");
      const btnForm = document.getElementById("btnFormation");
      const btnDuel = document.getElementById("btnDuel");
      const btnWait = document.getElementById("btnWait");

      // 1. 진형 변경 & 대기(행동완료)는 항시 활성화!
      if (btnForm) btnForm.disabled = false;
      if (btnWait) btnWait.disabled = false;

      // 2. 🗡️ 근접 공격: 적이 전장에 살아있으면 항시 활성화! (누르면 타겟 지정 후 돌격 공격!)
      if (btnAtk) {
        btnAtk.disabled = (allEnemies.length === 0);
        const canEncircle3 = adjEnemies.some(e => getSurroundingUnits(e, 'ally').length >= 3);
        if (canEncircle3) {
          btnAtk.innerHTML = '<span class="text-yellow-300 animate-pulse font-black">⚡ 3면포위 일제합공!</span>';
          btnAtk.className = "px-3 py-2 rounded bg-amber-600 hover:bg-amber-500 border-2 border-yellow-300 text-white font-black text-xs shadow-lg transition";
        } else if (adjEnemies.length > 0) {
          btnAtk.innerHTML = '🗡️ 근접 공격 (인접)';
          btnAtk.className = "px-3 py-2 rounded bg-blue-700 hover:bg-blue-600 border-2 border-cyan-400 text-white font-black text-xs shadow-lg transition animate-pulse";
        } else {
          btnAtk.innerHTML = '🗡️ 돌격 공격';
          btnAtk.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border border-blue-500 text-white font-bold text-xs shadow transition";
        }
      }

      // 3. 🏹 안행 궁시: 모든 장수 화살 사격 100% 항시 활성화! (사거리 4칸)
      if (btnArc) {
        btnArc.disabled = (allEnemies.length === 0);
        if (u.name.includes('황충')) {
          btnArc.innerHTML = '🏹 황충 신궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-emerald-800 hover:bg-emerald-700 border-2 border-yellow-300 text-yellow-300 font-black text-xs shadow-lg transition";
        } else if (u.name.includes('태사자')) {
          btnArc.innerHTML = '🏹 태사자 맹궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-cyan-800 hover:bg-cyan-700 border-2 border-cyan-300 text-cyan-200 font-black text-xs shadow-lg transition";
        } else if (u.name.includes('서황') || u.name.includes('공손찬')) {
          btnArc.innerHTML = `🏹 ${u.name} 명궁 (사거리4)`;
          btnArc.className = "px-3 py-2 rounded bg-teal-800 hover:bg-teal-700 border-2 border-yellow-400 text-yellow-200 font-black text-xs shadow-lg transition";
        } else {
          btnArc.innerHTML = '🏹 궁시 사격 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border-2 border-cyan-400 text-cyan-200 font-black text-xs shadow-lg transition";
        }
      }

      // 4. 🔥 불화살 & 화계
      if (btnFire) {
        btnFire.disabled = (allEnemies.length === 0);
        if (isArcher) {
          btnFire.innerHTML = `🔥 ${u.name} 맹화시 (불화살)`;
          btnFire.className = "px-3 py-2 rounded bg-red-800 hover:bg-red-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else {
          btnFire.innerHTML = '🔥 화계 (풍향확산)';
          btnFire.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      // 5. 🌀 혼란 & ⚡ 분기
      if (btnChaos) btnChaos.disabled = (allEnemies.length === 0);
      if (btnFlurry) btnFlurry.disabled = (allEnemies.length === 0);

      // 6. ⚔️ 일기토
      if (btnDuel) btnDuel.disabled = (allEnemies.length === 0);
    }"""

content = re.sub(old_update_pattern, new_update_code, content, count=1)
print("SUCCESS: Refined updateActionCommands for 100% active attack/archery buttons.")

# ---------------------------------------------------------------------------
# 4. onCmdArchery() 개선: 사거리 4칸 이내 적이 있으면 조준하고, 없으면 전장 모든 적 조준
# ---------------------------------------------------------------------------
old_archery_pattern = r"function onCmdArchery\(\)\s*\{[\s\S]*?renderBattlefield\(\);\s*\}"

new_archery_code = """function onCmdArchery() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      const isArcher = isMasterArcher(u);
      const arcRange = 4;
      sam5BattleState.skillMode = 'archery';
      
      const targets = getEnemiesInRange(u, arcRange);
      if (targets.length > 0) {
        sam5BattleState.attackableTargets = targets;
      } else {
        // 사거리 밖이면 전장의 모든 적을 타겟으로 지정하여 자동 돌격 후 사격!
        sam5BattleState.attackableTargets = UNITS.filter(en => en.faction === 'enemy' && en.troops > 0);
      }

      const title = isArcher ? (u.name.includes('황충') ? '황충 백발백중 신궁' : '태사자 강동맹궁') : '아군 원거리 궁시 사격';
      logBattle(`🏹 [${title}] 타격할 적 부대(붉은 타겟)를 클릭하여 화살비를 퍼부으십시오!`);
      renderBattlefield();
    }"""

content = re.sub(old_archery_pattern, new_archery_code, content, count=1)
print("SUCCESS: Refined onCmdArchery for seamless long-range targeting.")

# 파일 저장
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Saved updated HTML to Desktop.")

# 동기화
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
