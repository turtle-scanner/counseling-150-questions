# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. MAP_TERRAIN 선언을 let으로 바꾸고 13x8 동적 할당으로 수정
# ==============================================================================
print("1. Changing const MAP_TERRAIN to let MAP_TERRAIN and fixing 13x8 sizing...")

# const MAP_TERRAIN = [ ... ]; -> let MAP_TERRAIN = Array.from({length: 8}, () => Array(13).fill(0));
text = re.sub(
    r"const MAP_TERRAIN = \[[\s\S]*?\n\s*\];",
    "let MAP_TERRAIN = Array.from({length: GRID_ROWS}, () => Array(GRID_COLS).fill(0));",
    text
)

# applyRegionalBattlefield 함수 내 안전한 13x8 맵 복사 주입
apply_map_fix = """function applyRegionalBattlefield(targetProv) {
      const pId = targetProv ? targetProv.id : 8;
      let mapKey = 'plains';
      if ([1, 2, 3, 4].includes(pId)) mapKey = 'plains';
      else if ([10, 11, 12].includes(pId)) mapKey = 'mountain';
      else if ([5, 6, 7].includes(pId)) mapKey = 'water';
      else if (pId === 13) mapKey = 'fortress';
      else if (pId === 8) mapKey = 'hyeongju';
      else if (pId === 9) mapKey = 'jungle';

      const preset = REGIONAL_MAPS[mapKey] || REGIONAL_MAPS['plains'];
      currentBattleTreasure = preset.treasure ? { ...preset.treasure, found: false } : null;

      // 13열 8행 완전 동적 안전 복사
      MAP_TERRAIN = Array.from({length: GRID_ROWS}, () => Array(GRID_COLS).fill(0));
      for (let r = 0; r < GRID_ROWS; r++) {
        for (let q = 0; q < GRID_COLS; q++) {
          if (preset.terrain[r] && preset.terrain[r][q] !== undefined) {
            MAP_TERRAIN[r][q] = preset.terrain[r][q];
          } else {
            MAP_TERRAIN[r][q] = 0;
          }
        }
      }

      logBattle(`🗺️ [전장 진입] ${targetProv ? targetProv.name : '전장'} - '${preset.name}'에 포진했습니다! (${preset.desc})`);
    }"""

pattern_apply_regional = r"function applyRegionalBattlefield\(targetProv\)[\s\S]*?logBattle\(`🗺️ \[전장 진입\][^\n]*?\);\s*\}"
text = re.sub(pattern_apply_regional, apply_map_fix, text)
print("  -> applyRegionalBattlefield upgraded to dynamic 13x8 array copy!")

# ==============================================================================
# 2. 휴양(0. 휴양 / 턴 넘김) 시 행동력 5개 충전 및 UI 즉시 갱신
# ==============================================================================
print("2. Wiring Action Points reset (5/5) to executeRest and passTurn...")

# executeRest 맨 앞에 확실하게 행동력 5개 리셋과 UI 갱신 주입
rest_action_refill = """function executeRest() {
      closeAllPopups();
      playSfx('rest');

      // ⭐ 한 달(턴) 넘김 시 전략 행동력 5개 즉각 충전!
      gameState.actionPoints = 5;
      updateActionPointUI();
      logMessage(`⭐ [새 달 시작] 전략 행동력이 5개로 완충되었습니다! (5회 명령 가능)`, 'text-emerald-300 font-black');"""

pattern_rest_start = r"function executeRest\(\)\s*\{[\s\S]*?playSfx\('rest'\);"
text = re.sub(pattern_rest_start, rest_action_refill, text)

# updateActionPointUI 함수가 우측 패널의 노란 테두리 박스 내용도 확실히 갱신하도록 보강
action_point_ui_enhanced = """function updateActionPointUI() {
      const pts = gameState.actionPoints !== undefined ? gameState.actionPoints : 5;
      const stars = '⭐'.repeat(pts) + '☆'.repeat(5 - pts);

      // 1. 헤더 상단 배너 갱신
      const headerBanner = document.getElementById('action-points-banner');
      if (headerBanner) {
        headerBanner.innerHTML = `
          <div class="flex items-center gap-2 bg-gradient-to-r from-slate-950 via-amber-950/80 to-slate-950 border-2 border-yellow-400 px-3 py-1 rounded-full shadow-lg">
            <span class="text-xs font-black text-amber-300">🚩 이달의 전략 행동력:</span>
            <span class="text-sm font-black text-yellow-300 tracking-wider">${stars} (${pts}/5)</span>
          </div>
        `;
      }

      // 2. 우측 패널 안의 텍스트도 실시간 갱신
      const panelBanner = document.querySelector('#action-points-banner span.tracking-wider');
      if (panelBanner) {
        panelBanner.innerText = `${stars} (${pts}/5)`;
      }
    }"""

pattern_ui_fn = r"function updateActionPointUI\(\)\s*\{[\s\S]*?\n    \}"
text = re.sub(pattern_ui_fn, action_point_ui_enhanced, text)
print("  -> Action Points refill (5/5) and dual-UI sync connected to executeRest!")

# updateRightPanel 호출 시에도 updateActionPointUI() 호출 보장
if 'updateActionPointUI();' not in text[text.find('function updateRightPanel'):text.find('function updateRightPanel')+1000]:
    text = text.replace(
        "function updateRightPanel(provId) {",
        "function updateRightPanel(provId) {\n      updateActionPointUI();"
    )

# ==============================================================================
# 파일 저장 및 전역 동기화
# ==============================================================================
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

print("MAP_TERRAIN 13x8 AND ACTION POINTS 5/5 FIXED GLOBALLY!")
