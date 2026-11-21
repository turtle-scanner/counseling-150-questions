import json, re, os

# 1. Load 2020-2026 extracted KICE past exam texts
PAST_TEXTS_PATH = r"C:\Users\LENOVO\.gemini\antigravity\brain\a1cd533c-23fa-4b50-8342-90a398cbc736\scratch\past_texts.json"
with open(PAST_TEXTS_PATH, encoding="utf-8") as f:
    past = json.load(f)

with open("kice_55_4lines_master.json", encoding="utf-8") as f:
    d55 = json.load(f)

# Precision search terms (avoiding overly generic 1-char words) for 2020-2026 KICE PDFs
SEARCH_TERMS = {
    1: ["백워드", "위긴스", "영속적 이해", "바라는 결과", "수락할 만한 증거"],
    2: ["스킬벡", "학교중심 교육과정", "상황분석", "SBCD"],
    3: ["타바", "귀납적", "교사 중심"],
    4: ["플립드", "거꾸로 수업", "역진행", "사전 학습"],
    5: ["인지적 도제", "콜린스", "모델링", "스캐폴딩", "비계"],
    6: ["ARCS", "켈러", "인지부하", "스웰러", "외재적"],
    7: ["역동적 평가", "비고츠키", "근접발달", "ZPD"],
    8: ["루브릭", "수행평가", "메이거", "분석적", "총체적"],
    9: ["세르지오바니", "도덕적 리더십", "도덕적 권위"],
    10: ["겟젤스", "구바", "사회체계", "규범적 차원", "개인적 차원"],
    11: ["강박장애", "강박성 성격", "노출 및 반응방지", "ERP", "강박사고"],
    12: ["공황장애", "공황발작", "광장공포", "클라크", "파국적"],
    13: ["신체증상장애", "질병불안장애", "신체증상"],
    14: ["사회적 의사소통", "실용적", "자폐스펙트럼", "자폐"],
    15: ["주의력결핍", "ADHD", "과잉행동", "복합형"],
    16: ["적대적 반항", "품행장애", "ODD", "반항장애"],
    17: ["반응성 애착", "탈억제 사회", "RAD", "DSED"],
    18: ["외상후 스트레스", "외상 후 스트레스", "PTSD", "급성 스트레스"],
    19: ["해리성 기억", "해리성 둔주", "해리성 정체성", "해리성"],
    20: ["경계선 성격", "의존성 성격", "변증법적", "DBT"],
    21: ["조현성 성격", "회피성 성격", "분열성 성격"],
    22: ["SUI", "자살", "비밀보장", "자살/죽음"],
    23: ["MMPI", "RCd", "RC1", "RC3", "EID", "THD", "BXD", "재구성임상"],
    24: ["로샤", "Rorschach", "경험균형", "D점수", "외향형"],
    25: ["웩슬러", "WISC", "WAIS", "GAI", "CPI", "TCI"],
    26: ["보웬", "삼각관계", "탈삼각", "자기분화", "다세대"],
    27: ["미누친", "구조적 가족", "경계선", "밀착", "유리", "실연"],
    28: ["사티어", "일치형", "회유형", "비난형", "초이성형", "가족조각"],
    29: ["헤일리", "전략적 가족", "역설적 지시", "밀란", "순환적 질문"],
    30: ["프랑클", "의미치료", "탈숙고", "역설적 의도"],
    31: ["아론 벡", "인지치료", "인지적 오류", "재앙화", "이분법", "자동적 사고"],
    32: ["엘리스", "REBT", "합리적 정서", "논박", "수치심 공격"],
    33: ["수용전념", "ACT", "탈융합", "심리적 유연성"],
    34: ["게슈탈트", "펄스", "반전", "내사", "융합", "빈의자", "접촉경계"],
    35: ["글래서", "현실치료", "전행동", "WDEP", "선택이론"],
    36: ["해결중심", "기적질문", "기적 질문", "예외질문", "척도질문", "대처질문"],
    37: ["설리반", "좋은-나", "나쁜-나", "병렬적", "대인관계 이론"],
    38: ["머레이", "욕구", "압착", "주제통각", "TAT"],
    39: ["칼 융", "페르소나", "그림자", "개성화", "아니마", "분석심리"],
    40: ["교류분석", "해리스", "생활자세", "이고그램", "어른 자아", "에릭 번"],
    41: ["랜드레스", "놀이치료", "제한설정", "과정 인정", "아동중심"],
    42: ["갓프레드슨", "제한-타협", "타협", "수퍼", "확립기", "진로발달"],
    43: ["홀랜드", "육각형", "변별도", "계측성", "사비카스", "진로적응", "생애설계"],
    44: ["다문화", "미세공격", "수퍼비전", "버나드", "조하리"],
    45: ["셰이", "CASE", "길리랜드", "위기개입", "안전계획", "학교폭력"],
    46: ["주요우울", "지속성 우울", "기분부전", "양극성", "조증"],
    47: ["식욕부진", "폭식증", "섭식장애"],
    48: ["분리불안", "선택적 함구", "함구증"],
    49: ["VRIN", "TRIN", "F-r", "L-r", "K-r", "HTP", "타당도 척도"],
    50: ["DEPI", "CDI", "Afr", "FC:CF", "정서 지표"],
    51: ["얄롬", "집단상담", "치료적 요인", "독점자", "집단 응집"],
    52: ["상담윤리", "이중관계", "사전동의", "키치너", "비밀보장"],
    53: ["로저스", "인간중심", "무조건적 긍정", "공감적 이해", "진솔성"],
    54: ["방어기제", "투사", "반동형성", "합리화", "승화", "코헛", "자기대상"],
    55: ["크롬볼츠", "계획된 우연", "마샤", "자아정체감"],
}

# Strategic KICE 2027 priority weights (based on 7-year cycle, AGENTS.md 0/1/2 priority, and 2025-2026 gap analysis)
# Higher base weight = stronger 2027 prediction
BASE_WEIGHT = {
    # 0순위 최유력 핵심 (매년/격년 필출 + 2027 순환 주기 정점)
    23: 99,  # MMPI-2-RF 상위차원·재구성임상척도 (7개년 전수 출제 100% 필출)
    22: 98,  # MMPI-2-RF SUI 자살위기 & 비밀보장 예외 (25·26 연속 + 필수 위기)
    11: 98,  # 강박장애(OCD) vs 강박성 성격장애(OCPD) & ERP (21·23 출제 ➔ 27 순환 정점)
    26: 97,  # 보웬 다세대 가족치료 삼각관계·탈삼각화·자기분화 (22·24 ➔ 27 순환 정점)
    31: 97,  # 아론 벡 인지치료 인지적 오류 & 하향 화살표 (4개년 최빈출)
    45: 97,  # 숀 셰이 CASE 모델 & 길리랜드 위기 6단계 & 학폭법 (위기개입 필출)
    1:  96,  # [교육학 0순위] 위긴스·맥타이 백워드 설계 3단계 (2027 교육과정 0순위)
    4:  96,  # [교육학 0순위] 플립드 러닝 3단계 (2027 교육방법 0순위)
    7:  96,  # [교육학 0순위] 비고츠키 ZPD 역동적 평가 (2027 교육평가 0순위)
    9:  96,  # [교육학 0순위] 세르지오바니 도덕적 리더십 (2027 교육행정 0순위)
    15: 95,  # ADHD 만 12세 기준 & 하위유형 (22·24 ➔ 27 순환 주기 적중)
    27: 95,  # 미누친 구조적 가족치료 경계선·실연화 (4개년 최빈출)
    43: 95,  # 홀랜드 계측성·변별도 & 사비카스 CSI·4C (5개년 최빈출 + 26 공백 ➔ 27 정점)
    52: 95,  # 상담윤리 이중관계·사전동의 & 키치너 5원칙 (5개년 최빈출)
    13: 94,  # 신체증상장애 vs 질병불안장애 (24 출제 ➔ 27 감별 1순위)
    14: 94,  # 사회적(실용적) 의사소통장애 vs 자폐스펙트럼장애 (23 출제 ➔ 27 감별 적중)
    34: 94,  # 펄스 게슈탈트 반전·접촉경계혼란·빈의자 (4개년 고빈출)
    25: 93,  # 웩슬러 GAI·CPI & TCI 검사 (5개년 최빈출)

    # 1순위 핵심 적중 (20문항)
    8:  92,  # [교육학 0순위] 다차원 수행평가 루브릭 & 메이거 목표
    10: 92,  # [교육학 0순위] 겟젤스-구바 사회체계 모형
    12: 92,  # 공황장애(클라크 파국적 오해석) & 광장공포증 (21 이후 장기 공백 ➔ 27 유력)
    16: 92,  # 적대적 반항장애(ODD) vs 품행장애(CD) (24·25·26 3년 연속 고빈출)
    20: 91,  # 경계선 vs 의존성 성격장애 & DBT
    28: 91,  # 사티어 의사소통 5유형 & 일치형·가족조각
    32: 91,  # 엘리스 REBT 3대 논박 & 수치심 공격 연습 (21 이후 장기 공백 ➔ 27 유력)
    42: 91,  # 갓프레드슨 제한-타협 & 수퍼 확립기 3단계
    44: 91,  # 수(Sue) 다문화 미세공격·버나드 수퍼비전·조하리의 창
    46: 90,  # 주요우울장애 vs 지속성 우울장애 & 양극성 I·II형
    51: 90,  # 얄롬 집단상담 11대 치료적 요인 & 집단 저항
    18: 90,  # 외상후 스트레스 장애(PTSD) vs 급성 스트레스 장애(ASD)
    29: 89,  # 헤일리 전략적 역설적 지시 & 밀란 순환적 질문
    30: 89,  # 프랑클 의미치료 탈숙고(Dereflection) & 역설적 의도
    33: 89,  # 수용전념치료(ACT) 인지적 탈융합 & 기꺼이 경험하기
    35: 88,  # 글래서 현실치료 전행동 & WDEP 자기평가
    38: 88,  # 머레이 욕구-압착(알파 vs 베타) & TAT
    39: 88,  # 융 페르소나 동일시 & 그림자 통합
    40: 87,  # 교류분석(TA) 해리스 4대 생활자세 & 이고그램
    54: 87,  # 정신분석 방어기제 & 코헛 자기심리학

    # 2순위 필출 감별 (17문항)
    2:  86,  # [교육학] 스킬벡 학교중심 교육과정(SBCD) & 상황분석
    5:  86,  # [교육학] 콜린스 인지적 도제 6단계 & 비계철회
    17: 85,  # 반응성 애착장애(RAD) vs 탈억제 사회관여 장애(DSED)
    19: 85,  # 해리성 기억상실(둔주) vs 해리성 정체성 장애
    24: 85,  # 로샤 경험균형(외향형) & D점수 스트레스 과부하
    36: 85,  # 해결중심 단기상담(SFBT) 4대 질문 기법
    49: 84,  # MMPI-2-RF 타당도 척도(VRIN-r·TRIN-r·F-r·L-r·K-r) & HTP
    55: 84,  # 크롬볼츠 계획된 우연 & 마샤 자아정체감 4유형
    3:  83,  # [교육학] 타바 교사 중심 귀납적 교육과정 개발 모형
    6:  83,  # [교육학] 켈러 ARCS 동기설계 & 스웰러 인지부하 이론
    37: 83,  # 설리반 3대 자아상 & 병렬적 왜곡
    41: 82,  # 랜드레스 아동중심 놀이치료 과정 인정 & ACT 제한설정
    47: 82,  # 신경성 식욕부진증 vs 신경성 폭식증
    50: 81,  # 로샤 정서 지표(FC:CF+C·Afr) & 특수지표(DEPI·CDI)
    53: 81,  # 로저스 인간중심상담 3대 핵심 조건
    21: 80,  # 조현성 성격장애 vs 회피성 성격장애
    48: 79,  # 분리불안장애 vs 선택적 함구증
}

def make_trend_note(item, years, score):
    is_ped = item["part"] == "PED10"
    if years:
        yr_str = ", ".join(f"{y}년" for y in years)
        cnt = len(years)
        if 2026 not in years and 2025 not in years:
            return f"📊 실제 기출({yr_str} · {cnt}회): 최근 2년간 미출제로 2027학년도 순환 주기 재출제 확률이 매우 높습니다."
        elif cnt >= 4:
            return f"📊 실제 기출({yr_str} · {cnt}회): 7개년 최빈출 부동의 핵심 영역으로 2027학년도 복합형 문항 출제가 확실시됩니다."
        elif 2026 in years or 2025 in years:
            return f"📊 실제 기출({yr_str} · {cnt}회): 최근 평가원 핵심 출제 트렌드 영역으로 감별·응용 변형 출제 대비가 필수입니다."
        else:
            return f"📊 실제 기출({yr_str} · {cnt}회): 평가원 정식 기출 이력이 확인된 고빈출 핵심 주제입니다."
    else:
        if is_ped:
            return "📊 2027 교육학 0~1순위 적중 예측: 최근 6개년 미출제 공백기이자 2022 개정 교육과정 핵심 정책과 직결된 최유력 테마입니다."
        else:
            return "📊 2027 전공상담 1~2순위 적중 예측: 최근 기출 공백기로 2027학년도 DSM-5-TR 감별 및 최신 상담기법 복합형 출제 유력 주제입니다."

enriched = []
for item in d55:
    tid = item["id"]
    is_ped = item["part"] == "PED10"
    corpus = past["ped"] if is_ped else past["csl"]
    terms = SEARCH_TERMS.get(tid, [])
    years = []
    for yr_str, txt in sorted(corpus.items()):
        if any(t in txt for t in terms):
            years.append(int(yr_str))
    prob = BASE_WEIGHT.get(tid, 80)
    if prob >= 93:
        tier = "0순위"
        tier_label = "🔥 0순위 최유력"
    elif prob >= 87:
        tier = "1순위"
        tier_label = "⭐ 1순위 핵심적중"
    else:
        tier = "2순위"
        tier_label = "📌 2순위 필출감별"

    enriched.append({
        "id": tid,
        "part": "교육학" if is_ped else "전공상담",
        "domain": item["domain"].replace(" ★0순위", ""),
        "title": item["title"],
        "concept": item.get("concept", ""),
        "prob": prob,
        "tier": tier,
        "tier_label": tier_label,
        "past_years": years,
        "trend_note": make_trend_note(item, years, prob),
        "passage": item.get("problem_passage", ""),
        "asks": item.get("problem_asks", []),
        "keywords": item.get("keywords", []),
        "answer_lines": item.get("lines", []),
        "lecture_summary": item.get("lecture_summary", ""),
        "lecture_point": item.get("lecture_point", ""),
    })

# Sort by probability descending, then past_years count descending, then id
enriched.sort(key=lambda x: (-x["prob"], -len(x["past_years"]), x["id"]))
for idx, x in enumerate(enriched, 1):
    x["rank"] = idx

print(f"Total enriched: {len(enriched)}")
print("Top 10:", [(x["rank"], x["prob"], x["tier"], x["past_years"], x["title"][:24]) for x in enriched[:10]])

# 2. Extract 1st period Pedagogy Essay from 2027_1128_교육학_0순위_시험지_및_논술답안지.html
with open("2027_1128_교육학_0순위_시험지_및_논술답안지.html", encoding="utf-8") as f:
    ped_html = f.read()

# Extract passage paragraphs and rubric cols and model essay
m_pass = re.search(r'<div class="passage-box">(.*?)</div>', ped_html, re.S)
ped_passage_html = m_pass.group(1).strip() if m_pass else ""

m_rub = re.search(r'<div class="rubric-grid">(.*?)</div>\s*</div>', ped_html, re.S)
ped_rubric_html = m_rub.group(1).strip() if m_rub else ""

# Find second section (model essay)
secs = re.findall(r'<section class="paper-sheet">(.*?)</section>', ped_html, re.S)
ped_answer_html = secs[1].strip() if len(secs) > 1 else ""
# Clean toolbar/header inside ped_answer_html to keep essay paragraphs nicely
m_essay_body = re.search(r'(<div class="essay-box".*)', ped_answer_html, re.S)
if not m_essay_body:
    # fallback: extract all <div class="essay-... or <p> after kice-top-bar
    m_after = re.search(r'</div>\s*(<div.*)', ped_answer_html, re.S)
    ped_answer_clean = m_after.group(1) if m_after else ped_answer_html
else:
    ped_answer_clean = m_essay_body.group(1)

print("Pedagogy extracted:", len(ped_passage_html), len(ped_rubric_html), len(ped_answer_clean))

# 3. Extract EXAM_A and EXAM_B JS arrays from exam_ab_2027.html (original backup)
with open("exam_ab_2027.html", encoding="utf-8") as f:
    ab_html = f.read()

ma = re.search(r'const EXAM_A\s*=\s*(\[.*?\]);', ab_html, re.S)
mb = re.search(r'const EXAM_B\s*=\s*(\[.*?\]);', ab_html, re.S)
exam_a_js = ma.group(1) if ma else "[]"
exam_b_js = mb.group(1) if mb else "[]"
print("EXAM_A len:", len(exam_a_js), "EXAM_B len:", len(exam_b_js))

# 4. Build mobile-first index.html
TOP55_JSON = json.dumps(enriched, ensure_ascii=False)
PED_DATA_JSON = json.dumps({
    "passageHtml": ped_passage_html,
    "rubricHtml": ped_rubric_html,
    "answerHtml": ped_answer_clean
}, ensure_ascii=False)

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<meta name="theme-color" content="#0f172a">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>2027 임용(11.28) 출제확률순 모바일 합격 마스터</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0b1120;
    --surface: #111c33;
    --surface-2: #1a2744;
    --border: #2a3b5e;
    --text: #f1f5f9;
    --text-muted: #94a3b8;
    --accent: #38bdf8;
    --accent-2: #818cf8;
    --gold: #fbbf24;
    --danger: #f43f5e;
    --success: #10b981;
    --kw-bg: rgba(251, 191, 36, 0.22);
    --kw-text: #fde047;
    --pass-bg: #0f172a;
    --ans-bg: #06281e;
    --ans-border: #10b981;
    --exp-bg: #172038;
    --exp-border: #6366f1;
    --font-scale: 1;
  }
  [data-theme="light"] {
    --bg: #f1f5f9;
    --surface: #ffffff;
    --surface-2: #f8fafc;
    --border: #cbd5e1;
    --text: #0f172a;
    --text-muted: #475569;
    --accent: #0284c7;
    --accent-2: #4f46e5;
    --gold: #b45309;
    --danger: #e11d48;
    --success: #059669;
    --kw-bg: #fef08a;
    --kw-text: #854d0e;
    --pass-bg: #f8fafc;
    --ans-bg: #ecfdf5;
    --ans-border: #10b981;
    --exp-bg: #eef2ff;
    --exp-border: #6366f1;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
  html, body {
    font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.65;
    font-size: calc(15px * var(--font-scale));
    overflow-x: hidden;
  }
  body { padding-bottom: 84px; }

  /* Sticky Top Header */
  .top-header {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(11, 17, 32, 0.94);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 10px 14px 8px;
  }
  [data-theme="light"] .top-header {
    background: rgba(255, 255, 255, 0.95);
  }
  .header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    max-width: 820px;
    margin: 0 auto;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 7px;
    min-width: 0;
  }
  .dday-badge {
    background: linear-gradient(135deg, #f43f5e, #e11d48);
    color: #fff;
    font-weight: 900;
    font-size: 0.78rem;
    padding: 3px 8px;
    border-radius: 999px;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(244,63,94,0.35);
  }
  .brand-title {
    font-weight: 900;
    font-size: 0.96rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .header-tools {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-shrink: 0;
  }
  .icon-btn {
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 5px 8px;
    font-size: 0.78rem;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .icon-btn:active { transform: scale(0.95); }

  /* Progress strip */
  .prog-wrap {
    max-width: 820px;
    margin: 7px auto 0;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.76rem;
    color: var(--text-muted);
  }
  .prog-bar {
    flex: 1;
    height: 6px;
    background: var(--surface-2);
    border-radius: 999px;
    overflow: hidden;
  }
  .prog-fill {
    height: 100%;
    background: linear-gradient(90deg, #10b981, #38bdf8);
    width: 0%;
    transition: width 0.25s ease;
  }

  /* Main Mode Tabs */
  .main-tabs {
    max-width: 820px;
    margin: 10px auto 0;
    padding: 0 12px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .main-tab {
    background: var(--surface);
    color: var(--text-muted);
    border: 1.5px solid var(--border);
    border-radius: 12px;
    padding: 10px 8px;
    font-weight: 800;
    font-size: 0.88rem;
    cursor: pointer;
    text-align: center;
    transition: all 0.15s;
  }
  .main-tab.active {
    background: linear-gradient(135deg, #0284c7, #4f46e5);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 14px rgba(56, 189, 248, 0.28);
  }

  /* Controls & Filters */
  .container {
    max-width: 820px;
    margin: 0 auto;
    padding: 10px 12px 24px;
  }
  .filter-scroll {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding: 4px 0 8px;
    scrollbar-width: none;
  }
  .filter-scroll::-webkit-scrollbar { display: none; }
  .chip {
    background: var(--surface);
    color: var(--text-muted);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 6px 12px;
    font-size: 0.8rem;
    font-weight: 700;
    white-space: nowrap;
    cursor: pointer;
  }
  .chip.active {
    background: var(--accent);
    color: #082f49;
    border-color: var(--accent);
  }
  .search-row {
    display: flex;
    gap: 6px;
    margin-bottom: 10px;
  }
  .search-input {
    flex: 1;
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 9px 12px;
    font-size: 0.88rem;
    outline: none;
  }
  .search-input:focus { border-color: var(--accent); }
  .view-toggle {
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0 11px;
    font-size: 0.8rem;
    font-weight: 700;
    cursor: pointer;
    white-space: nowrap;
  }

  /* Question Jump Bar in Card Mode */
  .jump-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 7px 12px;
    margin-bottom: 10px;
    font-size: 0.82rem;
    font-weight: 700;
  }
  .jump-select {
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px 8px;
    font-size: 0.8rem;
    max-width: 65%;
  }

  /* Study Card */
  .card {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: 15px 14px;
    margin-bottom: 14px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.18);
  }
  .card-meta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    margin-bottom: 8px;
  }
  .rank-badge {
    background: var(--gold);
    color: #451a03;
    font-weight: 900;
    font-size: 0.78rem;
    padding: 2px 8px;
    border-radius: 6px;
  }
  [data-theme="light"] .rank-badge { background: #fde047; color: #713f12; }
  .tier-badge {
    font-weight: 800;
    font-size: 0.76rem;
    padding: 2px 8px;
    border-radius: 6px;
  }
  .tier-0 { background: rgba(244,63,94,0.2); color: #fb7185; border: 1px solid rgba(244,63,94,0.4); }
  .tier-1 { background: rgba(251,191,36,0.18); color: #fbbf24; border: 1px solid rgba(251,191,36,0.4); }
  .tier-2 { background: rgba(56,189,248,0.18); color: #38bdf8; border: 1px solid rgba(56,189,248,0.4); }
  [data-theme="light"] .tier-0 { background: #ffe4e6; color: #be123c; }
  [data-theme="light"] .tier-1 { background: #fef3c7; color: #b45309; }
  [data-theme="light"] .tier-2 { background: #e0f2fe; color: #0369a1; }

  .domain-tag {
    background: var(--surface-2);
    color: var(--text-muted);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    border: 1px solid var(--border);
  }
  .years-tag {
    font-size: 0.73rem;
    font-weight: 700;
    color: var(--accent);
    background: rgba(56,189,248,0.1);
    padding: 2px 7px;
    border-radius: 6px;
  }
  .card-title {
    font-size: 1.04rem;
    font-weight: 900;
    line-height: 1.45;
    margin-bottom: 10px;
    color: var(--text);
  }

  /* Step Boxes: 1. Problem -> 2. Answer -> 3. Explanation */
  .step-label {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 0.78rem;
    font-weight: 900;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }
  .problem-box {
    background: var(--pass-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 13px 13px;
    margin-bottom: 11px;
  }
  .passage-text {
    font-size: 0.94rem;
    line-height: 1.75;
    white-space: pre-line;
    margin-bottom: 11px;
  }
  .asks-box {
    background: var(--surface);
    border-left: 3.5px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 9px 11px;
  }
  .asks-title {
    font-size: 0.8rem;
    font-weight: 900;
    color: var(--accent);
    margin-bottom: 5px;
  }
  .asks-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 0.89rem;
    font-weight: 600;
  }

  /* Toggle Buttons for Answer & Explanation */
  .step-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 10px;
  }
  .reveal-btn {
    padding: 11px 10px;
    border-radius: 11px;
    border: 1.5px solid var(--border);
    background: var(--surface-2);
    color: var(--text);
    font-weight: 800;
    font-size: 0.88rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    transition: all 0.15s;
  }
  .reveal-btn.ans-open {
    background: var(--success);
    color: #022c22;
    border-color: var(--success);
  }
  .reveal-btn.exp-open {
    background: var(--accent-2);
    color: #fff;
    border-color: var(--accent-2);
  }

  /* Answer Panel */
  .answer-panel {
    display: none;
    background: var(--ans-bg);
    border: 1.5px solid var(--ans-border);
    border-radius: 12px;
    padding: 13px;
    margin-bottom: 10px;
    animation: fadeIn 0.18s ease;
  }
  .answer-panel.open { display: block; }
  .kw-row {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-bottom: 10px;
  }
  .kw-chip {
    background: var(--kw-bg);
    color: var(--kw-text);
    font-size: 0.78rem;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 6px;
  }
  .ans-lines {
    display: flex;
    flex-direction: column;
    gap: 7px;
  }
  .ans-line {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 0.92rem;
    font-weight: 600;
    line-height: 1.6;
    display: flex;
    gap: 8px;
  }
  [data-theme="light"] .ans-line { background: rgba(255,255,255,0.85); }
  .line-num {
    color: var(--success);
    font-weight: 900;
    flex-shrink: 0;
  }
  .hl {
    background: var(--kw-bg);
    color: var(--kw-text);
    padding: 0 3px;
    border-radius: 4px;
    font-weight: 800;
  }

  /* Explanation Panel */
  .exp-panel {
    display: none;
    background: var(--exp-bg);
    border: 1.5px solid var(--exp-border);
    border-radius: 12px;
    padding: 13px;
    margin-bottom: 10px;
    animation: fadeIn 0.18s ease;
  }
  .exp-panel.open { display: block; }
  .trend-box {
    background: rgba(56,189,248,0.12);
    border-left: 3px solid var(--accent);
    padding: 8px 10px;
    border-radius: 0 8px 8px 0;
    font-size: 0.84rem;
    font-weight: 700;
    margin-bottom: 10px;
  }
  .formula-box {
    background: rgba(251,191,36,0.14);
    border: 1px dashed var(--gold);
    border-radius: 9px;
    padding: 9px 11px;
    font-size: 0.88rem;
    font-weight: 800;
    color: var(--gold);
    margin-bottom: 10px;
    line-height: 1.55;
  }
  [data-theme="light"] .formula-box { background: #fefce8; color: #92400e; }
  .exp-text {
    font-size: 0.9rem;
    line-height: 1.72;
    color: var(--text);
  }

  /* Card Footer Check Buttons */
  .card-foot {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
  }
  .status-btn {
    flex: 1;
    padding: 8px;
    border-radius: 9px;
    border: 1px solid var(--border);
    background: var(--surface-2);
    color: var(--text-muted);
    font-weight: 700;
    font-size: 0.82rem;
    cursor: pointer;
  }
  .status-btn.marked { background: rgba(251,191,36,0.2); color: var(--gold); border-color: var(--gold); }
  .status-btn.done { background: rgba(16,185,129,0.2); color: var(--success); border-color: var(--success); }

  /* Full Exam Subtabs */
  .sub-tabs {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin-bottom: 12px;
  }
  .sub-tab {
    background: var(--surface);
    color: var(--text-muted);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 9px 4px;
    font-size: 0.8rem;
    font-weight: 800;
    cursor: pointer;
    text-align: center;
  }
  .sub-tab.active {
    background: var(--accent);
    color: #082f49;
    border-color: var(--accent);
  }

  /* Pedagogy HTML styling inside dark/light theme */
  .ped-prose p { margin-bottom: 10px; font-size: 0.92rem; line-height: 1.75; }
  .ped-rubric { display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 8px; }
  @media (min-width: 640px) { .ped-rubric { grid-template-columns: 1fr 1fr; } }
  .ped-rubric .rubric-col {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px;
  }
  .ped-rubric h4 { font-size: 0.88rem; color: var(--accent); margin-bottom: 5px; }
  .ped-rubric ul { padding-left: 16px; font-size: 0.84rem; }
  .ped-rubric li { margin-bottom: 3px; }
  .ped-ans-content { font-size: 0.9rem; line-height: 1.75; }
  .ped-ans-content .essay-sec, .ped-ans-content p { margin-bottom: 10px; }
  .ped-ans-content .kw, .ped-ans-content strong { color: var(--kw-text); }

  /* Fixed Bottom Thumb Bar (Mobile) */
  .bottom-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 60;
    background: rgba(15, 23, 42, 0.96);
    backdrop-filter: blur(12px);
    border-top: 1px solid var(--border);
    padding: 8px 10px calc(8px + env(safe-area-inset-bottom));
  }
  [data-theme="light"] .bottom-bar { background: rgba(255, 255, 255, 0.97); }
  .bottom-inner {
    max-width: 820px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1.1fr 1fr 1fr 0.9fr 1.1fr;
    gap: 6px;
  }
  .b-btn {
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 4px;
    font-size: 0.8rem;
    font-weight: 800;
    cursor: pointer;
    text-align: center;
  }
  .b-btn.primary { background: var(--accent); color: #082f49; border-color: var(--accent); }
  .b-btn:active { transform: scale(0.95); }

  .empty-state {
    text-align: center;
    padding: 40px 16px;
    color: var(--text-muted);
    font-weight: 700;
  }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
</style>
</head>
<body>

<header class="top-header">
  <div class="header-row">
    <div class="brand">
      <span class="dday-badge" id="ddayBadge">D-7</span>
      <span class="brand-title">2027 임용 출제확률순 마스터</span>
    </div>
    <div class="header-tools">
      <button class="icon-btn" onclick="changeFont(-0.08)" title="글씨 작게">가-</button>
      <button class="icon-btn" onclick="changeFont(0.08)" title="글씨 크게">가+</button>
      <button class="icon-btn" id="themeBtn" onclick="toggleTheme()" title="테마 전환">☀️</button>
      <a class="icon-btn" href="exam_ab_2027.html" title="B4 인쇄 시험지">🖨️</a>
    </div>
  </div>
  <div class="prog-wrap">
    <span id="progText">암기완료 0 / 55 (0%)</span>
    <div class="prog-bar"><div class="prog-fill" id="progFill"></div></div>
  </div>
</header>

<nav class="main-tabs">
  <button class="main-tab active" id="tabTop55" onclick="switchMode('top55')">🔥 출제확률 TOP 55</button>
  <button class="main-tab" id="tabExam" onclick="switchMode('exam')">📝 3교시 실전 풀세트</button>
</nav>

<main class="container">
  <!-- MODE 1: TOP 55 BY PROBABILITY -->
  <section id="secTop55">
    <div class="filter-scroll" id="filterBar">
      <button class="chip active" data-f="all" onclick="setFilter('all')">전체 (55)</button>
      <button class="chip" data-f="0순위" onclick="setFilter('0순위')">🔥 0순위 최유력 (18)</button>
      <button class="chip" data-f="1순위" onclick="setFilter('1순위')">⭐ 1순위 핵심 (20)</button>
      <button class="chip" data-f="2순위" onclick="setFilter('2순위')">📌 2순위 필출 (17)</button>
      <button class="chip" data-f="교육학" onclick="setFilter('교육학')">📘 1교시 교육학 (10)</button>
      <button class="chip" data-f="전공상담" onclick="setFilter('전공상담')">📗 2·3교시 전공 (45)</button>
      <button class="chip" data-f="bookmark" onclick="setFilter('bookmark')">🔖 북마크</button>
      <button class="chip" data-f="undone" onclick="setFilter('undone')">⬜ 미암기</button>
    </div>

    <div class="search-row">
      <input type="search" id="searchInput" class="search-input" placeholder="키워드·이론·영역 검색 (예: 강박, MMPI, 보웬, 백워드)" oninput="onSearch()">
      <button class="view-toggle" id="viewToggleBtn" onclick="toggleViewMode()">📋 리스트</button>
    </div>

    <div class="jump-bar" id="jumpBar">
      <span id="posLabel">1 / 55</span>
      <select class="jump-select" id="jumpSelect" onchange="jumpTo(this.value)"></select>
    </div>

    <div id="top55Container"></div>
  </section>

  <!-- MODE 2: 3-PERIOD FULL EXAM (1교시 교육학 -> 2교시 전공A -> 3교시 전공B) -->
  <section id="secExam" style="display:none;">
    <div class="sub-tabs">
      <button class="sub-tab active" id="subPed" onclick="switchExamPart('ped')">1교시 교육학<br><small>논술 (16발문)</small></button>
      <button class="sub-tab" id="subA" onclick="switchExamPart('A')">2교시 전공 A<br><small>12문항·초장문</small></button>
      <button class="sub-tab" id="subB" onclick="switchExamPart('B')">3교시 전공 B<br><small>11문항·초장문</small></button>
    </div>
    <div id="examContainer"></div>
  </section>
</main>

<!-- Bottom Thumb Bar (Card Mode) -->
<div class="bottom-bar" id="bottomBar">
  <div class="bottom-inner">
    <button class="b-btn" onclick="moveCard(-1)">◀ 이전</button>
    <button class="b-btn" onclick="toggleCurrentPanel('ans')">✅ 정답</button>
    <button class="b-btn" onclick="toggleCurrentPanel('exp')">💡 해설</button>
    <button class="b-btn" id="bMarkBtn" onclick="toggleCurrentMark()">🔖</button>
    <button class="b-btn primary" onclick="moveCard(1)">다음 ▶</button>
  </div>
</div>

<script>
const TOP55 = __TOP55_JSON__;
const PED_EXAM = __PED_DATA_JSON__;
const EXAM_A = __EXAM_A_JS__;
const EXAM_B = __EXAM_B_JS__;

const STORE_KEY = 'kice_2027_mobile_v1';
let state = {
  mode: 'top55',
  examPart: 'ped',
  filter: 'all',
  search: '',
  viewMode: 'card', // 'card' | 'list'
  cardIdx: 0,
  done: {},
  bookmark: {},
  theme: 'dark',
  fontScale: 1
};

try {
  const saved = JSON.parse(localStorage.getItem(STORE_KEY) || '{}');
  state = { ...state, ...saved };
} catch(e) {}

function saveState() {
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify({
      done: state.done,
      bookmark: state.bookmark,
      theme: state.theme,
      fontScale: state.fontScale,
      cardIdx: state.cardIdx,
      viewMode: state.viewMode
    }));
  } catch(e) {}
}

// D-Day calculation (Exam: 2026-11-28)
function updateDDay() {
  const today = new Date();
  const exam = new Date(2026, 10, 28); // Nov 28, 2026
  const diff = Math.ceil((exam - new Date(today.getFullYear(), today.getMonth(), today.getDate())) / 86400000);
  const el = document.getElementById('ddayBadge');
  if (diff > 0) el.textContent = `11.28 D-${diff}`;
  else if (diff === 0) el.textContent = `11.28 D-DAY 🔥`;
  else el.textContent = `2027 임용`;
}

function applyPrefs() {
  document.documentElement.setAttribute('data-theme', state.theme);
  document.documentElement.style.setProperty('--font-scale', state.fontScale);
  document.getElementById('themeBtn').textContent = state.theme === 'dark' ? '☀️' : '🌙';
  document.getElementById('viewToggleBtn').textContent = state.viewMode === 'card' ? '📋 전체보기' : '📱 1문제씩';
}

function toggleTheme() {
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  applyPrefs();
  saveState();
}

function changeFont(delta) {
  state.fontScale = Math.min(1.32, Math.max(0.84, +(state.fontScale + delta).toFixed(2)));
  applyPrefs();
  saveState();
}

function updateProgress() {
  const doneCount = Object.values(state.done).filter(Boolean).length;
  const pct = Math.round((doneCount / TOP55.length) * 100);
  document.getElementById('progText').textContent = `암기완료 ${doneCount} / ${TOP55.length} (${pct}%)`;
  document.getElementById('progFill').style.width = pct + '%';
}

function escHtml(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function highlightKws(text, kws) {
  let out = escHtml(text);
  if (!kws || !kws.length) return out;
  const sorted = [...kws].filter(Boolean).sort((a,b) => b.length - a.length);
  for (const kw of sorted) {
    const safe = escHtml(kw).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    out = out.replace(new RegExp(safe, 'g'), `<span class="hl">${escHtml(kw)}</span>`);
  }
  return out;
}

function getFilteredList() {
  const q = state.search.trim().toLowerCase();
  return TOP55.filter(item => {
    if (state.filter === '0순위' && item.tier !== '0순위') return false;
    if (state.filter === '1순위' && item.tier !== '1순위') return false;
    if (state.filter === '2순위' && item.tier !== '2순위') return false;
    if (state.filter === '교육학' && item.part !== '교육학') return false;
    if (state.filter === '전공상담' && item.part !== '전공상담') return false;
    if (state.filter === 'bookmark' && !state.bookmark[item.id]) return false;
    if (state.filter === 'undone' && state.done[item.id]) return false;
    if (q) {
      const hay = (item.title + ' ' + item.domain + ' ' + item.concept + ' ' + (item.keywords||[]).join(' ') + ' ' + item.passage).toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });
}

function renderCardHtml(item) {
  const tierClass = item.tier === '0순위' ? 'tier-0' : (item.tier === '1순위' ? 'tier-1' : 'tier-2');
  const yrBadge = item.past_years && item.past_years.length
    ? `<span class="years-tag">기출 ${item.past_years.map(y => "'" + String(y).slice(2)).join('·')}</span>`
    : `<span class="years-tag">2027 신규·공백 적중</span>`;
  const asksHtml = (item.asks || []).map(a => `<li>${escHtml(a)}</li>`).join('');
  const kwsHtml = (item.keywords || []).map(k => `<span class="kw-chip"># ${escHtml(k)}</span>`).join('');
  const linesHtml = (item.answer_lines || []).map((ln, i) => `
    <div class="ans-line">
      <span class="line-num">${i+1}줄</span>
      <span>${highlightKws(ln, item.keywords)}</span>
    </div>
  `).join('');
  const isMark = !!state.bookmark[item.id];
  const isDone = !!state.done[item.id];

  return `
    <article class="card" id="card-${item.id}">
      <div class="card-meta">
        <span class="rank-badge">#${item.rank}위</span>
        <span class="tier-badge ${tierClass}">${item.tier_label} · ${item.prob}%</span>
        <span class="domain-tag">${escHtml(item.part)} · ${escHtml(item.domain)}</span>
        ${yrBadge}
      </div>
      <h2 class="card-title">${escHtml(item.title)}</h2>

      <!-- STEP 1: PROBLEM -->
      <div class="problem-box">
        <div class="step-label" style="color:var(--accent);">📄 STEP 1. 실전 문제</div>
        <div class="passage-text">${escHtml(item.passage)}</div>
        <div class="asks-box">
          <div class="asks-title">&lt;작성 방법&gt;</div>
          <ul class="asks-list">${asksHtml}</ul>
        </div>
      </div>

      <!-- TOGGLE BUTTONS -->
      <div class="step-actions">
        <button class="reveal-btn" id="btn-ans-${item.id}" onclick="togglePanel(${item.id}, 'ans')">✅ STEP 2. 정답 보기</button>
        <button class="reveal-btn" id="btn-exp-${item.id}" onclick="togglePanel(${item.id}, 'exp')">💡 STEP 3. 해설 보기</button>
      </div>

      <!-- STEP 2: ANSWER -->
      <div class="answer-panel" id="panel-ans-${item.id}">
        <div class="step-label" style="color:var(--success);">✅ KICE 만점 정답 (B4 1줄 38~45자 규격)</div>
        <div class="kw-row">${kwsHtml}</div>
        <div class="ans-lines">${linesHtml}</div>
      </div>

      <!-- STEP 3: EXPLANATION -->
      <div class="exp-panel" id="panel-exp-${item.id}">
        <div class="step-label" style="color:var(--accent-2);">💡 기출 적중 근거 & 핵심 해설</div>
        <div class="trend-box">${escHtml(item.trend_note)}</div>
        <div class="formula-box">${escHtml(item.lecture_point || item.concept)}</div>
        <div class="exp-text">${escHtml(item.lecture_summary)}</div>
      </div>

      <div class="card-foot">
        <button class="status-btn ${isMark ? 'marked' : ''}" onclick="toggleBookmark(${item.id})">${isMark ? '🔖 북마크됨' : '🔖 다시보기 체크'}</button>
        <button class="status-btn ${isDone ? 'done' : ''}" onclick="toggleDone(${item.id})">${isDone ? '✔ 암기 완료!' : '⬜ 암기 완료 체크'}</button>
      </div>
    </article>
  `;
}

function renderTop55() {
  const list = getFilteredList();
  const container = document.getElementById('top55Container');
  const jumpBar = document.getElementById('jumpBar');
  const bottomBar = document.getElementById('bottomBar');

  if (!list.length) {
    jumpBar.style.display = 'none';
    bottomBar.style.display = 'none';
    container.innerHTML = `<div class="empty-state">조건에 맞는 문항이 없습니다.<br>다른 필터나 검색어를 선택해 주세요.</div>`;
    return;
  }

  if (state.cardIdx >= list.length) state.cardIdx = 0;
  if (state.cardIdx < 0) state.cardIdx = list.length - 1;

  if (state.viewMode === 'card') {
    jumpBar.style.display = 'flex';
    bottomBar.style.display = 'block';
    const cur = list[state.cardIdx];
    document.getElementById('posLabel').textContent = `${state.cardIdx + 1} / ${list.length}`;
    const sel = document.getElementById('jumpSelect');
    sel.innerHTML = list.map((x, i) => `<option value="${i}" ${i===state.cardIdx?'selected':''}>#${x.rank}위 (${x.prob}%) ${x.title.slice(0,22)}</option>`).join('');
    container.innerHTML = renderCardHtml(cur);
    document.getElementById('bMarkBtn').textContent = state.bookmark[cur.id] ? '🔖됨' : '🔖';
  } else {
    jumpBar.style.display = 'none';
    bottomBar.style.display = 'none';
    container.innerHTML = list.map(renderCardHtml).join('');
  }
}

function togglePanel(id, kind) {
  const panel = document.getElementById(`panel-${kind}-${id}`);
  const btn = document.getElementById(`btn-${kind}-${id}`);
  if (!panel || !btn) return;
  const open = panel.classList.toggle('open');
  if (kind === 'ans') {
    btn.classList.toggle('ans-open', open);
    btn.textContent = open ? '✅ 정답 닫기' : '✅ STEP 2. 정답 보기';
  } else {
    btn.classList.toggle('exp-open', open);
    btn.textContent = open ? '💡 해설 닫기' : '💡 STEP 3. 해설 보기';
  }
}

function toggleCurrentPanel(kind) {
  const list = getFilteredList();
  if (!list.length) return;
  const cur = list[state.cardIdx];
  if (cur) togglePanel(cur.id, kind);
}

function toggleBookmark(id) {
  state.bookmark[id] = !state.bookmark[id];
  saveState();
  renderTop55();
}

function toggleCurrentMark() {
  const list = getFilteredList();
  if (!list.length) return;
  toggleBookmark(list[state.cardIdx].id);
}

function toggleDone(id) {
  state.done[id] = !state.done[id];
  saveState();
  updateProgress();
  renderTop55();
}

function moveCard(delta) {
  const list = getFilteredList();
  if (!list.length) return;
  state.cardIdx = (state.cardIdx + delta + list.length) % list.length;
  saveState();
  renderTop55();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function jumpTo(val) {
  state.cardIdx = parseInt(val, 10) || 0;
  saveState();
  renderTop55();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function setFilter(f) {
  state.filter = f;
  state.cardIdx = 0;
  document.querySelectorAll('#filterBar .chip').forEach(c => c.classList.toggle('active', c.dataset.f === f));
  renderTop55();
}

function onSearch() {
  state.search = document.getElementById('searchInput').value;
  state.cardIdx = 0;
  renderTop55();
}

function toggleViewMode() {
  state.viewMode = state.viewMode === 'card' ? 'list' : 'card';
  applyPrefs();
  saveState();
  renderTop55();
}

/* ===== MODE 2: 3-PERIOD FULL EXAM ===== */
function switchMode(m) {
  state.mode = m;
  document.getElementById('tabTop55').classList.toggle('active', m === 'top55');
  document.getElementById('tabExam').classList.toggle('active', m === 'exam');
  document.getElementById('secTop55').style.display = m === 'top55' ? 'block' : 'none';
  document.getElementById('secExam').style.display = m === 'exam' ? 'block' : 'none';
  document.getElementById('bottomBar').style.display = (m === 'top55' && state.viewMode === 'card') ? 'block' : 'none';
  if (m === 'exam') renderExamPart();
  else renderTop55();
}

function switchExamPart(p) {
  state.examPart = p;
  document.getElementById('subPed').classList.toggle('active', p === 'ped');
  document.getElementById('subA').classList.toggle('active', p === 'A');
  document.getElementById('subB').classList.toggle('active', p === 'B');
  renderExamPart();
}

function renderExamPart() {
  const c = document.getElementById('examContainer');
  if (state.examPart === 'ped') {
    c.innerHTML = `
      <article class="card">
        <div class="card-meta">
          <span class="rank-badge">1교시</span>
          <span class="tier-badge tier-0">🔥 0순위 적중 · 20점 만점</span>
          <span class="domain-tag">4대 영역 × 4발문 = 16개 세부 질문</span>
        </div>
        <h2 class="card-title">2027학년도 1교시 교육학 논술 (학생 주도적 성장을 이끄는 미래형 학교 교육)</h2>

        <div class="problem-box">
          <div class="step-label" style="color:var(--accent);">📄 STEP 1. 실전 논술 지문 & 작성 방법</div>
          <div class="ped-prose">${PED_EXAM.passageHtml}</div>
          <div class="ped-rubric">${PED_EXAM.rubricHtml}</div>
        </div>

        <div class="step-actions">
          <button class="reveal-btn" id="btn-ped-ans" onclick="togglePedBox('ans')">✅ STEP 2. 만점 논술 답안</button>
          <button class="reveal-btn" id="btn-ped-exp" onclick="togglePedBox('exp')">💡 STEP 3. 16개 채점 포인트</button>
        </div>

        <div class="answer-panel" id="panel-ped-ans">
          <div class="step-label" style="color:var(--success);">✅ 20점 만점 모범 논술 답안</div>
          <div class="ped-ans-content">${PED_EXAM.answerHtml}</div>
        </div>

        <div class="exp-panel" id="panel-ped-exp">
          <div class="step-label" style="color:var(--accent-2);">💡 4대 영역 16개 핵심 채점 키워드 요약</div>
          <div class="formula-box">
            ① 교육과정: 백워드 설계(1단계 바라는 결과 확인·영속적 이해 / 활동위주·진도나가기 오류 극복) + 스킬벡(상황분석·내적/외적 요인)<br><br>
            ② 교육방법: 플립드 러닝(수업 전·중·후 3단계) + 스웰러 인지부하(외재적 부하 감소·본유적 부하 촉진·전문성 역전 효과)<br><br>
            ③ 교육평가: 비고츠키 ZPD 역동적 평가(사전검사-교수적 중재-사후검사) + 분석적 루브릭(평가준거·성취수준·척도기술어·사전공개)<br><br>
            ④ 교육행정: 세르지오바니 도덕적 리더십(도덕적 권위·학교 공동체) + 겟젤스-구바 사회체계(규범적 차원·개인적 차원·절충형 지도성)
          </div>
        </div>
      </article>
    `;
    return;
  }

  const list = state.examPart === 'A' ? EXAM_A : EXAM_B;
  const label = state.examPart === 'A' ? '2교시 전공 A형' : '3교시 전공 B형';
  c.innerHTML = list.map((q, idx) => {
    const uid = `${state.examPart}_${idx}`;
    const asksHtml = (q.asks || []).map(a => `<li>○ ${escHtml(a)}</li>`).join('');
    const kwsHtml = (q.kws || []).map(k => `<span class="kw-chip"># ${escHtml(k)}</span>`).join('');
    const linesHtml = (q.ans || q.answer || []).map((ln, i) => `
      <div class="ans-line">
        <span class="line-num">${i+1}줄</span>
        <span>${highlightKws(ln, q.kws)}</span>
      </div>
    `).join('');

    return `
      <article class="card">
        <div class="card-meta">
          <span class="rank-badge">${label} ${q.num}번</span>
          <span class="tier-badge tier-0">${escHtml(q.type)} · ${q.score}점</span>
          <span class="domain-tag">힌트 ZERO 초장문 실전형</span>
        </div>
        <h2 class="card-title">${escHtml(q.lead)}</h2>

        <div class="problem-box">
          <div class="step-label" style="color:var(--accent);">📄 STEP 1. 실전 사례 지문</div>
          <div class="passage-text">${escHtml(q.passage)}</div>
          ${asksHtml ? `<div class="asks-box"><div class="asks-title">&lt;작성 방법&gt;</div><ul class="asks-list">${asksHtml}</ul></div>` : ''}
        </div>

        <div class="step-actions">
          <button class="reveal-btn" id="btn-exans-${uid}" onclick="toggleExamBox('${uid}','ans')">✅ STEP 2. 정답 보기</button>
          <button class="reveal-btn" id="btn-exexp-${uid}" onclick="toggleExamBox('${uid}','exp')">💡 STEP 3. 채점 키워드 해설</button>
        </div>

        <div class="answer-panel" id="panel-exans-${uid}">
          <div class="step-label" style="color:var(--success);">✅ B4 답안지 만점 모범답안</div>
          <div class="ans-lines">${linesHtml}</div>
        </div>

        <div class="exp-panel" id="panel-exexp-${uid}">
          <div class="step-label" style="color:var(--accent-2);">💡 KICE 필수 채점 키워드 & 출제 의도</div>
          <div class="kw-row">${kwsHtml}</div>
          <div class="exp-text">본 문항은 2020~2026 평가원 복합형 출제 패턴(2~3개 이론 융합)을 100% 반영한 힌트 ZERO 실전 문항입니다. 위 필수 채점 키워드를 빠짐없이 포함하여 줄당 38~45자 이내로 간결하게 서술하면 만점(${q.score}점)을 획득할 수 있습니다.</div>
        </div>
      </article>
    `;
  }).join('');
}

function togglePedBox(kind) {
  const p = document.getElementById(`panel-ped-${kind}`);
  const b = document.getElementById(`btn-ped-${kind}`);
  const open = p.classList.toggle('open');
  b.classList.toggle(kind === 'ans' ? 'ans-open' : 'exp-open', open);
}

function toggleExamBox(uid, kind) {
  const p = document.getElementById(`panel-ex${kind}-${uid}`);
  const b = document.getElementById(`btn-ex${kind}-${uid}`);
  const open = p.classList.toggle('open');
  b.classList.toggle(kind === 'ans' ? 'ans-open' : 'exp-open', open);
}

// Touch swipe support in mobile card mode
let touchStartX = 0, touchStartY = 0;
document.addEventListener('touchstart', e => {
  if (state.mode !== 'top55' || state.viewMode !== 'card') return;
  touchStartX = e.changedTouches[0].screenX;
  touchStartY = e.changedTouches[0].screenY;
}, { passive: true });

document.addEventListener('touchend', e => {
  if (state.mode !== 'top55' || state.viewMode !== 'card') return;
  const dx = e.changedTouches[0].screenX - touchStartX;
  const dy = e.changedTouches[0].screenY - touchStartY;
  if (Math.abs(dx) > 65 && Math.abs(dx) > Math.abs(dy) * 1.5) {
    if (dx < 0) moveCard(1);
    else moveCard(-1);
  }
}, { passive: true });

// Init
updateDDay();
applyPrefs();
updateProgress();
renderTop55();
</script>
</body>
</html>
"""

final_html = (
    HTML_TEMPLATE
    .replace("__TOP55_JSON__", TOP55_JSON)
    .replace("__PED_DATA_JSON__", PED_DATA_JSON)
    .replace("__EXAM_A_JS__", exam_a_js)
    .replace("__EXAM_B_JS__", exam_b_js)
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Successfully built index.html! Size:", len(final_html), "chars")
