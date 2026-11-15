// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

console.log('=== [1/6] 전쟁터 화면 초대형 98vw 와이드 & 캔버스 1280x640, HEX_RADIUS 46 확대 ===');

// 1. 모달 창 너비: max-w-6xl -> max-w-[98vw] w-[98vw]
content = content.replace(/max-w-6xl/g, 'max-w-[98vw] w-[98vw]');

// 2. 캔버스 해상도: 1160x590 -> 1280x640
content = content.replace(/width="1160" height="590"/g, 'width="1280" height="640"');
content = content.replace(
  'id="battleCanvas" width="1280" height="640" class="rounded border border-amber-900/80 cursor-pointer max-w-full h-auto bg-[#0a0f1d]"',
  'id="battleCanvas" width="1280" height="640" class="rounded-lg border-2 border-yellow-600/80 cursor-pointer w-full h-auto bg-[#080d1a] shadow-2xl"'
);

// 3. HEX_RADIUS = 46
content = content.replace(/const HEX_RADIUS = \d+;/, 'const HEX_RADIUS = 46;');

// 4. getHexPixel 오프셋 조정
const oldHexPixel = `function getHexPixel(q, r) {
      const x = 58 + q * HEX_W + (r % 2 === 1 ? HEX_W / 2 : 0);
      const y = 48 + r * (HEX_H * 0.75);
      return { x, y };
    }`;
const newHexPixel = `function getHexPixel(q, r) {
      const x = 65 + q * HEX_W + (r % 2 === 1 ? HEX_W / 2 : 0);
      const y = 56 + r * (HEX_H * 0.75);
      return { x, y };
    }`;
if (content.includes(oldHexPixel)) {
  content = content.replace(oldHexPixel, newHexPixel);
}

// 5. 유닛 그래픽 및 아바타 폰트 크기 확대
content = content.replace(/ctx\.arc\(x, y, 22, 0, Math\.PI \* 2\);/g, 'ctx.arc(x, y, 27, 0, Math.PI * 2);');
content = content.replace(/ctx\.font = "18px serif";/g, 'ctx.font = "24px serif";');
content = content.replace(/ctx\.font = "bold 11px sans-serif";\s*ctx\.fillStyle = unit\.isBoss \? "#fef08a" : "#ffffff";\s*ctx\.shadowColor = "#000000";\s*ctx\.shadowBlur = 4;\s*ctx\.fillText\(unit\.name, x, y \+ 14\);/,
  'ctx.font = "bold 13px sans-serif"; ctx.fillStyle = unit.isBoss ? "#fef08a" : "#ffffff"; ctx.shadowColor = "#000000"; ctx.shadowBlur = 5; ctx.fillText(unit.name, x, y + 17);'
);
content = content.replace(/const barW = 34;\s*const barH = 4;\s*ctx\.fillStyle = "#0f172a";\s*ctx\.fillRect\(x - barW \/ 2, y \+ 23, barW, barH\);/,
  'const barW = 46; const barH = 5; ctx.fillStyle = "#0f172a"; ctx.fillRect(x - barW / 2, y + 27, barW, barH);'
);

console.log('=== [2/6] 1달 행동력 시스템: 기본 5회 / 7대 특권 군주(유비, 조조, 손권, 장노, 원소, 원술, 마등) 6회 ===');

const actionSystemCode = `    // ==========================================================================
    // ⭐ 전략 지도 1턴(1달)당 행동 제한 시스템 (기본 5회 / 7대 특권 군주 6회)
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

      const headerBanner = document.getElementById('action-points-banner');
      if (headerBanner) {
        headerBanner.innerHTML = \`
          <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
            <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
            <span class="text-sm font-black text-yellow-300 tracking-wider">\${stars} (\${pts}/\${maxPts})</span>
          </div>
        \`;
      }

      const panelBanner = document.querySelector('#action-points-banner span.tracking-wider');
      if (panelBanner) {
        panelBanner.innerText = \`\${stars} (\${pts}/\${maxPts})\`;
      }
    }`;

// 행동력 함수 블록 교체
const actionBlockRegex = /\/\/ ==========================================================================\s*\/\/\s*⭐\s*전략 지도 1턴\(1달\)당[\s\S]*?function updateActionPointUI\(\) \{[\s\S]*?\n    \}/;
content = content.replace(actionBlockRegex, actionSystemCode);

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
  }
}

console.log('=== [3/6] 적군 시작 레벨: 여포 Lv.30, 조조 Lv.20, 손권 Lv.40 & 군량고 2부대 철통사수 ===');

const newPosConfig = `const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'boss' },               // 👑 적 총대장 (여포 Lv.30, 손권 Lv.40, 조조 Lv.20)
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },            // ⚔️ 적 본대 돌격장수
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },           // 🐎 아군 군량고 우회 기습대
        { q: 11, r: 3, form: 'bangwon', role: 'guard_depot_1' },    // 🛡️ 적 군량고 제1 철통사수대 (절대사수!)
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot_2' }     // 🛡️ 적 군량고 제2 철통사수대 (절대사수!)
      ];`;
content = content.replace(/const enemyPositions = \[\s*\{[\s\S]*?\];/, newPosConfig);

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

        const dynamicEnemySoldiers = Math.min(12000, Math.max(4000, enemySoldierPerUnit + (scaledLvl - 1) * 200));
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
          role: posCfg.role,
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
content = content.replace(/const enemyUnits = enemyPositions\.map\(\(posCfg, idx\) => \{[\s\S]*?return \{[\s\S]*?acted: false\s*\}\;\s*\}\)\;/, newEnemyGenComplete);

// 군량고 2부대 AI 철통사수
const newAiDepotGuard = `// 🛡️ 1. 적 군량창고 2부대 무조건 철통 사수 시스템 (절대 이탈 금지!)
          if (enemy.role === 'guard_depot_1' || enemy.role === 'guard_depot_2' || enemy.role === 'guard_depot') {
            let depotQ = 12, depotR = 4;
            for (let r = 0; r < GRID_ROWS; r++) {
              for (let q = 0; q < GRID_COLS; q++) {
                if (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] === 4) {
                  depotQ = q; depotR = r;
                }
              }
            }

            const intruders = allies.filter(a => getHexDistance(a.q, a.r, depotQ, depotR) <= 2.5);
            enemy.formation = 'bangwon';

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
              logBattle(\`🌾🛡️ \${enemy.name} 부대가 적 군량고 바로 앞을 철통 방원진으로 결사 사수하고 있습니다.\`);
            }
          }
          // 🐎 2. 아군 군량고 우회 기습부대`;
content = content.replace(/\/\/ 🛡️ 1\. 군량고 철통 수비대장[\s\S]*?\/\/ 🐎 2\. 아군 군량고 우회 기습부대/, newAiDepotGuard);

console.log('=== [4/6] 전쟁 난이도 상향: 적 레벨 공격력/방어력 동등 배율 & 1:1 출혈 강화 ===');

const newDmgLvl = `// 🔥 [쌍방 병종 숙련도 레벨 보정: 적군도 대등하게 강해짐!]
      const atkLvl = attacker.level || (attacker.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      atkPower *= (1.0 + (atkLvl - 1) * 0.055);

      const defLvl = defender.level || (defender.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      defPower *= (1.0 + (defLvl - 1) * 0.05);

      const elemAdv = getElementAdvantage(attacker.element, defender.element);
      diffMult *= elemAdv.mult;`;
content = content.replace(/\/\/ 아군 병종 숙련도 레벨 보정[\s\S]*?diffMult \*= elemAdv\.mult;/, newDmgLvl);

console.log('=== [5/6] 적 군벌들도 매달 훈련 및 전쟁 준비 수행 ===');

const newExecuteRest = `function executeRest() {
      closeAllPopups();
      playSfx('rest');

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
      document.getElementById('currentDate').innerText = \`\${gameState.year}년 \${gameState.month}월 (\${season})\`;

      // ⚔️🔥 [적장들도 매달 훈련 및 전쟁 준비 수행!]
      const enemyProvinces = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      if (enemyProvinces.length > 0) {
        const sampled = enemyProvinces.sort(() => 0.5 - Math.random()).slice(0, 3);
        sampled.forEach(prov => {
          const addSoldiers = 600 + Math.floor(Math.random() * 900);
          prov.soldiers = Math.min(60000, prov.soldiers + addSoldiers);
          prov.defense = Math.min(100, (prov.defense || 50) + 2);
        });

        const chiefProv = sampled[0];
        logMessage(\`⚔️ [적 군벌 동향] \${chiefProv.ruler}군(\${chiefProv.name})이 전군 특별 훈련 및 성벽 보수를 실시하여 전쟁 준비를 마쳤습니다! (병력 증원)\`, 'text-red-400 font-bold');

        // 🔥 [적 침공 이벤트 트리거: 18% 확률로 아군 영지 침공!]
        if (Math.random() < 0.22) {
          setTimeout(() => {
            triggerEnemyInvasion(chiefProv);
          }, 600);
        }
      }

      if ([1, 4, 7, 10].includes(gameState.month)) {
        collectQuarterlyTaxes();
      }

      const myProv = getMyCapital();
      if (myProv) {
        myProv.pop = Math.min(500000, myProv.pop + 300);
      }

      renderMapPins();
      updateRightPanel();
    }`;
content = content.replace(/function executeRest\(\) \{[\s\S]*?renderMapPins\(\);\s*\}/, newExecuteRest);

console.log('=== [6/6] 적 침공 시 일기토 or 영지 방어전 선택 & 전쟁 패배 시 게임오버(GameOver) 연출 ===');

// 1. GameOver 모달 및 적 침공 모달 HTML 주입
const invasionAndGameOverModalsHtml = `
  <!-- 🚨 적군 침공 긴급 경보 모달 (일기토 vs 10턴 방어 결전 선택) -->
  <div id="enemy-invasion-modal" class="fixed inset-0 modal-backdrop z-[99999] hidden flex items-center justify-center p-3 bg-black/85">
    <div class="koei-box w-full max-w-lg p-5 rounded-lg shadow-2xl border-4 border-red-600 bg-slate-950 text-white flex flex-col gap-4 animate-bounce-once">
      <div class="border-b-2 border-red-700 pb-2 flex items-center justify-between">
        <span class="text-lg font-black text-red-400 flex items-center gap-2">
          <span>🚨</span> <span>[긴급 경보] 적군 대군 침공!</span>
        </span>
        <span class="text-xs bg-red-900 text-red-200 px-2 py-0.5 rounded font-bold">생사 결단</span>
      </div>

      <div class="bg-red-950/60 p-3 rounded border border-red-800/80 text-sm leading-relaxed" id="enemyInvasionDesc">
        적 대군이 아군 영지로 쇄도하고 있습니다!
      </div>

      <div class="text-xs text-yellow-300 font-bold px-1">
        💡 군주의 결단을 내리십시오! 일기토로 적장을 베어 패주시킬 것인가, 10턴 헥스 방어전으로 맞설 것인가?
        <span class="text-red-400 block mt-1">※ 패배 시 즉시 참형되어 천하통일의 대업이 영원히 종결됩니다!</span>
      </div>

      <div class="grid grid-cols-2 gap-3 mt-1">
        <button onclick="resolveInvasionByDuel()" class="p-3 rounded bg-gradient-to-r from-red-700 to-amber-600 hover:from-red-600 hover:to-amber-500 border-2 border-yellow-300 text-white font-black text-sm shadow-xl flex flex-col items-center gap-1 transition transform hover:scale-[1.02]">
          <span class="text-xl">⚔️</span>
          <span>운명의 1:1 일기토</span>
          <span class="text-[10px] text-yellow-200 font-normal">승리 시 즉시 격퇴! (패배 시 참형)</span>
        </button>

        <button onclick="resolveInvasionByHexBattle()" class="p-3 rounded bg-gradient-to-r from-blue-800 to-indigo-700 hover:from-blue-700 hover:to-indigo-600 border-2 border-cyan-400 text-white font-black text-sm shadow-xl flex flex-col items-center gap-1 transition transform hover:scale-[1.02]">
          <span class="text-xl">🛡️</span>
          <span>10턴 헥스 영지 방어전</span>
          <span class="text-[10px] text-cyan-200 font-normal">성벽 사수 결전! (패배 시 멸망)</span>
        </button>
      </div>
    </div>
  </div>

  <!-- 💀 게임오버 (대업 종결 - 군주 처형 및 영지 멸망 엔딩 모달) -->
  <div id="game-over-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex items-center justify-center p-3 bg-black/95">
    <div class="koei-box w-full max-w-xl p-6 rounded-xl shadow-2xl border-4 border-red-700 bg-slate-950 text-white flex flex-col gap-4 text-center">
      <div class="text-5xl animate-pulse">💀</div>
      <h2 class="text-2xl font-black text-red-500 tracking-wider text-pixel">
        [천하통일 대업 좌절 - 패업 종결]
      </h2>
      <div id="gameOverReason" class="bg-red-950/70 p-4 rounded-lg border-2 border-red-800 text-slate-200 text-sm leading-relaxed text-left">
        전쟁에서 통한의 패배를 당하여 군주가 포로로 붙잡혀 참형되었습니다...
      </div>
      <p class="text-xs text-slate-400">
        푸른 하늘 아래 맺었던 도원결의의 맹세도, 한실 부흥의 웅대한 뜻도 여기서 끝이 났습니다...
      </p>
      <div class="pt-2">
        <button onclick="location.reload()" class="px-8 py-3 rounded-lg bg-gradient-to-r from-red-800 via-amber-700 to-red-800 hover:from-red-700 hover:to-amber-600 border-2 border-yellow-400 text-yellow-200 font-black text-base shadow-2xl transition transform hover:scale-105">
          🔄 처음부터 다시 도전 (새 게임 시작)
        </button>
      </div>
    </div>
  </div>
`;

if (!content.includes('id="enemy-invasion-modal"')) {
  content = content.replace('</body>', invasionAndGameOverModalsHtml + '\n</body>');
  console.log('Injected enemy-invasion-modal and game-over-modal HTML.');
}

// 2. 적 침공 이벤트 & 일기토/방어전 & GameOver 함수들 주입
const invasionAndGameOverJs = `
    // ==========================================================================
    // 🚨 적 침공 이벤트 & 일기토 vs 10턴 방어 결전 & 패배 시 게임오버 시스템
    // ==========================================================================
    let currentInvasionContext = null;

    function triggerEnemyInvasion(enemyProv) {
      if (sam5BattleState.battleOver === false && sam5BattleState.turn > 1) return; // 이미 전쟁 중이면 패스
      const myCapital = getMyCapital();
      if (!myCapital) return;

      currentInvasionContext = {
        enemyProv: enemyProv,
        targetProv: myCapital,
        enemyLeader: enemyProv.leader || enemyProv.ruler,
        soldiers: enemyProv.soldiers || 25000
      };

      const desc = document.getElementById("enemyInvasionDesc");
      if (desc) {
        desc.innerHTML = \`
          <div class="font-black text-red-300 text-base mb-1">
            🚨 \${enemyProv.ruler}군의 맹장 [\${currentInvasionContext.enemyLeader}] 장군이 병력 \${currentInvasionContext.soldiers.toLocaleString()}명을 이끌고 아군 영지 [\${myCapital.name}]으로 침공해 왔습니다!
          </div>
          <div class="text-xs text-slate-300">
            영지가 함락될 위기입니다! 1:1 일기토를 신청하여 적장을 일격에 베어 넘기거나, 전군을 집결시켜 10턴 헥스 영지 방어전에 돌입하십시오!
          </div>
        \`;
      }
      openModal('enemy-invasion-modal');
      playSfx('warning');
      logMessage(\`🚨 [적군 침공 경보!] \${enemyProv.ruler}군이 아군 본거지 \${myCapital.name}으로 침공했습니다!\`, 'text-red-400 font-black');
    }

    // 선택 1: 일기토로 침공 해결
    function resolveInvasionByDuel() {
      closeModal('enemy-invasion-modal');
      if (!currentInvasionContext) return;

      // 아군 맹장 관우/장비/조운 중 1명 선택
      const allyDuelist = MY_OFFICERS.find(o => o.id === 'guan_yu') || MY_OFFICERS[0];
      const enemyDuelist = {
        name: currentInvasionContext.enemyLeader,
        war: 92,
        avatar: '👹',
        title: '적 침공 총대장'
      };

      logMessage(\`⚔️ [운명의 일기토!] \${allyDuelist.name}(무력 \${allyDuelist.war}) 장군이 적장 \${enemyDuelist.name}(무력 \${enemyDuelist.war})과 생사를 건 결투에 돌입합니다!\`, 'text-yellow-300 font-black');

      // 일기토 모달 오픈
      sam5DuelState.p1 = allyDuelist;
      sam5DuelState.p2 = enemyDuelist;
      sam5DuelState.p1Hp = 100;
      sam5DuelState.p2Hp = 100;
      sam5DuelState.round = 1;
      sam5DuelState.isInvasionDuel = true; // 침공 결전 플래그

      document.getElementById("duelP1Name").innerText = allyDuelist.name;
      document.getElementById("duelP1War").innerText = \`무력 \${allyDuelist.war}\`;
      document.getElementById("duelP1Avatar").innerText = allyDuelist.icon || '🐉';
      document.getElementById("duelP1Hp").style.width = "100%";

      document.getElementById("duelP2Name").innerText = enemyDuelist.name;
      document.getElementById("duelP2War").innerText = \`무력 \${enemyDuelist.war}\`;
      document.getElementById("duelP2Avatar").innerText = enemyDuelist.avatar;
      document.getElementById("duelP2Hp").style.width = "100%";

      document.getElementById("duelLog").innerHTML = \`<p class="text-yellow-300 font-black">🚨 [영지의 운명이 걸린 일기토!] 패배 시 즉시 참형되어 게임이 끝납니다!</p>\`;
      document.getElementById("btnDuelRound").classList.remove("hidden");
      document.getElementById("btnDuelClose").classList.add("hidden");

      openModal("duelModal");
    }

    // 선택 2: 10턴 헥스 영지 방어전 돌입
    function resolveInvasionByHexBattle() {
      closeModal('enemy-invasion-modal');
      if (!currentInvasionContext) return;
      openHexBattle(currentInvasionContext.enemyProv, currentInvasionContext.targetProv);
    }

    // 💀 게임오버 모달 발동기 (전쟁 패배 시 게임 종료!)
    function triggerGameOver(reasonText) {
      closeAllPopups();
      sam5BattleState.battleOver = true;
      playSound('fire');

      const reasonBox = document.getElementById("gameOverReason");
      if (reasonBox) {
        reasonBox.innerHTML = \`
          <div class="text-red-400 font-black text-base mb-1">
            💥 통한의 패전 - \${reasonText}
          </div>
          <div class="text-xs text-slate-300 leading-relaxed">
            군주 \${gameState.rulerName}의 군세가 전멸하여 본거지가 함락되었고, 붙잡힌 군주는 적군 총사령관에 의해 형장의 이슬로 사라졌습니다.<br><br>
            이로써 난세를 평정하고 한실을 부흥시키려던 삼국 통일의 대업은 영원히 역사 속으로 사라졌습니다...
          </div>
        \`;
      }
      openModal('game-over-modal');
      logMessage(\`💀 [게임오버] \${reasonText} 천하통일의 대업이 종결되었습니다.\`, 'text-red-500 font-black');
    }
`;

// triggerDefeat 전면 수정: 패배 시 즉시 triggerGameOver 호출!
const oldTriggerDefeatRegex = /function triggerDefeat\(msg\) \{[\s\S]*?closeHexBattle\(false\);\s*\}/;
const newTriggerDefeat = `function triggerDefeat(msg) {
      if (sam5BattleState.battleOver) return;
      sam5BattleState.battleOver = true;
      playSound('fire');
      logBattle(\`통한의 패배: \${msg}\`);
      
      // 💀 사용자의 엄격한 룰: 전쟁에서 지면 즉시 게임오버!
      setTimeout(() => {
        closeModal('hex-battle-modal');
        triggerGameOver(\`전투 패배: \${msg}\`);
      }, 700);
    }`;

content = content.replace(oldTriggerDefeatRegex, newTriggerDefeat);

// 일기토 패배 시 GameOver 연동
const oldDuelRoundRegex = /function progressDuelRound\(\) \{[\s\S]*?function closeDuelModal/;
let duelCode = content.match(oldDuelRoundRegex);
if (duelCode && duelCode[0]) {
  let updatedDuel = duelCode[0].replace(
    'if (sam5DuelState.p1Hp <= 0) {',
    `if (sam5DuelState.p1Hp <= 0) {
        if (sam5DuelState.isInvasionDuel) {
          setTimeout(() => {
            closeModal('duelModal');
            triggerGameOver('침공 방어 일기토에서 패배하여 아군 총대장이 전사했습니다!');
          }, 1000);
          return;
        }`
  );
  content = content.replace(duelCode[0], updatedDuel);
  console.log('Connected invasion duel defeat to GameOver.');
}

// 스크립트 끝부분에 invasionAndGameOverJs 주입
content = content.replace('function triggerVictory(', invasionAndGameOverJs + '\n    function triggerVictory(');

fs.writeFileSync(file, content, 'utf8');
console.log('ALL MASTERPIECE UPDATES SUCCESSFULLY WRITTEN!');
