# -*- coding: utf-8 -*-
import os
import re

def build():
    print("=== 출전 장수 편성 & 피로도(연속 출전 제한) 시스템 빌드 시작 ===")

    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 출전 장수 편성 모달 HTML
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
        <span>💡 이번 전투에 출전할 장수를 <strong>최대 3명</strong> 선택하십시오.</span>
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

    # 2. MY_OFFICERS 배열에 fatigue: 0 속성 주입
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

    # 3. 출전 장수 편성 및 피로도 관리 JS 스크립트
    deploy_js = """
    // ==================== ⚔️ 출전 장수 편성 및 피로도(연속 출전 제한) 엔진 ====================
    let deployingTargetProv = null;
    let deployingFromProv = null;
    let selectedDeployOfficerIds = [];

    function openOfficerDeployModal(target, fromProv) {
      closeAllPopups();
      deployingTargetProv = target;
      deployingFromProv = fromProv;
      selectedDeployOfficerIds = [];

      document.getElementById('deploy-modal-title').innerText = `[출전 장수 편성] ${fromProv.name} ➔ ${target.name} 침공`;
      document.getElementById('deploy-target-desc').innerText = `목표: ${target.id}. ${target.name} (${target.ruler}군, 병력: ${target.soldiers.toLocaleString()}명) | 출격지: ${fromProv.name}`;

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
                <!-- 피로도 게이지 바 -->
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

      const idx = selectedDeployOfficerIds.indexOf(offId);
      if (idx !== -1) {
        selectedDeployOfficerIds.splice(idx, 1);
      } else {
        if (selectedDeployOfficerIds.length >= 3) {
          alert('출전 장수는 최대 3명까지 선발할 수 있습니다.');
          return;
        }
        selectedDeployOfficerIds.push(offId);
      }

      playTone(480, 0.08, 'sine', 0.15);
      renderDeployOfficerList();
    }

    function confirmOfficerDeployment() {
      if (selectedDeployOfficerIds.length === 0) {
        alert('최소 1명 이상의 장수를 출전 부대로 선발해야 합니다!');
        return;
      }

      // 출전 장수 피로도 +60 상승 (연속 출전 방지!)
      selectedDeployOfficerIds.forEach(id => {
        const off = MY_OFFICERS.find(o => o.id === id);
        if (off) {
          off.fatigue = Math.min(100, off.fatigue + 60);
          logMessage(`⚠️ [피로 누적] ${off.name}의 전투 피로도가 +60% 상승했습니다. (현재 피로도: ${off.fatigue}%)`, 'text-orange-300 text-[11px]');
        }
      });

      closeModal('officer-deploy-modal');
      playSfx('war');

      // 🔥 선택된 장수들을 거느리고 삼국지 5 헥스 전술 전장으로 출진!
      openHexBattle(deployingTargetProv, deployingFromProv);
    }
"""

    # 4. openWarModal에서 출전 장수 편성 모달 호출로 연결
    pattern_open_war = r"// 🔥 삼국지 5 헥스 전술 전장으로 즉시 진입!\s+openHexBattle\(target,\s*myProv\);\s+return;"
    replacement_open_war = """// 🔥 출전 장수 편성 & 피로도 선택 창 띄우기!
      openOfficerDeployModal(target, myProv);
      return;"""

    if re.search(pattern_open_war, html):
        html = re.sub(pattern_open_war, replacement_open_war, html)
        print("Successfully linked openWarModal to openOfficerDeployModal!")
    else:
        # direct replace
        html = html.replace("openHexBattle(target, myProv);", "openOfficerDeployModal(target, myProv);")
        print("Successfully replaced openHexBattle call with openOfficerDeployModal!")

    # 5. 턴 넘김(executeRest) 시 모든 장수의 피로도 -35% 자연 회복
    pattern_rest = r"function executeRest\(\)\s*\{[\s\S]*?logMessage\('💤 \[휴양\] 턴을 넘겨[\s\S]*?\}\s*\}"
    replacement_rest = """function executeRest() {
      closeAllPopups();
      passTurn();
      playSfx('build');
      
      // 🔥 모든 장수 피로도 -35% 자연 회복!
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        off.fatigue = Math.max(0, off.fatigue - 35);
      });

      logMessage('🍵 [휴양 & 장수 회복] 턴을 넘겨 전 영지의 내정을 정비하고, 모든 장수들의 피로도가 -35% 회복되었습니다!', 'text-emerald-300 font-bold');
      updateRightPanel(gameState.selectedProvId);
    }"""
    if re.search(pattern_rest, html):
        html = re.sub(pattern_rest, replacement_rest, html)
        print("Successfully patched executeRest with fatigue recovery!")

    # 6. 포상(executeReward) 시 장수 피로도 즉시 -50% 회복
    pattern_reward = r"function executeReward\(\)\s*\{[\s\S]*?logMessage\(`💰 \[포상\][\s\S]*?\}\s*\}"
    replacement_reward = """function executeReward() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 150) { alert('장수들에게 하사할 금 150전이 부족합니다.'); return; }
      myProv.gold -= 150;

      // 🔥 전 장수 피로도 즉시 -50% 대폭 회복!
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        off.fatigue = Math.max(0, off.fatigue - 50);
      });

      playSfx('victory');
      alert('🎉 [주연 및 포상 하사!]\\n장수들에게 황금과 주연을 베풀어 사기를 드높였습니다!\\n모든 장수들의 피로도가 즉시 -50% 회복되어 전선 출전이 가능해졌습니다!');
      logMessage('🍖 [포상 및 주연] 장수들에게 연회를 베풀어 전 장수의 피로도가 즉시 -50% 회복되었습니다!', 'text-yellow-300 font-black');
      updateRightPanel(myProv.id);
    }"""
    if re.search(pattern_reward, html):
        html = re.sub(pattern_reward, replacement_reward, html)
        print("Successfully patched executeReward with fatigue instant recovery!")

    # 7. 모달 HTML 주입
    html = html.replace("</body>", deploy_modal_html + "\n</body>")

    # 8. JS 스크립트 주입
    html = html.replace("</script>\n</body>", f"\n{deploy_js}\n</script>\n</body>")

    # 9. 대상 파일 4곳에 저장
    paths = [
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Generated: {p} ({len(html):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 출전 장수 편성 & 피로도 시스템 빌드 완료! ===")

if __name__ == "__main__":
    build()
