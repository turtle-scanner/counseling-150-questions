# -*- coding: utf-8 -*-
import re

html_path = r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded HTML: {len(text):,} bytes")

# ==============================================================================
# 1. 일기토 무력 삼총사: 여포 119, 관우 118, 장비 117
# ==============================================================================
print("1. Setting Duel War: Lu Bu 119, Guan Yu 118, Zhang Fei 117...")

duel_war_function = """    function getOfficerDuelWar(officer) {
      if (!officer) return 80;
      const n = (officer.name || '') + ' ' + (officer.fullName || '');
      if (n.includes('여포')) return 119; // 👹 천하무쌍 여포 무력 119!
      if (n.includes('관우')) return 118; // 🐉 군신 관우 무력 118!
      if (n.includes('장비')) return 117; // ⚡ 만인지적 장비 무력 117!
      return officer.war || 80;
    }"""

text = re.sub(
    r"function getOfficerDuelWar\(officer\)\s*\{[\s\S]*?\}",
    duel_war_function,
    text
)

# 헥스 일기토(onCmdDuel) 내 3대 맹장 대승 판정
hex_duel_trio = """      // 3대 맹장(여포 119, 관우 118, 장비 117) 일기토 대승 판정
      let isVictory = false;
      if (u.name.includes('여포')) {
        isVictory = true;
        logBattle(`👹⚡ [천하무쌍 여포 무력 119!] 여포의 방천화극이 일격에 적장 ${target.name}을 베어 넘겼습니다!`);
      } else if (u.name.includes('관우')) {
        isVictory = !target.name.includes('여포');
        logBattle(`🐉✨ [군신 관우 무력 118!] 청룡언월도의 섬광이 적장 ${target.name}의 투구를 쪼갰습니다!`);
      } else if (u.name.includes('장비')) {
        isVictory = !(target.name.includes('여포') || target.name.includes('관우'));
        logBattle(`⚡💥 [만인지적 장비 무력 117!] 장팔사모의 뇌천격이 적장 ${target.name}을 말 아래로 떨어뜨렸습니다!`);
      } else if (target.name.includes('여포')) {
        isVictory = false;
        logBattle(`👹⚡ [적장 여포 무력 119!] 천하무쌍 여포의 방천화극 앞에 ${u.name}이 중상을 입고 패퇴했습니다!`);
      } else {
        const winChance = 50 + (uWar - tWar) * 2.5;
        isVictory = (Math.random() * 100 < winChance);
      }"""

pattern_duel_judge = r"// 여포 무력 119 필살 대승 판정[\s\S]*?isVictory = \(Math\.random\(\) \* 100 < winChance\);\s*\}"
text = re.sub(pattern_duel_judge, hex_duel_trio, text)

# ==============================================================================
# 2. 5대 전설의 보물 시스템 (적토마, 청룡언월도, 사모, 옥새, 병법서들)
# ==============================================================================
print("2. Implementing 5 Legendary Treasures System...")

treasures_database = """
    // ==========================================================================
    // 🏆 5대 전설의 보물 (적토마, 청룡언월도, 장팔사모, 옥새, 병법서)
    // ==========================================================================
    const LEGENDARY_TREASURES = {
      red_hare: {
        id: 'red_hare',
        name: '적토마 (赤兎馬)',
        icon: '🐎',
        type: 'horse',
        effect: '무력 +5, 이동력 +2칸 (전국 최고 명마)',
        statWar: 5,
        statInt: 0,
        moveBonus: 2,
        desc: '하루 천 리를 달리는 붉은 갈기의 명마. 어떤 험지도 거침없이 돌파합니다.'
      },
      green_dragon: {
        id: 'green_dragon',
        name: '청룡언월도 (靑龍偃月刀)',
        icon: '🐉',
        type: 'weapon',
        effect: '무력 +10, 통솔 +6, 일기토 무력 118',
        statWar: 10,
        statInt: 0,
        statLead: 6,
        desc: '무게 82근의 신도. 푸른 용의 기운이 깃들어 적장을 단칼에 베어냅니다.'
      },
      serpent_spear: {
        id: 'serpent_spear',
        name: '장팔사모 (丈八蛇矛)',
        icon: '⚡',
        type: 'weapon',
        effect: '무력 +9, 분기 대미지 2.5배, 일기토 무력 117',
        statWar: 9,
        statInt: 0,
        desc: '길이 한 길 여덟 자의 구불구불한 뱀 모양 창. 찌르는 순간 적진이 두 동강 납니다.'
      },
      imperial_seal: {
        id: 'imperial_seal',
        name: '전국옥새 (傳國玉璽)',
        icon: '👑',
        type: 'royal',
        effect: '매력 100, 민충 100 영구 유지, 인재 등용 100%',
        statWar: 0,
        statInt: 5,
        statChr: 100,
        desc: '한나라 황실의 정통 옥새. 수서구룡의 조각과 함께 천명을 얻은 자만이 쥡니다.'
      },
      sun_tzu: {
        id: 'sun_tzu',
        name: '손자병법서 (孫子兵法)',
        icon: '📜',
        type: 'book',
        effect: '지력 +10, 통솔 +10, 계략 100% 명중',
        statWar: 0,
        statInt: 10,
        statLead: 10,
        desc: '손무가 저술한 불멸의 병법 대전. 화계와 혼란의 신산귀모를 100% 실현합니다.'
      },
      meng_de: {
        id: 'meng_de',
        name: '맹덕신서 (孟德新書)',
        icon: '📖',
        type: 'book',
        effect: '지력 +8, 통솔 +8, 궁시 사거리 +1칸',
        statWar: 0,
        statInt: 8,
        statLead: 8,
        desc: '조조가 평생의 실전 전술을 집대성한 병서. 원거리 사거리와 전술을 극대화합니다.'
      }
    };

    // 보물 발굴 시 보물 등록 함수
    function grantTreasureToHero(unit, treasureKey) {
      const t = LEGENDARY_TREASURES[treasureKey] || LEGENDARY_TREASURES.red_hare;
      if (!unit.treasures) unit.treasures = [];
      unit.treasures.push(t);

      if (t.statWar) unit.war += t.statWar;
      if (t.statInt) unit.int += t.statInt;
      if (t.statLead) unit.lead = (unit.lead || 80) + t.statLead;
      unit.morale = 100;

      playSound('fanfare');
      logBattle(`🏆✨ [전설의 보물 획득!] ${unit.name} 장군이 [${t.name}]을(를) 장착했습니다! (${t.effect})`);
      logMessage(`🏆✨ [보물 장착!] ${unit.name} 장군이 [${t.name}]을(를) 획득하여 능력이 비약적으로 상승했습니다!`, 'text-yellow-300 font-black text-sm');

      alert(`🏆✨ [전설의 보물 장착 성공!]\n\n${unit.name} 장군이 [${t.name}]을(를) 획득하여 무장 능력이 영구 상승했습니다!\n\n▶ 보물: ${t.name} (${t.icon})\n▶ 효과: ${t.effect}\n▶ 설명: ${t.desc}\n▶ 전군 사기 100 달성!`);
    }
"""

if 'const LEGENDARY_TREASURES =' not in text:
    idx = text.find("function checkTreasureDiscovery(")
    if idx != -1:
        text = text[:idx] + treasures_database + "\n\n    " + text[idx:]
        print("  -> LEGENDARY_TREASURES database injected!")

# checkTreasureDiscovery 함수를 보물 데이터베이스 연동으로 업그레이드
treasure_discovery_patch = """    function checkTreasureDiscovery(unit, q, r) {
      if (unit.faction !== 'ally') return;
      if (MAP_TERRAIN[r] && MAP_TERRAIN[r][q] === 7 && currentBattleTreasure && !currentBattleTreasure.found) {
        currentBattleTreasure.found = true;
        MAP_TERRAIN[r][q] = 0; // 평지화
        
        // 지역별 맞춤 보물 키 매핑
        let tKey = 'red_hare';
        if (currentBattleTreasure.name.includes('장팔사모')) tKey = 'serpent_spear';
        else if (currentBattleTreasure.name.includes('청룡언월도')) tKey = 'green_dragon';
        else if (currentBattleTreasure.name.includes('손자병법')) tKey = 'sun_tzu';
        else if (currentBattleTreasure.name.includes('옥새')) tKey = 'imperial_seal';
        else if (currentBattleTreasure.name.includes('의천검')) tKey = 'meng_de';

        grantTreasureToHero(unit, tKey);
      }
    }"""

pattern_check_treasure = r"function checkTreasureDiscovery\(unit, q, r\)[\s\S]*?alert\([^\)]*?\);\s*\}\s*\}"
text = re.sub(pattern_check_treasure, treasure_discovery_patch, text)
print("  -> checkTreasureDiscovery upgraded with grantTreasureToHero!")

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

print("Trio Duel & 5 Legendary Treasures Complete!")
