# -*- coding: utf-8 -*-
"""
삼국지 웹게임: 전술 전투 아군 부대 선택/원클릭 공격/돌격 이동 및 훈련 시 전 부대 레벨 +1 즉시 상승 패치
"""
import re

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. executeTraining() 전면 개편: 훈련 시 즉시 전 부대 레벨 +1 상승!
# ---------------------------------------------------------------------------
old_training_pattern = r"function executeTraining\(\)\s*\{[\s\S]*?updateRightPanel\(myProv\.id\);\s*\}"

new_training_code = """function executeTraining() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (!consumeActionPoint('훈련')) return;
      if (myProv.gold < 100) { 
        alert('군사 훈련을 위한 군비(금 100전)가 부족합니다.'); 
        refundActionPoint();
        return; 
      }
      myProv.gold -= 100;
      myProv.soldiers = Math.min(50000, myProv.soldiers + 500);
      playSfx('victory');
      
      // ⚔️ 훈련 1회당 전 부대 병과 레벨 즉시 +1 상승!
      if (gameState.troopLevel === undefined) gameState.troopLevel = 1;
      gameState.troopLevel++;
      gameState.troopExp = 0; // 다음 훈련을 위해 리셋
      
      // 레벨에 따른 정규 병종 승급 트리
      let promoMsg = '';
      if (gameState.troopLevel === 2) {
        gameState.troopTypeName = '숙련보병';
        promoMsg = '▶ [병종 진화] 숙련보병 승급! (공방 1.15배)';
      } else if (gameState.troopLevel === 3) {
        gameState.troopTypeName = '기마병';
        promoMsg = '▶ [병종 대승급] 기마병(騎馬兵) 승급! (공방 1.3배 & 기동력 +1)';
      } else if (gameState.troopLevel === 4) {
        gameState.troopTypeName = '강궁병';
        promoMsg = '▶ [병종 진화] 강궁병(强弓兵) 승급! (공방 1.45배 & 사거리 지원)';
      } else if (gameState.troopLevel === 5) {
        gameState.troopTypeName = '연노병';
        promoMsg = '▶ [병종 대승급] 제갈연노병(連弩兵) 승급! (공방 1.6배 & 연타 사격)';
      } else if (gameState.troopLevel === 6) {
        gameState.troopTypeName = '전차병';
        promoMsg = '▶ [병종 대승급] 철갑전차병(戰車兵) 승급! (공방 1.8배 & 방어선 돌파)';
      } else if (gameState.troopLevel === 7) {
        gameState.troopTypeName = '돌격기병';
        promoMsg = '▶ [병종 대승급] 호표기 돌격기병 승급! (공방 2.0배 & 치명타 2배)';
      } else if (gameState.troopLevel === 8) {
        gameState.troopTypeName = '서량철기병';
        promoMsg = '▶ [병종 대승급] 서량 철기병 승급! (공방 2.3배 & 철벽 방어)';
      } else if (gameState.troopLevel >= 9) {
        gameState.troopTypeName = '천하무적군';
        const mult = (1.0 + (gameState.troopLevel - 1) * 0.2).toFixed(1);
        promoMsg = `▶ [최종 신화] 천하무적군(天下無敵) 달성! (공방 ${mult}배 극대화)`;
      }

      updateTroopLevelUI();
      logMessage(`⚔️🎖️ [전군 맹훈련 대성공!] 아군 전 부대의 숙련도 레벨이 Lv.${gameState.troopLevel}(으)로 +1 레벨업했습니다! ${promoMsg}`, 'text-yellow-300 font-black text-sm');
      updateRightPanel(myProv.id);

      alert(`⚔️🎖️ [군사 맹훈련 완수 - 전 부대 레벨 +1 레벨업!]\\n\\n주군의 엄격하고 맹렬한 훈시 아래 전군이 피땀 흘려 훈련을 마쳤습니다!\\n\\n▶ 부대 병과 레벨: Lv.${gameState.troopLevel} [${gameState.troopTypeName}] (+1 UP!)\\n▶ 전투 공방 배율: ${(1.0 + (gameState.troopLevel - 1) * 0.15).toFixed(2)}배 대폭 강화!\\n${promoMsg}\\n▶ 헥스 전장 출전 시 모든 아군 부대의 공격력, 방어력, 돌파력이 영구 상승합니다!`);
    }"""

if re.search(old_training_pattern, content):
    content = re.sub(old_training_pattern, new_training_code, content, count=1)
    print("SUCCESS: Replaced executeTraining with level+1 logic.")
else:
    print("WARNING: Could not find old executeTraining pattern.")

# ---------------------------------------------------------------------------
# 2. disableAllCommands() 함수 정의 보장
# ---------------------------------------------------------------------------
disable_commands_code = """    function disableAllCommands() {
      const ids = ["btnAttack", "btnArchery", "btnFireSkill", "btnChaosSkill", "btnFlurry", "btnFormation", "btnDuel", "btnWait"];
      ids.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = true;
      });
    }
"""

if "function disableAllCommands" not in content:
    content = content.replace("function deselectUnit() {", disable_commands_code + "\n    function deselectUnit() {")
    print("SUCCESS: Added disableAllCommands function.")

# ---------------------------------------------------------------------------
# 3. handleHexClick(q, r) 및 selectUnit(unit) 전면 개편:
#    - 아군 부대 선택 후 전장의 적 클릭 시: 인접 공격 / 원거리 사격 / 돌격 이동 공격 100% 자동 발동!
#    - 이동 타일 클릭 시 정상 이동 후 즉시 공격 버튼 갱신
# ---------------------------------------------------------------------------
old_handle_hex_click_pattern = r"function handleHexClick\(q, r\)\s*\{[\s\S]*?renderBattlefield\(\);\s*\}"

new_handle_hex_click_code = """function handleHexClick(q, r) {
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

      // 2. [★원클릭 공격 혁신★] 아군 부대가 선택된 상태에서 적 부대를 직접 클릭했을 때 -> 즉시 공격/원거리/돌격 감행!
      if (selectedUnit && selectedUnit.faction === "ally" && !selectedUnit.acted && sam5BattleState.phase === "ally" && clickedUnit && clickedUnit.faction === "enemy") {
        const dist = getHexDistance(selectedUnit.q, selectedUnit.r, clickedUnit.q, clickedUnit.r);
        const isArcher = isMasterArcher(selectedUnit);

        // A. 인접 1칸 적 -> 즉시 근접 공격 또는 3면 포위 일제합공!
        if (dist === 1) {
          executeSkillAction('attack', clickedUnit);
          clearSkillMode();
          renderBattlefield();
          return;
        }

        // B. 사거리 4칸 이내 적 -> 원거리 신궁/맹화시/안행 궁시 사격!
        if (dist <= 4 && (isArcher || selectedUnit.formation === 'anhaeng')) {
          executeSkillAction('archery', clickedUnit);
          clearSkillMode();
          renderBattlefield();
          return;
        }

        // C. [★자동 돌격 이동 공격★] 이동하지 않은 상태라면, 적 인접 빈 타일로 쇄도 후 근접 공격!
        if (!selectedUnit.moved) {
          computeMovementRange(selectedUnit);
          const adjHexes = getHexNeighbors(clickedUnit.q, clickedUnit.r);
          const chargeHex = sam5BattleState.reachableHexes.find(h => adjHexes.some(a => a.q === h.q && a.r === h.r));
          if (chargeHex) {
            logBattle(`🏇 [질풍 돌격!] ${selectedUnit.name} 부대가 적장 ${clickedUnit.name}을 향해 쇄도하여 통렬한 돌격 공격을 감행합니다!`);
            selectedUnit.q = chargeHex.q;
            selectedUnit.r = chargeHex.r;
            selectedUnit.moved = true;
            sam5BattleState.reachableHexes = [];
            playSound('fanfare');
            executeSkillAction('attack', clickedUnit);
            renderBattlefield();
            return;
          }
        }

        // D. 적이 사거리 밖인 경우: 적에게 가장 가까운 이동 가능 타일로 급속 진격
        if (!selectedUnit.moved && sam5BattleState.reachableHexes.length > 0) {
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
            logBattle(`🏇 ${selectedUnit.name} 부대가 적장 ${clickedUnit.name}을 향해 급속 진격했습니다!`);
            playSound('fanfare');
            updateActionCommands();
            renderBattlefield();
            return;
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

      // 4. 부대 선택 (아군 우선 및 교대 선택 자유화)
      if (clickedUnit) {
        selectUnit(clickedUnit);
      } else {
        deselectUnit();
      }
      renderBattlefield();
    }"""

if re.search(old_handle_hex_click_pattern, content):
    content = re.sub(old_handle_hex_click_pattern, new_handle_hex_click_code, content, count=1)
    print("SUCCESS: Replaced handleHexClick with smart attack/charge logic.")
else:
    print("WARNING: Could not find old handleHexClick pattern.")

# ---------------------------------------------------------------------------
# 4. updateActionCommands() 전면 개편:
#    - 아군 부대 선택 시 진형변경/행동완료 항시 활성
#    - 근접공격/안행궁시 버튼 활성화 및 이동 후 타격 가능 적 타겟팅
# ---------------------------------------------------------------------------
old_update_commands_pattern = r"function updateActionCommands\(\)\s*\{[\s\S]*?if \(btnWait\) btnWait\.disabled = false;\s*\}"

new_update_commands_code = """function updateActionCommands() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.faction !== "ally" || u.acted || sam5BattleState.phase !== "ally") {
        disableAllCommands();
        return;
      }

      const isArcher = isMasterArcher(u);
      const adjEnemies = getEnemiesInRange(u, 1);
      const longRangeEnemies = getEnemiesInRange(u, 4);
      const allEnemies = UNITS.filter(en => en.faction === "enemy" && en.troops > 0);

      const btnAtk = document.getElementById("btnAttack");
      const btnArc = document.getElementById("btnArchery");
      const btnFire = document.getElementById("btnFireSkill");
      const btnChaos = document.getElementById("btnChaosSkill");
      const btnFlurry = document.getElementById("btnFlurry");
      const btnForm = document.getElementById("btnFormation");
      const btnDuel = document.getElementById("btnDuel");
      const btnWait = document.getElementById("btnWait");

      // 1. 진형 변경 & 대기(행동완료)는 언제나 항시 활성화!
      if (btnForm) btnForm.disabled = false;
      if (btnWait) btnWait.disabled = false;

      // 2. 🗡️ 근접 공격: 인접한 적이 있거나, 이동 전/후로 공격할 적이 존재하면 활성화!
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

      // 3. 🏹 안행 궁시: 사거리 4칸 이내 적이 있거나 원거리 사격 가능 시 활성화!
      if (btnArc) {
        btnArc.disabled = (longRangeEnemies.length === 0);
        if (u.name.includes('황충')) {
          btnArc.innerHTML = '🏹 황충 신궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-emerald-800 hover:bg-emerald-700 border-2 border-yellow-300 text-yellow-300 font-black text-xs shadow-lg transition";
        } else if (u.name.includes('태사자')) {
          btnArc.innerHTML = '🏹 태사자 맹궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-cyan-800 hover:bg-cyan-700 border-2 border-cyan-300 text-cyan-200 font-black text-xs shadow-lg transition";
        } else if (u.name.includes('서황') || u.name.includes('공손찬')) {
          btnArc.innerHTML = `🏹 ${u.name} 명궁 (사거리4)`;
          btnArc.className = "px-3 py-2 rounded bg-teal-800 hover:bg-teal-700 border-2 border-yellow-400 text-yellow-200 font-black text-xs shadow-lg transition";
        } else if (u.formation === 'anhaeng') {
          btnArc.innerHTML = '🏹 안행 궁시 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border-2 border-blue-400 text-cyan-200 font-black text-xs shadow transition";
        } else {
          btnArc.innerHTML = '🏹 안행 궁시 (전환사격)';
          btnArc.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-500 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      // 4. 🔥 불화살 & 화계
      if (btnFire) {
        if (isArcher) {
          btnFire.disabled = (longRangeEnemies.length === 0);
          btnFire.innerHTML = `🔥 ${u.name} 맹화시 (불화살)`;
          btnFire.className = "px-3 py-2 rounded bg-red-800 hover:bg-red-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else {
          const hasFire = u.skills.includes("화계") || u.skills.includes("화시") || u.int >= 75;
          const fireEnemies = getEnemiesInRange(u, 2);
          btnFire.disabled = !hasFire || fireEnemies.length === 0;
          btnFire.innerHTML = '🔥 화계 (풍향확산)';
          btnFire.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      // 5. 🌀 혼란 & ⚡ 분기
      if (btnChaos) {
        const canChaos = u.skills.includes("혼란") || u.int >= 75;
        btnChaos.disabled = !canChaos || getEnemiesInRange(u, 2).length === 0;
      }
      if (btnFlurry) {
        btnFlurry.disabled = !u.skills.includes("분기") || adjEnemies.length === 0;
      }

      // 6. ⚔️ 일기토
      if (btnDuel) {
        btnDuel.disabled = (adjEnemies.length === 0 && getEnemiesInRange(u, 2).length === 0);
      }
    }"""

if re.search(old_update_commands_pattern, content):
    content = re.sub(old_update_commands_pattern, new_update_commands_code, content, count=1)
    print("SUCCESS: Replaced updateActionCommands with robust activation logic.")
else:
    print("WARNING: Could not find old updateActionCommands pattern.")

# ---------------------------------------------------------------------------
# 5. onCmdAttack() 개선: 인접 적 및 돌격 가능 적 전체 타겟팅 지원
# ---------------------------------------------------------------------------
old_cmd_attack_pattern = r"function onCmdAttack\(\)\s*\{[\s\S]*?renderBattlefield\(\);\s*\}"

new_cmd_attack_code = """function onCmdAttack() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      sam5BattleState.skillMode = 'attack';
      const adjEnemies = getEnemiesInRange(u, 1);
      
      if (adjEnemies.length > 0) {
        sam5BattleState.attackableTargets = adjEnemies;
        const encircled = adjEnemies.find(e => getSurroundingUnits(e, 'ally').length >= 3);
        if (encircled) {
          logBattle(`⬛⬜⚡ [바둑의 3면 포위망 감지!] ${encircled.name}을 클릭하여 일제합공(300% 극딜)을 감행하십시오!`);
        } else {
          logBattle(`🗡️ [돌격 공격] 공격할 인접 적 부대(붉은 타겟)를 클릭하십시오.`);
        }
      } else {
        // 인접한 적이 없으면 전장의 모든 적을 타겟으로 지정 (클릭 시 자동 돌격 진격 후 공격!)
        sam5BattleState.attackableTargets = UNITS.filter(en => en.faction === 'enemy' && en.troops > 0);
        logBattle(`🏇 [돌격 진격 공격] 타격할 적 부대(붉은 타겟)를 클릭하면 전속력으로 돌격하여 베어버립니다!`);
      }
      renderBattlefield();
    }"""

if re.search(old_cmd_attack_pattern, content):
    content = re.sub(old_cmd_attack_pattern, new_cmd_attack_code, content, count=1)
    print("SUCCESS: Replaced onCmdAttack with charge-attack targeting.")
else:
    print("WARNING: Could not find old onCmdAttack pattern.")

# ---------------------------------------------------------------------------
# 6. checkUnification() 및 renderMapPins() 천하통일 즉시 엔딩 모달 보장
# ---------------------------------------------------------------------------
if "openUnificationEnding" not in content:
    ending_helper_code = """
    function openUnificationEnding() {
      playSfx('victory');
      logMessage(`👑🏆 [천하통일 대위업 달성!] ${gameState.rulerName} 주군께서 천하 13주를 100% 전면 통일하여 한나라 황제에 즉위하셨습니다!`, 'text-yellow-300 font-black text-sm animate-pulse');
      const rNameEl = document.getElementById('ending-ruler-name');
      if (rNameEl) rNameEl.innerText = `군주 ${gameState.rulerName}`;
      openModal('unification-ending-modal');
    }
    """
    content = content.replace("function checkUnification() {", ending_helper_code + "\n    function checkUnification() {")
    print("SUCCESS: Added openUnificationEnding helper.")

# renderMapPins 최상단 또는 checkUnification에서 13주 시 즉각 오픈
content = content.replace("if (myCount === 13) {", "if (myCount === 13) {\n        openUnificationEnding();")

# ---------------------------------------------------------------------------
# 7. 파일 저장
# ---------------------------------------------------------------------------
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("ALL PATCHES APPLIED TO DESKTOP HTML FILE SUCCESSFULLY!")
