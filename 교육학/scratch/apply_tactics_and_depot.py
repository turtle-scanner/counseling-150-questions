# -*- coding: utf-8 -*-
import os
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. 무장 데이터 수정: 여포, 손책 레벨 10 시작 및 황충 특기 강화
# ==============================================================================
print("1. Updating Officers (Lv.10 Lu Bu, Sun Ce & Hwang Chung archer)...")

# 여포 Lv.10 설정
text = re.sub(
    r"\{\s*name:\s*'여포 \(봉선\)'[\s\S]*?\}",
    "{ name: '여포 (봉선)', war: 100, int: 45, lead: 86, icon: '👹', title: '천하무쌍 비장', faceKey: 'lubu', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)', level: 10, exp: 1500, troopType: 'royal', troopName: '친위병 (천하무쌍)' }",
    text
)

# 손책 Lv.10 설정
text = re.sub(
    r"\{\s*name:\s*'손책 \(백부\)'[\s\S]*?\}",
    "{ name: '손책 (백부)', war: 92, int: 70, lead: 92, icon: '🐅', title: '소패왕', faceKey: 'sunce', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)', level: 10, exp: 1500, troopType: 'royal', troopName: '친위병 (소패왕 돌격대)' }",
    text
)

# MY_OFFICERS 황충 신궁 특화
text = re.sub(
    r"\{\s*id:\s*'huang_zhong'[\s\S]*?\}",
    "{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장 (신궁)', hp: 100, fatigue: 0, element: 'fire', elemIcon: '🔥', elemName: '불 (火 - 화시)', level: 3, exp: 200, troopType: 'archer', troopName: '정예궁병 (신궁)' }",
    text
)

# ==============================================================================
# 2. 6대 지역 전장 지형 맵: 아군 군량고(타일 8) 배치
# ==============================================================================
print("2. Updating REGIONAL_MAPS: adding Ally Depot (tile 8 at (0, 2))...")

# REGIONAL_MAPS 내 6개 프리셋의 terrain[2][0]을 8로 변경
# plains: [1, 0, 0, 1, 0, 0, 1, 0, 0] -> [8, 0, 0, 1, 0, 0, 1, 0, 0]
# mountain: [0, 0, 2, 0, 0, 2, 0, 0, 0] -> [8, 0, 2, 0, 0, 2, 0, 0, 0]
# water: [0, 0, 0, 5, 5, 5, 0, 1, 0] -> [8, 0, 0, 5, 5, 5, 0, 1, 0]
# fortress: [0, 0, 1, 0, 0, 3, 3, 0, 7] -> [8, 0, 1, 0, 0, 3, 3, 0, 7]
# hyeongju: [0, 0, 1, 0, 5, 0, 1, 0, 0] -> [8, 0, 1, 0, 5, 0, 1, 0, 0]
# jungle: [0, 0, 1, 0, 6, 6, 0, 0, 0] -> [8, 0, 1, 0, 6, 6, 0, 0, 0]

regional_maps_replacement = """REGIONAL_MAPS = {
      // 1. 하북 대평원 (유주 1, 기주 2, 청주 3, 연주 4)
      'plains': {
        name: '하북 대평원',
        desc: '광활한 평야와 듬성한 숲. 기병 돌격과 일화계가 맹위를 떨칩니다!',
        terrain: [
          [0, 1, 0, 0, 7, 0, 0, 1, 0], // (4, 0) 전설의 보물 사당!
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [8, 0, 0, 1, 0, 0, 1, 0, 0], // (0, 2) 🌾 아군 군량고!
          [0, 0, 0, 0, 0, 0, 0, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '적토마 (赤兎馬)', stat: '무력 +5, 기동력 +1칸', type: 'war', val: 5 }
      },
      // 2. 서촉 험산 협곡 (익주 10, 양주 11, 병주 12)
      'mountain': {
        name: '서촉 험산 협곡',
        desc: '좁은 협곡과 거친 암벽. 원거리 궁시와 기습 복병에 유리합니다!',
        terrain: [
          [2, 2, 0, 0, 0, 2, 2, 2, 2],
          [2, 0, 0, 7, 2, 2, 0, 0, 2], // (3, 1) 협곡 비밀 동굴!
          [8, 0, 2, 0, 0, 2, 0, 0, 0], // (0, 2) 🌾 아군 군량고!
          [0, 2, 0, 0, 0, 0, 2, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 2, 2, 0, 0, 2, 2, 0, 0],
          [2, 0, 0, 0, 2, 0, 0, 2, 0],
          [2, 2, 0, 0, 0, 0, 2, 2, 2]
        ],
        treasure: { name: '장팔사모 (丈八蛇矛)', stat: '무력 +7 영구 상승', type: 'war', val: 7 }
      },
      // 3. 강동 적벽 수향 수로 (양주 7, 서주 5, 예주 6)
      'water': {
        name: '강동 적벽 수향 수로',
        desc: '거대한 장강과 미로 같은 수로. 수군 화공과 배후 기습이 승패를 가릅니다!',
        terrain: [
          [0, 1, 5, 5, 0, 0, 1, 0, 0],
          [1, 0, 5, 5, 5, 0, 0, 0, 0],
          [8, 0, 0, 5, 5, 5, 0, 1, 0], // (0, 2) 🌾 아군 군량고!
          [0, 1, 0, 0, 5, 5, 5, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 0, 1, 0, 0, 5, 5, 7, 0], // (7, 4) 침몰 보물선!
          [1, 0, 0, 1, 0, 0, 5, 5, 0],
          [0, 0, 0, 0, 1, 0, 0, 5, 0]
        ],
        treasure: { name: '손자병법서 (孫子兵法)', stat: '지력 +8, 통솔 +6', type: 'int', val: 8 }
      },
      // 4. 중원 낙양 호로관 관문 (사례교위부 13)
      'fortress': {
        name: '중원 낙양 호로관 관문',
        desc: '철옹성 호로관 성벽과 거대 망루. 관문 방어선 돌파가 관건입니다!',
        terrain: [
          [0, 1, 0, 0, 0, 2, 2, 2, 0],
          [1, 0, 0, 0, 2, 2, 3, 2, 0],
          [8, 0, 1, 0, 0, 3, 3, 0, 7], // (0, 2) 🌾 아군 군량고! / (8, 2) 황실 비고!
          [0, 0, 0, 0, 0, 3, 0, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '의천검 (倚天劍)', stat: '무력 +8 영구 상승', type: 'war', val: 8 }
      },
      // 5. 형주 신야 복합 수륙 (형주 8)
      'hyeongju': {
        name: '형주 신야 복합 수륙 전장',
        desc: '평야, 수로, 숲이 뒤엉킨 천혜의 요충지. 진형과 풍향을 읽어야 승리합니다!',
        terrain: [
          [0, 7, 1, 0, 0, 5, 0, 1, 0], // (1, 0) 와룡선생 사당!
          [1, 0, 0, 0, 5, 5, 0, 0, 0],
          [8, 0, 1, 0, 5, 0, 1, 0, 0], // (0, 2) 🌾 아군 군량고!
          [0, 5, 5, 5, 0, 0, 0, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 1, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '청룡언월도 (靑龍偃月刀)', stat: '무력 +8, 통솔 +5', type: 'war', val: 8 }
      },
      // 6. 남월 교주 밀림 늪지대 (교주 9)
      'jungle': {
        name: '남월 교주 밀림 맹독 늪지대',
        desc: '독안개와 맹독 늪. 이동마다 체력 손실에 주의해야 합니다!',
        terrain: [
          [1, 6, 6, 1, 0, 0, 1, 6, 0],
          [6, 1, 0, 6, 6, 0, 0, 1, 0],
          [8, 0, 1, 0, 6, 6, 0, 0, 0], // (0, 2) 🌾 아군 군량고!
          [1, 0, 0, 0, 0, 6, 1, 0, 4], // (8, 3) 🌾 적 군량고!
          [0, 6, 1, 0, 0, 0, 6, 7, 0], // (7, 4) 남만 비밀 성소!
          [6, 1, 0, 1, 6, 0, 0, 6, 0],
          [0, 0, 6, 0, 1, 6, 0, 0, 0]
        ],
        treasure: { name: '옥새 (玉璽)', stat: '매력 +10 영구 상승', type: 'int', val: 10 }
      }
    };"""

text = re.sub(r"REGIONAL_MAPS\s*=\s*\{[\s\S]*?\n\s*\};", regional_maps_replacement, text)

# ==============================================================================
# 3. 출전 부대 수 시스템: Lv.1~9(3부대), Lv.10~19(4부대), Lv.20~49(5부대), Lv.50+(6부대)
# ==============================================================================
print("3. Implementing Deploy Scaling (getMaxDeployableCount) & Modal...")

deploy_scale_code = """
    // ==========================================================================
    // 🚩 출전 군단 규모 규칙: Lv.1~9(3부대) / Lv.10~19(4부대) / Lv.20~49(5부대) / Lv.50+(6부대)
    // ==========================================================================
    function getMaxDeployableCount() {
      const maxLvl = Math.max(
        ...MY_OFFICERS.map(o => o.level || 1),
        gameState.troopLevel || 1,
        1
      );
      if (maxLvl >= 50) return 6;
      if (maxLvl >= 20) return 5;
      if (maxLvl >= 10) return 4;
      return 3;
    }

    function openOfficerDeployModal(target, fromProv, isDefense = false) {
      closeAllPopups();
      deployingTargetProv = target;
      deployingFromProv = fromProv;
      isDeployDefense = isDefense;
      selectedDeployOfficerIds = [];

      const maxAllowed = getMaxDeployableCount();

      // 기본적으로 피로도 70% 미만인 장수 최대 maxAllowed명 자동 선택
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        if (off.fatigue < 70 && selectedDeployOfficerIds.length < maxAllowed) {
          selectedDeployOfficerIds.push(off.id);
        }
      });

      const maxLvl = Math.max(...MY_OFFICERS.map(o => o.level || 1), 1);
      const titleEl = document.getElementById('deploy-modal-title');
      const descEl = document.getElementById('deploy-target-desc');
      if (isDefense) {
        titleEl.innerText = `[방어 출전 편성] ${target.name} 방어전 (최대 ${maxAllowed}부대 출전 가능!)`;
        descEl.innerText = `침공해온 ${target.attackerRuler || target.ruler}군을 격퇴할 요격 장수를 선발하십시오. (최고 Lv.${maxLvl})`;
      } else {
        titleEl.innerText = `[출전 장수 편성] ${fromProv.name} ➔ ${target.name} 침공 (최대 ${maxAllowed}부대 편성!)`;
        descEl.innerText = `목표: ${target.id}. ${target.name} (${target.ruler}군) | 아군 최고 Lv.${maxLvl} (Lv.10: 4부대, Lv.20: 5부대, Lv.50: 6부대)`;
      }

      renderDeployOfficerList();
      openModal('officer-deploy-modal');
    }

    function renderDeployOfficerList() {
      const container = document.getElementById('deploy-officer-list');
      if (!container) return;

      const maxAllowed = getMaxDeployableCount();
      const maxLvl = Math.max(...MY_OFFICERS.map(o => o.level || 1), 1);

      // 상단 출전 규모 및 5대 속성 상성 안내 바 동적 주입
      const elemGuideHeader = `
        <div class="col-span-1 md:col-span-2 bg-slate-950/95 border-2 border-yellow-500/80 p-3 rounded-lg text-xs text-slate-200 mb-2 shadow-xl">
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-yellow-500/30">
            <span class="font-black text-amber-300 text-sm flex items-center gap-1.5">
              <span>🚩 [출전 군단 규모]</span>
              <span class="text-white bg-amber-600 px-2 py-0.5 rounded text-[11px]">최고 Lv.${maxLvl} 달성</span>
              <span class="text-yellow-300">➔ 최대 ${maxAllowed}개 부대 출전 가능!</span>
            </span>
            <span class="text-[11px] text-cyan-300 font-bold">선택: ${selectedDeployOfficerIds.length} / ${maxAllowed}부대</span>
          </div>
          <div class="text-[11px] text-slate-300 mb-2">
            ※ <strong>출전 해금 기준:</strong> Lv.1~9 (3부대) ➔ <span class="text-yellow-300 font-bold">Lv.10 (4부대)</span> ➔ <span class="text-cyan-300 font-bold">Lv.20 (5부대)</span> ➔ <span class="text-purple-300 font-bold">Lv.50 (6부대 대군단)</span>
          </div>
          <div class="font-black text-yellow-300 flex items-center justify-between mb-1.5">
            <span>🔮 5대 부대 속성 상성 (우세 시 대미지 +50% 극딜 폭발!)</span>
            <span class="text-[10px] text-cyan-300">적 세력 속성에 맞추어 출전시키십시오!</span>
          </div>
          <div class="grid grid-cols-5 gap-1.5 text-center text-[10px] font-bold">
            <div class="bg-blue-950/90 p-1.5 rounded border border-blue-500 text-cyan-200">💧 물 (손권)<br><span class="text-[9px] text-yellow-300">▶ 불(🔥) 격파</span></div>
            <div class="bg-red-950/90 p-1.5 rounded border border-red-500 text-red-200">🔥 불 (원소/공손)<br><span class="text-[9px] text-yellow-300">▶ 나무(🌲) 격파</span></div>
            <div class="bg-emerald-950/90 p-1.5 rounded border border-emerald-500 text-emerald-200">🌲 나무 (촉한)<br><span class="text-[9px] text-yellow-300">▶ 땅(⛰️) 격파</span></div>
            <div class="bg-amber-950/90 p-1.5 rounded border border-amber-500 text-amber-200">⛰️ 땅 (중원 육군)<br><span class="text-[9px] text-yellow-300">▶ 물(💧)/바람(🌪️)</span></div>
            <div class="bg-purple-950/90 p-1.5 rounded border border-purple-500 text-purple-200">🌪️ 바람 (서량 기병)<br><span class="text-[9px] text-yellow-300">▶ 물(💧) 격파</span></div>
          </div>
        </div>
      `;

      container.innerHTML = elemGuideHeader + MY_OFFICERS.map(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        const isExhausted = (off.fatigue >= 70);
        const isSelected = selectedDeployOfficerIds.includes(off.id);
        const offLvl = off.level || 1;
        const offTroopName = off.troopName || '보병';

        let statusBadge = '<span class="px-2 py-0.5 rounded text-[10px] bg-emerald-950 border border-emerald-500 text-emerald-300 font-bold">🟢 쾌조</span>';
        if (off.fatigue >= 70) {
          statusBadge = '<span class="px-2 py-0.5 rounded text-[10px] bg-red-950 border border-red-500 text-red-300 font-black animate-pulse">🔴 탈진</span>';
        } else if (off.fatigue >= 35) {
          statusBadge = '<span class="px-2 py-0.5 rounded text-[10px] bg-amber-950 border border-amber-500 text-amber-300 font-bold">🟡 보통</span>';
        }

        const cardBorder = isExhausted
          ? 'border-red-900/60 bg-slate-950/90 opacity-60 cursor-not-allowed'
          : (isSelected ? 'border-yellow-400 bg-amber-950/80 ring-2 ring-yellow-400 cursor-pointer shadow-lg' : 'border-blue-700 bg-blue-950/80 hover:border-yellow-400 cursor-pointer');

        return `
          <div onclick="toggleDeployOfficer('${off.id}')" class="p-2.5 rounded-lg border-2 transition flex items-center justify-between ${cardBorder}">
            <div class="flex items-center gap-2.5">
              <span class="text-3xl">${off.icon || '⚔️'}</span>
              <div class="space-y-0.5">
                <div class="flex items-center gap-2">
                  <span class="font-black text-xs text-white">${off.name}</span>
                  <span class="px-1.5 py-0.5 rounded text-[10px] bg-amber-900 border border-amber-400 text-yellow-300 font-bold">Lv.${offLvl} ${offTroopName}</span>
                  <span class="px-1.5 py-0.5 rounded text-[10px] bg-slate-900 border border-blue-400 text-cyan-300 font-bold">${off.elemIcon || '⛰️'} ${off.elemName || '땅 (土)'}</span>
                  ${statusBadge}
                </div>
                <div class="text-[11px] text-yellow-300">
                  무력: <strong>${off.war}</strong> | 지력: <strong>${off.int}</strong> | 통솔: <strong>${off.lead || 80}</strong>
                  ${off.name.includes('황충') ? '<span class=\"ml-1 text-red-400 font-bold\">[🏹신궁/화시 특화]</span>' : ''}
                </div>
                <div class="text-[10px] text-slate-300">
                  ${off.title || '용맹한 장수'} (피로도: ${off.fatigue || 0}%)
                </div>
              </div>
            </div>
            <div class="text-right">
              ${isSelected ? '<span class=\"px-3 py-1 bg-yellow-500 text-slate-950 font-black rounded text-xs shadow\">✓ 출전 선발</span>' : '<span class=\"px-3 py-1 bg-slate-800 text-slate-300 border border-slate-600 rounded text-xs\">선택</span>'}
            </div>
          </div>
        `;
      }).join('');
    }

    function toggleDeployOfficer(offId) {
      const off = MY_OFFICERS.find(o => o.id === offId);
      if (!off) return;
      if (off.fatigue >= 70) {
        alert(`⚠️ [출전 불가] ${off.name}은(는) 피로도(${off.fatigue}%)가 너무 높아 출전할 수 없습니다!\\n[0. 휴양]을 하거나 포상을 베풀어 피로도를 회복시키십시오.`);
        return;
      }

      const maxAllowed = getMaxDeployableCount();
      const maxLvl = Math.max(...MY_OFFICERS.map(o => o.level || 1), 1);

      if (selectedDeployOfficerIds.includes(offId)) {
        selectedDeployOfficerIds = selectedDeployOfficerIds.filter(id => id !== offId);
      } else {
        if (selectedDeployOfficerIds.length >= maxAllowed) {
          alert(`💡 현재 최고 레벨(Lv.${maxLvl}) 기준 최대 ${maxAllowed}명까지만 선택할 수 있습니다.\\n\\n▶ Lv.10 달성 시: 4개 부대\\n▶ Lv.20 달성 시: 5개 부대\\n▶ Lv.50 달성 시: 6개 부대 출전 가능!`);
          return;
        }
        selectedDeployOfficerIds.push(offId);
      }
      playSfx('select');
      renderDeployOfficerList();
    }
"""

# openOfficerDeployModal부터 confirmOfficerDeployment 직전까지 치환
pattern_deploy = r"function openOfficerDeployModal[\s\S]*?function confirmOfficerDeployment"
match_deploy = re.search(pattern_deploy, text)
if match_deploy:
    text = text[:match_deploy.start()] + deploy_scale_code.strip() + "\n\n    function confirmOfficerDeployment" + text[match_deploy.end():]
    print("  -> Deploy Scale functions successfully replaced!")
else:
    print("  -> ERROR: pattern_deploy not matched!")

# ==============================================================================
# 4. 헥스 전장 초기화: 6부대 좌표, 적 군량고 수비병(role: 'guard_depot') & 기습병(role: 'raider')
# ==============================================================================
print("4. Updating initHexBattleUnits (6 ally slots, enemy depot guard & raider)...")

init_units_code = """
    function initHexBattleUnits(targetProv, fromProv, deployedOfficers = []) {
      const maxAllowed = getMaxDeployableCount();

      // 1. 아군 유닛 세팅 (사용자가 선발한 장수들, 최대 6명)
      const allyOfficers = (deployedOfficers && deployedOfficers.length > 0)
        ? deployedOfficers
        : MY_OFFICERS.filter(o => (o.fatigue || 0) < 70).slice(0, maxAllowed);

      if (allyOfficers.length === 0) {
        allyOfficers.push(MY_OFFICERS[0]);
      }

      // 최대 6개 부대 안정적 포진 좌표 (본진 좌측)
      const allyPositions = [
        { q: 1, r: 4, form: 'gyorin' },    // 1번 선봉 중앙
        { q: 1, r: 5, form: 'bongsi' },    // 2번 남쪽 돌파
        { q: 0, r: 3, form: 'chuhaeng' },  // 3번 북쪽 기동
        { q: 0, r: 4, form: 'bangwon' },   // 4번 본진 중앙 수호 (Lv.10 해금)
        { q: 1, r: 3, form: 'anhaeng' },   // 5번 후방 원거리 지원 (Lv.20 해금)
        { q: 0, r: 5, form: 'gyorin' }     // 6번 남익 후위 호위 (Lv.50 해금)
      ];

      const soldierTotal = fromProv ? fromProv.soldiers : 20000;
      const soldierPerUnit = Math.floor(soldierTotal / Math.max(1, allyOfficers.length));

      const allyUnits = allyOfficers.map((off, idx) => {
        const pos = allyPositions[idx % allyPositions.length];
        const isHwang = off.name.includes('황충');
        const defaultSkills = isHwang
          ? ['신궁', '화시', '돌격', '분기']
          : (off.war >= 95 ? ['천하무쌍', '돌격', '분기', '일기토'] : (off.int >= 80 ? ['화계', '혼란', '고무', '수습'] : ['돌격', '분기', '화시']));

        return {
          id: off.id,
          faction: 'ally',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: off.title,
          avatar: off.icon || '⚔️',
          element: off.element || 'earth',
          elemIcon: off.elemIcon || '⛰️',
          elemName: off.elemName || '땅 (土)',
          level: off.level || 1,
          troopType: off.troopType || 'infantry',
          troopName: off.troopName || '보병',
          war: off.war,
          int: off.int,
          lead: off.lead || 85,
          chr: 85,
          troops: Math.min(10000, Math.max(3000, soldierPerUnit)),
          maxTroops: Math.min(10000, Math.max(3000, soldierPerUnit)),
          morale: 100,
          formation: isHwang ? 'anhaeng' : pos.form,
          availableFormations: ['gyorin', 'bongsi', 'bangwon', 'chuhaeng', 'anhaeng'],
          skills: defaultSkills,
          arcRange: isHwang ? 4 : (pos.form === 'anhaeng' ? 3 : 1),
          q: pos.q,
          r: pos.r,
          moved: false,
          acted: false
        };
      });

      // 2. 적군 유닛 세팅 (군량고 수비병 1명 + 아군 군량고 기습병 1명 + 본대 2~3명)
      const enemyRuler = targetProv ? targetProv.ruler : '동탁';
      const enemyOffList = (ENEMY_OFFICERS_BY_RULER[enemyRuler] || [
        { name: targetProv ? targetProv.leader : '적 수비대장', war: 86, int: 70, lead: 84, icon: '🛡️', title: '영지 수비대장' },
        { name: targetProv ? (targetProv.advisor || '참모 도위') : '참모', war: 75, int: 80, lead: 75, icon: '📜', title: '참모 도위' }
      ]).slice();

      // 만약 적 장수가 부족하면 추가
      if (enemyOffList.length < 4) {
        enemyOffList.push({ name: '군량도위 (보급대장)', war: 82, int: 65, lead: 84, icon: '🛡️', title: '군량고 철통 수비장수', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土)' });
        enemyOffList.push({ name: '돌격부장 (기습대)', war: 85, int: 50, lead: 78, icon: '🐎', title: '우회 기습 부장', element: 'wind', elemIcon: '🌪️', elemName: '바람 (風)' });
      }

      // 적 포진: 0번은 보스, 1번은 본대전투, 2번은 기습병(raider), 마지막은 군량고 수비병(guard_depot)
      const enemyPositions = [
        { q: 6, r: 3, form: 'bongsi', role: 'assault' },       // 적 보스 돌격
        { q: 6, r: 4, form: 'gyorin', role: 'assault' },       // 적 본대 보조
        { q: 5, r: 1, form: 'chuhaeng', role: 'raider' },      // 🐎 아군 군량고(0, 2) 우회 기습 부대!
        { q: 7, r: 3, form: 'bangwon', role: 'guard_depot' }   // 🛡️ 적 군량고(8, 3) 바로 앞 철통 수비대장!
      ];

      const enemyTotal = targetProv ? targetProv.soldiers : 24000;
      const enemySoldierPerUnit = Math.floor(enemyTotal / Math.max(1, enemyPositions.length));

      const enemyUnits = enemyPositions.map((posCfg, idx) => {
        const off = enemyOffList[idx % enemyOffList.length];
        const isDepotGuard = (posCfg.role === 'guard_depot');
        const isRaider = (posCfg.role === 'raider');
        const isBoss = (idx === 0);

        let unitTitle = off.title || '적군 맹장';
        if (isDepotGuard) unitTitle = '🛡️ [군량고 철통수비대장]';
        else if (isRaider) unitTitle = '🐎 [아군 군량고 우회기습대]';

        const offLvl = (off.name.includes('여포') || off.name.includes('손책')) ? 10 : (off.level || (isBoss ? 5 : 2));

        return {
          id: `enemy_${idx}`,
          faction: 'enemy',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: unitTitle,
          avatar: off.icon || (isDepotGuard ? '🛡️' : '👹'),
          element: off.element || (enemyRuler.includes('손') ? 'water' : (enemyRuler.includes('마') ? 'wind' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? 'fire' : 'earth'))),
          elemIcon: off.elemIcon || (enemyRuler.includes('손') ? '💧' : (enemyRuler.includes('마') ? '🌪️' : ([1,2,3,4].includes(targetProv ? targetProv.id : 1) ? '🔥' : '⛰️'))),
          elemName: off.elemName || '적 부대 속성',
          level: offLvl,
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          chr: 70,
          isBoss: isBoss,
          role: posCfg.role, // 'guard_depot', 'raider', 'assault'
          troops: Math.min(10000, Math.max(3000, enemySoldierPerUnit)),
          maxTroops: Math.min(10000, Math.max(3000, enemySoldierPerUnit)),
          morale: 100,
          formation: posCfg.form,
          availableFormations: ['gyorin', 'bongsi', 'bangwon', 'chuhaeng', 'anhaeng'],
          skills: off.war >= 95 ? ['천하무쌍', '돌격', '분기'] : ['돌격', '화계', '혼란'],
          q: posCfg.q,
          r: posCfg.r,
          moved: false,
          acted: false
        };
      });

      UNITS = [...allyUnits, ...enemyUnits];
      sam5BattleState.allySupplyBurned = false; // 아군 군량고 초기화
      sam5BattleState.supplyBurned = false;     // 적 군량고 초기화
    }
"""

pattern_init = r"function initHexBattleUnits[\s\S]*?UNITS\s*=\s*\[\.\.\.allyUnits,\s*\.\.\.enemyUnits\];\s*\}"
match_init = re.search(pattern_init, text)
if match_init:
    text = text[:match_init.start()] + init_units_code.strip() + text[match_init.end():]
    print("  -> initHexBattleUnits successfully replaced!")
else:
    print("  -> ERROR: pattern_init not matched!")

# ==============================================================================
# 5. 아군/적 군량고 피습 및 소각 함수 정의
# ==============================================================================
print("5. Defining Depot Raid & Defense mechanics...")

depot_raid_code = """
    // ==========================================================================
    // 🌾 적 군량고 습격 및 아군 군량고 피습 처리
    // ==========================================================================
    function triggerSupplyRaid(hero) {
      if (sam5BattleState.supplyBurned) return;
      sam5BattleState.supplyBurned = true;
      logBattle(`🌾💥 [전략 대성공!] ${hero.name} 부대가 적의 군량고를 기습 점령 및 불태웠습니다! 적군 전원 패닉 & 사기 급락!`);
      playSound('fire');

      // 적 전군 사기 25로 추락 및 병력 25% 이탈
      UNITS.filter(u => u.faction === "enemy" && u.troops > 0).forEach(enemy => {
        enemy.morale = Math.max(15, enemy.morale - 45);
        const lost = Math.floor(enemy.troops * 0.25);
        enemy.troops -= lost;
        showDamagePop(enemy.q, enemy.r, `군량소실! -${lost}`);
      });

      logMessage(`🔥 [적 군량고 점령 소각!] ${hero.name} 장군이 적의 후방 보급창을 궤멸시켜 적 전군이 패닉에 빠졌습니다!`, 'text-yellow-300 font-extrabold text-sm');
      gainTroopExp(50, '적 군량고 소각 기습 대성공');
      alert(`🌾💥 [전략 대성공! 적 군량고 기습 소각!]\n\n${hero.name} 부대가 적의 후방 군량고를 기습하여 잿더미로 만들었습니다!\n\n▶ 적 전군 패닉: 사기 급락 (-45) & 병력 25% 즉시 탈영!\n▶ 매 턴 적군 추가 탈영 발생! 승기를 잡았습니다!`);
    }

    function triggerAllySupplyRaid(enemyUnit) {
      if (sam5BattleState.allySupplyBurned) return;
      sam5BattleState.allySupplyBurned = true;
      logBattle(`🚨💥 [비보! 본진 군량고 피습!] 적장 ${enemyUnit.name} 부대가 아군의 본진 보급창(군량고)을 기습 점령 소각했습니다!`);
      playSound('fire');

      // 아군 전 부대 사기 급락 & 패닉
      UNITS.filter(u => u.faction === "ally" && u.troops > 0).forEach(ally => {
        ally.morale = Math.max(15, ally.morale - 40);
        showDamagePop(ally.q, ally.r, "🚨군량고 소각! 사기-40");
      });

      logMessage(`🚨 [비상! 아군 군량고 소각!] 적 기습부대에게 본진 보급창을 빼앗겼습니다! 매 턴 군량 결핍 탈영 발생!`, 'text-red-400 font-extrabold text-sm');
      alert(`🚨 [비상! 아군 군량고 피습 소각!]\n\n적 기습부대 ${enemyUnit.name}이 아군의 본진 보급창(군량고)을 점령하고 불태웠습니다!\n\n▶ 아군 전군 패닉: 사기 급락 (-40)!\n▶ 매 턴 보급 차단으로 병력 15% 탈영 손실 발생!\n▶ 10턴 내로 적 본대를 섬멸하지 못하면 전군 와해됩니다!`);
    }
"""

pattern_raid = r"function triggerSupplyRaid[\s\S]*?alert\([^\)]*?\);\s*\}"
match_raid = re.search(pattern_raid, text)
if match_raid:
    text = text[:match_raid.start()] + depot_raid_code.strip() + text[match_raid.end():]
    print("  -> triggerSupplyRaid & triggerAllySupplyRaid successfully added!")
else:
    print("  -> ERROR: pattern_raid not matched!")

# ==============================================================================
# 6. 바둑의 원리 (3면 포위 일제합공) & 적 포위 시 훨씬 강하게 이김 & 황충 화살/불화살
# ==============================================================================
print("6. Implementing Go (圍棋) 3-side Encirclement, Surrounding Bonus & Hwang Chung Archery...")

tactics_code = """
    // ==========================================================================
    // ⬛⬜ 바둑의 원리: 대상 유닛에 인접(거리 1)한 우군 부대 목록 반환
    // ==========================================================================
    function getSurroundingUnits(targetUnit, friendlyFaction) {
      if (!targetUnit) return [];
      return UNITS.filter(u => 
        u.faction === friendlyFaction &&
        u.troops > 0 &&
        getHexDistance(u.q, u.r, targetUnit.q, targetUnit.r) === 1
      );
    }

    // 황충 화살부대 특화 및 전술 군령 버튼 갱신
    function updateActionCommands() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.faction !== "ally" || u.acted || sam5BattleState.phase !== "ally") {
        disableAllCommands();
        return;
      }

      const isHwang = u.name.includes('황충');
      const form = FORMATIONS[u.formation];
      const adjEnemies = getEnemiesInRange(u, 1);
      
      // 황충은 진형 무관 초장거리 사거리 4칸 궁시 가능! 일반 안행진은 3칸
      const arcRange = isHwang ? 4 : (form ? form.arcRange : 1);
      const arcEnemies = getEnemiesInRange(u, arcRange);

      const btnAtk = document.getElementById("btnAttack");
      const btnArc = document.getElementById("btnArchery");
      const btnFire = document.getElementById("btnFireSkill");
      const btnChaos = document.getElementById("btnChaosSkill");
      const btnFlurry = document.getElementById("btnFlurry");
      const btnForm = document.getElementById("btnFormation");
      const btnDuel = document.getElementById("btnDuel");
      const btnWait = document.getElementById("btnWait");

      // 바둑 3면 포위 가능 적 검사
      const canEncircle3 = adjEnemies.some(e => getSurroundingUnits(e, 'ally').length >= 3);

      if (btnAtk) {
        btnAtk.disabled = adjEnemies.length === 0;
        if (canEncircle3) {
          btnAtk.innerHTML = '<span class="text-yellow-300 animate-pulse font-black">⚡ 3면포위 일제합공!</span>';
          btnAtk.className = "px-3 py-2 rounded bg-amber-600 hover:bg-amber-500 border-2 border-yellow-300 text-white font-black text-xs shadow-lg transition";
        } else {
          btnAtk.innerHTML = '🗡️ 근접 공격';
          btnAtk.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border border-blue-500 text-white font-bold text-xs shadow transition";
        }
      }

      if (btnArc) {
        if (isHwang) {
          btnArc.disabled = (arcEnemies.length === 0);
          btnArc.innerHTML = '🏹 황충 신궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-emerald-800 hover:bg-emerald-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else {
          btnArc.disabled = arcEnemies.length === 0 || arcRange < 2;
          btnArc.innerHTML = '🏹 안행 궁시';
          btnArc.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      if (btnFire) {
        if (isHwang) {
          btnFire.disabled = (arcEnemies.length === 0);
          btnFire.innerHTML = '🔥 황충 맹화시 (불화살)';
          btnFire.className = "px-3 py-2 rounded bg-red-800 hover:bg-red-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else {
          btnFire.disabled = !u.skills.includes("화계") && u.int < 75;
          btnFire.innerHTML = '🔥 화계 (풍향확산)';
          btnFire.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold text-xs shadow transition";
        }
      }

      if (btnChaos) btnChaos.disabled = !u.skills.includes("혼란") && u.int < 80;
      if (btnFlurry) btnFlurry.disabled = !u.skills.includes("분기") || adjEnemies.length === 0;
      if (btnForm) btnForm.disabled = false;
      if (btnDuel) btnDuel.disabled = adjEnemies.length === 0;
      if (btnWait) btnWait.disabled = false;
    }

    // ==========================================================================
    // 전투 액션 실행: 바둑의 원리 3면 포위 일제합공 & 황충 화살/불화살 연동
    // ==========================================================================
    function executeSkillAction(mode, targetPos) {
      const u = sam5BattleState.selectedUnit;
      const targetUnit = findUnitAt(targetPos.q, targetPos.r);
      const isHwang = u.name.includes('황충');

      if (mode === 'attack' && targetUnit) {
        // ⬛⬜ 바둑의 원리 및 포위망 검사
        const surroundingAllies = getSurroundingUnits(targetUnit, u.faction);
        const surroundCount = surroundingAllies.length; // 공격자 포함 인접 우군 수

        const adv = getElementAdvantage(u.element, targetUnit.element);
        let dmg = calculateCombatDamage(u, targetUnit, 'melee');

        if (surroundCount >= 3) {
          // ⬛⬜ 바둑의 원리: 3면 포위 일제합공 (활로 차단 극딜 300% & 적 반격 불가!)
          dmg = Math.floor(dmg * 2.8);
          logBattle(`⬛⬜⚡ [바둑의 3면 포위 일제합공 (圍棋 一齊攻擊)!]`);
          logBattle(`적장 ${targetUnit.name}의 3대 활로(숨구멍)를 완벽 차단! 포위한 [${surroundingAllies.map(a => a.name).join(', ')}] 부대가 일제히 쇄도하여 ${dmg.toLocaleString()} 섬멸 치명타를 가했습니다!`);
          playSound('fanfare');
          playSound('slash');
          showDamagePop(targetUnit.q, targetUnit.r, `⚡3면포위 일제공격! -${dmg}`);
          targetUnit.morale = Math.max(10, targetUnit.morale - 40);
          targetUnit.acted = true; // 혼란 행동불능

          applyDamage(targetUnit, dmg);
          surroundingAllies.forEach(a => gainTroopExp(30, '3면 포위 일제공격'));
          gainTroopExp(35, '바둑의 포위 섬멸 대승');
        } else if (surroundCount === 2) {
          // ⚔️ 2면 협공 (Pincer Attack: 대미지 +50% & 적 반격 절반)
          dmg = Math.floor(dmg * 1.5);
          logBattle(`⚔️🔥 [양면 협공!] 2개 부대가 적장 ${targetUnit.name}을 협공하여 ${dmg.toLocaleString()} 피해를 입혔습니다!`);
          playSound('slash');
          showDamagePop(targetUnit.q, targetUnit.r, `🔥협공! -${dmg}`);
          applyDamage(targetUnit, dmg);
          gainTroopExp(20, '양면 협공');

          if (targetUnit.troops > 0) {
            const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.35);
            applyDamage(u, counterDmg);
          }
        } else {
          // 일반 1:1 돌격 교전
          logBattle(`🗡️ ${u.name} 부대가 ${targetUnit.name}에게 돌격을 감행합니다!`);
          playSound('slash');
          applyDamage(targetUnit, dmg);
          gainTroopExp(15, '돌격 교전');

          if (adv.isAdv) {
            logBattle(adv.text);
            playSound('fanfare');
          } else if (adv.isDisadv) {
            logBattle(adv.text);
          }

          if (targetUnit.troops > 0) {
            const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.65);
            applyDamage(u, counterDmg);
          }
        }
      } else if (mode === 'archery' && targetUnit) {
        if (isHwang) {
          logBattle(`🏹🎯 [황충 백발백중 신궁 궁시!] 노장 황충의 철궁에서 뿜어진 화살이 ${targetUnit.name} 부대의 심장을 꿰뚫었습니다!`);
          playSound('arrow');
          const dmg = Math.floor(calculateCombatDamage(u, targetUnit, 'archery') * 1.45);
          applyDamage(targetUnit, dmg);
          showDamagePop(targetUnit.q, targetUnit.r, `🎯신궁 저격! -${dmg}`);
          gainTroopExp(25, '황충 신궁 저격 성공');
        } else {
          logBattle(`🏹 ${u.name} 부대의 화살비가 쏟아집니다!`);
          playSound('arrow');
          const dmg = calculateCombatDamage(u, targetUnit, 'archery');
          applyDamage(targetUnit, dmg);
          gainTroopExp(15, '궁시 지원');
        }
      } else if (mode === 'fire') {
        if (isHwang && targetUnit) {
          // 황충 전용 맹화시 (사거리 4칸 불화살 폭격)
          logBattle(`🔥🏹 [황충 맹화시(불화살) 폭격!] 황충의 불화살이 ${targetUnit.name} 부대 진영에 쏟아져 화염에 휩싸입니다!`);
          playSound('fire');
          const dmg = Math.floor(calculateCombatDamage(u, targetUnit, 'archery') * 1.65 + 800);
          applyDamage(targetUnit, dmg);
          sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });
          targetUnit.morale = Math.max(10, targetUnit.morale - 30);
          showDamagePop(targetUnit.q, targetUnit.r, `🔥맹화시! -${dmg}`);
          gainTroopExp(30, '황충 맹화시 불바다 성공');
        } else {
          logBattle(`🔥 [대화계] 불길이 거세게 치솟습니다! 남동풍을 타고 번져갑니다.`);
          playSound('fire');
          sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });
          gainTroopExp(25, '대화계 성공');
          if (targetUnit) {
            applyDamage(targetUnit, 1500);
            targetUnit.morale = Math.max(10, targetUnit.morale - 20);
          }
        }
      } else if (mode === 'chaos' && targetUnit) {
        const successRate = 55 + (u.int - targetUnit.int) * 2;
        if (Math.random() * 100 < successRate) {
          targetUnit.morale = Math.max(10, targetUnit.morale - 30);
          targetUnit.acted = true;
          gainTroopExp(25, '혼란 계략 성공');
          logBattle(`🌀 [혼란 대성공] ${targetUnit.name}의 군심이 무너져 행동 불능이 되었습니다!`);
          playSound('fanfare');
        } else {
          logBattle(`[혼란 실패] ${targetUnit.name}이 계략을 눈치챘습니다.`);
        }
      }

      finishUnitAction(u);
    }
"""

pattern_combat = r"function updateActionCommands[\s\S]*?function calculateCombatDamage"
match_combat = re.search(pattern_combat, text)
if match_combat:
    text = text[:match_combat.start()] + tactics_code.strip() + "\n\n    function calculateCombatDamage" + text[match_combat.end():]
    print("  -> updateActionCommands & executeSkillAction successfully replaced!")
else:
    print("  -> ERROR: pattern_combat not matched!")

# ==============================================================================
# 7. 적 AI 개선: 군량고 사수(guard_depot) & 아군 군량고 기습(raider) & 협공 로직
# ==============================================================================
print("7. Enhancing Enemy AI (Depot Guard & Raider for Ally Depot)...")

enemy_ai_code = """
    function runEnemyAI() {
      const enemies = UNITS.filter(u => u.faction === "enemy" && u.troops > 0);
      let step = 0;

      function executeNextEnemy() {
        if (step >= enemies.length || sam5BattleState.battleOver) {
          finishFullTurn();
          return;
        }

        const enemy = enemies[step];
        const allies = UNITS.filter(u => u.faction === "ally" && u.troops > 0);

        if (allies.length > 0) {
          // 🛡️ 1. 군량고 철통 수비대장 (role: 'guard_depot')
          if (enemy.role === 'guard_depot') {
            const depotQ = 8, depotR = 3;
            // 군량고 주변 2.5칸 이내에 아군이 침입했는지 감시
            const intruders = allies.filter(a => getHexDistance(a.q, a.r, depotQ, depotR) <= 2.5);

            if (intruders.length > 0) {
              // 침입한 아군 중 가장 가까운 자 요격
              let target = intruders[0];
              let minDist = getHexDistance(enemy.q, enemy.r, target.q, target.r);
              intruders.forEach(a => {
                const d = getHexDistance(enemy.q, enemy.r, a.q, a.r);
                if (d < minDist) { minDist = d; target = a; }
              });

              if (minDist === 1) {
                logBattle(`🛡️⚔️ [군량고 사수!] 적 수비장수 ${enemy.name}이 군량고에 침입한 ${target.name}에게 맹공을 퍼붓습니다!`);
                playSound('slash');
                const dmg = calculateCombatDamage(enemy, target, 'melee');
                applyDamage(target, dmg);
              } else {
                // 침입자를 가로막기 위해 이동
                const stepQ = enemy.q > target.q ? enemy.q - 1 : (enemy.q < target.q ? enemy.q + 1 : enemy.q);
                const stepR = enemy.r > target.r ? enemy.r - 1 : (enemy.r < target.r ? enemy.r + 1 : enemy.r);
                if (!findUnitAt(stepQ, stepR)) {
                  enemy.q = stepQ; enemy.r = stepR;
                  logBattle(`🛡️ 적 수비대장 ${enemy.name}이 군량고 방어선을 지키기 위해 요격에 나섰습니다.`);
                }
              }
            } else {
              // 침입자가 없으면 군량고 앞목(7, 3)을 굳건히 지키며 방원진 대기!
              if (enemy.q !== 7 || enemy.r !== 3) {
                const stepQ = enemy.q > 7 ? enemy.q - 1 : (enemy.q < 7 ? enemy.q + 1 : enemy.q);
                const stepR = enemy.r > 3 ? enemy.r - 1 : (enemy.r < 3 ? enemy.r + 1 : enemy.r);
                if (!findUnitAt(stepQ, stepR)) {
                  enemy.q = stepQ; enemy.r = stepR;
                }
              }
              enemy.formation = 'bangwon'; // 철통 방원진 유지
              logBattle(`🛡️ 적 수비대장 ${enemy.name}이 군량고 앞목을 철통 방원진으로 사수하고 있습니다!`);
            }
          }
          // 🐎 2. 아군 군량고 우회 기습부대 (role: 'raider')
          else if (enemy.role === 'raider' && !sam5BattleState.allySupplyBurned) {
            const allyDepotQ = 0, allyDepotR = 2;
            const distToAllyDepot = getHexDistance(enemy.q, enemy.r, allyDepotQ, allyDepotR);

            // 바로 인접한 아군이 있으면 먼저 공격
            const adjAllies = allies.filter(a => getHexDistance(enemy.q, enemy.r, a.q, a.r) === 1);
            if (adjAllies.length > 0 && Math.random() < 0.4) {
              const target = adjAllies[0];
              logBattle(`🐎 적 기습부대 ${enemy.name}이 진로를 가로막은 ${target.name}에게 기습 돌격을 감행합니다!`);
              playSound('slash');
              const dmg = calculateCombatDamage(enemy, target, 'melee');
              applyDamage(target, dmg);
            } else {
              // 아군 군량고(0, 2)를 향해 우회 쇄도!
              const stepQ = enemy.q > allyDepotQ ? enemy.q - 1 : (enemy.q < allyDepotQ ? enemy.q + 1 : enemy.q);
              const stepR = enemy.r > allyDepotR ? enemy.r - 1 : (enemy.r < allyDepotR ? enemy.r + 1 : enemy.r);

              if (stepQ === allyDepotQ && stepR === allyDepotR) {
                // 아군 군량고 점령 성공!
                enemy.q = stepQ; enemy.r = stepR;
                triggerAllySupplyRaid(enemy);
              } else if (!findUnitAt(stepQ, stepR)) {
                enemy.q = stepQ; enemy.r = stepR;
                logBattle(`🐎🚨 [적 기습 경보!] 적 기습부대 ${enemy.name}이 아군 본진 군량고를 노리고 우회 진격 중입니다!`);
              }
            }
          }
          // ⚔️ 3. 일반 적군 부대 (협공 및 전방 주력 교전)
          else {
            let closestAlly = null;
            let minDist = 999;
            allies.forEach(a => {
              const d = getHexDistance(enemy.q, enemy.r, a.q, a.r);
              if (d < minDist) { minDist = d; closestAlly = a; }
            });

            if (minDist === 1) {
              logBattle(`⚔️ 적장 ${enemy.name}이 ${closestAlly.name}에게 맹공을 퍼붓습니다!`);
              playSound('slash');
              const dmg = calculateCombatDamage(enemy, closestAlly, 'melee');
              applyDamage(closestAlly, dmg);
            } else {
              // 아군을 향해 진격
              const stepQ = enemy.q > closestAlly.q ? enemy.q - 1 : (enemy.q < closestAlly.q ? enemy.q + 1 : enemy.q);
              const stepR = enemy.r > closestAlly.r ? enemy.r - 1 : (enemy.r < closestAlly.r ? enemy.r + 1 : enemy.r);
              if (!findUnitAt(stepQ, stepR)) {
                enemy.q = stepQ; enemy.r = stepR;
                logBattle(`🏇 적군 ${enemy.name} 부대가 진형을 좁히며 쇄도합니다.`);
              }
            }
          }
        }

        enemy.acted = true;
        renderBattlefield();
        step++;
        setTimeout(executeNextEnemy, 550);
      }

      executeNextEnemy();
    }
"""

pattern_ai = r"function runEnemyAI[\s\S]*?function finishFullTurn"
match_ai = re.search(pattern_ai, text)
if match_ai:
    text = text[:match_ai.start()] + enemy_ai_code.strip() + "\n\n    function finishFullTurn" + text[match_ai.end():]
    print("  -> runEnemyAI successfully replaced with Depot Guard & Raider logic!")
else:
    print("  -> ERROR: pattern_ai not matched!")

# ==============================================================================
# 8. 턴 종료 시 군량고 소각 지속 피해 (아군 15% / 적 12% 병력 탈영)
# ==============================================================================
print("8. Adding turn starvation damage to finishFullTurn...")

# finishFullTurn 내부에 탈영 로직 주입
turn_starvation_code = """
      // 🌾 군량고 소각 시 매 턴 보급 결핍 탈영 연산
      if (sam5BattleState.allySupplyBurned) {
        UNITS.filter(u => u.faction === "ally" && u.troops > 0).forEach(ally => {
          const desert = Math.floor(ally.troops * 0.15);
          ally.troops = Math.max(0, ally.troops - desert);
          showDamagePop(ally.q, ally.r, `보급차단 -${desert}`);
          logBattle(`🌾🚨 [아군 보급 결핍] 군량고 소각으로 ${ally.name} 부대에서 ${desert.toLocaleString()}명이 탈영했습니다!`);
        });
      }

      if (sam5BattleState.supplyBurned) {
        UNITS.filter(u => u.faction === "enemy" && u.troops > 0).forEach(enemy => {
          const desert = Math.floor(enemy.troops * 0.12);
          enemy.troops = Math.max(0, enemy.troops - desert);
          showDamagePop(enemy.q, enemy.r, `적보급차단 -${desert}`);
          logBattle(`🌾 적군 ${enemy.name} 부대에서 군량 부족으로 ${desert.toLocaleString()}명이 탈영했습니다!`);
        });
      }
"""

if 'sam5BattleState.allySupplyBurned' not in text:
    target_turn_point = "sam5BattleState.phase = \"ally\";"
    idx = text.find(target_turn_point)
    if idx != -1:
        text = text[:idx] + turn_starvation_code + "\n      " + text[idx:]
        print("  -> Turn starvation damage successfully added to finishFullTurn!")
    else:
        print("  -> ERROR: target_turn_point not found in finishFullTurn!")

# ==============================================================================
# 9. 캔버스 렌더링: 아군 군량고(타일 8) 및 적 군량고(타일 4) 시각화
# ==============================================================================
print("9. Updating renderBattlefield for Ally Depot (tile 8)...")

# terrain === 4 아래에 terrain === 8 추가
terrain_color_pattern = r"else if \(terrain === 4\) tileColor = sam5BattleState\.supplyBurned \? \"#292524\" : \"#854d0e\"; // 보급창"
terrain_color_replacement = """else if (terrain === 4) tileColor = sam5BattleState.supplyBurned ? "#292524" : "#854d0e"; // 🌾 적 보급창
          else if (terrain === 8) tileColor = sam5BattleState.allySupplyBurned ? "#292524" : "#047857"; // 🌾 아군 보급창"""

text = re.sub(terrain_color_pattern, terrain_color_replacement, text)

# 지형 텍스트 라벨에도 terrain === 8 추가
terrain_label_pattern = r"else if \(terrain === 4\) ctx\.fillText\(sam5BattleState\.supplyBurned \? \"💥소실\" : \"🌾군량고\", x, y - 16\);"
terrain_label_replacement = """else if (terrain === 4) ctx.fillText(sam5BattleState.supplyBurned ? "💥소실" : "🌾적군량고", x, y - 16);
          else if (terrain === 8) ctx.fillText(sam5BattleState.allySupplyBurned ? "💥소실" : "🌾아군량고", x, y - 16);"""

text = re.sub(terrain_label_pattern, terrain_label_replacement, text)

# 이동 클릭 시 아군/적 군량고 도달 체크
click_depot_pattern = r"if \(q === 8 && r === 3 && !sam5BattleState\.supplyBurned\) \{\s*triggerSupplyRaid\(sam5BattleState\.selectedUnit\);\s*\}"
click_depot_replacement = """const destTerrain = MAP_TERRAIN[r] ? MAP_TERRAIN[r][q] : 0;
        if (destTerrain === 4 && !sam5BattleState.supplyBurned) {
          triggerSupplyRaid(sam5BattleState.selectedUnit);
        } else if (destTerrain === 8 && !sam5BattleState.allySupplyBurned) {
          logBattle(`🌾 아군 ${sam5BattleState.selectedUnit.name} 부대가 본진 군량고를 경비하고 있습니다.`);
        }"""

text = re.sub(click_depot_pattern, click_depot_replacement, text)

# ==============================================================================
# 파일 저장 및 복제
# ==============================================================================
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)
print(f"Main Desktop file updated: {len(text):,} bytes")

# 동기화 파일 저장
update_desktop_path = r'C:/Users/LENOVO/Desktop/sam3_update.html'
with open(update_desktop_path, 'w', encoding='utf-8') as f:
    f.write(text)

git_edu_path = r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/교육학/samgukji.html'
with open(git_edu_path, 'w', encoding='utf-8') as f:
    f.write(text)

git_root_path = r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/samgukji.html'
with open(git_root_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("All target files successfully updated and synced!")
