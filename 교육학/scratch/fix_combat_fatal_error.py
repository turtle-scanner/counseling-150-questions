# -*- coding: utf-8 -*-
"""
삼국지 웹게임: 치명적 ReferenceError(clearSkillMode 내 targetProv 미정의) 영구 수리 및
원클릭 자동 돌격 이동 공격 완벽 통합 패치
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. clearSkillMode() 내의 치명적인 applyRegionalBattlefield(targetProv); 완전 제거
# ---------------------------------------------------------------------------
old_clear_skill = """    function clearSkillMode() {
      sam5BattleState.skillMode = null;
      applyRegionalBattlefield(targetProv);
      sam5BattleState.attackableTargets = [];
    }"""

new_clear_skill = """    function clearSkillMode() {
      sam5BattleState.skillMode = null;
      sam5BattleState.attackableTargets = [];
    }"""

if old_clear_skill in content:
    content = content.replace(old_clear_skill, new_clear_skill)
    print("SUCCESS: Fixed fatal ReferenceError in clearSkillMode()!")
else:
    # 정규식으로 안전하게 교체
    content = re.sub(
        r"function clearSkillMode\(\)\s*\{[\s\S]*?sam5BattleState\.attackableTargets\s*=\s*\[\];\s*\}",
        new_clear_skill.strip(),
        content
    )
    print("SUCCESS: Replaced clearSkillMode() using regex.")

# ---------------------------------------------------------------------------
# 2. getElementAdvantage 내의 defRule.icon 안전 처리
# ---------------------------------------------------------------------------
content = content.replace("${defRule.icon}", "${defRule ? defRule.icon : ''}")

# ---------------------------------------------------------------------------
# 3. executeSkillAction('attack', targetPos) 내에 돌격 이동(Charge-Move) 내장
#    - 거리가 1보다 크고 아직 이동하지 않았다면, 적 인접 빈 타일로 먼저 이동 후 칼질!
# ---------------------------------------------------------------------------
old_exec_pattern = r"function executeSkillAction\(mode, targetPos\)\s*\{[\s\S]*?if \(mode === 'attack' && targetUnit\)\s*\{"

new_exec_prefix = """function executeSkillAction(mode, targetPos) {
      const u = sam5BattleState.selectedUnit;
      if (!u) return;
      const targetUnit = findUnitAt(targetPos.q, targetPos.r);
      if (!targetUnit) return;
      const isArcher = isMasterArcher(u);

      if (mode === 'attack' && targetUnit) {
        // [★돌격 이동 자동 결합★] 적과 거리가 1칸보다 멀고 아직 이동하지 않았다면 적 앞으로 즉시 쇄도 이동!
        const curDist = getHexDistance(u.q, u.r, targetUnit.q, targetUnit.r);
        if (curDist > 1 && !u.moved) {
          computeMovementRange(u);
          const adjHexes = getHexNeighbors(targetUnit.q, targetUnit.r);
          const chargeHex = sam5BattleState.reachableHexes.find(h => adjHexes.some(a => a.q === h.q && a.r === h.r));
          if (chargeHex) {
            u.q = chargeHex.q;
            u.r = chargeHex.r;
            u.moved = true;
            sam5BattleState.reachableHexes = [];
            logBattle(`🏇 [질풍 쇄도!] ${u.name} 부대가 적장 ${targetUnit.name}의 코앞으로 돌진하여 일격을 가합니다!`);
            playSound('fanfare');
          } else if (sam5BattleState.reachableHexes.length > 0) {
            // 가장 가까운 타일로 전진
            let bestHex = null;
            let bestD = 999;
            sam5BattleState.reachableHexes.forEach(h => {
              const d = getHexDistance(h.q, h.r, targetUnit.q, targetUnit.r);
              if (d < bestD) { bestD = d; bestHex = h; }
            });
            if (bestHex) {
              u.q = bestHex.q;
              u.r = bestHex.r;
              u.moved = true;
              sam5BattleState.reachableHexes = [];
            }
          }
        }"""

content = re.sub(old_exec_pattern, new_exec_prefix, content, count=1)
print("SUCCESS: Embedded charge-move directly into executeSkillAction('attack').")

# ---------------------------------------------------------------------------
# 4. 파일 저장 및 동기화
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
