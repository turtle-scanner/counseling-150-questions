# -*- coding: utf-8 -*-
import os
import json
import re

def main():
    base_script = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\build_samguk3_final_master.py"
    with open(base_script, "r", encoding="utf-8") as f:
        src = f.read()

    # 1. war-target-modal HTML 정의 (침공 목표 적 영지 선택 모달)
    war_target_modal_html = """
  <!-- ==================== 침공 목표 적 영지 선택 모달 (인접 영지 공격 버그 완전 박멸) ==================== -->
  <div id="war-target-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-red-500 max-h-[88vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-red-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚔️</span>
          <h2 class="text-base font-black text-red-300 text-pixel">
            [침공 목표 선택] 아군 영지와 국경이 맞닿은 적 영지
          </h2>
        </div>
        <button onclick="closeModal('war-target-modal')" class="text-slate-400 hover:text-white font-mono text-sm px-2 py-0.5 border border-slate-600 rounded">
          ✕ 닫기
        </button>
      </div>

      <div class="text-xs text-amber-200 mb-2 px-1 flex items-center justify-between">
        <span>🚩 침공할 적 영지를 선택하면 즉시 해당 영지로 대군이 출진합니다!</span>
        <span class="text-slate-400 text-[11px]">(국경 인접 영지만 공격 가능)</span>
      </div>

      <div id="war-target-list" class="space-y-2 overflow-y-auto max-h-[58vh] pr-1">
        <!-- 동적 렌더링 -->
      </div>

      <div class="pt-3 border-t border-red-900/80 flex items-center justify-between">
        <span class="text-[11px] text-slate-400">💡 지도에서 적 영지를 직접 클릭한 후 [이 적 영지 침공] 버튼을 눌러도 출진할 수 있습니다.</span>
        <button onclick="closeModal('war-target-modal')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-white font-bold text-xs rounded border border-slate-500">
          돌아가기
        </button>
      </div>
    </div>
  </div>
"""

    # 2. battle-modal 내부에 "장수 골라 1:1 결투 개시" 대형 배너 버튼 추가
    duel_in_battle_banner = """
        <!-- 🔥 장수 골라 1:1 결투 (일기토) 완벽 통합 배너 -->
        <div class="p-2.5 bg-gradient-to-r from-red-950 via-amber-950 to-red-950 border-2 border-amber-400 rounded-lg shadow-lg flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl animate-bounce">⚔️</span>
            <div>
              <div class="text-yellow-300 font-black text-xs flex items-center gap-1.5">
                <span>장수 골라 1:1 진검승부 (일기토)!</span>
                <span class="px-1.5 py-0.2 bg-red-800 text-[10px] text-yellow-100 rounded border border-yellow-400">적장 생포 시 즉시 함락</span>
              </div>
              <div class="text-slate-300 text-[11px]">아군 맹장(관우, 장비, 조운 등)을 골라 적장과 1:1로 맞붙습니다!</div>
            </div>
          </div>
          <button onclick="battleStartOfficerDuel()" class="px-3.5 py-2 bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-white font-black text-xs rounded border-2 border-yellow-300 shadow-xl flex items-center gap-1 animate-pulse">
            <span>🗡️</span> 1:1 결투 개시!
          </button>
        </div>
"""

    # 3. 우측 정보 패널 하단에 원클릭 액션 버튼 컨테이너 HTML
    action_btn_container_html = """
        <!-- 🔥 영지 즉시 침공 / 출진 원클릭 액션 버튼 -->
        <div id="panel-action-btn-container" class="mt-2.5 pt-2 border-t border-blue-700/60">
        </div>
"""

    # 4. JS: openWarModal 및 openWarTargetSelectModal 및 battleStartOfficerDuel 구현
    war_logic_js = """
    // ==================== 🔥 인접 적 영지 침공 및 전쟁 시스템 (완전 개편) ====================
    function openWarModal(targetProvId = null, fromProvId = null) {
      closeAllPopups();

      // 1. 공격 목표 적 영지 결정
      let target = null;
      if (targetProvId) {
        target = PROVINCES.find(p => p.id === targetProvId);
      } else {
        const sel = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (sel && sel.ruler !== gameState.rulerName) {
          target = sel; // 유저가 지도에서 적 영지를 선택해둔 상태!
        }
      }

      // 목표 적 영지가 아직 지정되지 않은 경우(아군 영지 선택 또는 전체 전쟁 클릭) 목록 모달 오픈!
      if (!target) {
        openWarTargetSelectModal();
        return;
      }

      // 아군 영지를 대상으로 공격하려 한 경우
      if (target.ruler === gameState.rulerName) {
        alert('아군 영지는 공격할 수 없습니다! 적의 영지를 선택하십시오.');
        openWarTargetSelectModal();
        return;
      }

      // 2. 이 적 영지와 국경이 맞닿아 있는(인접한) 아군 영지들 찾기
      const adjMyProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName && target.adj.includes(p.id));

      if (adjMyProvs.length === 0) {
        alert(`[공격 불가] ${target.id}. ${target.name} (${target.ruler})은(는) 아군 영지와 국경이 맞닿아 있지 않아 직접 공격할 수 없습니다!\\n국경을 맞대고 있는 인접 적 영지를 먼저 공략하십시오.`);
        openWarTargetSelectModal();
        return;
      }

      // 3. 출진할 아군 영지 결정
      let myProv = null;
      if (fromProvId) {
        myProv = adjMyProvs.find(p => p.id === fromProvId);
      }
      if (!myProv) {
        const sel = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (sel && adjMyProvs.some(p => p.id === sel.id)) {
          myProv = sel;
        } else {
          // 인접 아군 영지 중 병력이 가장 많은 곳에서 출진!
          myProv = adjMyProvs.slice().sort((a, b) => b.soldiers - a.soldiers)[0];
        }
      }

      if (myProv.soldiers < 100) {
        alert(`출진할 ${myProv.name}의 병사가 부족합니다! (최소 100명 이상 필요)`);
        return;
      }

      // 4. 전투 데이터 초기화
      battleData.targetProv = target;
      battleData.fromProv = myProv;
      battleData.turn = 1;
      battleData.myPower = 100;
      battleData.enemyPower = 100;
      battleData.mySoldiers = myProv.soldiers;
      battleData.enemySoldiers = target.soldiers;
      battleData.storageHp = gameState.storageHp;

      // 5. 모달 UI 바인딩
      document.getElementById('battle-title').innerText = `[야전 결전] ${myProv.name} ➔ ${target.name} (${gameState.rulerName}군 vs ${target.ruler}군)`;
      document.getElementById('battle-enemy-name').innerText = `⚔️ 적군 (${target.ruler} 수비군: ${target.name})`;
      document.getElementById('battle-enemy-def-tag').innerText = `성벽 방어력: ${target.defense}`;
      document.getElementById('battle-my-soldiers-txt').innerText = myProv.soldiers.toLocaleString();
      document.getElementById('battle-enemy-soldiers-txt').innerText = target.soldiers.toLocaleString();
      document.getElementById('battle-storage-pct').innerText = `${gameState.storageHp}%`;
      document.getElementById('battle-storage-bar').style.width = `${gameState.storageHp}%`;

      document.getElementById('battle-enemy-power-pct').innerText = '100%';
      document.getElementById('battle-enemy-bar').style.width = '100%';
      document.getElementById('battle-my-power-pct').innerText = '100%';
      document.getElementById('battle-my-bar').style.width = '100%';

      document.getElementById('battle-modal-logs').innerHTML = `
        <div class="text-yellow-300 font-bold">🚩 [출진 개시] ${myProv.name}의 아군 ${myProv.soldiers.toLocaleString()}명이 ${target.name}(${target.ruler}군)을 향해 진격을 개시했습니다!</div>
        <div class="text-cyan-200">⚔️ 상단의 [1:1 결투 개시]를 눌러 장수를 골라 적장과 1번씩 맞붙거나, 아래 [총공격]으로 적군을 격멸하십시오!</div>
      `;

      playSfx('war');
      openModal('battle-modal');
    }

    // 침공 목표 적 영지 목록 모달
    function openWarTargetSelectModal() {
      closeAllPopups();
      const myProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName);

      const attackableEnemyProvs = [];
      PROVINCES.forEach(p => {
        if (p.ruler !== gameState.rulerName) {
          const adjMine = myProvs.filter(myP => p.adj.includes(myP.id));
          if (adjMine.length > 0) {
            attackableEnemyProvs.push({
              prov: p,
              fromList: adjMine
            });
          }
        }
      });

      if (attackableEnemyProvs.length === 0) {
        alert('인접한 적의 영지가 없습니다! 영지를 이동하거나 턴을 넘기십시오.');
        return;
      }

      const listEl = document.getElementById('war-target-list');
      if (listEl) {
        listEl.innerHTML = attackableEnemyProvs.map(item => {
          const p = item.prov;
          const fromNames = item.fromList.map(m => `${m.id}.${m.name}(${m.soldiers.toLocaleString()}명)`).join(', ');
          return `
            <div class="p-2.5 rounded bg-blue-950/90 border border-amber-500/60 flex items-center justify-between hover:border-yellow-300 transition shadow">
              <div class="space-y-0.5">
                <div class="flex items-center gap-2">
                  <span class="text-red-400 font-black text-sm">${p.id}. ${p.name}</span>
                  <span class="px-2 py-0.5 rounded text-xs bg-red-900 text-yellow-200 border border-red-500 font-bold">${p.ruler} 군벌</span>
                  <span class="text-xs text-slate-300">병력: <b class="text-yellow-300">${p.soldiers.toLocaleString()}</b>명</span>
                  <span class="text-xs text-slate-300">성벽: <b class="text-cyan-300">${p.defense}</b></span>
                </div>
                <div class="text-[11px] text-emerald-300">
                  🚩 출진 가능 아군 영지: ${fromNames}
                </div>
              </div>
              <button onclick="closeModal('war-target-modal'); openWarModal(${p.id});" class="px-3.5 py-1.5 rounded bg-red-700 hover:bg-red-600 text-yellow-100 font-black text-xs border border-yellow-300 shadow flex items-center gap-1 animate-pulse">
                <span>⚔️</span> 침공 출진!
              </button>
            </div>
          `;
        }).join('');
      }

      openModal('war-target-modal');
    }

    // 야전 중 장수 1:1 일기토 출진 연결
    function battleStartOfficerDuel() {
      if (!battleData.targetProv) return;
      // 일기토 모달에서 해당 적 영지 적장과 맞붙도록 설정
      openDuelSelectModal();
      const provSelect = document.getElementById('duel-enemy-prov-select');
      if (provSelect) {
        provSelect.value = battleData.targetProv.id;
        updateEnemyOfficersList();
      }
    }
"""

    # 5. updateRightPanel 끝부분에 원클릭 액션 버튼 추가 로직 삽입
    panel_btn_inject_js = """
      // 🔥 우측 패널 하단 원클릭 침공 / 출진 버튼 동적 렌더링
      const actionContainer = document.getElementById('panel-action-btn-container');
      if (actionContainer) {
        if (p.ruler !== gameState.rulerName) {
          actionContainer.innerHTML = `
            <button onclick="openWarModal(${p.id})" class="w-full py-2 bg-gradient-to-r from-red-700 to-rose-700 hover:from-red-600 hover:to-rose-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex items-center justify-center gap-1.5 animate-pulse">
              <span>⚔️</span> 이 적 영지 즉시 침공 (전쟁 개시!)
            </button>
          `;
        } else {
          actionContainer.innerHTML = `
            <button onclick="openWarTargetSelectModal()" class="w-full py-2 bg-gradient-to-r from-blue-800 to-indigo-800 hover:from-blue-700 hover:to-indigo-700 text-cyan-100 font-bold text-xs rounded border border-cyan-300 shadow flex items-center justify-center gap-1.5">
              <span>🚩</span> 인접 적 영지 침공 작전 개시
            </button>
          `;
        }
      }
"""

    # 6. duelAction에서 승리 시 야전 결전과 연동하는 로직 강화
    # duelState.enemyHp <= 0 시: battleData.targetProv가 있으면 endBattleVictory() 자동 호출
    duel_victory_patch = """
      if (duelState.enemyHp <= 0) {
        duelState.inDuel = false;
        playSfx('victory');
        logDuel(`🎉🏆 [일기토 완전 승리!] ${my.name}이 ${enemy.name}을 말 아래로 낙마시키고 생포했습니다!!`, 'text-yellow-300 font-extrabold text-sm');
        logMessage(`👑 [일기토 대승] ${my.name}이 적장 ${enemy.name}과의 결투에서 대승을 거두었습니다! (금 500전 노획)`, 'text-yellow-300 font-black');

        if (battleData.targetProv) {
          logMessage(`🚩 [영지 점령] 적장이 일기토에서 격파되어 적군이 총붕괴했습니다! ${battleData.targetProv.name}을 점령했습니다!`, 'text-yellow-300 font-black');
          alert(`🎉🏆 [일기토 대승리!]\n${my.name}이 적장 ${enemy.name}을 베어 적군이 총붕괴하고 패주했습니다!\n${battleData.targetProv.name}을 완전히 점령하여 아군 영지로 편입했습니다!`);
          endBattleVictory();
        } else {
          const myProv = getMyCapital();
          myProv.gold += 500;
          updateRightPanel(myProv.id);
          alert(`🎉 [일기토 승리] ${my.name}이 적장 ${enemy.name}을 격파했습니다!\n적군의 사기가 곤두박질치고 군자금 500전을 전리품으로 획득했습니다!\n(다음 장수를 골라 또 대결할 수 있습니다)`);
        }
        setTimeout(() => closeModal('duel-modal'), 1800);
      }
"""

    # 문자열 치환 수행
    # A. HTML에 war-target-modal 추가 (battle-modal 바로 앞)
    target_needle = '<!-- ==================== 실전 야전 배틀 모달 ==================== -->'
    if target_needle in src:
        src = src.replace(target_needle, war_target_modal_html + "\n" + target_needle)
        print("Successfully added war-target-modal HTML")
    else:
        print("Warning: target_needle for battle-modal not found!")

    # B. battle-modal 내부에 일기토 배너 추가
    # battle-modal-logs 바로 위에 삽입
    target_logs = '<div class="bg-blue-950 border border-blue-800 p-2 rounded max-h-[90px] overflow-y-auto text-xs font-mono text-slate-200 space-y-0.5" id="battle-modal-logs">'
    if target_logs in src:
        src = src.replace(target_logs, duel_in_battle_banner + "\n" + target_logs)
        print("Successfully added duel_in_battle_banner")
    else:
        print("Warning: target_logs not found")

    # C. 우측 패널에 action_btn_container_html 추가
    # rate-horse 주변 또는 panel-defense 하단
    target_panel = '<div class="flex items-center justify-between text-xs font-bold text-slate-200 mb-2 px-1">'
    target_panel_bottom = """      <div class="mt-3 pt-2 border-t border-blue-800/80 text-[11px] text-slate-300 space-y-1">"""
    if target_panel_bottom in src:
        src = src.replace(target_panel_bottom, action_btn_container_html + "\n" + target_panel_bottom)
        print("Successfully added action_btn_container_html to right panel")
    else:
        # 대안: id="rate-horse" 부근
        needle_rate = 'id="rate-horse"'
        if needle_rate in src:
            src = src.replace('</span>\n          </div>\n        </div>', '</span>\n          </div>\n        </div>\n' + action_btn_container_html, 1)
            print("Successfully added action_btn_container_html (alt)")

    # D. openWarModal 교체
    old_war_start = """    // ==================== 실전 야전 결전 모달 ====================
    function openWarModal() {"""
    old_war_end = """      playSfx('war');
      openModal('battle-modal');
    }"""
    
    # regex로 openWarModal 함수 찾아서 교체
    pattern_war = r'// ==================== 실전 야전 결전 모달 ====================\s+function openWarModal\(\) \{[\s\S]*?playSfx\(\'war\'\);\s+openModal\(\'battle-modal\'\);\s+\}'
    if re.search(pattern_war, src):
        src = re.sub(pattern_war, war_logic_js, src)
        print("Successfully replaced openWarModal with improved war logic")
    else:
        # 일반 find로 시도
        idx = src.find('function openWarModal() {')
        if idx != -1:
            idx2 = src.find("openModal('battle-modal');", idx)
            idx3 = src.find("}", idx2)
            src = src[:idx] + war_logic_js + src[idx3+1:]
            print("Successfully replaced openWarModal via find/substring")

    # E. updateRightPanel에 panel_btn_inject_js 삽입
    target_storage = "const storageStatusEl = document.getElementById('food-storage-status');"
    if target_storage in src:
        src = src.replace(target_storage, panel_btn_inject_js + "\n      " + target_storage)
        print("Successfully injected panel action buttons into updateRightPanel")

    # F. duelAction 승리 로직 패치
    pattern_duel_vic = r'if \(duelState\.enemyHp <= 0\) \{[\s\S]*?setTimeout\(\(\) => closeModal\(\'duel-modal\'\), 1800\);\s+\}'
    if re.search(pattern_duel_vic, src):
        src = re.sub(pattern_duel_vic, duel_victory_patch.strip(), src)
        print("Successfully patched duelAction victory logic")

    # 새로운 파이썬 빌더 스크립트 저장
    new_script_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\build_samguk3_war_fixed_runner.py"
    with open(new_script_path, "w", encoding="utf-8") as f:
        f.write(src)
    print(f"Saved new script runner to {new_script_path}")

    # 이제 이 스크립트를 직접 실행하여 HTML 파일들을 빌드!

if __name__ == "__main__":
    main()
