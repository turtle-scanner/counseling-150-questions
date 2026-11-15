# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. 캔버스 크기 및 모달 너비 확장 (1160 x 590 대형 전장)
# ==============================================================================
print("1. Expanding Canvas to 1160x590 and Modal Width...")

text = re.sub(
    r'<canvas id="battleCanvas" width="\d+" height="\d+"',
    '<canvas id="battleCanvas" width="1160" height="590"',
    text
)

# 모달 컨테이너 너비 확장 (max-w-7xl)
text = re.sub(
    r'<div class="relative w-full max-w-5xl bg-gradient-to-b',
    '<div class="relative w-full max-w-7xl bg-gradient-to-b',
    text
)

# ==============================================================================
# 2. 그리드 상수 13 x 8 및 헥스 크기 최적화
# ==============================================================================
print("2. Updating Grid to 13 COLS x 8 ROWS with HEX_RADIUS 38...")

grid_constants_code = """const GRID_COLS = 13;
    const GRID_ROWS = 8;
    const HEX_RADIUS = 38;
    const HEX_W = Math.sqrt(3) * HEX_RADIUS;
    const HEX_H = 2 * HEX_RADIUS;"""

pattern_grid = r"const GRID_COLS = \d+;\s*const GRID_ROWS = \d+;\s*const HEX_RADIUS = \d+;\s*const HEX_W = Math\.sqrt\(3\) \* HEX_RADIUS;\s*const HEX_H = 2 \* HEX_RADIUS;"
text = re.sub(pattern_grid, grid_constants_code, text)

# getHexPixel 좌표 오프셋 미세조정
hex_pixel_code = """function getHexPixel(q, r) {
      const x = 58 + q * HEX_W + (r % 2 === 1 ? HEX_W / 2 : 0);
      const y = 48 + r * (HEX_H * 0.75);
      return { x, y };
    }"""

pattern_pixel = r"function getHexPixel\(q, r\)\s*\{[\s\S]*?\}"
text = re.sub(pattern_pixel, hex_pixel_code, text)

# ==============================================================================
# 3. 6대 지형 전체에 맞춤 성벽(타일 3)과 성문(타일 9) 13x8 맵 구축!
# ==============================================================================
print("3. Building 13x8 Regional Maps with Castle Walls (3) and Gates (9)...")

# 타일 정의:
# 0: 평지, 1: 숲, 2: 산악, 3: 🧱 성벽(통과불가), 4: 🌾 적 군량고(12, 4),
# 5: 수로, 6: 늪지대, 7: 🏆 보물, 8: 🌾 아군 군량고(0, 3), 9: ⛩️ 성문(통과가능)

regional_maps_large = """REGIONAL_MAPS = {
      // 1. 하북 대평원 (유주 1, 기주 2, 청주 3, 연주 4) - 하북 방어 목책 성벽 & 2대 관문 성문
      'plains': {
        name: '하북 대평원 & 하북 관문 대성벽',
        desc: '광활한 평원을 가로지르는 철옹성 성벽! 2곳의 성문(⛩️)을 돌파하거나 우회하십시오!',
        terrain: [
          [0, 1, 0, 0, 7, 0, 3, 0, 1, 0, 0, 1, 0], // (4, 0) 전설의 보물 사당!
          [0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0], // (6, 2) ⛩️ 북쪽 하북 성문!
          [8, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 0, 0], // (0, 3) 🌾 아군 군량고!
          [0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4], // (12, 4) 🌾 적 군량고!
          [0, 0, 0, 0, 0, 0, 9, 0, 0, 1, 0, 0, 0], // (6, 5) ⛩️ 남쪽 하북 성문!
          [0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 3, 0, 1, 0, 0, 1, 0]
        ],
        treasure: { name: '적토마 (赤兎馬)', stat: '무력 +5, 기동력 +1칸', type: 'war', val: 5 }
      },
      // 2. 서촉 험산 협곡 (익주 10, 양주 11, 병주 12) - 검각/양평관 천혜의 암벽 관문 성벽
      'mountain': {
        name: '서촉 험산 협곡 & 검각 천혜 성벽',
        desc: '험준한 암벽산맥 사이에 버틴 검각 철벽 성벽! 좁은 협곡 성문(⛩️)을 사수하십시오!',
        terrain: [
          [2, 2, 0, 0, 0, 2, 3, 2, 2, 0, 0, 2, 2],
          [2, 0, 0, 7, 2, 2, 3, 2, 0, 0, 2, 0, 2], // (3, 1) 협곡 비밀 동굴!
          [0, 0, 2, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0],
          [8, 0, 2, 0, 0, 0, 9, 0, 0, 0, 2, 0, 0], // (0, 3) 🌾 아군 군량고! / (6, 3) ⛩️ 검각 성문!
          [0, 2, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 4], // (12, 4) 🌾 적 군량고!
          [0, 2, 2, 0, 0, 0, 9, 0, 2, 2, 0, 0, 0], // (6, 5) ⛩️ 남쪽 우회 관문!
          [2, 0, 0, 0, 2, 2, 3, 2, 0, 0, 2, 2, 0],
          [2, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 2, 2]
        ],
        treasure: { name: '장팔사모 (丈八蛇矛)', stat: '무력 +7 영구 상승', type: 'war', val: 7 }
      },
      // 3. 강동 적벽 수향 수로 (양주 7, 서주 5, 예주 6) - 장강 수채 철쇄 수상 방벽 & 수상 수문
      'water': {
        name: '강동 적벽 수향 & 장강 수상 철쇄 성벽',
        desc: '거대한 장강을 가로지르는 철쇄 수상 방벽! 수문(⛩️)을 통과해 적진을 강습하십시오!',
        terrain: [
          [0, 1, 5, 5, 0, 0, 3, 0, 0, 5, 5, 1, 0],
          [1, 0, 5, 5, 5, 0, 3, 0, 5, 5, 5, 0, 0],
          [0, 0, 0, 5, 5, 0, 9, 0, 5, 5, 0, 1, 0], // (6, 2) ⛩️ 북쪽 수상 수문!
          [8, 0, 1, 0, 5, 5, 3, 5, 5, 0, 1, 0, 0], // (0, 3) 🌾 아군 군량고!
          [0, 1, 0, 0, 5, 5, 3, 5, 5, 0, 0, 0, 4], // (12, 4) 🌾 적 군량고!
          [0, 0, 1, 0, 0, 0, 9, 0, 0, 5, 5, 7, 0], // (6, 5) ⛩️ 남쪽 수상 수문! / (11, 5) 침몰 보물선!
          [1, 0, 0, 1, 0, 0, 3, 0, 0, 1, 5, 5, 0],
          [0, 0, 0, 0, 1, 0, 3, 1, 0, 0, 0, 5, 0]
        ],
        treasure: { name: '손자병법서 (孫子兵法)', stat: '지력 +8, 통솔 +6', type: 'int', val: 8 }
      },
      // 4. 중원 낙양 호로관 (사례교위부 13) - 난공불락 호로관 거대 석벽 & 호로관 철갑 성문
      'fortress': {
        name: '중원 낙양 호로관 난공불락 대성벽',
        desc: '천하제일 관문 호로관 성벽! 굳게 닫힌 철갑 성문(⛩️)을 화공과 궁시로 무너뜨리십시오!',
        terrain: [
          [0, 1, 0, 0, 0, 2, 3, 2, 2, 0, 0, 1, 0],
          [1, 0, 0, 0, 2, 2, 3, 2, 0, 0, 0, 0, 7], // (12, 1) 황실 비고!
          [0, 0, 1, 0, 0, 0, 9, 0, 0, 1, 0, 0, 0], // (6, 2) ⛩️ 호로관 제1철문!
          [8, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], // (0, 3) 🌾 아군 군량고!
          [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4], // (12, 4) 🌾 적 군량고!
          [0, 1, 0, 0, 0, 0, 9, 0, 0, 0, 1, 0, 0], // (6, 5) ⛩️ 호로관 제2철문!
          [0, 0, 1, 1, 0, 2, 3, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1, 0]
        ],
        treasure: { name: '의천검 (倚天劍)', stat: '무력 +8 영구 상승', type: 'war', val: 8 }
      },
      // 5. 형주 신야 복합 수륙 (형주 8) - 신야 팔괘 목책 성벽 & 성문
      'hyeongju': {
        name: '형주 신야 복합 수륙 & 신야 목책 방벽',
        desc: '평야와 수로를 잇는 신야 방벽! 성문(⛩️)을 사수하며 와룡선생의 계략을 펼치십시오!',
        terrain: [
          [0, 7, 1, 0, 0, 5, 3, 5, 0, 1, 0, 1, 0], // (1, 0) 와룡 사당!
          [1, 0, 0, 0, 5, 5, 3, 0, 0, 0, 5, 0, 0],
          [0, 0, 1, 0, 5, 0, 9, 0, 1, 0, 0, 0, 0], // (6, 2) ⛩️ 신야 북문!
          [8, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], // (0, 3) 🌾 아군 군량고!
          [0, 5, 5, 5, 0, 0, 3, 0, 0, 0, 0, 0, 4], // (12, 4) 🌾 적 군량고!
          [0, 1, 0, 0, 0, 0, 9, 0, 1, 0, 1, 0, 0], // (6, 5) ⛩️ 신야 남문!
          [0, 0, 1, 1, 0, 5, 3, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1, 0, 0]
        ],
        treasure: { name: '청룡언월도 (靑龍偃月刀)', stat: '무력 +8, 통솔 +5', type: 'war', val: 8 }
      },
      // 6. 남월 교주 밀림 맹독 (교주 9) - 남만 거석 성벽 & 토성 관문
      'jungle': {
        name: '남월 교주 밀림 & 남만 거석 방벽',
        desc: '독안개 늪지에 세워진 고대 거석 성벽! 성문(⛩️)을 뚫고 적 보급로를 끊으십시오!',
        terrain: [
          [1, 6, 6, 1, 0, 0, 3, 0, 1, 6, 0, 1, 0],
          [6, 1, 0, 6, 6, 0, 3, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 6, 0, 9, 0, 0, 0, 6, 0, 0], // (6, 2) ⛩️ 남만 북쪽 관문!
          [8, 0, 0, 0, 0, 0, 3, 0, 6, 1, 0, 0, 0], // (0, 3) 🌾 아군 군량고!
          [0, 6, 1, 0, 0, 0, 3, 0, 0, 0, 6, 7, 4], // (12, 4) 🌾 적 군량고! / (11, 4) 남만 성소!
          [6, 1, 0, 1, 6, 0, 9, 0, 0, 6, 0, 0, 0], // (6, 5) ⛩️ 남만 남쪽 관문!
          [0, 0, 6, 0, 1, 6, 3, 0, 0, 0, 6, 0, 0],
          [1, 0, 0, 0, 0, 1, 3, 1, 6, 0, 0, 1, 0]
        ],
        treasure: { name: '옥새 (玉璽)', stat: '매력 +10 영구 상승', type: 'int', val: 10 }
      }
    };"""

text = re.sub(
    r"REGIONAL_MAPS\s*=\s*\{[\s\S]*?\n\s*\};",
    regional_maps_large,
    text
)
print("  -> 13x8 Regional Maps with Wall(3) and Gate(9) successfully injected!")

# ==============================================================================
# 4. 캔버스 렌더링: 성벽(3: 🧱성벽) 및 성문(9: ⛩️성문) 시각화
# ==============================================================================
print("4. Updating Canvas Terrain Renderer for Walls (3) and Gates (9)...")

wall_color_code = """if (terrain === 1) tileColor = "#14532d"; // 숲
          else if (terrain === 2) tileColor = "#44403c"; // 산악
          else if (terrain === 3) tileColor = "#334155"; // 🧱 성벽 (석조 방벽)
          else if (terrain === 9) tileColor = "#78350f"; // ⛩️ 성문/관문
          else if (terrain === 4) tileColor = sam5BattleState.supplyBurned ? "#292524" : "#854d0e"; // 🌾 적 보급창
          else if (terrain === 8) tileColor = sam5BattleState.allySupplyBurned ? "#292524" : "#047857"; // 🌾 아군 보급창
          else if (terrain === 5) tileColor = "#1e3a8a"; // 강물/수로
          else if (terrain === 6) tileColor = "#4a044e"; // 늪지대/독천
          else if (terrain === 7) tileColor = "#b45309"; // 🏆 전설의 보물 상자"""

pattern_tile_color = r"if \(terrain === 1\) tileColor = \"#14532d\";[\s\S]*?else if \(terrain === 7\) tileColor = \"#b45309\"; // 🏆 전설의 보물 상자"
text = re.sub(pattern_tile_color, wall_color_code, text)

wall_label_code = """if (terrain === 1) ctx.fillText("🌲숲", x, y - 16);
          else if (terrain === 2) ctx.fillText("⛰️산", x, y - 16);
          else if (terrain === 3) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = "#cbd5e1";
            ctx.fillText("🧱성벽", x, y - 14);
            ctx.font = "14px sans-serif";
            ctx.fillText("🛡️", x, y + 14);
          }
          else if (terrain === 9) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = "#fde047";
            ctx.fillText("⛩️성문", x, y - 14);
            ctx.font = "14px sans-serif";
            ctx.fillText("🚪", x, y + 14);
          }
          else if (terrain === 4) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = sam5BattleState.supplyBurned ? "#ef4444" : "#facc15";
            ctx.fillText(sam5BattleState.supplyBurned ? "💥적량고소실" : "🌾적군군량고", x, y - 16);
            ctx.font = "14px sans-serif";
            ctx.fillText(sam5BattleState.supplyBurned ? "🔥" : "🏯", x, y + 16);
          }
          else if (terrain === 8) {
            ctx.font = "bold 11px sans-serif";
            ctx.fillStyle = sam5BattleState.allySupplyBurned ? "#ef4444" : "#34d399";
            ctx.fillText(sam5BattleState.allySupplyBurned ? "💥아량고소실" : "🌾아군군량고", x, y - 16);
            ctx.font = "14px sans-serif";
            ctx.fillText(sam5BattleState.allySupplyBurned ? "🔥" : "🏰", x, y + 16);
          }"""

pattern_tile_label = r"if \(terrain === 1\) ctx\.fillText\(\"🌲숲\", x, y - 16\);[\s\S]*?else if \(terrain === 8\) \{[\s\S]*?\}"
text = re.sub(pattern_tile_label, wall_label_code, text)
print("  -> Terrain Renderer updated with Wall & Gate visual tokens!")

# ==============================================================================
# 5. 아군/적군 초기 배치 좌표 확장 (13열 와이드 대전장 최적화)
# ==============================================================================
print("5. Scaling Unit Initial Positions for 13-column battlefield...")

units_pos_large = """      // 13열 와이드 대전장 아군 포진 (좌측 본진)
      const allyPositions = [
        { q: 2, r: 3, form: 'gyorin' },    // 1번 선봉 중앙
        { q: 2, r: 4, form: 'bongsi' },    // 2번 남쪽 돌파
        { q: 1, r: 2, form: 'chuhaeng' },  // 3번 북쪽 기동
        { q: 1, r: 3, form: 'bangwon' },   // 4번 본진 중앙 수호
        { q: 2, r: 2, form: 'anhaeng' },   // 5번 후방 원거리 지원
        { q: 1, r: 5, form: 'gyorin' }     // 6번 남익 후위 호위
      ];"""

pattern_ally_pos = r"const allyPositions = \[[\s\S]*?\];"
text = re.sub(pattern_ally_pos, units_pos_large, text, count=1)

enemy_pos_large = """      // 13열 와이드 대전장 적군 포진 (성문 수비 & 본대 & 군량고 철통수비)
      const enemyPositions = [
        { q: 9, r: 3, form: 'bongsi', role: 'assault' },       // 적 보스 돌격대
        { q: 9, r: 4, form: 'gyorin', role: 'assault' },       // 적 본대
        { q: 8, r: 2, form: 'chuhaeng', role: 'raider' },      // 🐎 아군 군량고(0, 3) 우회 기습대!
        { q: 7, r: 2, form: 'bangwon', role: 'gate_guard' },   // 🛡️ 성문(6, 2) 철통 수비대장!
        { q: 11, r: 4, form: 'bangwon', role: 'guard_depot' }  // 🛡️ 적 군량고(12, 4) 사수대장!
      ];"""

pattern_enemy_pos = r"const enemyPositions = \[[\s\S]*?\];"
text = re.sub(pattern_enemy_pos, enemy_pos_large, text, count=1)
print("  -> Unit Deployment Positions scaled to 13-column battlefield!")

# ==============================================================================
# 6. 이동 및 성벽 통과 불가 규칙 (BFS 알고리즘 내 성벽 3 차단 & 성문 9 통과)
# ==============================================================================
print("6. Enforcing Wall Block & Gate Pass in BFS pathfinding...")

bfs_wall_check = """          // 🧱 성벽(3)은 어떤 지상 유닛도 절대 통과 불가! (성문 9는 통과 가능)
          if (terrain === 3) continue;

          // 적 유닛 타일은 절대 통과 불가 (돌파 저지)
          const occupant = findUnitAt(n.q, n.r);
          if (occupant && occupant.troops > 0 && occupant.faction !== unit.faction) {
            continue;
          }"""

pattern_bfs_wall = r"// 호로관 관문\(3\)은 아군 직접 진입 불가[\s\S]*?continue;\s*\}"
text = re.sub(pattern_bfs_wall, bfs_wall_check, text)

# 이동 클릭 시 군량고 도달 검사 좌표 (적 군량고: destTerrain === 4, 아군: destTerrain === 8)
# 이미 destTerrain === 4 및 destTerrain === 8로 체크하고 있으므로 13열 맵에서도 100% 자동 적용됨!

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

print("ALL LARGE BATTLEFIELD & CASTLE GATES COMPLETED!")
