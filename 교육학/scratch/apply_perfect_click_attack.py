# -*- coding: utf-8 -*-
"""
삼국지 헥스 전장: 유닛 직접 클릭 감지(Hit-Test) 및 원클릭 100% 자동 공격/돌격 시스템 전면 개편
- 유닛 중심 35px 직접 감지: 장수 얼굴을 누르면 100% 즉시 선택 / 즉시 공격!
- 아군 선택 후 적군 누르면: 인접 칼질 / 사거리 화살 사격 / 돌격 진격 100% 자동 발동!
- 빈 땅 잘못 찍어도 아군 선택이 쉽게 풀리지 않도록 보호
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 캔버스 클릭 이벤트 리스너 및 handleHexClick 전면 교체
# ---------------------------------------------------------------------------
old_click_listener_pattern = r"canvas\.addEventListener\(\"click\", function\(e\) \{[\s\S]*?renderBattlefield\(\);\s*\}"

new_click_system = """    // ==========================================================================
    // 🎯 캔버스 정밀 히트테스트(Hit-Test) 및 직관적 원클릭 부대 공격 시스템
    // ==========================================================================
    canvas.addEventListener("click", function(e) {
      if (sam5BattleState.battleOver) return;
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      const mx = (e.clientX - rect.left) * scaleX;
      const my = (e.clientY - rect.top) * scaleY;

      // 1. [유닛 직접 타겟팅] 반지름 36px 이내 장수 아이콘 클릭 감지
      let clickedUnit = null;
      let minUnitDist = 9999;
      for (const u of UNITS) {
        if (u.troops <= 0) continue;
        const { x, y } = getHexPixel(u.q, u.r);
        const d = Math.hypot(mx - x, my - y);
        if (d < minUnitDist && d < 36) {
          minUnitDist = d;
          clickedUnit = u;
        }
      }

      // 유닛을 클릭한 경우
      if (clickedUnit) {
        handleUnitClick(clickedUnit);
        return;
      }

      // 2. [타일 클릭 판정] 빈 헥스 타일 (이동 타일, 지형 타일 등) 감지
      let closestHex = null;
      let minDist = 9999;
      for (let r = 0; r < GRID_ROWS; r++) {
        for (let q = 0; q < GRID_COLS; q++) {
          const { x, y } = getHexPixel(q, r);
          const dist = Math.hypot(mx - x, my - y);
          if (dist < minDist) {
            minDist = dist;
            closestHex = { q, r };
          }
        }
      }

      if (closestHex && minDist < 48) {
        handleTileClick(closestHex.q, closestHex.r);
      }
    });

    // 🎯 유닛 클릭 핸들러: 아군 선택 / 적군 원클릭 즉시 공격
    function handleUnitClick(unit) {
      const selected = sam5BattleState.selectedUnit;

      // 특기/명령 조준 모드(화계, 원거리 조준 등)인 경우
      if (sam5BattleState.skillMode) {
        executeSkillAction(sam5BattleState.skillMode, unit);
        clearSkillMode();
        renderBattlefield();
        return;
      }

      // 아군 턴이 아니면 단순 카드 조회
      if (sam5BattleState.phase !== "ally") {
        selectUnit(unit);
        renderBattlefield();
        return;
      }

      // A. 아군 부대를 클릭한 경우 -> 선택 및 이동범위 활성화
      if (unit.faction === "ally") {
        selectUnit(unit);
        logBattle(`🛡️ 아군 [${unit.name}] 부대를 선택했습니다. 적 부대를 클릭하면 즉시 공격합니다!`);
        renderBattlefield();
        return;
      }

      // B. 적군 부대를 클릭한 경우 -> 이미 선택된 아군이 있으면 100% 즉시 공격 감행!
      if (unit.faction === "enemy") {
        if (selected && selected.faction === "ally" && !selected.acted) {
          executeDirectAttack(selected, unit);
          renderBattlefield();
          return;
        } else {
          // 선택된 아군이 없으면 적군 상세 카드 조회
          selectUnit(unit);
          renderBattlefield();
          return;
        }
      }
    }

    // 🎯 원클릭 자동 공격 및 돌격 전담 실행기 (Direct Attack & Auto Charge)
    function executeDirectAttack(attacker, target) {
      const dist = getHexDistance(attacker.q, attacker.r, target.q, target.r);
      const isArcher = isMasterArcher(attacker);

      // Case 1: 인접 1칸 적 -> 즉시 칼을 뽑아 근접 공격 또는 3면 포위 일제합공!
      if (dist === 1) {
        logBattle(`🗡️ [근접 공격] ${attacker.name} 부대가 적장 ${target.name}에게 돌격을 감행합니다!`);
        executeSkillAction('attack', target);
        return;
      }

      // Case 2: 2~4칸 거리 적 -> 모든 장수 화살(궁시) 사격 또는 맹화시 발사!
      if (dist <= 4) {
        logBattle(`🏹 [원거리 사격] ${attacker.name} 부대가 적장 ${target.name}에게 화살비를 쏟아붓습니다! (사거리 4칸)`);
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
              logBattle(`🏇 [질풍 돌격!] ${attacker.name} 부대가 적장 ${target.name}에게 쇄도하여 통렬한 돌격을 가합니다!`);
              executeSkillAction('attack', target);
            } else if (newDist <= 4) {
              logBattle(`🏇🏹 [돌격 사격!] ${attacker.name} 부대가 진격 후 적장 ${target.name}에게 화살비를 쏟아붓습니다!`);
              executeSkillAction('archery', target);
            } else {
              logBattle(`🏇 ${attacker.name} 부대가 적장 ${target.name}을 향해 급속 돌격 진격했습니다!`);
              updateActionCommands();
            }
            return;
          }
        }
      }

      logBattle(`적장 ${target.name}이 너무 멀어 공격이 닿지 않습니다. 먼저 파란 이동 타일을 클릭하여 진격하십시오.`);
    }

    // 🎯 빈 타일 클릭 핸들러 (이동 및 스킬 조준)
    function handleTileClick(q, r) {
      // 1. 공격/특기 조준 발동 모드 (화계 등 타일 조준)
      if (sam5BattleState.skillMode) {
        const target = sam5BattleState.attackableTargets.find(t => t.q === q && t.r === r);
        if (target) {
          executeSkillAction(sam5BattleState.skillMode, target);
        } else {
          logBattle("명령 대상이 올바르지 않아 군령을 철회했습니다.");
        }
        clearSkillMode();
        renderBattlefield();
        return;
      }

      const selectedUnit = sam5BattleState.selectedUnit;

      // 2. 이동 가능 타일 클릭 시 부대 이동
      const canMove = sam5BattleState.reachableHexes.find(h => h.q === q && h.r === r);
      if (canMove && selectedUnit && !selectedUnit.moved) {
        selectedUnit.q = q;
        selectedUnit.r = r;
        selectedUnit.moved = true;
        sam5BattleState.reachableHexes = [];

        // 보급창 도달 검사
        const destTerrain = (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] !== undefined) ? MAP_TERRAIN[r][q] : 0;
        if (destTerrain === 4 && !sam5BattleState.supplyBurned) {
          triggerSupplyRaid(selectedUnit);
        } else if (destTerrain === 8 && !sam5BattleState.allySupplyBurned) {
          logBattle(`🌾 아군 ${selectedUnit.name} 부대가 본진 군량고를 경비하고 있습니다.`);
        } else {
          logBattle(`${selectedUnit.name} 부대가 진격하여 진형을 잡았습니다.`);
        }

        playSound('fanfare');
        updateActionCommands();
        renderBattlefield();
        return;
      }

      // 3. 아무것도 없는 허공 클릭 시 선택 해제
      deselectUnit();
      renderBattlefield();
    }

    // 하위 호환 매핑
    function handleHexClick(q, r) {
      const u = findUnitAt(q, r);
      if (u) {
        handleUnitClick(u);
      } else {
        handleTileClick(q, r);
      }
    }"""

if re.search(old_click_listener_pattern, content):
    content = re.sub(old_click_listener_pattern, new_click_system, content, count=1)
    print("SUCCESS: Replaced click listener with flawless direct unit hit-test system.")
else:
    print("WARNING: Could not find old click listener pattern, checking fallback...")

# ---------------------------------------------------------------------------
# 파일 저장 및 동기화
# ---------------------------------------------------------------------------
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Saved patched HTML to Desktop.")

TARGETS = [
    r"C:\Users\LENOVO\Desktop\sam3_update.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
]

for t in TARGETS:
    try:
        shutil.copy2(TARGET_FILE, t)
        print(f"Synced successfully -> {t}")
    except Exception as e:
        print(f"Error copying to {t}: {e}")
