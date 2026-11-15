import re, os, subprocess

# 1. Load HTML
html_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Update CSS font-weights:
# ONLY 영역 및 핵심 표제어 is bold!
# td-q: normal (400)
# ans-box: normal (400)
# write-guide: normal (400)
# kw-badge: 800 (bold)
# kw-name: 900 (bold)

html = re.sub(r'\.td-q\s*\{[^}]*\}', '''.td-q {
      width: 34%;
      color: #111111;
      font-size: 0.77rem;
      font-weight: 400;
      line-height: 1.25;
    }''', html)

html = re.sub(r'\.ans-box\s*\{[^}]*\}', '''.ans-box {
      font-weight: 400;
      color: #111111;
      font-size: 0.78rem;
      line-height: 1.25;
    }''', html)

html = re.sub(r'\.write-guide\s*\{[^}]*\}', '''.write-guide {
      font-size: 0.64rem;
      color: #444444;
      font-weight: 400;
      display: block;
    }''', html)

html = re.sub(r'\.td-num\s*\{[^}]*\}', '''.td-num {
      text-align: center;
      font-weight: 600;
      color: #222222;
      width: 4.5%;
      font-size: 0.80rem;
    }''', html)

# 3. Clean full-name English in kw-name
kw_clean_map = {
    "스킬벡 학교중심 교육과정 개발 모형 (SBCD)": "스킬벡 학교중심 교육과정 개발 모형 (SBCD)",
    "영 교육과정 (Null Curriculum, 아이즈너)": "영 교육과정 (아이즈너)",
    "잠재적 교육과정 (Hidden Curriculum, 잭슨/드리븐)": "잠재적 교육과정 (잭슨·드리븐)",
    "중핵 교육과정 (Core Curriculum)": "중핵 교육과정",
    "메타인지적 지식 (Metacognitive Knowledge)": "메타인지적 지식 (초인지 지식)",
    "교육과정 압축 (Curriculum Compacting, 렌줄리)": "교육과정 압축 (렌줄리)",
    "일관성 (Consistency, 홀랜드 육각형 모델)": "일관성 (홀랜드 육각형)",
    "계측성 (Calculus)": "계측성 (홀랜드)",
    "변별성 (Differentiation)": "변별성 (홀랜드)",
    "정체성 (Identity)": "정체성 (홀랜드)",
    "일치성 (Congruence)": "일치성 (홀랜드)",
    "탐색기 (Exploration Stage)": "탐색기 (잠정기·전환기·실행기)",
    "C-DAC 모형 (진로발달 평가 및 상담 모델)": "C-DAC 모형 (진로발달 다차원 평가)",
    "진로장벽 (Career Barriers, 지각된 장벽)": "진로장벽 (스완슨 지각된 장벽)",
    "진로관심(Concern), 진로통제(Control), 진로호기심(Curiosity), 진로자신감(Confidence)": "생애적응도 4C (관심·통제·호기심·자신감)",
    "롤모델(영웅), 즐겨 보는 잡지나 TV 프로그램": "롤모델(존경하는 인물), 애호 TV 프로그램",
    "RCd (침체 척도, Demoralization)": "RCd (의기소침 척도)",
    "보편성 (Universality)": "보편성 (얄롬)",
    "이타주의 (Altruism)": "이타주의 (얄롬)",
    "차단하기 (Blocking)": "차단하기 (집단상담 기법)",
    "연결하기 (Linking)": "연결하기 (집단상담 기법)",
    "열린 영역 (Open Area, 개방 영역)": "개방 영역 (열린 창)",
    "눈먼 영역 (Blind Area, 맹목적 영역)": "맹검 영역 (눈먼 창)",
    "숨겨진 영역 (Hidden Area, 비밀 영역)": "은폐 영역 (숨겨진 창)",
    "나-아닌-나 (Not-me)": "나-아닌-나 (설리반 자아상)",
    "알파 압착 (Alpha Press), 베타 압착 (Beta Press)": "알파 압착, 베타 압착 (머레이)",
    "페르소나 (Persona)": "페르소나 (외적 인격)",
    "그림자 (Shadow)": "그림자 (원초적 본능)",
    "아니마 (Anima), 아니무스 (Animus)": "아니마, 아니무스 (내적 인격)",
    "자기 (Self)": "자기 (정신 전체의 중심)",
    "개성화 과정 (자기실현, Individuation)": "개성화 과정 (자기실현)",
    "직면 (Confrontation)": "직면 기법",
    "인지삼제 (Cognitive Triad, 부정적 인지 3요소)": "인지삼제 (자신·세상·미래)",
    "하향 화살표 기법 (Downward Arrow Technique)": "하향 화살표 기법 (벡 핵심신념)",
    "행동 실험 (Behavioral Experiment)": "행동 실험 (인지행동 기법)",
    "논리적 논박 (Logical Disputation)": "논리적 논박 (REBT)",
    "실증적 논박 (Empirical Disputation, 경험적 논박)": "실증적 논박 (경험적 논박)",
    "실용적 논박 (Pragmatic Disputation, 기능적 논박)": "실용적 논박 (기능적 논박)",
    "반전 (Retroflection)": "반전 (게슈탈트 접촉경계혼란)",
    "내사 (Introjection)": "내사 (게슈탈트 접촉경계혼란)",
    "융합 (Confluence)": "융합 (게슈탈트 접촉경계혼란)",
    "빈의자 기법 (Empty-Chair Technique)": "빈 의자 기법 (게슈탈트)",
    "역설적 의도 (Paradoxical Intention)": "역설적 의도 (프랑클)",
    "탈숙고 (Dereflection)": "탈숙고 (Dereflection)", # 고정 유지
    "자기분화 (Differentiation of Self)": "자기분화 (보웬)",
    "삼각관계 (Triangulation)": "삼각관계 (보웬)",
    "가족투사과정 (Family Projection Process)": "가족투사과정 (보웬)",
    "다세대 전수과정 (Multigenerational Transmission Process)": "다세대 전수 과정 (보웬)",
    "감정적 단절 (Emotional Cutoff)": "정서적 단절 (보웬)",
    "가계도 (Genogram)": "가계도 (3세대 가족도)",
    "나의 입장 기법 (I-position 기법)": "나-입장 취하기 기법 (I-position)",
    "탈삼각화 (Detriangulation)": "탈삼각화 (보웬)",
    "명확한 경계선 (Clear Boundary, 점선)": "명확한 경계선 (정상 가족)",
    "경직된 경계선 (Rigid Boundary, 실선, 유리가족)": "경직된 경계선 (격리·유리)",
    "산만한 경계선 (밀착된 경계선, Diffuse Boundary)": "밀착된 경계선 (모호·혼란 경계선)",
    "실연 (Enactment)": "실연 (구조적 가족치료)",
    "균형깨기 (Unbalancing)": "균형깨기 (구조적 가족치료)",
    "회유형 (Placating Type)": "회유형 (사티어 의사소통)",
    "강박장애 (OCD, Obsessive-Compulsive Disorder)": "강박장애 (OCD)",
    "강박성 성격장애 (OCPD)": "강박성 성격장애 (OCPD)",
    "자폐스펙트럼장애 (ASD)": "자폐스펙트럼장애 (ASD)",
    "신체증상장애 (Somatic Symptom Disorder)": "신체증상장애",
    "질병불안장애 (Illness Anxiety Disorder)": "질병불안장애",
    "공황장애 (Panic Disorder)": "공황장애 (공황발작)",
    "광장공포증 (Agoraphobia, 6개월 이상 지속)": "광장공포증 (공공장소 공포)",
    "파괴적 기분조절부전장애 (DMDD)": "파괴적 기분조절부전장애 (DMDD)",
    "주요우울장애 (Major Depressive Disorder)": "주요우울장애 (MDD)",
    "지속성 우울장애 (기분저하증, Dysthymia)": "지속성 우울장애 (기분부전장애)",
    "제1형 양극성 장애 (Bipolar I Disorder)": "제1형 양극성 장애 (조증 에피소드)",
    "제2형 양극성 장애 (Bipolar II Disorder)": "제2형 양극성 장애 (경조증 에피소드)",
    "반응성 애착장애 (RAD, Reactive Attachment Disorder)": "반응성 애착장애 (RAD)",
    "탈억제 사회관여 장애 (DSED)": "탈억제 사회관여 장애 (DSED)",
    "적대적 반항장애 (ODD)": "적대적 반항장애 (ODD)",
    "품행장애 (CD, Conduct Disorder)": "품행장애 (CD)",
    "외상후 스트레스 장애 (PTSD)": "외상후 스트레스 장애 (PTSD)",
    "급성 스트레스 장애 (ASD, Acute Stress Disorder)": "급성 스트레스 장애 (ASD)",
    "경계선 성격장애 (Borderline Personality Disorder)": "경계선 성격장애 (BPD)",
    "의존성 성격장애 (Dependent Personality Disorder)": "의존성 성격장애",
    "회피성 성격장애 (Avoidant Personality Disorder)": "회피성 성격장애",
    "조현성 성격장애 (분열성 성격장애, Schizoid)": "조현성 성격장애 (분열성 성격장애)",
    "조현형 성격장애 (분열형 성격장애, Schizotypal)": "조현형 성격장애 (분열형 성격장애)",
    "자기애성 성격장애 (Narcissistic Personality Disorder)": "자기애성 성격장애",
    "편집성 성격장애 (Paranoid Personality Disorder)": "편집성 성격장애",
    "반사회성 성격장애 (Antisocial Personality Disorder)": "반사회성 성격장애",
    "연극성 성격장애 (히스테리성 성격장애, Histrionic)": "연극성 성격장애 (히스테리성 성격장애)",
    "상반행동 차별강화 (DRI, Differential Reinforcement of Incompatible Behavior)": "상반행동 차별강화 (DRI)",
    "대체행동 차별강화 (DRA, Differential Reinforcement of Alternative Behavior)": "대체행동 차별강화 (DRA)",
    "타행동 차별강화 (DRO, Differential Reinforcement of Other Behavior, 무반응 차별강화)": "타행동 차별강화 (DRO, 무반응 차별강화)",
    "체계적 둔감법 (Systematic Desensitization, 월페)": "체계적 둔감법 (월페)",
    "홍수법 (Flooding)": "홍수법 (노출치료)",
    "A(감정 인정) ➔ C(제한 전달) ➔ T(대안 제시)": "ACT 모델 (감정 인정 ➔ 제한 전달 ➔ 대안 제시)",
    "S(구체성), L(치명도), A(접근성), P(근접성/친밀도)": "SLAP 모델 (구체성·치명도·접근성·근접성)",
    "CASE 모델 (Chronological Assessment of Suicide Events)": "CASE 모델 (숀 셰이, 연대기적 사건 평가)",
    "비난형 (Blaming Type)": "비난형 (사티어)",
    "초이성형 (Super-reasonable Type)": "초이성형 (사티어)",
    "산만형 (Irrelevant Type)": "산만형 (사티어)",
    "교사 역할 (Teacher Role)": "교사 역할 (버나드)",
    "상담자 역할 (Counselor Role)": "상담자 역할 (버나드)",
    "자문가 역할 (Consultant Role)": "자문가 역할 (버나드)",
    "다중관계 (이중관계, Multiple Relationships)": "다중관계 (이중관계)",
    "사전동의 (Informed Consent, 충분한 정보에 근거한 동의)": "사전동의 (충분한 정보에 근거한 동의)"
}

for old_kw, new_kw in kw_clean_map.items():
    html = html.replace(f'<div class="kw-name">{old_kw}</div>', f'<div class="kw-name">{new_kw}</div>')

# 4. Clean unnecessary English in Question prompts (td-q)
q_clean_pairs = [
    ("타일러(Tyler)가", "타일러가"),
    ("수퍼(Super)의", "수퍼의"),
    ("갓프레드슨(Gottfredson)의", "갓프레드슨의"),
    ("사비카스(Savickas)의", "사비카스의"),
    ("크롬볼츠(Krumboltz)의", "크롬볼츠의"),
    ("얄롬(Yalom)이", "얄롬이"),
    ("조하리의 창(Johari Window)", "조하리의 창"),
    ("설리반(Sullivan)의", "설리반의"),
    ("머레이(Murray)의", "머레이의"),
    ("융(Jung)의", "융의"),
    ("사티어(Satir)의", "사티어의"),
    ("랜드레스(Landreth)의", "랜드레스의"),
    ("버나드(Bernard)의", "버나드의"),
    ("비전형 반응(Faking bad)", "비전형 왜곡 반응"),
    ("정신증적 과장(Faking bad)", "정신증적 과장 왜곡"),
    ("좋은 모습(Faking good)", "긍정적 자기제시(좋은 모습)"),
    ("자아(Ego)를", "자아를"),
    ("자기(Self)를", "자기를"),
    ("자기(Self)'이다", "자기'이다")
]

for old_q, new_q in q_clean_pairs:
    html = html.replace(old_q, new_q)

# 5. Clean item 128 answer full names:
html = html.replace("계획의 구체성(Specificity), 수단의 치명도(Lethality), 도구에의 접근성(Availability), 인적 지지의 근접성(Proximity)", "구체성(S), 치명도(L), 접근성(A), 근접성(P)")

# Save updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated HTML successfully.")
