# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. gameState에 actionPoints = 5 (턴당 5회 전략 행동 제한) 추가
# ==============================================================================
print("1. Adding actionPoints (5 per turn) to gameState...")

if 'actionPoints: 5' not in text:
    text = text.replace(
        "difficulty: 'hard',",
        "difficulty: 'hard',\n      actionPoints: 5,\n      maxActionPoints: 5,"
    )

# consumeActionPoint & updateActionPointUI 함수 추가
action_points_system = """
    // ==========================================================================
    // ⭐ 전략 지도 1턴(1달)당 5회 행동 제한 시스템
    // ==========================================================================
    function getRemainingActionPoints() {
      if (gameState.actionPoints === undefined) gameState.actionPoints = 5;
      return gameState.actionPoints;
    }

    function consumeActionPoint(actionName = '전략 명령') {
      if (gameState.actionPoints === undefined) gameState.actionPoints = 5;
      if (gameState.actionPoints <= 0) {
        alert(`⚠️ [행동력 소진]\\n\\n이번 달(턴)에 하달할 수 있는 5회의 전략 명령을 모두 소진하였습니다!\\n\\n상단 좌측의 [0. 휴양]을 클릭하여 다음 달로 넘어가십시오.`);
        return false;
      }
      gameState.actionPoints--;
      updateActionPointUI();
      logMessage(`⭐ [행동력 소모] '${actionName}' 수행 완료 (잔여 행동력: ${gameState.actionPoints} / 5)`, 'text-yellow-300 font-bold');
      return true;
    }

    function resetMonthlyActionPoints() {
      gameState.actionPoints = 5;
      updateActionPointUI();
      logMessage(`⭐ [새 달 시작] 전략 행동력이 5개로 가득 충전되었습니다! (5회 명령 가능)`, 'text-emerald-300 font-black');
    }

    function updateActionPointUI() {
      const pts = gameState.actionPoints !== undefined ? gameState.actionPoints : 5;
      const el = document.getElementById('action-points-banner');
      const stars = '⭐'.repeat(pts) + '☆'.repeat(5 - pts);
      if (el) {
        el.innerHTML = `
          <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
            <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
            <span class="text-sm font-black text-yellow-300 tracking-wider">${stars} (${pts}/5)</span>
          </div>
        `;
      }
    }
"""

if 'function consumeActionPoint' not in text:
    insert_target = "function executeRest() {"
    idx = text.find(insert_target)
    if idx != -1:
        text = text[:idx] + action_points_system + "\n    " + text[idx:]
        print("  -> consumeActionPoint system injected!")
    else:
        print("  -> ERROR: executeRest not found!")

# 휴양(턴 넘김) 시 행동력 리셋 주입
if 'resetMonthlyActionPoints();' not in text:
    text = text.replace(
        "logMessage(`${gameState.year}년 ${gameState.month}월이 되었습니다.",
        "resetMonthlyActionPoints();\n      logMessage(`${gameState.year}년 ${gameState.month}월이 되었습니다."
    )
    print("  -> resetMonthlyActionPoints wired to monthly advance!")

# 전략 행동 함수들에 consumeActionPoint 검사 주입
actions_to_wrap = [
    ('function executeDev() {', 'executeDev', '영지 개간/상업 개발'),
    ('function executeFlood() {', 'executeFlood', '제방 치수 공사'),
    ('function executeRecruit() {', 'executeRecruit', '모병 및 징집'),
    ('function executeTrain() {', 'executeTrain', '정예 훈련'),
    ('function executeRelief() {', 'executeRelief', '주민 구휼'),
    ('function executeSearch() {', 'executeSearch', '인재 수색'),
    ('function executeShipBuilding() {', 'executeShipBuilding', '누선 함선 건조')
]

for fn_sig, fn_name, desc in actions_to_wrap:
    pattern = re.escape(fn_sig)
    replacement = f"""{fn_sig}
      if (!consumeActionPoint('{desc}')) return;"""
    if f"consumeActionPoint('{desc}')" not in text:
        text = re.sub(pattern, replacement, text)
        print(f"  -> {fn_name} wrapped with consumeActionPoint!")

# 상단 헤더에 action-points-banner 표시 UI 탑재
header_banner = """<div id="action-points-banner" class="flex items-center">
        <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
          <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
          <span class="text-sm font-black text-yellow-300 tracking-wider">⭐⭐⭐⭐⭐ (5/5)</span>
        </div>
      </div>"""

if 'id="action-points-banner"' not in text:
    nav_target = '<div class="flex items-center gap-1.5">'
    idx = text.find(nav_target)
    if idx != -1:
        text = text[:idx] + header_banner + "\n      " + text[idx:]
        print("  -> Action Points Banner added to Top Header!")

# ==============================================================================
# 2. ZOC(Zone of Control) 및 적 통과 저지 BFS 이동 알고리즘 구현
# ==============================================================================
print("2. Implementing ZOC & BFS Hex Pathfinding (No Passing Through Enemies)...")

zoc_pathfinding_code = """
    // ==========================================================================
    // 🛡️ 헥스 인접 6방향 탐색 및 ZOC(통제선 / 적 돌파 저지) BFS 이동 알고리즘
    // ==========================================================================
    function getHexNeighbors(q, r) {
      const isOdd = (r % 2 !== 0);
      const diffs = isOdd ? [
        { dq: 1, dr: 0 }, { dq: -1, dr: 0 },
        { dq: 1, dr: -1 }, { dq: 0, dr: -1 },
        { dq: 1, dr: 1 }, { dq: 0, dr: 1 }
      ] : [
        { dq: 1, dr: 0 }, { dq: -1, dr: 0 },
        { dq: 0, dr: -1 }, { dq: -1, dr: -1 },
        { dq: 0, dr: 1 }, { dq: -1, dr: 1 }
      ];
      return diffs.map(d => ({ q: q + d.dq, r: r + d.dr }))
        .filter(n => n.q >= 0 && n.q < GRID_COLS && n.r >= 0 && n.r < GRID_ROWS);
    }

    function isEnemyAdjacent(q, r, friendlyFaction) {
      const neighbors = getHexNeighbors(q, r);
      return neighbors.some(n => {
        const u = findUnitAt(n.q, n.r);
        return u && u.troops > 0 && u.faction !== friendlyFaction;
      });
    }

    function computeMovementRange(unit) {
      sam5BattleState.reachableHexes = [];
      const form = FORMATIONS[unit.formation];
      const maxMove = Math.max(1, 2 + (form ? form.moveBonus : 0));

      // BFS 큐: { q, r, cost }
      const queue = [{ q: unit.q, r: unit.r, cost: 0 }];
      const visited = new Map();
      visited.set(`${unit.q},${unit.r}`, 0);

      while (queue.length > 0) {
        const curr = queue.shift();

        if (curr.cost >= maxMove) continue;

        const neighbors = getHexNeighbors(curr.q, curr.r);

        for (const n of neighbors) {
          const terrain = (MAP_TERRAIN[n.r] && MAP_TERRAIN[n.r][n.q] !== undefined) ? MAP_TERRAIN[n.r][n.q] : 0;

          // 호로관 관문(3)은 아군 직접 진입 불가
          if (terrain === 3 && unit.faction === "ally") continue;

          // ⚠️ 적 유닛이 있는 타일은 절대 통과 불가! (적 돌파 저지)
          const occupant = findUnitAt(n.q, n.r);
          if (occupant && occupant.troops > 0 && occupant.faction !== unit.faction) {
            continue; // 적이 길목을 막고 있으면 뚫고 갈 수 없음!
          }

          // 지형별 이동 비용: 산악(2)은 2 소모, 독천(6)은 2 소모, 기타 1
          let moveCost = 1;
          if (terrain === 2 || terrain === 6) moveCost = 2;

          const nextCost = curr.cost + moveCost;
          if (nextCost > maxMove) continue;

          const key = `${n.q},${n.r}`;
          if (!visited.has(key) || visited.get(key) > nextCost) {
            visited.set(key, nextCost);

            // 다른 유닛이 없는 빈 타일이면 이동 가능 타일로 등록
            if (!occupant || occupant.id === unit.id) {
              sam5BattleState.reachableHexes.push({ q: n.q, r: n.r });
            }

            // ⚠️ ZOC (Zone of Control) 규칙: 적 부대와 바로 인접한 헥스에 진입하면 적의 저지로 더 이상 전진 불가 (즉시 정지!)
            const enteredZoc = isEnemyAdjacent(n.q, n.r, unit.faction);
            if (!enteredZoc) {
              queue.push({ q: n.q, r: n.r, cost: nextCost });
            }
          }
        }
      }
    }
"""

pattern_move = r"function computeMovementRange[\s\S]*?function updateUnitDetailCard"
match_move = re.search(pattern_move, text)
if match_move:
    text = text[:match_move.start()] + zoc_pathfinding_code.strip() + "\n\n    function updateUnitDetailCard" + text[match_move.end():]
    print("  -> ZOC & BFS Hex Pathfinding successfully replaced!")
else:
    print("  -> ERROR: pattern_move not matched!")

# ==============================================================================
# 3. 아군 군량고 렌더링 강조 & 적 AI: 아군 군량고 및 총대장(유비) 집중 공격
# ==============================================================================
print("3. Enhancing Depot Visuals & Enemy Focus Fire on Commander/Depot...")

# 캔버스 렌더링에서 아군 군량고(8)와 적 군량고(4) 시각 효과 극대화
depot_render_pattern = r"else if \(terrain === 8\) ctx\.fillText\(sam5BattleState\.allySupplyBurned \? \"💥소실\" : \"🌾아군량고\", x, y - 16\);"
depot_render_replacement = """else if (terrain === 8) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = sam5BattleState.allySupplyBurned ? "#ef4444" : "#34d399";
            ctx.fillText(sam5BattleState.allySupplyBurned ? "💥아군량고소실" : "🌾아군군량고", x, y - 16);
            ctx.font = "14px sans-serif";
            ctx.fillText(sam5BattleState.allySupplyBurned ? "🔥" : "🏰", x, y + 16);
          }"""

text = re.sub(depot_render_pattern, depot_render_replacement, text)

# 적 군량고도 시각 강화
depot_enemy_pattern = r"else if \(terrain === 4\) ctx\.fillText\(sam5BattleState\.supplyBurned \? \"💥소실\" : \"🌾적군량고\", x, y - 16\);"
depot_enemy_replacement = """else if (terrain === 4) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = sam5BattleState.supplyBurned ? "#ef4444" : "#facc15";
            ctx.fillText(sam5BattleState.supplyBurned ? "💥적군량고소실" : "🌾적군군량고", x, y - 16);
            ctx.font = "14px sans-serif";
            ctx.fillText(sam5BattleState.supplyBurned ? "🔥" : "🏯", x, y + 16);
          }"""

text = re.sub(depot_enemy_pattern, depot_enemy_replacement, text)

# 적 AI(runEnemyAI) 고도화: 아군 군량고(0, 2) 침공 & 총대장(유비) 집중 점사!
smart_enemy_ai = """
    function runEnemyAI() {
      const enemies = UNITS.filter(u => u.faction === "enemy" && u.troops > 0);
      let step = 0;

      function executeNextEnemy() {
        if (step >= enemies.length || sam5BattleState.battleOver) {
          finishFullTurn();
          return;
        }

        const enemy = enemies[step];
        const allies = UNITS.filter(u => u.faction === "ally" && u.troops > 0);

        if (allies.length > 0) {
          // 아군 총대장 탐색 (유비 우선, 없으면 0번 장수)
          const commander = allies.find(a => a.name.includes('유비') || a.id === 'liu_bei') || allies[0];
          const allyDepotQ = 0, allyDepotR = 2;

          // 🛡️ 1. 군량고 철통 수비대장 (role: 'guard_depot')
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
                logBattle(`🛡️⚔️ [군량고 사수!] 적 수비장수 ${enemy.name}이 군량고에 침입한 ${target.name}에게 맹공을 퍼붓습니다!`);
                playSound('slash');
                const dmg = calculateCombatDamage(enemy, target, 'melee');
                applyDamage(target, dmg);
              } else {
                const stepQ = enemy.q > target.q ? enemy.q - 1 : (enemy.q < target.q ? enemy.q + 1 : enemy.q);
                const stepR = enemy.r > target.r ? enemy.r - 1 : (enemy.r < target.r ? enemy.r + 1 : enemy.r);
                if (!findUnitAt(stepQ, stepR)) {
                  enemy.q = stepQ; enemy.r = stepR;
                  logBattle(`🛡️ 적 수비대장 ${enemy.name}이 군량고 방어선을 지키기 위해 요격에 나섰습니다.`);
                }
              }
            } else {
              if (enemy.q !== 7 || enemy.r !== 3) {
                const stepQ = enemy.q > 7 ? enemy.q - 1 : (enemy.q < 7 ? enemy.q + 1 : enemy.q);
                const stepR = enemy.r > 3 ? enemy.r - 1 : (enemy.r < 3 ? enemy.r + 1 : enemy.r);
                if (!findUnitAt(stepQ, stepR)) {
                  enemy.q = stepQ; enemy.r = stepR;
                }
              }
              enemy.formation = 'bangwon';
              logBattle(`🛡️ 적 수비대장 ${enemy.name}이 군량고 앞목을 철통 방원진으로 사수하고 있습니다!`);
            }
          }
          // 🐎 2. 아군 군량고 우회 기습부대 (role: 'raider')
          else if (enemy.role === 'raider' && !sam5BattleState.allySupplyBurned) {
            const distToAllyDepot = getHexDistance(enemy.q, enemy.r, allyDepotQ, allyDepotR);
            const adjAllies = allies.filter(a => getHexDistance(enemy.q, enemy.r, a.q, a.r) === 1);

            // 바로 앞을 아군이 가로막고 있으면 돌파 시도 공격!
            if (adjAllies.length > 0) {
              const target = adjAllies[0];
              logBattle(`🐎 적 기습부대 ${enemy.name}이 군량고 진로를 가로막은 ${target.name}에게 돌파 공격을 가합니다!`);
              playSound('slash');
              const dmg = calculateCombatDamage(enemy, target, 'melee');
              applyDamage(target, dmg);
            } else {
              // 아군 군량고(0, 2)를 향해 우회 쇄도!
              const stepQ = enemy.q > allyDepotQ ? enemy.q - 1 : (enemy.q < allyDepotQ ? enemy.q + 1 : enemy.q);
              const stepR = enemy.r > allyDepotR ? enemy.r - 1 : (enemy.r < allyDepotR ? enemy.r + 1 : enemy.r);

              if (stepQ === allyDepotQ && stepR === allyDepotR) {
                enemy.q = stepQ; enemy.r = stepR;
                triggerAllySupplyRaid(enemy);
              } else if (!findUnitAt(stepQ, stepR)) {
                enemy.q = stepQ; enemy.r = stepR;
                logBattle(`🐎🚨 [적 기습 경보!] 적 기습부대 ${enemy.name}이 아군 본진 군량고를 노리고 우회 진격 중입니다!`);
              }
            }
          }
          // 👑 3. 적 본대: 아군 총대장(유비) 집중 포위 공격 (Focus Fire on Commander!)
          else {
            const target = commander || allies[0];
            const distToCommander = getHexDistance(enemy.q, enemy.r, target.q, target.r);
            const adjAllies = allies.filter(a => getHexDistance(enemy.q, enemy.r, a.q, a.r) === 1);

            if (distToCommander === 1) {
              // 총대장에게 집중 공격!
              logBattle(`👑⚡ [총대장 집중 공격!] 적장 ${enemy.name}이 아군 총대장 ${target.name}에게 맹공을 퍼붓습니다!`);
              playSound('slash');
              const dmg = Math.floor(calculateCombatDamage(enemy, target, 'melee') * 1.25);
              applyDamage(target, dmg);
              if (target.troops <= 0) {
                logBattle(`🚨 [비보!] 아군 총대장 ${target.name}이 쓰러졌습니다!`);
              }
            } else if (adjAllies.length > 0) {
              // 총대장으로 가는 길을 막는 호위 아군 공격
              const blocker = adjAllies[0];
              logBattle(`⚔️ 적장 ${enemy.name}이 총대장을 호위하는 ${blocker.name}에게 맹공을 퍼붓습니다!`);
              playSound('slash');
              const dmg = calculateCombatDamage(enemy, blocker, 'melee');
              applyDamage(blocker, dmg);
            } else {
              // 총대장을 향해 좁혀오며 진격!
              const stepQ = enemy.q > target.q ? enemy.q - 1 : (enemy.q < target.q ? enemy.q + 1 : enemy.q);
              const stepR = enemy.r > target.r ? enemy.r - 1 : (enemy.r < target.r ? enemy.r + 1 : enemy.r);
              if (!findUnitAt(stepQ, stepR)) {
                enemy.q = stepQ; enemy.r = stepR;
                logBattle(`🏇 적장 ${enemy.name} 부대가 총대장 ${target.name}을 포위하기 위해 쇄도합니다.`);
              }
            }
          }
        }

        enemy.acted = true;
        renderBattlefield();
        step++;
        setTimeout(executeNextEnemy, 550);
      }

      executeNextEnemy();
    }
"""

pattern_ai = r"function runEnemyAI[\s\S]*?function finishFullTurn"
match_ai = re.search(pattern_ai, text)
if match_ai:
    text = text[:match_ai.start()] + smart_enemy_ai.strip() + "\n\n    function finishFullTurn" + text[match_ai.end():]
    print("  -> Smart Enemy AI (Depot Raid & Focus Fire on Commander) successfully replaced!")
else:
    print("  -> ERROR: pattern_ai not matched!")

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

print("Tactical Masterpiece files successfully synced!")
