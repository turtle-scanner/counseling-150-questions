# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1. isTrueRuler 보강: 정확한 군주명 본인 일치 검사!
# ('장위 (장로동생)' 같은 친척/부하는 군주가 아니므로 절대 총대장 판정 금지!)
ruler_check_logic = '''
    const RULER_BOSS_NAMES = ['조조', '원소', '손책', '손권', '유표', '유장', '장로', '마등', '공손찬', '동탁', '여포', '장각', '사마의'];
    function isTrueRulerOfficer(u) {
      if (!u) return false;
      const n = (u.name || '').trim();
      return RULER_BOSS_NAMES.some(r => n === r || n.startsWith(r + ' ') || n.startsWith(r + '('));
    }
'''

# 2. checkVictoryCondition 정밀 교체
new_check_victory_exact = '''
    function checkVictoryCondition() {
      if (typeof sam5BattleState !== 'undefined' && sam5BattleState.battleOver) return;

      const aliveEnemies = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.filter(u => u.faction === "enemy" && u.troops > 0 && !u.defeated)
        : [];
      const aliveAllies = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.filter(u => u.faction === "ally" && u.troops > 0 && !u.defeated)
        : [];

      // 오직 본인 이름이 '조조', '원소', '장로' 등 군주 본인인 경우만 군주 총대장으로 인정!
      const realBoss = (typeof UNITS !== 'undefined' && Array.isArray(UNITS))
        ? UNITS.find(u => u.faction === "enemy" && isTrueRulerOfficer(u))
        : null;

      const targetRuler = (hexBattleContext.targetProv && hexBattleContext.targetProv.ruler) ? hexBattleContext.targetProv.ruler : '적';

      // 1) 적 군주 본인을 직접 격파했을 때만 총대장 패퇴 승리!
      if (realBoss && (realBoss.troops <= 0 || realBoss.defeated)) {
        triggerVictory(`${targetRuler}군의 총대장 군주 [${realBoss.name}]이(가) 패배하여 퇴각했습니다! 적 군세가 붕괴하여 대승을 거두었습니다!`);
        return;
      }

      // 2) 전장의 모든 적 부대(남은 적 부대 0개)가 전멸했을 때만 승리!
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
    html = html[:start_idx] + ruler_check_logic.strip() + '\n\n' + new_check_victory_exact.strip() + html[cur:]
    print("Replaced checkVictoryCondition with strict name-matching ruler check!")

# 3. endDuelBattle에서도 isTrueRulerOfficer 적용
m_ed = re.search(r'function\s+endDuelBattle\s*\([^)]*\)\s*\{', html)
if m_ed:
    # replace RULER_BOSSES logic inside endDuelBattle
    html = re.sub(
        r'const RULER_BOSSES\s*=\s*\[[^\]]+\];\s*if\s*\(RULER_BOSSES\.some\([^)]+\)\)\s*\{\s*isEnemyBoss\s*=\s*true;\s*\}',
        'isEnemyBoss = isTrueRulerOfficer(p2);',
        html
    )
    print("Updated endDuelBattle to use isTrueRulerOfficer!")

open(target_html_path, 'w', encoding='utf-8').write(html)

# Syntax check
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp = f'temp_verify_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        print(f'SYNTAX ERROR in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:500])
        sys.exit(1)
print('Node.js syntax check: 100% VALID JS!')

# Copy to all 5 target files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
print('All 6 files updated with strict ruler boss check!')
