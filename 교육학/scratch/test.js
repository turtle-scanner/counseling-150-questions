
    
    // TTS Voice Setup
    function speakText(text) {
      if ('speechSynthesis' in window) {
        // Cancel any ongoing speech
        window.speechSynthesis.cancel();
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ko-KR';
        utterance.rate = 1.3;  // Slightly faster/upbeat
        utterance.pitch = 1.7; // Higher pitch for a brighter/cuter female voice tone
        
        // Try to force a female voice if multiple Korean voices exist
        const voices = window.speechSynthesis.getVoices();
        const koVoices = voices.filter(v => v.lang.includes('ko'));
        if (koVoices.length > 0) {
          utterance.voice = koVoices[0]; // Usually the default OS female voice (Heami/Yuna)
        }
        
        window.speechSynthesis.speak(utterance);
      }
    }

    let items = [{"num": 1, "badge": "교육과정", "kw": "백워드 설계 모형 (영속적 이해)", "q": "평가 계획 선행 수립, 역방향 3단계 설계, 목표·평가·교수 일관성 극대화", "ans": "원하는 결과 확인(1단계) ➔ 수용 가능한 증거 결정(평가 계획, 2단계) ➔ 학습 경험 및 교수 계획(3단계) 순으로 단원을 개발하여 영속적 이해를 도모하는 '백워드 설계 모형'임."}, {"num": 5, "badge": "교육과정", "kw": "표현적 결과, 교육적 감식안, 교육비평", "q": "행동목표 한계 비판, 사전 목표 배제, 다의적 성과, 학생 성취 질적 차이 감별, 전문적 심미안", "ans": "사전 목표 없이 활동 중이나 후에 얻어지는 표현적 결과, 성취의 미묘한 질적 차이를 감지하는 교사의 안목인 교육적 감식안, 그리고 이를 언어화하여 공유하는 교육비평임."}, {"num": 3, "badge": "교육과정", "kw": "타바 교사중심 귀납적 교육과정 모형", "q": "현장 교사 주도, 구체적 단원 선행 개발, 상향식 일반화, 귀납적 모형", "ans": "현장 교사가 시험 단원 개발부터 시작하여 검증, 개정·통합, 구조 정착, 확산의 절차를 밟아 수업 현장 적합성을 극대화하는 '타바의 귀납적 교육과정 개발 모형'임."}, {"num": 4, "badge": "교육과정", "kw": "워커 자연주의적 숙의 모형", "q": "참여자 신념 출발, 이해관계 치열한 토론·타협, 숙의 과정, 자연주의적 모형", "ans": "참여자들의 가치와 신념을 확인하는 강령(출발점) ➔ 다양한 대안을 검토하고 타협하는 숙의 ➔ 최종 교육과정을 구조화하는 설계의 3단계로 구성된 '워커의 숙의 모형'임."}, {"num": 151, "badge": "교육행정", "kw": "도덕적 리더십 (세르지오바니)", "q": "추종자 자율성·책무성 신뢰, 가치·규범 공유, 도덕적 공동체 변혁, 서번트 기반 리더십", "ans": "학교 구성원들이 내면화된 선의와 전문적 책무성에 따라 스스로 주도적으로 직무를 수행하도록 이끄는 '도덕적 리더십'임."}, {"num": 159, "badge": "교육평가", "kw": "역동적 평가 (비고츠키 ZPD 기반)", "q": "정적 결과물 평가 탈피, 상호작용 및 비계 제공, 잠재적 발달 수준 진단", "ans": "근접발달영역(ZPD)을 토대로 교수와 평가를 통합하여 아동의 미래 잠재력과 학습 가능성을 진단하는 '역동적 평가'임."}, {"num": 153, "badge": "교육행정", "kw": "변혁적 리더십 (번스·배스)", "q": "고차원적 욕구 진작, 비전 공유, 지적 자극, 개별적 배려, 기대 이상 성과 창출", "ans": "이상적 영향력, 영감적 동기화, 지적 자극, 개별적 배려의 4요소를 통해 구성원의 변화와 헌신을 유도하는 '변혁적 리더십'임."}, {"num": 157, "badge": "교육행정", "kw": "겟젤스-구바 사회체계 모형", "q": "규범적 차원과 개인적 차원 상호작용, 체제이론 모형", "ans": "제도의 사회적 기대와 개인의 심리적 욕구 성향이 상호 조화를 이룰 때 조직의 효과성과 만족도가 극대화된다는 '겟젤스-구바 사회체계 모형'임."}, {"num": 158, "badge": "교육평가", "kw": "성장참조평가", "q": "사전 대비 진보·성장 초점, 초기 능력과 최종 성취 차이 판정", "ans": "출발점 수준 대비 최종 도달 수준의 향상도를 기준으로 평가하여 개별화된 학업 성취와 학습 동기를 촉진하는 '성장참조평가'임."}, {"num": 160, "badge": "교육평가", "kw": "루브릭 (채점기준표)", "q": "과제 수행 과정·결과물 객관적 평가, 성취 기준·질적 수준 다차원 표, 구체화된 채점 도구", "ans": "평가 준거와 성취 수준별 질적 특성을 명확히 진술하여 채점의 객관도를 높이고 학생에게 유의미한 피드백을 제공하는 '루브릭(채점기준표)'임."}, {"num": 2, "badge": "교육과정", "kw": "스킬벡 학교중심 교육과정 개발 모형 (SBCD)", "q": "지역사회 요구 분석, 학교 내외 상황적 특성 분석, 자율적 교육과정 편성·운영", "ans": "상황 분석(외적·내적 요인)을 첫 단계로 삼아 목표 설정, 프로그램 구성, 해석 및 실행, 모니터링·피드백의 5단계를 거치는 '스킬벡의 학교중심 교육과정 개발 모형'임."}, {"num": 6, "badge": "교육과정", "kw": "영 교육과정", "q": "교육적 가치 충분, 정책적·의도적 배제, 공식 교육과정 누락", "ans": "교육적 가치가 충분함에도 공식 교육과정에서 공식적으로 배제되고 누락되어 학생들이 배울 기회를 박탈당하는 '영 교육과정'임."}, {"num": 7, "badge": "교육과정", "kw": "잠재적 교육과정", "q": "물리적 환경·교사 언행·보상 체계, 은연중 은밀한 학습, 무의식적 신념·가치관 총체", "ans": "학교의 제도적 환경, 교사의 언행, 권위주의적 문화 등을 통해 공식적 의도와 무관하게 은연중에 학습되는 '잠재적 교육과정'임."}, {"num": 8, "badge": "교육과정", "kw": "중핵 교육과정", "q": "사회적 문제·실생활 관심사 중심, 분과 교과 유기적 결합, 통합 학습 유도", "ans": "사회적 문제나 실생활 관심사를 중심핵으로 두고, 주변에 여러 분과 교과 내용을 통합 조직하여 문제 해결력을 기르는 '중핵 교육과정'임."}, {"num": 9, "badge": "교육과정", "kw": "학교 자율시간", "q": "학교·교사 교육과정 자율성 확대, 초·중학교 도입, 자율적 시수 편성 제도", "ans": "국가 교육과정에 없는 새로운 과목이나 융합 활동을 학교와 지역 특성에 맞추어 자율적으로 개설·운영할 수 있도록 시수를 확보한 '학교 자율시간'임."}, {"num": 10, "badge": "교육과정", "kw": "메타인지적 지식", "q": "지식 차원 4가지 범주, 인지 과정 자체 성찰·조절, 최상위 지식 범주", "ans": "자신의 학습 전략에 대한 지식, 인지 과제의 조건에 대한 지식, 자기 자신에 대한 성찰적 지식을 포괄하는 최상위 지식인 '메타인지적 지식'임."}, {"num": 11, "badge": "교육과정", "kw": "융합 교육과정 (광역·상관 교육과정)", "q": "분과적 조직 방식 탈피, 인접 교과 공통 내용 묶음, 교과 정체성 유지 통합", "ans": "교과의 고유한 경계를 유지하면서 교과 간 관련된 내용을 1:1로 연결하여 가르치는 '상관 교육과정' 또는 유사 교과를 대영역으로 묶는 '광역 교육과정'임."}, {"num": 12, "badge": "교육과정", "kw": "지식의 구조, 나선형 교육과정", "q": "학문 기저 핵심 개념·원리, 학년 상승에 따른 폭·깊이 심화, 반복 조직 원리", "ans": "각 학문의 핵심 아이디어와 원리인 '지식의 구조'를 학습자의 발달 수준에 맞추어 점진적으로 심화·확대하여 반복 조직하는 '나선형 교육과정'임."}, {"num": 13, "badge": "교육과정", "kw": "쿠레레 4단계 (회귀-전진-분석-종합)", "q": "생애사적 체험 바탕, 과거 소환, 미래 상상, 현재 비판적 성찰, 4단계 실존적 자서전 방법론", "ans": "과거를 회상하는 회귀 ➔ 미래를 조망하는 전진 ➔ 현재를 객관화하는 분석 ➔ 삶을 통합하는 종합의 4단계를 거치는 '파이나의 쿠레레 자서전적 방법'임."}, {"num": 14, "badge": "교육과정", "kw": "교육과정 압축", "q": "우수 학생 대상, 숙달된 교과 내용 압축·생략, 심화·확충 학습 시간 확보", "ans": "영재 및 우수 학습자가 이미 숙달한 정규 교육과정 내용을 압축·생략하여 심화 탐구 및 프로젝트 학습 시간을 확보해 주는 '교육과정 압축'임."}, {"num": 60, "badge": "성격심리", "kw": "개성화 과정 (자기실현)", "q": "인생 후반기, 자아의 자기 자각, 의식·무의식 융합, 전인적 고유 존재 성숙", "ans": "자아가 페르소나와 그림자, 원형들을 통찰하고 통합하여 참된 자기를 실현해 나가는 전인적 성장 과정인 '개성화 과정'임."}, {"num": 72, "badge": "상담이론", "kw": "융합 (게슈탈트)", "q": "자신과 타인 경계 상실, 밀착 상태, 갈등·차이 용납 불가, 접촉경계혼란", "ans": "자신과 타인의 경계가 사라져 밀착됨으로써 차이와 갈등을 수용하지 못하고 독자적 독립성을 상실하는 '융합'임."}, {"num": 76, "badge": "가족치료", "kw": "자기분화 (보웬)", "q": "가족 감정적 소용돌이·융합 탈피, 지적·정서적 체계 분리, 자율성 유지 능력", "ans": "가족의 정서적 소용돌이에 휘말리지 않고 지적 체계와 정서적 체계를 분리하여 주체적 자율성을 유지하는 능력인 '자기분화'임."}, {"num": 80, "badge": "가족치료", "kw": "정서적 단절 (보웬)", "q": "원가족 극심한 밀착·불안 회피, 신체적 도피·대화 거부, 관계 단절, 미분화 방어 행동", "ans": "원가족과의 미해결된 정서적 융합과 불안을 견디지 못하여 물리적으로 도망치거나 접촉을 단절하며 거짓 독립을 연출하는 '정서적 단절'임."}, {"num": 84, "badge": "가족치료", "kw": "명확한 경계선 (미누친)", "q": "정보·정서 교류 조절, 보이지 않는 규칙, 적절한 자율성·친밀성 동시 보장", "ans": "하위체계 간의 자율성과 독립성을 보호하면서도 필요할 때 따뜻한 정서적 교류와 소통이 원활하게 이루어지는 '명확한 경계선'임."}, {"num": 85, "badge": "가족치료", "kw": "경직된 경계선 (유리가족, 미누친)", "q": "소통 극도 차단, 지나친 독립성·고립감, 배려·보살핌 결여", "ans": "하위체계 간의 소통이 극도로 차단되어 구성원 간 배려와 지지가 결여되고 고립감을 유발하는 '경직된 경계선(유리가족)'임."}, {"num": 86, "badge": "가족치료", "kw": "산만한 경계선 (밀착가족, 미누친)", "q": "부모·자녀 경계 붕괴, 사생활 침해, 감정 즉각 전염, 병리적 경계선", "ans": "가족원 간의 경계가 지나치게 허물어져 사생활이 침해되고 한 사람의 감정이 온 가족에게 즉각 전염되는 '산만한 경계선(밀착가족)'임."}, {"num": 38, "badge": "심리검사", "kw": "RC1 (신체증상 호소 척도)", "q": "기질적 신체 이상 무, 신체적 통증·피로 호소, 심리적 갈등 신체화", "ans": "기질적 이상 없이 신체적 통증과 피로를 호소하며 심리적 불안을 신체 증상으로 전환시키는 경향을 측정하는 'RC1' 척도임."}, {"num": 56, "badge": "성격심리", "kw": "페르소나 (융)", "q": "사회 집단 요구·규범 적응, 공적 가면, 외적 인격", "ans": "사회의 요구와 규범에 적응하기 위해 쓰는 공적 가면이지만, 자아와 지나치게 동일시하면 내면의 소외를 낳는 '페르소나'임."}, {"num": 67, "badge": "상담이론", "kw": "논리적 논박 (REBT)", "q": "신념의 논리적 모순 지적, 논리적 전제 도출 과정 질문", "ans": "전제와 결론 사이의 논리적 모순과 비약을 밝혀내어 신념의 비합리성을 검증하는 '논리적 논박'임."}, {"num": 68, "badge": "상담이론", "kw": "실증적 논박 (경험적 논박, REBT)", "q": "현실 경험적 사실 확인, 현실 증거 검증", "ans": "실제 현실 세계의 객관적 사실과 경험적 증거에 비추어 내담자의 신념이 타당한지 검증하는 '실증적 논박(경험적 논박)'임."}, {"num": 69, "badge": "상담이론", "kw": "실용적 논박 (기능적 논박, REBT)", "q": "집착의 유용성 질문, 감정 안정·목표 달성 도움 여부 파악", "ans": "해당 신념을 고수하는 것이 내담자의 감정 안정과 실질적인 목표 달성에 실질적으로 도움이 되는지 따지는 '실용적 논박'임."}, {"num": 70, "badge": "상담이론", "kw": "반전 (게슈탈트)", "q": "공격성·요구 외부 표출 실패, 자해·신체화, 신체·마음 방향 전환", "ans": "타인에게 표현하고 싶은 분노나 요구를 외부로 표출하지 못하고 자신에게 돌려 자해하거나 신체화 증상을 일으키는 '반전'임."}, {"num": 71, "badge": "상담이론", "kw": "내사 (게슈탈트)", "q": "타인 규범·신념 무비판적 수용, 통째로 삼킴, 죄책감 시달림", "ans": "타인의 가치관이나 규범을 비판적으로 수용하지 못하고 무비판적으로 통째로 삼켜 죄책감에 시달리는 접촉경계혼란인 '내사'임."}, {"num": 74, "badge": "상담이론", "kw": "역설적 의도 (의미치료)", "q": "두려워하는 상황 적극 의도, 회피 상황 간절한 바람, 예기불안 단절", "ans": "두려워하고 회피하던 바로 그 증상이나 상황을 스스로 간절히 바라고 의도하게 만들어 예기불안의 악순환을 해체하는 '역설적 의도'임."}, {"num": 75, "badge": "상담이론", "kw": "탈숙고(Dereflection)", "q": "병리적 과다반영 중단, 외부 가치 있는 과업·타인 봉사 주의 전환", "ans": "증상에 대한 병리적 과다반영(자기감시)을 멈추고 외부의 의미 있는 과업이나 타인을 위한 봉사로 주의를 돌리는 '탈숙고(Dereflection)'임."}, {"num": 83, "badge": "가족치료", "kw": "탈삼각화 (보웬)", "q": "가족원 편들기·감정적 소용돌이 거부, 정서적 중립성 유지, 삼각관계 해체", "ans": "상담자가 가족의 정서적 편들기에 휘말리지 않고 중립적 위치를 지켜냄으로써 당사자 둘만의 갈등을 직접 직면하게 하는 '탈삼각화'임."}, {"num": 98, "badge": "정신병리", "kw": "광장공포증", "q": "대중교통·밀폐공간 등 2가지 이상 상황, 공황 발생 시 즉각 탈출·도움 곤란 공포, 극도 회피", "ans": "대중교통, 열린 공간, 밀폐 공간 등 공황 발생 시 즉각 탈출하기 어렵거나 도움받기 어려운 2가지 이상의 상황을 극도로 회피하는 '광장공포증'임."}, {"num": 108, "badge": "정신병리", "kw": "외상후 스트레스 장애 (PTSD)", "q": "생명 위협·외상 사건, 침습적 기억·자극 회피, 인지·기분 부정적 변화, 과각성 1개월 이상 지속", "ans": "생명을 위협하는 외상 사건 후 침습적 재경험, 외상 자극 회피, 인지와 기분의 부정적 변화, 과각성 증상이 1개월 이상 지속되는 '외상후 스트레스 장애(PTSD)'임."}, {"num": 112, "badge": "정신병리", "kw": "경계선 성격장애", "q": "극심한 유기 불안, 극단적 이상화·평가절하 반복, 정체감 혼란, 만성적 공허감, 충동적 자해", "ans": "버림받는 것에 대한 극심한 유기 불안, 극단적 이상화와 평가절하의 반복, 정체감 혼란, 충동적 자해 행동을 보이는 '경계선 성격장애'임."}, {"num": 136, "badge": "상담수퍼비전", "kw": "교사 역할 (버나드 수퍼비전)", "q": "상담 이론·심리검사 해석·치료 기법 직접 강의, 지도 역할", "ans": "초보 상담자에게 상담 이론, 심리검사 해석, 치료 기법을 직접 강의하고 지도하는 버나드 모델의 '교사' 역할임."}, {"num": 138, "badge": "상담수퍼비전", "kw": "자문가 역할 (버나드 수퍼비전)", "q": "동등한 동료, 사례 개입 전략·목표 브레인스토밍 및 논의 역할", "ans": "상담자와 수퍼바이저가 동등한 동료로서 사례 개입 전략과 목표를 협력적으로 브레인스토밍하고 논의하는 '자문가' 역할임."}, {"num": 183, "badge": "다문화상담", "kw": "미세공격 (미세모욕, 미세폭행, 미세무효화)", "q": "소수 집단 대상, 무의식적·은연중 사소한 누적적 폄훼·차별 행동, 3대 하위 유형", "ans": "노골적 차별인 미세폭행, 미묘한 경멸인 미세모욕, 정체성 부인인 미세무효화로 구성된 일상적 차별 기제인 '미세공격'임."}, {"num": 186, "badge": "상담이론", "kw": "인지적 탈융합 (수용전념치료 ACT)", "q": "부정적 생각·기억 객관적 사실과 분리, 머릿속 지나가는 언어적 사건으로 조망", "ans": "생각과 자아를 동일시하는 인지적 융합 상태에서 벗어나 생각을 흘러가는 관찰 대상으로 분리하는 '인지적 탈융합' 기법임."}, {"num": 187, "badge": "상담이론", "kw": "심리적 유연성 (ACT 헥사플렉스)", "q": "수용·탈융합 등 6가지 핵심 과정, 삶의 고통 수용, 가치 있는 행동 실천 능력", "ans": "불필요한 고통 회피를 멈추고 자신의 가치 지향적 삶을 향해 전념 행동을 선택·유지하는 능력인 '심리적 유연성'임."}, {"num": 191, "badge": "가족치료", "kw": "가장기법 (마달레네스)", "q": "마치 문제행동 있는 것처럼 가장 지시, 증상의 자발적 통제화, 역설적 기법", "ans": "문제 증상을 통제 불가능한 질병이 아니라 연기하고 흉내 내는 놀이로 전환시켜 증상의 강박성을 해체하는 '가장기법'임."}, {"num": 16, "badge": "진로상담", "kw": "일관성 (홀랜드)", "q": "성격 6가지 유형 분류, 서로 인접한 유형 간 심리적 일치성·안정성 높음", "ans": "개인의 흥미 프로파일이나 직업 코드의 첫 두 글자가 육각형 상에서 인접해 있을수록 내적 조화와 진로 안정성이 높다는 '일관성'임."}, {"num": 17, "badge": "진로상담", "kw": "계측성 (홀랜드)", "q": "6개 유형 간 이론적·심리적 유사성, 기하학적 육각형 거리에 반비례", "ans": "육각형 상의 기하학적 거리와 성격 유형 간의 심리적 유사성이 반비례하여 인접한 유형은 상관이 높고 대각선 유형은 상관이 가장 낮다는 '계측성'임."}, {"num": 18, "badge": "진로상담", "kw": "변별성 (홀랜드)", "q": "특정 한두 개 유형 점수 매우 높음, 나머지 뚜렷하게 낮음, 흥미 특성 선명 분화", "ans": "흥미 프로파일의 최고점과 최저점 간의 차이가 커서 개인의 직업적 흥미가 얼마나 명확하고 뚜렷하게 분화되어 있는가를 뜻하는 '변별성'임."}, {"num": 19, "badge": "진로상담", "kw": "정체성 (홀랜드)", "q": "목표·흥미·적성 주관적 확신, 명확하고 안정된 청사진, 직업 환경 명확성", "ans": "자신의 목표, 흥미, 적성에 대해 주관적으로 명확하고 안정된 청사진을 가지고 있는 확신 정도를 의미하는 '정체성'임."}, {"num": 20, "badge": "진로상담", "kw": "일치성 (홀랜드)", "q": "성격 유형과 직업 환경 유형 완벽 부합, 높은 직업 만족도 및 생산성", "ans": "개인의 성격 유형과 종사하는 직업 환경의 유형이 일치할수록 높은 직업 만족도, 생산성, 적응도를 나타낸다는 '일치성'임."}, {"num": 21, "badge": "진로상담", "kw": "탐색기 (수퍼)", "q": "고등학교 시기, 잠정기·전환기·실행기 경유, 구체적 진로 목표 탐색·선택", "ans": "자아개념을 다양한 직업적 역할 속에서 검증하고 구체적인 진로 방향을 모색하는 15~24세 시기의 '탐색기'임."}, {"num": 22, "badge": "진로상담", "kw": "확립기 3단계 (수정 ➔ 안정 ➔ 공고화)", "q": "25~44세 성인기, 적합한 직업 분야 정착·발전, 3대 하위 단계", "ans": "자신에게 맞지 않는 분야를 바꾸어 검증하는 수정(시행) ➔ 일자리에 정착하는 안정 ➔ 승진과 인정을 받으며 지위를 굳히는 공고화의 3단계임."}, {"num": 23, "badge": "진로상담", "kw": "C-DAC 모형 (진로발달 평가·상담)", "q": "진로성숙도·직업적응도 체계적 평가, 생애역할·진로발달단계·가치관·적성 포괄 진단", "ans": "생애공간(다양한 역할)과 생애주기(발달단계)를 통합 사정하여 내담자의 진로성숙과 의사결정을 지원하는 종합 평가 모형인 'C-DAC 모델'임."}, {"num": 24, "badge": "진로상담", "kw": "제한 4단계 (크기/힘 ➔ 성역할 ➔ 사회적 지위 ➔ 내적 자아)", "q": "아동기~청소년기 진로 포부 영역 축소, 4단계 과정", "ans": "1단계 크기 및 힘 지향성 ➔ 2단계 성역할 지향성 ➔ 3단계 사회적 가치 지향성 ➔ 4단계 내적 고유한 자아 지향성의 4단계임."}];
    // Load custom items from local storage
    const customItems = JSON.parse(localStorage.getItem('kice_custom_items') || '[]');
    items = items.concat(customItems);

    
    
    function exportData() {
      const customItems = localStorage.getItem('kice_custom_items');
      if (!customItems) {
        alert('저장된 나만의 문제가 없습니다.');
        return;
      }
      const blob = new Blob([customItems], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'kice_custom_cards_backup.json';
      a.click();
      URL.revokeObjectURL(url);
    }
    
    function importData(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          if (Array.isArray(data)) {
            localStorage.setItem('kice_custom_items', JSON.stringify(data));
            alert('성공적으로 복원되었습니다! 페이지를 새로고침합니다.');
            location.reload();
          } else {
            alert('잘못된 파일 형식입니다.');
          }
        } catch (err) {
          alert('파일을 읽는 중 오류가 발생했습니다.');
        }
      };
      reader.readAsText(file);
    }

    function shuffleCards() {
      const highYield = ['장애', '평가', '가족', '진로', '이론', '치료', '검사', '척도', 'MMPI', 'DSM', '보웬', '미누친', '벡', '합리적', '자폐', '강박', '해리', '성격'];
      
      items.sort((a, b) => {
        let aScore = Math.random(); // Add base randomness
        let bScore = Math.random();
        highYield.forEach(k => { 
          if(a.q.includes(k) || a.kw.includes(k)) aScore += 5; 
        });
        highYield.forEach(k => { 
          if(b.q.includes(k) || b.kw.includes(k)) bScore += 5; 
        });
        return bScore - aScore;
      });
      
      currentIndex = 0;
      
      // PERSISTENT INDEX
      const lastKw = localStorage.getItem('kice_last_kw');
      if (lastKw) {
        const foundIdx = items.findIndex(item => item.kw === lastKw);
        if (foundIdx !== -1) currentIndex = foundIdx;
      }

      renderCard(currentIndex);
      initTable();
      alert('🔥 2027 임용고시 출제 1순위(A급 킬러) 예측 배열로 정렬되었습니다!');
    }

    function openAddCardModal() {
      document.getElementById('add-modal').style.display = 'flex';
    }
    
    function closeAddCardModal() {
      document.getElementById('add-modal').style.display = 'none';
    }

    function saveNewCard() {
      const badge = document.getElementById('new-badge').value.trim() || '추가문제';
      const kw = document.getElementById('new-kw').value.trim();
      const q = document.getElementById('new-q').value.trim();
      const ans = document.getElementById('new-ans').value.trim();
      
      if(!kw || !q) {
        alert('표제어와 문제 단서는 필수 입력입니다!');
        return;
      }
      
      const newItem = { badge, kw, q, ans };
      
      // Save to local storage
      const saved = JSON.parse(localStorage.getItem('kice_custom_items') || '[]');
      saved.push(newItem);
      localStorage.setItem('kice_custom_items', JSON.stringify(saved));
      
      // Update running memory
      items.push(newItem);
      
      // Clear form
      document.getElementById('new-badge').value = '';
      document.getElementById('new-kw').value = '';
      document.getElementById('new-q').value = '';
      document.getElementById('new-ans').value = '';
      
      closeAddCardModal();
      alert('문제가 성공적으로 추가되었습니다!');
      
      // Refresh UI
      totalPages = Math.ceil(items.length / itemsPerPage);
      initTable();
      renderCard(currentIndex);
    }

    
    // ANKI STATE
    let currentIndex = 0;
    let isFlipped = false;

    // TABLE STATE
    let tablePage = 0;
    const itemsPerPage = 4;
    let totalPages = Math.ceil(items.length / itemsPerPage);

    const elBadge = document.getElementById('c-badge');
    const elQ = document.getElementById('c-q');
    const elInput = document.getElementById('c-input');
    const elFlipBtn = document.getElementById('btn-flip');
    const elBack = document.getElementById('c-back');
    const elKw = document.getElementById('c-kw');
    const elAns = document.getElementById('c-ans');
    const elPFill = document.getElementById('p-fill');
    const elPText = document.getElementById('p-text');
    const modal = document.getElementById('reward-modal');

    // UI SWITCHER
    
    let isKwHidden = false;
    
    let isAnsHidden = false;
    function toggleTableAns() {
      isAnsHidden = !isAnsHidden;
      const tableBody = document.getElementById('table-body');
      const btn = document.getElementById('btn-toggle-ans');
      if (isAnsHidden) {
        tableBody.classList.add('hide-ans');
        btn.innerText = '👀 공식 정답 보이기';
        btn.style.background = '#facc15';
        btn.style.color = '#000';
      } else {
        tableBody.classList.remove('hide-ans');
        btn.innerText = '👀 공식 정답 가리기';
        btn.style.background = '#475569';
        btn.style.color = '#fff';
      }
    }

    function toggleTableKw() {
      isKwHidden = !isKwHidden;
      const tableBody = document.getElementById('table-body');
      const btn = document.getElementById('btn-toggle-kw');
      if (isKwHidden) {
        tableBody.classList.add('hide-kw');
        btn.innerText = '👀 영역 및 표제어 보이기';
        btn.style.background = '#facc15';
        btn.style.color = '#000';
      } else {
        tableBody.classList.remove('hide-kw');
        btn.innerText = '👀 영역 및 표제어 가리기';
        btn.style.background = '#475569';
        btn.style.color = '#fff';
      }
    }

    
    function startDictation() {
      if (window.hasOwnProperty('webkitSpeechRecognition') || window.hasOwnProperty('SpeechRecognition')) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.lang = 'ko-KR';
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.onstart = function() {
          document.getElementById('c-input').placeholder = '듣고 있습니다... 말씀해 주세요!';
        };
        recognition.onresult = function(e) {
          const t = e.results[0][0].transcript;
          const input = document.getElementById('c-input');
          input.value += (input.value ? ' ' : '') + t;
          input.placeholder = '실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요...';
        };
        recognition.onerror = function(e) { 
          alert('음성 인식 오류: ' + e.error); 
          document.getElementById('c-input').placeholder = '실제 임용고시 B4 답안지 양식입니다. 이곳에 타이핑하세요...';
        };
        recognition.start();
      } else {
        alert('이 브라우저에서는 음성 인식을 지원하지 않습니다. (최신 크롬/사파리 브라우저를 이용해주세요)');
      }
    }

    function switchMode(mode) {
      if(mode === 'anki') {
        document.getElementById('mode-anki').style.display = 'block';
        document.getElementById('mode-table').style.display = 'none';
        document.getElementById('btn-anki').classList.add('active');
        document.getElementById('btn-table').classList.remove('active');
      } else {
        document.getElementById('mode-anki').style.display = 'none';
        document.getElementById('mode-table').style.display = 'block';
        document.getElementById('btn-anki').classList.remove('active');
        document.getElementById('btn-table').classList.add('active');
      }
    }

    // ANKI LOGIC
    
    let originalItems = [];
    let isStarMode = false;
    
    // Call this at the end of window.onload or script execution
    
      // AUTO-FORMAT SENTENCE BREAKS
      items.forEach(item => {
        item.q = item.q.replace(/([가-힣](?:다|임|함|요)\.)\s+/g, '$1\n');
        item.ans = item.ans.replace(/([가-힣](?:다|임|함|요)\.)\s+/g, '$1\n');
      });

      setTimeout(() => { originalItems = [...items]; }, 500);

    function getStars() {
      return JSON.parse(localStorage.getItem('kice_stars') || '[]');
    }
    
    function toggleCurrentStar() {
      if (!items[currentIndex]) return;
      const kw = items[currentIndex].kw;
      let stars = getStars();
      if (stars.includes(kw)) {
        stars = stars.filter(k => k !== kw);
      } else {
        stars.push(kw);
      }
      localStorage.setItem('kice_stars', JSON.stringify(stars));
      updateStarUI();
    }
    
    function updateStarUI() {
      if (!items[currentIndex]) return;
      const kw = items[currentIndex].kw;
      const stars = getStars();
      const starEl = document.getElementById('c-star');
      if (starEl) {
        starEl.innerText = stars.includes(kw) ? '⭐' : '☆';
        starEl.style.transform = stars.includes(kw) ? 'scale(1.2)' : 'scale(1)';
      }
    }
    
    function toggleStarMode() {
      isStarMode = !isStarMode;
      const btn = document.getElementById('btn-starmode');
      if (isStarMode) {
        const stars = getStars();
        const starredItems = originalItems.filter(item => stars.includes(item.kw));
        if (starredItems.length === 0) {
          alert('별표(⭐) 표시된 문제가 없습니다! 어려운 문제에 별표를 먼저 눌러주세요.');
          isStarMode = false;
          return;
        }
        items = starredItems;
        btn.style.background = '#facc15';
        btn.style.color = '#000';
        btn.innerText = '⭐ 별표 모드 (ON)';
      } else {
        items = [...originalItems];
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '⭐ 별표 모드 (OFF)';
      }
      currentIndex = 0;
      renderCard(currentIndex);
      initTable();
    }

    
    function updateDashboard() {
      let srsData = JSON.parse(localStorage.getItem('kice_srs') || '{}');
      const now = new Date().getTime();
      let countNew = 0, countDue = 0, countDone = 0;
      items.forEach(item => {
        if (!srsData[item.kw]) countNew++;
        else if (srsData[item.kw] <= now) countDue++;
        else countDone++;
      });
      document.getElementById('stat-new').innerText = countNew;
      document.getElementById('stat-due').innerText = countDue;
      document.getElementById('stat-done').innerText = countDone;
      
      if (lastDueCount > 0 && countDue === 0 && countDone > 0) {
        fireConfetti();
      }
      lastDueCount = countDue;
    }

    
    function formatText(text) {
      if (!text) return '';
      let t = text.replace(/\*\*(.*?)\*\*/g, '<span style="color:#d97706; font-weight:bold;">$1</span>');
      // Replace LaTeX arrows safely
      t = t.split('$\Rightarrow$').join('➔');
      t = t.split('\Rightarrow').join('➔');
      t = t.split('$\rightarrow$').join('→');
      t = t.split('\rightarrow').join('→');
      t = t.split('$\Leftrightarrow$').join('↔');
      t = t.split('\Leftrightarrow').join('↔');
      return t;
    }

    
    // --- MEMORY UPGRADES LOGIC ---
    let isAutoTTS = false;
    let isClozeMode = false;
    
    function toggleAutoTTS() {
      isAutoTTS = !isAutoTTS;
      const btn = document.getElementById('btn-tts');
      if (isAutoTTS) {
        btn.style.background = '#8b5cf6';
        btn.style.color = '#fff';
        btn.innerText = '🔊 자동 낭독 (ON)';
        if (items[currentIndex]) speakTextClean(items[currentIndex].q);
      } else {
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '🔊 자동 낭독 (OFF)';
        window.speechSynthesis.cancel();
      }
    }
    
    function speakTextClean(text) {
      if (!text) return;
      // Remove symbols and markdown that shouldn't be read aloud
      let clean = text.replace(/\*\*/g, '').replace(/\$/g, '').replace(/\\Rightarrow/g, '다음으로').replace(/➔/g, '다음으로');
      speakText(clean);
    }
    
    function toggleClozeMode() {
      isClozeMode = !isClozeMode;
      const btn = document.getElementById('btn-cloze');
      if (isClozeMode) {
        btn.style.background = '#ec4899';
        btn.style.color = '#fff';
        btn.innerText = '🕳️ 빈칸 뚫기 (ON)';
      } else {
        btn.style.background = '#1e293b';
        btn.style.color = '#cbd5e1';
        btn.innerText = '🕳️ 빈칸 뚫기 (OFF)';
      }
      renderCard(currentIndex);
    }
    
    function generateCloze(text) {
      let words = text.split(' ');
      let candidates = [];
      for(let i=0; i<words.length; i++) {
        let w = words[i].replace(/[.,!?()]/g, '');
        // Pick words longer than 1 character that aren't typical sentence endings
        if(w.length >= 2 && !w.endsWith('임') && !w.endsWith('함')) {
          candidates.push(i);
        }
      }
      candidates.sort(() => 0.5 - Math.random());
      let selected = candidates.slice(0, Math.min(3, Math.max(1, Math.floor(candidates.length / 3))));
      
      let result = [];
      for(let i=0; i<words.length; i++) {
        if(selected.includes(i)) {
          result.push('[        ?        ]');
        } else {
          result.push(words[i]);
        }
      }
      return result.join(' ');
    }
    
    function getChosung(str) {
      const cho = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"];
      let result = "";
      for(let i=0; i<str.length; i++) {
        let code = str.charCodeAt(i) - 44032;
        if(code > -1 && code < 11172) {
          result += cho[Math.floor(code/588)];
        } else {
          result += str.charAt(i);
        }
      }
      return result;
    }
    
    function showChosungHint() {
      if(!items[currentIndex]) return;
      const hintBox = document.getElementById('hint-box');
      hintBox.style.display = 'block';
      hintBox.innerText = getChosung(items[currentIndex].ans);
    }
    // -----------------------------

    function renderCard(index) {
      const item = items[index];
      elBadge.innerHTML = formatText(item.badge);
      elQ.innerHTML = formatText(item.q);
      elKw.innerHTML = formatText(item.kw);
      elAns.innerHTML = formatText(item.ans);
        updateDashboard();
      localStorage.setItem('kice_last_kw', item.kw);
      
      elPText.innerText = index + 1;
      elPFill.style.width = ((index + 1) / items.length * 100) + '%';

      isFlipped = false;
      elBack.style.display = 'none';
      elFlipBtn.innerText = '💡 정답 확인하기 (뒤집기)';
      elFlipBtn.classList.remove('flipped');
      
        document.getElementById('hint-box').style.display = 'none';
        
        if (isAutoTTS) {
          setTimeout(() => speakTextClean(item.q), 300); // slight delay so it feels natural
        }
        
        if (isClozeMode) {
          elInput.value = generateCloze(item.ans);
        } else {
          elInput.value = '';
        }

      if(document.getElementById('kice-q-num')) {
        document.getElementById('kice-q-num').innerText = index + 1;
      }
    }

    function toggleFlip() {
      if(isFlipped) {
        elBack.style.display = 'none';
        elFlipBtn.innerText = '💡 정답 확인하기 (뒤집기)';
        elFlipBtn.classList.remove('flipped');
        isFlipped = false;
      } else {
        elBack.style.display = 'block';
        elFlipBtn.innerText = '숨기기';
        elFlipBtn.classList.add('flipped');
        isFlipped = true;
      }
    }

        function goNext() {
      if(currentIndex < items.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0; // loop to start
      }
      renderCard(currentIndex);
    }

    function goPrev() {
      if(currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = items.length - 1; // loop to end
      }
      renderCard(currentIndex);
    }

    // TABLE LOGIC
    function initTable() {
      const tbody = document.getElementById('table-body');
      let html = '';
      items.forEach((item, i) => {
        html += `<tr class="table-row" id="tr-${i}">
          <td class="td-num"><b>${i+1}</b></td>
          <td><span class="td-badge">[${item.badge}]</span><br><span class="td-kw">${item.kw}</span></td>
          <td class="td-q">${item.q}</td>
          <td class="td-ans">${item.ans}</td>
        </tr>`;
      });
      tbody.innerHTML = html;
      updateTablePagination();
    }

    function updateTablePagination() {
      for(let i=0; i<items.length; i++) {
        const tr = document.getElementById(`tr-${i}`);
        if(i >= tablePage * itemsPerPage && i < (tablePage + 1) * itemsPerPage) {
          tr.classList.add('active-page');
        } else {
          tr.classList.remove('active-page');
        }
      }
      document.getElementById('t-page').innerText = `페이지 ${tablePage + 1} / ${totalPages}`;
    }

    function goNextPage() {
      if(tablePage < totalPages - 1) {
        tablePage++;
        updateTablePagination();
        window.scrollTo(0, 0);
      }
    }

    function goPrevPage() {
      if(tablePage > 0) {
        tablePage--;
        updateTablePagination();
        window.scrollTo(0, 0);
      }
    }

    // REWARD LOGIC
    
    function handleSRS(level) {
      // Save interval data
      const now = new Date().getTime();
      let addMs = 0;
      if (level === 'again') addMs = 5 * 60 * 1000;
      if (level === 'hard') addMs = 1 * 24 * 60 * 60 * 1000;
      if (level === 'good') addMs = 5 * 24 * 60 * 60 * 1000;
      if (level === 'easy') addMs = 7 * 24 * 60 * 60 * 1000;
      
      let srsData = JSON.parse(localStorage.getItem('kice_srs') || '{}');
      if (items[currentIndex]) {
        srsData[items[currentIndex].kw] = now + addMs;
        localStorage.setItem('kice_srs', JSON.stringify(srsData));
      }
      
      // Trigger appropriate reward UI and audio
      if (level === 'again' || level === 'hard') {
        showRewardUI('wrong');
      } else {
        showRewardUI('right');
      }
      updateDashboard();
      localStorage.setItem('kice_last_kw', item.kw);
    }

    function showRewardUI(type) {
      const t = document.getElementById('reward-title');
      const m = document.getElementById('reward-msg');
      
      if(type === 'right') {
        const rewardImages = ['images/go1.png', 'images/go2.jpg', 'images/go3.png', 'images/go4.jpg', 'images/go5.jpg'];
        const randomImg = rewardImages[Math.floor(Math.random() * rewardImages.length)];
        document.getElementById('reward-img').src = randomImg;
        
        t.innerText = '🎉 완벽합니다! 최고예요!';
        speakText('화이팅!');
        m.innerHTML = '선생님의 노력은 절대 배신하지 않습니다!<br>이 기세로 2027 합격까지 화이팅! 💖';
        document.querySelector('.modal-content').style.borderColor = '#ec4899';
        
        // Fire confetti
        const duration = 2 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 1001 };
        function randomInRange(min, max) { return Math.random() * (max - min) + min; }
        const interval = setInterval(function() {
          const timeLeft = animationEnd - Date.now();
          if (timeLeft <= 0) { return clearInterval(interval); }
          const particleCount = 50 * (timeLeft / duration);
          confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
          confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
        }, 250);
      } else {
        document.getElementById('reward-img').src = 'images/cheer3.jpg';
        t.innerText = '🐕 괜찮아요! 토닥토닥';
        speakText('힘내세요!');
        m.innerHTML = '틀린 부분은 지금 확실히 잡으면 됩니다!<br>다시 한번 눈도장 찍고 다음으로 넘어가요! 🐾';
        document.querySelector('.modal-content').style.borderColor = '#38bdf8';
      }
      
      modal.style.display = 'flex';
    }

    function closeReward() {
      modal.style.display = 'none';
      goNext();
    }

    // INIT
    renderCard(currentIndex);
    initTable();
  
    // Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      // Modal handles
      if (document.getElementById('add-modal') && document.getElementById('add-modal').style.display === 'flex') return;
      if (document.getElementById('reward-modal') && document.getElementById('reward-modal').style.display === 'flex') {
        if (e.code === 'Space' || e.code === 'ArrowRight' || e.code === 'Enter') {
          e.preventDefault();
          closeReward();
        }
        return;
      }
      if (document.getElementById('mode-anki').style.display === 'none') return;

      const isTyping = ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName);
      
      // If typing, allow escape to unfocus, and allow Ctrl+Key combinations to bypass
      if (isTyping) {
        if (e.code === 'Escape') {
          document.activeElement.blur();
        }
        // If holding Ctrl, allow navigation even while typing
        if (e.ctrlKey) {
          if (e.code === 'Space' || e.code === 'Enter') {
            e.preventDefault();
            toggleFlip();
          } else if (e.code === 'ArrowRight') {
            e.preventDefault();
            goNext();
          } else if (e.code === 'ArrowLeft') {
            e.preventDefault();
            goPrev();
          }
        }
        return; // otherwise ignore normal arrows/space in textarea
      }
      
      // Normal non-typing shortcuts
      if (e.code === 'Space' || e.code === 'Enter') {
        e.preventDefault();
        toggleFlip();
      } else if (e.code === 'ArrowRight') {
        goNext();
      } else if (e.code === 'ArrowLeft') {
        goPrev();
      }
    });

