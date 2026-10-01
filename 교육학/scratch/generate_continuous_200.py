import json
import sys
import os

sys.path.insert(0, os.path.abspath('scratch'))
import generate_continuous_150 as gen_base

# 1~150 items
with open('scratch/items_150_raw.json', 'r', encoding='utf-8') as f:
    items_150 = json.load(f)

refined_kws = dict(gen_base.refined_kws)
compact_answers = dict(gen_base.compact_answers)

# 151~200 new items
items_50_new = [
    {
        "num": 151,
        "badge": "교육행정",
        "kw": "도덕적 리더십 (세르지오바니)",
        "q": "지도자가 추종자의 자율성과 도덕적 책무성을 신뢰하며, 학교를 가치와 규범을 공유하는 도덕적 공동체로 변혁시키는 서번트 기반 리더십의 명칭을 쓸 것.",
        "ans": "학교 구성원들이 내면화된 선의와 전문적 책무성에 따라 스스로 주도적으로 직무를 수행하도록 이끄는 '도덕적 리더십'이다."
    },
    {
        "num": 152,
        "badge": "교육행정",
        "kw": "분산적 리더십 (스필레인)",
        "q": "학교장 한 사람의 독점적 권한에서 벗어나, 학교의 상황적 맥락 속에서 지도자, 추종자, 상황의 상호작용을 통해 리더십 실행을 공동 분담하는 리더십 명칭을 쓸 것.",
        "ans": "리더와 구성원 간의 상호작용 및 조직 상황의 분산성을 바탕으로 다수의 구성원이 전문성을 발휘하여 공동의 목표를 달성하는 '분산적 리더십'이다."
    },
    {
        "num": 153,
        "badge": "교육행정",
        "kw": "변혁적 리더십 (번스·배스)",
        "q": "구성원의 고차원적 욕구와 사기를 진작시키고 학교의 비전 공유, 지적 자극, 개별적 배려를 통해 기대 이상의 성과를 창출하는 리더십의 명칭을 쓸 것.",
        "ans": "이상적 영향력, 영감적 동기화, 지적 자극, 개별적 배려의 4요소를 통해 구성원의 변화와 헌신을 유도하는 '변혁적 리더십'이다."
    },
    {
        "num": 154,
        "badge": "교육행정",
        "kw": "임상장학 (골드해머·코건)",
        "q": "교사의 실제 교실 수업 행위를 개선하기 위해 장학담당자와 교사가 동등한 입장에서 사전 협의회, 수업 관찰, 피드백 협의회의 3단계를 밟는 장학의 명칭을 쓸 것.",
        "ans": "교실 수업 관찰 데이터를 객관적으로 수집·분석하여 교사의 구체적 수업 기술 향상을 1:1로 지원하는 교사 중심의 '임상장학'이다."
    },
    {
        "num": 155,
        "badge": "교육행정",
        "kw": "동료장학",
        "q": "둘 이상의 동료 교사들이 수업 개선과 전문성 신장을 위해 상호 수업을 참관하고 협의하며 교수 전략과 자료를 공동 개발하는 장학의 명칭을 쓸 것.",
        "ans": "동료 교사 간의 자율적 협동성을 바탕으로 상호 수업 관찰과 피드백을 주고받으며 교수 능력을 개발하는 '동료장학'이다."
    },
    {
        "num": 156,
        "badge": "교육행정",
        "kw": "관료제 5대 원리 (베버)",
        "q": "현대 학교 조직의 특성 중, 전문화(분업), 권한의 계층화, 규칙과 규정, 몰인정성(비인간성), 경력 지향성의 원리를 제시한 고전적 조직 모형의 명칭을 쓸 것.",
        "ans": "업무의 효율성과 조직의 합리성을 극대화하기 위해 명확한 위계질서와 엄격한 규칙에 따라 운영되는 베버의 '관료제 조직 모형'이다."
    },
    {
        "num": 157,
        "badge": "교육행정",
        "kw": "겟젤스-구바 사회체계 모형",
        "q": "학교 조직 내 인간 행동을 규범적 차원(제도, 역할, 기대)과 개인적 차원(개인, 인성, 욕구 성향)의 유기적 상호작용 결과로 설명하는 체제이론 모형의 명칭을 쓸 것.",
        "ans": "제도의 사회적 기대와 개인의 심리적 욕구 성향이 상호 조화를 이룰 때 조직의 효과성과 만족도가 극대화된다는 '겟젤스-구바 사회체계 모형'이다."
    },
    {
        "num": 158,
        "badge": "교육평가",
        "kw": "성장참조평가",
        "q": "교육과정을 통해 학생이 사전에 비해 얼마나 많은 진보와 성장을 이루었는가에 초점을 두어 초기 능력과 최종 성취 간의 차이를 판정하는 평가 유형의 명칭을 쓸 것.",
        "ans": "출발점 수준 대비 최종 도달 수준의 향상도를 기준으로 평가하여 개별화된 학업 성취와 학습 동기를 촉진하는 '성장참조평가'이다."
    },
    {
        "num": 159,
        "badge": "교육평가",
        "kw": "역동적 평가 (비고츠키 ZPD 기반)",
        "q": "정적인 결과물 평가에서 벗어나, 평가자와 학습자 간의 상호작용과 힌트·비계를 제공하면서 학습자의 잠재적 발달 수준과 학습 능력을 진단하는 평가의 명칭을 쓸 것.",
        "ans": "근접발달영역(ZPD)을 토대로 교수와 평가를 통합하여 아동의 미래 잠재력과 학습 가능성을 진단하는 '역동적 평가'이다."
    },
    {
        "num": 160,
        "badge": "교육평가",
        "kw": "루브릭 (채점기준표)",
        "q": "수행평가에서 학생의 과제 수행 과정과 결과물을 객관적·체계적으로 평가하기 위해 성취 기준과 질적 수준을 다차원 표로 구체화한 채점 도구의 명칭을 쓸 것.",
        "ans": "평가 준거와 성취 수준별 질적 특성을 명확히 진술하여 채점의 객관도를 높이고 학생에게 유의미한 피드백을 제공하는 '루브릭(채점기준표)'이다."
    },
    {
        "num": 161,
        "badge": "교수학습",
        "kw": "정교화 이론 (라이겔루스)",
        "q": "학습 내용을 단순한 정수(전체 개요)에서 시작하여 점진적으로 세부적이고 복잡한 수준으로 구체화해 나가는 줌인-줌아웃 방식의 거시적 교수설계 이론 명칭을 쓸 것.",
        "ans": "정수(기본 골격) 제시 ➔ 점진적 정교화 ➔ 요약자 ➔ 종합자 등의 전략을 통해 전체와 부분의 유기적 이해를 돕는 라이겔루스의 '정교화 이론'이다."
    },
    {
        "num": 162,
        "badge": "교수학습",
        "kw": "9가지 수업사태 (가네)",
        "q": "학습자의 내적 인지과정을 촉진하기 위해 교사가 제공하는 주의집중, 학습목표 제시, 선수학습 회상 등 9단계 외적 교수 활동을 체계화한 수업 모형의 명칭을 쓸 것.",
        "ans": "주의집중부터 파지와 학습 전이 증진까지 인간의 내적 정보처리 과정을 1:1로 지원하는 가네의 '9가지 수업사태'이다."
    },
    {
        "num": 163,
        "badge": "교수학습",
        "kw": "플립드 러닝 (역진행 수업)",
        "q": "전통적인 수업 방식을 뒤집어 교실 밖에서 온라인 사전 영상으로 핵심 지식을 습득하고, 정규 수업 시간에는 토론, 프로젝트, 협동학습 등 심화 활동을 수행하는 교수법 명칭을 쓸 것.",
        "ans": "기본 개념 습득을 사전 가정학습으로 이관하고 교실에서는 학생 중심의 고차원적 문제 해결 활동을 전개하는 '플립드 러닝(역진행 수업)'이다."
    },
    {
        "num": 164,
        "badge": "교수학습",
        "kw": "ARCS 동기모델 (켈러)",
        "q": "교수설계에서 학습자의 학습 동기를 유발하고 지속시키기 위한 4대 핵심 범주인 주의집중, 관련성, 자신감, 만족감의 영문 약자로 명명된 동기 모델의 명칭을 쓸 것.",
        "ans": "주의집중(A), 관련성(R), 자신감(C), 만족감(S)의 4대 범주 전략을 수업 전반에 걸쳐 유기적으로 투입하는 켈러의 'ARCS 동기모델'이다."
    },
    {
        "num": 165,
        "badge": "교육심리",
        "kw": "자기결정성 이론 (데시·라이언)",
        "q": "개인이 외적 통제에 의존하지 않고 주체적으로 행동하기 위해 충족되어야 하는 3가지 기본 심리적 욕구인 자율성, 유능성, 관계성을 제시한 동기 이론의 명칭을 쓸 것.",
        "ans": "자율성(선택권), 유능성(효능감), 관계성(소속감)의 욕구가 충족될 때 외적 동기가 내재적 동기로 통합·발달한다는 '자기결정성 이론'이다."
    },
    {
        "num": 166,
        "badge": "진로상담",
        "kw": "하렌 진로의사결정 3유형 (합리적, 직관적, 의존적)",
        "q": "개인이 진로 결정을 내릴 때 나타내는 전형적인 인지적 양식으로, 논리적 분석형, 즉각적 감정형, 타인 위임형의 3대 의사결정 유형을 제시한 학자의 모델을 쓸 것.",
        "ans": "체계적으로 정보를 탐색하는 '합리적 유형', 순간의 느낌에 의존하는 '직관적 유형', 타인의 결정에 책임을 전가하는 '의존적 유형'이다."
    },
    {
        "num": 167,
        "badge": "진로상담",
        "kw": "겔라트 의사결정 모델",
        "q": "진로의사결정을 예측 체계, 가치 체계, 결정 기준의 세 가지 요소를 바탕으로 순환적·연속적으로 전개해 나가는 의사결정 모형의 명칭을 쓸 것.",
        "ans": "대안별 결과 가능성을 따지는 예측 체계와 개인적 선호도인 가치 체계를 결합하여 최선의 진로 대안을 선택하는 겔라트의 '의사결정 모델'이다."
    },
    {
        "num": 168,
        "badge": "심리검사",
        "kw": "WMI (작업기억 지표, K-WISC-V)",
        "q": "웩슬러 아동 지능검사(K-WISC-V) 5대 지표 중, 시각·청각 정보에 주의를 집중하고 머릿속에서 일시적으로 유지·조작하는 능력을 평가하는 지표의 공식 약자를 쓸 것.",
        "ans": "숫자 및 그림기억 소검사를 통해 주의력과 정보 조작 능력을 측정하는 작업기억 지표인 'WMI'이다."
    },
    {
        "num": 169,
        "badge": "심리검사",
        "kw": "PSI (처리속도 지표, K-WISC-V)",
        "q": "K-WISC-V 5대 기본 지표 중, 단순 시각 정보를 빠르고 정확하게 식별하고 손-눈 협응으로 기호를 변환하거나 찾는 정신운동 속도 지표의 공식 약자를 쓸 것.",
        "ans": "기호쓰기와 동형찾기 소검사를 통해 시각적 탐색 속도와 처리 효율성을 평가하는 처리속도 지표인 'PSI'이다."
    },
    {
        "num": 170,
        "badge": "심리검사",
        "kw": "T점수 공식 및 표준점수",
        "q": "정규분포에서 원점수를 평균 50, 표준편차 10으로 변환하여 개인의 상대적 위치를 표준화한 점수의 명칭과 산출 공식(10Z + 50)의 척도 명칭을 쓸 것.",
        "ans": "Z점수에 10을 곱하고 50을 더하여 소수점과 음수를 없앤 표준점수 척도인 'T점수'이다."
    },
    {
        "num": 171,
        "badge": "심리검사",
        "kw": "문장완성검사 (SCT)",
        "q": "미완성된 문장의 뒷부분을 피검자가 자유롭게 연상하여 완성하게 함으로써 내담자의 욕구, 콤플렉스, 부모상, 이성관 등 대인관계 역동을 탐색하는 반구조화 투사검사의 명칭을 쓸 것.",
        "ans": "가족, 성, 자기개념, 대인관계 4대 영역의 무의식적 태도와 갈등을 파악하는 대표적 반투사 검사인 '문장완성검사(SCT)'이다."
    },
    {
        "num": 172,
        "badge": "심리검사",
        "kw": "로샤 검사 (형태반응 Ro%, 람다 Lambda)",
        "q": "10장의 잉크반점 카드에 대한 반응 중, 피검자가 잉크의 객관적 형태에 얼마나 충실하게 반응했는지를 나타내는 지표와 단순 반응 비율(람다)을 뜻하는 검사의 명칭을 쓸 것.",
        "ans": "자극의 형태 특징에 근거하여 현실 검증력과 정서 조절 양식을 다각도로 평가하는 투사적 성격검사인 '로샤 검사'이다."
    },
    {
        "num": 173,
        "badge": "심리검사",
        "kw": "검사-재검사 신뢰도 (안정성 계수)",
        "q": "동일한 측정 도구를 동일한 대상에게 일정한 시간 간격을 두고 두 번 실시하여 얻은 두 검사 점수 간의 상관계수로 측정의 시간적 안정성을 나타내는 신뢰도의 명칭을 쓸 것.",
        "ans": "측정 도구가 시간의 경과에도 불구하고 일관된 결과를 산출하는지를 검증하는 '검사-재검사 신뢰도'이다."
    },
    {
        "num": 174,
        "badge": "심리검사",
        "kw": "공존타당도, 예측타당도 (준거타당도)",
        "q": "새로운 검사의 타당도를 검증할 때, 이미 공인된 현재 기준의 검사와 비교하는 타당도와 미래의 특정 행동이나 성공을 예견하는 타당도를 각각 구분하여 쓸 것.",
        "ans": "현재 시점의 공인 준거와 상관을 구하는 '공존타당도'와, 미래의 수행 결과를 예측하는 능력을 평가하는 '예측타당도'이다."
    },
    {
        "num": 175,
        "badge": "진로상담",
        "kw": "진로의사결정 곤란 검사 (CDDQ)",
        "q": "진로의사결정 과정에서 겪는 어려움을 의사결정 이전 단계(준비도 부족), 의사결정 중 단계(정보 부족), 의사결정 실행 단계(일관성 없는 정보)로 범주화한 진로장벽 진단 도구 명칭을 쓸 것.",
        "ans": "준비도, 정보 부족, 일관성 없는 정보의 3대 대영역에서 내담자의 의사결정 곤란 원인을 세부 진단하는 'CDDQ(진로의사결정 곤란 검사)'이다."
    },
    {
        "num": 176,
        "badge": "성격심리",
        "kw": "아들러 4대 생활양식 (지배형, 기생형, 회피형, 사회적 유용형)",
        "q": "아들러의 개인심리학에서 사회적 관심과 활동 수준의 고저에 따라 개인의 독특한 삶의 태도를 4가지 범주로 분류한 생활양식의 공식 명칭을 쓸 것.",
        "ans": "독단적이고 공격적인 지배형, 타인에게 의존하는 기생형, 도전을 피하는 회피형, 사회에 공헌하는 '사회적 유용형'의 4대 생활양식이다."
    },
    {
        "num": 177,
        "badge": "성격심리",
        "kw": "열등감 보상, 우월성 추구 (아들러)",
        "q": "인간이 선천적으로 지닌 신체적·심리적 무력감과 불완전성을 극복하기 위해 잠재력을 발휘하고 더 높은 완성으로 나아가게 만드는 핵심 동기 2가지를 쓸 것.",
        "ans": "인간 행동의 보편적 출발점인 '열등감(보상 기제)'과, 자기완성과 이상 실현을 향해 나아가는 원동력인 '우월성 추구'이다."
    },
    {
        "num": 178,
        "badge": "정신분석",
        "kw": "반동형성 (방어기제)",
        "q": "무의식 속의 수용할 수 없는 충동, 적대감, 공격성을 정반대의 과장된 친절이나 극단적인 도덕적 행동으로 위장하여 표현하는 자아방어기제의 명칭을 쓸 것.",
        "ans": "본래의 억압된 충동과 완전히 반대되는 태도나 행동을 과도하게 표출하여 불안을 방어하는 '반동형성'이다."
    },
    {
        "num": 179,
        "badge": "정신분석",
        "kw": "전치 (치환, 전위)",
        "q": "특정 대상에게 느낀 분노나 적대감을 직접 표현하지 못하고, 덜 위협적이고 만만한 제3의 대상(예: 종로에서 뺨 맞고 한강에서 눈 흘기기)에게 화풀이하는 방어기제의 명칭을 쓸 것.",
        "ans": "본능적 충동이나 공격성을 원래의 대상 대신 안전하고 취약한 대리 대상에게로 돌리는 '전치(치환)'이다."
    },
    {
        "num": 180,
        "badge": "정신분석",
        "kw": "승화 (방어기제)",
        "q": "성적 충동이나 공격적 충동 등 사회적으로 용납되기 어려운 원초적 에너지를 예술, 학문, 스포츠, 봉사 등 건설적이고 가치 있는 활동으로 전환시키는 가장 성숙한 방어기제의 명칭을 쓸 것.",
        "ans": "무의식의 본능적 욕구를 사회적으로 유용하고 인정받는 창조적 출구로 변용시키는 가장 성숙한 방어기제인 '승화'이다."
    },
    {
        "num": 181,
        "badge": "정신분석",
        "kw": "훈습 (Working Through)",
        "q": "정신분석에서 내담자가 상담자의 해석을 통해 자신의 무의식적 저항과 전이를 통찰한 후, 이를 실제 일상생활 속에서 반복적으로 재경험하며 새로운 행동으로 정착시켜 나가는 지속적 과정의 명칭을 쓸 것.",
        "ans": "통찰된 무의식 갈등을 현실에 적용하고 반복 수정하여 자아의 통합과 영구적 성격 변화를 이루는 '훈습'이다."
    },
    {
        "num": 182,
        "badge": "다문화상담",
        "kw": "수(Sue) 다문화 역량 3대 차원 (인식, 지식, 기술)",
        "q": "전문상담교사가 다양한 문화적 배경을 지닌 학생을 효과적으로 돕기 위해 갖추어야 할 3대 다문화 상담 역량(자신의 문화적 신념 자각, 내담자 세계관 이해, 적절한 개입 전략)의 명칭을 쓸 것.",
        "ans": "상담자 자신의 편견과 가치관을 자각하는 '인식', 타문화에 대한 '지식', 문화적으로 적합한 상담 '기술'의 3대 차원이다."
    },
    {
        "num": 183,
        "badge": "다문화상담",
        "kw": "미세공격 (미세모욕, 미세폭행, 미세무효화)",
        "q": "일상생활에서 소수 집단이나 다문화 학생을 향해 무의식적·은연중에 행해지는 사소하지만 누적적인 언어적·비언어적 폄훼와 차별 행동을 뜻하는 공식 용어와 3대 하위 유형을 쓸 것.",
        "ans": "노골적 차별인 미세폭행, 미묘한 경멸인 미세모욕, 정체성 부인인 미세무효화로 구성된 일상적 차별 기제인 '미세공격'이다."
    },
    {
        "num": 184,
        "badge": "성격심리",
        "kw": "자기통제 및 지연만족 (만족지연)",
        "q": "눈앞의 즉각적인 작은 보상이나 유혹을 물리치고, 장기적인 더 큰 목표와 미래의 보상을 달성하기 위해 자신의 충동을 억제하고 통제하는 인지적 능력의 명칭을 쓸 것.",
        "ans": "장기적 목표 달성을 위해 현재의 충동적 만족을 보류하고 인내하는 인지-행동적 자기조절 능력인 '지연만족(만족지연)'이다."
    },
    {
        "num": 185,
        "badge": "성격심리",
        "kw": "빅파이브 (Big 5 성격 5요인 모델)",
        "q": "골드버그와 코스타·맥크래가 제안한 인간 성격의 보편적 5대 특질(외향성, 친화성, 성실성, 신경증, 개방성)을 뜻하는 성격 모델의 명칭을 쓸 것.",
        "ans": "외향성(E), 친화성(A), 성실성(C), 신경증(N), 개방성(O)의 5가지 차원으로 개인의 성격을 포괄적으로 기술하는 'Big 5(5요인 모델)'이다."
    },
    {
        "num": 186,
        "badge": "상담이론",
        "kw": "인지적 탈융합 (수용전념치료 ACT)",
        "q": "수용전념치료(ACT)에서 부정적 생각이나 기억을 객관적 사실이나 현실 그 자체와 동일시하지 않고, 단지 머릿속을 지나가는 언어적 사건이나 생각 찌꺼기로 분리하여 바라보게 하는 기법의 명칭을 쓸 것.",
        "ans": "생각과 자아를 동일시하는 인지적 융합 상태에서 벗어나 생각을 흘러가는 관찰 대상으로 분리하는 '인지적 탈융합' 기법이다."
    },
    {
        "num": 187,
        "badge": "상담이론",
        "kw": "심리적 유연성 (ACT 헥사플렉스)",
        "q": "ACT의 궁극적 치료 목표로서, 수용, 탈융합, 현재 접촉, 맥락적 자기, 가치, 전념행동의 6가지 핵심 과정을 통해 삶의 고통을 수용하며 가치 있는 행동을 실천하는 능력의 명칭을 쓸 것.",
        "ans": "불필요한 고통 회피를 멈추고 자신의 가치 지향적 삶을 향해 전념 행동을 선택·유지하는 능력인 '심리적 유연성'이다."
    },
    {
        "num": 188,
        "badge": "상담이론",
        "kw": "자기교시훈련 (메이켄바움)",
        "q": "충동적이거나 주의가 산만한 아동에게 인지적 자기통제력을 길러주기 위해 인지적 모델링 ➔ 외현적 지도 ➔ 외현적 자기지도 ➔ 흐려진 자기지도 ➔ 내현적 자기지도로 내면화하는 훈련의 명칭을 쓸 것.",
        "ans": "교사의 시범과 혼잣말을 아동 내면의 인지적 통제 언어로 단계적으로 전환시키는 '자기교시훈련'이다."
    },
    {
        "num": 189,
        "badge": "상담이론",
        "kw": "스트레스 면역훈련 (SIT, 메이켄바움)",
        "q": "스트레스 상황에 대한 대처 능력을 길러주기 위해 개념적 교육 단계 ➔ 대처 기술 획득 및 시연 단계 ➔ 실제 적용 및 유지 단계의 3단계를 거치는 인지행동 치료 프로그램의 명칭을 쓸 것.",
        "ans": "백신을 접종하듯 점진적으로 스트레스 유발 상황에 노출시키며 인지적 대처 기술을 숙달시키는 '스트레스 면역훈련(SIT)'이다."
    },
    {
        "num": 190,
        "badge": "가족치료",
        "kw": "시련기법 (헤일리)",
        "q": "증상(예: 야뇨증, 불면)을 유지하는 것이 그 증상을 포기하는 것보다 훨씬 더 큰 신체적·심리적 고통이나 번거로움을 겪도록 의도적으로 엄격한 과제를 부과하는 기법의 명칭을 쓸 것.",
        "ans": "증상이 발생할 때마다 힘들고 유익한 고된 과제(시련)를 완수하게 하여 증상의 이득을 무력화하고 소거하는 '시련기법'이다."
    },
    {
        "num": 191,
        "badge": "가족치료",
        "kw": "가장기법 (마달레네스)",
        "q": "전략적 가족치료에서 내담자에게 저항을 줄이기 위해 '마치 문제행동이 있는 것처럼 가장해 보라'고 지시하여 증상을 자발적 통제 하에 두게 만드는 역설적 기법의 명칭을 쓸 것.",
        "ans": "문제 증상을 통제 불가능한 질병이 아니라 연기하고 흉내 내는 놀이로 전환시켜 증상의 강박성을 해체하는 '가장기법'이다."
    },
    {
        "num": 192,
        "badge": "가족치료",
        "kw": "빙산 탐색 기법 (사티어)",
        "q": "인간의 경험을 수면 위의 행동(1수준)과 수면 아래의 대처방식, 감정, 감정에 대한 감정, 지각, 기대, 열망, 자기(7수준)로 구조화하여 내면의 심층 변형을 이끄는 사티어 기법의 명칭을 쓸 것.",
        "ans": "표면적 문제행동 밑에 숨겨진 기대, 열망, 참된 자기와의 접촉을 단계적으로 파고내려가는 '빙산 탐색 기법'이다."
    },
    {
        "num": 193,
        "badge": "가족치료",
        "kw": "가족조각 기법 (사티어)",
        "q": "가족원들의 비언어적 의사소통, 정서적 거리감, 권력 위계를 가시화하기 위해 가족원들의 몸짓과 시선, 위치를 조각상처럼 배치해 보게 하는 공간적 치료 기법의 명칭을 쓸 것.",
        "ans": "가족의 무의식적 관계 역동과 내면의 정서를 공간적인 신체 조형물로 형상화하여 통찰을 촉진하는 '가족조각 기법'이다."
    },
    {
        "num": 194,
        "badge": "행동치료",
        "kw": "토큰경제",
        "q": "표적 바람직한 행동을 수행할 때마다 즉각 상징적 보상(스티커, 토큰)을 지급하고, 이를 일정 수량 모으면 실제 특권이나 물질적 강화물(후속강화물)로 교환해 주는 체계의 명칭을 쓸 것.",
        "ans": "조건강화물인 토큰을 매개로 지연된 후속강화물과 연계하여 바람직한 적응 행동의 발생 빈도를 체계적으로 증가시키는 '토큰경제'이다."
    },
    {
        "num": 195,
        "badge": "행동치료",
        "kw": "행동조성 (셰이핑)",
        "q": "학습자가 현재 전혀 수행하지 못하는 새로운 표적 행동을 형성하기 위해, 최종 목표 행동에 점진적으로 근접하는 행동에만 단계적으로 차별 강화를 제공하는 기법의 명칭을 쓸 것.",
        "ans": "최종 목표 행동의 도달을 위해 점진적 접근 행동만을 연속적으로 강화해 나가는 '행동조성(셰이핑)'이다."
    },
    {
        "num": 196,
        "badge": "정신병리",
        "kw": "신경성 식욕부진증 (거식증)",
        "q": "체중 증가와 비만에 대한 극심한 공포로 인해 현저한 저체중 상태에서도 음식 섭취를 제한하고, 자신의 체형과 체중에 대해 심각한 인지적 왜곡을 보이는 섭식장애의 공식 명칭을 쓸 것.",
        "ans": "신체 건강에 치명적인 현저한 저체중과 체형에 대한 왜곡된 자기평가를 특징으로 하는 '신경성 식욕부진증'이다."
    },
    {
        "num": 197,
        "badge": "정신병리",
        "kw": "신경성 폭식증",
        "q": "통제력을 상실한 채 짧은 시간 동안 통상적인 양보다 훨씬 많은 음식을 먹어치우는 폭식 삽화와 더불어, 체중 증가를 막기 위해 구토나 하제 사용 등 부적절한 보상행동을 주 1회 이상 반복하는 장애의 명칭을 쓸 것.",
        "ans": "통제 불능의 반복적 폭식과 스스로 유도한 구토 등 부적응적 보상행동이 필수적으로 동반되는 '신경성 폭식증'이다."
    },
    {
        "num": 198,
        "badge": "정신병리",
        "kw": "신체변형장애 (신체이형장애)",
        "q": "타인의 눈에는 전혀 띄지 않거나 아주 사소한 외모적 결함에 집착하여 하루에 수 시간씩 거울을 확인하거나 피부를 뜯고 외출을 거부하는 강박 관련 장애의 명칭을 쓸 것.",
        "ans": "인지된 외모의 사소한 결점에 대한 과도한 몰두와 반복적인 확인 행동을 특징으로 하는 '신체변형장애'이다."
    },
    {
        "num": 199,
        "badge": "정신병리",
        "kw": "작위성 장애 (인위성 장애)",
        "q": "경제적 보상이나 처벌 회피 등 외적인 현실적 이득이 전혀 없음에도 불구하고, 순전히 '환자 역할'을 하여 타인의 동정과 관심을 얻기 위해 신체적·심리적 증상을 고의로 꾸며내거나 자해하는 장애의 명칭을 쓸 것.",
        "ans": "외적 현실 보상 없이 오직 환자 역할을 획득하기 위해 질병 증상을 의도적으로 날조하거나 유발하는 '작위성 장애'이다."
    },
    {
        "num": 200,
        "badge": "정신병리",
        "kw": "조현병 음성증상 (정서적 둔마, 무의욕증)",
        "q": "조현병 환자에게서 관찰되는 정상적 기능의 결핍 현상으로, 감정 표현이 메마르고 자발적 활동 의지가 완전히 상실되는 핵심 병리 현상의 공식 범주 명칭을 쓸 것.",
        "ans": "외부 자극에 대한 감정 반응이 소실되는 정서적 둔마와 목표 지향적 행동을 시작·유지하지 못하는 '조현병의 음성증상'이다."
    }
]

# Combine all 200 items
all_200 = []
for it in items_150:
    num = it['num']
    badge = it['badge']
    kw = refined_kws.get(num, it['kw_name'])
    q = it['question']
    ans = compact_answers.get(num, it['answer'])
    all_200.append({
        'num': num,
        'badge': badge,
        'kw': kw,
        'q': q,
        'ans': ans
    })

for it in items_50_new:
    all_200.append(it)

print(f"Total compiled items: {len(all_200)}")
assert len(all_200) == 200

# HTML generation
html_lines = []
html_lines.append('<!DOCTYPE html>')
html_lines.append('<html lang="ko">')
html_lines.append('<head>')
html_lines.append('  <meta charset="UTF-8">')
html_lines.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
html_lines.append('  <title>2027 KICE 전문상담 1~200 핵심 표제어 연속 총정리 표 (아이케어 다크모드 / 맑은 고딕 10pt)</title>')
html_lines.append('  <style>')
html_lines.append('    @page {')
html_lines.append('      size: A4 portrait;')
html_lines.append('      margin: 12mm 10mm 12mm 10mm;')
html_lines.append('    }')
html_lines.append('    html, body, div, table, thead, tbody, tr, th, td, p, h1, h2, h3, span, button, a {')
html_lines.append('      box-sizing: border-box;')
html_lines.append('      margin: 0;')
html_lines.append('      padding: 0;')
html_lines.append('    }')
html_lines.append('    body {')
html_lines.append('      font-family: "Malgun Gothic", "맑은 고딕", "Apple SD Gothic Neo", sans-serif;')
html_lines.append('      background: #0f1117;')
html_lines.append('      color: #e2e8f0;')
html_lines.append('      line-height: 1.65;')
html_lines.append('      padding: 24px 16px;')
html_lines.append('      -webkit-font-smoothing: antialiased;')
html_lines.append('    }')
html_lines.append('    .no-print-bar {')
html_lines.append('      max-width: 1200px;')
html_lines.append('      margin: 0 auto 20px auto;')
html_lines.append('      background: #161a23;')
html_lines.append('      color: #f1f5f9;')
html_lines.append('      padding: 16px 24px;')
html_lines.append('      border-radius: 12px;')
html_lines.append('      border: 1px solid #2d3748;')
html_lines.append('      display: flex;')
html_lines.append('      justify-content: space-between;')
html_lines.append('      align-items: center;')
html_lines.append('      flex-wrap: wrap;')
html_lines.append('      gap: 14px;')
html_lines.append('      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);')
html_lines.append('    }')
html_lines.append('    .bar-title {')
html_lines.append('      font-size: 1.18rem;')
html_lines.append('      font-weight: 800;')
html_lines.append('      color: #fbbf24;')
html_lines.append('      display: flex;')
html_lines.append('      align-items: center;')
html_lines.append('      gap: 8px;')
html_lines.append('    }')
html_lines.append('    .bar-sub {')
html_lines.append('      font-size: 0.88rem;')
html_lines.append('      color: #94a3b8;')
html_lines.append('      margin-top: 4px;')
html_lines.append('    }')
html_lines.append('    .btn-group {')
html_lines.append('      display: flex;')
html_lines.append('      gap: 10px;')
html_lines.append('      align-items: center;')
html_lines.append('    }')
html_lines.append('    .btn-action {')
html_lines.append('      background: #fbbf24;')
html_lines.append('      color: #0f1117;')
html_lines.append('      border: 1px solid #f59e0b;')
html_lines.append('      padding: 10px 18px;')
html_lines.append('      border-radius: 8px;')
html_lines.append('      font-size: 0.95rem;')
html_lines.append('      font-weight: 800;')
html_lines.append('      cursor: pointer;')
html_lines.append('      text-decoration: none;')
html_lines.append('      display: inline-flex;')
html_lines.append('      align-items: center;')
html_lines.append('      gap: 6px;')
html_lines.append('      font-family: inherit;')
html_lines.append('      transition: background 0.2s;')
html_lines.append('    }')
html_lines.append('    .btn-action:hover {')
html_lines.append('      background: #f59e0b;')
html_lines.append('    }')
html_lines.append('    .btn-home {')
html_lines.append('      background: #1e2536;')
html_lines.append('      color: #e2e8f0;')
html_lines.append('      border-color: #334155;')
html_lines.append('    }')
html_lines.append('    .btn-home:hover {')
html_lines.append('      background: #2d3748;')
html_lines.append('    }')
html_lines.append('    .btn-theme {')
html_lines.append('      background: #1e2536;')
html_lines.append('      color: #fbbf24;')
html_lines.append('      border-color: #d97706;')
html_lines.append('    }')
html_lines.append('    .btn-theme:hover {')
html_lines.append('      background: #2d3748;')
html_lines.append('    }')
html_lines.append('    .table-container {')
html_lines.append('      max-width: 1200px;')
html_lines.append('      margin: 0 auto;')
html_lines.append('      background: #11141d;')
html_lines.append('      border: 1.5px solid #2d3748;')
html_lines.append('      border-radius: 10px;')
html_lines.append('      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6);')
html_lines.append('      overflow: hidden;')
html_lines.append('    }')
html_lines.append('    .table-info-bar {')
html_lines.append('      background: #161b26;')
html_lines.append('      border-bottom: 2px solid #d97706;')
html_lines.append('      padding: 12px 20px;')
html_lines.append('      display: flex;')
html_lines.append('      justify-content: space-between;')
html_lines.append('      align-items: center;')
html_lines.append('      font-size: 0.92rem;')
html_lines.append('      font-weight: 800;')
html_lines.append('      color: #fbbf24;')
html_lines.append('    }')
html_lines.append('    table {')
html_lines.append('      width: 100%;')
html_lines.append('      border-collapse: collapse;')
html_lines.append('      font-family: "Malgun Gothic", "맑은 고딕", "Apple SD Gothic Neo", sans-serif;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      background: #11141d;')
html_lines.append('    }')
html_lines.append('    thead {')
html_lines.append('      background: #161a24;')
html_lines.append('      position: sticky;')
html_lines.append('      top: 0;')
html_lines.append('      z-index: 20;')
html_lines.append('    }')
html_lines.append('    th {')
html_lines.append('      background: #161a24;')
html_lines.append('      color: #fbbf24;')
html_lines.append('      border: 1px solid #283042;')
html_lines.append('      padding: 11px 8px;')
html_lines.append('      font-weight: 800;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      text-align: center;')
html_lines.append('      letter-spacing: -0.2px;')
html_lines.append('    }')
html_lines.append('    td {')
html_lines.append('      border: 1px solid #222938;')
html_lines.append('      padding: 10px 13px;')
html_lines.append('      vertical-align: top;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      line-height: 1.65;')
html_lines.append('      color: #e2e8f0;')
html_lines.append('    }')
html_lines.append('    tr:nth-child(even) {')
html_lines.append('      background: #141822;')
html_lines.append('    }')
html_lines.append('    tr:nth-child(odd) {')
html_lines.append('      background: #10131b;')
html_lines.append('    }')
html_lines.append('    tr:hover {')
html_lines.append('      background: #1e2433;')
html_lines.append('    }')
html_lines.append('    .td-num {')
html_lines.append('      width: 50px;')
html_lines.append('      text-align: center;')
html_lines.append('      font-weight: 800;')
html_lines.append('      color: #fbbf24;')
html_lines.append('      font-size: 10pt;')
html_lines.append('    }')
html_lines.append('    .td-kw {')
html_lines.append('      width: 22%;')
html_lines.append('      word-break: keep-all;')
html_lines.append('    }')
html_lines.append('    .kw-badge {')
html_lines.append('      display: inline-block;')
html_lines.append('      font-size: 8.5pt;')
html_lines.append('      font-weight: 700;')
html_lines.append('      color: #38bdf8;')
html_lines.append('      background: #0f2744;')
html_lines.append('      border: 1px solid #0284c7;')
html_lines.append('      padding: 2px 6px;')
html_lines.append('      border-radius: 4px;')
html_lines.append('      margin-bottom: 4px;')
html_lines.append('    }')
html_lines.append('    .kw-name {')
html_lines.append('      font-weight: 800;')
html_lines.append('      color: #fde047;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      line-height: 1.5;')
html_lines.append('    }')
html_lines.append('    .td-q {')
html_lines.append('      width: 36%;')
html_lines.append('      color: #f1f5f9;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      word-break: keep-all;')
html_lines.append('      line-height: 1.65;')
html_lines.append('    }')
html_lines.append('    .td-ans {')
html_lines.append('      width: 37%;')
html_lines.append('      color: #fef08a;')
html_lines.append('      font-size: 10pt;')
html_lines.append('      font-weight: 600;')
html_lines.append('      word-break: keep-all;')
html_lines.append('      line-height: 1.65;')
html_lines.append('    }')
html_lines.append('    body.light-theme {')
html_lines.append('      background: #f8fafc;')
html_lines.append('      color: #0f172a;')
html_lines.append('    }')
html_lines.append('    body.light-theme .no-print-bar {')
html_lines.append('      background: #0f172a;')
html_lines.append('      border-color: #334155;')
html_lines.append('    }')
html_lines.append('    body.light-theme .bar-title {')
html_lines.append('      color: #38bdf8;')
html_lines.append('    }')
html_lines.append('    body.light-theme .bar-sub {')
html_lines.append('      color: #cbd5e1;')
html_lines.append('    }')
html_lines.append('    body.light-theme .btn-action {')
html_lines.append('      background: #0284c7;')
html_lines.append('      color: #ffffff;')
html_lines.append('      border-color: #38bdf8;')
html_lines.append('    }')
html_lines.append('    body.light-theme .table-container {')
html_lines.append('      background: #ffffff;')
html_lines.append('      border: 1.5px solid #cbd5e1;')
html_lines.append('    }')
html_lines.append('    body.light-theme .table-info-bar {')
html_lines.append('      background: #f1f5f9;')
html_lines.append('      color: #0f172a;')
html_lines.append('      border-bottom: 2px solid #0f172a;')
html_lines.append('    }')
html_lines.append('    body.light-theme table {')
html_lines.append('      background: #ffffff;')
html_lines.append('    }')
html_lines.append('    body.light-theme thead, body.light-theme th {')
html_lines.append('      background: #1e293b;')
html_lines.append('      color: #ffffff;')
html_lines.append('      border-color: #334155;')
html_lines.append('    }')
html_lines.append('    body.light-theme td {')
html_lines.append('      border-color: #cbd5e1;')
html_lines.append('      color: #0f172a;')
html_lines.append('    }')
html_lines.append('    body.light-theme tr:nth-child(even) {')
html_lines.append('      background: #f8fafc;')
html_lines.append('    }')
html_lines.append('    body.light-theme tr:nth-child(odd) {')
html_lines.append('      background: #ffffff;')
html_lines.append('    }')
html_lines.append('    body.light-theme tr:hover {')
html_lines.append('      background: #f1f5f9;')
html_lines.append('    }')
html_lines.append('    body.light-theme .td-num {')
html_lines.append('      color: #0284c7;')
html_lines.append('    }')
html_lines.append('    body.light-theme .kw-badge {')
html_lines.append('      background: #e0f2fe;')
html_lines.append('      color: #1e40af;')
html_lines.append('      border-color: #bae6fd;')
html_lines.append('    }')
html_lines.append('    body.light-theme .kw-name {')
html_lines.append('      color: #0f172a;')
html_lines.append('    }')
html_lines.append('    body.light-theme .td-q {')
html_lines.append('      color: #334155;')
html_lines.append('    }')
html_lines.append('    body.light-theme .td-ans {')
html_lines.append('      color: #0f172a;')
html_lines.append('    }')
html_lines.append('    @media print {')
html_lines.append('      @page {')
html_lines.append('        size: A4 portrait;')
html_lines.append('        margin: 12mm 10mm 12mm 10mm;')
html_lines.append('      }')
html_lines.append('      body {')
html_lines.append('        background: #ffffff !important;')
html_lines.append('        color: #000000 !important;')
html_lines.append('        padding: 0 !important;')
html_lines.append('        font-family: "Malgun Gothic", "맑은 고딕", sans-serif !important;')
html_lines.append('      }')
html_lines.append('      .no-print-bar {')
html_lines.append('        display: none !important;')
html_lines.append('      }')
html_lines.append('      .table-container {')
html_lines.append('        max-width: 100% !important;')
html_lines.append('        box-shadow: none !important;')
html_lines.append('        border: none !important;')
html_lines.append('        border-radius: 0 !important;')
html_lines.append('        margin: 0 !important;')
html_lines.append('        background: #ffffff !important;')
html_lines.append('      }')
html_lines.append('      .table-info-bar {')
html_lines.append('        border-bottom: 2px solid #000000 !important;')
html_lines.append('        padding: 6px 4px !important;')
html_lines.append('        font-size: 9.5pt !important;')
html_lines.append('        background: #f1f5f9 !important;')
html_lines.append('        color: #000000 !important;')
html_lines.append('      }')
html_lines.append('      table {')
html_lines.append('        width: 100% !important;')
html_lines.append('        border-collapse: collapse !important;')
html_lines.append('        font-size: 10pt !important;')
html_lines.append('        background: #ffffff !important;')
html_lines.append('      }')
html_lines.append('      thead {')
html_lines.append('        display: table-header-group !important;')
html_lines.append('      }')
html_lines.append('      tbody {')
html_lines.append('        display: table-row-group !important;')
html_lines.append('      }')
html_lines.append('      tr {')
html_lines.append('        page-break-inside: avoid !important;')
html_lines.append('        break-inside: avoid !important;')
html_lines.append('      }')
html_lines.append('      th {')
html_lines.append('        background: #f1f5f9 !important;')
html_lines.append('        color: #000000 !important;')
html_lines.append('        border: 1px solid #94a3b8 !important;')
html_lines.append('        font-size: 10pt !important;')
html_lines.append('        padding: 6px 5px !important;')
html_lines.append('      }')
html_lines.append('      td {')
html_lines.append('        border: 1px solid #cbd5e1 !important;')
html_lines.append('        font-size: 10pt !important;')
html_lines.append('        padding: 6px 8px !important;')
html_lines.append('        line-height: 1.45 !important;')
html_lines.append('        color: #000000 !important;')
html_lines.append('      }')
html_lines.append('      .kw-name {')
html_lines.append('        color: #000000 !important;')
html_lines.append('      }')
html_lines.append('      .td-num {')
html_lines.append('        color: #0284c7 !important;')
html_lines.append('      }')
html_lines.append('      .td-q {')
html_lines.append('        color: #334155 !important;')
html_lines.append('      }')
html_lines.append('      .td-ans {')
html_lines.append('        color: #000000 !important;')
html_lines.append('      }')
html_lines.append('      tr:nth-child(even) {')
html_lines.append('        background: #f8fafc !important;')
html_lines.append('      }')
html_lines.append('      tr:nth-child(odd) {')
html_lines.append('        background: #ffffff !important;')
html_lines.append('      }')
html_lines.append('    }')
html_lines.append('  </style>')
html_lines.append('</head>')
html_lines.append('<body>')
html_lines.append('')
html_lines.append('  <div class="no-print-bar">')
html_lines.append('    <div>')
html_lines.append('      <div class="bar-title">🏛️ 2027 KICE 전문상담 1~200 핵심 표제어 연속 총정리 표</div>')
html_lines.append('      <div class="bar-sub">아이케어(Eye-Care) 저자극 웜다크 모드 · 맑은 고딕 10pt · 빈칸 없는 완결형 1~200 풀세트 테이블</div>')
html_lines.append('    </div>')
html_lines.append('    <div class="btn-group">')
html_lines.append('      <button id="themeToggleBtn" class="btn-action btn-theme" onclick="toggleTheme()">☀️ 라이트 모드로 전환</button>')
html_lines.append('      <a href="index.html" class="btn-action btn-home">🏠 모의고사 홈</a>')
html_lines.append('      <button class="btn-action" onclick="window.print()">🖨️ A4 바로 인쇄 / PDF 저장</button>')
html_lines.append('    </div>')
html_lines.append('  </div>')
html_lines.append('')
html_lines.append('  <div class="table-container">')
html_lines.append('    <div class="table-info-bar">')
html_lines.append('      <span>📋 2027 임용고시 전문상담 4점 만점 공식 서술 정답 총정리 (No. 1 ~ 200 풀세트)</span>')
html_lines.append('      <span>KICE 공인 명칭·약어 / 맑은 고딕 10pt / 눈이 편안한 웜다크 배색</span>')
html_lines.append('    </div>')
html_lines.append('    <table>')
html_lines.append('      <thead>')
html_lines.append('        <tr>')
html_lines.append('          <th style="width: 55px;">No.</th>')
html_lines.append('          <th style="width: 22%;">영역 및 핵심 표제어</th>')
html_lines.append('          <th style="width: 36%;">❓ KICE 실전 힌트 박멸 문제 (단서)</th>')
html_lines.append('          <th style="width: 37%;">🏆 KICE 4점 만점 공식 서술 정답</th>')
html_lines.append('        </tr>')
html_lines.append('      </thead>')
html_lines.append('      <tbody>')

for it in all_200:
    num = it['num']
    badge = it['badge']
    kw = it['kw']
    q = it['q']
    ans = it['ans']
    
    html_lines.append('        <tr>')
    html_lines.append(f'          <td class="td-num">{num}</td>')
    html_lines.append('          <td class="td-kw">')
    html_lines.append(f'            <span class="kw-badge">{badge}</span>')
    html_lines.append(f'            <div class="kw-name">{kw}</div>')
    html_lines.append('          </td>')
    html_lines.append(f'          <td class="td-q">{q}</td>')
    html_lines.append(f'          <td class="td-ans">{ans}</td>')
    html_lines.append('        </tr>')

html_lines.append('      </tbody>')
html_lines.append('    </table>')
html_lines.append('  </div>')
html_lines.append('')
html_lines.append('  <script>')
html_lines.append('    function toggleTheme() {')
html_lines.append('      var b = document.body;')
html_lines.append('      var btn = document.getElementById("themeToggleBtn");')
html_lines.append('      if (b.classList.contains("light-theme")) {')
html_lines.append('        b.classList.remove("light-theme");')
html_lines.append('        btn.innerText = "☀️ 라이트 모드로 전환";')
html_lines.append('      } else {')
html_lines.append('        b.classList.add("light-theme");')
html_lines.append('        btn.innerText = "🌙 아이케어 웜다크 모드";')
html_lines.append('      }')
html_lines.append('    }')
html_lines.append('  </script>')
html_lines.append('</body>')
html_lines.append('</html>')

full_html = '\n'.join(html_lines)

# Strict Asterisk Check
if '*' in full_html:
    raise ValueError("Found asterisk in generated HTML!")

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Successfully written 200 items to:", target_path)
print("File length in lines:", len(html_lines))
print("File size in bytes:", len(full_html.encode('utf-8')))
print("Zero asterisks strictly verified!")
