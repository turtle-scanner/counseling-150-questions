# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 군주 / 총사령관 명단
# ['조조', '원소', '손책', '손권', '유표', '유장', '장로', '마등', '공손찬', '동탁', '여포']

new_end_duel_battle = '''
    function endDuelBattle(result, narrative, isCaptured = false) {
      sam5DuelState.battleOver = true;
      const { p1, p2 } = sam5DuelState;
      const capName = p2 ? p2.name : '적장';

      // 6대 전술 버튼 숨기기
      const actionGrid = document.getElementById("duelActionGrid");
      if (actionGrid) actionGrid.classList.add("hidden");

      const logBox = document.getElementById("duelNarrative");

      if (result === 'victory') {
        playSound('fanfare');

        // 1. 적장 포로 생포 처리
        gameState.capturedOfficers = gameState.capturedOfficers || [];
        if (!gameState.capturedOfficers.some(c => c.name === capName)) {
          gameState.capturedOfficers.push({
            name: capName,
            war: p2.war || 85,
            int: p2.int || 75,
            lead: p2.lead || 80,
            avatar: p2.avatar || '⚔️',
            capturedDate: (gameState.year || 208) + "년 " + (gameState.month || 1) + "월"
          });
        }

        // 2. 🔥 사용자 전용 규칙: 일기토 승리 시 해당 적 부대만 즉시 전멸 & 전장에서 소멸!
        let enemyEliminated = false;
        let isEnemyBoss = false;

        // 주요 군주/총사령관 목록 (이들을 잡았을 때만 총사령관 판정!)
        const RULER_BOSSES = ['조조', '원소', '손책', '손권', '유표', '유장', '장로', '마등', '공손찬', '동탁', '여포', '장각', '사마의'];
        if (RULER_BOSSES.some(r => capName.includes(r))) {
          isEnemyBoss = true;
        }

        // 전술 헥스 전장 유닛 검색 및 부대 궤멸
        const allUnits = [];
        if (typeof UNITS !== 'undefined' && Array.isArray(UNITS)) allUnits.push(...UNITS);
        if (typeof sam5BattleState !== 'undefined' && Array.isArray(sam5BattleState.units)) {
          sam5BattleState.units.forEach(u => { if (!allUnits.includes(u)) allUnits.push(u); });
        }

        allUnits.forEach(u => {
          if (u && (u.faction === 'enemy' || u.side === 'enemy')) {
            if (u.name === capName || u.name.includes(capName) || (capName && capName.includes(u.name))) {
              u.troops = 0;
              u.hp = 0;
              u.acted = true;
              u.defeated = true;
              enemyEliminated = true;
              if (u.isBoss) isEnemyBoss = true;
            }
          }
        });

        // sam5BattleState.units 에서 0명 부대 필터링 제거하여 맵에서 깨끗하게 소멸
        if (typeof sam5BattleState !== 'undefined' && Array.isArray(sam5BattleState.units)) {
          sam5BattleState.units = sam5BattleState.units.filter(u => u.troops > 0 && !u.defeated);
        }

        // 남은 적 부대 수 계산
        const remainingEnemies = (typeof sam5BattleState !== 'undefined' && Array.isArray(sam5BattleState.units))
          ? sam5BattleState.units.filter(u => (u.faction === 'enemy' || u.side === 'enemy') && u.troops > 0 && !u.defeated)
          : [];

        // 영지 수비군 병력 삭감
        if (gameState.selectedProvId) {
          const prov = PROVINCES.find(p => p.id === gameState.selectedProvId);
          if (prov && prov.ruler !== gameState.rulerName) {
            prov.soldiers = Math.max(0, prov.soldiers - 3000);
          }
        }

        logMessage(`⛓️ [적장 포로 생포 & 부대 소멸!] ${p1.name} 장군이 일기토에서 적장 [${capName}]을 생포하여 감옥에 투옥하고, 해당 적 부대를 전멸시켰습니다! (남은 적 부대: ${remainingEnemies.length}개)`, 'text-yellow-300 font-extrabold text-sm');

        // 승리 배너 렌더링
        let statusDesc = '';
        if (isEnemyBoss) {
          statusDesc = `🚩 적군 총사령관 <span class="text-rose-400 font-black">[${capName}]</span>을 생포하여 <strong>적 전군이 완전 항복</strong>했습니다!`;
        } else if (remainingEnemies.length === 0) {
          statusDesc = `🚩 전장의 <strong>모든 적 부대가 전멸</strong>하여 전쟁에서 승리했습니다!`;
        } else {
          statusDesc = `⚔️ 적장 [${capName}] 부대가 소멸되었습니다! <strong>남은 적군 ${remainingEnemies.length}개 부대</strong>를 계속 소탕하십시오!`;
        }

        if (logBox) {
          logBox.innerHTML = `
            <div class="p-3 rounded-xl bg-amber-950/95 border-2 border-yellow-400 text-yellow-200 text-center shadow-2xl flex flex-col items-center gap-2">
              <div class="text-base font-black text-yellow-300 flex items-center justify-center gap-1.5 animate-bounce">
                <span>🏆</span> [대승! 적장 ${capName} 포로 생포 & 부대 궤멸]
              </div>
              <div class="text-xs text-slate-200 leading-relaxed">
                <span class="text-yellow-300 font-bold">${p1.name}</span> 장군이 적장 <span class="text-rose-400 font-bold">[${capName}]</span>을 제압하여 포로로 사로잡았습니다!<br>
                ${statusDesc}
              </div>
              <button onclick="closeDuelModal()" class="mt-2 px-8 py-2.5 rounded-lg bg-gradient-to-r from-amber-600 via-yellow-500 to-amber-600 hover:from-amber-500 hover:to-yellow-400 text-black font-black text-xs shadow-2xl border-2 border-yellow-200 transform hover:scale-105 transition cursor-pointer">
                🏁 결투 결과 확인 & 전장 복귀 (확인)
              </button>
            </div>
          `;
        }

        // 전장 갱신
        if (typeof renderSam5Grid === 'function') renderSam5Grid();
        if (typeof updateSam5TopHUD === 'function') updateSam5TopHUD();

        // 1.5초 후 자동 닫힘 및 전장 복귀
        setTimeout(() => {
          closeDuelModal();

          // 🔥 오직 '적 군주/총사령관'을 잡았거나 '남은 적 부대가 0개'일 때만 전쟁 전체 승리 판정!
          if (isEnemyBoss || remainingEnemies.length === 0) {
            setTimeout(() => {
              if (typeof triggerVictory === 'function') {
                const winReason = isEnemyBoss 
                  ? `적 총사령관 [${capName}]을 일기토로 생포하여 적군이 완전 궤멸했습니다!`
                  : `모든 적군 부대를 전멸시키고 영지를 완전 평정했습니다!`;
                triggerVictory(winReason);
              }
            }, 500);
          }
        }, 1500);

      } else if (result === 'defeat') {
        playSound('fire');
        if (logBox) {
          logBox.innerHTML = `
            <div class="p-3 rounded-xl bg-red-950/95 border-2 border-red-500 text-rose-200 text-center flex flex-col items-center gap-2">
              <div class="text-sm font-black text-red-300">💥 [결투 패배] 아군 장수 분전 후 후퇴...</div>
              <div class="text-xs text-slate-300">
                ${p1.name} 장군이 혼신을 다해 싸웠으나 깊은 부상을 입고 본진으로 안전하게 후퇴했습니다.
              </div>
              <button onclick="closeDuelModal()" class="mt-1 px-6 py-2 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-600">
                확인
              </button>
            </div>
          `;
        }
        logMessage(`💥 [일기토 패전] ${p1.name} 장군이 일기토에서 분전하였으나 후퇴하였습니다.`, 'text-red-400 font-bold');
        setTimeout(() => closeDuelModal(), 1500);

      } else {
        if (logBox) {
          logBox.innerHTML = `
            <div class="p-3 rounded-xl bg-blue-950/95 border-2 border-cyan-400 text-cyan-200 text-center flex flex-col items-center gap-2">
              <div class="text-sm font-black text-cyan-300">🐎 [작전상 후퇴] 안전하게 결투장 탈출!</div>
              <div class="text-xs text-slate-300">
                ${p1.name} 장군이 목숨을 보전하여 아군 진영으로 무사히 복귀하였습니다.
              </div>
              <button onclick="closeDuelModal()" class="mt-1 px-6 py-2 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-600">
                확인
              </button>
            </div>
          `;
        }
        setTimeout(() => closeDuelModal(), 1500);
      }
    }
'''

# Find endDuelBattle in html and replace it
fn_pattern = r'function\s+endDuelBattle\s*\([^)]*\)\s*\{'
m = re.search(fn_pattern, html)
if m:
    start_idx = m.start()
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
    html = html[:start_idx] + new_end_duel_battle.strip() + html[cur:]
    print("Replaced endDuelBattle with boss/all-units rule successfully!")

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

# Sync to all 5 target files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
print('All 6 files synchronized successfully!')
