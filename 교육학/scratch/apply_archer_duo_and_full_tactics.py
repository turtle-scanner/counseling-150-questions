# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. 태사자 데이터에 신궁/화시 명궁 특화 부여
# ==============================================================================
print("1. Updating Taishi Ci data to Master Archer...")
text = re.sub(
    r"\{\s*name:\s*'태사자 \(자의\)'[\s\S]*?\}",
    "{ name: '태사자 (자의)', war: 95, int: 72, lead: 86, icon: '🏹', title: '강동의 신궁 명장 (백발백중)', skills: ['신궁', '화시', '돌격', '분기'], element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)', arcRange: 4 }",
    text
)

# ==============================================================================
# 2. 명궁 판별 함수 및 updateActionCommands, executeSkillAction 전면 고도화
# ==============================================================================
print("2. Enhancing Master Archer & Command Handlers...")

archer_system_code = """
    // ==========================================================================
    // 🏹 명궁 판별 (황충 & 태사자): 진형 무관 초장거리 4칸 궁시 & 4칸 맹화시(불화살)
    // ==========================================================================
    function isMasterArcher(unit) {
      if (!unit) return false;
      const n = (unit.name || '') + ' ' + (unit.fullName || '');
      return n.includes('황충') || n.includes('태사자');
    }

    // ⬛⬜ 바둑의 원리: 대상 유닛에 인접(거리 1)한 우군 부대 목록 반환
    function getSurroundingUnits(targetUnit, friendlyFaction) {
      if (!targetUnit) return [];
      return UNITS.filter(u => 
        u.faction === friendlyFaction &&
        u.troops > 0 &&
        getHexDistance(u.q, u.r, targetUnit.q, targetUnit.r) === 1
      );
    }

    // 전술 군령 버튼 갱신
    function updateActionCommands() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.faction !== "ally" || u.acted || sam5BattleState.phase !== "ally") {
        disableAllCommands();
        return;
      }

      const isArcher = isMasterArcher(u);
      const form = FORMATIONS[u.formation];
      const adjEnemies = getEnemiesInRange(u, 1);
      
      // 명궁(황충/태사자)이거나 안행진이면 사거리 4칸 초장거리!
      const longRangeEnemies = getEnemiesInRange(u, 4);

      const btnAtk = document.getElementById("btnAttack");
      const btnArc = document.getElementById("btnArchery");
      const btnFire = document.getElementById("btnFireSkill");
      const btnChaos = document.getElementById("btnChaosSkill");
      const btnFlurry = document.getElementById("btnFlurry");
      const btnForm = document.getElementById("btnFormation");
      const btnDuel = document.getElementById("btnDuel");
      const btnWait = document.getElementById("btnWait");

      // 바둑 3면 포위 가능 적 검사
      const canEncircle3 = adjEnemies.some(e => getSurroundingUnits(e, 'ally').length >= 3);

      if (btnAtk) {
        btnAtk.disabled = (adjEnemies.length === 0);
        if (canEncircle3) {
          btnAtk.innerHTML = '<span class="text-yellow-300 animate-pulse font-black">⚡ 3면포위 일제합공!</span>';
          btnAtk.className = "px-3 py-2 rounded bg-amber-600 hover:bg-amber-500 border-2 border-yellow-300 text-white font-black text-xs shadow-lg transition";
        } else {
          btnAtk.innerHTML = '🗡️ 근접 공격';
          btnAtk.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border border-blue-500 text-white font-bold text-xs shadow transition";
        }
      }

      // 🏹 안행 궁시 버튼 (황충/태사자 및 4칸 이내 적 있을 시 활성화!)
      if (btnArc) {
        btnArc.disabled = (longRangeEnemies.length === 0);
        if (u.name.includes('황충')) {
          btnArc.innerHTML = '🏹 황충 신궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-emerald-800 hover:bg-emerald-700 border-2 border-yellow-300 text-yellow-300 font-black text-xs shadow-lg transition";
        } else if (u.name.includes('태사자')) {
          btnArc.innerHTML = '🏹 태사자 맹궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-cyan-800 hover:bg-cyan-700 border-2 border-cyan-300 text-cyan-200 font-black text-xs shadow-lg transition";
        } else if (u.formation === 'anhaeng') {
          btnArc.innerHTML = '🏹 안행 궁시 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border-2 border-blue-400 text-cyan-200 font-black text-xs shadow transition";
        } else {
          btnArc.innerHTML = '🏹 안행 궁시 (전환사격)';
          btnArc.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-500 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      // 🔥 불화살/화계 버튼 (황충/태사자는 4칸 불화살 항시 활성화!)
      if (btnFire) {
        if (isArcher) {
          btnFire.disabled = (longRangeEnemies.length === 0);
          const archerTitle = u.name.includes('황충') ? '황충' : '태사자';
          btnFire.innerHTML = `🔥 ${archerTitle} 맹화시 (불화살)`;
          btnFire.className = "px-3 py-2 rounded bg-red-800 hover:bg-red-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else {
          const hasFire = u.skills.includes("화계") || u.skills.includes("화시") || u.int >= 75;
          const fireEnemies = getEnemiesInRange(u, 2);
          btnFire.disabled = !hasFire || fireEnemies.length === 0;
          btnFire.innerHTML = '🔥 화계 (풍향확산)';
          btnFire.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      if (btnChaos) {
        const canChaos = u.skills.includes("혼란") || u.int >= 80;
        btnChaos.disabled = !canChaos || getEnemiesInRange(u, 2).length === 0;
      }
      if (btnFlurry) btnFlurry.disabled = !u.skills.includes("분기") || adjEnemies.length === 0;
      if (btnForm) btnForm.disabled = false;
      if (btnDuel) btnDuel.disabled = adjEnemies.length === 0;
      if (btnWait) btnWait.disabled = false;
    }

    // ==========================================================================
    // ⚔️ 전술 군령 실행 핸들러 모음 (안행 궁시 & 불화살 & 일제합공)
    // ==========================================================================
    function onCmdAttack() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      sam5BattleState.skillMode = 'attack';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, 1);

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

      const isArcher = isMasterArcher(u);

      // 안행진이 아니면 자동으로 안행진(雁行陣)으로 전술 전환!
      if (u.formation !== 'anhaeng' && !isArcher) {
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
        const title = isArcher ? (u.name.includes('황충') ? '황충 백발백중 신궁' : '태사자 강동맹궁') : '안행 궁시 장거리 사격';
        logBattle(`🏹 [${title}] 사거리 ${arcRange}칸 이내의 붉은 타겟 적을 클릭하여 화살비를 퍼부으십시오!`);
      }
      renderBattlefield();
    }

    function onCmdFireSkill() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      const isArcher = isMasterArcher(u);
      const fireRange = isArcher ? 4 : 2; // 명궁(황충/태사자)은 사거리 4칸 원거리 불화살 폭격!

      sam5BattleState.skillMode = 'fire';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, fireRange);

      if (isArcher) {
        const archerTitle = u.name.includes('황충') ? '황충 맹화시' : '태사자 불화살';
        logBattle(`🔥🏹 [${archerTitle}] 사거리 ${fireRange}칸 이내의 적을 클릭하여 불화살을 쏟아부으십시오! (화염 지속 생성)`);
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

    // ==========================================================================
    // 전투 액션 실행: 바둑 3면 포위 일제합공 & 황충/태사자 원거리 화살 및 불화살
    // ==========================================================================
    function executeSkillAction(mode, targetPos) {
      const u = sam5BattleState.selectedUnit;
      const targetUnit = findUnitAt(targetPos.q, targetPos.r);
      const isArcher = isMasterArcher(u);

      if (mode === 'attack' && targetUnit) {
        // ⬛⬜ 바둑의 원리 및 포위망 검사
        const surroundingAllies = getSurroundingUnits(targetUnit, u.faction);
        const surroundCount = surroundingAllies.length;

        const adv = getElementAdvantage(u.element, targetUnit.element);
        let dmg = calculateCombatDamage(u, targetUnit, 'melee');

        if (surroundCount >= 3) {
          // ⬛⬜ 바둑의 원리: 3면 포위 일제합공 (활로 차단 극딜 300% & 적 반격 불가!)
          dmg = Math.floor(dmg * 2.8);
          logBattle(`⬛⬜⚡ [바둑의 3면 포위 일제합공 (圍棋 一齊攻擊)!]`);
          logBattle(`적장 ${targetUnit.name}의 3대 활로(숨구멍)를 완벽 차단! 포위한 [${surroundingAllies.map(a => a.name).join(', ')}] 부대가 일제히 쇄도하여 ${dmg.toLocaleString()} 섬멸 치명타를 가했습니다!`);
          playSound('fanfare');
          playSound('slash');
          showDamagePop(targetUnit.q, targetUnit.r, `⚡3면포위 일제공격! -${dmg}`);
          targetUnit.morale = Math.max(10, targetUnit.morale - 40);
          targetUnit.acted = true; // 혼란 행동불능

          applyDamage(targetUnit, dmg);
          surroundingAllies.forEach(a => gainTroopExp(30, '3면 포위 일제공격'));
          gainTroopExp(35, '바둑의 포위 섬멸 대승');
        } else if (surroundCount === 2) {
          // ⚔️ 2면 협공 (Pincer Attack: 대미지 +50% & 적 반격 절반)
          dmg = Math.floor(dmg * 1.5);
          logBattle(`⚔️🔥 [양면 협공!] 2개 부대가 적장 ${targetUnit.name}을 협공하여 ${dmg.toLocaleString()} 피해를 입혔습니다!`);
          playSound('slash');
          showDamagePop(targetUnit.q, targetUnit.r, `🔥협공! -${dmg}`);
          applyDamage(targetUnit, dmg);
          gainTroopExp(20, '양면 협공');

          if (targetUnit.troops > 0) {
            const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.35);
            applyDamage(u, counterDmg);
          }
        } else {
          // 일반 1:1 돌격 교전
          logBattle(`🗡️ ${u.name} 부대가 ${targetUnit.name}에게 돌격을 감행합니다!`);
          playSound('slash');
          applyDamage(targetUnit, dmg);
          gainTroopExp(15, '돌격 교전');

          if (adv.isAdv) {
            logBattle(adv.text);
            playSound('fanfare');
          } else if (adv.isDisadv) {
            logBattle(adv.text);
          }

          if (targetUnit.troops > 0) {
            const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.65);
            applyDamage(u, counterDmg);
          }
        }
      } else if (mode === 'archery' && targetUnit) {
        if (isArcher) {
          const archerTitle = u.name.includes('황충') ? '황충 백발백중 신궁' : '태사자 강동맹궁';
          logBattle(`🏹🎯 [${archerTitle} 원거리 저격!] 4칸 밖에서 뿜어진 화살이 ${targetUnit.name} 부대의 심장을 꿰뚫었습니다!`);
          playSound('arrow');
          const dmg = Math.floor(calculateCombatDamage(u, targetUnit, 'archery') * 1.5);
          applyDamage(targetUnit, dmg);
          showDamagePop(targetUnit.q, targetUnit.r, `🎯장거리 저격! -${dmg}`);
          gainTroopExp(25, '원거리 신궁 저격');
        } else {
          logBattle(`🏹 ${u.name} 부대의 화살비가 쏟아집니다! (사거리 4칸)`);
          playSound('arrow');
          const dmg = calculateCombatDamage(u, targetUnit, 'archery');
          applyDamage(targetUnit, dmg);
          gainTroopExp(15, '궁시 지원');
        }
      } else if (mode === 'fire') {
        if (isArcher && targetUnit) {
          // 황충 / 태사자 맹화시 (사거리 4칸 불화살 폭격)
          const archerTitle = u.name.includes('황충') ? '황충 맹화시' : '태사자 불화살';
          logBattle(`🔥🏹 [${archerTitle} 원거리 불화살 폭격!] 4칸 밖에서 날아든 불화살이 ${targetUnit.name} 부대 진영을 덮쳐 화염에 휩싸입니다!`);
          playSound('fire');
          const dmg = Math.floor(calculateCombatDamage(u, targetUnit, 'archery') * 1.7 + 900);
          applyDamage(targetUnit, dmg);
          sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });
          targetUnit.morale = Math.max(10, targetUnit.morale - 35);
          showDamagePop(targetUnit.q, targetUnit.r, `🔥원거리 맹화시! -${dmg}`);
          gainTroopExp(30, '원거리 불화살 폭격 성공');
        } else {
          logBattle(`🔥 [대화계] 불길이 거세게 치솟습니다! 남동풍을 타고 번져갑니다.`);
          playSound('fire');
          sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });
          gainTroopExp(25, '대화계 성공');
          if (targetUnit) {
            applyDamage(targetUnit, 1500);
            targetUnit.morale = Math.max(10, targetUnit.morale - 20);
          }
        }
      } else if (mode === 'chaos' && targetUnit) {
        const successRate = 55 + (u.int - targetUnit.int) * 2;
        if (Math.random() * 100 < successRate) {
          targetUnit.morale = Math.max(10, targetUnit.morale - 30);
          targetUnit.acted = true;
          gainTroopExp(25, '혼란 계략 성공');
          logBattle(`🌀 [혼란 대성공] ${targetUnit.name}의 군심이 무너져 행동 불능이 되었습니다!`);
          playSound('fanfare');
        } else {
          logBattle(`[혼란 실패] ${targetUnit.name}이 계략을 눈치챘습니다.`);
        }
      }

      finishUnitAction(u);
    }
"""

# updateActionCommands 시작부터 calculateCombatDamage 직전까지 치환
pattern_range = r"function updateActionCommands[\s\S]*?function calculateCombatDamage"
match_range = re.search(pattern_range, text)
if match_range:
    text = text[:match_range.start()] + archer_system_code.strip() + "\n\n    function calculateCombatDamage" + text[match_range.end():]
    print("  -> Master Archer duo system successfully injected!")
else:
    print("  -> ERROR: pattern_range not matched!")

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

print("Archer duo and tactics synchronization complete!")
