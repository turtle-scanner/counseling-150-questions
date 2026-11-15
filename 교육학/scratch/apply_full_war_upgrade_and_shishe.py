# -*- coding: utf-8 -*-
import os
import re

def main():
    print("=== 삼국지 3 전쟁 대업그레이드 & 사섭 초상화 & 침공 매칭 버그 수리 시작 ===")

    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 사섭 Base64 로드
    shishe_b64_file = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\shishe_b64.txt"
    with open(shishe_b64_file, "r", encoding="utf-8") as f:
        shishe_data_uri = f.read().strip()
    print(f"사섭 Data URI 로드 완료: {len(shishe_data_uri)} 문자")

    # PORTRAITS에 shishe 주입
    if '"shishe":' not in html:
        portraits_pattern = r'const PORTRAITS = \{'
        html = re.sub(portraits_pattern, f'const PORTRAITS = {{\n      "shishe": "{shishe_data_uri}",', html, count=1)
        print("PORTRAITS에 shishe 등록 완료!")

    # updateRulerPortraitDisplay에 사섭 분기 추가
    shishe_display_code = """      } else if (ruler === '사섭') {
        faceImg.src = p['shishe'] || p['liubei'];
        nameText.innerText = '군주 사섭 (士燮)';
        statsText.innerText = '통솔: 75 | 무력: 75 | 교주태수';
"""
    if "ruler === '사섭'" not in html:
        # '원술' 분기 앞에 삽입
        html = html.replace("} else if (ruler === '원술') {", shishe_display_code + "      } else if (ruler === '원술') {")
        print("updateRulerPortraitDisplay에 사섭 분기 추가 완료!")

    # ENEMY_OFFICERS_BY_RULER['사섭']에 faceKey 추가
    html = html.replace("{ name: '사섭 (위언)', war: 62, int: 82, lead: 75, icon: '👑', title: '교지태수' }",
                        "{ name: '사섭 (위언)', war: 62, int: 82, lead: 75, icon: '👑', title: '교지태수', faceKey: 'shishe' }")

    # 2. MY_OFFICERS에 fatigue: 0 속성 주입
    html = html.replace("{ id: 'guan_yu', name: '관우 (운장)', war: 98, int: 84, lead: 97, icon: '🐉', title: '무성 (청룡언월도)', hp: 100 }",
                        "{ id: 'guan_yu', name: '관우 (운장)', war: 98, int: 84, lead: 97, icon: '🐉', title: '무성 (청룡언월도)', hp: 100, fatigue: 0 }")
    html = html.replace("{ id: 'zhang_fei', name: '장비 (익덕)', war: 99, int: 35, lead: 88, icon: '⚡', title: '만인지적 (장팔사모)', hp: 100 }",
                        "{ id: 'zhang_fei', name: '장비 (익덕)', war: 99, int: 35, lead: 88, icon: '⚡', title: '만인지적 (장팔사모)', hp: 100, fatigue: 0 }")
    html = html.replace("{ id: 'zhao_yun', name: '조운 (자룡)', war: 97, int: 86, lead: 92, icon: '🛡️', title: '상산 조자룡 (일기당천)', hp: 100 }",
                        "{ id: 'zhao_yun', name: '조운 (자룡)', war: 97, int: 86, lead: 92, icon: '🛡️', title: '상산 조자룡 (일기당천)', hp: 100, fatigue: 0 }")
    html = html.replace("{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장', hp: 100 }",
                        "{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장', hp: 100, fatigue: 0 }")
    html = html.replace("{ id: 'wei_yan', name: '위연 (문장)', war: 91, int: 70, lead: 84, icon: '🗡️', title: '한중태수 맹장', hp: 100 }",
                        "{ id: 'wei_yan', name: '위연 (문장)', war: 91, int: 70, lead: 84, icon: '🗡️', title: '한중태수 맹장', hp: 100, fatigue: 0 }")
    html = html.replace("{ id: 'liu_bei', name: '유비 (현덕)', war: 75, int: 78, lead: 80, icon: '👑', title: '한실종친 군주 (쌍고검)', hp: 100 }",
                        "{ id: 'liu_bei', name: '유비 (현덕)', war: 75, int: 78, lead: 80, icon: '👑', title: '한실종친 군주 (쌍고검)', hp: 100, fatigue: 0 }")

    # 3. 출전 장수 편성 모달 HTML 주입 (기존에 없으면)
    deploy_modal_html = """
  <!-- ==================== ⚔️ 출전 장수 편성 & 피로도 선택 모달 ==================== -->
  <div id="officer-deploy-modal" class="fixed inset-0 modal-backdrop z-[99999] hidden flex items-center justify-center p-3 bg-black/90">
    <div class="koei-box w-full max-w-2xl p-4 rounded-lg shadow-2xl border-4 border-red-500 max-h-[92vh] flex flex-col justify-between overflow-y-auto">
      
      <!-- 헤더 -->
      <div class="flex items-center justify-between border-b-2 border-red-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-2xl">⚔️</span>
          <div>
            <h2 class="text-base font-black text-red-300 text-pixel" id="deploy-modal-title">
              [출전 장수 편성] 침공 부대 선발
            </h2>
            <div class="text-[11px] text-amber-200" id="deploy-target-desc">
              침공 목표 영지로 출격할 장수를 지명하십시오.
            </div>
          </div>
        </div>
        <button onclick="closeModal('officer-deploy-modal')" class="text-slate-400 hover:text-white font-mono text-xs px-2 py-1 border border-slate-600 rounded">
          ✕ 취소
        </button>
      </div>

      <!-- 안내 바 -->
      <div class="bg-blue-950/80 border border-amber-500/60 p-2.5 rounded text-xs text-slate-200 mb-3 flex items-center justify-between">
        <span>💡 이번 전투에 출전할 장수를 <strong>1~3명</strong> 선택하십시오.</span>
        <span class="text-yellow-300 font-bold bg-amber-950 px-2.5 py-0.5 rounded border border-amber-500" id="deploy-selected-count">선택: 0 / 3명</span>
      </div>

      <!-- 장수 카드 리스트 -->
      <div id="deploy-officer-list" class="grid grid-cols-1 md:grid-cols-2 gap-2.5 max-h-[50vh] overflow-y-auto p-1">
        <!-- 동적 렌더링 -->
      </div>

      <!-- 하단 출진 버튼 -->
      <div class="border-t border-red-900/80 pt-3 mt-2 flex items-center justify-between">
        <div class="text-[11px] text-slate-400">
          • ⚠️ 피로도 70% 이상인 장수는 <strong>탈진하여 연속 출전 불가</strong> (휴양 필요)
        </div>
        <button onclick="confirmOfficerDeployment()" id="btn-deploy-confirm" class="px-6 py-2.5 bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-white font-black text-xs rounded border-2 border-yellow-300 shadow-xl flex items-center gap-1.5 animate-pulse">
          <span>⚔️</span> 선발 장수 출진! (전장 돌입)
        </button>
      </div>

    </div>
  </div>
"""
    if 'id="officer-deploy-modal"' not in html:
        html = html.replace('<!-- ==================== 1:1 장수 전략 결투 (일기토) 모달 ==================== -->',
                            deploy_modal_html + '\n  <!-- ==================== 1:1 장수 전략 결투 (일기토) 모달 ==================== -->')
        print("출전 장수 편성 모달 HTML 주입 완료!")

    # 4. 침공 알림 모달에 3개 옵션 탑재 (1:1 요격, 10턴 헥스 요격, 성벽 농성)
    invasion_buttons_old = """      <div class="grid grid-cols-2 gap-3 pt-2">
        <button onclick="handleInvasionDuel()" class="py-3 bg-red-700 hover:bg-red-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex items-center justify-center gap-1">
          <span>⚔️</span> 장수 출진 1:1 요격전!
        </button>
        <button onclick="handleInvasionDefend()" class="py-3 bg-blue-800 hover:bg-blue-700 text-cyan-100 font-bold text-xs rounded border-2 border-cyan-300 shadow flex items-center justify-center gap-1">
          <span>🛡️</span> 성벽 결사 농성!
        </button>
      </div>"""

    invasion_buttons_new = """      <div class="grid grid-cols-3 gap-2 pt-2">
        <button onclick="handleInvasionDuel()" class="py-2.5 px-1 bg-red-700 hover:bg-red-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex flex-col items-center justify-center text-center">
          <span class="text-sm">⚔️</span>
          <span>1:1 적장 진검요격!</span>
          <span class="text-[9px] text-yellow-200">적장 일기토 격파</span>
        </button>
        <button onclick="handleInvasionHexBattle()" class="py-2.5 px-1 bg-amber-700 hover:bg-amber-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex flex-col items-center justify-center text-center">
          <span class="text-sm">🚩</span>
          <span>10턴 헥스 전술요격!</span>
          <span class="text-[9px] text-yellow-200">출전 장수 3인 선발</span>
        </button>
        <button onclick="handleInvasionDefend()" class="py-2.5 px-1 bg-blue-800 hover:bg-blue-700 text-cyan-100 font-bold text-xs rounded border-2 border-cyan-300 shadow flex flex-col items-center justify-center text-center">
          <span class="text-sm">🛡️</span>
          <span>성벽 결사 농성!</span>
          <span class="text-[9px] text-cyan-200">성벽 방어력 수성</span>
        </button>
      </div>"""

    if invasion_buttons_old in html:
        html = html.replace(invasion_buttons_old, invasion_buttons_new)
        print("침공 알림 모달 버튼 3개 옵션 개편 완료!")

    # 5. 전쟁 및 결투 JS 엔진 대대적 업그레이드
    # handleInvasionDuel, handleInvasionHexBattle, openDuelSelectModal, updateEnemyOfficersList, startDuelFight, duelAction
    duel_and_war_js = """
    // ==================== ⚔️ 출전 장수 편성 & 피로도(연속 출전 제한) 엔진 ====================
    let deployingTargetProv = null;
    let deployingFromProv = null;
    let isDeployDefense = false;
    let selectedDeployOfficerIds = [];

    function openOfficerDeployModal(target, fromProv, isDefense = false) {
      closeAllPopups();
      deployingTargetProv = target;
      deployingFromProv = fromProv;
      isDeployDefense = isDefense;
      selectedDeployOfficerIds = [];

      // 기본적으로 피로도 70% 미만인 장수 최대 3명 자동 선택
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        if (off.fatigue < 70 && selectedDeployOfficerIds.length < 3) {
          selectedDeployOfficerIds.push(off.id);
        }
      });

      const titleEl = document.getElementById('deploy-modal-title');
      const descEl = document.getElementById('deploy-target-desc');
      if (isDefense) {
        titleEl.innerText = `[방어 출전 장수 편성] ${target.name} 방어전 출격!`;
        descEl.innerText = `침공해온 ${target.attackerRuler || target.ruler}군을 격퇴할 요격 장수를 선발하십시오.`;
      } else {
        titleEl.innerText = `[출전 장수 편성] ${fromProv.name} ➔ ${target.name} 침공`;
        descEl.innerText = `목표: ${target.id}. ${target.name} (${target.ruler}군, 병력: ${target.soldiers.toLocaleString()}명) | 출격지: ${fromProv.name}`;
      }

      renderDeployOfficerList();
      openModal('officer-deploy-modal');
    }

    function renderDeployOfficerList() {
      const container = document.getElementById('deploy-officer-list');
      if (!container) return;

      container.innerHTML = MY_OFFICERS.map(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        const isExhausted = (off.fatigue >= 70);
        const isSelected = selectedDeployOfficerIds.includes(off.id);

        let statusBadge = '<span class="px-2 py-0.5 rounded text-[10px] bg-emerald-950 border border-emerald-500 text-emerald-300 font-bold">🟢 쾌조</span>';
        if (off.fatigue >= 70) {
          statusBadge = '<span class="px-2 py-0.5 rounded text-[10px] bg-red-950 border border-red-500 text-red-300 font-black animate-pulse">🔴 탈진 (연속출전 불가)</span>';
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
                  ${statusBadge}
                </div>
                <div class="text-[11px] text-yellow-300">
                  무력: <strong>${off.war}</strong> | 지력: ${off.int} | 통솔: ${off.lead || 80}
                </div>
                <div class="w-40 bg-slate-900 h-2 rounded-full overflow-hidden border border-slate-700 mt-1">
                  <div class="h-full rounded-full ${off.fatigue >= 70 ? 'bg-red-500' : (off.fatigue >= 35 ? 'bg-amber-400' : 'bg-emerald-400')}" style="width: ${off.fatigue}%;"></div>
                </div>
                <div class="text-[10px] text-slate-400">
                  피로도: <strong class="${off.fatigue >= 70 ? 'text-red-400 font-black' : 'text-slate-300'}">${off.fatigue}%</strong>
                </div>
              </div>
            </div>
            <div>
              <input type="checkbox" ${isSelected ? 'checked' : ''} ${isExhausted ? 'disabled' : ''} class="w-4 h-4 accent-amber-500 pointer-events-none">
            </div>
          </div>
        `;
      }).join('');

      document.getElementById('deploy-selected-count').innerText = `선택: ${selectedDeployOfficerIds.length} / 3명`;
    }

    function toggleDeployOfficer(offId) {
      const off = MY_OFFICERS.find(o => o.id === offId);
      if (!off) return;
      if (off.fatigue >= 70) {
        alert(`⚠️ [출전 불가] ${off.name}은(는) 이전 전투로 인한 극심한 피로(피로도 ${off.fatigue}%)로 인해 연속 출전할 수 없습니다!\\n[0. 휴양]을 하거나 포상을 베풀어 피로도를 회복시키십시오.`);
        return;
      }

      if (selectedDeployOfficerIds.includes(offId)) {
        selectedDeployOfficerIds = selectedDeployOfficerIds.filter(id => id !== offId);
      } else {
        if (selectedDeployOfficerIds.length >= 3) {
          alert("💡 출전 장수는 최대 3명까지만 선택할 수 있습니다.");
          return;
        }
        selectedDeployOfficerIds.push(offId);
      }
      playSfx('select');
      renderDeployOfficerList();
    }

    function confirmOfficerDeployment() {
      if (selectedDeployOfficerIds.length === 0) {
        alert("⚠️ 최소 1명 이상의 장수를 출전 부대로 선택해야 합니다!");
        return;
      }

      const deployedOfficers = MY_OFFICERS.filter(o => selectedDeployOfficerIds.includes(o.id));
      closeModal('officer-deploy-modal');

      if (isDeployDefense && pendingInvasion) {
        // 방어 10턴 헥스 결전
        const targetProv = pendingInvasion.targetProv;
        const fakeFromProv = {
          id: pendingInvasion.fromProv.id,
          name: pendingInvasion.targetProv.name + " 수비진",
          soldiers: targetProv.soldiers,
          ruler: gameState.rulerName
        };
        const enemyTargetProv = {
          id: pendingInvasion.fromProv.id,
          name: `${pendingInvasion.attackerRuler} 침공군`,
          soldiers: pendingInvasion.invasionForce,
          ruler: pendingInvasion.attackerRuler,
          leader: pendingInvasion.attackerRuler
        };
        openHexBattle(enemyTargetProv, fakeFromProv, deployedOfficers);
      } else {
        // 일반 공격 10턴 헥스 결전
        openHexBattle(deployingTargetProv, deployingFromProv, deployedOfficers);
      }
    }

    // ==================== 🚨 적군 침공 요격 처리 (손책 등 침공 군주 100% 매칭) ====================
    function handleInvasionDuel() {
      closeModal('invasion-alert-modal');
      if (!pendingInvasion) return;
      const { attackerRuler, fromProv, targetProv } = pendingInvasion;
      openDuelSelectModal(fromProv ? fromProv.id : null, attackerRuler);
      logMessage(`⚔️ [장수 출진 요격] 침공해온 ${attackerRuler}군 지휘부를 1:1로 격파하기 위해 결투를 개시합니다!`, 'text-yellow-300 font-bold');
    }

    function handleInvasionHexBattle() {
      closeModal('invasion-alert-modal');
      if (!pendingInvasion) return;
      const { attackerRuler, targetProv, fromProv } = pendingInvasion;
      openOfficerDeployModal(targetProv, fromProv, true);
      logMessage(`🚩 [10턴 헥스 요격] 침공해온 ${attackerRuler}군에 맞서 출전 장수를 편성합니다!`, 'text-yellow-300 font-black');
    }

    // ==================== 1:1 장수 전략 결투 (일기토) 시스템 ====================
    let selectedMyOfficerIdx = 0;

    function openDuelSelectModal(targetProvId = null, specificRuler = null) {
      closeAllPopups();
      const myContainer = document.getElementById('duel-my-officer-list');
      myContainer.innerHTML = '';

      // 피로도 반영 렌더링
      MY_OFFICERS.forEach((off, idx) => {
        if (off.fatigue === undefined) off.fatigue = 0;
        const isExhausted = (off.fatigue >= 70);
        const isSelected = (idx === selectedMyOfficerIdx);
        const item = document.createElement('div');
        item.className = `p-2 rounded border text-xs flex flex-col justify-between transition ${
          isExhausted
            ? 'bg-slate-900 border-red-900/60 opacity-50 cursor-not-allowed'
            : (isSelected ? 'bg-amber-900 border-yellow-300 ring-2 ring-yellow-400 cursor-pointer' : 'bg-blue-900/60 border-blue-600 hover:bg-blue-800 cursor-pointer')
        }`;
        
        let fatigueBadge = `<span class="text-[10px] ${off.fatigue >= 70 ? 'text-red-400 font-black' : (off.fatigue >= 35 ? 'text-amber-300' : 'text-emerald-300')}">피로 ${off.fatigue}%</span>`;
        if (isExhausted) fatigueBadge += ` <span class="text-[9px] text-red-500 font-bold">[탈진]</span>`;

        item.innerHTML = `
          <div class="flex items-center justify-between font-bold text-white">
            <span class="flex items-center gap-1">${off.icon} ${off.name}</span>
            ${fatigueBadge}
          </div>
          <div class="text-[11px] text-yellow-300 mt-1">무력: <strong>${off.war}</strong> | 지력: ${off.int}</div>
          <div class="text-[10px] text-slate-300">${off.title}</div>
        `;
        if (!isExhausted) {
          item.onclick = () => {
            selectedMyOfficerIdx = idx;
            openDuelSelectModal(targetProvId, specificRuler);
          };
        } else {
          item.onclick = () => {
            alert(`⚠️ [출전 불가] ${off.name}은(는) 피로도(${off.fatigue}%)가 너무 높아 1:1 결투에 나설 수 없습니다! (휴양 필요)`);
          };
        }
        myContainer.appendChild(item);
      });

      // 선택된 장수가 탈진이면 쾌조 장수로 자동 선택
      if (MY_OFFICERS[selectedMyOfficerIdx] && MY_OFFICERS[selectedMyOfficerIdx].fatigue >= 70) {
        const ableIdx = MY_OFFICERS.findIndex(o => (o.fatigue || 0) < 70);
        if (ableIdx !== -1) selectedMyOfficerIdx = ableIdx;
      }

      // 목표 적 영지 셀렉트박스 설정
      const provSelect = document.getElementById('duel-enemy-prov-select');
      provSelect.innerHTML = '';

      let targetRuler = specificRuler;
      if (pendingInvasion) {
        targetRuler = pendingInvasion.attackerRuler;
        if (!targetProvId && pendingInvasion.fromProv) targetProvId = pendingInvasion.fromProv.id;
      }

      const enemies = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      enemies.forEach(p => {
        const opt = document.createElement('option');
        opt.value = p.id;
        opt.innerText = `${p.id}. ${p.name} (${p.ruler}령)`;
        if (targetProvId && p.id === targetProvId) opt.selected = true;
        else if (!targetProvId && targetRuler && p.ruler === targetRuler) opt.selected = true;
        provSelect.appendChild(opt);
      });

      if (targetProvId) {
        provSelect.value = targetProvId;
      } else if (targetRuler) {
        const matched = enemies.find(p => p.ruler === targetRuler);
        if (matched) provSelect.value = matched.id;
      }

      updateEnemyOfficersList(targetRuler);

      // 모달 제목 텍스트 반영
      const modalHeaderTitle = document.querySelector('#duel-select-modal h2');
      if (modalHeaderTitle) {
        if (pendingInvasion) {
          modalHeaderTitle.innerText = `⚔️ [방어 요격 결투] ${pendingInvasion.attackerRuler}군 침공 요격!`;
        } else {
          modalHeaderTitle.innerText = `⚔️ 1:1 장수 진검승부 (일기토 결투)`;
        }
      }

      openModal('duel-select-modal');
    }

    function updateEnemyOfficersList(targetRuler = null) {
      const provSelect = document.getElementById('duel-enemy-prov-select');
      const offSelect = document.getElementById('duel-enemy-officer-select');
      offSelect.innerHTML = '';
      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId);
      if (!prov) return;

      const rulerName = (pendingInvasion && pendingInvasion.attackerRuler) ? pendingInvasion.attackerRuler : (targetRuler || prov.ruler);

      const list = ENEMY_OFFICERS_BY_RULER[rulerName] || ENEMY_OFFICERS_BY_RULER[prov.ruler] || [
        { name: prov.leader, war: 80, int: 70, lead: 80, icon: '⚔️', title: '영지 수비장군' }
      ];

      list.forEach((off, i) => {
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = `${off.name} (무력 ${off.war} / 지력 ${off.int})`;
        offSelect.appendChild(opt);
      });
    }

    function startDuelFight() {
      closeModal('duel-select-modal');
      const provSelect = document.getElementById('duel-enemy-prov-select');
      const offSelect = document.getElementById('duel-enemy-officer-select');
      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId);

      const myOff = MY_OFFICERS[selectedMyOfficerIdx];
      const rulerName = (pendingInvasion && pendingInvasion.attackerRuler) ? pendingInvasion.attackerRuler : (prov ? prov.ruler : '적군');
      const list = ENEMY_OFFICERS_BY_RULER[rulerName] || (prov ? ENEMY_OFFICERS_BY_RULER[prov.ruler] : null) || [
        { name: prov ? prov.leader : '적장', war: 80, int: 70, lead: 80, icon: '⚔️', title: '영지 수비장군' }
      ];
      const enemyOff = list[parseInt(offSelect.value, 10) || 0];

      duelState.round = 1;
      duelState.myOfficer = myOff;
      duelState.enemyOfficer = enemyOff;
      duelState.myHp = 100;
      duelState.enemyHp = 100;
      duelState.enemyConfused = false;
      duelState.inDuel = true;

      // 출전 장수 피로도 +40%
      if (myOff.fatigue === undefined) myOff.fatigue = 0;
      myOff.fatigue = Math.min(100, myOff.fatigue + 40);

      const enemyWar = (gameState.difficulty === 'hard') ? enemyOff.war + 10 : enemyOff.war;
      const enemyInt = (gameState.difficulty === 'hard') ? enemyOff.int + 8 : enemyOff.int;

      document.getElementById('duel-round-badge').innerText = '제 1 합';
      document.getElementById('duel-my-name').innerText = myOff.name;
      document.getElementById('duel-my-icon').innerText = myOff.icon;
      document.getElementById('duel-my-stats').innerText = `무력: ${myOff.war} | 지력: ${myOff.int} | 피로: ${myOff.fatigue}%`;
      document.getElementById('duel-my-hp-txt').innerText = '100 / 100';
      document.getElementById('duel-my-hp-bar').style.width = '100%';

      document.getElementById('duel-enemy-name').innerText = enemyOff.name;
      document.getElementById('duel-enemy-stats').innerText = `무력: ${enemyWar} | 지력: ${enemyInt}`;
      document.getElementById('duel-enemy-hp-txt').innerText = '100 / 100';
      document.getElementById('duel-enemy-hp-bar').style.width = '100%';

      const enemyImg = document.getElementById('duel-enemy-img');
      const enemyIcon = document.getElementById('duel-enemy-icon');
      if (enemyOff.faceKey && PORTRAITS[enemyOff.faceKey]) {
        enemyImg.src = PORTRAITS[enemyOff.faceKey];
        enemyImg.classList.remove('hidden');
        enemyIcon.classList.add('hidden');
      } else {
        enemyImg.classList.add('hidden');
        enemyIcon.classList.remove('hidden');
        enemyIcon.innerText = enemyOff.icon || '👹';
      }

      const log = document.getElementById('duel-combat-log');
      log.innerHTML = `
        <div class="text-yellow-300 font-extrabold">🚩 [진검승부 결투 개전] ${myOff.name} vs ${enemyOff.name}!</div>
        <div class="text-cyan-200">${pendingInvasion ? `🚨 ${pendingInvasion.attackerRuler}군의 침공을 저지하기 위한 필사의 요격전!` : '두 장수가 말을 몰아 창검을 맞부딪치며 제 1합에 돌입합니다!'}</div>
      `;

      playSfx('war');
      openModal('duel-modal');
    }
"""

    # 치환하기 위해 handleInvasionDuel 부터 startDuelFight 끝까지 탐색
    start_kw = "// 아군 침공 요격 처리\n    function handleInvasionDuel()"
    end_kw = "openModal('duel-modal');\n    }"

    if start_kw in html and end_kw in html:
        part1 = html[:html.find(start_kw)]
        part2 = html[html.find(end_kw) + len(end_kw):]
        html = part1 + duel_and_war_js.strip() + "\n" + part2
        print("결투 및 침공 요격 JS 엔진 교체 완료!")
    else:
        print("경고: 결투 교체 키워드를 찾지 못함. 대체 검색 시도...")
        alt_start = "function handleInvasionDuel()"
        idx1 = html.find(alt_start)
        idx2 = html.find("openModal('duel-modal');\n    }")
        if idx1 != -1 and idx2 != -1:
            part1 = html[:idx1]
            part2 = html[idx2 + len(end_kw):]
            html = part1 + duel_and_war_js.strip() + "\n" + part2
            print("대체 검색으로 결투 엔진 교체 성공!")

    # 6. duelAction 내부의 승리/패배 판정 시 pendingInvasion 처리 강화
    duel_win_old = """      if (duelState.enemyHp <= 0) {
        duelState.inDuel = false;
        playSfx('victory');
        logDuel(`🎉🏆 [일기토 완전 승리!] ${my.name}이 ${enemy.name}을 말 아래로 낙마시키고 생포했습니다!!`, 'text-yellow-300 font-extrabold text-sm');
        logMessage(`👑 [일기토 대승] ${my.name}이 적장 ${enemy.name}과의 결투에서 대승을 거두었습니다! (금 500전 노획)`, 'text-yellow-300 font-black');

        if (battleData.targetProv) {
          logMessage(`🚩 [영지 점령] 적장이 일기토에서 격파되어 적군이 총붕괴했습니다! ${battleData.targetProv.name}을 점령했습니다!`, 'text-yellow-300 font-black');
          alert(`🎉🏆 [일기토 대승리!]
${my.name}이 적장 ${enemy.name}을 베어 적군이 총붕괴하고 패주했습니다!
${battleData.targetProv.name}을 완전히 점령하여 아군 영지로 편입했습니다!`);
          endBattleVictory();
        } else {
          const myProv = getMyCapital();
          myProv.gold += 500;
          updateRightPanel(myProv.id);
          alert(`🎉 [일기토 승리] ${my.name}이 적장 ${enemy.name}을 격파했습니다!
적군의 사기가 곤두박질치고 군자금 500전을 전리품으로 획득했습니다!
(다음 장수를 골라 또 대결할 수 있습니다)`);
        }
        setTimeout(() => closeModal('duel-modal'), 1800);
      } else if (duelState.myHp <= 0) {
        duelState.inDuel = false;
        logDuel(`💀 [패배] ${my.name}이 부상을 입고 휘하 장졸들의 호위를 받으며 긴급 철수했습니다!`, 'text-red-500 font-black');
        logMessage(`⚠️ [일기토 패배] ${my.name}이 결투 중 부상을 입고 후퇴했습니다.`, 'text-red-400');
        alert(`⚠️ ${my.name}이 부상을 입고 후퇴했습니다! 다른 장수를 골라 재도전하십시오.`);
        setTimeout(() => closeModal('duel-modal'), 1800);
      }"""

    duel_win_new = """      if (duelState.enemyHp <= 0) {
        duelState.inDuel = false;
        playSfx('victory');
        logDuel(`🎉🏆 [일기토 완전 승리!] ${my.name}이 ${enemy.name}을 말 아래로 낙마시키고 생포했습니다!!`, 'text-yellow-300 font-extrabold text-sm');
        logMessage(`👑 [일기토 대승] ${my.name}이 적장 ${enemy.name}과의 결투에서 대승을 거두었습니다! (금 500전 노획)`, 'text-yellow-300 font-black');

        if (pendingInvasion) {
          const inv = pendingInvasion;
          pendingInvasion = null;
          const myProv = inv.targetProv;
          myProv.gold += 800;
          myProv.food += 5000;
          logMessage(`🎉🛡️ [침공군 완전 격퇴!] ${my.name} 장군이 쳐들어온 ${inv.attackerRuler}군의 선봉장 ${enemy.name}을 베어 적군 ${inv.invasionForce.toLocaleString()}명이 사기를 잃고 패주했습니다! (노획: 금 800전, 군량 5,000석)`, 'text-emerald-300 font-black');
          alert(`🎉🛡️ [수성 요격 대승!]\n\n${my.name} 장군이 ${inv.attackerRuler}군의 선봉장 ${enemy.name}을 1:1 결투로 베었습니다!\n지휘관을 잃은 적군 ${inv.invasionForce.toLocaleString()}명이 전의를 상실하고 패주하였습니다!\n\n전리품: 금 800전, 군량 5,000석 노획!`);
          updateRightPanel(myProv.id);
        } else if (battleData.targetProv) {
          logMessage(`🚩 [영지 점령] 적장이 일기토에서 격파되어 적군이 총붕괴했습니다! ${battleData.targetProv.name}을 점령했습니다!`, 'text-yellow-300 font-black');
          alert(`🎉🏆 [일기토 대승리!]\\n${my.name}이 적장 ${enemy.name}을 베어 적군이 총붕괴하고 패주했습니다!\\n${battleData.targetProv.name}을 완전히 점령하여 아군 영지로 편입했습니다!`);
          endBattleVictory();
        } else {
          const myProv = getMyCapital();
          myProv.gold += 500;
          updateRightPanel(myProv.id);
          alert(`🎉 [일기토 승리] ${my.name}이 적장 ${enemy.name}을 격파했습니다!\n적군의 사기가 곤두박질치고 군자금 500전을 전리품으로 획득했습니다!\n(다음 장수를 골라 또 대결할 수 있습니다)`);
        }
        setTimeout(() => closeModal('duel-modal'), 1800);
      } else if (duelState.myHp <= 0) {
        duelState.inDuel = false;
        my.fatigue = 85; // 패배 장수 극심한 탈진
        logDuel(`💀 [패배] ${my.name}이 부상을 입고 휘하 장졸들의 호위를 받으며 긴급 철수했습니다!`, 'text-red-500 font-black');
        logMessage(`⚠️ [일기토 패배] ${my.name}이 결투 중 부상을 입고 후퇴했습니다. (탈진: 피로도 85%)`, 'text-red-400');
        
        if (pendingInvasion) {
          const inv = pendingInvasion;
          pendingInvasion = null;
          const target = inv.targetProv;
          const loss = Math.floor(target.soldiers * 0.25);
          target.soldiers = Math.max(500, target.soldiers - loss);
          target.defense = Math.max(10, target.defense - 10);
          logMessage(`⚠️ [방어선 돌파] ${my.name} 장군이 패배하여 ${inv.attackerRuler}군이 ${target.name}으로 난입했습니다! (병사 ${loss.toLocaleString()}명 손실)`, 'text-red-400 font-black');
          alert(`⚠️ [방어선 돌파!]\n${my.name} 장군이 부상을 입고 후퇴하면서 ${inv.attackerRuler}군에게 수성 피해를 입었습니다!`);
          updateRightPanel(target.id);
        } else {
          alert(`⚠️ ${my.name}이 부상을 입고 후퇴했습니다! 다른 장수를 골라 재도전하십시오.`);
        }
        setTimeout(() => closeModal('duel-modal'), 1800);
      }"""

    if duel_win_old in html:
        html = html.replace(duel_win_old, duel_win_new)
        print("duelAction 침공 격퇴 및 피로도 판정 로직 교체 완료!")

    # 7. 휴양(executeRest) 시 피로도 -35% 자연 회복 주입
    rest_hook = """      // 장수 피로도 자연 회복 (-35%)
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        off.fatigue = Math.max(0, off.fatigue - 35);
      });
      logMessage(`💤 [휴양 효과] 한 달이 지나며 전 장수들의 피로도가 35% 자연 회복되었습니다.`, 'text-cyan-200');
"""
    if "피로도가 35% 자연 회복되었습니다" not in html:
        html = html.replace("const seasonStr = `${curIcon} ${gameState.year}년 ${gameState.month}월 (${curSeason})`;",
                            rest_hook + "      const seasonStr = `${curIcon} ${gameState.year}년 ${gameState.month}월 (${curSeason})`;")
        print("executeRest에 피로도 -35% 회복 주입 완료!")

    # 8. 포상/연회 시 피로도 -50% 대폭 회복 주입
    reward_hook = """
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        off.fatigue = Math.max(0, off.fatigue - 50);
      });
      logMessage(`🍖 [연회 포상] 술과 고기를 하사하여 전 장수들의 피로도가 50% 대폭 회복되었습니다!`, 'text-emerald-300 font-bold');
"""
    if "피로도가 50% 대폭 회복되었습니다" not in html and "function executeReward()" in html:
        html = html.replace("function executeReward() {", "function executeReward() {" + reward_hook)
        print("executeReward에 피로도 -50% 회복 주입 완료!")

    # 9. openWarModal이 openOfficerDeployModal을 거치도록 연동
    open_war_old = """    function openWarModal(targetProvId = null, fromProvId = null) {
      closeAllPopups();
      
      const myProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName);
      if (myProvs.length === 0) {
        alert("⚠️ 통솔 가능한 아군 영지가 없습니다!");
        return;
      }

      let myProv = null;
      let target = null;

      if (targetProvId) {
        target = PROVINCES.find(p => p.id === targetProvId);
        if (fromProvId) {
          myProv = PROVINCES.find(p => p.id === fromProvId);
        } else {
          // 해당 타겟과 인접한 아군 영지 검색
          myProv = myProvs.find(p => p.adj.includes(target.id));
          if (!myProv) {
            // 인접하지 않으면 가장 많은 병력을 가진 아군 영지에서 출진
            myProvs.sort((a, b) => b.soldiers - a.soldiers);
            myProv = myProvs[0];
          }
        }
      } else {
        const curProv = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (curProv && curProv.ruler !== gameState.rulerName) {
          target = curProv;
          myProv = myProvs.find(p => p.adj.includes(target.id)) || myProvs[0];
        } else {
          openWarTargetSelectModal();
          return;
        }
      }

      if (!target || !myProv) {
        openWarTargetSelectModal();
        return;
      }

      if (myProv.soldiers < 1000) {
        alert(`⚠️ [출진 불가] ${myProv.name}의 병력(${myProv.soldiers.toLocaleString()}명)이 너무 적어 침공할 수 없습니다! (최소 1,000명 필요)`);
        return;
      }

      openHexBattle(target, myProv);
    }"""

    open_war_new = """    function openWarModal(targetProvId = null, fromProvId = null) {
      closeAllPopups();
      
      const myProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName);
      if (myProvs.length === 0) {
        alert("⚠️ 통솔 가능한 아군 영지가 없습니다!");
        return;
      }

      let myProv = null;
      let target = null;

      if (targetProvId) {
        target = PROVINCES.find(p => p.id === targetProvId);
        if (fromProvId) {
          myProv = PROVINCES.find(p => p.id === fromProvId);
        } else {
          myProv = myProvs.find(p => p.adj.includes(target.id));
          if (!myProv) {
            myProvs.sort((a, b) => b.soldiers - a.soldiers);
            myProv = myProvs[0];
          }
        }
      } else {
        const curProv = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (curProv && curProv.ruler !== gameState.rulerName) {
          target = curProv;
          myProv = myProvs.find(p => p.adj.includes(target.id)) || myProvs[0];
        } else {
          openWarTargetSelectModal();
          return;
        }
      }

      if (!target || !myProv) {
        openWarTargetSelectModal();
        return;
      }

      if (myProv.soldiers < 1000) {
        alert(`⚠️ [출진 불가] ${myProv.name}의 병력(${myProv.soldiers.toLocaleString()}명)이 너무 적어 침공할 수 없습니다! (최소 1,000명 필요)`);
        return;
      }

      // ⚔️ 바로 전장으로 가는 대신, 출전 장수 편성 모달(피로도 확인 및 선발)을 거침!
      openOfficerDeployModal(target, myProv, false);
    }"""

    if open_war_old in html:
        html = html.replace(open_war_old, open_war_new)
        print("openWarModal 출전 장수 편성 연동 완료!")

    # 10. 헥스 전장 엔진 대대적 업그레이드 (다이내믹 유닛 편성 & restartBattle 버그 수리)
    hex_upgrade_js = """
    // ==================== ⚔️ 삼국지 V 10턴 헥스 결전 엔진 대업그레이드 ====================
    let hexBattleContext = {
      targetProv: null,
      fromProv: null,
      deployedOfficers: [],
      capturedOfficer: null
    };

    function initHexBattleUnits(targetProv, fromProv, deployedOfficers = []) {
      // 1. 아군 유닛 세팅 (사용자가 선발한 장수들)
      const allyOfficers = (deployedOfficers && deployedOfficers.length > 0)
        ? deployedOfficers
        : MY_OFFICERS.filter(o => (o.fatigue || 0) < 70).slice(0, 3);

      if (allyOfficers.length === 0) {
        allyOfficers.push(MY_OFFICERS[0]);
      }

      const allyPositions = [
        { q: 1, r: 4, form: 'gyorin' },
        { q: 1, r: 5, form: 'bongsi' },
        { q: 0, r: 3, form: 'chuhaeng' }
      ];

      const soldierTotal = fromProv ? fromProv.soldiers : 15000;
      const soldierPerUnit = Math.floor(soldierTotal / Math.max(1, allyOfficers.length));

      const allyUnits = allyOfficers.map((off, idx) => {
        const pos = allyPositions[idx % allyPositions.length];
        return {
          id: off.id,
          faction: 'ally',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: off.title,
          avatar: off.icon || '⚔️',
          war: off.war,
          int: off.int,
          lead: off.lead || 85,
          chr: 85,
          troops: Math.min(10000, Math.max(3000, soldierPerUnit)),
          maxTroops: Math.min(10000, Math.max(3000, soldierPerUnit)),
          morale: 100,
          formation: pos.form,
          availableFormations: ['gyorin', 'bongsi', 'bangwon', 'chuhaeng'],
          skills: off.war >= 95 ? ['천하무쌍', '돌격', '분기', '일기토'] : (off.int >= 80 ? ['화계', '혼란', '고무', '수습'] : ['돌격', '분기', '화시']),
          q: pos.q,
          r: pos.r,
          moved: false,
          acted: false
        };
      });

      // 2. 적군 유닛 세팅 (침공 또는 방어 대상 군주의 명장들)
      const enemyRuler = targetProv ? targetProv.ruler : '동탁';
      const enemyOffList = ENEMY_OFFICERS_BY_RULER[enemyRuler] || [
        { name: targetProv ? targetProv.leader : '적 수비대장', war: 86, int: 70, lead: 84, icon: '🛡️', title: '영지 수비대장' },
        { name: targetProv ? (targetProv.advisor || '참모 도위') : '참모', war: 75, int: 80, lead: 75, icon: '📜', title: '참모 도위' }
      ];

      const enemyPositions = [
        { q: 6, r: 3, form: 'bongsi' },
        { q: 6, r: 4, form: 'gyorin' },
        { q: 5, r: 2, form: 'anhaeng' },
        { q: 7, r: 2, form: 'bangwon' }
      ];

      const enemyTotal = targetProv ? targetProv.soldiers : 18000;
      const enemySoldierPerUnit = Math.floor(enemyTotal / Math.max(1, enemyOffList.length));

      const enemyUnits = enemyOffList.slice(0, 4).map((off, idx) => {
        const pos = enemyPositions[idx % enemyPositions.length];
        return {
          id: `enemy_${idx}`,
          faction: 'enemy',
          name: off.name.split(' ')[0],
          fullName: off.name,
          title: off.title,
          avatar: off.icon || '👹',
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          chr: 70,
          isBoss: (idx === 0),
          troops: Math.min(10000, Math.max(2500, enemySoldierPerUnit)),
          maxTroops: Math.min(10000, Math.max(2500, enemySoldierPerUnit)),
          morale: 95,
          formation: pos.form,
          availableFormations: ['gyorin', 'bongsi', 'anhaeng'],
          skills: off.war >= 90 ? ['돌격', '분기', '일기토'] : (off.int >= 75 ? ['화계', '혼란'] : ['돌격', '화시']),
          q: pos.q,
          r: pos.r,
          moved: false,
          acted: false
        };
      });

      UNITS = [...allyUnits, ...enemyUnits];
    }

    function resetHexBattlefield(targetProv, fromProv, deployedOfficers = []) {
      sam5BattleState.turn = 1;
      sam5BattleState.phase = "ally";
      sam5BattleState.battleOver = false;
      sam5BattleState.supplyBurned = false;
      sam5BattleState.fireTiles = [{ q: 4, r: 2, turns: 2 }];
      sam5BattleState.selectedUnit = null;
      sam5BattleState.reachableHexes = [];
      sam5BattleState.attackableTargets = [];
      sam5BattleState.skillMode = null;

      initHexBattleUnits(targetProv, fromProv, deployedOfficers);

      const enemyRuler = targetProv ? targetProv.ruler : '적군';
      const turnInfoEl = document.getElementById("turnInfo");
      if (turnInfoEl) turnInfoEl.innerText = `제 1 / 10 턴 [아군 행동]`;
      const turnCountEl = document.getElementById("turnCountdownText");
      if (turnCountEl) turnCountEl.innerText = `10 턴 남음!`;
      const barEl = document.getElementById("turnProgressBar");
      if (barEl) {
        barEl.style.width = '100%';
        barEl.className = 'turn-meter-bar h-full rounded-full bg-emerald-500';
      }

      const titleEl = document.getElementById('hex-modal-title');
      if (titleEl && targetProv && fromProv) {
        titleEl.innerText = `[삼국지 V 10턴 헥스 결전] ${fromProv.name} ➔ ${targetProv.name} (${gameState.rulerName}군 vs ${enemyRuler}군)`;
      }

      logBattle(`⚔️ [개전] ${gameState.rulerName}군과 ${enemyRuler}군이 전장에서 대치합니다! 10턴 내로 적 본대를 궤멸시키십시오!`);
      renderBattlefield();
      deselectUnit();
    }

    function openHexBattle(targetProv, fromProv, deployedOfficers = []) {
      closeAllPopups();
      hexBattleContext.targetProv = targetProv;
      hexBattleContext.fromProv = fromProv;
      hexBattleContext.deployedOfficers = deployedOfficers;
      hexBattleContext.capturedOfficer = null;

      // 출전 장수들에게 피로도 +60% 누적 부여!
      if (deployedOfficers && deployedOfficers.length > 0) {
        deployedOfficers.forEach(off => {
          if (off.fatigue === undefined) off.fatigue = 0;
          off.fatigue = Math.min(100, off.fatigue + 60);
        });
      }

      resetHexBattlefield(targetProv, fromProv, deployedOfficers);
      openModal('hex-battle-modal');
      logMessage(`⚔️ [전술 결전 돌입] ${fromProv.name}의 아군이 ${targetProv.name}의 ${targetProv.ruler}군을 상대로 10턴 헥스 결전에 돌입했습니다!`, 'text-yellow-300 font-black');
    }

    function restartBattle() {
      if (hexBattleContext.targetProv && hexBattleContext.fromProv) {
        resetHexBattlefield(hexBattleContext.targetProv, hexBattleContext.fromProv, hexBattleContext.deployedOfficers);
      } else {
        const dummyTarget = PROVINCES.find(p => p.ruler !== gameState.rulerName) || PROVINCES[1];
        const dummyFrom = getMyCapital();
        resetHexBattlefield(dummyTarget, dummyFrom);
      }
    }
"""

    # 헥스 전장 교체 (openHexBattle 정의부터 restartBattle 정의까지)
    # 기존 openHexBattle ~ restartBattle 교체
    hex_start = "function openHexBattle(targetProv, fromProv) {"
    hex_end = "function restartBattle() {\n      location.reload();\n    }"

    if hex_start in html and hex_end in html:
        # 그 사이 함수들(onHexBattleVictory 등)은 보존
        # onHexBattleVictory 위치 찾기
        v_idx = html.find("function onHexBattleVictory(targetProv) {")
        if v_idx != -1:
            part_before = html[:html.find(hex_start)]
            # onHexBattleVictory 부터 restartBattle 직전까지 추출
            victory_part = html[v_idx:html.find(hex_end)]
            part_after = html[html.find(hex_end) + len(hex_end):]
            
            # 새 코드 조합
            new_hex_all = hex_upgrade_js.strip() + "\n\n    " + victory_part.strip() + "\n\n"
            html = part_before + new_hex_all + part_after
            print("헥스 전장 엔진 대업그레이드 및 restartBattle 새로고침 버그 수리 완료!")

    # 11. 헥스 전장 적군 턴 텍스트 교체 (동탁군 하드코딩 제거)
    html = html.replace('`제 ${sam5BattleState.turn} / 10 턴 [동탁군 반격 개시]`',
                        '`제 ${sam5BattleState.turn} / 10 턴 [적군 반격 개시]`')

    # 파일 쓰기
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("데스크톱 타겟 파일 저장 완료!")

    # 복사본들도 동기화
    sam3_update_path = r"C:\Users\LENOVO\Desktop\sam3_update.html"
    if os.path.exists(sam3_update_path):
        with open(sam3_update_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("sam3_update.html 동기화 완료!")

    repo_path1 = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html"
    with open(repo_path1, "w", encoding="utf-8") as f:
        f.write(html)
    repo_path2 = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    with open(repo_path2, "w", encoding="utf-8") as f:
        f.write(html)
    print("Git 레포 html 파일들 동기화 완료!")

    print("=== 빌드 완료 ===")

if __name__ == "__main__":
    main()
