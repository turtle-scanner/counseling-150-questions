# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

command_handlers_code = """
    // ==========================================================================
    // ⚔️ 전술 군령 실행 핸들러 모음 (안행 궁시 초장거리 4칸 사격 & 화계 & 일제합공)
    // ==========================================================================
    function onCmdAttack() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      sam5BattleState.skillMode = 'attack';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, 1);

      // 바둑 3면 포위 가능 적 검사
      const encircled = sam5BattleState.attackableTargets.find(e => getSurroundingUnits(e, 'ally').length >= 3);
      if (encircled) {
        logBattle(`⬛⬜⚡ [바둑의 3면 포위망 감지!] ${encircled.name}을 클릭하여 일제합공(300% 극딜)을 감행하십시오!`);
      } else {
        logBattle(`🗡️ [돌격 공격] 공격할 인접 적 부대(붉은 타일)를 클릭하십시오.`);
      }
      renderBattlefield();
    }

    function onCmdArchery() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      const isHwang = u.name.includes('황충');

      // 안행진이 아니면 자동으로 안행진(雁行陣)으로 전술 전환!
      if (u.formation !== 'anhaeng' && !isHwang) {
        u.formation = 'anhaeng';
        logBattle(`🏹 [진형 전환] ${u.name} 부대가 장거리 사격을 위해 [안행진(雁行)]으로 전술을 전환했습니다! (사거리 4칸)`);
        playSound('fanfare');
        updateUnitDetailCard(u);
      }

      const arcRange = 4; // 사거리 4칸 초장거리 지원!
      sam5BattleState.skillMode = 'archery';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, arcRange);

      if (sam5BattleState.attackableTargets.length === 0) {
        logBattle(`🏹 사거리 ${arcRange}칸 이내에 조준할 수 있는 적 부대가 없습니다.`);
      } else {
        logBattle(`🏹 [안행 궁시 장거리 사격] 사거리 ${arcRange}칸 이내의 붉은 타겟 적을 클릭하여 일제사격을 퍼부으십시오!`);
      }
      renderBattlefield();
    }

    function onCmdFireSkill() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      const isHwang = u.name.includes('황충');
      const fireRange = isHwang ? 4 : 2; // 황충은 사거리 4칸 불화살 폭격!

      sam5BattleState.skillMode = 'fire';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, fireRange);

      if (isHwang) {
        logBattle(`🔥🏹 [황충 맹화시] 사거리 ${fireRange}칸 이내의 적을 클릭하여 불화살을 쏟아부으십시오! (화염 지속 생성)`);
      } else {
        logBattle(`🔥 [화계] 사거리 ${fireRange}칸 이내의 적이나 타일을 클릭하여 화공을 감행하십시오!`);
      }
      renderBattlefield();
    }

    function onCmdChaosSkill() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      sam5BattleState.skillMode = 'chaos';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, 2);
      logBattle(`🌀 [혼란 계략] 혼란에 빠뜨릴 적 부대를 클릭하십시오. (사거리 2칸)`);
      renderBattlefield();
    }

    function onCmdFlurry() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      sam5BattleState.skillMode = 'attack';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, 1);
      logBattle(`⚡ [분기 맹공] 인접한 적에게 강력한 연속 공격을 가합니다!`);
      renderBattlefield();
    }

    function clearSkillMode() {
      sam5BattleState.skillMode = null;
      sam5BattleState.attackableTargets = [];
    }

    function finishUnitAction(u) {
      u.acted = true;
      u.moved = true;
      sam5BattleState.selectedUnit = null;
      sam5BattleState.reachableHexes = [];
      sam5BattleState.attackableTargets = [];
      clearSkillMode();
      updateActionCommands();
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
    }
"""

# executeSkillAction 함수 바로 위에 command_handlers_code를 삽입
target_point = "function executeSkillAction(mode, targetPos) {"
idx = text.find(target_point)
if idx != -1:
    text = text[:idx] + command_handlers_code + "\n    " + text[idx:]
    print("Command handlers successfully injected before executeSkillAction!")
else:
    print("ERROR: executeSkillAction not found!")

# 파일 저장 및 전역 동기화
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

print("All synchronized successfully!")
