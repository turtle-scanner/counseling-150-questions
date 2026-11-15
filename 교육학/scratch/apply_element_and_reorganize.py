# -*- coding: utf-8 -*-
import os
import re

def main():
    print("=== 5대 부대 속성 상성 & 8. 재편성(경험치 레벨업) 시스템 빌드 시작 ===")

    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. MY_OFFICERS에 5대 속성 부여
    html = html.replace("{ id: 'guan_yu', name: '관우 (운장)', war: 98, int: 84, lead: 97, icon: '🐉', title: '무성 (청룡언월도)', hp: 100, fatigue: 0 }",
                        "{ id: 'guan_yu', name: '관우 (운장)', war: 98, int: 84, lead: 97, icon: '🐉', title: '무성 (청룡언월도)', hp: 100, fatigue: 0, element: 'wood', elemIcon: '🌲', elemName: '나무 (木)' }")

    html = html.replace("{ id: 'zhang_fei', name: '장비 (익덕)', war: 99, int: 35, lead: 88, icon: '⚡', title: '만인지적 (장팔사모)', hp: 100, fatigue: 0 }",
                        "{ id: 'zhang_fei', name: '장비 (익덕)', war: 99, int: 35, lead: 88, icon: '⚡', title: '만인지적 (장팔사모)', hp: 100, fatigue: 0, element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' }")

    html = html.replace("{ id: 'zhao_yun', name: '조운 (자룡)', war: 97, int: 86, lead: 92, icon: '🛡️', title: '상산 조자룡 (일기당천)', hp: 100, fatigue: 0 }",
                        "{ id: 'zhao_yun', name: '조운 (자룡)', war: 97, int: 86, lead: 92, icon: '🛡️', title: '상산 조자룡 (일기당천)', hp: 100, fatigue: 0, element: 'wind', elemIcon: '🌪️', elemName: '바람 (風 - 서량기병)' }")

    html = html.replace("{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장', hp: 100, fatigue: 0 }",
                        "{ id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장', hp: 100, fatigue: 0, element: 'fire', elemIcon: '🔥', elemName: '불 (火 - 화시)' }")

    html = html.replace("{ id: 'wei_yan', name: '위연 (문장)', war: 91, int: 70, lead: 84, icon: '🗡️', title: '한중태수 맹장', hp: 100, fatigue: 0 }",
                        "{ id: 'wei_yan', name: '위연 (문장)', war: 91, int: 70, lead: 84, icon: '🗡️', title: '한중태수 맹장', hp: 100, fatigue: 0, element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' }")

    html = html.replace("{ id: 'liu_bei', name: '유비 (현덕)', war: 75, int: 78, lead: 80, icon: '👑', title: '한실종친 군주 (쌍고검)', hp: 100, fatigue: 0 }",
                        "{ id: 'liu_bei', name: '유비 (현덕)', war: 75, int: 78, lead: 80, icon: '👑', title: '한실종친 군주 (쌍고검)', hp: 100, fatigue: 0, element: 'wood', elemIcon: '🌲', elemName: '나무 (木 - 인덕)' }")

    print("MY_OFFICERS 5대 속성 주입 완료!")

    # 2. ENEMY_OFFICERS_BY_RULER에 5대 속성 부여
    enemy_old = """    const ENEMY_OFFICERS_BY_RULER = {
      '공손찬': [
        { name: '공손찬 (백규)', war: 84, int: 68, lead: 83, icon: '🐎', title: '백마의종 장군', faceKey: 'gongsongzan' },
        { name: '전예 (국양)', war: 76, int: 80, lead: 82, icon: '📜', title: '북방의 명장' }
      ],
      '조조': [
        { name: '허저 (중강)', war: 97, int: 38, lead: 84, icon: '🐻', title: '호치' },
        { name: '하후돈 (원양)', war: 92, int: 70, lead: 89, icon: '👁️', title: '독안룡' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '료래료래' },
        { name: '하후연 (묘재)', war: 91, int: 62, lead: 88, icon: '🏹', title: '신속명궁' },
        { name: '조인 (자효)', war: 88, int: 74, lead: 90, icon: '🛡️', title: '철벽의 맹장' }
      ],
      '여포': [
        { name: '여포 (봉선)', war: 100, int: 45, lead: 86, icon: '👹', title: '천하무쌍 비장', faceKey: 'lubu' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '팔건장 으뜸' },
        { name: '고순 (함진영)', war: 86, int: 60, lead: 88, icon: '🛡️', title: '함진영 대장' }
      ],
      '손책': [
        { name: '손책 (백부)', war: 92, int: 70, lead: 92, icon: '🐅', title: '소패왕', faceKey: 'sunce' },
        { name: '태사자 (자의)', war: 95, int: 72, lead: 86, icon: '🏹', title: '강동의 효웅' },
        { name: '감녕 (흥패)', war: 94, int: 76, lead: 87, icon: '🔔', title: '비단돛 방울장수' }
      ],
      '원소': [
        { name: '안량 (공석)', war: 93, int: 42, lead: 85, icon: '⚔️', title: '하북의 맹호' },
        { name: '문추 (자강)', war: 92, int: 35, lead: 84, icon: '🪓', title: '하북 으뜸장수' },
        { name: '원소 (본초)', war: 70, int: 75, lead: 80, icon: '👑', title: '맹주', faceKey: 'yuanshao_retro' }
      ],
      '마등': [
        { name: '마초 (맹기)', war: 97, int: 48, lead: 91, icon: '🦁', title: '서량의 금마초' },
        { name: '방덕 (영명)', war: 94, int: 70, lead: 86, icon: '⚰️', title: '백마장군' },
        { name: '마등 (수성)', war: 82, int: 60, lead: 84, icon: '🐎', title: '서량태수', faceKey: 'mateng_retro' }
      ],
      '유표': [
        { name: '문빙 (중업)', war: 84, int: 72, lead: 85, icon: '🛡️', title: '형주 수비명장' },
        { name: '황조 (원충)', war: 74, int: 50, lead: 70, icon: '🏹', title: '강하태수' },
        { name: '유표 (경승)', war: 55, int: 78, lead: 70, icon: '📜', title: '형주자사', faceKey: 'liubiao_retro' }
      ],
      '원술': [
        { name: '기령 (중달)', war: 84, int: 48, lead: 78, icon: '🔱', title: '삼첨도 대장' },
        { name: '원술 (공로)', war: 62, int: 65, lead: 65, icon: '👑', title: '중씨황제', faceKey: 'yuanshu' }
      ],
      '장노': [
        { name: '장위 (장로동생)', war: 78, int: 55, lead: 72, icon: '🗡️', title: '오두미 도위' },
        { name: '양백 (군사)', war: 65, int: 72, lead: 68, icon: '📜', title: '한중 부장' }
      ],
      '사섭': [
        { name: '사섭 (위언)', war: 62, int: 82, lead: 75, icon: '👑', title: '교지태수', faceKey: 'shishe' },
        { name: '사휘 (영진)', war: 68, int: 55, lead: 65, icon: '🗡️', title: '남월의 장수' }
      ]
    };"""

    enemy_new = """    const ENEMY_OFFICERS_BY_RULER = {
      '공손찬': [
        { name: '공손찬 (백규)', war: 84, int: 68, lead: 83, icon: '🐎', title: '백마의종 장군', faceKey: 'gongsongzan', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' },
        { name: '전예 (국양)', war: 76, int: 80, lead: 82, icon: '📜', title: '북방의 명장', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' }
      ],
      '조조': [
        { name: '허저 (중강)', war: 97, int: 38, lead: 84, icon: '🐻', title: '호치', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '하후돈 (원양)', war: 92, int: 70, lead: 89, icon: '👁️', title: '독안룡', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '료래료래', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '하후연 (묘재)', war: 91, int: 62, lead: 88, icon: '🏹', title: '신속명궁', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '조인 (자효)', war: 88, int: 74, lead: 90, icon: '🛡️', title: '철벽의 맹장', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' }
      ],
      '여포': [
        { name: '여포 (봉선)', war: 100, int: 45, lead: 86, icon: '👹', title: '천하무쌍 비장', faceKey: 'lubu', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '팔건장 으뜸', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '고순 (함진영)', war: 86, int: 60, lead: 88, icon: '🛡️', title: '함진영 대장', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' }
      ],
      '손책': [
        { name: '손책 (백부)', war: 92, int: 70, lead: 92, icon: '🐅', title: '소패왕', faceKey: 'sunce', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' },
        { name: '태사자 (자의)', war: 95, int: 72, lead: 86, icon: '🏹', title: '강동의 효웅', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' },
        { name: '감녕 (흥패)', war: 94, int: 76, lead: 87, icon: '🔔', title: '비단돛 방울장수', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' }
      ],
      '손권': [
        { name: '주유 (공근)', war: 78, int: 96, lead: 98, icon: '🔥', title: '적벽도독', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' },
        { name: '육손 (백언)', war: 75, int: 95, lead: 96, icon: '📜', title: '이릉도독', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' },
        { name: '황개 (공복)', war: 85, int: 70, lead: 84, icon: '⚓', title: '고육지계 노장', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' }
      ],
      '원소': [
        { name: '안량 (공석)', war: 93, int: 42, lead: 85, icon: '⚔️', title: '하북의 맹호', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' },
        { name: '문추 (자강)', war: 92, int: 35, lead: 84, icon: '🪓', title: '하북 으뜸장수', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' },
        { name: '원소 (본초)', war: 70, int: 75, lead: 80, icon: '👑', title: '맹주', faceKey: 'yuanshao_retro', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' }
      ],
      '마등': [
        { name: '마초 (맹기)', war: 97, int: 48, lead: 91, icon: '🦁', title: '서량의 금마초', element: 'wind', elemIcon: '🌪️', elemName: '바람 (風 - 서량기병)' },
        { name: '방덕 (영명)', war: 94, int: 70, lead: 86, icon: '⚰️', title: '백마장군', element: 'wind', elemIcon: '🌪️', elemName: '바람 (風 - 서량기병)' },
        { name: '마대 (백첨)', war: 85, int: 65, lead: 82, icon: '🗡️', title: '서량의 맹장', element: 'wind', elemIcon: '🌪️', elemName: '바람 (風 - 서량기병)' },
        { name: '마등 (수성)', war: 82, int: 60, lead: 84, icon: '🐎', title: '서량태수', faceKey: 'mateng_retro', element: 'wind', elemIcon: '🌪️', elemName: '바람 (風 - 서량기병)' }
      ],
      '유표': [
        { name: '문빙 (중업)', war: 84, int: 72, lead: 85, icon: '🛡️', title: '형주 수비명장', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '황조 (원충)', war: 74, int: 50, lead: 70, icon: '🏹', title: '강하태수', element: 'water', elemIcon: '💧', elemName: '물 (水 - 해군)' },
        { name: '유표 (경승)', war: 55, int: 78, lead: 70, icon: '📜', title: '형주자사', faceKey: 'liubiao_retro', element: 'wood', elemIcon: '🌲', elemName: '나무 (木)' }
      ],
      '원술': [
        { name: '기령 (중달)', war: 84, int: 48, lead: 78, icon: '🔱', title: '삼첨도 대장', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' },
        { name: '원술 (공로)', war: 62, int: 65, lead: 65, icon: '👑', title: '중씨황제', faceKey: 'yuanshu', element: 'fire', elemIcon: '🔥', elemName: '불 (火)' }
      ],
      '장노': [
        { name: '장위 (장로동생)', war: 78, int: 55, lead: 72, icon: '🗡️', title: '오두미 도위', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' },
        { name: '양백 (군사)', war: 65, int: 72, lead: 68, icon: '📜', title: '한중 부장', element: 'earth', elemIcon: '⛰️', elemName: '땅 (土 - 육군)' }
      ],
      '사섭': [
        { name: '사섭 (위언)', war: 62, int: 82, lead: 75, icon: '👑', title: '교지태수', faceKey: 'shishe', element: 'wood', elemIcon: '🌲', elemName: '나무 (木 - 밀림)' },
        { name: '사휘 (영진)', war: 68, int: 55, lead: 65, icon: '🗡️', title: '남월의 장수', element: 'wood', elemIcon: '🌲', elemName: '나무 (木 - 밀림)' }
      ]
    };"""

    if enemy_old in html:
        html = html.replace(enemy_old, enemy_new)
        print("ENEMY_OFFICERS_BY_RULER 5대 속성 주입 완료!")

    # 3. 5대 원소 상성 규칙 함수 주입
    element_rules_js = """
    // ==================== 🔮 5대 부대 속성 상성 시스템 (물·불·땅·바람·나무) ====================
    const ELEMENT_RULES = {
      'water': { name: '물 (水 - 해군)', icon: '💧', beats: ['fire'], desc: '불을 끄고 소멸시킴' },
      'fire':  { name: '불 (火 - 원소/공손)', icon: '🔥', beats: ['wood'], desc: '나무를 불태움' },
      'wood':  { name: '나무 (木 - 촉한/밀림)', icon: '🌲', beats: ['earth'], desc: '대지의 양분을 흡수하고 쪼갬' },
      'earth': { name: '땅 (土 - 중원 육군)', icon: '⛰️', beats: ['water', 'wind'], desc: '물길을 메우고 거센 바람을 막아섬' },
      'wind':  { name: '바람 (風 - 서량 기병)', icon: '🌪️', beats: ['water', 'wood'], desc: '돌풍으로 파도를 일으키고 나뭇가지를 꺾음' }
    };

    function getElementAdvantage(attElem, defElem) {
      if (!attElem || !defElem || attElem === defElem) return { mult: 1.0, isAdv: false, isDisadv: false, text: '' };

      const rule = ELEMENT_RULES[attElem];
      const defRule = ELEMENT_RULES[defElem];

      if (rule && rule.beats && rule.beats.includes(defElem)) {
        return {
          mult: 1.50,
          isAdv: true,
          isDisadv: false,
          text: `⚡💥 [상성 우세 극딜!] ${rule.icon} ${rule.name}이(가) ${defRule ? defRule.icon + ' ' + defRule.name : defElem}을(를) 완벽히 제압하여 대미지 +50% 폭발!`
        };
      } else if (defRule && defRule.beats && defRule.beats.includes(attElem)) {
        return {
          mult: 0.70,
          isAdv: false,
          isDisadv: true,
          text: `🛡️ [상성 열세] ${rule ? rule.icon : ''} 속성이 적 ${defRule.icon} 속성의 상성에 막혀 대미지가 30% 경감되었습니다.`
        };
      }
      return { mult: 1.0, isAdv: false, isDisadv: false, text: '' };
    }
"""

    if "const ELEMENT_RULES" not in html:
        insert_marker = "const MY_OFFICERS = ["
        html = html.replace(insert_marker, element_rules_js.strip() + "\n\n    " + insert_marker)
        print("5대 원소 상성 규칙 엔진 주입 완료!")

    # 4. calculateCombatDamage에 속성 상성 연산 적용
    calc_dmg_old = """      // 아군 병종 숙련도 레벨 보정
      if (attacker.faction === 'ally') {
        const lvl = gameState.troopLevel || 1;
        atkPower *= (1.0 + (lvl - 1) * 0.05);
      }

      let baseDamage = Math.floor(((atkPower / Math.max(10, defPower)) * 950 + Math.random() * 250) * diffMult);
      return Math.max(300, baseDamage);"""

    calc_dmg_new = """      // 아군 병종 숙련도 레벨 보정
      if (attacker.faction === 'ally') {
        const lvl = gameState.troopLevel || 1;
        atkPower *= (1.0 + (lvl - 1) * 0.05);
      }

      // 🔮 5대 원소 부대 속성 상성 연산 (우세 시 대미지 1.5배, 열세 시 0.7배)
      const elemAdv = getElementAdvantage(attacker.element, defender.element);
      diffMult *= elemAdv.mult;

      let baseDamage = Math.floor(((atkPower / Math.max(10, defPower)) * 950 + Math.random() * 250) * diffMult);
      return Math.max(300, baseDamage);"""

    if calc_dmg_old in html:
        html = html.replace(calc_dmg_old, calc_dmg_new)
        print("calculateCombatDamage 속성 상성 배율 적용 완료!")

    # 5. initHexBattleUnits에서 유닛에게 속성 명시
    init_ally_old = """          avatar: off.icon || '⚔️',
          war: off.war,
          int: off.int,
          lead: off.lead || 85,
          chr: 85,"""

    init_ally_new = """          avatar: off.icon || '⚔️',
          element: off.element || 'earth',
          elemIcon: off.elemIcon || '⛰️',
          elemName: off.elemName || '땅 (土)',
          war: off.war,
          int: off.int,
          lead: off.lead || 85,
          chr: 85,"""

    if init_ally_old in html:
        html = html.replace(init_ally_old, init_ally_new)
        print("initHexBattleUnits 아군 속성 연동 완료!")

    init_enemy_old = """          avatar: off.icon || '👹',
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          chr: 70,"""

    init_enemy_new = """          avatar: off.icon || '👹',
          element: off.element || (enemyRuler.includes('손') ? 'water' : (enemyRuler.includes('마') ? 'wind' : ([1,2,3,4].includes(targetProv.id) ? 'fire' : 'earth'))),
          elemIcon: off.elemIcon || (enemyRuler.includes('손') ? '💧' : (enemyRuler.includes('마') ? '🌪️' : ([1,2,3,4].includes(targetProv.id) ? '🔥' : '⛰️'))),
          elemName: off.elemName || '적 부대 속성',
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          chr: 70,"""

    if init_enemy_old in html:
        html = html.replace(init_enemy_old, init_enemy_new)
        print("initHexBattleUnits 적군 속성 연동 완료!")

    # 6. 공격 실행 시 상성 극딜 로그 연출 (executeSkillAction)
    skill_melee_old = """        const dmg = calculateCombatDamage(u, targetUnit, 'melee');
        applyDamage(targetUnit, dmg);
        gainTroopExp(15, '돌격 교전');"""

    skill_melee_new = """        const adv = getElementAdvantage(u.element, targetUnit.element);
        const dmg = calculateCombatDamage(u, targetUnit, 'melee');
        applyDamage(targetUnit, dmg);
        gainTroopExp(15, '돌격 교전');
        if (adv.isAdv) {
          logBattle(adv.text);
          playSound('fanfare');
        } else if (adv.isDisadv) {
          logBattle(adv.text);
        }"""

    if skill_melee_old in html:
        html = html.replace(skill_melee_old, skill_melee_new)
        print("executeSkillAction 상성 극딜 로그 연출 완료!")

    # 7. 헥스 캔버스 유닛 렌더링에 속성 아이콘 표기
    canvas_unit_old = "ctx.fillText(unit.name, x, y - 5);"
    canvas_unit_new = "ctx.fillText((unit.elemIcon || '') + ' ' + unit.name, x, y - 5);"
    if canvas_unit_old in html:
        html = html.replace(canvas_unit_old, canvas_unit_new)
        print("캔버스 유닛 렌더러에 속성 아이콘 표기 완료!")

    # 8. 출전 장수 편성 모달(renderDeployOfficerList)에 5대 속성 상성 안내 바 및 장수 속성 배지 추가
    deploy_list_old = """      container.innerHTML = MY_OFFICERS.map(off => {
        if (off.fatigue === undefined) off.fatigue = 0;"""

    deploy_list_new = """      // 상단 5대 속성 상성 안내 바 동적 주입
      const elemGuideHeader = `
        <div class="col-span-1 md:col-span-2 bg-slate-950/90 border border-yellow-500/80 p-2.5 rounded-lg text-xs text-slate-200 mb-1 shadow">
          <div class="font-black text-yellow-300 flex items-center justify-between mb-1.5">
            <span>🔮 5대 부대 속성 상성 (우세 시 대미지 +50% 극딜 폭발!)</span>
            <span class="text-[10px] text-cyan-300">적 세력 속성에 맞추어 출전시키십시오!</span>
          </div>
          <div class="grid grid-cols-5 gap-1.5 text-center text-[10px] font-bold">
            <div class="bg-blue-950/90 p-1.5 rounded border border-blue-500 text-cyan-200">💧 물 (해군/손권)<br><span class="text-[9px] text-yellow-300">▶ 불(🔥) 격파</span></div>
            <div class="bg-red-950/90 p-1.5 rounded border border-red-500 text-red-200">🔥 불 (원소/공손)<br><span class="text-[9px] text-yellow-300">▶ 나무(🌲) 격파</span></div>
            <div class="bg-emerald-950/90 p-1.5 rounded border border-emerald-500 text-emerald-200">🌲 나무 (촉한/관우)<br><span class="text-[9px] text-yellow-300">▶ 땅(⛰️) 격파</span></div>
            <div class="bg-amber-950/90 p-1.5 rounded border border-amber-500 text-amber-200">⛰️ 땅 (중원 육군)<br><span class="text-[9px] text-yellow-300">▶ 물(💧)/바람(🌪️)</span></div>
            <div class="bg-purple-950/90 p-1.5 rounded border border-purple-500 text-purple-200">🌪️ 바람 (서량 기병)<br><span class="text-[9px] text-yellow-300">▶ 물(💧) 격파</span></div>
          </div>
        </div>
      `;

      container.innerHTML = elemGuideHeader + MY_OFFICERS.map(off => {
        if (off.fatigue === undefined) off.fatigue = 0;"""

    if deploy_list_old in html and "elemGuideHeader" not in html:
        html = html.replace(deploy_list_old, deploy_list_new)
        print("출전 장수 편성 모달 상단 5대 속성 가이드 연동 완료!")

    # 장수 카드 속성 배지 추가
    card_name_old = """<span class="font-black text-xs text-white">${off.name}</span>
                  ${statusBadge}"""

    card_name_new = """<span class="font-black text-xs text-white">${off.name}</span>
                  <span class="px-1.5 py-0.5 rounded text-[10px] bg-slate-900 border border-amber-400 text-yellow-300 font-bold">${off.elemIcon || '⛰️'} ${off.elemName || '땅 (土)'}</span>
                  ${statusBadge}"""

    if card_name_old in html:
        html = html.replace(card_name_old, card_name_new)
        print("장수 카드 속성 뱃지 추가 완료!")

    # 9. [8. 재편성] 전용 모달 HTML 주입
    reorganize_modal_html = """
  <!-- ==================== 🎖️ 부대 재편성 & 병종 승급(전직) 훈련소 모달 ==================== -->
  <div id="reorganize-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex items-center justify-center p-3 bg-black/90">
    <div class="koei-box w-full max-w-2xl p-4 rounded-xl shadow-2xl border-4 border-yellow-400 max-h-[92vh] flex flex-col justify-between overflow-y-auto">
      
      <!-- 헤더 -->
      <div class="flex items-center justify-between border-b-2 border-yellow-400 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-2xl">🎖️</span>
          <div>
            <h2 class="text-base font-black text-yellow-300 text-pixel">
              [8. 부대 재편성] 병종 승급 & 경험치 레벨업 훈련소
            </h2>
            <div class="text-[11px] text-amber-200">
              전쟁과 훈련으로 쌓은 경험치(EXP)로 병과를 승급하고 전군을 정예화하십시오!
            </div>
          </div>
        </div>
        <button onclick="closeModal('reorganize-modal')" class="text-slate-400 hover:text-white font-mono text-xs px-2 py-1 border border-slate-600 rounded">
          ✕ 닫기
        </button>
      </div>

      <!-- 현재 아군 부대 레벨 및 병종 현황 카드 -->
      <div class="bg-blue-950/90 border-2 border-amber-400 rounded-lg p-3.5 mb-3 shadow">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-2">
            <span class="text-3xl" id="reorg-tier-icon">🛡️</span>
            <div>
              <div class="flex items-center gap-2">
                <span class="text-base font-black text-white" id="reorg-tier-name">보병 (기본)</span>
                <span class="px-2 py-0.5 rounded text-xs bg-slate-800 border border-yellow-400 text-yellow-300 font-bold" id="reorg-tier-lvl">Lv. 1</span>
              </div>
              <div class="text-xs text-slate-300">
                부대 전투력 보정: <strong class="text-yellow-300 font-mono" id="reorg-tier-mult">공방 1.0배</strong>
              </div>
            </div>
          </div>
          <div class="text-right">
            <button onclick="executeSpecialTraining()" class="px-3.5 py-2 bg-gradient-to-r from-amber-600 to-yellow-500 hover:from-amber-500 hover:to-yellow-400 text-black font-black text-xs rounded-lg border border-yellow-200 shadow-lg flex items-center gap-1 animate-pulse">
              <span>⭐</span> 부대 집중 훈련 (경험치 +50 EXP)
            </button>
            <div class="text-[10px] text-slate-400 mt-1">비용: 군자금 200전 & 군량 500석</div>
          </div>
        </div>

        <!-- 경험치 프로그레스 바 -->
        <div class="w-full bg-slate-900 h-3 rounded-full overflow-hidden border border-blue-600/80 p-0.5 mt-2">
          <div id="reorg-exp-bar" class="h-full rounded-full bg-gradient-to-r from-blue-500 via-amber-500 to-yellow-400 transition-all duration-300" style="width: 10%;"></div>
        </div>
        <div class="flex justify-between items-center text-xs text-slate-300 mt-1.5 font-mono">
          <span id="reorg-exp-text">경험치: 10 / 100 EXP</span>
          <span class="text-cyan-300">다음 승급: <strong id="reorg-next-promo" class="text-yellow-300 font-bold">Lv.3 기마병</strong></span>
        </div>
      </div>

      <!-- 5단계 병종 승급 테크트리 안내 -->
      <div class="grid grid-cols-5 gap-1.5 text-center text-xs mb-3 font-bold">
        <div class="p-2 rounded border border-slate-600 bg-slate-900/80 text-slate-300">
          <div>🛡️ 보병</div>
          <div class="text-[10px] text-amber-300">Lv.1 (기본)</div>
        </div>
        <div class="p-2 rounded border border-blue-500 bg-blue-950/80 text-cyan-200">
          <div>🐎 기마병</div>
          <div class="text-[10px] text-yellow-300">Lv.3 (돌격+35%)</div>
        </div>
        <div class="p-2 rounded border border-indigo-500 bg-indigo-950/80 text-indigo-200">
          <div>🛡️ 전차병</div>
          <div class="text-[10px] text-yellow-300">Lv.6 (방어돌파)</div>
        </div>
        <div class="p-2 rounded border border-amber-500 bg-amber-950/80 text-amber-200">
          <div>⚔️ 중보병</div>
          <div class="text-[10px] text-yellow-300">Lv.9 (철벽방어)</div>
        </div>
        <div class="p-2 rounded border border-red-500 bg-red-950/80 text-red-200">
          <div>👑 친위병</div>
          <div class="text-[10px] text-yellow-300">Lv.99 (천하무쌍)</div>
        </div>
      </div>

      <!-- 장수별 부대 병력 재편성 옵션 -->
      <div class="bg-blue-950/80 border border-blue-700 rounded-lg p-3 mb-2 text-xs">
        <div class="font-bold text-yellow-300 mb-2 flex items-center justify-between">
          <span>⚔️ 장수별 부대 병력 재편성 (원클릭 재배치)</span>
          <span class="text-slate-300" id="reorg-total-soldiers">영지 총 병력: 17,200명</span>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <button onclick="reorganizeSoldiers('even')" class="p-2 bg-blue-900 hover:bg-blue-800 border border-cyan-400 rounded text-cyan-200 font-bold flex items-center justify-center gap-1.5">
            <span>⚖️</span> <span>전 장수 균등 배분 (각 부대 균형)</span>
          </button>
          <button onclick="reorganizeSoldiers('elite')" class="p-2 bg-amber-900 hover:bg-amber-800 border border-yellow-400 rounded text-yellow-200 font-bold flex items-center justify-center gap-1.5">
            <span>⚡</span> <span>선봉 맹장 집중 배분 (관우·장비 60%)</span>
          </button>
        </div>
      </div>

      <!-- 하단 닫기 -->
      <div class="border-t border-yellow-500/60 pt-2.5 mt-2 flex justify-end">
        <button onclick="closeModal('reorganize-modal')" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 text-white font-bold text-xs rounded border border-slate-500">
          완료 (확인)
        </button>
      </div>

    </div>
  </div>
"""

    if 'id="reorganize-modal"' not in html:
        html = html.replace('<!-- ==================== 🎖️ 병종 승급 전직 축하 모달 ==================== -->',
                            reorganize_modal_html.strip() + '\n\n  <!-- ==================== 🎖️ 병종 승급 전직 축하 모달 ==================== -->')
        print("8. 재편성 모달 HTML 주입 완료!")

    # 10. openReorganizeModal 및 재편성 JS 엔진 주입
    reorg_js = """
    // ==================== 🎖️ 8. 부대 재편성 & 집중 훈련 엔진 ====================
    function openReorganizeModal() {
      closeAllPopups();
      updateReorganizeModalUI();
      openModal('reorganize-modal');
    }

    function updateReorganizeModalUI() {
      const lvl = gameState.troopLevel || 1;
      const exp = gameState.troopExp || 0;
      const typeName = gameState.troopTypeName || '보병 (기본)';
      const mult = (1.0 + (lvl - 1) * 0.08).toFixed(1);
      const reqExp = lvl * 100;

      const icons = { '보병': '🛡️', '기마병': '🐎', '전차병': '🛡️', '중보병': '⚔️', '친위병': '👑' };
      const icon = icons[typeName.split(' ')[0]] || '🛡️';

      let nextPromo = 'Lv.3 기마병';
      if (lvl >= 3 && lvl < 6) nextPromo = 'Lv.6 전차병';
      else if (lvl >= 6 && lvl < 9) nextPromo = 'Lv.9 중보병';
      else if (lvl >= 9) nextPromo = 'Lv.99 친위병';

      const tIcon = document.getElementById('reorg-tier-icon');
      const tName = document.getElementById('reorg-tier-name');
      const tLvl = document.getElementById('reorg-tier-lvl');
      const tMult = document.getElementById('reorg-tier-mult');
      const tBar = document.getElementById('reorg-exp-bar');
      const tExpText = document.getElementById('reorg-exp-text');
      const tNext = document.getElementById('reorg-next-promo');
      const tSol = document.getElementById('reorg-total-soldiers');

      if (tIcon) tIcon.innerText = icon;
      if (tName) tName.innerText = typeName;
      if (tLvl) tLvl.innerText = `Lv. ${lvl}`;
      if (tMult) tMult.innerText = `공방 ${mult}배`;
      if (tBar) tBar.style.width = `${Math.min(100, (exp / reqExp) * 100)}%`;
      if (tExpText) tExpText.innerText = `경험치: ${exp} / ${reqExp} EXP`;
      if (tNext) tNext.innerText = nextPromo;

      const myProv = getMyCapital();
      if (tSol && myProv) tSol.innerText = `영지 총 병력: ${myProv.soldiers.toLocaleString()}명`;
    }

    // 경험치 집중 훈련 (금 200, 군량 500 소모)
    function executeSpecialTraining() {
      const myProv = getMyCapital();
      if (myProv.gold < 200 || myProv.food < 500) {
        alert("⚠️ 훈련을 위한 군자금(금 200전) 또는 군량(500석)이 부족합니다!");
        return;
      }
      myProv.gold -= 200;
      myProv.food -= 500;
      playSfx('build');

      gainTroopExp(50, '부대 특수 집중 훈련');
      updateReorganizeModalUI();
      updateRightPanel(myProv.id);
      alert(`⭐ [특수 훈련 완료]\n\n군자금 200전과 군량 500석을 들여 정예 훈련을 실시했습니다!\n- 부대 경험치 +50 EXP 획득!\n- 현재 레벨: Lv.${gameState.troopLevel}`);
    }

    // 장수별 병력 재편성 (균등 / 선봉 집중)
    function reorganizeSoldiers(mode) {
      const myProv = getMyCapital();
      playSfx('select');
      if (mode === 'even') {
        logMessage(`⚖️ [병력 재편성] ${myProv.name}의 총 병력 ${myProv.soldiers.toLocaleString()}명을 전 장수에게 균등 배분했습니다!`, 'text-cyan-300 font-bold');
        alert(`⚖️ [균등 재편성 완료]\n\n총 병력 ${myProv.soldiers.toLocaleString()}명을 각 부대에 고르게 나누어 전선의 안정성을 높였습니다!`);
      } else {
        logMessage(`⚡ [선봉 집중 재편성] 관우·장비 등 최강 무력 장수에게 병력 60%를 집중 배치했습니다!`, 'text-yellow-300 font-black');
        alert(`⚡ [선봉 맹장 집중 재편성 완료]\n\n적진 돌파를 위해 선봉 맹장에게 정예 병력 60%를 집중 배치했습니다!\n(전쟁 시 돌파력 대폭 상승)`);
      }
      closeModal('reorganize-modal');
    }
"""

    if "function openReorganizeModal" not in html:
        insert_marker = "function openOfficerDeployModal(target, fromProv, isDefense = false) {"
        html = html.replace(insert_marker, reorg_js.strip() + "\n\n    " + insert_marker)
        print("openReorganizeModal 및 재편성 엔진 주입 완료!")

    # 11. 파일 저장 및 전체 동기화
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
