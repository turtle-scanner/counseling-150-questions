# -*- coding: utf-8 -*-
import os
import re

def main():
    print("=== 전쟁 종료 후 지도로 복귀 & 민충 100 지원병 8000명 시스템 빌드 시작 ===")

    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. closeHexBattle 및 confirmExitBattleToMap 함수 추가
    close_hex_js = """
    // ==================== 🗺️ 헥스 전장 ➔ 전국 지도 안전 복귀 시스템 ====================
    function confirmExitBattleToMap() {
      if (confirm("전쟁에서 철수하여 전국 지도로 복귀하시겠습니까?\\n(현재 전투가 종료되고 본거지 지도로 안전하게 이동합니다)")) {
        closeHexBattle(false);
      }
    }

    function closeHexBattle(isVictory = false) {
      closeModal('hex-battle-modal');
      sam5BattleState.battleOver = true;

      if (isVictory) {
        if (hexBattleContext.targetProv) {
          onHexBattleVictory(hexBattleContext.targetProv);
        } else {
          renderMapPins();
          updateRightPanel(gameState.selectedProvId);
        }
      } else {
        logMessage('🐎 [전장 퇴각] 본대로 전군 퇴각하여 전국 지도로 안전하게 복귀했습니다.', 'text-slate-300 font-bold');
        const returnProvId = (hexBattleContext.fromProv && hexBattleContext.fromProv.id) ? hexBattleContext.fromProv.id : gameState.selectedProvId;
        updateRightPanel(returnProvId);
        renderMapPins();
      }
    }
"""

    if "function closeHexBattle" not in html:
        # restartBattle 뒤에 삽입
        target_marker = "function restartBattle() {"
        html = html.replace(target_marker, close_hex_js.strip() + "\n\n    " + target_marker)
        print("closeHexBattle 및 confirmExitBattleToMap 함수 추가 완료!")

    # 2. triggerVictory & triggerDefeat 수정 (전투 종료 시 지도로 복귀 연동)
    trigger_old = """    function triggerVictory(msg) {
      if (sam5BattleState.battleOver) return;
      sam5BattleState.battleOver = true;
      playSound('fanfare');
      alert(`🎉 [대승리 - 10턴 결전 완료]\\n\\n${msg}\\n소요 턴: ${sam5BattleState.turn}턴만에 완벽한 승리를 거두었습니다!`);
      logBattle(`🏆 대승리! ${msg}`);
    }

    function triggerDefeat(msg) {
      if (sam5BattleState.battleOver) return;
      sam5BattleState.battleOver = true;
      playSound('fire');
      alert(`💀 [작전 실패 - 시간 초과 패배]\\n\\n${msg}`);
      logBattle(`통한의 패배: ${msg}`);
    }"""

    trigger_new = """    function triggerVictory(msg) {
      if (sam5BattleState.battleOver) return;
      sam5BattleState.battleOver = true;
      playSound('fanfare');
      
      const targetName = (hexBattleContext.targetProv && hexBattleContext.targetProv.name) ? hexBattleContext.targetProv.name : '적 영지';
      logBattle(`🏆 대승리! ${msg}`);
      logMessage(`🎉🏆 [전쟁 대승리!] ${targetName}을(를) 격파하고 완전히 점령했습니다! 전국 지도로 개선 복귀합니다.`, 'text-yellow-300 font-black text-sm');

      alert(`🎉🏆 [대승리 - 10턴 결전 승리!]\\n\\n${msg}\\n소요 턴: ${sam5BattleState.turn}턴만에 완벽한 승리를 거두었습니다!\\n\\n▶ [확인]을 누르면 전국 지도로 복귀하여 영지를 점령하고 포로를 처분합니다.`);
      
      // 즉시 전국 지도로 복귀하며 영지 점령 및 포로 처분 모달 호출!
      closeHexBattle(true);
    }

    function triggerDefeat(msg) {
      if (sam5BattleState.battleOver) return;
      sam5BattleState.battleOver = true;
      playSound('fire');
      logBattle(`통한의 패배: ${msg}`);
      logMessage(`⚠️ [작전 실패] ${msg} 본대로 전군 퇴각하여 전국 지도로 복귀합니다.`, 'text-red-400 font-bold');

      alert(`💀 [작전 실패 - 본대 퇴각]\\n\\n${msg}\\n\\n전군 퇴각하여 본진(전국 지도)으로 안전하게 철수합니다.`);
      
      // 전국 지도로 안전 복귀!
      closeHexBattle(false);
    }"""

    if trigger_old in html:
        html = html.replace(trigger_old, trigger_new)
        print("triggerVictory / triggerDefeat 지도로 복귀 연동 완료!")
    else:
        # 혹시 줄바꿈 차이가 있을 경우 정규식 교체 시도
        pattern = re.compile(r'function triggerVictory\(msg\) \{[\s\S]*?logBattle\(`통한의 패배: \$\{msg\}`\);\s*\}', re.MULTILINE)
        if pattern.search(html):
            html = pattern.sub(trigger_new.strip(), html)
            print("정규식으로 triggerVictory / triggerDefeat 지도로 복귀 연동 완료!")

    # 3. checkVictoryCondition 적장 이름 동적 개선
    check_victory_old = """      if (boss && boss.troops <= 0) {
        triggerVictory("동탁군의 총대장 여포가 퇴각했습니다! 적 군세가 붕괴하여 대승을 거두었습니다!");
      } else if (!enemiesAlive) {
        triggerVictory("동탁군 전 부대를 궤멸시켰습니다! 천하에 이름을 떨친 완벽한 승리입니다!");
      } else if (!alliesAlive) {
        triggerDefeat("연합군 전 부대가 전멸하여 패배했습니다...");
      }"""

    check_victory_new = """      const targetRuler = (hexBattleContext.targetProv && hexBattleContext.targetProv.ruler) ? hexBattleContext.targetProv.ruler : '적';
      if (boss && boss.troops <= 0) {
        triggerVictory(`${targetRuler}군의 총대장 ${boss.name}이(가) 퇴각했습니다! 적 군세가 붕괴하여 대승을 거두었습니다!`);
      } else if (!enemiesAlive) {
        triggerVictory(`${targetRuler}군 전 부대를 궤멸시켰습니다! 천하에 이름을 떨친 완벽한 승리입니다!`);
      } else if (!alliesAlive) {
        triggerDefeat("아군 전 부대가 전멸하여 패배했습니다...");
      }"""

    if check_victory_old in html:
        html = html.replace(check_victory_old, check_victory_new)
        print("checkVictoryCondition 적장명 동적화 완료!")

    # 4. hex-battle-modal 상단 헤더 우측에 눈에 띄는 [🗺️ 전국 지도로 복귀] 버튼 탑재
    header_btn_old = """        <button onclick="closeHexBattle(false)" class="sam5-btn px-3 py-1 rounded text-xs bg-red-900 text-white font-bold border border-red-500">
          🏳️ 퇴각 (전장 이탈)
        </button>"""

    header_btn_new = """        <div class="flex items-center gap-2">
          <button onclick="confirmExitBattleToMap()" class="px-4 py-1.5 rounded text-xs bg-gradient-to-r from-blue-700 via-indigo-700 to-blue-800 hover:from-blue-600 hover:to-indigo-600 text-yellow-200 border-2 border-yellow-400 font-black shadow-lg flex items-center gap-1.5 animate-pulse">
            <span>🗺️</span> <span>전국 지도로 복귀 (퇴각)</span>
          </button>
          <button onclick="confirmExitBattleToMap()" class="text-slate-400 hover:text-white font-mono text-sm px-2 py-0.5 border border-slate-600 rounded">
            ✕
          </button>
        </div>"""

    if header_btn_old in html:
        html = html.replace(header_btn_old, header_btn_new)
        print("헥스 전장 상단 [전국 지도로 복귀] 버튼 보강 완료!")

    # 5. 하단 btnEndTurn 옆에도 [🗺️ 지도로 복귀] 버튼 추가
    end_turn_block_old = """        <!-- 턴 종료 버튼 -->
        <div class="mt-3 pt-2 border-t border-yellow-900/60">
          <button onclick="endPlayerTurn()" id="btnEndTurn" class="w-full sam5-btn py-2.5 rounded text-xs bg-gradient-to-r from-red-950 via-red-900 to-amber-900 hover:from-red-800 hover:to-amber-800 text-yellow-200 border-yellow-500 font-black shadow-lg flex items-center justify-center gap-1.5">
            <span>🚩</span> <span>아군 턴 종료 (적군 행동 개시)</span>
          </button>
        </div>"""

    end_turn_block_new = """        <!-- 턴 종료 & 지도로 복귀 버튼 바 -->
        <div class="mt-3 pt-2 border-t border-yellow-900/60 flex items-center gap-2">
          <button onclick="endPlayerTurn()" id="btnEndTurn" class="flex-1 sam5-btn py-2.5 rounded text-xs bg-gradient-to-r from-red-950 via-red-900 to-amber-900 hover:from-red-800 hover:to-amber-800 text-yellow-200 border-yellow-500 font-black shadow-lg flex items-center justify-center gap-1.5">
            <span>🚩</span> <span>아군 턴 종료</span>
          </button>
          <button onclick="confirmExitBattleToMap()" class="px-3 sam5-btn py-2.5 rounded text-xs bg-blue-950 hover:bg-blue-900 text-cyan-200 hover:text-white border border-cyan-400 font-black shadow flex items-center justify-center gap-1">
            <span>🗺️</span> <span>지도로 복귀</span>
          </button>
        </div>"""

    if end_turn_block_old in html:
        html = html.replace(end_turn_block_old, end_turn_block_new)
        print("헥스 전장 하단 턴 종료 옆 [지도로 복귀] 버튼 추가 완료!")

    # 6. 민충 100 달성 시 정예 의용 지원병 8000명 대거 집결 시스템
    volunteers_js = """
    // ==================== 👥 민충 100 달성 시 의용 지원병 8,000명 집결 시스템 ====================
    function checkMaxLoyaltyVolunteers(prov) {
      if (!prov || prov.ruler !== gameState.rulerName) return;
      if (prov.loyalty >= 100 && !prov.volunteersJoined) {
        prov.volunteersJoined = true;
        const rewardSoldiers = 8000;
        prov.soldiers += rewardSoldiers;
        playSfx('victory');

        logMessage(`🎉👥 [의용 지원병 8,000명 대거 집결!] ${prov.name}의 백성 충성도(민충)가 100(만점)을 달성하여, 주군의 높은 인덕에 감복한 정예 의용군 8,000명이 스스로 무기를 들고 자원입대했습니다! (병사: +8,000명)`, 'text-emerald-300 font-black text-sm animate-pulse');

        alert(`🎉👥 [선정의 결실 - 의용 지원병 8,000명 대거 집결!]\\n\\n${prov.name} 백성들의 민충(民忠)이 100(만점)에 도달했습니다!\\n\\n"유비 주군과 같은 어진 성군을 위해 목숨 바쳐 싸우겠습니다!"\\n\\n향토 청년들과 정예 의용군 8,000명이 스스로 무기를 들고 군에 자원입대하였습니다!\\n\\n▶ ${prov.name} 병력: +8,000명 대거 합류!\\n▶ 현재 총 병력: ${prov.soldiers.toLocaleString()}명`);

        renderMapPins();
        updateRightPanel(prov.id);
      }
    }
"""

    if "function checkMaxLoyaltyVolunteers" not in html:
        insert_marker = "function updateRightPanel(provId) {"
        html = html.replace(insert_marker, volunteers_js.strip() + "\n\n    " + insert_marker)
        print("checkMaxLoyaltyVolunteers 함수 추가 완료!")

    # updateRightPanel 내부에 checkMaxLoyaltyVolunteers 호출 및 안내문구 주입
    # document.getElementById('bar-loy').style.width = p.loyalty + '%'; 바로 뒤
    loy_update_old = "document.getElementById('bar-loy').style.width = p.loyalty + '%';"
    loy_update_new = """document.getElementById('bar-loy').style.width = p.loyalty + '%';
      checkMaxLoyaltyVolunteers(p);

      const loyHintEl = document.getElementById('loyalty-volunteers-hint');
      if (loyHintEl) {
        if (p.ruler === gameState.rulerName) {
          if (p.volunteersJoined) {
            loyHintEl.innerHTML = '<span class=\"text-emerald-300 font-bold\">✨ 민충 100 달성 완료 (의용군 8,000명 참전 완료)</span>';
          } else {
            loyHintEl.innerHTML = `<span class=\"text-amber-300 font-bold animate-pulse\">💡 민충 100 달성 시: 정예 의용 지원병 8,000명 즉시 자원입대! (현재: ${p.loyalty}/100)</span>`;
          }
        } else {
          loyHintEl.innerHTML = '';
        }
      }"""

    if loy_update_old in html and "checkMaxLoyaltyVolunteers(p);" not in html:
        html = html.replace(loy_update_old, loy_update_new)
        print("updateRightPanel에 민충 100 의용군 체크 연동 완료!")

    # 우측 패널 HTML의 민충 행 아래에 <div id="loyalty-volunteers-hint"> 안내 추가
    loy_html_old = """          <div class="flex items-center justify-between gap-2">
            <span class="text-yellow-400 w-10">민충</span>
            <div class="flex-1 gauge-container"><div id="bar-loy" class="gauge-gold" style="width: 60%;"></div></div>
            <span id="val-loy" class="w-16 text-right font-mono text-yellow-300">60</span>
          </div>"""

    loy_html_new = """          <div class="flex items-center justify-between gap-2">
            <span class="text-yellow-400 w-10">민충</span>
            <div class="flex-1 gauge-container"><div id="bar-loy" class="gauge-gold" style="width: 60%;"></div></div>
            <span id="val-loy" class="w-16 text-right font-mono text-yellow-300">60</span>
          </div>
          <div id="loyalty-volunteers-hint" class="text-[10px] text-right px-1 -mt-1 mb-1">
            <span class="text-amber-300 font-bold">💡 민충 100 달성 시: 의용 지원병 8,000명 합류!</span>
          </div>"""

    if loy_html_old in html:
        html = html.replace(loy_html_old, loy_html_new)
        print("우측 패널에 민충 100 지원병 8,000명 안내 텍스트 추가 완료!")

    # 7. 주민선정(executeRelief) 구휼 시 민충 100 체크 연동
    relief_old = """    function executeRelief() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.food < 1000) {
        alert("⚠️ 구휼을 위한 군량이 부족합니다! (군량 1,000석 필요)");
        return;
      }
      myProv.food -= 1000;
      myProv.loyalty = Math.min(100, myProv.loyalty + 8);
      myProv.pop = Math.min(800000, myProv.pop + 2000);
      playSfx('build');
      updateRightPanel(myProv.id);
      logMessage(`🌾 [주민 구휼] 곡식 1,000석을 백성들에게 무상 급여하여 민심(민충)이 8 상승하고 유민들이 유입되었습니다!`, 'text-cyan-200 font-bold');
      alert(`🌾 [선정 및 구휼]\\n\\n군량 1,000석을 굶주린 백성들에게 풀어 민심을 크게 얻었습니다!\\n- 영지 민충 +8 상승\\n- 피난민 유입 (인구 +2,000명)`);
    }"""

    relief_new = """    function executeRelief() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.food < 1000) {
        alert("⚠️ 구휼을 위한 군량이 부족합니다! (군량 1,000석 필요)");
        return;
      }
      myProv.food -= 1000;
      myProv.loyalty = Math.min(100, myProv.loyalty + 10);
      myProv.pop = Math.min(800000, myProv.pop + 2500);
      playSfx('build');
      
      logMessage(`🌾 [주민 구휼] 곡식 1,000석을 백성들에게 무상 급여하여 민충이 ${myProv.loyalty}/100으로 상승했습니다! (인구 +2,500명)`, 'text-cyan-200 font-bold');

      // 민충 100 도달 시 즉시 지원병 8,000명 집결 체크!
      checkMaxLoyaltyVolunteers(myProv);

      updateRightPanel(myProv.id);
      
      if (myProv.loyalty < 100) {
        alert(`🌾 [선정 및 주민 구휼]\\n\\n군량 1,000석을 굶주린 백성들에게 풀어 민심을 크게 얻었습니다!\\n- 현재 영지 민충: ${myProv.loyalty} / 100 (+10 상승)\\n- 피난민 유입 (인구 +2,500명)\\n\\n💡 민충 100 달성 시: 정예 의용 지원병 8,000명이 대거 자원입대합니다!`);
      }
    }"""

    if relief_old in html:
        html = html.replace(relief_old, relief_new)
        print("executeRelief 구휼 시 민충 100 지원병 연동 완료!")

    # 8. 파일 저장 및 동기화
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("데스크톱 타겟 파일 저장 완료!")

    for p in [r"C:\Users\LENOVO\Desktop\sam3_update.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
    print("모든 파일 동기화 완료!")

if __name__ == "__main__":
    main()
