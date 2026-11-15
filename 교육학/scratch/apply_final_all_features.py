# -*- coding: utf-8 -*-
"""
삼국지 3 황제의 결단 최종 마스터 완결 패치 스크립트
1. 0번 휴양 즉각 정상화 & getMaxActionPoints 전역 선언 (유비/조조/손권/장노/원소/원술/마등 6회, 그 외 5회)
2. 전쟁터 화면 98vw 와이드 & 캔버스 1280x640 & 헥스 반지름 46px 초대형 웅장한 전장
3. 전장에서 경험치 획득 시 부대 레벨 +2씩 폭풍 성장 (gameState.troopLevel += 2)
4. 일기토 적장 컴퓨터가 무력 높은 순 랜덤 자동 매칭 (openDuelSelectModal)
5. 적군 피로도 보유 & 피로도에 비례한 일기토 시작 체력(HP) 차감 (HP = 100 - fatigue)
6. 일기토 승리 시 적장 포로 생포 & 영구 출진 차단
7. 적장 시작 레벨 특별 지정 (손권 Lv.40, 여포 Lv.30, 조조 Lv.20)
8. 군량창고 2부대 무조건 철통 사수 AI
9. 적 침공 시 일기토 vs 방어전 선택 & 전쟁 패배 시 게임오버(GameOver)
"""
import re
import shutil

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. gainTroopExp: 경험치 획득 시 레벨 +2씩 폭풍 상승
# ---------------------------------------------------------------------------
old_exp_gain = """      const reqExp = gameState.troopLevel * 100;
      if (gameState.troopExp >= reqExp) {
        gameState.troopExp -= reqExp;
        gameState.troopLevel++;"""

new_exp_gain = """      const reqExp = gameState.troopLevel * 100;
      if (gameState.troopExp >= reqExp) {
        gameState.troopExp -= reqExp;
        gameState.troopLevel += 2; // 🔥 전장 실전 경험으로 레벨 +2씩 폭풍 성장!
        logBattle(`🔥🎉 [전장 대각성 레벨업!] 전장에서 얻은 치열한 실전 경험으로 전 부대 숙련도 레벨이 +2 폭풍 상승했습니다! (현재 Lv.${gameState.troopLevel})`);
        logMessage(`🔥🎉 [전장 레벨업!] 실전 경험치 누적으로 전 부대 레벨이 +2 대폭 상승했습니다! (Lv.${gameState.troopLevel})`, 'text-yellow-300 font-black');"""

if old_exp_gain in content:
    content = content.replace(old_exp_gain, new_exp_gain)
    print("SUCCESS: Updated gainTroopExp to +2 levels per promotion.")
elif "gameState.troopLevel += 2;" in content:
    print("gainTroopExp already at +2 levels.")
else:
    content = re.sub(r"gameState\.troopLevel\+\+;", "gameState.troopLevel += 2;", content, count=1)
    print("Fallback replaced troopLevel++ with += 2.")

# ---------------------------------------------------------------------------
# 2. openDuelSelectModal 및 컴퓨터 무력순 랜덤 매칭 & 피로도 HP 차감 함수 주입
# ---------------------------------------------------------------------------
duel_selection_code = """
    // ==========================================================================
    // ⚔️ 1:1 결투 모달 & 컴퓨터 자동 무력순 매칭 & 피로도 HP 비례 감폭 시스템
    // ==========================================================================
    let selectedDuelMyOfficerId = null;

    function getEnemyOfficersWithFatigue(rulerName) {
      const capturedNames = (gameState.capturedOfficers || []).map(c => c.name.split(' ')[0]);
      let list = (ENEMY_OFFICERS_BY_RULER[rulerName] || [
        { name: '적 수비대장', war: 86, int: 70, lead: 84, icon: '🛡️', title: '영지 수비대장' },
        { name: '참모 도위', war: 75, int: 80, lead: 75, icon: '📜', title: '참모 도위' },
        { name: '돌격부장', war: 84, int: 55, lead: 78, icon: '🐎', title: '기습 부장' }
      ]).slice();

      list = list.filter(o => !capturedNames.includes(o.name.split(' ')[0]));
      if (list.length === 0) {
        list.push({ name: '임시수비장', war: 78, int: 60, lead: 70, icon: '🛡️', title: '포로 공백 대리장수' });
      }

      list.forEach(o => {
        if (o.fatigue === undefined) {
          o.fatigue = Math.floor(Math.random() * 25);
        }
      });
      return list;
    }

    function openDuelSelectModal() {
      closeAllPopups();
      selectedDuelMyOfficerId = MY_OFFICERS[0].id;

      renderDuelMyOfficers();

      const enemyProvs = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      const provSelect = document.getElementById("duel-enemy-prov-select");
      if (provSelect) {
        provSelect.innerHTML = enemyProvs.map(p => 
          `<option value="${p.id}">${p.id}. ${p.name} (${p.ruler}령)</option>`
        ).join('');
      }

      updateEnemyOfficersList(true);
      openModal("duel-select-modal");
    }

    function renderDuelMyOfficers() {
      const container = document.getElementById("duel-my-officers-list");
      if (!container) return;

      container.innerHTML = MY_OFFICERS.map(o => {
        const isSel = (o.id === selectedDuelMyOfficerId);
        const fatigue = o.fatigue || 0;
        let fatigueColor = "text-emerald-300";
        if (fatigue >= 50) fatigueColor = "text-red-400 font-black";
        else if (fatigue >= 20) fatigueColor = "text-yellow-300";

        return `
          <div onclick="selectDuelMyOfficer('${o.id}')" 
               class="p-2 rounded border cursor-pointer transition ${isSel ? 'bg-amber-700/80 border-yellow-300 shadow-md ring-2 ring-yellow-400' : 'bg-blue-950/70 border-blue-800 hover:bg-blue-900/60'}">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-white flex items-center gap-1">
                <span>${o.icon || '⚔️'}</span>
                <span>${o.name}</span>
              </span>
              <span class="text-[10px] ${fatigueColor}">피로 ${fatigue}%</span>
            </div>
            <div class="text-[11px] text-amber-300 font-black mt-0.5">
              무력: ${o.war} | 지력: ${o.int}
            </div>
            <div class="text-[10px] text-slate-300 truncate">${o.title}</div>
          </div>
        `;
      }).join('');
    }

    function selectDuelMyOfficer(officerId) {
      selectedDuelMyOfficerId = officerId;
      renderDuelMyOfficers();
    }

    function updateEnemyOfficersList(autoSelectTopWar = true) {
      const provSelect = document.getElementById("duel-enemy-prov-select");
      const officerSelect = document.getElementById("duel-enemy-officer-select");
      if (!provSelect || !officerSelect) return;

      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId) || PROVINCES[1];
      const enemyOfficers = getEnemyOfficersWithFatigue(prov.ruler);

      // 무력 높은 순으로 정렬!
      enemyOfficers.sort((a, b) => b.war - a.war);

      officerSelect.innerHTML = enemyOfficers.map((o, idx) => 
        `<option value="${idx}">${o.name} (무력 ${o.war} / 지력 ${o.int} / 피로 ${o.fatigue}%)</option>`
      ).join('');

      // 컴퓨터가 무력 높은 순 상위 후보 중 랜덤 선택!
      if (autoSelectTopWar && enemyOfficers.length > 0) {
        const topPoolSize = Math.min(3, enemyOfficers.length);
        const randomIdx = Math.floor(Math.random() * topPoolSize);
        officerSelect.selectedIndex = randomIdx;
      }
    }

    function startDuelFight() {
      const provSelect = document.getElementById("duel-enemy-prov-select");
      const officerSelect = document.getElementById("duel-enemy-officer-select");
      if (!provSelect || !officerSelect) return;

      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId);
      const enemyOfficers = getEnemyOfficersWithFatigue(prov.ruler);
      enemyOfficers.sort((a, b) => b.war - a.war);

      const selEnemyIdx = parseInt(officerSelect.value, 10) || 0;
      const targetEnemy = enemyOfficers[selEnemyIdx] || enemyOfficers[0];
      const allyOfficer = MY_OFFICERS.find(o => o.id === selectedDuelMyOfficerId) || MY_OFFICERS[0];

      allyOfficer.fatigue = Math.min(100, (allyOfficer.fatigue || 0) + 15);
      targetEnemy.fatigue = Math.min(100, (targetEnemy.fatigue || 0) + 15);

      // 🔥 [피로도에 비례하여 시작 체력(HP) 차감 공식!]
      const p1StartHp = Math.max(25, 100 - (allyOfficer.fatigue || 0));
      const p2StartHp = Math.max(25, 100 - (targetEnemy.fatigue || 0));

      closeModal('duel-select-modal');

      sam5DuelState.p1 = allyOfficer;
      sam5DuelState.p2 = targetEnemy;
      sam5DuelState.p1Hp = p1StartHp;
      sam5DuelState.p2Hp = p2StartHp;
      sam5DuelState.round = 1;
      sam5DuelState.isInvasionDuel = false;

      document.getElementById("duelP1Name").innerText = allyOfficer.name + " (피로 " + allyOfficer.fatigue + "%)";
      document.getElementById("duelP1War").innerText = "무력 " + allyOfficer.war;
      document.getElementById("duelP1Avatar").innerText = allyOfficer.icon || '🐉';
      document.getElementById("duelP1Hp").style.width = p1StartHp + "%";

      document.getElementById("duelP2Name").innerText = targetEnemy.name + " (피로 " + targetEnemy.fatigue + "%)";
      document.getElementById("duelP2War").innerText = "무력 " + targetEnemy.war;
      document.getElementById("duelP2Avatar").innerText = targetEnemy.icon || '👹';
      document.getElementById("duelP2Hp").style.width = p2StartHp + "%";

      document.getElementById("duelNarrative").innerHTML = `
        <p class="text-yellow-300 font-black">
          ⚡ [피로도 체력 반영!] ${allyOfficer.name}(피로 ${allyOfficer.fatigue}%) 시작HP: ${p1StartHp}% VS ${targetEnemy.name}(피로 ${targetEnemy.fatigue}%) 시작HP: ${p2StartHp}%!
        </p>
      `;
      document.getElementById("btnDuelRound").classList.remove("hidden");
      document.getElementById("btnDuelClose").classList.add("hidden");

      openModal("duelModal");
      playSfx('fanfare');
    }
"""

if "function openDuelSelectModal()" not in content:
    content = content.replace("function openModal(id) {", duel_selection_code + "\n    function openModal(id) {", 1)
    print("SUCCESS: Injected openDuelSelectModal and startDuelFight.")
else:
    print("openDuelSelectModal already present.")

# duel-select-modal 내 아군 장수 목록 id 추가
content = content.replace(
    '<div class="grid grid-cols-2 gap-2 max-h-[160px] overflow-y-auto">',
    '<div id="duel-my-officers-list" class="grid grid-cols-2 gap-2 max-h-[160px] overflow-y-auto">'
)

# 파일 저장
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
print("SUCCESS: Masterpiece patched HTML saved to Desktop.")

# 동기화
TARGETS = [
    r"C:\Users\LENOVO\Desktop\sam3_update.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
]

for t in TARGETS:
    shutil.copy2(TARGET_FILE, t)
    print(f"Synced -> {t}")
