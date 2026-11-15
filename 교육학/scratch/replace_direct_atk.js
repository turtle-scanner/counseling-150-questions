const fs = require('fs');
const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

const startTag = 'function executeDirectAttack(attacker, target) {';
const endTag = 'function handleUnitClick(unit) {';

const startIdx = content.indexOf(startTag);
const endIdx = content.indexOf(endTag);

if (startIdx === -1 || endIdx === -1) {
  console.error('Tags not found:', startIdx, endIdx);
  process.exit(1);
}

const oldFunc = content.substring(startIdx, endIdx);

const newFunc = `function executeDirectAttack(attacker, target) {
      if (!attacker || !target) return;
      const dist = getHexDistance(attacker.q, attacker.r, target.q, target.r);
      const isArcher = isMasterArcher(attacker);

      // Case 1: 인접 1칸 적 -> 즉시 칼을 뽑아 근접 공격 또는 3면 포위 일제합공!
      if (dist === 1) {
        logBattle("🗡️ [근접 공격] " + attacker.name + " 부대가 적장 " + target.name + "에게 돌격을 감행합니다!");
        executeSkillAction('attack', target);
        return;
      }

      // Case 2: 2~4칸 거리 적 -> 모든 장수 화살(궁시) 사격 또는 맹화시 발사!
      if (dist <= 4) {
        logBattle("🏹 [원거리 사격] " + attacker.name + " 부대가 적장 " + target.name + "에게 화살비를 쏟아붓습니다! (사거리 4칸)");
        executeSkillAction('archery', target);
        return;
      }

      // Case 3: 4칸 초과 거리 적 -> 적 인접 타일로 맹렬히 돌격 진격 후 공격!
      if (!attacker.moved) {
        computeMovementRange(attacker);
        if (sam5BattleState.reachableHexes.length > 0) {
          let bestHex = null;
          let bestDist = 999;
          sam5BattleState.reachableHexes.forEach(h => {
            const d = getHexDistance(h.q, h.r, target.q, target.r);
            if (d < bestDist) {
              bestDist = d;
              bestHex = h;
            }
          });

          if (bestHex) {
            attacker.q = bestHex.q;
            attacker.r = bestHex.r;
            attacker.moved = true;
            sam5BattleState.reachableHexes = [];
            playSound('fanfare');

            const newDist = getHexDistance(attacker.q, attacker.r, target.q, target.r);
            if (newDist === 1) {
              logBattle("🏇 [질풍 돌격!] " + attacker.name + " 부대가 적장 " + target.name + "에게 쇄도하여 통렬한 돌격을 가합니다!");
              executeSkillAction('attack', target);
            } else if (newDist <= 4) {
              logBattle("🏇🏹 [돌격 사격!] " + attacker.name + " 부대가 진격 후 적장 " + target.name + "에게 화살비를 쏟아붓습니다!");
              executeSkillAction('archery', target);
            } else {
              logBattle("🏇 " + attacker.name + " 부대가 적장 " + target.name + "을 향해 급속 돌격 진격했습니다!");
              updateActionCommands();
            }
            return;
          }
        }
      }

      logBattle("적장 " + target.name + "이 너무 멀어 공격이 닿지 않습니다. 먼저 녹색 이동 타일을 클릭하여 진격하십시오.");
    }

    `;

content = content.replace(oldFunc, newFunc);
fs.writeFileSync(file, content, 'utf8');
console.log('SUCCESS: Cleanly replaced executeDirectAttack without any string escape issues!');
