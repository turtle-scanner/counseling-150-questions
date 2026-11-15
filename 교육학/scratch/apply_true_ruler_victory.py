# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1. checkVictoryCondition 수정: 군주(조조, 원소 등)를 잡거나 모든 적 부대가 0개일 때만 승리!
new_check_victory = '''
    function checkVictoryCondition() {
      if (typeof sam5BattleState !== 'undefined' && sam5BattleState.battleOver) return;

      const aliveEnemies = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.filter(u => u.faction === "enemy" && u.troops > 0 && !u.defeated)
        : [];
      const aliveAllies = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.filter(u => u.faction === "ally" && u.troops > 0 && !u.defeated)
        : [];

      // 🔥 사용자 지정 룰: 오직 '조조, 원소 등 적 군주' 또는 '모든 부대 전멸' 시에만 승리!
      const RULER_BOSSES = ['조조', '원소', '손책', '손권', '유표', '유장', '장로', '마등', '공손찬', '동탁', '여포', '장각', '사마의'];
      const realBoss = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.find(u => u.faction === "enemy" && RULER_BOSSES.some(r => (u.name && u.name.includes(r)) || (u.fullName && u.fullName.includes(r))))
        : null;

      const targetRuler = (hexBattleContext.targetProv && hexBattleContext.targetProv.ruler) ? hexBattleContext.targetProv.ruler : '적';

      // 1) 적 군주를 직접 격파했을 때만 총대장 패퇴 승리!
      if (realBoss && (realBoss.troops <= 0 || realBoss.defeated)) {
        triggerVictory(`${targetRuler}군의 총대장 군주 [${realBoss.name}]이(가) 패배하여 퇴각했습니다! 적 군세가 붕괴하여 대승을 거두었습니다!`);
        return;
      }

      // 2) 전장의 모든 적 부대가 전멸했을 때만 승리! (일반 적장은 부대만 없어지고 계속 싸움)
      if (aliveEnemies.length === 0) {
        triggerVictory(`${targetRuler}군 전 부대를 완전히 궤멸시켰습니다! 천하에 이름을 떨친 완벽한 승리입니다!`);
        return;
      }

      // 3) 아군 전 부대 전멸 시
      if (aliveAllies.length === 0) {
        triggerDefeat("아군 전 부대가 전멸하여 패배했습니다...");
        return;
      }
    }
'''

# Replace checkVictoryCondition
m_cv = re.search(r'function\s+checkVictoryCondition\s*\([^)]*\)\s*\{', html)
if m_cv:
    start_idx = m_cv.start()
    open_idx = html.find('{', start_idx)
    depth = 1
    cur = open_idx + 1
    while depth > 0 and cur < len(html):
        ch = html[cur]
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        elif ch in ('"', "'", '`'):
            q = ch
            cur += 1
            while cur < len(html):
                if html[cur] == '\\': cur += 2; continue
                if html[cur] == q: break
                cur += 1
        cur += 1
    html = html[:start_idx] + new_check_victory.strip() + html[cur:]
    print("Replaced checkVictoryCondition with true ruler/all-units rule successfully!")

open(target_html_path, 'w', encoding='utf-8').write(html)

# 2. Also run add_sango_event_system logic to include Zhuge Liang and Sango
print("Now running sango integration...")
