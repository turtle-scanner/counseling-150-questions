# -*- coding: utf-8 -*-
import re, subprocess, sys, shutil, os

with open(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script1.js', 'r', encoding='utf-8', errors='ignore') as f:
    src_code = f.read()

with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    dst_html = f.read()

missing_list = [
  'battleActionAttack', 'battleActionRaidStorage', 'battleActionTrap', 'battleStartOfficerDuel',
  'clearLogs', 'confirmTrade', 'duelAction', 'executeAlliance', 'executeAppoint', 'executeBreakAlliance',
  'executeCommerceDev', 'executeConfiscate', 'executeDelegate', 'executeDirectOrder', 'executeEmergencyTax',
  'executeFireOfficer', 'executeFloodControl', 'executeHeal', 'executeHireOfficer', 'executeJointOperation',
  'executeLandDev', 'executeRelief', 'executeSearchOfficer', 'executeStratagem', 'executeTraining',
  'executeTreasureSearch', 'executeWander', 'handleInvasionDefend', 'handleInvasionDuel', 'handleInvasionHexBattle',
  'openDuelSelectModal', 'openInfoModal', 'openQuestModal', 'openReorganizeModal',
  'openTaxRateModal', 'openTradeModal', 'openTreasureModal', 'renderInfoTable', 'reorganizeSoldiers',
  'retreatFromBattleModal', 'selectScenario', 'toggleBGM'
]

# Extract all functions from src_code
# A robust regex to find function signatures and their entire body or extract ranges
extracted_blocks = []

for fn in missing_list:
    # Check if already present in dst_html
    if f'function {fn}' in dst_html or f'{fn} =' in dst_html:
        print(f"Skipping {fn}, already exists in dst_html.")
        continue

    # Find in src_code
    pattern = r'function\s+' + re.escape(fn) + r'\s*\([^)]*\)\s*\{'
    m = re.search(pattern, src_code)
    if not m:
        # maybe let fn = ...
        pattern2 = re.escape(fn) + r'\s*=\s*(?:function|\([^)]*\)\s*=>)'
        m = re.search(pattern2, src_code)
    if m:
        start_idx = m.start()
        # count braces to find full body
        open_idx = src_code.find('{', start_idx)
        if open_idx != -1:
            depth = 1
            cur = open_idx + 1
            while depth > 0 and cur < len(src_code):
                ch = src_code[cur]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                elif ch in ('"', "'", '`'):
                    quote = ch
                    cur += 1
                    while cur < len(src_code):
                        if src_code[cur] == '\\':
                            cur += 2
                            continue
                        if src_code[cur] == quote:
                            break
                        cur += 1
                cur += 1
            fn_code = src_code[start_idx:cur]
            extracted_blocks.append((fn, fn_code))
            print(f"Successfully extracted {fn} (Length: {len(fn_code)})")
        else:
            print(f"Brace not found for {fn}")
    else:
        print(f"NOT FOUND IN SRC_CODE: {fn}")

# Add onCmdAmbushSkill
ambush_skill_code = '''
    function onCmdAmbushSkill() {
      if (!isMyTurn || isHexGameOver) return;
      const unit = hexBattleContext.units.find(u => u.id === selectedHexUnitId && u.side === 'player' && !u.hasActed);
      if (!unit) { alert('행동 가능한 아군 부대를 먼저 선택하십시오.'); return; }
      logMessage(`🌿 [매복 병법] ${unit.name} 부대가 숲 지형에 은밀히 매복하여 방어력을 200% 상승시키고 적을 기습합니다!`, 'text-emerald-400 font-bold');
      playSfx('build');
      unit.def *= 2;
      unit.hasActed = true;
      renderHexBattleMap();
      renderHexActionUI();
    }
'''

# Also add robust Keyboard and Mouse System
keyboard_mouse_code = '''
    // ==================== 🎮 마우스 및 키보드 통합 컨트롤 시스템 ====================
    window.addEventListener('DOMContentLoaded', () => {
      initKeyboardAndMouseControls();
    });

    function initKeyboardAndMouseControls() {
      // 키보드 단축키 (0~9, d, w, t, c, r, m, ESC, Space, Enter)
      document.addEventListener('keydown', (e) => {
        // 인풋이나 텍스트에어리어 입력 중일 때는 제외
        if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;

        const key = e.key;
        console.log('Keyboard Pressed:', key);

        // ESC: 모든 팝업 및 열려있는 모달 닫기
        if (key === 'Escape') {
          closeAllPopups();
          document.querySelectorAll('.modal-backdrop, [id$=\"-modal\"]').forEach(el => {
            if (!el.classList.contains('hidden')) {
              el.classList.add('hidden');
              el.style.display = 'none';
              el.style.pointerEvents = 'none';
            }
          });
          return;
        }

        // 0: 휴양 (턴 종료 및 행동력 완충)
        if (key === '0') {
          e.preventDefault();
          executeRest();
          return;
        }

        // 1: 군사 팝업 토글
        if (key === '1') {
          e.preventDefault();
          togglePopup(null, 'popup-military');
          return;
        }

        // 2: 인사 팝업 토글
        if (key === '2') {
          e.preventDefault();
          togglePopup(null, 'popup-personnel');
          return;
        }

        // 3: 외교 팝업 토글
        if (key === '3') {
          e.preventDefault();
          togglePopup(null, 'popup-diplomacy');
          return;
        }

        // 4: 정보 모달 열기
        if (key === '4') {
          e.preventDefault();
          openInfoModal();
          return;
        }

        // 5: 개발 팝업 토글
        if (key === '5') {
          e.preventDefault();
          togglePopup(null, 'popup-develop');
          return;
        }

        // 6: 상인 팝업 토글
        if (key === '6') {
          e.preventDefault();
          togglePopup(null, 'popup-merchant');
          return;
        }

        // 7: 특별 팝업 토글
        if (key === '7') {
          e.preventDefault();
          togglePopup(null, 'popup-special');
          return;
        }

        // 8: 계략 팝업 토글
        if (key === '8') {
          e.preventDefault();
          togglePopup(null, 'popup-stratagem');
          return;
        }

        // 9: 기능 팝업 토글
        if (key === '9') {
          e.preventDefault();
          togglePopup(null, 'popup-system');
          return;
        }

        // D 또는 d: 장수 골라 1:1 결투 즉시 열기
        if (key === 'd' || key === 'D') {
          e.preventDefault();
          openDuelSelectModal();
          return;
        }

        // W 또는 w: 전쟁 모달 즉시 열기
        if (key === 'w' || key === 'W') {
          e.preventDefault();
          openWarModal();
          return;
        }

        // T 또는 t: 군사 훈련 즉시 실행
        if (key === 't' || key === 'T') {
          e.preventDefault();
          executeTraining();
          return;
        }

        // C 또는 c: 징병 실행
        if (key === 'c' || key === 'C') {
          e.preventDefault();
          executeConscription();
          return;
        }

        // R 또는 r: 모병 실행
        if (key === 'r' || key === 'R') {
          e.preventDefault();
          executeRecruit();
          return;
        }

        // M 또는 m: 배경음악 및 효과음 토글
        if (key === 'm' || key === 'M') {
          e.preventDefault();
          toggleBGM();
          return;
        }
      });
    }

    // togglePopup 함수가 이벤트 없이(null) 호출되어도 안전하게 작동하도록 보강
    const origTogglePopup = window.togglePopup || togglePopup;
    function togglePopup(e, id) {
      if (e && e.stopPropagation) e.stopPropagation();
      const popup = document.getElementById(id);
      if (!popup) return;
      const isOpen = popup.classList.contains('show');
      closeAllPopups();
      if (!isOpen) {
        popup.classList.add('show');
        playSfx('select');
      }
    }
'''

# Combine extracted functions into a big chunk
combined_js = "\n\n    // ==================== 🚀 복원된 핵심 커맨드 및 조작 시스템 ====================\n"
for fn, fcode in extracted_blocks:
    combined_js += f"\n    // --- {fn} ---\n" + fcode + "\n"

combined_js += "\n" + ambush_skill_code + "\n" + keyboard_mouse_code + "\n"

# Insert combined_js before the closing </script> in dst_html
last_script_idx = dst_html.rfind('</script>')
if last_script_idx != -1:
    new_html = dst_html[:last_script_idx] + combined_js + dst_html[last_script_idx:]
    print("Combined JS successfully inserted before </script>!")
else:
    print("Error: </script> not found!")
    sys.exit(1)

# Save to sam3_update.html
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Saved to C:\\Users\\LENOVO\\Desktop\\sam3_update.html")

# Check Node.js syntax
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', new_html, re.DOTALL)
has_err = False
for idx, sc in enumerate(scripts):
    tmp_f = f'temp_check_all_{idx}.js'
    with open(tmp_f, 'w', encoding='utf-8') as tf:
        tf.write(sc)
    res = subprocess.run(['node', '--check', tmp_f], capture_output=True)
    if res.returncode != 0:
        has_err = True
        err = res.stderr.decode('utf-8', errors='replace')
        print(f"Syntax Error in Script {idx}:")
        print(err[:600])
    else:
        print(f"Script {idx}: 100% VALID JS! Length: {len(sc)}")

if not has_err:
    print("ALL SCRIPTS 100% VALID! Syncing to all files...")
    targets = [
        r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
    ]
    for tgt in targets:
        shutil.copy2(r'C:\Users\LENOVO\Desktop\sam3_update.html', tgt)
        print(f"Copied to {tgt}")
    print("All targets synchronized successfully!")
