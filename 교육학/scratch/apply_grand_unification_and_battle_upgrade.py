# -*- coding: utf-8 -*-
import os
import re

def main():
    print("=== 대망의 천하통일 엔딩 & 지역별 맞춤 전장 & 보물 발굴 & 난이도 밸런스 & 경험치 시스템 빌드 ===")

    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 엔딩 일러스트 Base64 로드
    with open(r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\ending_b64.txt", "r", encoding="utf-8") as f:
        ending_b64 = f.read().strip()
    print(f"엔딩 Base64 로드 완료 ({len(ending_b64)}자)")

    # 2. 천하통일 황제 즉위식 엔딩 모달 HTML 주입
    ending_modal_html = f"""
  <!-- ==================== 👑 대망의 천하통일 황제 즉위식 & 영웅 에필로그 모달 ==================== -->
  <div id="unification-ending-modal" class="fixed inset-0 modal-backdrop z-[9999999] hidden flex items-center justify-center p-3 bg-black/95">
    <div class="koei-box w-full max-w-3xl p-5 rounded-xl shadow-2xl border-4 border-yellow-400 max-h-[95vh] flex flex-col justify-between overflow-y-auto">
      
      <!-- 상단 헤더 -->
      <div class="text-center border-b-2 border-yellow-400 pb-2 mb-3">
        <h2 class="text-xl sm:text-2xl font-black text-yellow-300 text-pixel tracking-widest animate-pulse">
          👑 祝! [천하통일] 대망의 한나라 황제 즉위식 👑
        </h2>
        <div class="text-xs text-amber-200 mt-1 font-bold">
          서기 200여 년, 길고 길었던 난세를 평정하고 천하 13주를 하나로 통일하다!
        </div>
      </div>

      <!-- 황제 즉위식 웅장한 일러스트 -->
      <div class="w-full h-56 sm:h-64 rounded-lg overflow-hidden border-2 border-yellow-500 shadow-2xl mb-3 relative bg-slate-900">
        <img src="{ending_b64}" class="w-full h-full object-cover" alt="황제 즉위식">
        <div class="absolute bottom-2 left-3 bg-black/75 px-3 py-1 rounded border border-yellow-400 text-xs text-yellow-200 font-bold">
          🏛️ 낙양 황궁 대전단: 백관과 만백성의 만세 환호 속 황제 즉위
        </div>
      </div>

      <!-- 감동의 서사시 스토리 본문 -->
      <div class="space-y-3 text-xs text-slate-100 leading-relaxed bg-blue-950/90 p-4 rounded-lg border border-amber-500/80 max-h-56 overflow-y-auto font-sans shadow-inner">
        <p class="text-sm font-bold text-yellow-300">
          "천하는 마침내 어진 성군의 품에서 하나가 되었도다!"
        </p>
        <p>
          십수 년 동안 이어진 군웅할거의 참혹한 난세가 마침내 종식되었습니다.<br>
          <strong class="text-yellow-300 font-black" id="ending-ruler-name">군주 유비 (현덕)</strong>께서는 형주의 작은 신야에서 대의(大義)의 기치를 올린 이래, 조조의 패도와 손권의 강동, 원소의 하북 군세를 어진 인덕과 백성을 위하는 충정으로 모두 평정하고 <strong>천하 13주 전 국토를 완전히 통일</strong>하였습니다!
        </p>
        <p class="text-amber-200 font-bold">
          📜 [낙양 황궁 황제 제단 즉위]
          불타올랐던 낙양의 종묘사직을 웅장하게 재건하고, 구주(九州)의 옥새를 봉안하여 만백성과 백관들의 우레와 같은 만세 삼창 속에 한나라의 정통을 잇는 <strong>대황제(大皇帝)</strong>의 자리에 등극하셨습니다!
        </p>
        <div class="p-3 bg-slate-950/80 rounded-lg border border-amber-500/60 space-y-1.5 text-slate-200">
          <div class="text-amber-300 font-black text-[13px] border-b border-amber-600/40 pb-1 mb-1">🎖️ [개국공신 논공행상 봉작]</div>
          <div>• <strong class="text-emerald-300">대장군 (大將軍) 관우 (운장)</strong>: 청룡언월도를 높이 들며 황제 폐하의 만수무강을 축원하다.</div>
          <div>• <strong class="text-yellow-300">거기장군 (車騎將軍) 장비 (익덕)</strong>: 만인지적의 맹위로 천하를 떨치고 도성을 굳건히 수호하다.</div>
          <div>• <strong class="text-cyan-300">표기장군 (驃騎將軍) 조운 (자룡)</strong>: 상산 조자룡, 황제의 친위대장으로서 만백성의 절대적 존경을 받다.</div>
          <div>• <strong class="text-orange-300">정서대장군 (征西大將軍) 황충 (한승)</strong>: 백발백중의 노익장으로 서방 국경을 굳건히 평정하다.</div>
          <div>• <strong class="text-purple-300">진원장군 (鎭遠將軍) 위연 (문장)</strong>: 한중을 수호한 용맹으로 북방 국경의 안녕을 책임지다.</div>
        </div>
        <p class="text-emerald-300 font-bold">
          백성들은 무기를 거두고 괭이를 들어 풍년을 노래하며, 밤에도 집 대문을 잠그지 않는 <strong>진정한 태평연월(太平烟月)</strong>이 도래하였습니다.<br>
          역사는 오늘을 기록하여 말하길, <em>"어짊으로 천하를 얻고 백성을 자식처럼 아낀 위대한 성군"</em>이라 영원히 기릴 것입니다!
        </p>
      </div>

      <!-- 하단 버튼 바 -->
      <div class="border-t-2 border-yellow-500/80 pt-3 mt-3 flex items-center justify-between gap-3">
        <button onclick="closeModal('unification-ending-modal')" class="px-5 py-2.5 bg-blue-900 hover:bg-blue-800 text-cyan-200 font-bold text-xs rounded-lg border border-cyan-400 shadow">
          🏰 천하 태평성대 자유 통치 계속하기
        </button>
        <button onclick="location.reload()" class="px-6 py-2.5 bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-yellow-100 font-black text-xs rounded-lg border-2 border-yellow-300 shadow-xl flex items-center gap-1.5 animate-pulse">
          <span>🔄</span> 새로운 군주로 천하통일 재도전!
        </button>
      </div>

    </div>
  </div>
"""

    if 'id="unification-ending-modal"' not in html:
        # officer-deploy-modal 앞에 삽입
        html = html.replace('<!-- ==================== ⚔️ 출전 장수 편성 & 피로도 선택 모달 ==================== -->',
                            ending_modal_html.strip() + '\n\n  <!-- ==================== ⚔️ 출전 장수 편성 & 피로도 선택 모달 ==================== -->')
        print("천하통일 엔딩 모달 HTML 주입 완료!")

    # 3. checkUnification 함수를 엔딩 모달 호출로 대개편!
    unify_old = """    function checkUnification() {
      const myCount = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      if (myCount === 13) {
        alert('🎉 경축! 13주를 전면 평정하고 한나라 황제에 즉위하여 천하태평성대를 열었습니다!');
        logMessage('👑 [천하통일 달성] 13주 전 국토를 통일하여 황제의 자리에 올랐습니다!', 'text-yellow-300 font-extrabold');
      }
    }"""

    unify_new = """    function checkUnification() {
      const myCount = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      if (myCount === 13) {
        playSfx('victory');
        logMessage(`👑🏆 [천하통일 대위업 달성!] ${gameState.rulerName} 주군께서 천하 13주를 100% 전면 통일하여 한나라 황제에 즉위하셨습니다!`, 'text-yellow-300 font-black text-sm animate-pulse');
        
        // 엔딩 모달 오픈!
        const rNameEl = document.getElementById('ending-ruler-name');
        if (rNameEl) rNameEl.innerText = `군주 ${gameState.rulerName}`;
        openModal('unification-ending-modal');
      }
    }"""

    if unify_old in html:
        html = html.replace(unify_old, unify_new)
        print("checkUnification 엔딩 모달 호출로 개편 완료!")

    # 4. openWarModal에서 무조건 [출전 장수 편성 모달] 먼저 오픈!
    # "전쟁하기전에 먼저 출전 장수 고를 수 있도록 해주고"
    open_war_call_old = """      // 🔥 삼국지 5 헥스 전술 전장으로 즉시 진입!
      openHexBattle(target, myProv);
      return;"""

    open_war_call_new = """      // ⚔️ 전쟁 돌입 전 반드시 출전 장수 편성 모달(장수 선발 & 피로도 확인)을 먼저 오픈!
      openOfficerDeployModal(target, myProv, false);
      return;"""

    if open_war_call_old in html:
        html = html.replace(open_war_call_old, open_war_call_new)
        print("openWarModal 출전 장수 편성 선행 오픈 연동 완료!")
    else:
        # 혹시 기존 텍스트 형태 검색
        if "openHexBattle(target, myProv);" in html:
            html = html.replace("openHexBattle(target, myProv);", "openOfficerDeployModal(target, myProv, false);")
            print("openWarModal 직행을 openOfficerDeployModal로 교체 완료!")

    # 5. 병사 경험치(gainTroopExp) 및 updateTroopLevelUI 시스템 완비
    troop_exp_js = """
    // ==================== 🎖️ 병종 숙련도 경험치(EXP) & 전직 승급 엔진 ====================
    function gainTroopExp(amount, reason = '') {
      if (gameState.troopExp === undefined) gameState.troopExp = 0;
      if (gameState.troopLevel === undefined) gameState.troopLevel = 1;
      if (gameState.troopTypeName === undefined) gameState.troopTypeName = '보병 (기본)';

      gameState.troopExp += amount;
      if (reason) {
        logMessage(`🎖️ [경험치 획득] ${reason} (+${amount} EXP)`, 'text-yellow-300 font-bold');
      }

      const reqExp = gameState.troopLevel * 100;
      if (gameState.troopExp >= reqExp) {
        gameState.troopExp -= reqExp;
        gameState.troopLevel++;
        playSfx('victory');

        let promoTitle = '';
        let promoDesc = '';
        let promoIcon = '🐎';

        if (gameState.troopLevel === 3) {
          gameState.troopTypeName = '기마병';
          promoTitle = '🎉 [병종 승급] 기마병(騎馬兵) 승급 달성!';
          promoDesc = '병사들이 3레벨에 도달하여 전원 기마병으로 전직했습니다! 평지 돌격력 +35%, 기동력 +1칸 증가!';
          promoIcon = '🐎';
        } else if (gameState.troopLevel === 6) {
          gameState.troopTypeName = '전차병';
          promoTitle = '🎉 [병종 승급] 전차병(戰車兵) 승급 달성!';
          promoDesc = '병사들이 6레벨에 도달하여 철갑 전차병으로 전직했습니다! 적 방어선 돌파 확률 대폭 향상!';
          promoIcon = '🛡️';
        } else if (gameState.troopLevel === 9) {
          gameState.troopTypeName = '중보병';
          promoTitle = '🎉 [병종 승급] 정예 중보병(重步兵) 승급 달성!';
          promoDesc = '병사들이 9레벨에 도달하여 철벽의 중보병으로 전직했습니다! 방어력 +50% 향상!';
          promoIcon = '⚔️';
        }

        if (promoTitle) {
          const tIcon = document.getElementById('promo-icon');
          const tTitle = document.getElementById('promo-title');
          const tDesc = document.getElementById('promo-desc');
          if (tIcon) tIcon.innerText = promoIcon;
          if (tTitle) tTitle.innerText = promoTitle;
          if (tDesc) tDesc.innerText = promoDesc;
          openModal('troop-promotion-modal');
        } else {
          logMessage(`⭐ [부대 숙련도 상승] 아군 병사들의 레벨이 Lv.${gameState.troopLevel}로 올랐습니다! (공방 보정 +${gameState.troopLevel * 4}%)`, 'text-emerald-300 font-black');
        }
      }

      updateTroopLevelUI();
    }

    function updateTroopLevelUI() {
      const typeEl = document.getElementById('panel-troop-type');
      const lvlEl = document.getElementById('panel-troop-lvl');
      const expBar = document.getElementById('panel-troop-exp-bar');
      const expText = document.getElementById('panel-troop-exp-text');
      const multEl = document.getElementById('panel-troop-mult');

      const lvl = gameState.troopLevel || 1;
      const exp = gameState.troopExp || 0;
      const typeName = gameState.troopTypeName || '보병 (기본)';
      const mult = (1.0 + (lvl - 1) * 0.08).toFixed(1);

      if (typeEl) typeEl.innerText = `${typeName}`;
      if (lvlEl) lvlEl.innerText = `Lv. ${lvl}`;
      if (expBar) expBar.style.width = `${Math.min(100, (exp / (lvl * 100)) * 100)}%`;
      if (expText) expText.innerText = `경험치: ${exp} / ${lvl * 100} EXP`;
      if (multEl) multEl.innerText = `공방 ${mult}배`;
    }
"""

    if "function gainTroopExp" not in html:
        insert_marker = "function setDifficulty(level) {"
        html = html.replace(insert_marker, troop_exp_js.strip() + "\n\n    " + insert_marker)
        print("gainTroopExp 및 updateTroopLevelUI 엔진 주입 완료!")

    # 6. 지역별 6대 맞춤 전장 프리셋 & 숨겨진 보물 기믹 엔진 탑재
    regional_battlefields_js = """
    // ==================== 🗺️ 지역별 6대 맞춤 전장 & 숨겨진 보물 기믹 엔진 ====================
    const REGIONAL_MAPS = {
      // 1. 하북 대평원 (유주 1, 기주 2, 청주 3, 연주 4)
      'plains': {
        name: '하북 대평원',
        desc: '광활한 평야와 숲. 기병 돌격에 최적화된 개활지 전장!',
        terrain: [
          [0, 1, 0, 0, 7, 0, 0, 1, 0], // (4, 0) 북방 비밀 초원에 보물!
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 4], // (8, 3) 군량고
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '적토마 (赤兎馬)', stat: '무력 +5, 기동력 +1칸', type: 'war', val: 5 }
      },
      // 2. 서촉 촉도 험산 협곡 (익주 10, 량주 11, 병주 12)
      'mountain': {
        name: '서촉 촉도 험산 협곡',
        desc: '험준한 산악과 좁은 협곡. 낙석과 원거리 궁시 공격에 최적!',
        terrain: [
          [2, 2, 0, 0, 0, 2, 2, 2, 2],
          [2, 0, 0, 7, 2, 2, 0, 0, 2], // (3, 1) 협곡 비밀동굴에 보물!
          [0, 0, 2, 0, 0, 2, 0, 0, 0],
          [0, 2, 0, 0, 0, 0, 2, 0, 4],
          [0, 2, 2, 0, 0, 2, 2, 0, 0],
          [2, 0, 0, 0, 2, 0, 0, 2, 0],
          [2, 2, 0, 0, 0, 0, 2, 2, 2]
        ],
        treasure: { name: '장팔사모 (丈八蛇矛)', stat: '무력 +7 영구 상승', type: 'war', val: 7 }
      },
      // 3. 강동 적벽 수향 수로 (양주 7, 서주 5, 예주 6)
      'water': {
        name: '강동 적벽 수향 수로',
        desc: '거대한 장강 수로와 갈대숲. 수계와 화계 전술의 성지!',
        terrain: [
          [0, 1, 5, 5, 0, 0, 1, 0, 0],
          [1, 0, 5, 5, 5, 0, 0, 0, 0],
          [0, 0, 0, 5, 5, 5, 0, 1, 0],
          [0, 1, 0, 0, 5, 5, 5, 0, 4],
          [0, 0, 1, 0, 0, 5, 5, 7, 0], // (7, 4) 비경 섬에 보물!
          [1, 0, 0, 1, 0, 0, 5, 5, 0],
          [0, 0, 0, 0, 1, 0, 0, 5, 0]
        ],
        treasure: { name: '손자병법서 (孫子兵法)', stat: '지력 +8, 통솔 +6', type: 'int', val: 8 }
      },
      // 4. 중원 낙양 호로관 요새 (사례교위부 13)
      'fortress': {
        name: '중원 낙양 호로관 요새',
        desc: '철벽의 관문 요새와 거대 보급창. 결사항전의 요충지!',
        terrain: [
          [0, 1, 0, 0, 0, 2, 2, 2, 0],
          [1, 0, 0, 0, 2, 2, 3, 2, 0],
          [0, 0, 1, 0, 0, 3, 3, 0, 7], // (8, 2) 황궁 비보!
          [0, 0, 0, 0, 0, 3, 0, 0, 4],
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '의천검 (倚天劍)', stat: '무력 +8 영구 상승', type: 'war', val: 8 }
      },
      // 5. 형주 신야 복합 구릉 (형주 8)
      'hyeongju': {
        name: '형주 신야 복합 구릉',
        desc: '숲과 강, 언덕이 얽힌 천하 요충지 복합 전장!',
        terrain: [
          [0, 7, 1, 0, 0, 5, 0, 1, 0], // (1, 0) 무성 사당 보물!
          [1, 0, 0, 0, 5, 5, 0, 0, 0],
          [0, 0, 1, 0, 5, 0, 1, 0, 0],
          [0, 5, 5, 5, 0, 0, 0, 0, 4],
          [0, 1, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        treasure: { name: '청룡언월도 (靑龍偃月刀)', stat: '무력 +8, 통솔 +5', type: 'war', val: 8 }
      },
      // 6. 남월 교주 밀림 늪 (교주 9)
      'jungle': {
        name: '남월 교주 밀림 맹수 늪',
        desc: '깊은 늪지대와 정글 독천. 턴당 체력 손실 주의!',
        terrain: [
          [1, 6, 6, 1, 0, 0, 1, 6, 0],
          [6, 1, 0, 6, 6, 0, 0, 1, 0],
          [0, 0, 1, 0, 6, 6, 0, 0, 0],
          [1, 0, 0, 0, 0, 6, 1, 0, 4],
          [0, 6, 1, 0, 0, 0, 6, 7, 0], // (7, 4) 부족 제단 보물!
          [6, 1, 0, 1, 6, 0, 0, 6, 0],
          [0, 0, 6, 0, 1, 6, 0, 0, 0]
        ],
        treasure: { name: '태평요술서 (太平要術)', stat: '지력 +10 영구 상승', type: 'int', val: 10 }
      }
    };

    let currentBattleTreasure = null;

    function applyRegionalBattlefield(targetProv) {
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

      // 맵 깊은 복사
      for (let r = 0; r < GRID_ROWS; r++) {
        for (let q = 0; q < GRID_COLS; q++) {
          MAP_TERRAIN[r][q] = preset.terrain[r][q];
        }
      }

      logBattle(`🗺️ [전장 진입] ${targetProv ? targetProv.name : '전장'} - '${preset.name}'에 포진했습니다! (${preset.desc})`);
    }

    // 전설의 보물 히든 발굴 이벤트
    function checkTreasureDiscovery(unit, q, r) {
      if (unit.faction !== 'ally') return;
      if (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] === 7 && currentBattleTreasure && !currentBattleTreasure.found) {
        currentBattleTreasure.found = true;
        MAP_TERRAIN[r][q] = 0; // 평지화
        
        playSound('fanfare');
        const t = currentBattleTreasure;

        // 장수 능력치 가산
        if (t.type === 'war') unit.war += t.val;
        if (t.type === 'int') unit.int += t.val;
        unit.morale = 100;
        UNITS.filter(u => u.faction === 'ally').forEach(u => u.morale = 100);

        logBattle(`🏆✨ [전설의 보물 발굴!] ${unit.name} 장군이 비밀 사당에서 [${t.name}]을(를) 획득했습니다! (${t.stat}, 전군 사기 100 달성!)`);
        logMessage(`🏆✨ [보물 획득!] ${unit.name} 장군이 전장에서 [${t.name}]을(를) 발굴 획득했습니다! (${t.stat})`, 'text-yellow-300 font-extrabold text-sm');

        alert(`🏆✨ [전설의 보물 발굴 성공!]\\n\\n${unit.name} 부대가 전장의 비경에서 [${t.name}]을(를) 발견하였습니다!\\n\\n▶ 효과: ${t.stat}\\n▶ 부대 능력치 영구 상승 & 아군 전 부대 사기 100(최대) 달성!`);
      }
    }
"""

    if "function applyRegionalBattlefield" not in html:
        insert_marker = "function resetHexBattlefield(targetProv, fromProv, deployedOfficers = []) {"
        html = html.replace(insert_marker, regional_battlefields_js.strip() + "\n\n    " + insert_marker)
        print("지역별 6대 전장 및 보물 엔진 주입 완료!")

    # 7. resetHexBattlefield 내부에서 applyRegionalBattlefield 호출 연동
    if "applyRegionalBattlefield(targetProv);" not in html:
        html = html.replace("sam5BattleState.skillMode = null;",
                            "sam5BattleState.skillMode = null;\n      applyRegionalBattlefield(targetProv);")
        print("resetHexBattlefield에 지역별 전장 지형 자동 생성 연동 완료!")

    # 8. 유닛 이동 시 checkTreasureDiscovery 호출 연동
    move_marker_old = "if (q === 8 && r === 3 && !sam5BattleState.supplyBurned) {"
    move_marker_new = "checkTreasureDiscovery(sam5BattleState.selectedUnit, q, r);\n        if (q === 8 && r === 3 && !sam5BattleState.supplyBurned) {"
    if move_marker_old in html and "checkTreasureDiscovery" not in html:
        html = html.replace(move_marker_old, move_marker_new)
        print("유닛 이동 시 보물 발견 연동 완료!")

    # 9. 헥스 캔버스 렌더링에 새 타일(5: 강물, 6: 늪지대, 7: 보물) 시각화 추가
    render_tile_old = """          else if (terrain === 4) tileColor = sam5BattleState.supplyBurned ? "#292524" : "#854d0e"; // 보급창"""
    render_tile_new = """          else if (terrain === 4) tileColor = sam5BattleState.supplyBurned ? "#292524" : "#854d0e"; // 보급창
          else if (terrain === 5) tileColor = "#1e3a8a"; // 강물/수로
          else if (terrain === 6) tileColor = "#4a044e"; // 늪지대/독천
          else if (terrain === 7) tileColor = "#b45309"; // 🏆 전설의 보물 상자"""

    if render_tile_old in html and "tileColor = \"#1e3a8a\";" not in html:
        html = html.replace(render_tile_old, render_tile_new)
        print("캔버스 타일 렌더러에 강물/늪/보물 색상 추가 완료!")

    render_text_old = """          else if (terrain === 4) ctx.fillText(sam5BattleState.supplyBurned ? "💥소실" : "🌾군량고", x, y + 20);"""
    render_text_new = """          else if (terrain === 4) ctx.fillText(sam5BattleState.supplyBurned ? "💥소실" : "🌾군량고", x, y + 20);
          else if (terrain === 5) ctx.fillText("🌊장강", x, y + 20);
          else if (terrain === 6) ctx.fillText("☠️독천", x, y + 20);
          else if (terrain === 7) ctx.fillText("🏆보물", x, y + 20);"""

    if render_text_old in html and "ctx.fillText(\"🏆보물\"" not in html:
        html = html.replace(render_text_old, render_text_new)
        print("캔버스 타일 텍스트에 강물/늪/보물 아이콘 추가 완료!")

    # 10. 전투 시 경험치(EXP) 획득 연동 & 난이도 밸런스 조정
    # 공격 시 gainTroopExp(15, ...)
    dmg_hook_old = """        const dmg = calculateCombatDamage(u, targetUnit, 'melee');
        applyDamage(targetUnit, dmg);

        if (targetUnit.troops > 0) {
          const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.45);
          applyDamage(u, counterDmg);
        }"""

    dmg_hook_new = """        const dmg = calculateCombatDamage(u, targetUnit, 'melee');
        applyDamage(targetUnit, dmg);
        gainTroopExp(15, '돌격 교전');

        if (targetUnit.troops > 0) {
          const counterDmg = Math.floor(calculateCombatDamage(targetUnit, u, 'melee') * 0.65);
          applyDamage(u, counterDmg);
        }"""

    if dmg_hook_old in html:
        html = html.replace(dmg_hook_old, dmg_hook_new)
        print("근접 공격 시 경험치 +15 및 반격 밸런스 조정 완료!")

    # 화계 시 경험치
    fire_hook_old = "sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });"
    fire_hook_new = "sam5BattleState.fireTiles.push({ q: targetPos.q, r: targetPos.r, turns: 3 });\n        gainTroopExp(25, '대화계 성공');"
    if fire_hook_old in html and "gainTroopExp(25, '대화계 성공');" not in html:
        html = html.replace(fire_hook_old, fire_hook_new, 1)
        print("화계 시 경험치 +25 연동 완료!")

    # 혼란 시 경험치
    chaos_hook_old = "targetUnit.acted = true;\n          logBattle(`🌀 [혼란 대성공]"
    chaos_hook_new = "targetUnit.acted = true;\n          gainTroopExp(25, '혼란 계략 성공');\n          logBattle(`🌀 [혼란 대성공]"
    if chaos_hook_old in html and "gainTroopExp(25, '혼란 계략 성공');" not in html:
        html = html.replace(chaos_hook_old, chaos_hook_new)
        print("혼란 시 경험치 +25 연동 완료!")

    # 승리 시 경험치 +60
    win_exp_old = "function triggerVictory(msg) {"
    win_exp_new = "function triggerVictory(msg) {\n      gainTroopExp(60, '10턴 결전 대승리');"
    if win_exp_old in html and "gainTroopExp(60, '10턴 결전 대승리');" not in html:
        html = html.replace(win_exp_old, win_exp_new)
        print("결전 승리 시 경험치 +60 대량 획득 연동 완료!")

    # 11. calculateCombatDamage 난이도 황금 밸런스 튜닝
    combat_calc_old = """    function calculateCombatDamage(attacker, defender, type) {
      const aForm = FORMATIONS[attacker.formation] || FORMATIONS.gyorin;
      const dForm = FORMATIONS[defender.formation] || FORMATIONS.gyorin;

      let atkPower = (attacker.war * 0.65 + attacker.lead * 0.35) * (attacker.troops / 4500);
      let defPower = (defender.lead * 0.65 + defender.war * 0.35) * (defender.troops / 4500);

      if (type === 'archery') {
        atkPower *= aForm.arcMod;
        if (defender.formation === 'bangwon') defPower *= 3.0; // 방원진 활 철벽 방어
      } else {
        atkPower *= aForm.atkMod;
        defPower *= dForm.defMod;
      }

      atkPower *= (attacker.morale / 100);

      // 10턴 내에 승부가 시원하게 나도록 대미지 배율 튜닝 (1.4배)
      let baseDamage = Math.floor(((atkPower / Math.max(10, defPower)) * 1200 + Math.random() * 300) * 1.4);
      return Math.max(400, baseDamage);
    }"""

    combat_calc_new = """    function calculateCombatDamage(attacker, defender, type) {
      const aForm = FORMATIONS[attacker.formation] || FORMATIONS.gyorin;
      const dForm = FORMATIONS[defender.formation] || FORMATIONS.gyorin;

      let atkPower = (attacker.war * 0.60 + attacker.lead * 0.40) * (attacker.troops / 4200);
      let defPower = (defender.lead * 0.60 + defender.war * 0.40) * (defender.troops / 4200);

      if (type === 'archery') {
        atkPower *= aForm.arcMod;
        if (defender.formation === 'bangwon') defPower *= 2.4;
      } else {
        atkPower *= aForm.atkMod;
        defPower *= dForm.defMod;
      }

      atkPower *= (attacker.morale / 100);

      // 🔥 난이도 황금 밸런스 계수 (초급: 1.2배 / 중급: 1.0배 실전 / 상급: 0.9배 긴장감)
      let diffMult = 1.0;
      if (attacker.faction === 'ally') {
        if (gameState.difficulty === 'easy') diffMult = 1.20;
        else if (gameState.difficulty === 'hard') diffMult = 0.90;
      } else {
        if (gameState.difficulty === 'easy') diffMult = 0.85;
        else if (gameState.difficulty === 'hard') diffMult = 1.25;
      }

      // 지형 방어 보너스 (숲: 1.15, 산악: 1.25, 관문: 1.80)
      const terrain = (defender.q >= 0 && defender.r >= 0 && MAP_TERRAIN[defender.r]) ? MAP_TERRAIN[defender.r][defender.q] : 0;
      if (terrain === 1) defPower *= 1.15;
      else if (terrain === 2) defPower *= 1.25;
      else if (terrain === 3) defPower *= 1.80;

      // 아군 병종 숙련도 레벨 보정
      if (attacker.faction === 'ally') {
        const lvl = gameState.troopLevel || 1;
        atkPower *= (1.0 + (lvl - 1) * 0.05);
      }

      let baseDamage = Math.floor(((atkPower / Math.max(10, defPower)) * 950 + Math.random() * 250) * diffMult);
      return Math.max(300, baseDamage);
    }"""

    if combat_calc_old in html:
        html = html.replace(combat_calc_old, combat_calc_new)
        print("calculateCombatDamage 난이도 밸런스 공식 교체 완료!")

    # 12. 파일 저장 및 4개 복사본 전체 동기화
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("데스크톱 파일 저장 완료!")

    for p in [r"C:\Users\LENOVO\Desktop\sam3_update.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
    print("모든 파일 및 Git 저장소 동기화 완료!")

if __name__ == "__main__":
    main()
