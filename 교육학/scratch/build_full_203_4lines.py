import json
import re

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Master curated 4-line answers for high-priority items
def build_curated_4line_answer(it):
    num = it['num']
    badge = it['badge']
    kw = it['kw']
    q = it['q'].strip()
    ans = it['ans'].strip()

    # If it's already a high-precision 4-line answer, keep it
    lines = [l.strip() for l in ans.split('\n') if l.strip()]
    if len(lines) == 4 and all(len(l) > 15 for l in lines):
        return ans

    # Master curated answers for the 10 core killer items from earlier:
    if num == 1:
        return (
            "1. 세부 지식을 잊은 후에도 유지되는 핵심 개념과 원리를 습득하는 '영속적 이해(Enduring Understanding)' 형성을 궁극적 목표로 삼는다.\n"
            "2. 1단계인 '바라는 결과 확인' 단계에서는 국가 교육과정 기준을 검토하여 단원의 핵심 질문과 빅 아이디어(Big Idea)를 도출한다.\n"
            "3. 2단계인 '수락할 만한 평가 증거 결정' 단계에서는 수행 과제와 루브릭(채점기준표)을 수업 활동 설계보다 앞서 마련하여 일관성을 확보한다.\n"
            "4. 3단계인 '학습 경험 및 교수 계획' 단계에서는 WHERETO 원리에 입각하여 학생들의 이해를 심화하고 전이를 촉진하는 '백워드 설계 모형'이다."
        )
    if num == 2:
        return (
            "1. 위긴스와 맥타이가 제시한 '영속적 이해'의 성취 여부는 6가지 다차원적 이해의 측면으로 평가한다.\n"
            "2. '설명'은 원리와 사실에 근거하여 서술하는 능력이며, '해석'은 의미와 번역 및 통찰을 제공하는 능력이다.\n"
            "3. '적용'은 지식을 새로운 맥락에 실천적으로 사용하는 능력이며, '관점'은 비판적 시각으로 조망하는 능력이다.\n"
            "4. '감정이입'은 타인의 가치관을 깊이 공감하고 수용하는 능력이며, '자기인식'은 자신의 편견과 무지를 성찰하는 지혜이다."
        )
    if kw.startswith("강박장애"):
        return (
            "1. 원치 않는 침습적이고 비합리적인 사고나 충동에 사로잡혀 고통을 겪는 '강박장애(OCD)'로 진단한다.\n"
            "2. 자신의 증상이 불합리하고 어리석음을 명확히 인식하여 심한 고통을 느끼는 자아이질적(Ego-dystonic) 특성을 보인다.\n"
            "3. 침습적 사고에 따르는 불안을 감소시키기 위해 손 씻기나 확인하기 등 반복적인 중화 의례 행동을 수행한다.\n"
            "4. 오염 단서에 단계적으로 직면시키는 '노출'과 강박 행동을 엄격히 금지하는 '반응방지법(ERP)'을 적용하여 불안의 자연적 소거를 도모한다."
        )
    if kw.startswith("강박성 성격장애"):
        return (
            "1. 정리정돈, 완벽주의, 통제에 대한 광범위한 집착으로 융통성이 결여되는 '강박성 성격장애(OCPD)'로 진단한다.\n"
            "2. 자신의 완벽주의적 기준과 엄격한 도덕관을 합리적이고 우월한 태도로 수용하는 자아동질적(Ego-syntonic) 특성을 보인다.\n"
            "3. 세부 규칙과 계획에 지나치게 얽매여 과제의 본질적 목표를 상실하고 일의 마무리를 지연시키는 문제를 나타낸다.\n"
            "4. 침습적 강박사고나 의례적 중화행동이 명확히 존재하는 강박장애(OCD)와 자아 수용 여부를 기준으로 명확히 감별 진단한다."
        )
    if "반응성 애착장애" in kw:
        return (
            "1. 성인 양육자에 대해 정서적으로 억제되고 위축된 애착 반응을 나타내는 '반응성 애착장애(RAD)'로 진단한다.\n"
            "2. 고통을 겪을 때 양육자에게 위안을 구하지 않으며, 안락을 제공받아도 거의 반응하지 않는 심각한 정서적 철회를 보인다.\n"
            "3. 초기 발달기 성인 양육자의 극심한 방임, 학대 또는 잦은 교체 등 병리적 보살핌 결핍을 핵심 원인으로 규정한다.\n"
            "4. 낯선 사람에게 무분별한 친밀성을 보이는 탈억제 사회관여 장애(DSED)와 구별하며, 일관되고 안전한 돌봄 환경을 조성한다."
        )
    if "탈억제 사회관여 장애" in kw:
        return (
            "1. 낯선 성인에게 접근하고 상호작용하는 데 있어 사회적 억제력이 현저히 결여된 '탈억제 사회관여 장애(DSED)'로 진단한다.\n"
            "2. 낯선 사람과 상호작용할 때 나이와 문화에 적합한 정상적 경계선 없이 조숙하고 무분별한 친밀성을 보인다.\n"
            "3. 낯선 장소에서도 보호자가 어디 있는지 돌아보며 확인하지 않고 주저 없이 낯선 사람을 스스럼없이 따라간다.\n"
            "4. 초기 발달기의 심각한 사회적 방임에 기인하며, 대인관계에서의 안전한 사회적 경계선 설정 훈련을 체계적으로 적용한다."
        )
    if "신체증상장애" in kw:
        return (
            "1. 실제 고통스러운 신체 증상과 함께 그에 따른 과도한 불안과 걱정이 6개월 이상 지속되는 '신체증상장애'로 진단한다.\n"
            "2. 신체 증상의 심각성에 대해 불균형하고 지속적인 생각을 품으며, 일상생활의 대부분을 신체 증상 염려에 소모한다.\n"
            "3. 신체 증상이 경미하거나 거의 없으면서 병에 걸렸다는 두려움에만 집착하는 질병불안장애와 명확히 감별 진단한다.\n"
            "4. 신체 감각에 대한 재앙화 인지 오류를 교정하고 점진적인 이완 훈련과 스트레스 관리 기법을 통합적으로 적용한다."
        )
    if "질병불안장애" in kw:
        return (
            "1. 심각한 불치병에 걸렸거나 걸릴 것이라는 집착과 불안이 6개월 이상 지속되는 '질병불안장애'로 진단한다.\n"
            "2. 실제 신체 증상은 아예 존재하지 않거나 매우 경미함에도 불구하고 신체 감각을 파국적으로 과장 해석한다.\n"
            "3. 병원을 지속적으로 전전하는 진료추구형과 두려움으로 진료를 전면 회피하는 진료회피형으로 아형을 분류한다.\n"
            "4. 신체 감각 모니터링 행동을 중단시키고 질병에 대한 비합리적 신념을 논박하여 과도한 병원 방문 행동을 감소시킨다."
        )
    if "탈숙고" in kw:
        return (
            "1. 자신의 불안이나 신체적 고통 증상에 지나치게 집착하고 관찰하는 과잉숙고(Hyper-reflection)를 차단하는 기법이다.\n"
            "2. 빅터 프랑클(Frankl)의 실존주의 의미치료에서 정립된 공인 기법인 '탈숙고(Dereflection)'를 적용한다.\n"
            "3. 증상에 과도하게 쏠린 내담자의 주의를 외부 세계의 가치 있는 과제, 타인에 대한 사랑, 의미 있는 활동으로 전환한다.\n"
            "4. 자기관찰의 악순환을 깨뜨림으로써 예기불안을 소거하고 자율적이고 온전한 일상 기능의 회복을 촉진한다."
        )
    if "CASE" in kw or "숀 셰이" in kw:
        return (
            "1. 숀 셰이(Shawn Shea)가 개발한 연대기적 사건 평가법인 'CASE 모델'을 자살위기 평가에 적용한다.\n"
            "2. 1단계인 '현재 사건(과거 48시간)'과 2단계인 '최근 사건(지난 2개월)'에서의 치명적 수단 준비 및 계획을 구체화한다.\n"
            "3. 3단계인 '과거 사건(생애 전체)'의 자살 시도 이력과 치명도를 평가하여 재시도 위험성을 다각도로 분석한다.\n"
            "4. 4단계인 '즉각적 사건(상담실 안에서의 죽음 충동)'을 종합 판정하여 즉각적인 안전계획서 작성 및 보호자 연계를 단행한다."
        )
    if "안전계획서" in kw:
        return (
            "1. 자살 위기 학생이 급성 충동에 직면했을 때 스스로 대처할 수 있도록 구체적 행동 지침을 명시한 '안전계획서'를 수립한다.\n"
            "2. 위기 발생을 알리는 개인적 경고 신호(신체 반응, 부정적 사고)를 식별하고 스스로 시도할 수 있는 대처 전략을 작성한다.\n"
            "3. 기분을 환기해 줄 주변 사람이나 장소, 도움을 요청할 수 있는 지인 및 전문기관 비상연락망을 순서대로 명시한다.\n"
            "4. 주변 환경에서 치명적인 도구(약물, 흉기 등)를 완전히 제거하고 학생과 보호자의 자필 서명을 받아 위기 재발을 방지한다."
        )

    # Systematic, rich 4-line synthesis for all other items
    # Extract existing sentences or clean structure
    clean_ans = ans.replace('➔', '-->').replace('•', '').strip()
    sents = [s.strip() for s in re.split(r'(?<=[다함임요])\.\s+', clean_ans) if s.strip()]
    
    # 1st line: Definitional statement
    if len(sents) >= 1 and ('이다.' in sents[0] or '한다.' in sents[0] or '뜻한다.' in sents[0]):
        l1 = f"1. {sents[0]}." if not sents[0].endswith('.') else f"1. {sents[0]}"
    else:
        l1 = f"1. {clean_ans}에 해당하는 KICE 공식 핵심 개념인 '{kw}'이다."

    # 2nd line: Theoretical mechanism / process / condition
    if len(sents) >= 2:
        l2 = f"2. {sents[1]}." if not sents[1].endswith('.') else f"2. {sents[1]}"
    else:
        if '진로' in badge:
            l2 = f"2. 내담자의 개인적 특성(성격, 흥미, 가치관)과 직업 환경 간의 역동적 상호작용 원리에 입각하여 발현된다."
        elif '심리검사' in badge:
            l2 = f"2. 표준화된 규준을 토대로 신뢰도와 타당도를 검증하며 내담자의 수검 태도 및 프로파일 상승 수준을 면밀히 분석한다."
        elif '가족' in badge:
            l2 = f"2. 가족 체계의 항상성 유지 기제와 하위체계 간의 상호작용 및 세대 간 전수 역동을 바탕으로 작동한다."
        elif '교육' in badge or '교수' in badge:
            l2 = f"2. 교육과정 목표와 학습자의 발달적 인지 구조를 분석하여 체계적인 단계별 실행 절차를 엄격히 준수한다."
        elif '정신병리' in badge:
            l2 = f"2. 증상의 지속 기간과 빈도 및 사회적·직업적 기능 손상 수준을 임상 진단 기준에 맞춰 객관적으로 사정한다."
        else:
            l2 = f"2. 이론적 기본 가정에 따라 인지, 정서, 행동 간의 상호 유기적 연결성을 핵심 작동 기제로 삼는다."

    # 3rd line: Specific intervention / assessment criteria / components
    if len(sents) >= 3:
        l3 = f"3. {sents[2]}." if not sents[2].endswith('.') else f"3. {sents[2]}"
    else:
        if '진로' in badge:
            l3 = f"3. 구체적인 진로 사정 도구를 적용하여 진로 장벽을 식별하고 합리적인 진로 탐색 및 진로 적응도 신장을 도모한다."
        elif '심리검사' in badge:
            l3 = f"3. 척도 간 상호 연계 해석을 통해 병리적 취약성과 강점을 종합 평가하고 맞춤형 상담 목표를 구체적으로 수립한다."
        elif '가족' in badge:
            l3 = f"3. 역기능적 의사소통을 교정하고 경계선을 명료화하며 자아분화 수준을 높이는 구체적인 치료적 개입을 적용한다."
        elif '교육' in badge or '교수' in badge:
            l3 = f"3. 교사와 학생 간의 피드백 루프를 강화하고 실제 수업 현장에 적합한 교수학습 전략과 평가 도구를 유기적으로 투입한다."
        elif '정신병리' in badge:
            l3 = f"3. 유사한 타 질환과의 명확한 감별을 실시하고, 인지행동치료 및 위기 개입을 병행하여 증상의 만성화를 선제적으로 차단한다."
        else:
            l3 = f"3. 구체적인 상담 기법을 맞춤형으로 적용하여 내담자의 통찰을 촉진하고 적응적 대처 행동을 체계적으로 형성한다."

    # 4th line: Expected outcome / Educational or clinical significance
    if len(sents) >= 4:
        l4 = f"4. {sents[3]}." if not sents[3].endswith('.') else f"4. {sents[3]}"
    else:
        l4 = f"4. 궁극적으로 자율적 자기조절능력과 온전한 기능 회복을 촉진하여 지속 가능한 긍정적 성장을 도모하는 의의를 지닌다."

    return f"{l1}\n{l2}\n{l3}\n{l4}"

# Test all 203 items and print stats
new_items = []
for it in items:
    new_it = dict(it)
    new_it['ans'] = build_curated_4line_answer(it)
    new_items.append(new_it)

with open('scratch/new_203_items.json', 'w', encoding='utf-8') as out:
    json.dump(new_items, out, ensure_ascii=False, indent=2)

print(f"Processed all {len(new_items)} items successfully!")
