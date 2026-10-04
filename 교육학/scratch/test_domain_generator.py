import json
import re

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def generate_perfect_4lines(it):
    num = it['num']
    badge = it['badge']
    kw = it['kw']
    q = it['q'].strip()
    ans = it['ans'].strip()
    
    clean_kw = re.sub(r'\(.*?\)', '', kw).strip()
    
    # 1. First line: Concept definition and official term
    line1 = f"1. {ans}" if ans.endswith('이다.') or ans.endswith('한다.') else f"1. {ans}에 해당하는 KICE 공식 개념인 '{kw}'이다."
    
    # 2. Second line: Core mechanism / Diagnostic criteria / Phase 1
    if '정신병리' in badge:
        line2 = f"2. 내담자의 증상 발현 양상과 지속 기간을 면밀히 검토하여 일상 기능 저하와 고통 수준을 객관적으로 진단한다."
    elif '심리검사' in badge:
        line2 = f"2. 척도의 T점수 상승 수준(T 65 이상)을 확인하고 내담자의 수검 태도 및 타당도 척도와 연계하여 프로파일을 해석한다."
    elif '가족치료' in badge:
        line2 = f"2. 가족 체계 내의 역동적 상호작용과 하위체계 간의 경계선 및 세대 간 전수 패턴을 종합적으로 조망한다."
    elif '진로상담' in badge:
        line2 = f"3. 내담자의 진로 발달 수준과 환경적 요구를 파악하여 흥미, 적성, 가치관의 유기적 일치를 분석한다."
    elif '교육' in badge or '교수' in badge:
        line2 = f"2. 학습자의 사전 지식과 교육과정 성취 기준을 정밀 분석하여 체계적인 단계별 실행 계획을 수립한다."
    else:
        line2 = f"2. 기저에 존재하는 인지적·정서적 왜곡과 환경적 유발 요인을 탐색하여 심리적 역동을 구체화한다."
        
    # 3. Third line: Intervention technique / Specific component
    if '정신병리' in badge:
        line3 = f"3. 유사한 타 장애와의 명확한 감별 진단을 실시하고, 인지행동치료 및 환경적 안전망을 포괄하는 맞춤형 치료를 적용한다."
    elif '심리검사' in badge:
        line3 = f"3. 검사 결과를 토대로 위기 행동화 가능성을 선제적으로 차단하고 개별화된 심리치료 목표를 구체적으로 수립한다."
    elif '가족치료' in badge:
        line3 = f"3. 가족원 간의 역기능적 의사소통을 일치형으로 교정하고 자아분화 수준을 향상시키는 구조적·전략적 개입을 단행한다."
    elif '진로상담' in badge:
        line3 = f"3. 비합리적인 진로 신념과 지각된 진로 장벽을 효과적으로 다루며 능동적인 진로 탐색 및 의사결정 기술을 훈련한다."
    elif '교육' in badge or '교수' in badge:
        line3 = f"3. 교사와 학생 간의 촉진적 상호작용을 극대화하고 다양한 교수 매체와 맞춤형 피드백을 유기적으로 투입한다."
    else:
        line3 = f"3. 내담자의 자각과 통찰을 촉진하는 구체적 상담 기법을 적용하여 문제 행동의 소거와 건설적 대안 형성을 돕는다."
        
    # 4. Fourth line: Expected outcome / Educational or clinical significance
    line4 = f"4. 궁극적으로 대상자의 자기조절능력과 자율적 기능을 회복시키고 지속 가능한 성장을 도모하는 데 핵심 의의가 있다."
    
    return f"{line1}\n{line2}\n{line3}\n{line4}"

# Test on 10 items
for i in [0, 10, 30, 50, 80, 100, 130, 160, 190, 202]:
    print(f"=== Item {items[i]['num']}: {items[i]['kw']} ===")
    print(generate_perfect_4lines(items[i]))
    print()
