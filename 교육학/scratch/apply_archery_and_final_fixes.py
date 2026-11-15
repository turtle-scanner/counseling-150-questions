# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# 1. FORMATIONS.anhaeng 사거리 4칸으로 대폭 확장!
text = re.sub(
    r"anhaeng:\s*\{[\s\S]*?moveBonus:\s*0[\s\S]*?\}",
    """anhaeng: {
        name: "안행 (雁行)",
        desc: "궁시 초장거리 사거리 4칸 (원거리 폭격), 사격 피해 +65%, 원거리 요격 특화.",
        atkMod: 0.85, defMod: 0.80, arcRange: 4, arcMod: 1.65, moveBonus: 0,
        badgeBg: "#1d4ed8", color: "#bfdbfe"
      }""",
    text
)
print("1. FORMATIONS.anhaeng arcRange updated to 4!")

# 2. triggerSupplyRaid & triggerAllySupplyRaid 교체
raid_code = """    // ==========================================================================
    // 🌾 적 군량고 습격 및 아군 군량고 피습 처리
    // ==========================================================================
    function triggerSupplyRaid(hero) {
      if (sam5BattleState.supplyBurned) return;
      sam5BattleState.supplyBurned = true;
      logBattle(`🌾💥 [전략 대성공!] ${hero.name} 부대가 적의 군량고를 기습 점령 및 불태웠습니다! 적 전군 패닉 & 사기 급락!`);
      playSound('fire');

      // 적 전군 사기 급락 및 병력 25% 이탈
      UNITS.filter(u => u.faction === "enemy" && u.troops > 0).forEach(enemy => {
        enemy.morale = Math.max(15, enemy.morale - 45);
        const lost = Math.floor(enemy.troops * 0.25);
        enemy.troops -= lost;
        showDamagePop(enemy.q, enemy.r, `군량소실! -${lost}`);
      });

      const alertEl = document.getElementById("tacticalAlertText");
      if (alertEl) alertEl.innerText = "🎉 적 군량고 소실! 10턴 내에 전멸시킬 수 있는 절호의 기회입니다!";

      logMessage(`🔥 [적 군량고 점령 소각!] ${hero.name} 장군이 적 후방 보급창을 궤멸시켜 적 전군이 패닉에 빠졌습니다!`, 'text-yellow-300 font-extrabold text-sm');
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

      const alertEl = document.getElementById("tacticalAlertText");
      if (alertEl) alertEl.innerText = "🚨 아군 군량고 소실! 매 턴 보급 결핍 탈영 발생! 속전속결로 적을 섬멸하십시오!";

      logMessage(`🚨 [비상! 아군 군량고 소각!] 적 기습부대에게 본진 보급창을 빼앗겼습니다! 매 턴 군량 결핍 탈영 발생!`, 'text-red-400 font-extrabold text-sm');
      alert(`🚨 [비상! 아군 군량고 피습 소각!]\n\n적 기습부대 ${enemyUnit.name}이 아군의 본진 보급창(군량고)을 점령하고 불태웠습니다!\n\n▶ 아군 전군 패닉: 사기 급락 (-40)!\n▶ 매 턴 보급 차단으로 병력 15% 탈영 손실 발생!\n▶ 10턴 내로 적 본대를 섬멸하지 못하면 전군 와해됩니다!`);
    }"""

pattern_old_raid = r"function triggerSupplyRaid\(hero\)\s*\{[\s\S]*?document\.getElementById\(\"tacticalAlertText\"\)\.innerText\s*=\s*\"[^\"]*?\";\s*\}"
match_old_raid = re.search(pattern_old_raid, text)
if match_old_raid:
    text = text[:match_old_raid.start()] + raid_code + text[match_old_raid.end():]
    print("2. triggerSupplyRaid & triggerAllySupplyRaid successfully injected!")
else:
    print("2. WARNING: pattern_old_raid not matched, searching by func name...")
    p = text.find("function triggerSupplyRaid")
    if p != -1:
        end_p = text.find("function computeMovementRange", p)
        text = text[:p] + raid_code + "\n\n    " + text[end_p:]
        print("2. triggerSupplyRaid replaced via computeMovementRange boundary!")

# 3. onCmdArchery 개편: 사거리 4칸 초장거리 일제사격 + 비안행진 시 자동 안행진 전술 전환
archery_code = """    function onCmdArchery() {
      const u = sam5BattleState.selectedUnit;
      if (!u) return;

      // 안행진이 아니면 자동으로 안행진(雁行陣)으로 전술 전환!
      if (u.formation !== 'anhaeng' && !u.name.includes('황충')) {
        u.formation = 'anhaeng';
        logBattle(`🏹 [진형 전환] ${u.name} 부대가 장거리 사격을 위해 [안행진(雁行)]으로 전술을 전환했습니다! (사거리 4칸)`);
        playSound('fanfare');
        updateUnitDetailCard(u);
      }

      const arcRange = 4; // 사거리 4칸 초장거리 지원!
      sam5BattleState.skillMode = 'archery';
      sam5BattleState.attackableTargets = getEnemiesInRange(u, arcRange);

      if (sam5BattleState.attackableTargets.length === 0) {
        logBattle(`🏹 사거리 ${arcRange}칸 이내에 조준할 수 있는 적 부대가 없습니다.`);
      } else {
        logBattle(`🏹 [안행 궁시 장거리 사격] 사거리 ${arcRange}칸 이내의 붉은 타겟 적을 조준하십시오!`);
      }
      renderBattlefield();
    }"""

pattern_archery = r"function onCmdArchery\(\)\s*\{[\s\S]*?renderBattlefield\(\);\s*\}"
match_archery = re.search(pattern_archery, text)
if match_archery:
    text = text[:match_archery.start()] + archery_code + text[match_archery.end():]
    print("3. onCmdArchery updated to 4-range auto-anhaeng switch!")
else:
    print("3. WARNING: pattern_archery not matched!")

# 4. updateActionCommands 내 btnArchery 활성화 완화 (적 4칸 이내에 있으면 언제든 활성화!)
btn_archery_fix = """      // 장거리 4칸 이내 적이 있으면 궁시 버튼 상시 활성화!
      const longRangeEnemies = getEnemiesInRange(u, 4);
      if (btnArc) {
        btnArc.disabled = (longRangeEnemies.length === 0);
        if (isHwang) {
          btnArc.innerHTML = '🏹 황충 신궁 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-emerald-800 hover:bg-emerald-700 border-2 border-yellow-400 text-yellow-300 font-black text-xs shadow-lg transition";
        } else if (u.formation === 'anhaeng') {
          btnArc.innerHTML = '🏹 안행 궁시 (사거리4)';
          btnArc.className = "px-3 py-2 rounded bg-blue-900 hover:bg-blue-800 border-2 border-blue-400 text-cyan-200 font-black text-xs shadow transition";
        } else {
          btnArc.innerHTML = '🏹 안행 궁시 (전환사격)';
          btnArc.className = "px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-500 text-slate-200 font-bold text-xs shadow transition";
        }
      }"""

pattern_update_arc = r"if \(btnArc\) \{[\s\S]*?btnArc\.className = [^\n]*?;\s*\}\s*\}"
match_update_arc = re.search(pattern_update_arc, text)
if match_update_arc:
    text = text[:match_update_arc.start()] + btn_archery_fix + text[match_update_arc.end():]
    print("4. updateActionCommands btnArchery logic enhanced!")

# 5. 파일 저장 및 전역 동기화
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

print("All files updated with long-range anhaeng archery & depot defenses!")
