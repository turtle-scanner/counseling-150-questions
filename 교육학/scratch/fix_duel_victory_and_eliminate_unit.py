# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1. closeDuelModal 완벽 강화: duelModal & duel-modal 둘 다 display none !important, 적 부대 궤멸 후 헥스 전장 재렌더링
enhanced_close_duel = '''
    function closeDuelModal() {
      try {
        ['duelModal', 'duel-modal'].forEach(id => {
          const m = document.getElementById(id);
          if (m) {
            m.classList.add('hidden');
            m.style.setProperty('display', 'none', 'important');
            m.style.setProperty('pointer-events', 'none', 'important');
          }
        });
        if (typeof sam5BattleState !== 'undefined' && sam5BattleState.selectedUnit) {
          finishUnitAction(sam5BattleState.selectedUnit);
        }
        if (typeof renderSam5Grid === 'function') renderSam5Grid();
        if (typeof updateSam5TopHUD === 'function') updateSam5TopHUD();
      } catch (e) {
        console.error('closeDuelModal error:', e);
      }
    }
'''

# 2. endDuelBattle 완벽 업그레이드:
# - 적장 포로 생포 확실히 기록
# - 일기토 패배 적 부대 즉시 궤멸 (troops = 0, defeated = true, 전장에서 완전히 소멸)
# - 결과창(logBox) 안에 [🏁 결투 결과 확인 & 전장 복귀] 큰 버튼 직접 삽입
# - 1.8초 후 자동 닫힘 타이머 적용 (사용자가 누르지 않아도 부드럽게 전장 복귀)
enhanced_end_duel = '''
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

        // 2. 🔥 사용자 요청 100% 반영: 일기토 승리 시 해당 적 부대 즉시 전멸 & 전장에서 완전 소멸!
        let enemyEliminated = false;
        let isEnemyBoss = false;

        // 전술 헥스 전장(UNITS 및 sam5BattleState.units)에서 적 부대 검색 및 궤멸
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

        // 영지 수비군/적군 병력에서도 반영
        if (gameState.selectedProvId) {
          const prov = PROVINCES.find(p => p.id === gameState.selectedProvId);
          if (prov && prov.ruler !== gameState.rulerName) {
            prov.soldiers = Math.max(0, prov.soldiers - 3000);
          }
        }

        logMessage(`⛓️ [적장 포로 생포 & 부대 궤멸!] ${p1.name} 장군이 일기토에서 적장 [${capName}]을 생포하여 감옥에 투옥하고, 적 부대를 전멸시켰습니다!`, 'text-yellow-300 font-extrabold text-sm');

        // 승리 배너 + 확인 버튼 삽입 (클릭 시 즉시 복귀 & 1.8초 후 자동 복귀)
        if (logBox) {
          logBox.innerHTML = `
            <div class="p-3 rounded-xl bg-amber-950/95 border-2 border-yellow-400 text-yellow-200 text-center shadow-2xl flex flex-col items-center gap-2">
              <div class="text-base font-black text-yellow-300 flex items-center justify-center gap-1.5 animate-bounce">
                <span>🏆</span> [대승! 적장 ${capName} 포로 생포 & 적 부대 완전 궤멸!]
              </div>
              <div class="text-xs text-slate-200 leading-relaxed">
                <span class="text-yellow-300 font-bold">${p1.name}</span> 장군이 적장 <span class="text-rose-400 font-bold">[${capName}]</span>을 완전히 제압하여 포로로 사로잡았습니다!<br>
                적장은 아군 감옥에 투옥되었으며, <strong>적 부대는 전장에서 완전히 소멸</strong>하였습니다!
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

        // 1.8초 후 자동 닫힘 및 전장 복귀 타이머 (멈춤 현상 완전 박멸!)
        setTimeout(() => {
          closeDuelModal();
          // 적 총대장이 궤멸되었거나 남은 적군이 없으면 전투 대승리 판정
          const remainingEnemies = (typeof sam5BattleState !== 'undefined' && Array.isArray(sam5BattleState.units))
            ? sam5BattleState.units.filter(u => (u.faction === 'enemy' || u.side === 'enemy') && u.troops > 0)
            : [];
          if (isEnemyBoss || remainingEnemies.length === 0) {
            setTimeout(() => {
              if (typeof triggerVictory === 'function') {
                triggerVictory(`운명의 일기토 대승! 적장 [${capName}]을 생포하여 적군이 완전 궤멸했습니다!`);
              }
            }, 600);
          }
        }, 1800);

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
        setTimeout(() => closeDuelModal(), 1800);

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
        setTimeout(() => closeDuelModal(), 1800);
      }
    }
'''

# Find endDuelBattle in html and replace it
fn_pattern = r'function\s+endDuelBattle\s*\([^)]*\)\s*\{'
m = re.search(fn_pattern, html)
if m:
    start_idx = m.start()
    # find closing brace
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
    html = html[:start_idx] + enhanced_end_duel.strip() + html[cur:]
    print("Replaced endDuelBattle successfully!")
else:
    print("WARNING: endDuelBattle not found, appending to script...")
    last_script = html.rfind('</script>')
    html = html[:last_script] + '\n' + enhanced_end_duel + '\n' + html[last_script:]

# Also replace closeDuelModal
m2 = re.search(r'function\s+closeDuelModal\s*\([^)]*\)\s*\{', html)
if m2:
    start_idx = m2.start()
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
    html = html[:start_idx] + enhanced_close_duel.strip() + html[cur:]
    print("Replaced closeDuelModal successfully!")

# Ensure closeDuelModal is also defined at the bottom of the script for 100% guarantee
last_script_idx = html.rfind('</script>')
html = html[:last_script_idx] + '\n' + enhanced_close_duel + '\n' + html[last_script_idx:]

open(target_html_path, 'w', encoding='utf-8').write(html)

# Check syntax
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp = f'temp_verify_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        print(f'SYNTAX ERROR in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:500])
        sys.exit(1)
print('Node.js check: ALL SCRIPTS VALID JS!')

# Copy to all 5 files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
    print('Synced to:', tgt)
