# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. getHexPixel 뒤 중복 중괄호 '};\n    }' 수리
# ==============================================================================
print("1. Fixing syntax error around getHexPixel...")
text = text.replace(
    "const y = 48 + r * (HEX_H * 0.75);\n      return { x, y };\n    };\n    }",
    "const y = 48 + r * (HEX_H * 0.75);\n      return { x, y };\n    }"
)
text = text.replace(
    "return { x, y };\n    };\n    }",
    "return { x, y };\n    }"
)

# ==============================================================================
# 2. 일기토 시스템: 여포 무력 119 & 절대 무적 패왕 설정!
# ==============================================================================
print("2. Implementing Lu Bu War 119 in Duel System (Undefeated Warlord)...")

# 2-1. ENEMY_OFFICERS_BY_RULER['여포'] 무장 데이터: 기본 무력 100, 일기토 특수 무력 119
text = re.sub(
    r"\{\s*name:\s*'여포 \(봉선\)'[\s\S]*?\}",
    "{ name: '여포 (봉선)', war: 100, duelWar: 119, int: 45, lead: 86, icon: '👹', title: '천하무쌍 비장 (일기토 무력 119)', faceKey: 'lubu', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)', level: 10, exp: 1500, troopType: 'royal', troopName: '친위병 (천하무쌍)' }",
    text
)

# 2-2. 메인 1:1 결투(openDuelSelectModal & executeDuelAttack)에서 여포 무력 119 적용
duel_lubu_boost = """    function getOfficerDuelWar(officer) {
      if (!officer) return 80;
      const n = (officer.name || '') + ' ' + (officer.fullName || '');
      if (n.includes('여포')) return 119; // 🔥 천하무쌍 여포는 일기토 무력 119!
      return officer.war || 80;
    }"""

if 'function getOfficerDuelWar' not in text:
    target_duel = "function openDuelSelectModal("
    idx = text.find(target_duel)
    if idx != -1:
        text = text[:idx] + duel_lubu_boost + "\n\n    " + text[idx:]
        print("  -> getOfficerDuelWar helper injected!")

# 2-3. 메인 1:1 결투 시작 시 여포 무력 119 표시 및 대미지 배율 극대화
duel_setup_patch = """      const myWar = getOfficerDuelWar(myOff);
      const enemyWar = getOfficerDuelWar(enemyOff);

      if ((myOff.name || '').includes('여포') || (enemyOff.name || '').includes('여포')) {
        logMessage(`👹⚡ [천하무쌍 비장 강림!] 여포의 무력이 [119]로 각성하여 모든 장수를 압도합니다!`, 'text-red-400 font-black text-sm');
      }"""

if 'getOfficerDuelWar(myOff)' not in text:
    pattern_duel_start = r"duelState\.myOfficer = myOff;\s*duelState\.enemyOfficer = enemyOff;"
    replacement_duel_start = """duelState.myOfficer = myOff;
      duelState.enemyOfficer = enemyOff;
      myOff.war = getOfficerDuelWar(myOff);
      enemyOff.war = getOfficerDuelWar(enemyOff);
      if ((myOff.name || '').includes('여포') || (enemyOff.name || '').includes('여포')) {
        logMessage(`👹⚡ [천하무쌍 비장 강림!] 여포의 무력이 [119]로 폭발하여 일기토 절대무적을 자랑합니다!`, 'text-red-400 font-black text-sm');
      }"""
    text = re.sub(pattern_duel_start, replacement_duel_start, text)
    print("  -> Duel start patched with Lu Bu War 119!")

# 2-4. 헥스 전장 1:1 결투(onCmdDuel & sam5DuelState)에서도 여포 무력 119 보장
hex_duel_patch = """function onCmdDuel() {
      const u = sam5BattleState.selectedUnit;
      if (!u || u.acted || sam5BattleState.phase !== 'ally') return;

      const adjEnemies = getEnemiesInRange(u, 1);
      if (adjEnemies.length === 0) {
        logBattle("인접한 적 부대가 없어 일기토를 신청할 수 없습니다.");
        return;
      }

      const target = adjEnemies[0];
      const uWar = getOfficerDuelWar(u);
      const tWar = getOfficerDuelWar(target);

      logBattle(`⚔️🏇 [일기토 신청!] ${u.name}(무력:${uWar}) 장군이 적장 ${target.name}(무력:${tWar})에게 1:1 결투를 신청했습니다!`);
      playSound('fanfare');

      // 여포 무력 119 필살 대승 판정
      let isVictory = false;
      if (u.name.includes('여포')) {
        isVictory = true;
        logBattle(`👹⚡ [천하무쌍 여포 무력 119!] 여포의 방천화극이 일격에 적장 ${target.name}을 베어 넘겼습니다!`);
      } else if (target.name.includes('여포')) {
        isVictory = false;
        logBattle(`👹⚡ [적장 여포 무력 119!] 적장 여포의 방천화극 앞에 ${u.name}이 중상을 입고 패퇴했습니다!`);
      } else {
        const winChance = 50 + (uWar - tWar) * 2.5;
        isVictory = (Math.random() * 100 < winChance);
      }

      if (isVictory) {
        playSound('slash');
        logBattle(`🏆✨ [일기토 대승!] ${u.name} 장군이 적장 ${target.name}을 격파하여 적 전군이 패닉에 빠졌습니다!`);
        target.troops = 0;
        showDamagePop(target.q, target.r, "☠️일기토 전사!");
        gainTroopExp(50, '일기토 대승');
        checkVictoryCondition();
      } else {
        playSound('slash');
        logBattle(`🚨 [일기토 패배!] ${u.name} 부대가 큰 타격을 입고 사기가 꺾였습니다.`);
        u.troops = Math.max(100, Math.floor(u.troops * 0.4));
        u.morale = Math.max(10, u.morale - 40);
        showDamagePop(u.q, u.r, "일기토 패배!");
      }

      finishUnitAction(u);
    }"""

pattern_on_cmd_duel = r"function onCmdDuel\(\)\s*\{[\s\S]*?finishUnitAction\(u\);\s*\}"
match_on_cmd_duel = re.search(pattern_on_cmd_duel, text)
if match_on_cmd_duel:
    text = text[:match_on_cmd_duel.start()] + hex_duel_patch + text[match_on_cmd_duel.end():]
    print("  -> onCmdDuel upgraded with Lu Bu War 119!")
else:
    # 없으면 executeSkillAction 바로 뒤에 주입
    idx = text.find("function onCmdWait()")
    if idx != -1:
        text = text[:idx] + hex_duel_patch + "\n\n    " + text[idx:]
        print("  -> onCmdDuel injected before onCmdWait!")

# ==============================================================================
# 파일 저장 및 전역 동기화
# ==============================================================================
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

print("Lu Bu War 119 & Syntax Fix Sync Complete!")
