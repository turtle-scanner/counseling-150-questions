// -*- coding: utf-8 -*-
const fs = require('fs');

const file = 'C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html';
let content = fs.readFileSync(file, 'utf8');

console.log('=== [1/2] 1:1 결투 모달 & 무력순 랜덤 적장 매칭 & 피로도 HP 연동 구현 ===');

const duelSelectionJs = `
    // ==========================================================================
    // ⚔️ 1:1 결투 모달 & 컴퓨터 자동 무력순 매칭 & 피로도 HP 비례 감폭 시스템
    // ==========================================================================
    let selectedDuelMyOfficerId = null;

    // 적 장수 DB에 피로도(fatigue) 속성 보장
    function getEnemyOfficersWithFatigue(rulerName) {
      const capturedNames = (gameState.capturedOfficers || []).map(c => c.name.split(' ')[0]);
      let list = (ENEMY_OFFICERS_BY_RULER[rulerName] || [
        { name: '적 수비대장', war: 86, int: 70, lead: 84, icon: '🛡️', title: '영지 수비대장' },
        { name: '참모 도위', war: 75, int: 80, lead: 75, icon: '📜', title: '참모 도위' },
        { name: '돌격부장', war: 84, int: 55, lead: 78, icon: '🐎', title: '기습 부장' }
      ]).slice();

      // 포로로 잡힌 장수 영구 제외!
      list = list.filter(o => !capturedNames.includes(o.name.split(' ')[0]));
      if (list.length === 0) {
        list.push({ name: '임시수비장', war: 78, int: 60, lead: 70, icon: '🛡️', title: '포로 공백 대리장수' });
      }

      // 피로도 초기화 및 누적값 보장
      list.forEach(o => {
        if (o.fatigue === undefined) {
          // 적군도 0~35% 사이의 실시간 피로도 보유
          o.fatigue = Math.floor(Math.random() * 25);
        }
      });
      return list;
    }

    // 1:1 결투 선택 모달 오픈
    function openDuelSelectModal() {
      closeAllPopups();
      selectedDuelMyOfficerId = MY_OFFICERS[0].id;

      // 1. 아군 장수 목록 렌더링 (피로도 포함)
      renderDuelMyOfficers();

      // 2. 적 영지 셀렉트 렌더링
      const enemyProvs = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      const provSelect = document.getElementById("duel-enemy-prov-select");
      if (provSelect) {
        provSelect.innerHTML = enemyProvs.map(p => 
          \`<option value="\${p.id}">\${p.id}. \${p.name} (\${p.ruler}령)</option>\`
        ).join('');
      }

      // 3. 적 장수 무력순 랜덤 자동 매칭!
      updateEnemyOfficersList(true); // true: 컴퓨터 자동 랜덤 선택

      openModal("duel-select-modal");
    }

    // 아군 장수 목록 렌더링
    function renderDuelMyOfficers() {
      const container = document.getElementById("duel-my-officers-list");
      if (!container) return;

      container.innerHTML = MY_OFFICERS.map(o => {
        const isSel = (o.id === selectedDuelMyOfficerId);
        const fatigue = o.fatigue || 0;
        let fatigueColor = "text-emerald-300";
        if (fatigue >= 50) fatigueColor = "text-red-400 font-black";
        else if (fatigue >= 20) fatigueColor = "text-yellow-300";

        return \`
          <div onclick="selectDuelMyOfficer('\${o.id}')" 
               class="p-2 rounded border cursor-pointer transition \${isSel ? 'bg-amber-700/80 border-yellow-300 shadow-md ring-2 ring-yellow-400' : 'bg-blue-950/70 border-blue-800 hover:bg-blue-900/60'}">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-white flex items-center gap-1">
                <span>\${o.icon || '⚔️'}</span>
                <span>\${o.name}</span>
              </span>
              <span class="text-[10px] \${fatigueColor}">피로 \${fatigue}%</span>
            </div>
            <div class="text-[11px] text-amber-300 font-black mt-0.5">
              무력: \${o.war} | 지력: \${o.int}
            </div>
            <div class="text-[10px] text-slate-300 truncate">\${o.title}</div>
          </div>
        \`;
      }).join('');
    }

    function selectDuelMyOfficer(officerId) {
      selectedDuelMyOfficerId = officerId;
      renderDuelMyOfficers();
    }

    // 적 영지 변경 시 적장 목록 갱신 (컴퓨터가 무력 상위 중 랜덤 자동 선택)
    function updateEnemyOfficersList(autoSelectTopWar = true) {
      const provSelect = document.getElementById("duel-enemy-prov-select");
      const officerSelect = document.getElementById("duel-enemy-officer-select");
      if (!provSelect || !officerSelect) return;

      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId) || PROVINCES[1];
      const enemyOfficers = getEnemyOfficersWithFatigue(prov.ruler);

      // 🔥 무력 높은 순으로 정렬!
      enemyOfficers.sort((a, b) => b.war - a.war);

      officerSelect.innerHTML = enemyOfficers.map((o, idx) => 
        \`<option value="\${idx}">\${o.name} (무력 \${o.war} / 지력 \${o.int} / 피로 \${o.fatigue}%)</option>\`
      ).join('');

      // 🎲 [컴퓨터가 무력 높은 순 상위 후보 중 랜덤 선택!]
      if (autoSelectTopWar && enemyOfficers.length > 0) {
        // 무력 상위 1~3위 중 무작위 선택
        const topPoolSize = Math.min(3, enemyOfficers.length);
        const randomIdx = Math.floor(Math.random() * topPoolSize);
        officerSelect.selectedIndex = randomIdx;
      }
    }

    // ⚔️ 결투 개시! (피로도에 비례한 시작 HP 차감 연동)
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

      // 결투 출전으로 피로도 +15% 누적!
      allyOfficer.fatigue = Math.min(100, (allyOfficer.fatigue || 0) + 15);
      targetEnemy.fatigue = Math.min(100, (targetEnemy.fatigue || 0) + 15);

      // 🔥 [피로도에 비례하여 시작 체력(HP) 차감 공식!]
      // 피로도 0% = HP 100, 피로도 20% = HP 80, 피로도 50% = HP 50 (최소 25 보장)
      const p1StartHp = Math.max(25, 100 - (allyOfficer.fatigue || 0));
      const p2StartHp = Math.max(25, 100 - (targetEnemy.fatigue || 0));

      closeModal('duel-select-modal');

      sam5DuelState.p1 = allyOfficer;
      sam5DuelState.p2 = targetEnemy;
      sam5DuelState.p1Hp = p1StartHp;
      sam5DuelState.p2Hp = p2StartHp;
      sam5DuelState.round = 1;
      sam5DuelState.isInvasionDuel = false; // 일반 결투

      document.getElementById("duelP1Name").innerText = \`\${allyOfficer.name} (피로 \${allyOfficer.fatigue}%)\`;
      document.getElementById("duelP1War").innerText = \`무력 \${allyOfficer.war}\`;
      document.getElementById("duelP1Avatar").innerText = allyOfficer.icon || '🐉';
      document.getElementById("duelP1Hp").style.width = \`\${p1StartHp}%\`;

      document.getElementById("duelP2Name").innerText = \`\${targetEnemy.name} (피로 \${targetEnemy.fatigue}%)\`;
      document.getElementById("duelP2War").innerText = \`무력 \${targetEnemy.war}\`;
      document.getElementById("duelP2Avatar").innerText = targetEnemy.icon || '👹';
      document.getElementById("duelP2Hp").style.width = \`\${p2StartHp}%\`;

      document.getElementById("duelNarrative").innerHTML = \`
        <p class="text-yellow-300 font-black">
          ⚡ [피로도 체력 반영!] \${allyOfficer.name}(피로 \${allyOfficer.fatigue}%) 시작HP: \${p1StartHp}% VS \${targetEnemy.name}(피로 \${targetEnemy.fatigue}%) 시작HP: \${p2StartHp}%!
        </p>
      \`;
      document.getElementById("btnDuelRound").classList.remove("hidden");
      document.getElementById("btnDuelClose").classList.add("hidden");

      openModal("duelModal");
      playSfx('fanfare');
    }
`;

content = content.replace('function openModal(modalId) {', duelSelectionJs + '\n    function openModal(modalId) {');

console.log('=== [2/2] duel-select-modal 내 아군 장수 목록 컨테이너 ID 매핑 ===');

// duel-select-modal HTML 내 아군 장수 목록 영역에 id="duel-my-officers-list" 추가
const oldMyOfficersBox = `<div class="grid grid-cols-2 gap-2 max-h-[160px] overflow-y-auto">`;
const newMyOfficersBox = `<div id="duel-my-officers-list" class="grid grid-cols-2 gap-2 max-h-[160px] overflow-y-auto">`;

if (content.includes(oldMyOfficersBox)) {
  content = content.replace(oldMyOfficersBox, newMyOfficersBox);
  console.log('Added id duel-my-officers-list to duel select modal markup.');
}

fs.writeFileSync(file, content, 'utf8');
console.log('SUCCESS: All duel random matching, enemy fatigue, and HP reduction features applied!');
