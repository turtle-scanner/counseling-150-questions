# -*- coding: utf-8 -*-
import re, subprocess, sys, shutil, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

ts_path = r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script.js'
fatigue_path = r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\apply_duel_random_and_fatigue.js'
target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'

ts_code = open(ts_path, 'r', encoding='utf-8', errors='ignore').read()
fatigue_code = open(fatigue_path, 'r', encoding='utf-8', errors='ignore').read()
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

def extract_fn(src, fn):
    pattern = r'function\s+' + re.escape(fn) + r'\s*\([^)]*\)\s*\{'
    m = re.search(pattern, src)
    if not m:
        return None
    start_idx = m.start()
    open_idx = src.find('{', start_idx)
    if open_idx == -1:
        return None
    depth = 1
    cur = open_idx + 1
    while depth > 0 and cur < len(src):
        ch = src[cur]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        elif ch in ('"', "'", '`'):
            quote = ch
            cur += 1
            while cur < len(src):
                if src[cur] == '\\':
                    cur += 2
                    continue
                if src[cur] == quote:
                    break
                cur += 1
        cur += 1
    return src[start_idx:cur]

fns_from_ts = [
    'changeRuler', 'checkUnification', 'confirmLoadSlot', 'deleteSlot',
    'endBattleDefeat', 'endBattleVictory', 'executeSpecialTraining',
    'getFormattedCurrentDate', 'getMyCapital', 'getOfficerDuelWar',
    'getSlotKey', 'logBattleMsg', 'logDuel', 'logMessage',
    'openRulerSelectModal', 'openUnificationEnding', 'playRetroBgmLoop',
    'playSfx', 'playTone', 'renderDeployOfficerList',
    'setOfficerCustomFormation', 'setOfficerCustomSoldiers',
    'simulateAIBattles', 'updateEnemyOfficersList',
    'updateReorganizeModalUI', 'updateSaveTitleDefault'
]

restored_chunks = []
for fn in fns_from_ts:
    if re.search(r'function\s+' + re.escape(fn) + r'\s*\(', html):
        print(f'Already in html: {fn}')
        continue
    code_block = extract_fn(ts_code, fn)
    if code_block:
        restored_chunks.append(f'// --- Restored: {fn} ---\n{code_block}')
        print(f'Extracted {fn} ({len(code_block)} chars)')
    else:
        print(f'FAILED to extract {fn}')

# getEnemyOfficersWithFatigue from fatigue_code
if not re.search(r'function\s+getEnemyOfficersWithFatigue\s*\(', html):
    eb = extract_fn(fatigue_code, 'getEnemyOfficersWithFatigue')
    if eb:
        restored_chunks.append(f'// --- Restored: getEnemyOfficersWithFatigue ---\n{eb}')
        print(f'Extracted getEnemyOfficersWithFatigue ({len(eb)} chars)')
    else:
        # fallback implementation
        restored_chunks.append('''
    function getEnemyOfficersWithFatigue(rulerName) {
      const pool = (typeof ENEMY_OFFICERS_BY_RULER !== 'undefined' && ENEMY_OFFICERS_BY_RULER[rulerName])
        ? ENEMY_OFFICERS_BY_RULER[rulerName]
        : [{ name: rulerName || '적장', war: 82, int: 75, fatigue: 0 }];
      return pool.map(o => ({ ...o, fatigue: o.fatigue || 0 }));
    }''')

# Bridge functions & missing safe wrappers
bridges = '''
    // --- Bridge & Safety Helpers ---
    function addTroopExp(amount, reason = '군사 훈련') {
      if (typeof gainTroopExp === 'function') return gainTroopExp(amount, reason);
    }
    function updateMainDisplay() {
      if (typeof renderMapPins === 'function') renderMapPins();
      const cap = typeof getMyCapital === 'function' ? getMyCapital() : null;
      if (cap && typeof updateRightPanel === 'function') updateRightPanel(gameState.selectedProvId || cap.id);
    }
    function renderHexBattleMap() {
      if (typeof renderSam5Grid === 'function') renderSam5Grid();
      if (typeof updateSam5TopHUD === 'function') updateSam5TopHUD();
    }
    function renderHexActionUI() {
      if (typeof updateSam5TopHUD === 'function') updateSam5TopHUD();
    }
    function applyRemoteAction(data) {
      console.log('Remote action received:', data);
    }
'''
restored_chunks.append(bridges)

# Upgrade executeAlliance so Liu Bei can always ally with Gongsun Zan (공손찬) or choose target ruler!
new_alliance_fn = '''
    function executeAlliance(preferredRuler) {
      closeAllPopups();
      const myProv = getMyCapital();
      if (!myProv) return;
      if (!Array.isArray(gameState.allies)) gameState.allies = [];

      // 공손찬 영지(1번 유주 등)가 존재하지 않거나 다른 군주로 되어있으면 공손찬 세력 확인
      const allEnemyRulers = [...new Set(PROVINCES.filter(p => p.ruler !== gameState.rulerName).map(p => p.ruler))];
      if (!allEnemyRulers.includes('공손찬')) {
        allEnemyRulers.unshift('공손찬');
      }
      const nonAllyRulers = allEnemyRulers.filter(r => !gameState.allies.includes(r));

      if (nonAllyRulers.length === 0) {
        alert('이미 천하의 모든 군벌과 동맹 관계입니다!');
        return;
      }

      // 유비일 경우 공손찬을 최우선 추천 (동문 사형 관계)
      let targetRuler = preferredRuler;
      if (!targetRuler) {
        if (nonAllyRulers.includes('공손찬')) {
          targetRuler = '공손찬';
        } else {
          targetRuler = nonAllyRulers[0];
        }
      }

      const isGongsun = (targetRuler === '공손찬' && gameState.rulerName === '유비');
      const cost = isGongsun ? 100 : 300;
      if (myProv.gold < cost) {
        alert(`외교 동맹 예물로 금 ${cost}전이 필요합니다. (현재 보유 금: ${myProv.gold})`);
        return;
      }

      myProv.gold -= cost;
      if (!gameState.allies.includes(targetRuler)) {
        gameState.allies.push(targetRuler);
      }
      // 만약 공손찬이 지도에 영지가 없다면 1번 유주(또는 북평)에 공손찬 동맹군 거점 표시 지원
      const p1 = PROVINCES.find(p => p.id === 1);
      if (targetRuler === '공손찬' && p1 && p1.ruler !== gameState.rulerName) {
        p1.ruler = '공손찬';
      }

      playSfx('victory');
      if (isGongsun) {
        logMessage(`🤝 [백마장군 공손찬 동맹] 유비의 동문 사형인 북평의 공손찬(백마의종)과 혈맹을 맺었습니다! (전쟁 시 조운·공손찬 지원군 가세)`, 'text-cyan-300 font-extrabold');
        alert(`🤝 [유비 & 공손찬 형제 동맹 체결!]\n\n"현덕 아우여! 우리의 옛 정을 생각하여 언제든 백마의종 기마대를 보내 돕겠네!"\n\n북평의 공손찬군과 동맹이 성사되었습니다! (전쟁 시 연합군 가세 & 침공 방어)`);
      } else {
        logMessage(`🤝 [동맹 체결 성공] ${targetRuler}군과 피의 맹약을 맺었습니다! (전쟁 시 연합군 지원)`, 'text-cyan-300 font-extrabold');
        alert(`🤝 [동맹 체결]\n${targetRuler}군과의 동맹이 성사되었습니다!\n전쟁 시 연합군이 가세합니다.`);
      }
      renderMapPins();
      updateRightPanel(gameState.selectedProvId || myProv.id);
    }
'''
restored_chunks.append(new_alliance_fn)

# Insert before </script>
last_script_idx = html.rfind('</script>')
final_html = html[:last_script_idx] + '\n\n' + '\n\n'.join(restored_chunks) + '\n' + html[last_script_idx:]

open(target_html_path, 'w', encoding='utf-8').write(final_html)
print('Updated sam3_update.html, size:', len(final_html))

# Syntax check with node
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', final_html, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp = f'temp_verify_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        print(f'SYNTAX ERROR in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:500])
        sys.exit(1)
    else:
        print(f'Script {idx} syntax OK ({len(sc)} chars)')
