# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. 4대 명궁 (황충, 서황, 태사자, 공손찬) 레벨 8 시작 & 원거리 화살 공격 등록
# ==============================================================================
print("1. Updating 4 Master Archers (Hwang Chung, Xu Huang, Taishi Ci, Gongsun Zan) to Lv.8...")

# 1-1. MY_OFFICERS 내 황충 Lv.8
text = re.sub(
    r"\{\s*id:\s*'huang_zhong'[\s\S]*?\}",
    "{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장 (신궁)', hp: 100, fatigue: 0, element: 'fire', elemIcon: '🔥', elemName: '불 (火 - 화시)', level: 8, exp: 1000, troopType: 'archer', troopName: '정예궁병 (신궁)', arcRange: 4 }",
    text
)

# 1-2. ENEMY_OFFICERS_BY_RULER['공손찬'] 공손찬 Lv.8
text = re.sub(
    r"\{\s*name:\s*'공손찬 \(백규\)'[\s\S]*?\}",
    "{ name: '공손찬 (백규)', war: 84, int: 68, lead: 83, icon: '🏹', title: '백마의종 신궁 (백마 궁기병)', faceKey: 'gongsongzan', element: 'fire', elemIcon: '🔥', elemName: '불 (火)', level: 8, exp: 1000, arcRange: 4 }",
    text
)

# 1-3. ENEMY_OFFICERS_BY_RULER['손책'] 태사자 Lv.8
text = re.sub(
    r"\{\s*name:\s*'태사자 \(자의\)'[\s\S]*?\}",
    "{ name: '태사자 (자의)', war: 95, int: 72, lead: 86, icon: '🏹', title: '강동의 신궁 명장 (백발백중)', skills: ['신궁', '화시', '돌격', '분기'], element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)', level: 8, exp: 1000, arcRange: 4 }",
    text
)

# 1-4. 조조군에 '서황 (공명)' 추가 (Lv.8 명궁)
if "'서황 (공명)'" not in text:
    target_caocao = "'조조': ["
    idx = text.find(target_caocao)
    if idx != -1:
        insert_xuhuang = "'조조': [\n        { name: '서황 (공명)', war: 91, int: 74, lead: 88, icon: '🏹', title: '양평관 대부명궁', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)', level: 8, exp: 1000, arcRange: 4 },"
        text = text[:idx] + insert_xuhuang + text[idx + len(target_caocao):]
        print("  -> Xu Huang (Lv.8 Master Archer) added to Cao Cao army!")

# 1-5. isMasterArcher 함수에 4인 전원 등록
master_archer_fn = """    function isMasterArcher(unit) {
      if (!unit) return false;
      const n = (unit.name || '') + ' ' + (unit.fullName || '');
      return n.includes('황충') || n.includes('서황') || n.includes('태사자') || n.includes('공손찬');
    }"""

text = re.sub(
    r"function isMasterArcher\(unit\)\s*\{[\s\S]*?\}",
    master_archer_fn,
    text
)
print("  -> isMasterArcher function updated for all 4 archers!")

# ==============================================================================
# 2. 훈련하면 레벨 1씩 올라가게 해줘 (executeTraining 개편)
# ==============================================================================
print("2. Enhancing executeTraining (Lv +1 Guaranteed on Training)...")

training_code = """function executeTraining() {
      closeAllPopups();
      if (!consumeActionPoint('군사 훈련')) return;
      const myProv = getMyCapital();
      if (myProv.gold < 100) { alert('군사 훈련을 위한 군비(금 100전)가 부족합니다.'); return; }
      myProv.gold -= 100;
      myProv.soldiers = Math.min(60000, myProv.soldiers + 300);
      playSfx('build');
      
      // 🔥 아군 전 장수 레벨 1씩 확정 상승!
      MY_OFFICERS.forEach(off => {
        off.level = (off.level || 1) + 1;
        off.exp = (off.exp || 0) + 100;
        off.war = Math.min(100, off.war + 1); // 무력 보너스
      });
      
      // 병종 숙련도 레벨도 상승
      gameState.troopLevel = (gameState.troopLevel || 1) + 1;
      const newLvl = Math.max(...MY_OFFICERS.map(o => o.level || 1));
      
      playSound('fanfare');
      logMessage(`⚔️⭐ [정예 맹훈련 완료] 아군 전 장수 및 부대의 레벨이 1씩 상승했습니다! (현재 최고 레벨: Lv.${newLvl})`, 'text-yellow-300 font-black text-sm');
      updateRightPanel(myProv.id);
      
      alert(`⚔️⭐ [정예 맹훈련 완료!]\n\n군사 맹훈련을 통해 아군 전 장수와 부대의 레벨이 1씩 상승하였습니다!\n\n▶ 아군 최고 레벨: Lv.${newLvl}\n▶ 효과: 이동거리 증가, 공격력/방어력 상승, 계략 성공률 대폭 증가!`);
    }"""

pattern_train = r"function executeTraining\(\)\s*\{[\s\S]*?updateRightPanel\(myProv\.id\);\s*\}"
match_train = re.search(pattern_train, text)
if match_train:
    text = text[:match_train.start()] + training_code + text[match_train.end():]
    print("  -> executeTraining successfully upgraded to Level +1 guaranteed!")
else:
    print("  -> WARNING: pattern_train not matched!")

# ==============================================================================
# 3. 레벨이 높을수록 이동거리 증가 & 계략 성공률 대폭 상승
# ==============================================================================
print("3. Implementing Level-scaled Movement and Tactics Success...")

# BFS 이동 거리 공식: 기본 2칸 + (레벨 / 3)칸 추가!
level_move_logic = """function computeMovementRange(unit) {
      sam5BattleState.reachableHexes = [];
      const form = FORMATIONS[unit.formation];
      
      // 🏇 레벨 스케일링 이동력: 기본 2 + 진형보너스 + (레벨 / 3) 추가 기동!
      const lvlBonus = Math.floor((unit.level || 1) / 3);
      const maxMove = Math.max(1, 2 + (form ? form.moveBonus : 0) + lvlBonus);

      const queue = [{ q: unit.q, r: unit.r, cost: 0 }];
      const visited = new Map();
      visited.set(`${unit.q},${unit.r}`, 0);

      while (queue.length > 0) {
        const curr = queue.shift();
        if (curr.cost >= maxMove) continue;

        const neighbors = getHexNeighbors(curr.q, curr.r);

        for (const n of neighbors) {
          const terrain = (MAP_TERRAIN[n.r] && MAP_TERRAIN[n.r][n.q] !== undefined) ? MAP_TERRAIN[n.r][n.q] : 0;
          if (terrain === 3 && unit.faction === "ally") continue;

          // 적 유닛 타일은 절대 통과 불가 (돌파 저지)
          const occupant = findUnitAt(n.q, n.r);
          if (occupant && occupant.troops > 0 && occupant.faction !== unit.faction) {
            continue;
          }

          let moveCost = 1;
          if (terrain === 2 || terrain === 6) moveCost = 2; // 산악/독천 2 소모

          const nextCost = curr.cost + moveCost;
          if (nextCost > maxMove) continue;

          const key = `${n.q},${n.r}`;
          if (!visited.has(key) || visited.get(key) > nextCost) {
            visited.set(key, nextCost);

            if (!occupant || occupant.id === unit.id) {
              sam5BattleState.reachableHexes.push({ q: n.q, r: n.r });
            }

            // ZOC: 적과 인접하면 이동력 남아도 즉시 정지
            const enteredZoc = isEnemyAdjacent(n.q, n.r, unit.faction);
            if (!enteredZoc) {
              queue.push({ q: n.q, r: n.r, cost: nextCost });
            }
          }
        }
      }

      // 안전장치: 인접한 빈 타일 중 적이 없는 곳은 언제나 최소 이동 보장
      const directNeighbors = getHexNeighbors(unit.q, unit.r);
      directNeighbors.forEach(n => {
        if (!findUnitAt(n.q, n.r) && !sam5BattleState.reachableHexes.some(h => h.q === n.q && h.r === n.r)) {
          sam5BattleState.reachableHexes.push({ q: n.q, r: n.r });
        }
      });
    }"""

text = re.sub(
    r"function computeMovementRange\(unit\)\s*\{[\s\S]*?\n    \}",
    level_move_logic,
    text
)
print("  -> Level-scaled computeMovementRange with safety fallback injected!")

# 계략 성공률 및 대미지에 레벨 스케일링 주입
chaos_success_pattern = r"const successRate = 55 \+ \(u\.int - targetUnit\.int\) \* 2;"
chaos_success_replacement = """// 🔮 레벨 비례 계략 성공률: 기본 60% + (레벨 * 4)% + 지력 차이 (고레벨일수록 확정 명중!)
        const lvlBonus = (u.level || 1) * 4;
        const successRate = Math.min(100, Math.max(30, 60 + lvlBonus + (u.int - targetUnit.int) * 2));"""

text = re.sub(chaos_success_pattern, chaos_success_replacement, text)

# ==============================================================================
# 4. 적들도 레벨업 & 전쟁을 통한 성장 & 훈련 및 병사 모집 자율 수행
# ==============================================================================
print("4. Implementing Enemy Faction Growth (Training, Recruitment & Combat Level-Up)...")

# 전투 중 적군 레벨업 연산 추가 (applyDamage 내부)
apply_damage_enhancement = """    function applyDamage(unit, damage, attacker = null) {
      unit.troops = Math.max(0, unit.troops - damage);
      showDamagePop(unit.q, unit.r, `-${damage}`);

      // 👹 적군도 교전을 통해 경험치 획득 및 레벨업!
      if (attacker && attacker.faction === 'enemy') {
        attacker.exp = (attacker.exp || 0) + 25;
        if (attacker.exp >= 100) {
          attacker.level = (attacker.level || 1) + 1;
          attacker.exp = 0;
          showDamagePop(attacker.q, attacker.r, `⭐적장 레벨업! Lv.${attacker.level}`);
          logBattle(`👹⭐ [적장 각성 레벨업!] 적장 ${attacker.name}이 실전 경험으로 Lv.${attacker.level}(으)로 승급했습니다!`);
        }
      }

      if (unit.troops <= 0) {
        logBattle(`☠️ [궤멸] ${unit.faction === 'ally' ? '아군' : '적장'} ${unit.name} 부대가 전멸하여 패주했습니다!`);
        // 격파한 적장에게 즉시 레벨 +1 보너스!
        if (attacker && attacker.faction === 'enemy') {
          attacker.level = (attacker.level || 1) + 1;
          attacker.morale = 100;
          showDamagePop(attacker.q, attacker.r, `⭐적장 격파 레벨업! Lv.${attacker.level}`);
          logBattle(`👹⚡ [적장 대폭 레벨업!] 적장 ${attacker.name}이 아군을 격파하고 Lv.${attacker.level}에 도달했습니다!`);
        }
        checkVictoryCondition();
      }
      renderBattlefield();
    }"""

pattern_apply_damage = r"function applyDamage\(unit, damage\)[\s\S]*?renderBattlefield\(\);\s*\}"
match_apply_damage = re.search(pattern_apply_damage, text)
if match_apply_damage:
    text = text[:match_apply_damage.start()] + apply_damage_enhancement.strip() + text[match_apply_damage.end():]
    print("  -> applyDamage upgraded with Enemy Combat Level-Up!")

# 적 군벌들의 매월 자율 징병 & 훈련 시스템
enemy_monthly_growth_code = """
    // ==========================================================================
    // 🚩 적 군벌 자율 성장: 매월 병사 모집(+1,000~2,500명) & 장수 정예 훈련(Lv.+1)
    // ==========================================================================
    function processEnemyFactionsTurn() {
      PROVINCES.forEach(p => {
        if (p.ruler !== gameState.rulerName && p.ruler !== '공백지') {
          // 1. 적 병사 모집
          const recruits = 800 + Math.floor(Math.random() * 1400);
          p.soldiers = Math.min(50000, p.soldiers + recruits);

          // 2. 적 장수 군사 훈련 (레벨 +1 성장)
          const enemyList = ENEMY_OFFICERS_BY_RULER[p.ruler];
          if (enemyList) {
            enemyList.forEach(e => {
              e.level = (e.level || 1) + 1;
            });
          }
        }
      });

      const enemyRulers = Object.keys(ENEMY_OFFICERS_BY_RULER).filter(r => r !== gameState.rulerName);
      if (enemyRulers.length > 0) {
        const activeRuler = enemyRulers[Math.floor(Math.random() * enemyRulers.length)];
        logMessage(`🚩 [적 군벌 동향] ${activeRuler}군이 영지에서 징병(+1,500명)과 정예 훈련(장수 Lv.+1)을 단행했습니다!`, 'text-red-300 font-bold');
      }
    }
"""

if 'function processEnemyFactionsTurn' not in text:
    idx = text.find('function executeRest() {')
    if idx != -1:
        text = text[:idx] + enemy_monthly_growth_code + "\n    " + text[idx:]
        print("  -> processEnemyFactionsTurn injected!")

# executeRest 안에 processEnemyFactionsTurn() 호출 주입
if 'processEnemyFactionsTurn();' not in text:
    text = text.replace(
        "resetMonthlyActionPoints();",
        "resetMonthlyActionPoints();\n      processEnemyFactionsTurn();"
    )
    print("  -> processEnemyFactionsTurn wired to monthly advance!")

# ==============================================================================
# 5. 아군 부대 이동 완전 정상화 (handleHexClick & selectUnit 안전장치)
# ==============================================================================
print("5. Polishing Unit Movement & Click Handlers...")

# 턴 시작 시 전 유닛 이동/행동 상태 무조건 완전 초기화 보장
turn_reset_code = """      // 부대 턴 리셋 (이동 및 행동 상태 완전 초기화)
      UNITS.forEach(u => {
        u.moved = false;
        u.acted = false;
      });
      sam5BattleState.phase = "ally";
      sam5BattleState.selectedUnit = null;
      sam5BattleState.reachableHexes = [];
      sam5BattleState.attackableTargets = [];"""

text = re.sub(
    r"// 부대 턴 리셋[\s\S]*?UNITS\.forEach\(u => \{[\s\S]*?\}\);",
    turn_reset_code.strip(),
    text
)

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

print("ALL COMPLETE AND SYNCED!")
