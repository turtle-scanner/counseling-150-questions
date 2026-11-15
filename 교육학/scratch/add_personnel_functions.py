# -*- coding: utf-8 -*-
target_path = r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html'
with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

personnel_code = """
    // ==================== 2. 인사 (포상, 장수수색, 주민구휼) ====================
    function executeReward() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 300) {
        alert(`⚠️ 군자금이 부족합니다! (포상/연회 비용: 금 300전 필요, 현재 보유: 금 ${myProv.gold}전)`);
        return;
      }
      myProv.gold -= 300;
      playSfx('build');

      // 전 장수 피로도 50% 대폭 회복!
      MY_OFFICERS.forEach(off => {
        if (off.fatigue === undefined) off.fatigue = 0;
        off.fatigue = Math.max(0, off.fatigue - 50);
      });

      updateRightPanel(myProv.id);
      logMessage(`🍖 [연회 및 포상] 금 300전을 하사하여 성대한 연회를 베풀었습니다! 전 장수의 피로도가 50% 회복되었습니다!`, 'text-emerald-300 font-black');
      alert(`🍖 [포상 및 성대한 연회]\\n\\n군자금 300전을 하사하여 맹장들과 군사들을 위로했습니다!\\n- 전 장수 피로도 50% 즉각 회복!\\n- 관우, 장비, 조운 등 맹장들의 사기가 드높아졌습니다!`);
    }

    function executeSearchOfficer() {
      closeAllPopups();
      const myProv = getMyCapital();
      playSfx('select');
      const foundNames = ['방통 (봉추)', '서서 (원직)', '마량 (백미)', '간옹 (헌화)', '미축 (자중)'];
      const picked = foundNames[Math.floor(Math.random() * foundNames.length)];
      logMessage(`🔍 [장수 수색] ${myProv.name} 일대에서 재야의 현사 '${picked}'을(를) 탐문 발견했습니다!`, 'text-yellow-300 font-bold');
      alert(`🔍 [인재 탐문!]\\n\\n${myProv.name}의 산야에서 은거 중이던 현사 [${picked}]을(를) 찾아내었습니다!\\n군주의 덕망에 이끌려 조만간 출사를 약속했습니다.`);
    }

    function executeHireOfficer() {
      closeAllPopups();
      alert("📜 [장수 등용] 영지 내 미관료 인재 또는 포로로 잡힌 적장을 등용합니다. (전쟁 승리 시 포로 등용 모달 지원)");
    }

    function executeRelief() {
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
    }

    function executeDelegate() { closeAllPopups(); alert("📜 [위임] 태수에게 영지 내정 및 방어를 전권 위임합니다."); }
    function executeAppoint() { closeAllPopups(); alert("📜 [임명] 영지의 태수 및 군사를 재배치 임명합니다."); }
    function executeDirectOrder() { closeAllPopups(); alert("📜 [명령] 각 장수에게 개별 특별 임무를 하달합니다."); }
    function executeFireOfficer() { closeAllPopups(); alert("⚠️ [해고] 장수를 관직에서 면직시킵니다."); }
    function executeConfiscate() { closeAllPopups(); alert("⚠️ [몰수] 장수가 소지한 보물이나 관직을 회수합니다."); }
"""

if "function executeReward()" not in html:
    insert_before = "function executeLandDev() {"
    html = html.replace(insert_before, personnel_code.strip() + "\n\n    " + insert_before)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added personnel functions!")

# sam3_update.html & repo sync
for p in [r"C:\Users\LENOVO\Desktop\sam3_update.html",
          r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
          r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
print("Sync complete!")
