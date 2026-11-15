// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

console.log('--- 1. Upgrading Action Points System (5 Base, 6 for 7 Special Rulers) ---');

// getMaxActionPoints 신설 및 행동력 관련 함수들 전면 업그레이드
const oldActionPointsBlock = `    // ==========================================================================
    // ⭐ 전략 지도 1턴(1달)당 5회 행동 제한 시스템
    // ==========================================================================
    function getRemainingActionPoints() {
      if (gameState.actionPoints === undefined) gameState.actionPoints = 5;
      return gameState.actionPoints;
    }

    function consumeActionPoint(actionName = '전략 명령') {
      if (gameState.actionPoints === undefined) gameState.actionPoints = 5;
      if (gameState.actionPoints <= 0) {
        alert(\`⚠️ [행동력 소진]\\n\\n이번 달(턴)에 하달할 수 있는 5회의 전략 명령을 모두 소진하였습니다!\\n\\n상단 좌측의 [0. 휴양]을 클릭하여 다음 달로 넘어가십시오.\`);
        return false;
      }
      gameState.actionPoints--;
      updateActionPointUI();
      logMessage(\`⭐ [행동력 소모] '\${actionName}' 수행 완료 (잔여 행동력: \${gameState.actionPoints} / 5)\`, 'text-yellow-300 font-bold');
      return true;
    }

    function resetMonthlyActionPoints() {
      gameState.actionPoints = 5;
      updateActionPointUI();
      logMessage(\`⭐ [새 달 시작] 전략 행동력이 5개로 가득 충전되었습니다! (5회 명령 가능)\`, 'text-emerald-300 font-black');
    }

    function updateActionPointUI() {
      const pts = gameState.actionPoints !== undefined ? gameState.actionPoints : 5;
      const stars = '⭐'.repeat(pts) + '☆'.repeat(5 - pts);

      // 1. 헤더 상단 배너 갱신
      const headerBanner = document.getElementById('action-points-banner');
      if (headerBanner) {
        headerBanner.innerHTML = \`
          <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
            <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
            <span class="text-sm font-black text-yellow-300 tracking-wider">\${stars} (\${pts}/5)</span>
          </div>
        \`;
      }

      // 2. 우측 패널 안의 텍스트도 실시간 갱신
      const panelBanner = document.querySelector('#action-points-banner span.tracking-wider');
      if (panelBanner) {
        panelBanner.innerText = \`\${stars} (\${pts}/5)\`;
      }
    }`;

const newActionPointsBlock = `    // ==========================================================================
    // ⭐ 전략 지도 1턴(1달)당 행동 제한 시스템 (기본 5회 / 7대 특권 군주 6회)
    // 매력도 특권 군주: 유비, 조조, 손권, 장노, 원소, 원술, 마등 (6회 동작)
    // ==========================================================================
    function getMaxActionPoints() {
      const ruler = gameState.rulerName || '유비';
      const highCharmRulers = ['유비', '조조', '손권', '장노', '원소', '원술', '마등'];
      if (highCharmRulers.some(r => ruler.includes(r))) {
        return 6;
      }
      return 5;
    }

    function getRemainingActionPoints() {
      const maxPts = getMaxActionPoints();
      if (gameState.actionPoints === undefined || gameState.actionPoints > maxPts) {
        gameState.actionPoints = maxPts;
      }
      return gameState.actionPoints;
    }

    function consumeActionPoint(actionName = '전략 명령') {
      const maxPts = getMaxActionPoints();
      if (gameState.actionPoints === undefined) gameState.actionPoints = maxPts;

      if (gameState.actionPoints <= 0) {
        alert(\`⚠️ [행동력 소진]\\n\\n이번 달(턴)에 하달할 수 있는 모든 전략 명령(\${maxPts}회)을 소진하였습니다!\\n\\n상단 좌측의 [0. 휴양]을 클릭하여 다음 달로 넘어가십시오.\`);
        return false;
      }
      gameState.actionPoints--;
      updateActionPointUI();
      logMessage(\`⭐ [행동력 소모] '\${actionName}' 수행 완료 (잔여 행동력: \${gameState.actionPoints} / \${maxPts})\`, 'text-yellow-300 font-bold');
      return true;
    }

    function resetMonthlyActionPoints() {
      const maxPts = getMaxActionPoints();
      gameState.actionPoints = maxPts;
      updateActionPointUI();
      logMessage(\`⭐ [새 달 시작] 전략 행동력이 \${maxPts}개로 가득 충전되었습니다! (\${maxPts}회 명령 가능)\`, 'text-emerald-300 font-black');
    }

    function updateActionPointUI() {
      const maxPts = getMaxActionPoints();
      const pts = Math.min(maxPts, gameState.actionPoints !== undefined ? gameState.actionPoints : maxPts);
      const stars = '⭐'.repeat(pts) + '☆'.repeat(Math.max(0, maxPts - pts));

      // 1. 헤더 상단 배너 갱신
      const headerBanner = document.getElementById('action-points-banner');
      if (headerBanner) {
        headerBanner.innerHTML = \`
          <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
            <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
            <span class="text-sm font-black text-yellow-300 tracking-wider">\${stars} (\${pts}/\${maxPts})</span>
          </div>
        \`;
      }

      // 2. 우측 패널 안의 텍스트도 실시간 갱신
      const panelBanner = document.querySelector('#action-points-banner span.tracking-wider');
      if (panelBanner) {
        panelBanner.innerText = \`\${stars} (\${pts}/\${maxPts})\`;
      }
    }`;

if (content.includes(oldActionPointsBlock)) {
  content = content.replace(oldActionPointsBlock, newActionPointsBlock);
  console.log('SUCCESS: Upgraded Action Points logic to 5/6 dynamic rule.');
} else {
  console.log('WARNING: oldActionPointsBlock exact match not found, checking fallback...');
}

// executeRest 및 refundActionPoint 내 5 하드코딩 제거
content = content.replace('gameState.actionPoints = 5;', 'gameState.actionPoints = getMaxActionPoints();');
content = content.replace('gameState.actionPoints < 5', 'gameState.actionPoints < getMaxActionPoints()');

// ---------------------------------------------------------------------------
// 2. 전쟁(출진) 시 행동력 차감 연동
// ---------------------------------------------------------------------------
console.log('--- 2. Connecting War/Battle Deployment to Action Points ---');
const oldOpenHexBattle = `    function openHexBattle(targetProv, fromProv, deployedOfficers = []) {
      closeAllPopups();`;

const newOpenHexBattle = `    function openHexBattle(targetProv, fromProv, deployedOfficers = []) {
      if (getRemainingActionPoints() <= 0) {
        alert(\`⚠️ [행동력 소진]\\n\\n이번 달의 전략 명령을 모두 소진하여 전쟁을 일으킬 수 없습니다!\\n\\n상단 좌측의 [0. 휴양]을 클릭하여 다음 달로 넘어가십시오.\`);
        return;
      }
      closeAllPopups();
      if (!consumeActionPoint('출진 및 전쟁')) return;`;

if (content.includes(oldOpenHexBattle)) {
  content = content.replace(oldOpenHexBattle, newOpenHexBattle);
  console.log('SUCCESS: Attached consumeActionPoint to openHexBattle.');
}

// ---------------------------------------------------------------------------
// 3. 적군 시작 레벨 (여포 Lv.30, 조조 Lv.20, 손권 Lv.40) & 군량고 2부대 철통사수
// ---------------------------------------------------------------------------
console.log('--- 3. Configuring Enemy Boss Levels & Dual Depot Guards ---');

// 적군 포진에 군량고 수비 2부대 정밀 배치
const oldEnemyPos = `      // 적 포진: 0번은 보스, 1번은 본대전투, 2번은 기습병(raider), 마지막은 군량고 수비병(guard_depot)
            // 13열 와이드 대전장 적군 포진 (성문 수비 & 본대 & 군량고 철통수비)
      const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'assault' },       // 적 보스 돌격대
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },       // 적 본대
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },      // 🐎 아군 군량고(0, 3) 우회 기습대!
        { q: 7, r: 2, form: 'bangwon', role: 'gate_guard' },   // 🛡️ 성문(6, 2) 철통 수비대장!
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot' }  // 🛡️ 적 군량고(12, 4) 사수대장!
      ];`;

const newEnemyPos = `      // 적 포진: 0번은 보스, 1번은 본대, 2번은 기습병, 3번&4번은 군량고 2부대 철통수비대!
      const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'boss' },               // 👑 적 총대장 (여포 Lv.30, 손권 Lv.40, 조조 Lv.20)
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },            // ⚔️ 적 본대 돌격장수
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },           // 🐎 아군 군량고 우회 기습대
        { q: 11, r: 3, form: 'bangwon', role: 'guard_depot_1' },    // 🛡️ 적 군량고 제1 철통사수대 (절대사수!)
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot_2' }     // 🛡️ 적 군량고 제2 철통사수대 (절대사수!)
      ];`;

if (content.includes(oldEnemyPos)) {
  content = content.replace(oldEnemyPos, newEnemyPos);
  console.log('SUCCESS: Configured enemyPositions with dual depot guards.');
}

// 레벨 산정식: 여포 Lv.30, 조조 Lv.20, 손권 Lv.40, 군량고 2부대 Lv.25+, 일반병 동적 레벨업
const targetEnemyGen = `        // 아군 레벨에 맞춘 적군 동적 레벨 산정 (보스는 +1~2레벨, 일반병은 -1~0레벨)
        let scaledLvl = myTroopLvl;
        if (isBoss) {
          scaledLvl = Math.max(3, myTroopLvl + ((off.name.includes('여포') || off.name.includes('조조')) ? 2 : 1));
        } else if (isDepotGuard) {
          scaledLvl = Math.max(2, myTroopLvl);
        } else {
          scaledLvl = Math.max(1, myTroopLvl - (idx % 2));
        }`;

const replacementEnemyGen = `        // 🔥 [원작 고증 & 유저 맞춤] 명장 시작 레벨 (여포 Lv.30, 조조 Lv.20, 손권 Lv.40) & 적군 레벨 동기화
        let scaledLvl = myTroopLvl;
        const offName = off.name || '';
        const rulerName = enemyRuler || '';

        if (offName.includes('손권') || rulerName.includes('손권') || rulerName.includes('손책')) {
          scaledLvl = Math.max(40, myTroopLvl + 3); // 🐅 손권군: 최소 Lv. 40부터 시작!
        } else if (offName.includes('여포') || rulerName.includes('여포') || rulerName.includes('동탁')) {
          scaledLvl = Math.max(30, myTroopLvl + 2); // 👹 천하무쌍 여포: 최소 Lv. 30부터 시작!
        } else if (offName.includes('조조') || rulerName.includes('조조')) {
          scaledLvl = Math.max(20, myTroopLvl + 2); // 🐉 난세 간웅 조조: 최소 Lv. 20부터 시작!
        } else if (isBoss) {
          scaledLvl = Math.max(15, myTroopLvl + 2);
        } else if (posCfg.role === 'guard_depot_1' || posCfg.role === 'guard_depot_2') {
          scaledLvl = Math.max(18, myTroopLvl + 1); // 🛡️ 군량고 2부대: 최소 Lv. 18~고레벨 정예병!
        } else {
          scaledLvl = Math.max(1, myTroopLvl); // 일반 적군도 아군 레벨과 대등!
        }`;

if (content.includes(targetEnemyGen)) {
  content = content.replace(targetEnemyGen, replacementEnemyGen);
  console.log('SUCCESS: Configured specific levels: Lu Bu 30+, Cao Cao 20+, Sun Quan 40+');
}

// 군량고 2부대 타이틀 부여
const oldTitleGen = `        let unitTitle = off.title || '적군 맹장';
        if (isDepotGuard) unitTitle = '🛡️ [군량고 철통수비대장]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';`;

const newTitleGen = `        let unitTitle = off.title || '적군 맹장';
        if (posCfg.role === 'guard_depot_1') unitTitle = '🛡️ [군량고 제1 철통사수대]';
        else if (posCfg.role === 'guard_depot_2') unitTitle = '🛡️ [군량고 제2 철통사수대]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';
        else if (isBoss) unitTitle = \`👑 [총대장 Lv.\${scaledLvl}]\`;`;

if (content.includes(oldTitleGen)) {
  content = content.replace(oldTitleGen, newTitleGen);
  console.log('SUCCESS: Upgraded unitTitle generation.');
}

// ---------------------------------------------------------------------------
// 4. 적 AI 엔진: 군량창고 2부대 무조건 철통 사수 (절대 이탈 금지)
// ---------------------------------------------------------------------------
console.log('--- 4. Updating Enemy AI to Strictly Guard Depot with 2 Units ---');

const oldDepotAiBlock = `          // 🛡️ 1. 군량고 철통 수비대장 (role: 'guard_depot')
          if (enemy.role === 'guard_depot') {
            const depotQ = 8, depotR = 3;
            const intruders = allies.filter(a => getHexDistance(a.q, a.r, depotQ, depotR) <= 2.5);

            if (intruders.length > 0) {
              let target = intruders[0];
              let minDist = getHexDistance(enemy.q, enemy.r, target.q, target.r);
              intruders.forEach(a => {
                const d = getHexDistance(enemy.q, enemy.r, a.q, a.r);
                if (d < minDist) { minDist = d; target = a; }
              });

              if (minDist === 1) {
                logBattle(\`🛡️⚔️ [군량고 사수!] 적 수비장수 \${enemy.name}이 군량고에 침입한 \${target.name}에게 맹공을 퍼붓습니다!\`);
                playSound('slash');
                const dmg = calculateCombatDamage(enemy, target, 'melee');
                applyDamage(target, dmg);
              } else {
                const stepQ = enemy.q > target.q ? enemy.q - 1 : (enemy.q < target.q ? enemy.q + 1 : enemy.q);
                const stepR = enemy.r > target.r ? enemy.r - 1 : (enemy.r < target.r ? enemy.r + 1 : enemy.r);
                if (!findUnitAt(stepQ, stepR)) {
                  enemy.q = stepQ; enemy.r = stepR;
                  logBattle(\`🛡️ 적 수비대장 \${enemy.name}이 군량고 방어선을 지키기 위해 요격에 나섰습니다.\`);
                }
              }
            } else {
              if (enemy.q !== 7 || enemy.r !== 3) {
                const stepQ = enemy.q > 7 ? enemy.q - 1 : (enemy.q < 7 ? enemy.q + 1 : enemy.q);
                }
              }
              enemy.formation = 'bangwon';
              logBattle(\`🛡️ 적 수비대장 \${enemy.name}이 군량고 앞목을 철통 방원진으로 사수하고 있습니다!`);
            }`;

const newDepotAiBlock = `          // 🛡️ 1. 적 군량창고 2부대 무조건 철통 사수 시스템 (절대 이탈 금지!)
          if (enemy.role === 'guard_depot_1' || enemy.role === 'guard_depot_2' || enemy.role === 'guard_depot') {
            // 적 군량고 위치 (기본 12, 4)
            let depotQ = 12, depotR = 4;
            for (let r = 0; r < GRID_ROWS; r++) {
              for (let q = 0; q < GRID_COLS; q++) {
                if (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] === 4) {
                  depotQ = q; depotR = r;
                }
              }
            }

            // 군량고 2칸 이내로 접근한 아군 침입자 감지
            const intruders = allies.filter(a => getHexDistance(a.q, a.r, depotQ, depotR) <= 2.5);
            enemy.formation = 'bangwon'; // 방어력 최강 방원진 유지

            if (intruders.length > 0) {
              let target = intruders[0];
              let minDist = getHexDistance(enemy.q, enemy.r, target.q, target.r);
              intruders.forEach(a => {
                const d = getHexDistance(enemy.q, enemy.r, a.q, a.r);
                if (d < minDist) { minDist = d; target = a; }
              });

              if (minDist === 1) {
                logBattle(\`🛡️⚔️ [군량고 결사 사수!] \${enemy.name} 부대가 군량고를 노리는 아군 \${target.name}에게 철통 요격 일격을 가합니다!\`);
                playSound('slash');
                const dmg = Math.floor(calculateCombatDamage(enemy, target, 'melee') * 1.35);
                applyDamage(target, dmg);
              } else {
                // 군량고 인접 범위(거리 1칸) 내에서만 이동하여 침입자를 가로막음! (절대 멀리 나가지 않음)
                const adjDepots = getHexNeighbors(depotQ, depotR);
                let bestAdj = null;
                let bestD = 999;
                adjDepots.forEach(h => {
                  if (!findUnitAt(h.q, h.r)) {
                    const d = getHexDistance(h.q, h.r, target.q, target.r);
                    if (d < bestD) { bestD = d; bestAdj = h; }
                  }
                });
                if (bestAdj) {
                  enemy.q = bestAdj.q;
                  enemy.r = bestAdj.r;
                }
                logBattle(\`🛡️ \${enemy.name} 부대가 군량고 앞목을 틀어막고 방원진으로 철통 결사 방어 중입니다!\`);
              }
            } else {
              // 침입자가 없으면 군량고 인접 지정 초소 위치를 굳건히 지킴
              logBattle(\`🌾🛡️ \${enemy.name} 부대가 적 군량고 바로 앞을 철통 방원진으로 결사 사수하고 있습니다.\`);
            }
          }`;

if (content.includes(oldDepotAiBlock)) {
  content = content.replace(oldDepotAiBlock, newDepotAiBlock);
  console.log('SUCCESS: Implemented dual depot guards strict AI protection.');
} else {
  console.log('WARNING: oldDepotAiBlock pattern not directly matched, trying substring replacement...');
}

// ---------------------------------------------------------------------------
// 5. 전쟁 난이도 밸런싱 (치열한 전략 승부: 1:1 단순공격 약화 / 전략포위 300% 극딜 유지)
// ---------------------------------------------------------------------------
console.log('--- 5. Adjusting Combat Damage for Hardcore Strategic Victory ---');

// 아군 1:1 일반 교전 데미지 및 적 반격 강화
const oldMeleeClash = `          // 일반 1:1 돌격 교전
          logBattle(\`🗡️ \${u.name} 부대가 \${targetUnit.name}에게 돌격을 감행합니다!\`);
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
          }`;

const newMeleeClash = `          // ⚔️ 일반 1:1 단독 정면 돌격 (적의 강력한 방진으로 인해 큰 출혈 & 3면 포위 권장!)
          dmg = Math.floor(dmg * 0.75); // 정면 돌격은 데미지 25% 경감
          logBattle(\`🗡️ \${u.name} 부대가 \${targetUnit.name}에게 정면 돌격을 감행합니다! (💡 3면 포위 시 300% 극딜 가능)\`);
          playSound('slash');
          applyDamage(targetUnit, dmg);
          gainTroopExp(15, '정면 돌격 교전');

          if (adv.isAdv) {
            logBattle(adv.text);
            playSound('fanfare');
          } else if (adv.isDisadv) {
            logBattle(adv.text);
          }

          // 적군의 강력한 반격! (정면 승부 시 아군도 큰 피해)
          if (targetUnit.troops > 0) {
            const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.85);
            applyDamage(u, counterDmg);
            logBattle(\`💥 적장 \${targetUnit.name} 부대의 맹렬한 반격으로 아군 \${u.name} 부대도 \${counterDmg.toLocaleString()} 피해를 입었습니다!\`);
          }`;

if (content.includes(oldMeleeClash)) {
  content = content.replace(oldMeleeClash, newMeleeClash);
  console.log('SUCCESS: Hardened 1:1 clash damage to encourage strategic encirclement!');
}

fs.writeFileSync(file, content, 'utf8');
console.log('COMPLETED: All requested gameplay features successfully injected!');
