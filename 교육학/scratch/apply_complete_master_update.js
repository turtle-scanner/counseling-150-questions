// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

console.log('=== [1/5] 1달 행동력 시스템: 기본 5회 / 7대 특권 군주(유비,조조,손권,장노,원소,원술,마등) 6회 ===');

const oldActionSection = `    // ==========================================================================
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

const newActionSection = `    // ==========================================================================
    // ⭐ 전략 지도 1턴(1달)당 행동 제한 시스템 (기본 5회 / 7대 특권 군주 6회)
    // 매력도 특권 군주: 유비, 조조, 손권, 장노, 원소, 원술, 마등 (1달에 6회 동작)
    // 그 외 군주: 1달에 반드시 5회만 동작 (전쟁 포함 모든 전략 메뉴)
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

if (content.includes(oldActionSection)) {
  content = content.replace(oldActionSection, newActionSection);
  console.log('Action points section replaced successfully.');
}

// executeRest 및 refundActionPoint 내 고정값 수정
content = content.replace(/gameState\.actionPoints = 5;/g, 'gameState.actionPoints = getMaxActionPoints();');
content = content.replace(/gameState\.actionPoints < 5/g, 'gameState.actionPoints < getMaxActionPoints()');

// 전쟁(출진) 오픈 시 행동력 소모 연동
if (content.includes('function openHexBattle(targetProv, fromProv, deployedOfficers = []) {')) {
  const oldWarOpen = `    function openHexBattle(targetProv, fromProv, deployedOfficers = []) {
      closeAllPopups();`;
  const newWarOpen = `    function openHexBattle(targetProv, fromProv, deployedOfficers = []) {
      if (getRemainingActionPoints() <= 0) {
        alert(\`⚠️ [행동력 소진]\\n\\n이번 달의 전략 명령을 모두 소진하여 전쟁을 일으킬 수 없습니다!\\n\\n상단 좌측의 [0. 휴양]을 클릭하여 다음 달로 넘어가십시오.\`);
        return;
      }
      closeAllPopups();
      if (!consumeActionPoint('출진 및 전쟁')) return;`;
  if (content.includes(oldWarOpen)) {
    content = content.replace(oldWarOpen, newWarOpen);
    console.log('Attached consumeActionPoint to openHexBattle successfully.');
  }
}

console.log('=== [2/5] 적군 포진: 군량창고 2부대 철통사수 & 여포 Lv.30, 조조 Lv.20, 손권 Lv.40 ===');

const oldPosBlock = `      const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'assault' },       // 적 보스 돌격대
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },       // 적 본대
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },      // 🐎 아군 군량고(0, 3) 우회 기습대!
        { q: 7, r: 2, form: 'gate_guard' },   // 🛡️ 성문(6, 2) 철통 수비대장!
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot' }  // 🛡️ 적 군량고(12, 4) 사수대장!
      ];`;

// 더 유연하게 enemyPositions 블록 찾기
const enemyPosRegex = /const enemyPositions = \[\s*\{[\s\S]*?\];/;
const newPosConfig = `const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'boss' },               // 👑 적 총대장 (여포 Lv.30, 손권 Lv.40, 조조 Lv.20)
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },            // ⚔️ 적 본대 돌격장수
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },           // 🐎 아군 군량고 우회 기습대
        { q: 11, r: 3, form: 'bangwon', role: 'guard_depot_1' },    // 🛡️ 적 군량고 제1 철통사수대 (절대사수!)
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot_2' }     // 🛡️ 적 군량고 제2 철통사수대 (절대사수!)
      ];`;

content = content.replace(enemyPosRegex, newPosConfig);
console.log('Updated enemyPositions regex replacement complete.');

// 적군 유닛 생성 맵핑 블록 교체
const enemyGenRegex = /const enemyUnits = enemyPositions\.map\(\(posCfg, idx\) => \{[\s\S]*?return \{[\s\S]*?acted: false\s*\}\;\s*\}\)\;/;

const newEnemyGenComplete = `// 🔥 [원작 고증 & 유저 맞춤] 명장 시작 레벨 (여포 Lv.30, 조조 Lv.20, 손권 Lv.40) & 적군 레벨 동기화
      const myTroopLvl = gameState.troopLevel || 1;

      const enemyUnits = enemyPositions.map((posCfg, idx) => {
        const off = enemyOffList[idx % enemyOffList.length];
        const isBoss = (idx === 0);
        const isRaider = (posCfg.role === 'raider');
        const isDepot1 = (posCfg.role === 'guard_depot_1');
        const isDepot2 = (posCfg.role === 'guard_depot_2');

        const offName = off.name || '';
        const rulerName = enemyRuler || '';

        // 시작 레벨 지정: 여포 Lv.30, 조조 Lv.20, 손권 Lv.40
        let scaledLvl = myTroopLvl;
        if (offName.includes('손권') || rulerName.includes('손권') || rulerName.includes('손책')) {
          scaledLvl = Math.max(40, myTroopLvl + 3); // 🐅 손권군: 최소 Lv. 40부터 시작!
        } else if (offName.includes('여포') || rulerName.includes('여포') || rulerName.includes('동탁')) {
          scaledLvl = Math.max(30, myTroopLvl + 2); // 👹 천하무쌍 여포: 최소 Lv. 30부터 시작!
        } else if (offName.includes('조조') || rulerName.includes('조조')) {
          scaledLvl = Math.max(20, myTroopLvl + 2); // 🐉 난세 간웅 조조: 최소 Lv. 20부터 시작!
        } else if (isBoss) {
          scaledLvl = Math.max(15, myTroopLvl + 2);
        } else if (isDepot1 || isDepot2) {
          scaledLvl = Math.max(18, myTroopLvl + 1); // 🛡️ 군량고 2부대: 최소 Lv. 18~고레벨 정예병!
        } else {
          scaledLvl = Math.max(1, myTroopLvl); // 일반 적군도 아군 레벨과 대등!
        }

        // 레벨에 따른 적군 병종명 부여
        let eTroopName = '보병';
        if (scaledLvl >= 16) eTroopName = isBoss ? '천하무적군' : '호표기/철기병';
        else if (scaledLvl >= 9) eTroopName = '근위 친위대';
        else if (scaledLvl >= 7) eTroopName = '철기병';
        else if (scaledLvl >= 5) eTroopName = '중갑 보병';
        else if (scaledLvl >= 3) eTroopName = '기마병';

        let unitTitle = off.title || '적군 맹장';
        if (isDepot1) unitTitle = '🛡️ [군량고 제1 철통사수대]';
        else if (isDepot2) unitTitle = '🛡️ [군량고 제2 철통사수대]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';
        else if (isBoss) unitTitle = \`👑 [총대장 Lv.\${scaledLvl}]\`;

        // 레벨에 따른 적군 병력 규모 동적 상향 (단단한 병력)
        const dynamicEnemySoldiers = Math.min(12000, Math.max(4000, enemySoldierPerUnit + (scaledLvl - 1) * 200));

        // 레벨에 따른 적장 무력/통솔 보정
        const statBonus = Math.floor((scaledLvl - 1) * 0.4);

        return {
          id: \`enemy_\${idx}\`,
          faction: 'enemy',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: unitTitle,
          avatar: off.icon || ((isDepot1 || isDepot2) ? '🛡️' : '👹'),
          element: off.element || (enemyRuler.includes('손') ? 'water' : (enemyRuler.includes('마') ? 'wind' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? 'fire' : 'earth'))),
          elemIcon: off.elemIcon || (enemyRuler.includes('손') ? '💧' : (enemyRuler.includes('마') ? '🌪️' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? '🔥' : '⛰️'))),
          elemName: off.elemName || '적 부대 속성',
          level: scaledLvl,
          troopName: eTroopName,
          war: Math.min(118, off.war + statBonus),
          int: off.int,
          lead: Math.min(115, (off.lead || 80) + statBonus),
          chr: 70,
          isBoss: isBoss,
          role: posCfg.role, // 'guard_depot_1', 'guard_depot_2', 'raider', 'assault', 'boss'
          troops: dynamicEnemySoldiers,
          maxTroops: dynamicEnemySoldiers,
          morale: 100,
          formation: posCfg.form,
          availableFormations: ['gyorin', 'bongsi', 'bangwon', 'chuhaeng', 'anhaeng'],
          skills: off.war >= 95 ? ['천하무쌍', '돌격', '분기'] : ['돌격', '화계', '혼란'],
          q: posCfg.q,
          r: posCfg.r,
          moved: false,
          acted: false
        };
      });`;

content = content.replace(enemyGenRegex, newEnemyGenComplete);
console.log('Updated enemyUnits generation regex replacement complete.');

console.log('=== [3/5] 적군 지능 강화: 군량창고 2부대 무조건 철통 사수 ===');

const oldAiSectionRegex = /\/\/ 🛡️ 1\. 군량고 철통 수비대장[\s\S]*?\/\/ 🐎 2\. 아군 군량고 우회 기습부대/;

const newAiDepotGuard = `// 🛡️ 1. 적 군량창고 2부대 무조건 철통 사수 시스템 (절대 이탈 금지!)
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
            enemy.formation = 'bangwon'; // 방어력 최강 방원진(방어 1위, 화살 차단) 상시 유지!

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
          }
          // 🐎 2. 아군 군량고 우회 기습부대`;

content = content.replace(oldAiSectionRegex, newAiDepotGuard);
console.log('Updated AI depot guard logic complete.');

console.log('=== [4/5] 전쟁 난이도 상향: 적 공격력/방어력 레벨 동등 적용 & 1:1 출혈 강화 ===');

// calculateCombatDamage 내 쌍방 레벨 보정
const dmgLvlRegex = /\/\/ 아군 병종 숙련도 레벨 보정[\s\S]*?diffMult \*= elemAdv\.mult;/;
const newDmgLvl = `// 🔥 [쌍방 병종 숙련도 레벨 보정: 적군도 대등하게 강해짐!]
      const atkLvl = attacker.level || (attacker.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      atkPower *= (1.0 + (atkLvl - 1) * 0.055);

      // 방어력 레벨 보정: 고레벨 부대는 방어력도 탄탄해져 일격사 방지
      const defLvl = defender.level || (defender.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      defPower *= (1.0 + (defLvl - 1) * 0.05);

      // 🔮 5대 원소 부대 속성 상성 연산 (우세 시 대미지 1.5배, 열세 시 0.7배)
      const elemAdv = getElementAdvantage(attacker.element, defender.element);
      diffMult *= elemAdv.mult;`;

content = content.replace(dmgLvlRegex, newDmgLvl);
console.log('Updated damage scaling complete.');

console.log('=== [5/5] 적장들도 매달 훈련 및 전쟁 준비 수행 (executeRest 내 군벌 AI) ===');

const restRegex = /function executeRest\(\) \{[\s\S]*?renderMapPins\(\);\s*\}/;

const newExecuteRest = `function executeRest() {
      closeAllPopups();
      playSfx('rest');

      // ⭐ 한 달(턴) 넘김 시 전략 행동력 충전 (기본 5개 / 7대 특권 군주 6개)
      const maxPts = getMaxActionPoints();
      gameState.actionPoints = maxPts;
      updateActionPointUI();
      logMessage(\`⭐ [새 달 시작] 전략 행동력이 \${maxPts}개로 완충되었습니다! (\${maxPts}회 명령 가능)\`, 'text-emerald-300 font-black');

      gameState.month++;
      if (gameState.month > 12) {
        gameState.month = 1;
        gameState.year++;
      }
      gameState.rates.riceSell = 90 + Math.floor(Math.random() * 35);
      gameState.rates.riceBuy = 45 + Math.floor(Math.random() * 25);
      gameState.rates.crossbow = 50 + Math.floor(Math.random() * 20);
      gameState.rates.heavyBow = 85 + Math.floor(Math.random() * 25);
      gameState.rates.horse = 40 + Math.floor(Math.random() * 25);

      const seasons = ['봄', '봄', '봄', '여름', '여름', '여름', '가을', '가을', '가을', '겨울', '겨울', '겨울'];
      const season = seasons[gameState.month - 1];
      const seasonEmoji = season === '봄' ? '🌸' : (season === '여름' ? '☀️' : (season === '가을' ? '🍁' : '❄️'));
      document.getElementById('currentDate').innerText = \`\${gameState.year}년 \${gameState.month}월 (\${season})\`;

      // ⚔️🔥 [적장들도 매달 훈련 및 전쟁 준비 수행!]
      const enemyProvinces = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      if (enemyProvinces.length > 0) {
        // 무작위 적 영지 2~3곳에서 훈련 및 전쟁 준비 수행!
        const sampled = enemyProvinces.sort(() => 0.5 - Math.random()).slice(0, 3);
        sampled.forEach(prov => {
          const addSoldiers = 500 + Math.floor(Math.random() * 800);
          prov.soldiers = Math.min(60000, prov.soldiers + addSoldiers);
          prov.defense = Math.min(100, (prov.defense || 50) + 2);
        });

        const chiefProv = sampled[0];
        logMessage(\`⚔️ [적 군벌 동향] \${chiefProv.ruler}군(\${chiefProv.name})이 전군 특별 훈련 및 성벽 보수를 실시하여 전쟁 준비를 마쳤습니다! (병력 +\${500 + Math.floor(Math.random() * 800)}명)\`, 'text-red-400 font-bold');
      }

      // 계절 수입
      if ([1, 4, 7, 10].includes(gameState.month)) {
        collectQuarterlyTaxes();
      }

      // 내정 자연 증감
      const myProv = getMyCapital();
      if (myProv) {
        myProv.pop = Math.min(500000, myProv.pop + 300);
      }

      renderMapPins();
      updateRightPanel();
    }`;

content = content.replace(restRegex, newExecuteRest);
console.log('Updated executeRest with active enemy warlord preparations.');

fs.writeFileSync(file, content, 'utf8');
console.log('ALL UPDATES WRITTEN TO DESKTOP HTML SUCCESSFULLY!');
