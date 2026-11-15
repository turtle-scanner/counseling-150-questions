// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

// ---------------------------------------------------------------------------
// 1. initHexBattleUnits 내 적군 레벨 동적 스케일링 (아군 레벨에 완벽 동기화)
// ---------------------------------------------------------------------------
const oldEnemyGenStart = `      const enemyUnits = enemyPositions.map((posCfg, idx) => {
        const off = enemyOffList[idx % enemyOffList.length];
        const isDepotGuard = (posCfg.role === 'guard_depot');
        const isRaider = (posCfg.role === 'raider');
        const isBoss = (idx === 0);

        let unitTitle = off.title || '적군 맹장';
        if (isDepotGuard) unitTitle = '🛡️ [군량고 철통수비대장]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';

        const offLvl = (off.name.includes('여포') || off.name.includes('손책')) ? 10 : (off.level || (isBoss ? 5 : 2));`;

const newEnemyGenStart = `      // 🔥 [적군 레벨 동적 스케일링 엔진] 아군 레벨에 맞춰 적군도 호적수로 함께 동적 성장!
      const myTroopLvl = gameState.troopLevel || 1;

      const enemyUnits = enemyPositions.map((posCfg, idx) => {
        const off = enemyOffList[idx % enemyOffList.length];
        const isDepotGuard = (posCfg.role === 'guard_depot');
        const isRaider = (posCfg.role === 'raider');
        const isBoss = (idx === 0);

        let unitTitle = off.title || '적군 맹장';
        if (isDepotGuard) unitTitle = '🛡️ [군량고 철통수비대장]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';

        // 아군 레벨에 맞춘 적군 동적 레벨 산정 (보스는 +1~2레벨, 일반병은 -1~0레벨)
        let scaledLvl = myTroopLvl;
        if (isBoss) {
          scaledLvl = Math.max(3, myTroopLvl + ((off.name.includes('여포') || off.name.includes('조조')) ? 2 : 1));
        } else if (isDepotGuard) {
          scaledLvl = Math.max(2, myTroopLvl);
        } else {
          scaledLvl = Math.max(1, myTroopLvl - (idx % 2));
        }

        // 레벨에 따른 적군 병종명 부여
        let eTroopName = '보병';
        if (scaledLvl >= 16) eTroopName = isBoss ? '천하무적군' : '호표기/철기병';
        else if (scaledLvl >= 9) eTroopName = '근위 친위대';
        else if (scaledLvl >= 7) eTroopName = '철기병';
        else if (scaledLvl >= 5) eTroopName = '중갑 보병';
        else if (scaledLvl >= 3) eTroopName = '기마병';

        // 레벨에 따른 적군 병력 규모 동적 상향
        const dynamicEnemySoldiers = Math.min(12000, Math.max(3500, enemySoldierPerUnit + (scaledLvl - 1) * 220));

        // 레벨에 따른 적장 능력치 미세 보정 (긴장감 넘치는 공방)
        const statBonus = Math.floor((scaledLvl - 1) * 0.4);`;

if (content.includes(oldEnemyGenStart)) {
  content = content.replace(oldEnemyGenStart, newEnemyGenStart);
  console.log('SUCCESS: Patched enemy level scaling in initHexBattleUnits');
} else {
  console.error('FAILED to find oldEnemyGenStart');
}

// return 블록 내 level, troops, troopName 매핑 갱신
const oldReturnBlock = `        return {
          id: \`enemy_\${idx}\`,
          faction: 'enemy',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: unitTitle,
          avatar: off.icon || (isDepotGuard ? '🛡️' : '👹'),
          element: off.element || (enemyRuler.includes('손') ? 'water' : (enemyRuler.includes('마') ? 'wind' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? 'fire' : 'earth'))),
          elemIcon: off.elemIcon || (enemyRuler.includes('손') ? '💧' : (enemyRuler.includes('마') ? '🌪️' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? '🔥' : '⛰️'))),
          elemName: off.elemName || '적 부대 속성',
          level: offLvl,
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          chr: 70,
          isBoss: isBoss,
          role: posCfg.role, // 'guard_depot', 'raider', 'assault'
          troops: Math.min(10000, Math.max(3000, enemySoldierPerUnit)),
          maxTroops: Math.min(10000, Math.max(3000, enemySoldierPerUnit)),`;

const newReturnBlock = `        return {
          id: \`enemy_\${idx}\`,
          faction: 'enemy',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: unitTitle,
          avatar: off.icon || (isDepotGuard ? '🛡️' : '👹'),
          element: off.element || (enemyRuler.includes('손') ? 'water' : (enemyRuler.includes('마') ? 'wind' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? 'fire' : 'earth'))),
          elemIcon: off.elemIcon || (enemyRuler.includes('손') ? '💧' : (enemyRuler.includes('마') ? '🌪️' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? '🔥' : '⛰️'))),
          elemName: off.elemName || '적 부대 속성',
          level: scaledLvl,
          troopName: eTroopName,
          war: Math.min(115, off.war + statBonus),
          int: off.int,
          lead: Math.min(110, (off.lead || 80) + statBonus),
          chr: 70,
          isBoss: isBoss,
          role: posCfg.role, // 'guard_depot', 'raider', 'assault'
          troops: dynamicEnemySoldiers,
          maxTroops: dynamicEnemySoldiers,`;

if (content.includes(oldReturnBlock)) {
  content = content.replace(oldReturnBlock, newReturnBlock);
  console.log('SUCCESS: Patched return block with scaledLvl and dynamicEnemySoldiers');
} else {
  console.error('FAILED to find oldReturnBlock');
}

// ---------------------------------------------------------------------------
// 2. calculateCombatDamage 내 공격/방어력 레벨 동적 연동
// ---------------------------------------------------------------------------
const oldDmgScaling = `      // 아군 병종 숙련도 레벨 보정
      if (attacker.faction === 'ally') {
        const lvl = gameState.troopLevel || 1;
        atkPower *= (1.0 + (lvl - 1) * 0.05);
      }`;

const newDmgScaling = `      // 🔥 [쌍방 병종 숙련도 레벨 보정: 적군도 대등하게 강해짐!]
      const atkLvl = attacker.level || (attacker.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      atkPower *= (1.0 + (atkLvl - 1) * 0.05);

      // 방어력 레벨 보정: 고레벨 부대는 방어력도 탄탄해져 일격사 방지
      const defLvl = defender.level || (defender.faction === 'ally' ? (gameState.troopLevel || 1) : 1);
      defPower *= (1.0 + (defLvl - 1) * 0.04);`;

if (content.includes(oldDmgScaling)) {
  content = content.replace(oldDmgScaling, newDmgScaling);
  console.log('SUCCESS: Patched bidirectional level scaling in calculateCombatDamage');
} else {
  console.error('FAILED to find oldDmgScaling');
}

// ---------------------------------------------------------------------------
// 3. updateUnitDetailCard 무장 상세 카드에 레벨 및 병종 실시간 표시
// ---------------------------------------------------------------------------
const oldTitleUpdate = `document.getElementById("unitGeneralTitle").innerText = \`\${unit.name} (\${unit.title})\`;`;
const newTitleUpdate = `const lvlBadge = unit.level ? \`[Lv.\${unit.level} \${unit.troopName || '정예'}] \` : '';
      document.getElementById("unitGeneralTitle").innerText = \`\${lvlBadge}\${unit.name} (\${unit.title})\`;`;

if (content.includes(oldTitleUpdate)) {
  content = content.replace(oldTitleUpdate, newTitleUpdate);
  console.log('SUCCESS: Patched updateUnitDetailCard to show Lv and troopName');
} else {
  console.error('FAILED to find oldTitleUpdate');
}

// ---------------------------------------------------------------------------
// 4. 전장 개전 시 호적수 긴장감 안내 로그 주입
// ---------------------------------------------------------------------------
const oldBattleLog = `logBattle(\`⚔️ [개전] \${gameState.rulerName}군과 \${enemyRuler}군이 전장에서 대치합니다! 10턴 내로 적 본대를 궤멸시키십시오!\`);`;
const newBattleLog = `const avgEnemyLvl = Math.round(enemyUnits.reduce((acc, u) => acc + (u.level || 1), 0) / Math.max(1, enemyUnits.length));
      logBattle(\`⚔️ [호적수 대치!] 아군(Lv.\${myTroopLvl})의 위세에 맞서 \${enemyRuler}군도 정예병(Lv.\${avgEnemyLvl} \${enemyUnits[0].troopName})으로 무장했습니다!\`);
      logBattle(\`⚔️ 10턴 내로 적 본대를 궤멸시키고 승리를 쟁취하십시오!\`);`;

if (content.includes(oldBattleLog)) {
  content = content.replace(oldBattleLog, newBattleLog);
  console.log('SUCCESS: Patched dynamic enemy introduction log');
} else {
  console.error('FAILED to find oldBattleLog');
}

fs.writeFileSync(file, content, 'utf8');
console.log('DONE: Applied all enemy level scaling patches to Desktop HTML.');
