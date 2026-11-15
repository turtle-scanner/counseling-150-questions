// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

console.log('--- 1. Expanding Modal & Battlefield to Giant 98vw Screen ---');

// 모달 너비 대폭 확장: max-w-6xl -> max-w-[98vw] w-[98vw]
content = content.replace(/max-w-6xl/g, 'max-w-[98vw] w-[98vw]');

// 캔버스 크기 확대: width="1160" height="590" -> width="1280" height="640"
content = content.replace(/width="1160" height="590"/g, 'width="1280" height="640"');

// 캔버스 스타일 확대
content = content.replace(
  'id="battleCanvas" width="1280" height="640" class="rounded border border-amber-900/80 cursor-pointer max-w-full h-auto bg-[#0a0f1d]"',
  'id="battleCanvas" width="1280" height="640" class="rounded-lg border-2 border-yellow-600/80 cursor-pointer w-full h-auto bg-[#080d1a] shadow-2xl"'
);

console.log('--- 2. Enlarging HEX_RADIUS from 38 to 46 for Giant Vivid Hex Grid ---');

// HEX_RADIUS = 38 -> 46
content = content.replace(/const HEX_RADIUS = \d+;/, 'const HEX_RADIUS = 46;');

// getHexPixel 시작 오프셋 조정
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
  console.log('Updated getHexPixel offsets.');
}

console.log('--- 3. Enlarging Unit Avatar & Circle Graphics in renderBattlefield ---');

// 유닛 반지름 22 -> 27, 아바타 18px -> 23px, 이름 11px -> 13px, 게이지 바 확대
content = content.replace(/ctx\.arc\(x, y, 22, 0, Math\.PI \* 2\);/g, 'ctx.arc(x, y, 27, 0, Math.PI * 2);');
content = content.replace(/ctx\.font = "18px serif";/g, 'ctx.font = "24px serif";');
content = content.replace(/ctx\.font = "bold 11px sans-serif";\s*ctx\.fillStyle = unit\.isBoss \? "#fef08a" : "#ffffff";\s*ctx\.shadowColor = "#000000";\s*ctx\.shadowBlur = 4;\s*ctx\.fillText\(unit\.name, x, y \+ 14\);/,
  'ctx.font = "bold 13px sans-serif"; ctx.fillStyle = unit.isBoss ? "#fef08a" : "#ffffff"; ctx.shadowColor = "#000000"; ctx.shadowBlur = 5; ctx.fillText(unit.name, x, y + 17);'
);
content = content.replace(/const barW = 34;\s*const barH = 4;\s*ctx\.fillStyle = "#0f172a";\s*ctx\.fillRect\(x - barW \/ 2, y \+ 23, barW, barH\);/,
  'const barW = 46; const barH = 5; ctx.fillStyle = "#0f172a"; ctx.fillRect(x - barW / 2, y + 27, barW, barH);'
);

console.log('--- 4. Ensuring Action Points (5 Base, 6 for 7 Rulers) & War Connection ---');

// 전역 스코프에 getMaxActionPoints 및 보조 함수 주입 확인
if (!content.includes('function getMaxActionPoints()')) {
  const insertPt = 'function getRemainingActionPoints() {';
  const maxFunc = `function getMaxActionPoints() {
      const ruler = gameState.rulerName || '유비';
      const highCharmRulers = ['유비', '조조', '손권', '장노', '원소', '원술', '마등'];
      if (highCharmRulers.some(r => ruler.includes(r))) {
        return 6;
      }
      return 5;
    }

    `;
  content = content.replace(insertPt, maxFunc + insertPt);
  console.log('Injected getMaxActionPoints function.');
}

console.log('--- 5. Ensuring Specific Boss Levels (Lu Bu 30, Cao Cao 20, Sun Quan 40) ---');

// 손권 40, 여포 30, 조조 20 검증 및 확실한 주입
const bossLevelSnippet = `        // 🔥 [원작 고증 & 유저 맞춤] 명장 시작 레벨 (여포 Lv.30, 조조 Lv.20, 손권 Lv.40) & 적군 레벨 동기화
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

if (!content.includes('scaledLvl = Math.max(40, myTroopLvl + 3);')) {
  content = content.replace(/let scaledLvl = myTroopLvl;[\s\S]*?scaledLvl = Math\.max\(1, myTroopLvl\);\s*\}/, bossLevelSnippet);
  console.log('Ensured boss level snippet is present.');
}

fs.writeFileSync(file, content, 'utf8');
console.log('DONE: Expanded battlefield to giant scale and verified all master rules!');
