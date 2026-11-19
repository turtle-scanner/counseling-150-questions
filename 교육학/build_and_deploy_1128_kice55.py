# -*- coding: utf-8 -*-
import json
import os
import shutil

# Load the validated 55 KICE 4-line items
with open("kice_55_4lines_master.json", "r", encoding="utf-8") as f:
    kice55_data = json.load(f)

# Load existing all_exam_master_data.json for PED(16), A(12), B(11)
with open("all_exam_master_data.json", "r", encoding="utf-8") as f:
    exam_master = json.load(f)

data_ped = exam_master["pedagogy"]
data_a = exam_master["counselingA"]
data_b = exam_master["counselingB"]

# Build Universal 4-Line Templates (내 교육학 논술 플랫폼 3선 + 전공상담 만능 템플릿 3선 = 총 6선)
templates_data = [
    {
        "id": 1,
        "domain": "내 교육학 플랫폼 (서론)",
        "title": "[내 교육학 플랫폼 1] 1교시 교육학 만능 서론 4줄 공식 (미래 교육환경 속에서 ~ 화제가 대두되고 있다)",
        "concept": "어떤 대주제가 나와도 (대주제) 자리만 바꿔 넣으면 1분 만에 서론 4줄 만점을 완성하는 변귀섭 대표님 전용 서론 플랫폼",
        "keywords": ["미래 교육환경 속에서", "화제가 대두되고 있다", "단편적 지식 전달이 아닌 역량", "교육과정, 교육방법, 교육평가, 교육행정"],
        "lines": [
            "최근 급변하는 미래 교육환경 속에서 (대주제)에 대한 화제가 대두되고 있다.",
            "이러한 패러다임에 맞춰 교사는 단편적 지식 전달이 아닌 역량을 함양해야 한다.",
            "여기에서는 제시문에 나온 교사들의 대화를 통해 (대주제) 방안을 살펴본다.",
            "교육과정, 교육방법, 교육평가, 교육행정의 4가지 측면에서 논하고자 한다."
        ],
        "line_blanks": [
            ["미래 교육환경 속에서", "(대주제)", "화제가 대두되고 있다"],
            ["단편적 지식 전달", "역량을 함양"],
            ["교사들의 대화", "(대주제) 방안"],
            ["교육과정, 교육방법, 교육평가, 교육행정"]
        ],
        "cases8": [
            {"q": "① 서론 첫머리 시대 배경 어구", "a": "최근 급변하는 미래 교육환경 속에서"},
            {"q": "② 서론 1줄 핵심 술어 공식", "a": "화제가 대두되고 있다"},
            {"q": "③ 서론 2줄 지양해야 할 전통적 교사상", "a": "단편적 지식 전달"},
            {"q": "④ 서론 2줄 지향해야 할 미래형 교사상", "a": "교육적 역량을 함양해야 한다"},
            {"q": "⑤ 서론 3줄 분석 대상 제시 어구", "a": "제시문에 나온 교사들의 대화를 통해"},
            {"q": "⑥ 서론 4줄 교육학 4대 핵심 영역", "a": "교육과정, 교육방법, 교육평가, 교육행정"},
            {"q": "⑦ 서론 4줄 마무리 서술어 공식", "a": "4가지 측면에서 논하고자 한다"},
            {"q": "⑧ 서론에서 문제지 제목을 그대로 넣는 칸", "a": "(대주제)"}
        ],
        "quiz_q": "내 교육학 플랫폼 서론 1번째 줄을 시작하는 대표님의 황금 도입 문장은?",
        "quiz_a": "최근 급변하는 미래 교육환경 속에서 (대주제)에 대한 화제가 대두되고 있다."
    },
    {
        "id": 2,
        "domain": "내 교육학 플랫폼 (본론 이처럼~)",
        "title": "[내 교육학 플랫폼 2] 1교시 교육학 본론 4대 영역 마무리 공식 (이처럼 교사가 ~에서 ~를 쓰면 ~이 실현된다)",
        "concept": "본론 1(교육과정)·본론 2(교육방법)·본론 3(교육평가)·본론 4(교육행정) 각 단락의 마지막 줄에 무조건 박아 넣는 만점 연결 공식",
        "keywords": ["이처럼 교사가 교육과정에서", "미래형 교육 혁신", "신개념 수업 혁신", "교사의 수석 역량"],
        "lines": [
            "이처럼 교사가 교육과정에서 (핵심키워드)를 쓰면 미래형 교육 혁신이 실현된다.",
            "이처럼 교사가 교육방법에서 (핵심키워드)를 쓰면 신개념 수업 혁신이 실현된다.",
            "이처럼 교사가 교육평가에서 (핵심키워드)를 쓰면 전인적 성장 평가가 실현된다.",
            "이처럼 교사가 교육행정에서 (핵심키워드)를 쓰면 교사의 수석 역량이 증진된다."
        ],
        "line_blanks": [
            ["이처럼 교사가 교육과정에서", "(핵심키워드)", "미래형 교육 혁신이 실현된다"],
            ["이처럼 교사가 교육방법에서", "(핵심키워드)", "신개념 수업 혁신이 실현된다"],
            ["이처럼 교사가 교육평가에서", "(핵심키워드)", "전인적 성장 평가가 실현된다"],
            ["이처럼 교사가 교육행정에서", "(핵심키워드)", "교사의 수석 역량이 증진된다"]
        ],
        "cases8": [
            {"q": "① 본론 모든 단락 마지막 줄 시작 접속어", "a": "이처럼 교사가"},
            {"q": "② 본론 1(교육과정) 마지막 줄 공식 효과", "a": "미래형 교육 혁신이 실현된다"},
            {"q": "③ 본론 2(교육방법) 마지막 줄 공식 효과", "a": "신개념 수업 혁신이 실현된다"},
            {"q": "④ 본론 3(교육평가) 마지막 줄 공식 효과", "a": "전인적 성장 평가가 실현된다"},
            {"q": "⑤ 본론 4(교육행정) 마지막 줄 공식 효과", "a": "교사의 수석 역량이 증진된다"},
            {"q": "⑥ 본론 1~4 단락 시작 번호 표기", "a": "첫째, 둘째, 셋째, 넷째"},
            {"q": "⑦ 백워드 설계 출제 시 이처럼~ 적용 예", "a": "이처럼 교사가 교육과정에서 백워드 설계를 쓰면"},
            {"q": "⑧ 동료장학 출제 시 이처럼~ 적용 예", "a": "이처럼 교사가 교육행정에서 동료장학을 활성화하면"}
        ],
        "quiz_q": "본론 4대 영역(과정·방법·평가·행정) 각 문단 마지막 줄을 닫는 대표님의 시그니처 공식은?",
        "quiz_a": "이처럼 교사가 ~에서 (핵심키워드)를 쓰면 ~이 실현된다"
    },
    {
        "id": 3,
        "domain": "내 교육학 플랫폼 (결론)",
        "title": "[내 교육학 플랫폼 3] 1교시 교육학 만능 결론 4줄 공식 (지금까지 ~ 든든한 버팀목이자 교육 안내자 및 성장 촉진자)",
        "concept": "1교시 종료 5분 전 생각할 필요 없이 손가락 근육 기억만으로 4줄을 일필휘지하여 구성·표현 4점 만점을 확정 짓는 결론 플랫폼",
        "keywords": ["지금까지 (대주제)를", "교사의 인식과 실천", "자기 연찬과 동료 교사와의 협업", "든든한 버팀목이자 교육 안내자 및 성장 촉진자"],
        "lines": [
            "지금까지 (대주제)를 교육과정, 교육방법, 교육평가, 교육행정에서 살펴보았다.",
            "다가오는 미래 교육이 성공하려면 무엇보다 교사의 인식과 실천이 중요하다.",
            "따라서 교사는 끊임없는 자기 연찬과 동료 교사와의 협업으로 성장해야 한다.",
            "또한 학생들에게 든든한 버팀목이자 교육 안내자 및 성장 촉진자가 되어야 한다."
        ],
        "line_blanks": [
            ["지금까지 (대주제)를", "교육과정, 교육방법, 교육평가, 교육행정"],
            ["미래 교육이 성공하려면", "교사의 인식과 실천이 중요하다"],
            ["자기 연찬", "동료 교사와의 협업"],
            ["든든한 버팀목", "교육 안내자", "성장 촉진자"]
        ],
        "cases8": [
            {"q": "① 결론 1줄 종합 요약 시작 어구", "a": "지금까지 (대주제)를"},
            {"q": "② 결론 1줄 4대 영역 재언급", "a": "교육과정, 교육방법, 교육평가, 교육행정에서 살펴보았다"},
            {"q": "③ 결론 2줄 미래 교육 성공의 핵심 요건", "a": "교사의 인식과 실천이 중요하다"},
            {"q": "④ 결론 3줄 교사 개인의 전문성 노력", "a": "끊임없는 자기 연찬"},
            {"q": "⑤ 결론 3줄 공동체적 전문성 노력", "a": "동료 교사와의 협업"},
            {"q": "⑥ 결론 4줄 학생을 위한 교사의 역할 1", "a": "든든한 버팀목"},
            {"q": "⑦ 결론 4줄 학생을 위한 교사의 역할 2", "a": "교육 안내자"},
            {"q": "⑧ 결론 4줄 학생을 위한 교사의 역할 3", "a": "성장 촉진자"}
        ],
        "quiz_q": "내 교육학 플랫폼 결론 마지막 줄에 들어가는 교사의 3대 비유적 핵심 역할은?",
        "quiz_a": "든든한 버팀목, 교육 안내자, 성장 촉진자"
    },
    {
        "id": 4,
        "domain": "전공상담 감별진단 만능틀",
        "title": "[만점 템플릿 4] 2·3교시 DSM-5-TR 감별진단 및 행동치료 개입 4줄 만능 템플릿",
        "concept": "진단명 1:1 대조 ➔ 결정적 감별 기준 ➔ 자아 동질/이질 기제 ➔ 노출 치료 개입의 4줄 공식",
        "keywords": ["공식 진단명", "결정적인 감별 기준", "자아 이질적 특성", "불안이 자연 소거"],
        "lines": [
            "사례에 나타난 1번 내담자의 공식 진단명은 갑이며 2번은 을로 각각 감별한다.",
            "두 장애를 임상적으로 구별하는 가장 결정적인 감별 기준은 핵심 증상의 유무이다.",
            "갑은 증상을 비합리적인 것으로 여겨 고통스러워하는 자아 이질적 특성을 나타낸다.",
            "두려운 자극에 직면하게 하고 회피 반응을 차단하여 불안이 자연 소거되도록 돕는다."
        ],
        "line_blanks": [
            ["공식 진단명"],
            ["결정적인 감별 기준", "핵심 증상의 유무"],
            ["자아 이질적 특성"],
            ["회피 반응을 차단", "불안이 자연 소거"]
        ],
        "cases8": [
            {"q": "① 감별진단 1줄 필수 키워드", "a": "공식 진단명"},
            {"q": "② 감별진단 2줄 필수 키워드", "a": "결정적인 감별 기준"},
            {"q": "③ 증상을 괴로워하는 특성", "a": "자아 이질적(Ego-dystonic)"},
            {"q": "④ 증상을 당연시하는 특성", "a": "자아 동질적(Ego-syntonic)"},
            {"q": "⑤ 행동치료 직면 기법", "a": "노출 및 반응방지(ERP)"},
            {"q": "⑥ 회피 차단 시 일어나는 원리", "a": "불안이 자연 소거"},
            {"q": "⑦ 단계적 불안 둔감화 기법", "a": "체계적 둔감법"},
            {"q": "⑧ 인지적 재구조화 병행", "a": "파국적 오해석 교정"}
        ],
        "quiz_q": "DSM-5-TR 감별진단 서술형 1번째 줄과 2번째 줄에 각각 들어가야 할 핵심 요소는?",
        "quiz_a": "공식 진단명, 결정적인 감별 기준"
    },
    {
        "id": 5,
        "domain": "전공상담 이론·가족 만능틀",
        "title": "[만점 템플릿 5] 2·3교시 상담이론 및 가족치료 사례개념화 4줄 만능 템플릿",
        "concept": "부적응 원인 개념화 ➔ 상담자 태도(중립성·공감) ➔ 지금-여기 기법 ➔ 자아 통합 및 분화",
        "keywords": ["역기능적 가족 경계선", "정서적 중립성", "지금 여기의 갈등", "자기분화와 심리적 유연성"],
        "lines": [
            "내담자의 심리적 부적응은 왜곡된 신념 체계와 역기능적 가족 경계선에서 비롯된다.",
            "상담자는 어느 한쪽에도 치우치지 않는 정서적 중립성과 공감적 수용 태도를 지킨다.",
            "상담실 안에서 지금 여기의 갈등과 억압된 감정을 직접 직면하고 탐색하도록 돕는다.",
            "소외된 내면의 감정을 통합하고 자율적인 자기분화와 심리적 유연성을 회복시킨다."
        ],
        "line_blanks": [
            ["왜곡된 신념 체계", "역기능적 가족 경계선"],
            ["정서적 중립성", "공감적 수용"],
            ["지금 여기의 갈등"],
            ["자기분화", "심리적 유연성"]
        ],
        "cases8": [
            {"q": "① 인지적 부적응 원인", "a": "왜곡된 신념 체계"},
            {"q": "② 가족체계적 부적응 원인", "a": "역기능적 가족 경계선"},
            {"q": "③ 보웬 상담자의 핵심 태도", "a": "정서적 중립성 유지"},
            {"q": "④ 인간중심 상담자의 핵심 태도", "a": "공감적 수용과 무조건적 긍정적 존중"},
            {"q": "⑤ 게슈탈트·실존 시공간 초점", "a": "지금-여기(Here and Now)"},
            {"q": "⑥ 억압된 감정 다루기", "a": "직면 및 미해결 과제 완결"},
            {"q": "⑦ 보웬 가족치료 궁극적 목표", "a": "자기분화 수준 향상"},
            {"q": "⑧ 수용전념치료(ACT) 궁극적 목표", "a": "심리적 유연성 회복"}
        ],
        "quiz_q": "상담이론 및 가족치료 개입에서 내담자의 무의식적 갈등과 감정을 다루는 시공간적 초점은?",
        "quiz_a": "지금-여기(Here and Now)"
    },
    {
        "id": 6,
        "domain": "전공상담 검사·위기 만능틀",
        "title": "[만점 템플릿 6] 2·3교시 심리검사 해석 및 자살·학폭 위기개입 4줄 만능 템플릿",
        "concept": "과부하 프로파일 해석 ➔ 지금-여기 즉각 사정 ➔ 비밀보장 예외 통보 ➔ 안전계획서 및 연계",
        "keywords": ["심리적 과부하 상태", "자살 충동과 계획", "비밀보장의 예외", "안전계획서와 전문 의료기관"],
        "lines": [
            "검사 결과 가용 자원에 비해 스트레스 자극이 훨씬 큰 심리적 과부하 상태를 보인다.",
            "즉각적인 생명 위협을 파악하기 위해 지금 여기에서의 자살 충동과 계획을 묻는다.",
            "자살 및 폭력 위기는 비밀보장의 예외 사안이므로 보호자에게 사실을 즉각 알린다.",
            "위기관리위원회를 소집하고 안전계획서를 작성하며 전문 의료기관으로 긴급 연계한다."
        ],
        "line_blanks": [
            ["심리적 과부하 상태"],
            ["지금 여기", "자살 충동과 계획"],
            ["비밀보장의 예외"],
            ["위기관리위원회", "안전계획서", "전문 의료기관"]
        ],
        "cases8": [
            {"q": "① 로샤 D<0, AdjD<0 및 RCd 고점 상태", "a": "심리적 과부하 상태"},
            {"q": "② CASE 모델 가장 먼저 사정할 영역", "a": "제시된 자살 사건과 즉각적 사건"},
            {"q": "③ 자살·학폭 위기 시 윤리적 원칙", "a": "비밀보장의 예외"},
            {"q": "④ 비밀보장 예외 시 1차 통보 대상", "a": "보호자 및 학교장 즉각 통보"},
            {"q": "⑤ 교내 위기 대응 기구 소집", "a": "위기관리위원회 소집"},
            {"q": "⑥ 내담자와 함께 작성하는 행동지침", "a": "안전계획서 작성"},
            {"q": "⑦ 자살 수단 사전 차단 조치", "a": "치명적 자살 수단 제거"},
            {"q": "⑧ 외부 전문기관 협진 조치", "a": "정신건강의학과 등 전문 의료기관 긴급 연계"}
        ],
        "quiz_q": "자살 및 생명 위협 위기 시 상담자가 법적·윤리적으로 반드시 발동해야 하는 원칙은?",
        "quiz_a": "비밀보장의 예외"
    }
]

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>2027학년도 11.28 임용고시 결전 - 55개 KICE 핵심키워드 4줄 정답 & 만점 템플릿 타이핑 마스터</title>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-main: #0a0f1d;
  --bg-card: #121929;
  --bg-card-header: #182238;
  --bg-passage: #0b1220;
  --border-kice: #22314d;
  --border-kice-focus: #38bdf8;
  --text-main: #f1f5f9;
  --text-sub: #94a3b8;
  --text-muted: #64748b;
  --accent-blue: #38bdf8;
  --accent-gold: #fbbf24;
  --accent-emerald: #10b981;
  --accent-rose: #f43f5e;
  --accent-purple: #c084fc;
  --font-scale: 1;
}}

body.b4-paper-mode {{
  --bg-main: #18191c;
  --bg-card: #e8e3d5;
  --bg-card-header: #dbd4c0;
  --bg-passage: #f3efe6;
  --border-kice: #8c826e;
  --border-kice-focus: #1e3a8a;
  --text-main: #111827;
  --text-sub: #374151;
  --text-muted: #4b5563;
  --accent-blue: #1e40af;
  --accent-gold: #b45309;
  --accent-emerald: #047857;
  --accent-rose: #b91c1c;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
button, input, textarea, select {{
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}}

body {{
  font-family: 'Noto Sans KR', sans-serif;
  background-color: var(--bg-main);
  color: var(--text-main);
  line-height: 1.6;
  min-height: 100vh;
  padding-bottom: 90px;
  user-select: text;
  transition: background-color 0.3s, color 0.3s;
}}

.kice-exam-header {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(10, 15, 29, 0.98);
  backdrop-filter: blur(12px);
  border-bottom: 2px solid #1e3a5f;
  padding: 10px 24px;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.7);
}}
body.b4-paper-mode .kice-exam-header {{
  background: rgba(220, 215, 200, 0.98);
  border-bottom: 2px solid #8c826e;
}}

.header-inner {{
  max-width: 1560px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}}

.brand-section {{
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}}

.kice-seal {{
  background: linear-gradient(135deg, #d97706, #b45309);
  color: #fff;
  font-size: 0.78rem;
  font-weight: 900;
  padding: 4px 10px;
  border-radius: 4px;
  letter-spacing: 0.5px;
  border: 1px solid #fbbf24;
}}

.exam-main-title {{
  font-size: 1.12rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}}

.examinee-tag {{
  color: #38bdf8;
  font-weight: 700;
  font-size: 0.85rem;
  background: rgba(56, 189, 248, 0.1);
  padding: 3px 8px;
  border-radius: 4px;
  border: 1px solid rgba(56, 189, 248, 0.3);
}}
body.b4-paper-mode .examinee-tag {{
  color: #1e3a8a;
  background: rgba(30, 58, 138, 0.1);
  border-color: #1e3a8a;
}}

.timer-container {{
  display: flex;
  align-items: center;
  gap: 8px;
  background: #091322;
  border: 1px solid #1e3a5f;
  padding: 4px 12px;
  border-radius: 8px;
}}
body.b4-paper-mode .timer-container {{
  background: #fdfbf7;
  border-color: #8c826e;
}}

.timer-label {{
  font-size: 0.75rem;
  color: var(--text-sub);
  font-weight: 600;
}}

.timer-digits {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--accent-gold);
  letter-spacing: 1px;
  min-width: 75px;
  text-align: center;
}}
.timer-digits.warning {{
  color: var(--accent-rose);
  animation: pulse-warn 1s infinite alternate;
}}

@keyframes pulse-warn {{
  from {{ opacity: 1; }}
  to {{ opacity: 0.4; }}
}}

.btn-timer {{
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.72rem;
  padding: 3px 7px;
  border-radius: 4px;
  cursor: pointer;
}}
body.b4-paper-mode .btn-timer {{
  background: #e2dcd0;
  color: #1f2937;
  border-color: #9ca3af;
}}

.wpm-badge {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--accent-emerald);
  background: rgba(16, 185, 129, 0.1);
  padding: 2px 7px;
  border-radius: 4px;
  border: 1px solid rgba(16, 185, 129, 0.3);
}}

.btn-asmr {{
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.75rem;
  padding: 5px 9px;
  border-radius: 6px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}}
.btn-asmr.on {{
  background: rgba(56, 189, 248, 0.2);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}}

.font-scale-ctrl {{
  display: flex;
  align-items: center;
  gap: 3px;
  background: #0d1525;
  padding: 2px 6px;
  border-radius: 6px;
  border: 1px solid var(--border-kice);
}}
body.b4-paper-mode .font-scale-ctrl {{
  background: #dbd4c0;
}}
.btn-font-scale {{
  background: transparent;
  border: none;
  color: var(--text-sub);
  font-size: 0.75rem;
  font-weight: 800;
  cursor: pointer;
  padding: 2px 5px;
}}
.btn-font-scale:hover {{ color: var(--accent-blue); }}

.header-actions {{
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}}

.btn-kice {{
  background: #131c2e;
  color: #e2e8f0;
  border: 1px solid #2a3a54;
  padding: 5px 10px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}}
body.b4-paper-mode .btn-kice {{
  background: #fdfbf7;
  color: #1f2937;
  border-color: #8c826e;
}}
.btn-kice:hover {{
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}}
.btn-kice.accent {{
  background: linear-gradient(135deg, #0284c7, #2563eb);
  border: none;
  color: #fff;
}}

.round-selector-group {{
  display: flex;
  align-items: center;
  gap: 4px;
  background: #0d1525;
  border: 1px solid var(--border-kice);
  padding: 3px 8px;
  border-radius: 6px;
}}
body.b4-paper-mode .round-selector-group {{
  background: #dbd4c0;
}}
.round-btn {{
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-sub);
  font-size: 0.76rem;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}}
.round-btn:hover {{ color: var(--accent-blue); }}
.round-btn.active {{
  background: linear-gradient(135deg, #0284c7, #2563eb);
  color: #fff;
  border-color: #38bdf8;
  box-shadow: 0 0 8px rgba(56, 189, 248, 0.4);
}}

.btn-kice.danger {{
  border-color: rgba(244, 63, 94, 0.4);
  color: #fda4af;
}}
.btn-kice.danger:hover {{
  background: rgba(244, 63, 94, 0.2);
  border-color: var(--accent-rose);
  color: var(--accent-rose);
}}

.sub-bar {{
  max-width: 1560px;
  margin: 12px auto 0;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}}

.period-tabs {{
  display: flex;
  gap: 6px;
  background: #0d1525;
  padding: 4px;
  border-radius: 8px;
  border: 1px solid var(--border-kice);
  flex-wrap: wrap;
}}
body.b4-paper-mode .period-tabs {{
  background: #dbd4c0;
}}

.period-tab-btn {{
  padding: 7px 14px;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 800;
  border: none;
  cursor: pointer;
  background: transparent;
  color: var(--text-sub);
  transition: all 0.2s;
}}
.period-tab-btn.active {{
  background: linear-gradient(135deg, #1e3a8a, #0284c7);
  color: #fff;
  box-shadow: 0 2px 10px rgba(2, 132, 199, 0.45);
}}
.period-tab-btn.highlight-tab {{
  border: 1px solid rgba(251, 191, 36, 0.4);
  color: #fde68a;
}}
.period-tab-btn.highlight-tab.active {{
  background: linear-gradient(135deg, #d97706, #b45309);
  color: #fff;
  border-color: #fbbf24;
  box-shadow: 0 2px 12px rgba(245, 158, 11, 0.5);
}}

/* 55선 세부 카테고리 필터 바 */
.kice55-filter-bar {{
  max-width: 1560px;
  margin: 10px auto 0;
  padding: 10px 24px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
}}
.k55-cat-btn {{
  background: #101726;
  border: 1px solid var(--border-kice);
  color: var(--text-sub);
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
}}
body.b4-paper-mode .k55-cat-btn {{
  background: #e5ded0;
  border-color: #a39985;
}}
.k55-cat-btn.active {{
  background: rgba(56, 189, 248, 0.2);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}}
.k55-search-input {{
  margin-left: auto;
  background: #080d18;
  border: 1px solid var(--border-kice);
  color: var(--text-main);
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 0.85rem;
  min-width: 260px;
}}
body.b4-paper-mode .k55-search-input {{
  background: #faf8f3;
  color: #111827;
}}

.filter-group {{
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}}

.filter-btn {{
  background: transparent;
  border: 1px solid var(--border-kice);
  color: var(--text-sub);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.78rem;
  cursor: pointer;
}}
.filter-btn.active {{
  background: rgba(251, 191, 36, 0.2);
  border-color: var(--accent-gold);
  color: var(--accent-gold);
  font-weight: 800;
}}

.nav-strip {{
  max-width: 1560px;
  margin: 8px auto 0;
  padding: 0 24px 6px;
  display: flex;
  gap: 6px;
  overflow-x: auto;
}}

.nav-pill {{
  background: #101726;
  border: 1px solid var(--border-kice);
  color: var(--text-sub);
  padding: 4px 10px;
  border-radius: 5px;
  font-size: 0.75rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s;
}}
body.b4-paper-mode .nav-pill {{
  background: #e5ded0;
  border-color: #a39985;
}}
.nav-pill:hover {{
  border-color: var(--accent-blue);
  color: #fff;
}}
.nav-pill.done {{
  border-color: var(--accent-emerald);
  color: var(--accent-emerald);
  background: rgba(16, 185, 129, 0.08);
}}
.nav-pill.bookmarked {{
  border-color: var(--accent-gold);
  color: var(--accent-gold);
}}

main {{
  max-width: 1560px;
  margin: 14px auto 0;
  padding: 0 24px;
  display: flex;
  flex-direction: column;
  gap: 22px;
}}

.q-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-kice);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
  transition: all 0.2s;
}}

.q-card-head {{
  background: var(--bg-card-header);
  padding: 10px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-kice);
  flex-wrap: wrap;
  gap: 8px;
}}

.q-num-title {{
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--accent-gold);
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}}

.bookmark-star {{
  cursor: pointer;
  font-size: 1.15rem;
  color: #4b5563;
  transition: transform 0.2s, color 0.2s;
}}
.bookmark-star.active {{
  color: var(--accent-gold);
  transform: scale(1.15);
}}

.type-pill {{
  font-size: 0.72rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 4px;
}}
.type-pill.fillin {{ background: rgba(192, 132, 252, 0.15); color: #d8b4fe; border: 1px solid #9333ea; }}
.type-pill.essay {{ background: rgba(56, 189, 248, 0.15); color: #7dd3fc; border: 1px solid #0284c7; }}
.type-pill.k55 {{ background: rgba(245, 158, 11, 0.2); color: #fde68a; border: 1px solid #f59e0b; }}

.q-card-body {{
  padding: 18px;
}}

.q-question-text {{
  font-size: calc(1.08rem * var(--font-scale));
  font-weight: 800;
  margin-bottom: 10px;
  line-height: 1.45;
  color: var(--text-main);
}}

.concept-banner {{
  background: rgba(56, 189, 248, 0.08);
  border-left: 4px solid var(--accent-blue);
  padding: 8px 14px;
  border-radius: 4px;
  font-size: calc(0.9rem * var(--font-scale));
  color: var(--text-sub);
  margin-bottom: 12px;
  font-weight: 600;
}}

/* 1단계: 1분 족집게 강의 & 이론 설명 박스 */
.lecture-step-box {{
  background: linear-gradient(135deg, rgba(88, 28, 135, 0.24) 0%, rgba(15, 23, 42, 0.9) 100%);
  border: 1px solid rgba(192, 132, 252, 0.45);
  border-left: 5px solid #c084fc;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 14px;
}}
body.b4-paper-mode .lecture-step-box {{
  background: #efe9f7;
  border-color: #7e22ce;
}}
.lecture-step-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(192, 132, 252, 0.25);
  font-size: 0.88rem;
  font-weight: 900;
  color: #e9d5ff;
}}
body.b4-paper-mode .lecture-step-header {{
  color: #581c87;
}}
.lecture-summary-text {{
  font-size: calc(0.95rem * var(--font-scale));
  line-height: 1.72;
  color: #f1f5f9;
  margin-bottom: 10px;
  font-weight: 500;
}}
body.b4-paper-mode .lecture-summary-text {{
  color: #1f2937;
}}
.lecture-point-bar {{
  background: rgba(251, 191, 36, 0.13);
  border: 1px solid rgba(251, 191, 36, 0.4);
  border-radius: 6px;
  padding: 8px 12px;
  font-size: calc(0.9rem * var(--font-scale));
  font-weight: 800;
  color: #fde047;
}}
body.b4-paper-mode .lecture-point-bar {{
  background: #fef3c7;
  color: #92400e;
  border-color: #d97706;
}}

/* 2단계: 실전 사례 문제 & 작성 방법 발문 박스 */
.problem-step-box {{
  background: linear-gradient(180deg, rgba(30, 58, 138, 0.22) 0%, rgba(11, 18, 32, 0.95) 100%);
  border: 1px solid rgba(56, 189, 248, 0.4);
  border-left: 5px solid var(--accent-blue);
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 14px;
}}
body.b4-paper-mode .problem-step-box {{
  background: #eef4fb;
  border-color: #1e40af;
}}
.problem-step-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(56, 189, 248, 0.25);
  font-size: 0.88rem;
  font-weight: 900;
  color: #7dd3fc;
}}
body.b4-paper-mode .problem-step-header {{
  color: #1e3a8a;
}}
.problem-passage-text {{
  background: rgba(7, 11, 20, 0.7);
  border: 1px solid #1e3a5f;
  border-radius: 6px;
  padding: 11px 14px;
  font-size: calc(0.92rem * var(--font-scale));
  line-height: 1.7;
  color: #e2e8f0;
  white-space: pre-line;
  margin-bottom: 10px;
}}
body.b4-paper-mode .problem-passage-text {{
  background: #ffffff;
  color: #111827;
  border-color: #9ca3af;
}}
.problem-asks-list {{
  background: rgba(16, 185, 129, 0.08);
  border: 1px dashed rgba(16, 185, 129, 0.45);
  border-radius: 6px;
  padding: 9px 14px;
  font-size: calc(0.88rem * var(--font-scale));
  line-height: 1.65;
  color: #a7f3d0;
  font-weight: 700;
}}
body.b4-paper-mode .problem-asks-list {{
  background: #ecfdf5;
  color: #065f46;
  border-color: #059669;
}}
.lbl-subq-caption {{
  font-size: calc(0.81rem * var(--font-scale));
  color: #7dd3fc;
  font-weight: 700;
  margin-bottom: 3px;
  padding-left: 4px;
}}
body.b4-paper-mode .lbl-subq-caption {{
  color: #1e40af;
}}

.passage-wrapper {{
  background: var(--bg-passage);
  border: 1px solid var(--border-kice);
  border-left: 4px solid var(--accent-blue);
  border-radius: 6px;
  padding: 14px 18px;
  margin-bottom: 14px;
  font-size: calc(0.94rem * var(--font-scale));
  line-height: 1.75;
  white-space: pre-line;
}}

.instructions-box {{
  background: rgba(0, 0, 0, 0.2);
  border: 1px dashed var(--border-kice);
  border-radius: 6px;
  padding: 12px 18px;
  margin-bottom: 14px;
  font-size: calc(0.88rem * var(--font-scale));
  line-height: 1.6;
  white-space: pre-line;
}}
body.b4-paper-mode .instructions-box {{
  background: #eae5d7;
}}
.instructions-box strong {{
  color: var(--accent-gold);
}}

/* 키워드 태그 */
.kw-tags-strip {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 14px;
  align-items: center;
}}
.kw-label-tag {{
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--accent-gold);
}}
.kw-pill {{
  font-size: calc(0.82rem * var(--font-scale));
  padding: 4px 10px;
  border-radius: 6px;
  background: #0f172a;
  border: 1px solid rgba(251, 191, 36, 0.35);
  color: #fde68a;
  font-weight: 700;
  transition: all 0.2s;
}}
body.b4-paper-mode .kw-pill {{
  background: #dbd4c0;
  color: #78350f;
  border-color: #b45309;
}}
.kw-pill.detected {{
  background: rgba(16, 185, 129, 0.25);
  border-color: var(--accent-emerald);
  color: #6ee7b7;
  font-weight: 900;
  box-shadow: 0 0 8px rgba(16, 185, 129, 0.35);
}}

/* ================= 1줄씩 손가락으로 보고 바로 따라치기 박스 ================= */
.line-by-line-box {{
  background: #09101d;
  border: 1px solid #1e3a5f;
  border-radius: 8px;
  padding: 10px 12px;
  margin-bottom: 12px;
}}
body.b4-paper-mode .line-by-line-box {{
  background: #f5f0e4;
  border-color: #8c826e;
}}
.lbl-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  padding-bottom: 5px;
  border-bottom: 1px solid var(--border-kice);
  font-size: 0.84rem;
  font-weight: 800;
  color: var(--accent-blue);
}}
.lbl-row {{
  margin-bottom: 6px;
}}
.lbl-row:last-child {{
  margin-bottom: 0;
}}
.lbl-target-line {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  font-size: max(16px, calc(1.02rem * var(--font-scale)));
  font-weight: 600;
  letter-spacing: 0px;
  word-spacing: 0px;
  font-variant-ligatures: none;
  line-height: 1.35;
  color: #fef08a;
  margin-bottom: 2px;
  padding: 5px 12px;
  background: rgba(251, 191, 36, 0.08);
  border: 1px solid rgba(251, 191, 36, 0.22);
  border-left: 3px solid var(--accent-gold);
  border-radius: 5px;
  font-family: 'JetBrains Mono', 'Noto Sans KR', monospace;
  transition: filter 0.2s;
}}
.lbl-target-line.masked-hint {{
  filter: blur(7px);
  cursor: pointer;
}}
.lbl-target-line.masked-hint:hover {{
  filter: blur(0);
}}
.kw-blank-slot {{
  display: inline;
  background: rgba(56, 189, 248, 0.22);
  color: transparent;
  border-bottom: 2px dashed #38bdf8;
  border-radius: 3px;
  cursor: pointer;
  user-select: none;
  transition: all 0.18s;
}}
.kw-blank-slot.chosung-mode {{
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.16);
  font-weight: 800;
}}
.kw-blank-slot:hover,
.kw-blank-slot.revealed {{
  color: #fef08a !important;
  background: rgba(251, 191, 36, 0.25);
  border-bottom: 2px solid var(--accent-gold);
}}
.kw-blank-slot.solved {{
  color: #6ee7b7 !important;
  background: rgba(16, 185, 129, 0.28);
  border-bottom: 2px solid #10b981;
}}
.btn-line-mini {{
  background: rgba(30, 41, 59, 0.85);
  border: 1px solid #334155;
  color: #94a3b8;
  font-size: 0.7rem;
  padding: 1px 5px;
  border-radius: 4px;
  cursor: pointer;
  line-height: 1.2;
}}
.btn-line-mini:hover {{
  background: #38bdf8;
  color: #000;
  border-color: #38bdf8;
}}
.broadcast-select {{
  background: #131c2e;
  color: #fde68a;
  border: 1px solid rgba(251, 191, 36, 0.45);
  border-radius: 5px;
  padding: 4px 8px;
  font-size: 0.76rem;
  font-weight: 700;
  cursor: pointer;
  outline: none;
}}
.btn-kw-blank-main {{
  background: rgba(16, 185, 129, 0.16) !important;
  border: 1px solid #10b981 !important;
  color: #6ee7b7 !important;
  font-weight: 800 !important;
}}
.btn-kw-blank-main.active {{
  background: #10b981 !important;
  color: #051b11 !important;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);
}}
body.b4-paper-mode .lbl-target-line {{
  color: #78350f;
  background: rgba(180, 83, 9, 0.1);
}}
.lbl-input-wrap {{
  display: flex;
  align-items: center;
  gap: 8px;
}}
.lbl-input {{
  flex: 1;
  background: #050a14;
  border: 1px solid #283a58;
  border-left: 3px solid var(--accent-blue);
  border-radius: 5px;
  padding: 5px 12px;
  color: #ffffff;
  font-size: max(16px, calc(1.02rem * var(--font-scale)));
  font-weight: 600;
  letter-spacing: 0px;
  word-spacing: 0px;
  font-variant-ligatures: none;
  line-height: 1.35;
  font-family: 'JetBrains Mono', 'Noto Sans KR', monospace;
  outline: none;
  transition: all 0.15s;
}}
.lbl-input::placeholder {{
  color: rgba(148, 163, 184, 0.28);
  font-weight: 600;
  letter-spacing: 0px;
}}
body.b4-paper-mode .lbl-input {{
  background: #ffffff;
  color: #111827;
  border-color: #9ca3af;
}}
.lbl-input:focus {{
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
}}
.lbl-input.line-ok {{
  border-color: var(--accent-emerald);
  background: rgba(16, 185, 129, 0.08);
}}
.lbl-char-badge {{
  font-size: 0.78rem;
  font-weight: 800;
  min-width: 95px;
  text-align: center;
  padding: 6px 8px;
  border-radius: 6px;
  background: #162033;
  color: #94a3b8;
  font-family: 'JetBrains Mono', monospace;
}}
body.b4-paper-mode .lbl-char-badge {{
  background: #dbd4c0;
  color: #374151;
}}
.lbl-char-badge.ok {{
  background: rgba(16, 185, 129, 0.2);
  color: var(--accent-emerald);
  border: 1px solid var(--accent-emerald);
}}
.lbl-char-badge.over {{
  background: rgba(244, 63, 94, 0.2);
  color: var(--accent-rose);
  border: 1px solid var(--accent-rose);
}}

/* 족집게 퀴즈 & 핵심키워드 손가락 타이핑 박스 */
.cases8-box {{
  background: linear-gradient(180deg, rgba(16, 185, 129, 0.07) 0%, rgba(15, 23, 42, 0.7) 100%);
  border: 1px solid rgba(16, 185, 129, 0.35);
  border-radius: 8px;
  padding: 12px 14px;
  margin-bottom: 14px;
}}
body.b4-paper-mode .cases8-box {{
  background: #ede7d6;
  border-color: #047857;
}}
.cases8-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(16, 185, 129, 0.25);
  font-size: 0.85rem;
  font-weight: 800;
  color: #34d399;
}}
body.b4-paper-mode .cases8-header {{
  color: #047857;
}}
.cases8-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}}
.case8-item {{
  background: rgba(9, 14, 26, 0.88);
  border: 1px solid #1e293b;
  border-left: 4px solid var(--accent-gold);
  border-radius: 8px;
  padding: 11px 14px;
  transition: all 0.15s;
}}
body.b4-paper-mode .case8-item {{
  background: #f8f5ec;
  border-color: #b5ab96;
}}
.case8-item.solved,
.case8-item.case-ok {{
  border-color: var(--accent-emerald);
  border-left: 5px solid var(--accent-emerald);
  background: rgba(16, 185, 129, 0.12);
}}
.case8-q-row {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: calc(0.9rem * var(--font-scale));
  color: #e2e8f0;
  margin-bottom: 8px;
  font-weight: 700;
}}
.case8-target-ans {{
  font-size: calc(0.9rem * var(--font-scale));
  font-weight: 800;
  color: #fde047;
  background: rgba(251, 191, 36, 0.14);
  border: 1px solid rgba(251, 191, 36, 0.35);
  padding: 4px 10px;
  border-radius: 5px;
}}
body.b4-paper-mode .case8-q-row {{
  color: #1f2937;
}}
body.b4-paper-mode .case8-target-ans {{
  color: #78350f;
  background: rgba(180, 83, 9, 0.14);
}}
.case8-ans-row {{
  display: flex;
  align-items: center;
  gap: 8px;
}}
.case8-target {{
  font-size: calc(0.9rem * var(--font-scale));
  font-weight: 800;
  color: #fef08a;
  background: rgba(251, 191, 36, 0.12);
  border: 1px solid rgba(251, 191, 36, 0.35);
  padding: 5px 10px;
  border-radius: 5px;
}}
body.b4-paper-mode .case8-target {{
  color: #78350f;
  background: rgba(180, 83, 9, 0.12);
}}
.case8-input {{
  display: block;
  width: 100%;
  background: #050a14;
  border: 1px solid #283a58;
  border-left: 3px solid var(--accent-blue);
  border-radius: 6px;
  padding: 9px 14px;
  color: #fff;
  font-size: calc(0.96rem * var(--font-scale));
  font-weight: 700;
  font-family: 'JetBrains Mono', 'Noto Sans KR', monospace;
  outline: none;
}}
body.b4-paper-mode .case8-input {{
  background: #fff;
  color: #111827;
  border-color: #9ca3af;
}}
.case8-input:focus {{
  border-color: var(--accent-blue);
}}
.case8-input.match {{
  border-color: var(--accent-emerald);
  color: #6ee7b7;
}}

.quiz-typing-box {{
  margin-top: 12px;
  padding: 12px 16px;
  background: rgba(56, 189, 248, 0.06);
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 8px;
}}
.quiz-q-text {{
  font-size: calc(0.92rem * var(--font-scale));
  font-weight: 700;
  color: #e2e8f0;
  margin-bottom: 8px;
}}
body.b4-paper-mode .quiz-q-text {{
  color: #1f2937;
}}
.quiz-a-row {{
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}}
.quiz-target-badge {{
  background: rgba(251, 191, 36, 0.18);
  border: 1px solid var(--accent-gold);
  color: #fef08a;
  font-weight: 800;
  font-size: calc(0.9rem * var(--font-scale));
  padding: 6px 12px;
  border-radius: 6px;
}}
body.b4-paper-mode .quiz-target-badge {{
  color: #78350f;
  background: rgba(180, 83, 9, 0.15);
}}
.quiz-input {{
  flex: 1;
  min-width: 220px;
  background: #050a14;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 7px 12px;
  color: #fff;
  font-size: calc(0.95rem * var(--font-scale));
  font-weight: 700;
}}
body.b4-paper-mode .quiz-input {{
  background: #fff;
  color: #111827;
}}
.quiz-input.match {{
  border-color: var(--accent-emerald);
  background: rgba(16, 185, 129, 0.15);
  color: #6ee7b7;
}}

/* 좌우 2분할 실전 B4 답안지 */
.sheet-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  align-items: stretch;
}}

@media (max-width: 1024px) {{
  .sheet-grid {{
    grid-template-columns: 1fr;
  }}
}}

.sheet-col {{
  display: flex;
  flex-direction: column;
}}

.sheet-col-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-sub);
}}

.b4-typing-sheet {{
  width: 100%;
  flex: 1;
  min-height: 170px;
  background-color: #070d18;
  background-image: linear-gradient(to bottom, transparent 39px, rgba(56, 189, 248, 0.38) 40px);
  background-size: 100% 40px;
  background-attachment: local;
  border: 1px solid #1e3a5f;
  border-radius: 6px;
  padding: 0 16px;
  color: #f8fafc;
  font-size: calc(1.05rem * var(--font-scale));
  font-family: 'JetBrains Mono', 'Noto Sans KR', monospace;
  line-height: 40px;
  resize: vertical;
  outline: none;
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.5);
  transition: border-color 0.2s, box-shadow 0.2s;
}}
body.b4-paper-mode .b4-typing-sheet {{
  background-color: #faf8f3;
  background-image: linear-gradient(to bottom, transparent 39px, rgba(30, 58, 138, 0.4) 40px);
  border-color: #8c826e;
  color: #111827;
  box-shadow: inset 0 1px 4px rgba(0,0,0,0.15);
}}
.b4-typing-sheet:focus {{
  border-color: var(--accent-blue);
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
}}
.b4-typing-sheet.error-overflow {{
  border-color: var(--accent-rose) !important;
}}

.line-status-chip {{
  font-size: 0.75rem;
  font-weight: 700;
  display: inline-flex;
  gap: 6px;
  align-items: center;
  flex-wrap: wrap;
}}
.chip-item {{
  padding: 1px 6px;
  border-radius: 3px;
  background: #1e293b;
  color: #94a3b8;
}}
body.b4-paper-mode .chip-item {{
  background: #dbd4c0;
  color: #374151;
}}
.chip-item.perfect {{
  background: rgba(16, 185, 129, 0.2);
  color: var(--accent-emerald);
  border: 1px solid var(--accent-emerald);
}}
.chip-item.overflow {{
  background: rgba(244, 63, 94, 0.25);
  color: var(--accent-rose);
  border: 1px solid var(--accent-rose);
}}

.b4-answer-sheet {{
  background-color: #091322;
  background-image: linear-gradient(to bottom, transparent 39px, rgba(251, 191, 36, 0.3) 40px);
  background-size: 100% 40px;
  background-attachment: local;
  border: 1px solid #1e3a5f;
  border-radius: 6px;
  padding: 0 16px;
  color: #fef08a;
  font-size: calc(1.05rem * var(--font-scale));
  font-family: 'JetBrains Mono', 'Noto Sans KR', monospace;
  line-height: 40px;
  white-space: pre-line;
  flex: 1;
  user-select: text;
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.5);
}}
body.b4-paper-mode .b4-answer-sheet {{
  background-color: #faf5eb;
  background-image: linear-gradient(to bottom, transparent 39px, rgba(180, 83, 9, 0.35) 40px);
  border-color: #8c826e;
  color: #92400e;
  box-shadow: inset 0 1px 4px rgba(0,0,0,0.15);
}}
.b4-answer-sheet.masked {{
  filter: blur(5px);
  user-select: none;
  cursor: pointer;
}}

.btn-sheet-mini {{
  background: #1e293b;
  border: 1px solid #334155;
  color: #94a3b8;
  font-size: 0.72rem;
  padding: 2px 7px;
  border-radius: 4px;
  cursor: pointer;
}}
body.b4-paper-mode .btn-sheet-mini {{
  background: #e2dcd0;
  color: #1f2937;
  border-color: #9ca3af;
}}
.btn-sheet-mini:hover {{ background: #38bdf8; color: #000; }}

.scoring-eval-bar {{
  margin-top: 10px;
  padding: 8px 12px;
  background: #0d1422;
  border: 1px solid #1e293b;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
}}
body.b4-paper-mode .scoring-eval-bar {{
  background: #eae4d5;
  border-color: #8c826e;
}}
.eval-score-text {{
  font-weight: 800;
  color: var(--accent-gold);
}}

#report-modal {{
  display: none;
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 9999;
  justify-content: center;
  align-items: center;
  padding: 20px;
}}
.modal-box {{
  background: #131c2e;
  border: 2px solid #38bdf8;
  border-radius: 12px;
  max-width: 650px;
  width: 100%;
  padding: 24px;
  color: #f8fafc;
  box-shadow: 0 10px 40px rgba(0,0,0,0.8);
}}
.modal-title {{
  font-size: 1.25rem;
  font-weight: 800;
  color: #38bdf8;
  margin-bottom: 16px;
  border-bottom: 1px solid #22314d;
  padding-bottom: 10px;
}}
.report-row {{
  margin-bottom: 12px;
}}
.report-bar-wrap {{
  background: #0a0f1d;
  height: 12px;
  border-radius: 6px;
  overflow: hidden;
  margin-top: 4px;
}}
.report-bar-fill {{
  height: 100%;
  background: linear-gradient(90deg, #0284c7, #10b981);
  width: 0%;
  transition: width 0.5s ease;
}}

/* ================= 태블릿(아이패드·갤럭시탭) 및 모바일 완벽 대응 ================= */
@media (max-width: 1180px) {{
  .kice-exam-header {{
    position: static;
    padding: 10px 12px;
  }}
  .exam-main-title {{
    font-size: 1rem;
  }}
  .header-actions {{
    width: 100%;
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 6px;
    gap: 6px;
  }}
  .sub-bar, .kice55-filter-bar, .nav-strip {{
    padding: 8px 12px;
  }}
  .period-tabs, .kice55-filter-bar, .nav-strip {{
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }}
  .btn-kice, .period-tab-btn, .k55-cat-btn, .filter-btn, .nav-pill, .btn-timer, .btn-asmr {{
    min-height: 38px;
    flex-shrink: 0;
    white-space: nowrap;
  }}
  .k55-search-input {{
    min-width: 220px;
    flex-shrink: 0;
  }}
  main {{
    padding: 12px;
  }}
  .q-card-head {{
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    padding: 12px 14px;
  }}
  .q-card-body {{
    padding: 12px 14px;
  }}
  .lbl-target-line {{
    font-size: 16px !important;
    padding: 5px 12px !important;
    letter-spacing: 0px !important;
    line-height: 1.35 !important;
    margin-bottom: 2px !important;
    word-break: keep-all;
    overflow-wrap: anywhere;
  }}
  .lbl-input-wrap {{
    flex-direction: row !important;
    align-items: center !important;
    gap: 6px !important;
  }}
  .lbl-char-badge {{
    min-width: 78px !important;
    padding: 4px 6px !important;
    font-size: 0.72rem !important;
    flex-shrink: 0;
  }}
  /* iOS/iPadOS Safari 입력창 포커스 시 자동 확대(Zoom) 방지 + 위쪽 정답 줄과 1:1 패딩/자간/줄간격 일치 */
  .lbl-input {{
    font-size: 16px !important;
    padding: 5px 12px !important;
    letter-spacing: 0px !important;
    line-height: 1.35 !important;
    min-height: 36px !important;
  }}
  .case8-input, .quiz-input, .b4-typing-sheet, .b4-answer-sheet, .k55-search-input, #pb-theme {{
    font-size: 16px !important;
    min-height: 44px;
  }}
  .sheet-grid {{
    grid-template-columns: 1fr !important;
  }}
  .modal-box {{
    width: 96vw !important;
    max-height: 90vh;
    padding: 16px !important;
  }}
  #ped-builder-modal div[style*="grid-template-columns:1fr 1fr"] {{
    grid-template-columns: 1fr !important;
  }}
}}

@media print {{
  body {{ background: #fff !important; color: #000 !important; }}
  .kice-exam-header, .sub-bar, .kice55-filter-bar, .nav-strip, .scoring-eval-bar, .header-actions, .btn-sheet-mini, #toast, #report-modal {{ display: none !important; }}
  main {{ max-width: 100% !important; margin: 0 !important; padding: 0 !important; }}
  .q-card {{ border: 2px solid #000 !important; box-shadow: none !important; margin-bottom: 20px !important; page-break-inside: avoid; }}
  .q-card-head {{ background: #f0f0f0 !important; color: #000 !important; border-bottom: 1px solid #000 !important; }}
  .b4-typing-sheet, .b4-answer-sheet {{ background: #fff !important; border: 1px solid #000 !important; color: #000 !important; }}
}}

#toast {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #10b981;
  color: #fff;
  padding: 10px 18px;
  border-radius: 6px;
  font-size: 0.88rem;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s, transform 0.3s;
  transform: translateY(10px);
  z-index: 9999;
}}
#toast.show {{ opacity: 1; transform: translateY(0); }}

/* [v6.5] 4대 실전 업그레이드 CSS (D-Day, 오늘 미션, 칼채점, 태블릿 터치 칩) */
.dday-seal {{
  background: linear-gradient(135deg, #e11d48, #be123c);
  color: #fff;
  font-size: 0.78rem;
  font-weight: 900;
  padding: 4px 10px;
  border-radius: 4px;
  border: 1px solid #fda4af;
  letter-spacing: 0.4px;
}}
.daily-mission-pill {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(16, 185, 129, 0.14);
  border: 1px solid rgba(16, 185, 129, 0.45);
  color: #6ee7b7;
  font-size: 0.8rem;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 6px;
}}
.daily-mission-bar-wrap {{
  width: 64px;
  height: 8px;
  background: #0f172a;
  border-radius: 99px;
  overflow: hidden;
  border: 1px solid rgba(16, 185, 129, 0.4);
}}
.daily-mission-bar-fill {{
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #10b981, #fde047);
  transition: width 0.3s ease;
}}
.touch-chip-tray {{
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid rgba(56, 189, 248, 0.38);
  border-radius: 8px;
  padding: 12px 14px;
  margin-bottom: 14px;
}}
.touch-chip-header {{
  font-size: 0.84rem;
  font-weight: 800;
  color: #7dd3fc;
  margin-bottom: 8px;
}}
.touch-chip-list {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}}
.touch-chip-btn {{
  background: #0f172a;
  border: 1.5px solid #38bdf8;
  color: #e0f2fe;
  font-size: calc(0.9rem * var(--font-scale));
  font-weight: 800;
  padding: 8px 14px;
  border-radius: 999px;
  cursor: pointer;
  min-height: 40px;
  transition: all 0.15s;
}}
.touch-chip-btn:hover {{
  background: rgba(56, 189, 248, 0.22);
  transform: translateY(-1px);
}}
.touch-chip-btn.used {{
  background: rgba(16, 185, 129, 0.25);
  border-color: #10b981;
  color: #6ee7b7;
  text-decoration: line-through;
  opacity: 0.65;
}}
.touch-chip-btn.trap-shake {{
  background: rgba(244, 63, 94, 0.25);
  border-color: #f43f5e;
  color: #fda4af;
}}
.kal-rubric-bar {{
  margin-top: 8px;
  padding: 8px 12px;
  background: rgba(15, 23, 42, 0.85);
  border: 1px solid #334155;
  border-left: 4px solid #fbbf24;
  border-radius: 6px;
  font-size: 0.84rem;
  font-weight: 700;
  color: #fde68a;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}}
body.b4-paper-mode .kal-rubric-bar {{
  background: #f5f0e4;
  color: #78350f;
  border-color: #b45309;
}}

/* [v7.0] 손글씨 사인펜 캔버스 패드 & 모의고사 배너 */
.hw-pad-wrap {{
  display: none;
  margin-top: 12px;
  background: #faf8f3;
  border: 2px solid #8c826e;
  border-radius: 8px;
  padding: 10px 12px;
}}
.hw-pad-wrap.open {{
  display: block;
}}
.hw-pad-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  color: #1e3a8a;
  font-size: 0.84rem;
  font-weight: 800;
}}
.hw-canvas {{
  width: 100%;
  height: 200px;
  display: block;
  background-color: #fffdf7;
  background-image: linear-gradient(to bottom, transparent 49px, rgba(30, 58, 138, 0.35) 50px);
  background-size: 100% 50px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  touch-action: none;
  cursor: crosshair;
}}
.mini-mock-banner {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  background: linear-gradient(90deg, rgba(225, 29, 72, 0.2), rgba(245, 158, 11, 0.2));
  border: 2px solid #f43f5e;
  border-radius: 10px;
  padding: 12px 16px;
  margin-bottom: 16px;
  color: #ffe4e6;
  font-weight: 800;
}}
.weak-item-card {{
  background: #0f172a;
  border: 1px solid #334155;
  border-left: 4px solid #f43f5e;
  border-radius: 8px;
  padding: 10px 14px;
  margin-bottom: 10px;
}}

/* [v7.5] 100% 실전 블라인드 모드 & 라디오 낭독 하이라이트 */
.q-card.radio-active {{
  border-color: #34d399 !important;
  box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.35), 0 10px 30px rgba(16, 185, 129, 0.25) !important;
}}
body.blind-exam-mode .concept-banner,
body.blind-exam-mode .lecture-step-box,
body.blind-exam-mode .kw-tags-strip,
body.blind-exam-mode .cases8-box,
body.blind-exam-mode .lbl-target-line,
body.blind-exam-mode .quiz-typing-box,
body.blind-exam-mode .b4-answer-sheet,
body.blind-exam-mode .touch-chip-tray {{
  display: none !important;
}}
</style>
</head>
<body>

<header class="kice-exam-header">
  <div class="header-inner">
    <div class="brand-section">
      <span class="dday-seal" id="dday-seal">D-12 (11.28 결전)</span>
      <span class="kice-seal">v7.5 최종완전체</span>
      <h1 class="exam-main-title">2027 임용 만점 템플릿 & 55개 KICE 핵심키워드 4줄 정답 타이핑</h1>
      <span class="examinee-tag">수험자: 변귀섭 대표님</span>
    </div>

    <div class="timer-container">
      <span class="timer-label">타이머</span>
      <span class="timer-digits" id="timer-display">30:00</span>
      <button class="btn-timer" onclick="toggleTimer()" id="btn-timer-toggle">일시정지</button>
      <button class="btn-timer" onclick="setCustomTimer(5)" style="color:#fde047; border-color:#f59e0b;" title="ADHD 초단기 5분 타임어택">⚡5분</button>
      <button class="btn-timer" onclick="setCustomTimer(10)" title="10분 집중 스프린트">10분</button>
      <button class="btn-timer" onclick="setCustomTimer(60)" title="실전 1교시/2교시 60분">60분</button>
      <span class="wpm-badge" id="wpm-display">0 타/분</span>
      <span class="wpm-badge" id="combo-display" style="color:#fbbf24; border-color:#f59e0b; background:rgba(245,158,11,0.15);">🔥 0 COMBO</span>
      <button class="btn-asmr" id="btn-asmr" onclick="toggleASMR()">🔔 시험장 소리·멘트 OFF</button>
      <select class="broadcast-select" id="exam-broadcast-select" onchange="playSelectedBroadcast(this.value)">
        <option value="">📢 시험장 방송 멘트 선택...</option>
        <option value="START">🔔 [본령] 시험 시작 타종 & 방송 멘트</option>
        <option value="PRE5">🔔 [예비령] 시험 시작 5분 전 유의사항 멘트</option>
        <option value="WARN10">🔔 [예고령] 시험 종료 10분 전 점검 멘트</option>
        <option value="END">🔔 [종료령] 시험 종료 타종 & 제출 멘트</option>
        <option value="CHEER">🏆 [특별방송] 변귀섭 대표님 최종합격 멘트</option>
      </select>
    </div>

    <div class="font-scale-ctrl">
      <button class="btn-font-scale" onclick="adjustFont(-0.05)">A-</button>
      <span style="font-size:0.75rem; color:var(--text-muted);">글꼴</span>
      <button class="btn-font-scale" onclick="adjustFont(0.05)">A+</button>
    </div>

    <div class="round-selector-group">
      <span style="font-size:0.75rem; color:var(--accent-gold); font-weight:800; margin-right:2px;">오늘의 회독:</span>
      <button class="round-btn active" id="round-btn-1" onclick="switchPracticeRound(1)">1회독</button>
      <button class="round-btn" id="round-btn-2" onclick="switchPracticeRound(2)">2회독</button>
      <button class="round-btn" id="round-btn-3" onclick="switchPracticeRound(3)">3회독</button>
    </div>

    <div class="header-actions">
      <button class="btn-kice" onclick="toggleLectureProblemMode()" id="btn-lecture-mode" style="background:rgba(192,132,252,0.18); border-color:#c084fc; color:#f3e8ff; font-weight:800;">🎓 강의+문제 ON</button>
      <button class="btn-kice" onclick="toggleBlindExamMode()" id="btn-blind-exam" style="border-color:#f43f5e; color:#fecdd3; font-weight:800;" title="강의·정답·힌트를 모두 숨기고 오직 문제와 빈 4줄 입력창만으로 실전 백지 테스트를 합니다">🙈 실전 블라인드 OFF</button>
      <button class="btn-kice btn-kw-blank-main" onclick="toggleKeywordBlankMode()" id="btn-kw-blank">🎯 핵심키워드 빈칸 만들기</button>
      <button class="btn-kice" onclick="toggleChosungHintMode()" id="btn-chosung-hint" style="border-color:#38bdf8; color:#7dd3fc; font-weight:800;" title="빈칸 안에 한글 초성(ㄱㄴㄷ) 힌트를 표시하여 0.5초 만에 연상 인출합니다">🔤 초성 힌트(ㄱㄴㄷ) 보기</button>
      <button class="btn-kice" onclick="toggleTouchChipMode()" id="btn-touch-chip" style="border-color:#38bdf8; color:#bae6fd; font-weight:800;" title="태블릿·모바일에서 타이핑 대신 키워드 칩을 터치해 빈칸을 조립합니다">👆 터치 조립 모드 OFF</button>
      <button class="btn-kice" onclick="toggleCases8Mode()" id="btn-cases8-mode" style="border-color:#38bdf8; color:#38bdf8; font-weight:800;">⚡ 경우의 수 8개 ON</button>
      <button class="btn-kice" onclick="toggleSingleFocusMode()" id="btn-single-focus" style="border-color:#c084fc; color:#e9d5ff; font-weight:800;">🔍 1문제 집중 모드 OFF</button>
      <button class="btn-kice" onclick="toggleRadioMode()" id="btn-radio" style="border-color:#34d399; color:#6ee7b7; font-weight:800;">📻 연속 자동낭독 OFF</button>
      <button class="btn-kice" onclick="toggleMiniMockExam()" id="btn-mini-mock" style="border-color:#f43f5e; color:#fda4af; font-weight:800;">🎲 실전 10문제 모의고사</button>
      <button class="btn-kice" onclick="openWeaknessModal()" style="border-color:#fb7185; color:#fecdd3; font-weight:800;">🚨 내 약점 1분 족보</button>
      <button class="btn-kice" onclick="openPedBuilderModal()" style="border-color:#fbbf24; color:#fde047; font-weight:800;">🏛️ 1교시 논술 자동조립기</button>
      <button class="btn-kice" onclick="togglePaperMode()" id="btn-paper-mode">B4 시험지 모드</button>
      <button class="btn-kice" onclick="toggleAllMasks()" id="btn-toggle-all">백지연습(정답 가리기)</button>
      <button class="btn-kice" onclick="shuffleCurrentPeriod()" id="btn-shuffle">랜덤 셔플</button>
      <button class="btn-kice" onclick="openReportModal()">📊 100문항 성적표</button>
      <button class="btn-kice" onclick="window.print()">B4 인쇄</button>
      <button class="btn-kice danger" onclick="clearCurrentAnswers()">현재 탭 비우기</button>
      <button class="btn-kice danger" onclick="clearAllPracticeRoundAnswers()">★ 오늘 전체 지우기</button>
      <button class="btn-kice accent" onclick="exportAnswers()">답안 제출 (TXT)</button>
    </div>
  </div>
</header>

<div class="sub-bar">
  <div class="period-tabs">
    <button class="period-tab-btn highlight-tab active" id="tab-btn-KICE55" onclick="switchPeriod('KICE55')">🔥 11.28 결전: 교육학 + 전공 45선 (총 65선)</button>
    <button class="period-tab-btn highlight-tab" id="tab-btn-TEMPLATE" onclick="switchPeriod('TEMPLATE')">🏛️ 내 교육학 플랫폼(서론·이처럼·결론) & 만능틀 (6선)</button>
    <button class="period-tab-btn" id="tab-btn-PED" onclick="switchPeriod('PED')">1교시 교육학 실전 (16제)</button>
    <button class="period-tab-btn" id="tab-btn-A" onclick="switchPeriod('A')">2교시 전공 A형 실전 (12제)</button>
    <button class="period-tab-btn" id="tab-btn-B" onclick="switchPeriod('B')">3교시 전공 B형 실전 (11제)</button>
  </div>
  <div class="filter-group">
    <div class="daily-mission-pill" id="daily-mission-pill" title="오늘 10문제를 완료하면 축하 팡파르가 울립니다!">
      <span>🎯 오늘 미션: <strong id="daily-mission-count">0</strong>/10</span>
      <div class="daily-mission-bar-wrap"><div class="daily-mission-bar-fill" id="daily-mission-bar"></div></div>
    </div>
    <button class="filter-btn" id="btn-incomplete-filter" onclick="toggleIncompleteFilter()" style="border-color:#f43f5e; color:#fda4af;">🔥 미완료 문항만 보기</button>
    <button class="filter-btn" id="btn-bookmark-filter" onclick="toggleBookmarkFilter()">북마크(★) 모아보기</button>
    <button class="filter-btn" onclick="exportWrongNotes()">단권화 노트 다운</button>
    <button class="filter-btn" onclick="exportProgressBackup()" style="border-color:#38bdf8; color:#7dd3fc;" title="PC·태블릿 간 학습 진도를 파일로 백업합니다">💾 진도 백업</button>
    <button class="filter-btn" onclick="document.getElementById('backup-file-input').click()" style="border-color:#a78bfa; color:#ddd6fe;" title="백업한 진도 파일을 불러와 이어서 학습합니다">📂 진도 불러오기</button>
    <input type="file" id="backup-file-input" accept=".json" style="display:none;" onchange="importProgressBackup(event)">
    <div class="status-badge">
      <span class="badge-count" id="progress-count" style="font-weight:900; color:var(--accent-emerald);">0 완료</span>
    </div>
  </div>
</div>

<!-- 55개 KICE 핵심키워드 전용 영역 필터 및 실시간 검색 -->
<div class="kice55-filter-bar" id="kice55-filter-bar">
  <button class="k55-cat-btn active" onclick="setK55Category('ALL', this)">전체 65선 (01~65)</button>
  <button class="k55-cat-btn" style="border-color:#fde047; color:#fde047; font-weight:900;" onclick="setK55Category('CORE55', this)">🔥 11.28 압축 55선 (교육학10 + 전공45)</button>
  <button class="k55-cat-btn" style="border-color:#f43f5e; color:#fda4af; font-weight:900;" onclick="setK55Category('PED10', this)">🎯 11.28 교육학 0순위 압축 10선</button>
  <button class="k55-cat-btn" onclick="setK55Category('PED20', this)">1교시 교육학 20선 + 내 교육학 플랫폼 (01~20)</button>
  <button class="k55-cat-btn" style="border-color:#fbbf24; color:#fde047;" onclick="switchPeriod('TEMPLATE')">🏛️ 내 교육학 플랫폼(서론·이처럼·결론) 집중연습</button>
  <button class="k55-cat-btn" onclick="setK55Category('COUNSEL35', this)">2·3교시 전공상담 45선 (21~65)</button>
  <button class="k55-cat-btn" onclick="setK55Category('DSM-5-TR 감별진단', this)">DSM-5-TR 감별 (14선)</button>
  <button class="k55-cat-btn" onclick="setK55Category('심리검사', this)">심리검사 (6선)</button>
  <button class="k55-cat-btn" onclick="setK55Category('가족치료', this)">가족치료 (4선)</button>
  <button class="k55-cat-btn" onclick="setK55Category('상담이론', this)">상담이론·집단·성격 (15선)</button>
  <button class="k55-cat-btn" onclick="setK55Category('진로·다문화·위기', this)">진로·다문화·윤리·위기 (6선)</button>
  <input type="text" class="k55-search-input" id="k55-search-input" placeholder="🔍 KICE 키워드·학자명·장애명 즉시 검색..." oninput="renderNav(); renderCards(); loadSavedAnswers();">
</div>

<div class="nav-strip" id="nav-strip"></div>

<main id="exam-cards-container"></main>

<div id="report-modal">
  <div class="modal-box">
    <div class="modal-title">🏆 2027학년도 11.28 임용 결전 종합 성취도 리포트</div>
    <div id="report-content"></div>
    <div style="text-align: right; margin-top: 20px;">
      <button class="btn-kice accent" onclick="closeReportModal()">확인 완료</button>
    </div>
  </div>
</div>

<!-- 1교시 교육학 논술 만능 플랫폼 1초 자동조립기 모달 -->
<div id="ped-builder-modal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:9999; justify-content:center; align-items:center; padding:20px;">
  <div class="modal-box" style="max-width:920px; max-height:92vh; overflow-y:auto; border-color:#10b981;">
    <div class="modal-title" style="color:#34d399; display:flex; justify-content:space-between; align-items:center;">
      <span>🏛️ [변귀섭 대표님 전용] 1교시 교육학 논술 만능 플랫폼 1초 자동조립기</span>
      <button class="btn-sheet-mini" onclick="closePedBuilderModal()">닫기 ✕</button>
    </div>
    <div style="font-size:0.86rem; color:#94a3b8; margin-bottom:12px;">
      문제지의 <strong>(대주제)</strong>와 4대 영역 출제 이론을 선택하면, 대표님의 시그니처 서론(<code>미래 교육환경 속에서 ~ 화제가 대두되고 있다</code>) · 본론(<code>이처럼 교사가 ~</code>) · 결론(<code>든든한 버팀목이자 교육 안내자 및 성장 촉진자</code>)과 4줄 핵심 정답이 <strong>20점 만점 풀세트 논술문</strong>으로 즉시 결합됩니다!
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:14px;">
      <div style="grid-column:1 / -1;">
        <label style="font-size:0.8rem; color:#fde047; font-weight:800;">📌 시험지 (대주제) 입력:</label>
        <input type="text" id="pb-theme" value="학생 맞춤형 교육 혁신과 교사의 수석 역량" oninput="generatePedFullEssay()" style="width:100%; margin-top:4px; padding:8px 12px; background:#090d16; border:1px solid #10b981; border-radius:6px; color:#fff; font-weight:700;">
      </div>
      <div>
        <label style="font-size:0.78rem; color:#38bdf8; font-weight:800;">① 교육과정 영역 선택:</label>
        <select id="pb-sel-curr" onchange="generatePedFullEssay()" style="width:100%; margin-top:4px; padding:7px; background:#090d16; border:1px solid #334155; border-radius:6px; color:#fff;"></select>
      </div>
      <div>
        <label style="font-size:0.78rem; color:#38bdf8; font-weight:800;">② 교육방법 영역 선택:</label>
        <select id="pb-sel-meth" onchange="generatePedFullEssay()" style="width:100%; margin-top:4px; padding:7px; background:#090d16; border:1px solid #334155; border-radius:6px; color:#fff;"></select>
      </div>
      <div>
        <label style="font-size:0.78rem; color:#38bdf8; font-weight:800;">③ 교육평가 영역 선택:</label>
        <select id="pb-sel-eval" onchange="generatePedFullEssay()" style="width:100%; margin-top:4px; padding:7px; background:#090d16; border:1px solid #334155; border-radius:6px; color:#fff;"></select>
      </div>
      <div>
        <label style="font-size:0.78rem; color:#38bdf8; font-weight:800;">④ 교육행정 영역 선택:</label>
        <select id="pb-sel-adm" onchange="generatePedFullEssay()" style="width:100%; margin-top:4px; padding:7px; background:#090d16; border:1px solid #334155; border-radius:6px; color:#fff;"></select>
      </div>
    </div>
    <textarea id="pb-output" readonly style="width:100%; height:360px; background:#070b12; border:1px solid #10b981; border-radius:8px; padding:14px; color:#fde047; font-size:0.95rem; line-height:1.75; font-family:'Noto Sans KR', sans-serif;"></textarea>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px;">
      <span id="pb-char-info" style="font-size:0.84rem; color:#34d399; font-weight:800;">총 28줄 (서론 4줄 + 본론 20줄 + 결론 4줄)</span>
      <div style="display:flex; gap:8px;">
        <button class="btn-kice" style="border-color:#38bdf8; color:#38bdf8;" onclick="speakPedFullEssay()">🎧 완성된 논술문 전체 음성 듣기</button>
        <button class="btn-kice accent" onclick="copyPedFullEssay()">📋 완성된 논술문 복사</button>
      </div>
    </div>
  </div>
</div>

<!-- 시험장 직전 1분 내 약점 키워드 족보 모달 -->
<div id="weakness-modal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:9999; justify-content:center; align-items:center; padding:20px;">
  <div class="modal-box" style="max-width:860px; max-height:90vh; overflow-y:auto; border-color:#f43f5e;">
    <div class="modal-title" style="color:#fda4af; display:flex; justify-content:space-between; align-items:center;">
      <span>🚨 [시험장 직전 1분 벼락치기] 내가 자주 놓친 약점 키워드 족보</span>
      <button class="btn-sheet-mini" onclick="closeWeaknessModal()">닫기 ✕</button>
    </div>
    <div id="weakness-content" style="font-size:0.9rem; line-height:1.6;"></div>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:16px; flex-wrap:wrap; gap:8px;">
      <button class="btn-kice" style="border-color:#38bdf8; color:#38bdf8;" onclick="speakWeaknessList()">🎧 약점 키워드 연속 듣기</button>
      <div style="display:flex; gap:8px;">
        <button class="btn-kice danger" onclick="clearWeaknessLog()">약점 기록 초기화</button>
        <button class="btn-kice accent" onclick="closeWeaknessModal()">확인 완료</button>
      </div>
    </div>
  </div>
</div>

<div id="toast">알림</div>

<script>
const dataKICE55 = {json.dumps(kice55_data, ensure_ascii=False)};
const dataTEMPLATE = {json.dumps(templates_data, ensure_ascii=False)};
const dataPED = {json.dumps(data_ped, ensure_ascii=False)};
const dataA = {json.dumps(data_a, ensure_ascii=False)};
const dataB = {json.dumps(data_b, ensure_ascii=False)};

let currentPeriod = 'KICE55';
let currentK55Cat = 'ALL';
let allMasked = false;
let isPaperMode = false;
let isBlankMode = false;
let showCases8 = true;
let showOnlyBookmarks = false;
let showOnlyIncomplete = false;
let isSingleFocusMode = false;
let singleFocusIdx = 0;
let isRadioPlaying = false;
let radioIndex = 0;
let comboCount = 0;
let isShuffled = false;
let currentFontScale = 1.0;
let bookmarks = JSON.parse(localStorage.getItem('kice_bookmarks') || '{{}}');

let totalTypedChars = 0;
let typingStartTime = null;
let timerSeconds = 30 * 60;
let timerInterval = null;
let isTimerRunning = true;

let audioCtx = null;
let noiseNode = null;
let examHallTimer = null;
let isAsmrOn = false;

function incrementCombo() {{
  comboCount++;
  const el = document.getElementById('combo-display');
  if (el) {{
    el.textContent = `🔥 ${{comboCount}} COMBO!`;
    el.style.transform = 'scale(1.18)';
    setTimeout(() => {{ el.style.transform = 'scale(1)'; }}, 180);
  }}
}}

function ensureAudioCtx() {{
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  if (audioCtx.state === 'suspended') audioCtx.resume();
  return audioCtx;
}}

function playSuccessChime() {{
  incrementCombo();
  try {{
    const ctx = ensureAudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(587.33, ctx.currentTime);
    osc.frequency.setValueAtTime(880.00, ctx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.15, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.6);
  }} catch(e) {{}}
}}

function playMiniHitSound() {{
  incrementCombo();
  try {{
    const ctx = ensureAudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(659.25, ctx.currentTime);
    osc.frequency.setValueAtTime(987.77, ctx.currentTime + 0.06);
    gain.gain.setValueAtTime(0.10, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.25);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.25);
  }} catch(e) {{}}
}}

function playPenStrokeSound() {{
  if (!isAsmrOn) return;
  try {{
    const ctx = ensureAudioCtx();
    const dur = 0.035;
    const bufSize = Math.floor(ctx.sampleRate * dur);
    const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const data = buf.getChannelData(0);
    for (let i = 0; i < bufSize; i++) {{
      const env = Math.sin((i / bufSize) * Math.PI);
      data[i] = (Math.random() * 2 - 1) * 0.04 * env;
    }}
    const src = ctx.createBufferSource();
    src.buffer = buf;
    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.value = 2400 + Math.random() * 600;
    filter.Q.value = 1.8;
    src.connect(filter);
    filter.connect(ctx.destination);
    src.start();
  }} catch(e) {{}}
}}

function playPaperTurnSound() {{
  try {{
    const ctx = ensureAudioCtx();
    const dur = 0.38;
    const bufSize = Math.floor(ctx.sampleRate * dur);
    const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const data = buf.getChannelData(0);
    for (let i = 0; i < bufSize; i++) {{
      const env = Math.sin((i / bufSize) * Math.PI);
      data[i] = (Math.random() * 2 - 1) * 0.03 * env;
    }}
    const src = ctx.createBufferSource();
    src.buffer = buf;
    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(900, ctx.currentTime);
    filter.frequency.linearRampToValueAtTime(2200, ctx.currentTime + 0.2);
    filter.frequency.linearRampToValueAtTime(700, ctx.currentTime + dur);
    src.connect(filter);
    filter.connect(ctx.destination);
    src.start();
  }} catch(e) {{}}
}}

// 실제 임용고시 고사장 4음 차임벨 (딩~ 동~ 댕~ 동~ : G4 - B4 - D5 - G5)
function playExamChime(onDone) {{
  try {{
    const ctx = ensureAudioCtx();
    const notes = [392.00, 493.88, 587.33, 783.99];
    const startTimes = [0, 0.48, 0.96, 1.44];
    notes.forEach((freq, idx) => {{
      const t = ctx.currentTime + startTimes[idx];
      const osc = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc2.type = 'triangle';
      osc.frequency.setValueAtTime(freq, t);
      osc2.frequency.setValueAtTime(freq * 2, t);
      gain.gain.setValueAtTime(0.001, t);
      gain.gain.linearRampToValueAtTime(0.18, t + 0.03);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.95);
      osc.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);
      osc.start(t);
      osc2.start(t);
      osc.stop(t + 1.0);
      osc2.stop(t + 1.0);
    }});
    if (onDone) setTimeout(onDone, 2300);
  }} catch(e) {{
    if (onDone) onDone();
  }}
}}

const EXAM_BROADCAST_SCRIPTS = {{
  start: "안내 말씀 드립니다. 지금부터 2027학년도 공립 중등학교 교사 임용후보자 선정경쟁시험을 시작하겠습니다. 수험생 여러분께서는 문제지의 문항 수와 인쇄 상태를 확인하시고, B4 답안지 작성 규격에 맞추어 침착하게 답안을 작성해 주시기 바랍니다.",
  START: "안내 말씀 드립니다. 지금부터 2027학년도 공립 중등학교 교사 임용후보자 선정경쟁시험을 시작하겠습니다. 수험생 여러분께서는 문제지의 문항 수와 인쇄 상태를 확인하시고, B4 답안지 작성 규격에 맞추어 침착하게 답안을 작성해 주시기 바랍니다.",
  prep: "수험생 여러분께 안내 말씀 드립니다. 본령 타종 5분 전입니다. 수험표와 신분증을 책상 좌측 상단에 놓아주시고, 컴퓨터용 사인펜과 흑색 필기구 외의 물품은 가방에 넣어 정리해 주시기 바랍니다.",
  PRE5: "수험생 여러분께 안내 말씀 드립니다. 본령 타종 5분 전입니다. 수험표와 신분증을 책상 좌측 상단에 놓아주시고, 컴퓨터용 사인펜과 흑색 필기구 외의 물품은 가방에 넣어 정리해 주시기 바랍니다.",
  warn10: "안내 말씀 드립니다. 시험 종료 10분 전입니다. 수험생 여러분께서는 작성하신 답안지의 누락 여부와 글자 수 규격을 다시 한번 확인해 주시기 바랍니다.",
  WARN10: "안내 말씀 드립니다. 시험 종료 10분 전입니다. 수험생 여러분께서는 작성하신 답안지의 누락 여부와 글자 수 규격을 다시 한번 확인해 주시기 바랍니다.",
  end: "시험 종료령이 울렸습니다. 수험생 여러분께서는 즉시 필기구를 내려놓으시고, 답안지를 오른쪽에, 문제지를 왼쪽에 놓아주시기 바랍니다. 감독관의 지시가 있을 때까지 자리에서 일어나지 마십시오.",
  END: "시험 종료령이 울렸습니다. 수험생 여러분께서는 즉시 필기구를 내려놓으시고, 답안지를 오른쪽에, 문제지를 왼쪽에 놓아주시기 바랍니다. 감독관의 지시가 있을 때까지 자리에서 일어나지 마십시오.",
  cheer: "안내 말씀 드립니다. 수험번호 1번 변귀섭 대표님, 지금까지 손끝에 새긴 55개 KICE 핵심 키워드와 440개 경우의 수가 오늘 시험지에서 100퍼센트 그대로 출제됩니다. 끝까지 침착하게 작성하시어 2027학년도 인천 전문상담교사 최종 합격을 진심으로 축하드립니다.",
  CHEER: "안내 말씀 드립니다. 수험번호 1번 변귀섭 대표님, 지금까지 손끝에 새긴 55개 KICE 핵심 키워드와 440개 경우의 수가 오늘 시험지에서 100퍼센트 그대로 출제됩니다. 끝까지 침착하게 작성하시어 2027학년도 인천 전문상담교사 최종 합격을 진심으로 축하드립니다."
}};

function playSelectedBroadcast(val) {{
  if (!val) return;
  const script = EXAM_BROADCAST_SCRIPTS[val];
  if (!script) return;
  showToast('🔔 [고사장 방송] ' + script.slice(0, 42) + '...');
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  playExamChime(() => {{
    if ('speechSynthesis' in window) {{
      const uttr = new SpeechSynthesisUtterance(script);
      uttr.lang = 'ko-KR';
      uttr.rate = 0.93;
      uttr.pitch = 0.98;
      window.speechSynthesis.speak(uttr);
    }}
  }});
  const sel = document.getElementById('exam-broadcast-select');
  if (sel) sel.value = '';
}}

function toggleASMR() {{
  if (!isAsmrOn) startASMR();
  else stopASMR();
}}

function startASMR() {{
  try {{
    const ctx = ensureAudioCtx();
    const bufferSize = ctx.sampleRate * 2;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {{
      data[i] = (Math.random() * 2 - 1) * 0.012;
    }}
    noiseNode = ctx.createBufferSource();
    noiseNode.buffer = buffer;
    noiseNode.loop = true;
    const filter = ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.value = 950;
    noiseNode.connect(filter);
    filter.connect(ctx.destination);
    noiseNode.start();
    isAsmrOn = true;

    // 주기적인 실제 고사장 시험지 넘기는 소리 & 주변 수험생 필기 소리 연출
    if (examHallTimer) clearInterval(examHallTimer);
    examHallTimer = setInterval(() => {{
      if (!isAsmrOn) return;
      if (Math.random() < 0.45) {{
        playPaperTurnSound();
      }} else {{
        for (let s = 0; s < 3; s++) {{
          setTimeout(() => playPenStrokeSound(), s * 110);
        }}
      }}
    }}, 6500);

    const btn = document.getElementById('btn-asmr');
    if (btn) {{
      btn.textContent = '🔔 시험장 소리·멘트 ON';
      btn.classList.add('on');
    }}
    // 시작 즉시 고사장 본령 타종 + 시작 안내 방송 송출
    playSelectedBroadcast('start');
  }} catch(e) {{
    showToast('오디오를 재생할 수 없습니다.');
  }}
}}

function stopASMR() {{
  if (noiseNode) {{
    try {{ noiseNode.stop(); noiseNode.disconnect(); }} catch(e) {{}}
    noiseNode = null;
  }}
  if (examHallTimer) {{
    clearInterval(examHallTimer);
    examHallTimer = null;
  }}
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  isAsmrOn = false;
  const btn = document.getElementById('btn-asmr');
  if (btn) {{
    btn.textContent = '🔔 시험장 소리·멘트 OFF';
    btn.classList.remove('on');
  }}
  showToast('시험장 현장음 및 방송이 종료되었습니다.');
}}

let isChosungHintMode = false;
let showLectureProblem = true;
let isTouchChipMode = false;
let isMiniMockMode = false;
let isBlindExamMode = false;
let miniMockIds = [];
const CHOSUNG_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];

function toggleBlindExamMode() {{
  isBlindExamMode = !isBlindExamMode;
  document.body.classList.toggle('blind-exam-mode', isBlindExamMode);
  const btn = document.getElementById('btn-blind-exam');
  if (btn) {{
    btn.classList.toggle('active', isBlindExamMode);
    btn.textContent = isBlindExamMode ? '🙈 실전 블라인드 ON (정답 보기)' : '🙈 실전 블라인드 OFF';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(isBlindExamMode
    ? '🙈 [100% 실전 블라인드 모드] 모든 힌트와 정답이 가려졌습니다! 오직 문제와 발문만 보고 4줄을 채워보세요.'
    : '🔓 블라인드 모드가 해제되었습니다! 방금 작성한 답안의 KICE 칼채점 결과를 확인하세요.');
}}

function toggleMiniMockExam() {{
  isMiniMockMode = !isMiniMockMode;
  const btn = document.getElementById('btn-mini-mock');
  if (isMiniMockMode) {{
    if (currentPeriod !== 'KICE55') switchPeriod('KICE55');
    pickMiniMockIds();
    setCustomTimer(20);
    if (btn) {{
      btn.classList.add('active');
      btn.textContent = '🎲 모의고사 종료';
    }}
    showToast('🎲 [실전 10문제 미니 모의고사] 교육학 3 + 전공 7 문제가 무작위 추첨되었습니다! (20분 시작)');
  }} else {{
    if (btn) {{
      btn.classList.remove('active');
      btn.textContent = '🎲 실전 10문제 모의고사';
    }}
    showToast('실전 모의고사 모드를 종료하고 전체 문항으로 복귀했습니다.');
  }}
  singleFocusIdx = 0;
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateMiniMockScoreBanner();
}}

function pickMiniMockIds() {{
  const pedPool = dataKICE55.filter(x => x.part === 'PED20').map(x => x.id).sort(() => Math.random() - 0.5).slice(0, 3);
  const cslPool = dataKICE55.filter(x => x.part === 'COUNSEL35').map(x => x.id).sort(() => Math.random() - 0.5).slice(0, 7);
  miniMockIds = [...pedPool, ...cslPool];
}}

function reshuffleMiniMock() {{
  pickMiniMockIds();
  setCustomTimer(20);
  singleFocusIdx = 0;
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateMiniMockScoreBanner();
  showToast('🎲 새로운 실전 10문제가 다시 추첨되었습니다!');
}}

function updateMiniMockScoreBanner() {{
  const el = document.getElementById('mini-mock-total-score');
  if (!el || !isMiniMockMode) return;
  let total = 0;
  miniMockIds.forEach(id => {{
    const q = dataKICE55.find(x => x.id === id);
    if (!q) return;
    const saved = localStorage.getItem(getRoundKeyPrefix() + 'KICE55' + id) || '';
    if (saved.trim().length > 0) {{
      const kws = q.keywords || [];
      const hits = kws.filter(kw => isKeywordSolvedInText(kw, saved)).length;
      total += kws.length > 0 ? (hits / kws.length) * 4.0 : 0;
    }}
  }});
  el.textContent = total.toFixed(1);
}}

function openWeaknessModal() {{
  const modal = document.getElementById('weakness-modal');
  const box = document.getElementById('weakness-content');
  if (!modal || !box) return;
  const log = JSON.parse(localStorage.getItem('kice_weak_keywords') || '{{}}');
  const entries = Object.entries(log).filter(([, v]) => v && v.missed && v.missed.length > 0);
  let html = '';
  if (entries.length === 0) {{
    html = `
      <div style="background:rgba(16,185,129,0.12); border:1px solid #10b981; border-radius:8px; padding:14px; margin-bottom:12px; color:#a7f3d0;">
        🎉 아직 답안 작성 중 누락된 약점 키워드가 없습니다! (타이핑 연습 중 빠진 키워드가 생기면 이곳에 자동으로 모입니다.)
      </div>
      <div style="font-weight:800; color:#fde047; margin-bottom:8px;">⚡ [기본 탑재] 시험장 직전 가장 많이 실수하는 0순위 족보 5선</div>
      <div class="weak-item-card"><strong>#21 강박장애 vs 강박성 성격장애</strong><br><span style="color:#fda4af;">핵심:</span> 자아 이질적 vs 자아 동질적 · 노출 및 반응방지(ERP)</div>
      <div class="weak-item-card"><strong>#24 사회적(실용적) 의사소통장애 vs 자폐스펙트럼장애</strong><br><span style="color:#fda4af;">핵심:</span> 제한적이고 반복적인 행동 패턴(상동 행동) 유무 · 화용론적 언어 결함</div>
      <div class="weak-item-card"><strong>#40 빅터 프랑클 의미치료</strong><br><span style="color:#fda4af;">핵심:</span> 탈숙고(Dereflection) · 역설적 의도</div>
      <div class="weak-item-card"><strong>#48 머레이 욕구-압착 이론</strong><br><span style="color:#fda4af;">핵심:</span> 알파 압착(객관적 실제) vs 베타 압착(주관적 지각 · 행동 지배)</div>
      <div class="weak-item-card"><strong>#55 숀 셰이 (Shawn Shea) CASE 모델 & 길리랜드</strong><br><span style="color:#fda4af;">핵심:</span> 제시-최근-과거-즉각 사건 · 참여 유도(안전계획서) · 학폭 제6호(출석정지)</div>
    `;
  }} else {{
    html = `<div style="margin-bottom:10px; color:#fecdd3; font-weight:700;">총 <strong>${{entries.length}}개</strong> 문항에서 누락된 키워드가 감지되었습니다. 시험장 들어가기 직전 이 키워드들만 눈으로 찍고 들어가세요!</div>`;
    entries.forEach(([k, info]) => {{
      html += `
        <div class="weak-item-card">
          <div style="font-weight:800; color:#f8fafc; margin-bottom:4px;">${{escapeHtml(info.title || k)}}</div>
          <div style="color:#fda4af; font-weight:700;">❌ 누락 키워드: ${{info.missed.map(m => `<span style="background:rgba(244,63,94,0.2); padding:2px 7px; border-radius:4px; margin-right:4px;">${{escapeHtml(m)}}</span>`).join('')}}</div>
        </div>
      `;
    }});
  }}
  box.innerHTML = html;
  modal.style.display = 'flex';
}}

function closeWeaknessModal() {{
  const modal = document.getElementById('weakness-modal');
  if (modal) modal.style.display = 'none';
}}

function speakWeaknessList() {{
  const log = JSON.parse(localStorage.getItem('kice_weak_keywords') || '{{}}');
  const entries = Object.entries(log).filter(([, v]) => v && v.missed && v.missed.length > 0);
  if (entries.length === 0) {{
    speakAnswer('시험장 직전 핵심 족보. 강박장애는 자아 이질적, 노출 및 반응방지. 프랑클 의미치료는 탈숙고와 역설적 의도. 머레이는 알파 압착과 베타 압착. 숀 셰이 케이쓰 모델은 제시, 최근, 과거, 즉각 사건 순입니다.');
    return;
  }}
  const txt = entries.map(([, info]) => `${{info.title}}의 놓친 키워드는 ${{info.missed.join(', ')}} 입니다.`).join(' ');
  speakAnswer(txt);
}}

function clearWeaknessLog() {{
  if (!confirm('누락 약점 키워드 기록을 초기화하시겠습니까?')) return;
  localStorage.removeItem('kice_weak_keywords');
  openWeaknessModal();
  showToast('약점 키워드 기록이 초기화되었습니다.');
}}

function toggleHandwritingPad(key) {{
  const wrap = document.getElementById('hw-wrap-' + key);
  if (!wrap) return;
  const isOpen = wrap.classList.toggle('open');
  if (isOpen) {{
    initHandwritingCanvas(key);
  }}
}}

function initHandwritingCanvas(key) {{
  const canvas = document.getElementById('hw-canvas-' + key);
  if (!canvas || canvas.dataset.hwInit === '1') return;
  canvas.dataset.hwInit = '1';
  const rect = canvas.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.max(300, Math.floor((rect.width || 700) * dpr));
  canvas.height = Math.floor(200 * dpr);
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  ctx.strokeStyle = '#0f172a';
  ctx.lineWidth = 2.6;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';

  let drawing = false;
  const getPos = (e) => {{
    const r = canvas.getBoundingClientRect();
    return {{ x: e.clientX - r.left, y: e.clientY - r.top }};
  }};
  canvas.addEventListener('pointerdown', (e) => {{
    drawing = true;
    canvas.setPointerCapture(e.pointerId);
    const p = getPos(e);
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
  }});
  canvas.addEventListener('pointermove', (e) => {{
    if (!drawing) return;
    const p = getPos(e);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
  }});
  const stopDraw = () => {{ drawing = false; }};
  canvas.addEventListener('pointerup', stopDraw);
  canvas.addEventListener('pointercancel', stopDraw);
}}

function clearHandwritingPad(key) {{
  const canvas = document.getElementById('hw-canvas-' + key);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}}

function toggleTouchChipMode() {{
  isTouchChipMode = !isTouchChipMode;
  const btn = document.getElementById('btn-touch-chip');
  if (btn) {{
    btn.classList.toggle('active', isTouchChipMode);
    btn.textContent = isTouchChipMode ? '👆 터치 조립 모드 ON' : '👆 터치 조립 모드 OFF';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(isTouchChipMode
    ? '👆 [태블릿 원터치 조립 모드] 키워드 칩을 터치하면 빈칸에 자동으로 채워집니다!'
    : '원터치 조립 모드를 껐습니다.');
}}

function handleTouchChipClick(period, num, lineIdx, isCorrect, chipText, btnEl) {{
  if (!isCorrect) {{
    if (btnEl) btnEl.classList.add('trap-shake');
    showToast(`⚠️ "${{chipText}}"은(는) 오답 함정 키워드입니다! 지문 단서를 다시 확인하세요.`);
    return;
  }}
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const key = period + num;
  const lines = q.lines || q.answer.split('\\n');
  const kwList = q.keywords || extractKeywords(q.answer);
  const targetIdx = (lineIdx >= 0 && lineIdx < lines.length) ? lineIdx : 0;
  const inp = document.getElementById(`lbl-in-${{key}}-${{targetIdx}}`);
  if (!inp) return;

  // 아직 해당 줄 입력창이 비어있으면 뼈대를 먼저 채운 뒤 해당 키워드 꽂아 넣기
  if (!inp.value.trim()) {{
    const blanks = (q.line_blanks && q.line_blanks[targetIdx] && q.line_blanks[targetIdx].length > 0)
      ? q.line_blanks[targetIdx]
      : kwList;
    let skel = lines[targetIdx];
    [...new Set(blanks)].sort((a, b) => b.length - a.length).forEach(kw => {{
      skel = skel.split(kw).join('□'.repeat(kw.length));
    }});
    inp.value = skel;
  }}
  const mask = '□'.repeat(chipText.length);
  if (inp.value.includes(mask)) {{
    inp.value = inp.value.replace(mask, chipText);
  }} else if (inp.value.includes('□')) {{
    inp.value = inp.value.replace(/□+/, chipText);
  }} else if (!inp.value.includes(chipText)) {{
    inp.value = (inp.value.trim() + ' ' + chipText).trim();
  }}
  if (btnEl) btnEl.classList.add('used');
  playMiniHitSound();
  handleLineByLineInput(period, num, targetIdx, lines.length);
}}

function updateDDayBadge() {{
  const el = document.getElementById('dday-seal');
  if (!el) return;
  const target = new Date('2026-11-28T00:00:00+09:00');
  const now = new Date();
  const todayMidnight = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const targetMidnight = new Date(target.getFullYear(), target.getMonth(), target.getDate());
  const diffDays = Math.round((targetMidnight - todayMidnight) / (1000 * 60 * 60 * 24));
  if (diffDays > 0) el.textContent = `D-${{diffDays}} (11.28 결전)`;
  else if (diffDays === 0) el.textContent = '🔥 D-DAY (오늘이 결전일!)';
  else el.textContent = `D+${{Math.abs(diffDays)}} (수고하셨습니다)`;
}}

function getDailyMissionKey() {{
  const d = new Date();
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `kice_daily_${{y}}-${{m}}-${{day}}`;
}}

function recordDailyDone(key) {{
  const storageKey = getDailyMissionKey();
  const arr = JSON.parse(localStorage.getItem(storageKey) || '[]');
  if (!arr.includes(key)) {{
    arr.push(key);
    localStorage.setItem(storageKey, JSON.stringify(arr));
    updateDailyMissionUI();
    if (arr.length === 10) {{
      playSuccessChime();
      showToast('🎉 축하합니다! 오늘의 10문제 미션을 100% 완수하셨습니다!');
    }}
  }}
}}

function updateDailyMissionUI() {{
  const arr = JSON.parse(localStorage.getItem(getDailyMissionKey()) || '[]');
  const cntEl = document.getElementById('daily-mission-count');
  const barEl = document.getElementById('daily-mission-bar');
  if (cntEl) cntEl.textContent = arr.length;
  if (barEl) barEl.style.width = Math.min(100, (arr.length / 10) * 100) + '%';
}}

function exportProgressBackup() {{
  const data = {{}};
  for (let i = 0; i < localStorage.length; i++) {{
    const k = localStorage.key(i);
    if (k && k.startsWith('kice_')) data[k] = localStorage.getItem(k);
  }}
  const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json;charset=utf-8' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  const dt = new Date().toISOString().slice(0, 10).replace(/-/g, '');
  a.href = url;
  a.download = `2027_임용_학습진도_백업_${{dt}}.json`;
  a.click();
  URL.revokeObjectURL(url);
  showToast('💾 PC ↔ 태블릿 진도 백업 파일이 저장되었습니다!');
}}

function importProgressBackup(event) {{
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (e) => {{
    try {{
      const obj = JSON.parse(e.target.result);
      let count = 0;
      Object.keys(obj).forEach(k => {{
        if (k.startsWith('kice_')) {{
          localStorage.setItem(k, obj[k]);
          count++;
        }}
      }});
      bookmarks = JSON.parse(localStorage.getItem('kice_bookmarks') || '{{}}');
      renderNav();
      renderCards();
      loadSavedAnswers();
      updateProgress();
      updateDailyMissionUI();
      showToast(`📂 진도 복원 완료! (${{count}}개 학습 기록이 동기화되었습니다)`);
    }} catch(err) {{
      showToast('⚠️ 올바른 백업 JSON 파일이 아닙니다.');
    }}
    event.target.value = '';
  }};
  reader.readAsText(file, 'utf-8');
}}

function toggleLectureProblemMode() {{
  showLectureProblem = !showLectureProblem;
  const btn = document.getElementById('btn-lecture-mode');
  if (btn) {{
    btn.classList.toggle('active', showLectureProblem);
    btn.textContent = showLectureProblem ? '🎓 강의+문제 ON' : '🎓 강의+문제 OFF';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(showLectureProblem
    ? '🎓 [1단계 강의 ➔ 2단계 문제 ➔ 3단계 4줄 정답] 모드가 켜졌습니다!'
    : '강의와 문제를 접고 4줄 정답 타이핑만 표시합니다.');
}}

function speakCardLecture(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const txt = (q.lecture_summary || '') + ' ' + (q.lecture_point || '').replace('⚡', '');
  if (txt.trim()) speakAnswer(txt);
}}

function speakCardProblem(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const txt = (q.problem_passage || '') + ' 작성 방법. ' + (q.problem_asks || []).join(' ');
  if (txt.trim()) speakAnswer(txt);
}}

function toChosung(str) {{
  if (!str) return '';
  let out = '';
  for (let i = 0; i < str.length; i++) {{
    const code = str.charCodeAt(i) - 0xAC00;
    if (code >= 0 && code <= 11171) {{
      out += CHOSUNG_LIST[Math.floor(code / 588)];
    }} else {{
      out += str[i];
    }}
  }}
  return out;
}}

function toggleKeywordBlankMode() {{
  isBlankMode = !isBlankMode;
  if (!isBlankMode) isChosungHintMode = false;
  const btn = document.getElementById('btn-kw-blank');
  if (btn) {{
    btn.classList.toggle('active', isBlankMode);
    btn.textContent = isBlankMode ? '🎯 핵심키워드 빈칸 ON (클릭·타이핑 시 열림)' : '🎯 핵심키워드 빈칸 만들기';
  }}
  const cBtn = document.getElementById('btn-chosung-hint');
  if (cBtn) {{
    cBtn.classList.toggle('active', isChosungHintMode);
    cBtn.textContent = isChosungHintMode ? '🔤 초성 힌트(ㄱㄴㄷ) ON' : '🔤 초성 힌트(ㄱㄴㄷ) 보기';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(isBlankMode
    ? '🎯 핵심키워드 빈칸 모드가 켜졌습니다! 빈칸을 클릭하거나 아래에 타이핑하면 정답이 열립니다.'
    : '핵심키워드 전체 보기 모드로 전환되었습니다.');
}}

function toggleChosungHintMode() {{
  isChosungHintMode = !isChosungHintMode;
  if (isChosungHintMode && !isBlankMode) {{
    isBlankMode = true;
    const btn = document.getElementById('btn-kw-blank');
    if (btn) {{
      btn.classList.add('active');
      btn.textContent = '🎯 핵심키워드 빈칸 ON (클릭·타이핑 시 열림)';
    }}
  }}
  const cBtn = document.getElementById('btn-chosung-hint');
  if (cBtn) {{
    cBtn.classList.toggle('active', isChosungHintMode);
    cBtn.textContent = isChosungHintMode ? '🔤 초성 힌트(ㄱㄴㄷ) ON' : '🔤 초성 힌트(ㄱㄴㄷ) 보기';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(isChosungHintMode
    ? '🔤 [ADHD 초성 연상 모드] 빈칸 안에 한글 초성(ㄱㄴㄷ) 힌트가 표시됩니다! (클릭 시 정답 확인)'
    : '초성 힌트를 끄고 일반 빈칸으로 표시합니다.');
}}

function toggleCases8Mode() {{
  showCases8 = !showCases8;
  const btn = document.getElementById('btn-cases8-mode');
  if (btn) {{
    btn.classList.toggle('active', showCases8);
    btn.textContent = showCases8 ? '⚡ 경우의 수 8개 ON' : '⚡ 경우의 수 8개 OFF';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(showCases8
    ? '⚡ ADHD 도파민 연타 모드: 나올 수 있는 경우의 수 8개(총 800개)가 표시됩니다!'
    : '경우의 수 8개 박스를 접고 답안지만 표시합니다.');
}}

function normalizeKiceSyn(s) {{
  return s.replace(/\\s+/g, '')
    .replace(/분화도/g, '변별도')
    .replace(/압력/g, '압착')
    .replace(/대지/g, '강령')
    .replace(/메타인지/g, '초인지')
    .replace(/소환/g, '회귀');
}}

function isKeywordSolvedInText(kw, typedText) {{
  if (!typedText || !kw) return false;
  const normTyped = normalizeKiceSyn(typedText);
  const normKw = normalizeKiceSyn(kw);
  if (normTyped.includes(normKw)) return true;
  const noParen = kw.replace(/\\(.*?\\)/g, '').trim();
  const normNoParen = normalizeKiceSyn(noParen);
  if (normNoParen.length >= 2 && normTyped.includes(normNoParen)) return true;
  const parts = noParen.split(/[·/\\s,]+/).filter(x => x.length >= 2);
  if (parts.length > 0 && parts.every(p => normTyped.includes(normalizeKiceSyn(p)))) return true;
  return false;
}}

function formatTextWithBlanks(text, blanks, typedText) {{
  if (!text) return '';
  if (!isBlankMode || !blanks || blanks.length === 0) {{
    return escapeHtml(text);
  }}
  const uniq = [...new Set(blanks.filter(b => b && b.trim().length > 0))].sort((a, b) => b.length - a.length);
  let safeHtml = escapeHtml(text);
  uniq.forEach((kw, idx) => {{
    const escKw = escapeHtml(kw);
    const solved = isKeywordSolvedInText(kw, typedText || '');
    const cls = 'kw-blank-slot' + (solved ? ' solved' : (isChosungHintMode ? ' chosung-mode' : ''));
    const displayStr = (!solved && isChosungHintMode) ? escapeHtml(toChosung(kw)) : escKw;
    const token = `__KW_SLOT_${{idx}}__`;
    safeHtml = safeHtml.split(escKw).join(token);
    safeHtml = safeHtml.split(token).join(
      `<span class="${{cls}}" data-kw="${{escKw}}" onclick="this.textContent=this.getAttribute('data-kw'); this.classList.toggle('revealed')" title="클릭하거나 아래 입력창에 키워드를 타이핑하면 열립니다">${{displayStr}}</span>`
    );
  }});
  return safeHtml;
}}

function speakSingleLine(period, num, lineIdx) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const lines = q.lines || q.answer.split('\\n');
  if (lines[lineIdx]) speakAnswer(lines[lineIdx]);
}}

function fillSingleLine(period, num, lineIdx) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const key = period + num;
  const lines = q.lines || q.answer.split('\\n');
  if (!lines[lineIdx]) return;
  const inp = document.getElementById(`lbl-in-${{key}}-${{lineIdx}}`);
  if (inp) {{
    inp.value = lines[lineIdx];
    handleLineByLineInput(period, num, lineIdx, lines.length);
    inp.focus();
  }}
}}

function setCustomTimer(mins) {{
  timerSeconds = mins * 60;
  updateTimerUI();
  if (!isTimerRunning) {{
    startTimer();
    isTimerRunning = true;
    const btn = document.getElementById('btn-timer-toggle');
    if (btn) btn.textContent = '일시정지';
  }}
  showToast(`⏱️ 타이머가 ${{mins}}분 스프린트로 설정되었습니다!`);
}}

function speakAnswer(text) {{
  if (!('speechSynthesis' in window)) {{
    showToast('이 브라우저는 음성 낭독을 지원하지 않습니다.');
    return;
  }}
  window.speechSynthesis.cancel();
  const clean = text.replace(/\\n/g, ' ').replace(/[㉠㉡㉢]/g, '');
  const uttr = new SpeechSynthesisUtterance(clean);
  uttr.lang = 'ko-KR';
  uttr.rate = 0.95;
  window.speechSynthesis.speak(uttr);
  showToast('KICE 모범답안 음성 낭독을 시작합니다.');
}}

function adjustFont(delta) {{
  currentFontScale = Math.max(0.85, Math.min(1.35, currentFontScale + delta));
  document.documentElement.style.setProperty('--font-scale', currentFontScale);
  showToast(`글꼴 크기: ${{Math.round(currentFontScale * 100)}}%`);
}}

function startTimer() {{
  if (timerInterval) clearInterval(timerInterval);
  timerInterval = setInterval(() => {{
    if (timerSeconds > 0) {{
      timerSeconds--;
      updateTimerUI();
      if (timerSeconds === 600 && isAsmrOn) {{
        playSelectedBroadcast('warn10');
      }}
    }} else {{
      clearInterval(timerInterval);
      playSelectedBroadcast('end');
      alert("🔔 시험 종료령이 울렸습니다! 작성하신 답안지를 최종 점검해 주세요.");
    }}
  }}, 1000);
}}

function updateTimerUI() {{
  const m = Math.floor(timerSeconds / 60);
  const s = timerSeconds % 60;
  const el = document.getElementById('timer-display');
  el.textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  el.classList.toggle('warning', timerSeconds < 300);
}}

function toggleTimer() {{
  const btn = document.getElementById('btn-timer-toggle');
  if (isTimerRunning) {{
    clearInterval(timerInterval);
    isTimerRunning = false;
    btn.textContent = '계속';
  }} else {{
    startTimer();
    isTimerRunning = true;
    btn.textContent = '일시정지';
  }}
}}

function resetTimer() {{
  timerSeconds = 30 * 60;
  updateTimerUI();
  if (!isTimerRunning) {{
    startTimer();
    isTimerRunning = true;
    document.getElementById('btn-timer-toggle').textContent = '일시정지';
  }}
}}

function togglePaperMode() {{
  isPaperMode = !isPaperMode;
  document.body.classList.toggle('b4-paper-mode', isPaperMode);
  document.getElementById('btn-paper-mode').textContent = isPaperMode ? 'CBT 다크 모드' : 'B4 시험지 모드';
}}

function toggleBookmarkFilter() {{
  showOnlyBookmarks = !showOnlyBookmarks;
  document.getElementById('btn-bookmark-filter').classList.toggle('active', showOnlyBookmarks);
  singleFocusIdx = 0;
  renderCards();
  loadSavedAnswers();
}}

function toggleIncompleteFilter() {{
  showOnlyIncomplete = !showOnlyIncomplete;
  const btn = document.getElementById('btn-incomplete-filter');
  if (btn) {{
    btn.classList.toggle('active', showOnlyIncomplete);
    btn.textContent = showOnlyIncomplete ? '🔥 미완료만 보기 ON' : '🔥 미완료 문항만 보기';
  }}
  singleFocusIdx = 0;
  renderCards();
  loadSavedAnswers();
  showToast(showOnlyIncomplete
    ? '🔥 아직 완료하지 않은 문항만 모아서 보여줍니다! 하나씩 격파해 보세요!'
    : '전체 문항 보기로 복귀했습니다.');
}}

function toggleSingleFocusMode() {{
  isSingleFocusMode = !isSingleFocusMode;
  singleFocusIdx = 0;
  const btn = document.getElementById('btn-single-focus');
  if (btn) {{
    btn.classList.toggle('active', isSingleFocusMode);
    btn.textContent = isSingleFocusMode ? '🔍 1문제 집중 모드 ON' : '🔍 1문제 집중 모드 OFF';
  }}
  renderCards();
  loadSavedAnswers();
  showToast(isSingleFocusMode
    ? '🔍 ADHD 초집중 모드: 화면에 딱 1문제만 크게 표시합니다! (◀ 이전 / 다음 ▶ 이동)'
    : '전체 스크롤 모드로 전환되었습니다.');
}}

function stepSingleCard(delta) {{
  let items = getFilteredItems();
  if (items.length === 0) return;
  singleFocusIdx = (singleFocusIdx + delta + items.length) % items.length;
  renderCards();
  loadSavedAnswers();
}}

function toggleRadioMode() {{
  if (isRadioPlaying) {{
    isRadioPlaying = false;
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    document.querySelectorAll('.q-card.radio-active').forEach(el => el.classList.remove('radio-active'));
    const btn = document.getElementById('btn-radio');
    if (btn) btn.textContent = '📻 연속 자동낭독 OFF';
    showToast('연속 자동낭독이 중지되었습니다.');
    return;
  }}
  if (!('speechSynthesis' in window)) {{
    showToast('이 브라우저는 음성 합성을 지원하지 않습니다.');
    return;
  }}
  isRadioPlaying = true;
  radioIndex = 0;
  const btn = document.getElementById('btn-radio');
  if (btn) btn.textContent = '📻 연속 자동낭독 ON (중지하려면 클릭)';
  showToast('📻 현재 목록의 전 문항 핵심 키워드 & 4줄 정답 연속 자동낭독을 시작합니다!');
  playNextRadioCard();
}}

function playNextRadioCard() {{
  if (!isRadioPlaying) return;
  const items = getFilteredItems();
  document.querySelectorAll('.q-card.radio-active').forEach(el => el.classList.remove('radio-active'));
  if (radioIndex >= items.length) {{
    isRadioPlaying = false;
    const btn = document.getElementById('btn-radio');
    if (btn) btn.textContent = '📻 연속 자동낭독 OFF';
    showToast('🏆 현재 목록의 모든 문항 연속 낭독이 완료되었습니다!');
    return;
  }}
  const q = items[radioIndex];
  const key = currentPeriod + q.num;
  const card = document.getElementById('card-' + key);
  if (card) {{
    card.classList.add('radio-active');
    card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
  }}

  const kwStr = (q.keywords || []).join(', ');
  const script = `${{q.title}}. 핵심 키워드: ${{kwStr}}. 4줄 만점 정답. ${{(q.lines || []).join(' ')}}`;
  window.speechSynthesis.cancel();
  const uttr = new SpeechSynthesisUtterance(script);
  uttr.lang = 'ko-KR';
  uttr.rate = 0.98;
  uttr.onend = () => {{
    if (!isRadioPlaying) return;
    radioIndex++;
    setTimeout(playNextRadioCard, 700);
  }};
  window.speechSynthesis.speak(uttr);
}}

function openPedBuilderModal() {{
  const modal = document.getElementById('ped-builder-modal');
  if (!modal) return;
  const currItems = dataKICE55.filter(x => x.domain === '교육과정');
  const methItems = dataKICE55.filter(x => x.domain === '교육방법');
  const evalItems = dataKICE55.filter(x => x.domain === '교육평가');
  const admItems = dataKICE55.filter(x => x.domain === '교육행정');

  const fillSel = (selId, arr) => {{
    const sel = document.getElementById(selId);
    if (!sel || sel.options.length > 0) return;
    arr.forEach(item => {{
      const opt = document.createElement('option');
      opt.value = item.id;
      opt.textContent = `[#${{String(item.id).padStart(2, '0')}}] ${{item.title}}`;
      sel.appendChild(opt);
    }});
  }};
  fillSel('pb-sel-curr', currItems);
  fillSel('pb-sel-meth', methItems);
  fillSel('pb-sel-eval', evalItems);
  fillSel('pb-sel-adm', admItems);
  generatePedFullEssay();
  modal.style.display = 'flex';
}}

function closePedBuilderModal() {{
  const modal = document.getElementById('ped-builder-modal');
  if (modal) modal.style.display = 'none';
}}

function generatePedFullEssay() {{
  const theme = (document.getElementById('pb-theme')?.value || '학생 맞춤형 교육 혁신과 교사의 수석 역량').trim();
  const getById = (selId, fallbackId) => {{
    const id = parseInt(document.getElementById(selId)?.value || fallbackId, 10);
    return dataKICE55.find(x => x.id === id) || dataKICE55[0];
  }};
  const cItem = getById('pb-sel-curr', 1);
  const mItem = getById('pb-sel-meth', 11);
  const eItem = getById('pb-sel-eval', 16);
  const aItem = getById('pb-sel-adm', 19);

  const getClosing = (item, fallback) => {{
    if (item.ped_platform && item.ped_platform[1]) return item.ped_platform[1].text;
    return fallback;
  }};

  const essayLines = [
    `[서론: 변귀섭 대표님 만능 서론 플랫폼]`,
    `최근 급변하는 미래 교육환경 속에서 '${{theme}}'에 대한 화제가 대두되고 있다.`,
    `이러한 패러다임에 맞춰 교사는 단편적 지식 전달이 아닌 역량을 함양해야 한다.`,
    `여기에서는 제시문에 나온 교사들의 대화를 통해 '${{theme}}' 방안을 살펴본다.`,
    `교육과정, 교육방법, 교육평가, 교육행정의 4가지 측면에서 논하고자 한다.`,
    ``,
    `[본론 1: 교육과정 - ${{cItem.title}}]`,
    `첫째, 교육과정 측면에서 ${{cItem.lines[0]}}`,
    `${{cItem.lines[1]}}`,
    `${{cItem.lines[2]}}`,
    `${{cItem.lines[3]}}`,
    `${{getClosing(cItem, '이처럼 교사가 교육과정에서 핵심 원리를 쓰면 미래형 교육 혁신이 실현된다.')}}`,
    ``,
    `[본론 2: 교육방법 - ${{mItem.title}}]`,
    `둘째, 교육방법 측면에서 ${{mItem.lines[0]}}`,
    `${{mItem.lines[1]}}`,
    `${{mItem.lines[2]}}`,
    `${{mItem.lines[3]}}`,
    `${{getClosing(mItem, '이처럼 교사가 교육방법에서 핵심 전략을 쓰면 신개념 수업 혁신이 실현된다.')}}`,
    ``,
    `[본론 3: 교육평가 - ${{eItem.title}}]`,
    `셋째, 교육평가 측면에서 ${{eItem.lines[0]}}`,
    `${{eItem.lines[1]}}`,
    `${{eItem.lines[2]}}`,
    `${{eItem.lines[3]}}`,
    `${{getClosing(eItem, '이처럼 교사가 교육평가에서 핵심 평가를 쓰면 전인적 성장 평가가 실현된다.')}}`,
    ``,
    `[본론 4: 교육행정 - ${{aItem.title}}]`,
    `넷째, 교육행정 측면에서 ${{aItem.lines[0]}}`,
    `${{aItem.lines[1]}}`,
    `${{aItem.lines[2]}}`,
    `${{aItem.lines[3]}}`,
    `${{getClosing(aItem, '이처럼 교사가 교육행정에서 협력 문화를 쓰면 교사의 수석 역량이 증진된다.')}}`,
    ``,
    `[결론: 변귀섭 대표님 만능 결론 플랫폼]`,
    `지금까지 '${{theme}}'를 교육과정, 교육방법, 교육평가, 교육행정에서 살펴보았다.`,
    `다가오는 미래 교육이 성공하려면 무엇보다 교사의 인식과 실천이 중요하다.`,
    `따라서 교사는 끊임없는 자기 연찬과 동료 교사와의 협업으로 성장해야 한다.`,
    `또한 학생들에게 든든한 버팀목이자 교육 안내자 및 성장 촉진자가 되어야 한다.`
  ];

  const out = document.getElementById('pb-output');
  const fullTxt = essayLines.join('\\n');
  if (out) out.value = fullTxt;
  const info = document.getElementById('pb-char-info');
  if (info) info.textContent = `총 28문장 완벽 결합 (${{fullTxt.length}}자 / 20점 만점 규격 100% 충족)`;
}}

function copyPedFullEssay() {{
  const out = document.getElementById('pb-output');
  if (out && out.value) {{
    navigator.clipboard.writeText(out.value).then(() => showToast('🏛️ 완성된 1교시 교육학 20점 만점 논술문이 복사되었습니다!'));
  }}
}}

function speakPedFullEssay() {{
  const out = document.getElementById('pb-output');
  if (out && out.value) {{
    const clean = out.value.replace(/\\[.*?\\]/g, '');
    speakAnswer(clean);
  }}
}}

function toggleBookmark(key) {{
  bookmarks[key] = !bookmarks[key];
  localStorage.setItem('kice_bookmarks', JSON.stringify(bookmarks));
  renderNav();
  renderCards();
  loadSavedAnswers();
  showToast(bookmarks[key] ? '북마크에 추가되었습니다.' : '북마크가 해제되었습니다.');
}}

function shuffleCurrentPeriod() {{
  isShuffled = !isShuffled;
  document.getElementById('btn-shuffle').textContent = isShuffled ? '원래 순서로' : '랜덤 셔플';
  renderNav();
  renderCards();
  loadSavedAnswers();
  showToast(isShuffled ? '문항이 무작위로 셔플되었습니다.' : '정상 순서로 복원되었습니다.');
}}

let currentRound = parseInt(localStorage.getItem('kice_current_round') || '1', 10);

function getRoundKeyPrefix() {{
  return `kice_r${{currentRound}}_`;
}}

function switchPracticeRound(roundNum) {{
  currentRound = roundNum;
  localStorage.setItem('kice_current_round', currentRound);
  for (let r = 1; r <= 3; r++) {{
    const el = document.getElementById('round-btn-' + r);
    if (el) el.classList.toggle('active', r === currentRound);
  }}
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateProgress();
  showToast(`[오늘의 ${{currentRound}}회독] 답안지로 전환되었습니다.`);
}}

function setK55Category(cat, btnEl) {{
  currentK55Cat = cat;
  document.querySelectorAll('.k55-cat-btn').forEach(b => b.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateProgress();
}}

function clearCurrentAnswers() {{
  if (!confirm(`현재 탭의 작성 답안을 모두 지우고 새로 연습하시겠습니까?`)) return;
  const items = getList();
  const prefix = getRoundKeyPrefix();
  items.forEach(q => {{
    const key = currentPeriod + q.num;
    localStorage.removeItem(prefix + key);
    localStorage.removeItem(prefix + key + '_quiz');
    for (let i = 0; i < 6; i++) {{
      localStorage.removeItem(prefix + key + '_L' + i);
    }}
    for (let c = 0; c < 8; c++) {{
      localStorage.removeItem(prefix + key + '_C' + c);
    }}
    for (let p = 0; p < 4; p++) {{
      localStorage.removeItem(prefix + key + '_P' + p);
    }}
  }});
  renderNav();
  renderCards();
  updateProgress();
  showToast(`현재 탭 답안이 깨끗하게 초기화되었습니다.`);
}}

function clearAllPracticeRoundAnswers() {{
  const msg = `정말 [오늘의 ${{currentRound}}회독] 전체 답안지를 깨끗하게 비우고 새로 시작하시겠습니까?`;
  if (!confirm(msg)) return;
  const prefix = getRoundKeyPrefix();
  const keysToRemove = [];
  for (let i = 0; i < localStorage.length; i++) {{
    const k = localStorage.key(i);
    if (k && k.startsWith(prefix)) keysToRemove.push(k);
  }}
  keysToRemove.forEach(k => localStorage.removeItem(k));
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateProgress();
  resetTimer();
  showToast(`[오늘의 ${{currentRound}}회독] 전과목 답안지가 1초 만에 백지 초기화되었습니다!`);
}}

function switchPeriod(p) {{
  currentPeriod = p;
  isShuffled = false;
  document.getElementById('btn-shuffle').textContent = '랜덤 셔플';
  ['KICE55', 'TEMPLATE', 'PED', 'A', 'B'].forEach(tabId => {{
    const btn = document.getElementById('tab-btn-' + tabId);
    if (btn) btn.classList.toggle('active', tabId === p);
  }});
  const filterBar = document.getElementById('kice55-filter-bar');
  if (filterBar) filterBar.style.display = (p === 'KICE55') ? 'flex' : 'none';
  renderNav();
  renderCards();
  loadSavedAnswers();
  updateProgress();
}}

function getList() {{
  let list = [];
  if (currentPeriod === 'KICE55') {{
    const query = (document.getElementById('k55-search-input')?.value || '').trim().toLowerCase();
    list = dataKICE55.filter(item => {{
      if (currentK55Cat === 'CORE55' && item.part === 'PED20' && ![1, 4, 5, 8, 10, 12, 13, 15, 17, 18].includes(item.id)) return false;
      if (currentK55Cat === 'PED10' && ![1, 4, 5, 8, 10, 12, 13, 15, 17, 18].includes(item.id)) return false;
      if (currentK55Cat === 'PED20' && item.part !== 'PED20') return false;
      if (currentK55Cat === 'COUNSEL35' && item.part !== 'COUNSEL35') return false;
      if (!['ALL', 'CORE55', 'PED10', 'PED20', 'COUNSEL35'].includes(currentK55Cat) && item.domain !== currentK55Cat) return false;
      if (query) {{
        const casesStr = (item.cases8 || []).map(c => c.q + ' ' + c.a).join(' ');
        const hay = (item.title + ' ' + item.concept + ' ' + item.keywords.join(' ') + ' ' + item.lines.join(' ') + ' ' + item.quiz_a + ' ' + casesStr).toLowerCase();
        if (!hay.includes(query)) return false;
      }}
      return true;
    }}).map(item => ({{
      num: item.id,
      title: `[#${{String(item.id).padStart(2, '0')}} ${{item.domain}}] ${{item.title}}`,
      concept: item.concept,
      type: item.part === 'PED20' ? '교육학 4줄정답' : '전공상담 4줄정답',
      score: 4,
      content: item.problem_passage || '',
      instructions: (item.problem_asks || []).join('\\n'),
      lecture_summary: item.lecture_summary || '',
      lecture_point: item.lecture_point || '',
      problem_passage: item.problem_passage || '',
      problem_asks: item.problem_asks || [],
      lines: item.lines,
      line_blanks: item.line_blanks || [],
      cases8: item.cases8 || [],
      ped_platform: item.ped_platform || [],
      answer: item.lines.join('\\n'),
      keywords: item.keywords,
      quiz_q: item.quiz_q,
      quiz_a: item.quiz_a,
      isFourLineMode: true
    }}));
  }} else if (currentPeriod === 'TEMPLATE') {{
    list = dataTEMPLATE.map(item => ({{
      num: item.id,
      title: item.title,
      concept: item.concept,
      type: item.domain,
      score: 4,
      content: '',
      instructions: '',
      lecture_summary: item.concept || '',
      lecture_point: '⚡ 시험장 1초 공식: ' + (item.keywords || []).join(' ➔ '),
      problem_passage: '',
      problem_asks: [],
      lines: item.lines,
      line_blanks: item.line_blanks || [],
      cases8: item.cases8 || [],
      ped_platform: [],
      answer: item.lines.join('\\n'),
      keywords: item.keywords,
      quiz_q: item.quiz_q,
      quiz_a: item.quiz_a,
      isFourLineMode: true
    }}));
  }} else if (currentPeriod === 'PED') {{
    list = dataPED.map(item => ({{
      num: item.num,
      title: `[${{item.domain}} ${{item.num}}번] ${{item.title}} - ${{item.concept}}`,
      type: '교육학 논술',
      score: 4,
      content: item.sub_questions.map((sq, i) => `${{i+1}}. ${{sq}}`).join('\\n'),
      instructions: '<작성 방법 및 채점 루브릭>\\n' + item.rubric.map(r => '○ ' + r).join('\\n'),
      lecture_summary: item.lecture_summary || '',
      lecture_point: item.lecture_point || '',
      problem_passage: item.sub_questions.map((sq, i) => `${{i+1}}. ${{sq}}`).join('\\n'),
      problem_asks: item.problem_asks || item.sub_questions || [],
      lines: item.model_answer,
      line_blanks: item.line_blanks || [],
      cases8: item.cases8 || [],
      ped_platform: item.ped_platform || [],
      answer: item.model_answer.join('\\n'),
      keywords: item.keywords,
      quiz_q: item.quiz_q || '',
      quiz_a: item.quiz_a || '',
      isFourLineMode: false
    }}));
  }} else {{
    const raw = currentPeriod === 'A' ? dataA : dataB;
    list = raw.map(item => ({{
      ...item,
      lecture_summary: item.lecture_summary || '',
      lecture_point: item.lecture_point || '',
      problem_passage: item.content || '',
      problem_asks: item.problem_asks || [],
      lines: item.lines || (item.answer ? item.answer.split('\\n') : []),
      line_blanks: item.line_blanks || [],
      cases8: item.cases8 || [],
      ped_platform: item.ped_platform || [],
      quiz_q: item.quiz_q || '',
      quiz_a: item.quiz_a || '',
      isFourLineMode: true
    }}));
  }}

  if (isShuffled) {{
    list = [...list].sort(() => Math.random() - 0.5);
  }}
  return list;
}}

function renderNav() {{
  const nav = document.getElementById('nav-strip');
  const items = getList();
  nav.innerHTML = '';
  items.forEach(item => {{
    const key = currentPeriod + item.num;
    const pill = document.createElement('button');
    pill.className = 'nav-pill';
    pill.id = 'nav-pill-' + key;
    const isBm = !!bookmarks[key];
    const labelNum = currentPeriod === 'KICE55' ? '#' + String(item.num).padStart(2, '0') : (currentPeriod + item.num + '번');
    pill.textContent = (isBm ? '★ ' : '') + labelNum;
    if (isBm) pill.classList.add('bookmarked');

    pill.onclick = () => {{
      const card = document.getElementById('card-' + key);
      if (card) {{
        card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        const firstInput = document.getElementById(`case8-in-${{key}}-0`) || document.getElementById(`lbl-in-${{key}}-0`) || document.getElementById('ta-' + key);
        if (firstInput) firstInput.focus();
      }}
    }};
    nav.appendChild(pill);
  }});
}}

function getFilteredItems() {{
  let items = getList();
  if (isMiniMockMode && currentPeriod === 'KICE55' && miniMockIds.length > 0) {{
    items = miniMockIds.map(id => items.find(q => q.num === id)).filter(Boolean);
  }}
  if (showOnlyBookmarks) {{
    items = items.filter(q => !!bookmarks[currentPeriod + q.num]);
  }}
  if (showOnlyIncomplete) {{
    items = items.filter(q => {{
      const key = currentPeriod + q.num;
      const pill = document.getElementById('nav-pill-' + key);
      if (pill && pill.classList.contains('done')) return false;
      const saved = localStorage.getItem(getRoundKeyPrefix() + key) || '';
      const linesArr = q.lines || q.answer.split('\\n');
      return saved.trim().length < Math.floor(linesArr.join('').length * 0.6);
    }});
  }}
  return items;
}}

function renderCards() {{
  const container = document.getElementById('exam-cards-container');
  let items = getFilteredItems();
  container.innerHTML = '';

  if (isMiniMockMode && currentPeriod === 'KICE55') {{
    const mBanner = document.createElement('div');
    mBanner.className = 'mini-mock-banner';
    mBanner.innerHTML = `
      <div>🎲 <strong>[실전 10문제 미니 모의고사]</strong> 교육학 3문제 + 전공상담 7문제 (총 40점 만점) · 현재 실시간 점수: <span id="mini-mock-total-score" style="color:#fde047; font-size:1.15rem;">0.0</span> / 40.0점</div>
      <div style="display:flex; gap:8px;">
        <button class="btn-sheet-mini" style="border-color:#fde047; color:#fde047;" onclick="reshuffleMiniMock()">🎲 새 10문제 다시 뽑기</button>
        <button class="btn-sheet-mini" style="border-color:#fda4af; color:#fda4af;" onclick="toggleMiniMockExam()">모의고사 종료</button>
      </div>
    `;
    container.appendChild(mBanner);
  }}

  if (items.length === 0) {{
    container.innerHTML = '<div style="text-align:center; padding: 40px; color: var(--text-muted); font-weight:700;">🎉 조건에 해당하는 문항이 없습니다 (모두 완료되었거나 북마크가 없습니다)!</div>';
    return;
  }}

  if (isSingleFocusMode) {{
    if (singleFocusIdx >= items.length) singleFocusIdx = items.length - 1;
    if (singleFocusIdx < 0) singleFocusIdx = 0;
    const navBar = document.createElement('div');
    navBar.style.cssText = 'display:flex; justify-content:space-between; align-items:center; background:linear-gradient(90deg, rgba(16,185,129,0.18), rgba(59,130,246,0.18)); border:2px solid #10b981; border-radius:12px; padding:10px 16px; margin-bottom:16px;';
    navBar.innerHTML = `
      <button class="btn-tool" onclick="stepSingleCard(-1)" style="background:#0f172a; border-color:#10b981; color:#6ee7b7; font-weight:800;">◀ 이전 문제 (Alt+←)</button>
      <div style="font-weight:900; color:#ecfdf5; font-size:0.95rem;">🔍 [ADHD 1문제 초집중 모드] 현재 <span style="color:#fde047;">${{singleFocusIdx + 1}}</span> / 총 ${{items.length}}문제</div>
      <button class="btn-tool" onclick="stepSingleCard(1)" style="background:#0f172a; border-color:#10b981; color:#6ee7b7; font-weight:800;">다음 문제 (Alt+→) ▶</button>
    `;
    container.appendChild(navBar);
    items = [items[singleFocusIdx]];
  }}

  items.forEach((q, cardIdx) => {{
    const key = currentPeriod + q.num;
    const isBm = !!bookmarks[key];
    const card = document.createElement('div');
    card.className = 'q-card';
    card.id = 'card-' + key;

    const badgeCls = q.type === '기입형' ? 'fillin' : (currentPeriod === 'KICE55' || currentPeriod === 'TEMPLATE' ? 'k55' : 'essay');
    const kwList = q.keywords || extractKeywords(q.answer);
    const linesArr = q.lines || q.answer.split('\\n');
    const isPed6 = (currentPeriod === 'PED');
    const minC = isPed6 ? 50 : 38;
    const maxC = isPed6 ? 60 : 45;

    // [ADHD 도파민 8연타] 나올 수 있는 경우의 수 8개 그리드 생성
    let cases8Html = '';
    if (showCases8 && q.cases8 && q.cases8.length > 0) {{
      const itemsHtml = q.cases8.map((c, cIdx) => {{
        const targetBadgeHtml = formatTextWithBlanks(c.a, [c.a], '');
        return `
          <div class="case8-item" id="case8-box-${{key}}-${{cIdx}}">
            <div class="case8-q-row">
              <span class="case8-q-label">${{escapeHtml(c.q)}}</span>
              <span class="case8-target-ans" id="case8-target-${{key}}-${{cIdx}}">${{targetBadgeHtml}}</span>
            </div>
            <input type="text"
              class="case8-input"
              id="case8-in-${{key}}-${{cIdx}}"
              placeholder="${{escapeHtml(c.a)}} (보고 치기 / Enter 다음)"
              oninput="handleCase8Input('${{currentPeriod}}', ${{q.num}}, ${{cIdx}})"
              onkeydown="handleCase8Keydown(event, '${{key}}', ${{cIdx}}, ${{q.cases8.length}})">
          </div>
        `;
      }}).join('');

      cases8Html = `
        <div class="cases8-box">
          <div class="cases8-header">
            <div class="cases8-title">
              <span>⚡ [ADHD 도파민 스피드 인출] 시험에 나올 수 있는 경우의 수 8개 (짧게 핵심만 치고 Enter!)</span>
              <span class="cases8-badge-count" id="cases8-count-${{key}}">0 / ${{q.cases8.length}} 격파</span>
            </div>
            <div style="display:flex; gap:6px;">
              <button class="btn-sheet-mini" onclick="fillAllCases8ForCard('${{currentPeriod}}', ${{q.num}})">8개 자동채우기</button>
              <button class="btn-sheet-mini" onclick="clearCases8ForCard('${{currentPeriod}}', ${{q.num}})">8개 비우기</button>
            </div>
          </div>
          <div class="cases8-grid">
            ${{itemsHtml}}
          </div>
        </div>
      `;
    }}

    // [1단계: 🎓 1분 족집게 미니강의 & 핵심 이론 설명]
    let lectureStepHtml = '';
    if (showLectureProblem && (q.lecture_summary || q.lecture_point)) {{
      lectureStepHtml = `
        <div class="lecture-step-box">
          <div class="lecture-step-header">
            <span>🎓 [1단계: 1분 족집게 강의 & 핵심 이론 설명] 왜 출제되며 어떻게 이해해야 할까?</span>
            <button class="btn-sheet-mini" style="border-color:#c084fc; color:#e9d5ff;" onclick="speakCardLecture('${{currentPeriod}}', ${{q.num}})">🎧 1분 강의 듣기</button>
          </div>
          ${{q.lecture_summary ? `<div class="lecture-summary-text">🗣️ <strong>일타 핵심 해설:</strong> ${{escapeHtml(q.lecture_summary)}}</div>` : ''}}
          ${{q.lecture_point ? `<div class="lecture-point-bar">${{escapeHtml(q.lecture_point)}}</div>` : ''}}
        </div>
      `;
    }}

    // [2단계: 📝 KICE 실전 사례 문제 & 작성 방법 (1~4줄 1:1 매칭 발문)]
    let problemStepHtml = '';
    if (showLectureProblem && (q.problem_passage || (q.problem_asks && q.problem_asks.length > 0))) {{
      const asksHtml = (q.problem_asks || []).map(ask => `<div>${{escapeHtml(ask)}}</div>`).join('');
      problemStepHtml = `
        <div class="problem-step-box">
          <div class="problem-step-header">
            <span>📝 [2단계: KICE 실전 사례 문제 & 4대 세부 발문] (아래 1~4줄 정답과 1:1 대응)</span>
            <button class="btn-sheet-mini" style="border-color:#38bdf8; color:#7dd3fc;" onclick="speakCardProblem('${{currentPeriod}}', ${{q.num}})">🎧 문제 지문 듣기</button>
          </div>
          ${{q.problem_passage ? `<div class="problem-passage-text">${{escapeHtml(q.problem_passage)}}</div>` : ''}}
          ${{asksHtml ? `<div class="problem-asks-list"><div style="color:#fde047; margin-bottom:4px;">&lt;작성 방법 (아래 1줄~4줄 정답을 순서대로 작성하시오)&gt;</div>${{asksHtml}}</div>` : ''}}
        </div>
      `;
    }}

    // [태블릿 전용] 👆 원터치 키워드 조립 칩 트레이 생성
    let touchChipHtml = '';
    if (isTouchChipMode && linesArr.length >= 1) {{
      const correctChips = [];
      linesArr.forEach((ln, idx) => {{
        const lbs = (q.line_blanks && q.line_blanks[idx] && q.line_blanks[idx].length > 0)
          ? q.line_blanks[idx]
          : kwList;
        lbs.forEach(b => {{
          if (b && !correctChips.some(x => x.text === b)) {{
            correctChips.push({{ text: b, lineIdx: idx, isCorrect: true }});
          }}
        }});
      }});
      const trapPool = ['인지적 융합', '역설적 의도', '자아 동질적', '규범적 차원', '탈목표 평가', '병렬적 왜곡', '외재적 부하', '수용 영역']
        .filter(t => !correctChips.some(c => c.text.includes(t) || t.includes(c.text)));
      const traps = trapPool.slice(0, 2).map(t => ({{ text: t, lineIdx: -1, isCorrect: false }}));
      const allChips = [...correctChips, ...traps].sort((a, b) => (a.text.length * 7 + a.text.charCodeAt(0)) % 13 - (b.text.length * 7 + b.text.charCodeAt(0)) % 13);
      const chipsBtnsHtml = allChips.map((ch, cIdx) => `
        <button class="touch-chip-btn" id="tchip-${{key}}-${{cIdx}}" onclick="handleTouchChipClick('${{currentPeriod}}', ${{q.num}}, ${{ch.lineIdx}}, ${{ch.isCorrect}}, '${{escapeHtml(ch.text).replace(/'/g, "\\\\'")}}', this)">
          ${{escapeHtml(ch.text)}}
        </button>
      `).join('');
      touchChipHtml = `
        <div class="touch-chip-tray">
          <div class="touch-chip-header">👆 [태블릿 원터치 조립 모드] 정답 키워드 칩을 톡톡 터치하면 1~4줄 빈칸에 자동으로 꽂힙니다! (오답 함정 2개 주의)</div>
          <div class="touch-chip-list">${{chipsBtnsHtml}}</div>
        </div>
      `;
    }}

    // 1줄씩 보고 따라치기 HTML 생성 (핵심키워드 빈칸 모드 연동 & 1:1 가로 길이 일치)
    let lineByLineHtml = '';
    if (linesArr.length >= 4) {{
      const rowsHtml = linesArr.map((ln, idx) => {{
        const lineBlanks = (q.line_blanks && q.line_blanks[idx] && q.line_blanks[idx].length > 0)
          ? q.line_blanks[idx]
          : kwList;
        const targetLineInner = formatTextWithBlanks(ln, lineBlanks, '');
        const subQText = (showLectureProblem && q.problem_asks && q.problem_asks[idx]) ? q.problem_asks[idx] : '';
        return `
        <div class="lbl-row">
          ${{subQText ? `<div class="lbl-subq-caption">📌 ${{escapeHtml(subQText)}}</div>` : ''}}
          <div class="lbl-target-line" id="lbl-target-${{key}}-${{idx}}">
            <span class="lbl-target-text" id="lbl-target-text-${{key}}-${{idx}}">${{targetLineInner}}</span>
            <span style="display:inline-flex; align-items:center; gap:5px; flex-shrink:0;">
              <button class="btn-line-mini" onclick="speakSingleLine('${{currentPeriod}}', ${{q.num}}, ${{idx}})" title="이 줄만 음성으로 듣기">🔊</button>
              <button class="btn-line-mini" onclick="fillSingleLine('${{currentPeriod}}', ${{q.num}}, ${{idx}})" title="이 줄만 즉시 자동채우기">⚡</button>
              <span style="font-size:0.78rem; color:var(--accent-blue);">${{ln.length}}자</span>
            </span>
          </div>
          <div class="lbl-input-wrap">
            <input type="text"
              class="lbl-input"
              id="lbl-in-${{key}}-${{idx}}"
              placeholder="${{isBlindExamMode ? '힌트 없이 직접 4줄 답안을 작성하세요 (Enter 다음 줄)...' : (isBlankMode ? '위의 파란색 빈칸 키워드가 포함된 문장을 완성하세요 (Enter 다음 줄)...' : escapeHtml(ln))}}"
              oninput="handleLineByLineInput('${{currentPeriod}}', ${{q.num}}, ${{idx}}, ${{linesArr.length}})"
              onkeydown="handleLineKeydown(event, '${{key}}', ${{idx}}, ${{linesArr.length}}, ${{cardIdx}})">
            <span class="lbl-char-badge" id="lbl-badge-${{key}}-${{idx}}">0자 / ${{minC}}~${{maxC}}자</span>
          </div>
        </div>
      `;
      }}).join('');

      lineByLineHtml = `
        <div class="line-by-line-box">
          <div class="lbl-header">
            <span>✍️ [3단계: 4줄 만점 정답 적기] 문장 길이 1:1 맞춤 따라치기 ${{(isBlankMode ? '(🎯 핵심키워드 빈칸 모드 ON)' : '(Enter 키로 다음 줄 즉시 이동)')}}</span>
            <div style="display:flex; gap:6px;">
              <button class="btn-sheet-mini" style="border-color:#38bdf8; color:#38bdf8;" onclick="fillSkeletonForCard('${{currentPeriod}}', ${{q.num}})" title="조사·서술어 뼈대는 미리 채워두고 핵심키워드 자리만 직접 채워 넣습니다">✏️ 빈칸 뼈대만 입력창에 넣기</button>
              <button class="btn-sheet-mini" onclick="fillAllLinesForCard('${{currentPeriod}}', ${{q.num}})">모범정답 자동채우기</button>
            </div>
          </div>
          ${{rowsHtml}}
        </div>
      `;
    }}

    // [변귀섭 대표님 전용] 내 교육학 논술 플랫폼 (서론 공식 · 본론 이처럼~ · 결론 공식) 따라치기 구역
    let pedPlatformHtml = '';
    if (q.ped_platform && q.ped_platform.length > 0) {{
      const platRowsHtml = q.ped_platform.map((pItem, pIdx) => {{
        const targetInner = formatTextWithBlanks(pItem.text, pItem.blanks || [], '');
        return `
        <div class="lbl-row">
          <div class="lbl-target-line" style="border-left-color: #10b981; background: rgba(16, 185, 129, 0.08);">
            <span class="lbl-target-text" id="ped-plat-target-${{key}}-${{pIdx}}"><strong style="color:#34d399; margin-right:6px;">[${{escapeHtml(pItem.label)}}]</strong>${{targetInner}}</span>
            <span style="font-size:0.78rem; color:#34d399; flex-shrink:0;">${{pItem.text.length}}자</span>
          </div>
          <div class="lbl-input-wrap">
            <input type="text"
              class="lbl-input"
              id="ped-plat-in-${{key}}-${{pIdx}}"
              placeholder="${{escapeHtml(pItem.text)}}"
              oninput="handlePedPlatInput('${{currentPeriod}}', ${{q.num}}, ${{pIdx}})"
              onkeydown="handlePedPlatKeydown(event, '${{key}}', ${{pIdx}}, ${{q.ped_platform.length}}, ${{cardIdx}})">
            <span class="lbl-char-badge" id="ped-plat-badge-${{key}}-${{pIdx}}">0자 / 38~45자</span>
          </div>
        </div>
        `;
      }}).join('');

      pedPlatformHtml = `
        <div class="line-by-line-box" style="border-color: rgba(16, 185, 129, 0.45); background: rgba(6, 78, 59, 0.14);">
          <div class="lbl-header" style="color: #34d399;">
            <span>🏛️ [내 교육학 플랫폼 따라치기] "미래 교육환경 속에서 (대주제)에 대한 화제가 대두되고 있다. ~ 이처럼 교사가 ~"</span>
            <div style="display:flex; gap:6px;">
              <button class="btn-sheet-mini" style="border-color:#10b981; color:#34d399;" onclick="fillPedPlatForCard('${{currentPeriod}}', ${{q.num}})">내 플랫폼 자동채우기</button>
              <button class="btn-sheet-mini" onclick="clearPedPlatForCard('${{currentPeriod}}', ${{q.num}})">비우기</button>
            </div>
          </div>
          ${{platRowsHtml}}
        </div>
      `;
    }}

    // 족집게 핵심키워드 퀴즈 박스
    let quizHtml = '';
    if (q.quiz_q && q.quiz_a) {{
      const quizTargetHtml = formatTextWithBlanks(q.quiz_a, [q.quiz_a], '');
      quizHtml = `
        <div class="quiz-typing-box">
          <div class="quiz-q-text">🎯 <strong>[족집게 1순위 대표 키워드 인출]</strong> ${{escapeHtml(q.quiz_q)}}</div>
          <div class="quiz-a-row">
            <span class="quiz-target-badge" id="quiz-target-${{key}}">정식 키워드 정답: ${{quizTargetHtml}}</span>
            <input type="text"
              class="quiz-input"
              id="quiz-in-${{key}}"
              placeholder="왼쪽 노란색 KICE 정식 키워드를 보고 그대로 타이핑하세요 (Enter 치면 다음 문제로 이동)..."
              oninput="handleQuizInputByCard('${{currentPeriod}}', ${{q.num}})"
              onkeydown="handleQuizKeydown(event, ${{cardIdx}})">
          </div>
        </div>
      `;
    }}

    card.innerHTML = `
      <div class="q-card-head">
        <div class="q-num-title">
          <span class="bookmark-star ${{isBm ? 'active' : ''}}" onclick="toggleBookmark('${{key}}')">★</span>
          <span>#${{String(q.num).padStart(2, '0')}}</span>
          <span class="type-pill ${{badgeCls}}">${{escapeHtml(q.type)}}</span>
          <span style="color:#fff;">${{escapeHtml(q.title)}}</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
          <button class="btn-sheet-mini" style="border-color:#fbbf24; color:#fde047;" onclick="toggleHandwritingPad('${{key}}')" title="태블릿 펜슬이나 손가락으로 직접 4줄을 사인펜처럼 써봅니다">✍️ 손글씨 써보기</button>
          <button class="btn-sheet-mini" onclick="toggleKeywordBlankMode()" title="모든 문장의 핵심 채점 키워드를 빈칸으로 만듭니다">🎯 빈칸 모드 ${{isBlankMode ? 'ON' : 'OFF'}}</button>
          <button class="btn-sheet-mini" onclick="speakCardAnswer('${{currentPeriod}}', ${{q.num}})">음성 듣기 🎧</button>
          <span class="q-score-tag" style="font-weight:800; color:var(--accent-gold);">[${{q.score}}점 만점]</span>
        </div>
      </div>

      <div class="q-card-body">
        ${{q.concept ? `<div class="concept-banner">💡 <strong>한 줄 핵심 공식:</strong> ${{escapeHtml(q.concept)}}</div>` : ''}}

        <!-- [1단계] 1분 족집게 강의 & 핵심 이론 설명 -->
        ${{lectureStepHtml}}

        <!-- [2단계] KICE 실전 사례 문제 & 작성 방법 (1~4줄 1:1 발문) -->
        ${{problemStepHtml}}

        <!-- KICE 정식 채점 키워드 배지 바 -->
        <div class="kw-tags-strip" id="kw-tags-${{key}}">
          <span class="kw-label-tag">🔑 KICE 정식 채점 키워드:</span>
          ${{kwList.map((kw, idx) => `<span class="kw-pill" id="kw-${{key}}-${{idx}}">${{formatTextWithBlanks(kw, [kw], '')}}</span>`).join('')}}
        </div>

        <!-- [태블릿 전용] 원터치 키워드 조립 칩 -->
        ${{touchChipHtml}}

        <!-- [3단계] 발문 ①~④ 1:1 매칭 4줄 만점 정답 따라치기 구역 -->
        ${{lineByLineHtml}}

        <!-- [변귀섭 대표님 전용] 내 교육학 논술 플랫폼 따라치기 구역 -->
        ${{pedPlatformHtml}}

        <!-- [ADHD 맞춤] 나올 수 있는 경우의 수 8개 스피드 인출 구역 -->
        ${{cases8Html}}

        <!-- 족집게 핵심키워드 따라치기 구역 -->
        ${{quizHtml}}

        <!-- B4 실전 4줄 답안지 통합 구역 -->
        <div class="sheet-grid" style="margin-top: 14px;">
          <div class="sheet-col">
            <div class="sheet-col-header">
              <span>📄 B4 실전 통합 답안지 (${{isPed6 ? '6줄 50~60자' : '4줄 38~45자'}} 자동 연동)</span>
              <div class="line-status-chip" id="chip-box-${{key}}">
                <span class="chip-item">총 0자</span>
              </div>
            </div>
            <textarea 
              class="b4-typing-sheet" 
              id="ta-${{key}}" 
              style="min-height: ${{isPed6 ? '250px' : '170px'}};"
              placeholder="${{isPed6 ? '위 1~6줄 입력창에 타이핑하거나 이곳에 직접 6줄로 타이핑하세요...' : '위 1~4줄 입력창에 타이핑하거나 이곳에 직접 4줄(38~45자)로 타이핑하세요...'}}"
              oninput="handleTextareaInput('${{currentPeriod}}', ${{q.num}})"></textarea>
          </div>

          <div class="sheet-col">
            <div class="sheet-col-header">
              <span>🏆 KICE 100% 만점 공식 4줄 정답지</span>
              <div>
                <button class="btn-sheet-mini" onclick="toggleMask('${{currentPeriod}}', ${{q.num}})">가리기/보기</button>
                <button class="btn-sheet-mini" onclick="copyModelAnswer('${{currentPeriod}}', ${{q.num}})">정답 복사</button>
              </div>
            </div>
            <div class="b4-answer-sheet" id="ans-${{key}}" style="min-height: ${{isPed6 ? '250px' : '170px'}};">${{escapeHtml(q.answer)}}</div>
          </div>
        </div>

        <div class="scoring-eval-bar">
          <span>B4 답안지 규격: <strong>${{isPed6 ? '공백 포함 줄당 50~60자 (총 6줄)' : '공백 포함 줄당 38~45자 (총 4줄 만점)'}}</strong></span>
          <span class="eval-score-text" id="eval-score-${{key}}">판정 대기</span>
        </div>
        <div class="kal-rubric-bar" id="kal-rubric-${{key}}">
          <span>🎯 [KICE 4점 만점 실시간 칼채점] 답안을 입력하면 필수 채점 키워드 적중 점수와 누락 키워드를 즉시 알려줍니다.</span>
        </div>
        <div class="hw-pad-wrap" id="hw-wrap-${{key}}">
          <div class="hw-pad-header">
            <span>✍️ [B4 실전 4줄 사인펜 손글씨 연습 패드] 태블릿 펜슬이나 손가락으로 직접 써보세요!</span>
            <div style="display:flex; gap:6px;">
              <button class="btn-sheet-mini" onclick="clearHandwritingPad('${{key}}')">🧹 지우기</button>
              <button class="btn-sheet-mini" onclick="toggleHandwritingPad('${{key}}')">접기</button>
            </div>
          </div>
          <canvas class="hw-canvas" id="hw-canvas-${{key}}"></canvas>
        </div>
      </div>
    `;

    container.appendChild(card);
  }});
  if (typeof applyTabletInputAttrs === 'function') applyTabletInputAttrs();
}}

function extractKeywords(ans) {{
  if (!ans) return [];
  const lines = ans.split('\\n');
  const kws = [];
  lines.forEach(l => {{
    const words = l.split(/[,\\s]+/);
    words.forEach(w => {{
      if (w.length >= 3 && !['들어갈', '공식', '명칭은', '정식', '있으며', '위해', '통해'].includes(w)) {{
        if (!kws.includes(w) && kws.length < 5) kws.push(w);
      }}
    }});
  }});
  return kws;
}}

function handleCase8Keydown(e, key, cIdx, totalCases) {{
  if (e.key === 'Enter') {{
    e.preventDefault();
    if (cIdx + 1 < totalCases) {{
      const nextCaseInp = document.getElementById(`case8-in-${{key}}-${{cIdx + 1}}`);
      if (nextCaseInp) nextCaseInp.focus();
    }} else {{
      const firstLineInp = document.getElementById(`lbl-in-${{key}}-0`);
      if (firstLineInp) firstLineInp.focus();
    }}
  }}
}}

function handleCase8Input(period, num, cIdx, silent) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.cases8 || !q.cases8[cIdx]) return;
  const key = period + num;
  const inp = document.getElementById(`case8-in-${{key}}-${{cIdx}}`);
  const box = document.getElementById(`case8-box-${{key}}-${{cIdx}}`);
  const targetEl = document.getElementById(`case8-target-${{key}}-${{cIdx}}`);
  if (!inp) return;

  const val = inp.value.trim();
  localStorage.setItem(getRoundKeyPrefix() + key + '_C' + cIdx, val);
  if (!silent) playPenStrokeSound();

  const targetAns = q.cases8[cIdx].a;
  const isSolved = val.length >= 1 && isKeywordSolvedInText(targetAns, val);
  const wasSolved = inp.classList.contains('match');

  inp.classList.toggle('match', isSolved);
  if (box) box.classList.toggle('solved', isSolved);
  if (targetEl) {{
    targetEl.innerHTML = formatTextWithBlanks(targetAns, [targetAns], isSolved ? targetAns : val);
  }}
  if (isSolved && !wasSolved && !silent) {{
    playMiniHitSound();
    if (typeof incrementCombo === 'function') incrementCombo();
  }}
  updateCases8Counter(period, num, q.cases8.length);
}}

function updateCases8Counter(period, num, totalCases) {{
  const key = period + num;
  let solvedCount = 0;
  for (let i = 0; i < totalCases; i++) {{
    const inp = document.getElementById(`case8-in-${{key}}-${{i}}`);
    if (inp && inp.classList.contains('match')) solvedCount++;
  }}
  const badge = document.getElementById(`cases8-count-${{key}}`);
  if (badge) {{
    badge.textContent = solvedCount === totalCases
      ? `🏆 ${{solvedCount}} / ${{totalCases}} 완벽 격파!`
      : `${{solvedCount}} / ${{totalCases}} 격파`;
    badge.style.color = solvedCount === totalCases ? '#34d399' : '#fde047';
  }}
}}

function fillAllCases8ForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.cases8) return;
  const key = period + num;
  q.cases8.forEach((c, cIdx) => {{
    const inp = document.getElementById(`case8-in-${{key}}-${{cIdx}}`);
    if (inp) {{
      inp.value = c.a;
      handleCase8Input(period, num, cIdx, true);
    }}
  }});
  playSuccessChime();
  showToast('⚡ 경우의 수 8개 핵심 키워드가 모두 채워졌습니다!');
}}

function clearCases8ForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.cases8) return;
  const key = period + num;
  q.cases8.forEach((c, cIdx) => {{
    const inp = document.getElementById(`case8-in-${{key}}-${{cIdx}}`);
    if (inp) {{
      inp.value = '';
      handleCase8Input(period, num, cIdx, true);
    }}
  }});
  showToast('경우의 수 8개 입력창을 비웠습니다.');
}}

function fillSkeletonForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const key = period + num;
  const lines = q.lines || q.answer.split('\\n');
  const kwList = q.keywords || extractKeywords(q.answer);

  lines.forEach((ln, idx) => {{
    const blanks = (q.line_blanks && q.line_blanks[idx] && q.line_blanks[idx].length > 0)
      ? q.line_blanks[idx]
      : kwList;
    let skel = ln;
    const sorted = [...new Set(blanks)].sort((a, b) => b.length - a.length);
    sorted.forEach(kw => {{
      const mask = '□'.repeat(kw.length);
      skel = skel.split(kw).join(mask);
    }});
    const inp = document.getElementById(`lbl-in-${{key}}-${{idx}}`);
    if (inp) {{
      inp.value = skel;
      localStorage.setItem(getRoundKeyPrefix() + key + '_L' + idx, skel);
    }}
  }});
  const ta = document.getElementById('ta-' + key);
  if (ta) {{
    const combined = [];
    for (let i = 0; i < lines.length; i++) {{
      combined.push(document.getElementById(`lbl-in-${{key}}-${{i}}`)?.value || '');
    }}
    ta.value = combined.join('\\n');
  }}
  evaluateCard(period, num);
  const firstInp = document.getElementById(`lbl-in-${{key}}-0`);
  if (firstInp) firstInp.focus();
  showToast('✏️ 문장 뼈대가 입력되었습니다! □□□ 자리만 핵심 키워드로 바꿔 치세요.');
}}

function handleLineKeydown(e, key, idx, totalLines, cardIdx) {{
  if (e.key === 'Enter') {{
    e.preventDefault();
    if (idx + 1 < totalLines) {{
      const nextEl = document.getElementById(`lbl-in-${{key}}-${{idx + 1}}`);
      if (nextEl) nextEl.focus();
    }} else {{
      const pedPlatEl = document.getElementById(`ped-plat-in-${{key}}-0`);
      if (pedPlatEl) {{
        pedPlatEl.focus();
        return;
      }}
      const quizEl = document.getElementById(`quiz-in-${{key}}`);
      if (quizEl) quizEl.focus();
      else focusNextCardFirstLine(cardIdx);
    }}
  }}
}}

function handlePedPlatKeydown(e, key, pIdx, totalP, cardIdx) {{
  if (e.key === 'Enter') {{
    e.preventDefault();
    if (pIdx + 1 < totalP) {{
      const nextEl = document.getElementById(`ped-plat-in-${{key}}-${{pIdx + 1}}`);
      if (nextEl) nextEl.focus();
    }} else {{
      const quizEl = document.getElementById(`quiz-in-${{key}}`);
      if (quizEl) quizEl.focus();
      else focusNextCardFirstLine(cardIdx);
    }}
  }}
}}

function handlePedPlatInput(period, num, pIdx, silent) {{
  if (!silent) playPenStrokeSound();
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.ped_platform || !q.ped_platform[pIdx]) return;
  const key = period + num;
  const pItem = q.ped_platform[pIdx];
  const inp = document.getElementById(`ped-plat-in-${{key}}-${{pIdx}}`);
  const badge = document.getElementById(`ped-plat-badge-${{key}}-${{pIdx}}`);
  const targetEl = document.getElementById(`ped-plat-target-${{key}}-${{pIdx}}`);
  if (!inp) return;

  const val = inp.value;
  localStorage.setItem(getRoundKeyPrefix() + key + '_P' + pIdx, val);
  const len = val.length;
  const isOk = (len >= 38 && len <= 45);
  const isOver = len > 45;
  const wasOk = inp.classList.contains('line-ok');

  if (badge) {{
    badge.textContent = `${{len}}자 / 38~45자`;
    badge.className = 'lbl-char-badge' + (isOk ? ' ok' : (isOver ? ' over' : ''));
  }}
  inp.classList.toggle('line-ok', isOk);
  if (targetEl) {{
    const targetInner = formatTextWithBlanks(pItem.text, pItem.blanks || [], val);
    targetEl.innerHTML = `<strong style="color:#34d399; margin-right:6px;">[${{escapeHtml(pItem.label)}}]</strong>${{targetInner}}`;
  }}
  if (isOk && !wasOk && !silent) {{
    playMiniHitSound();
    if (typeof incrementCombo === 'function') incrementCombo();
  }}
}}

function fillPedPlatForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.ped_platform) return;
  const key = period + num;
  q.ped_platform.forEach((pItem, pIdx) => {{
    const inp = document.getElementById(`ped-plat-in-${{key}}-${{pIdx}}`);
    if (inp) {{
      inp.value = pItem.text;
      handlePedPlatInput(period, num, pIdx, true);
    }}
  }});
  playSuccessChime();
  showToast('🏛️ 내 교육학 플랫폼(서론·이처럼~·결론) 문장이 자동 입력되었습니다!');
}}

function clearPedPlatForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q || !q.ped_platform) return;
  const key = period + num;
  q.ped_platform.forEach((pItem, pIdx) => {{
    const inp = document.getElementById(`ped-plat-in-${{key}}-${{pIdx}}`);
    if (inp) {{
      inp.value = '';
      handlePedPlatInput(period, num, pIdx, true);
    }}
  }});
  showToast('내 교육학 플랫폼 입력창을 비웠습니다.');
}}

function handleQuizKeydown(e, cardIdx) {{
  if (e.key === 'Enter') {{
    e.preventDefault();
    focusNextCardFirstLine(cardIdx);
  }}
}}

function focusNextCardFirstLine(cardIdx) {{
  const items = getList();
  if (cardIdx + 1 < items.length) {{
    const nextQ = items[cardIdx + 1];
    const nextKey = currentPeriod + nextQ.num;
    const nextCard = document.getElementById('card-' + nextKey);
    if (nextCard) nextCard.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    const nextInp = document.getElementById(`case8-in-${{nextKey}}-0`) || document.getElementById(`lbl-in-${{nextKey}}-0`) || document.getElementById('ta-' + nextKey);
    if (nextInp) setTimeout(() => nextInp.focus(), 180);
  }}
}}

function handleLineByLineInput(period, num, lineIdx, totalLines) {{
  playPenStrokeSound();
  const key = period + num;
  const combinedLines = [];
  for (let i = 0; i < totalLines; i++) {{
    const inp = document.getElementById(`lbl-in-${{key}}-${{i}}`);
    const val = inp ? inp.value : '';
    combinedLines.push(val);
    localStorage.setItem(getRoundKeyPrefix() + key + '_L' + i, val);
  }}
  const ta = document.getElementById('ta-' + key);
  if (ta) {{
    ta.value = combinedLines.join('\\n');
  }}
  evaluateCard(period, num);
}}

function handleTextareaInput(period, num) {{
  playPenStrokeSound();
  const key = period + num;
  const ta = document.getElementById('ta-' + key);
  if (!ta) return;
  const lines = ta.value.split('\\n');
  for (let i = 0; i < 6; i++) {{
    const inp = document.getElementById(`lbl-in-${{key}}-${{i}}`);
    if (inp) {{
      inp.value = lines[i] || '';
      localStorage.setItem(getRoundKeyPrefix() + key + '_L' + i, inp.value);
    }}
  }}
  evaluateCard(period, num);
}}

function fillAllLinesForCard(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (!q) return;
  const key = period + num;
  const lines = q.lines || q.answer.split('\\n');
  lines.forEach((ln, idx) => {{
    const inp = document.getElementById(`lbl-in-${{key}}-${{idx}}`);
    if (inp) {{
      inp.value = ln;
      localStorage.setItem(getRoundKeyPrefix() + key + '_L' + idx, ln);
    }}
  }});
  const ta = document.getElementById('ta-' + key);
  if (ta) ta.value = lines.join('\\n');
  evaluateCard(period, num);
  showToast('4줄 모범정답이 자동 입력되었습니다.');
}}

function speakCardAnswer(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (q && q.answer) speakAnswer(q.answer);
}}

function handleQuizInputByCard(period, num) {{
  playPenStrokeSound();
  const items = getList();
  const q = items.find(x => x.num === num);
  if (q && q.quiz_a) handleQuizInput(period + num, q.quiz_a);
}}

function handleQuizInput(key, targetAns) {{
  const el = document.getElementById('quiz-in-' + key);
  if (!el) return;
  const val = el.value.trim();
  localStorage.setItem(getRoundKeyPrefix() + key + '_quiz', val);
  const isOk = val.length >= 2 && isKeywordSolvedInText(targetAns, val);
  el.classList.toggle('match', isOk);
  const quizTarget = document.getElementById('quiz-target-' + key);
  if (quizTarget) {{
    quizTarget.innerHTML = '정식 키워드 정답: ' + formatTextWithBlanks(targetAns, [targetAns], isOk ? targetAns : val);
  }}
}}

function evaluateCard(period, num) {{
  const key = period + num;
  const ta = document.getElementById('ta-' + key);
  if (!ta) return;
  const text = ta.value;
  const lines = text.split('\\n');
  const chipBox = document.getElementById('chip-box-' + key);
  const evalScore = document.getElementById('eval-score-' + key);

  if (!typingStartTime) typingStartTime = Date.now();
  totalTypedChars += 1;
  const elapsedMin = (Date.now() - typingStartTime) / 60000;
  if (elapsedMin > 0.05) {{
    const wpm = Math.round(totalTypedChars / elapsedMin);
    document.getElementById('wpm-display').textContent = wpm + ' 타/분';
  }}

  const isPed = (period === 'PED');
  const targetLines = isPed ? 6 : 4;
  const minChars = isPed ? 50 : 38;
  const maxChars = isPed ? 60 : 45;

  let chipsHtml = `<span class="chip-item">총 ${{text.length}}자</span>`;
  let validLineCount = 0;
  let hasOverflow = false;

  const items = getList();
  const q = items.find(x => x.num === num);
  const kwList = q ? (q.keywords || extractKeywords(q.answer)) : [];
  const modelLines = q ? (q.lines || q.answer.split('\\n')) : [];

  for (let idx = 0; idx < targetLines; idx++) {{
    const l = lines[idx] || '';
    const len = l.length;
    const isNotSkeleton = !l.includes('□');
    const isOk = (len >= minChars && len <= maxChars && isNotSkeleton);
    const isOver = len > maxChars;
    if (isOk) validLineCount++;
    if (isOver) hasOverflow = true;
    chipsHtml += `<span class="chip-item ${{isOk ? 'perfect' : (isOver ? 'overflow' : '')}}">${{idx+1}}줄:${{len}}자</span>`;

    // Update 1-line badge & input border
    const badge = document.getElementById(`lbl-badge-${{key}}-${{idx}}`);
    const inp = document.getElementById(`lbl-in-${{key}}-${{idx}}`);
    if (badge) {{
      badge.textContent = `${{len}}자 / ${{minC_str(minChars, maxChars)}}`;
      badge.className = 'lbl-char-badge' + (isOk ? ' ok' : (isOver ? ' over' : ''));
    }}
    if (inp) {{
      const wasLineOk = inp.classList.contains('line-ok');
      inp.classList.toggle('line-ok', isOk);
      if (isOk && !wasLineOk) {{
        playMiniHitSound();
        if (typeof incrementCombo === 'function') incrementCombo();
      }}
    }}

    // 핵심키워드 빈칸 모드일 때 타이핑한 줄의 빈칸 실시간 오픈!
    if (q && modelLines[idx]) {{
      const targetTextEl = document.getElementById(`lbl-target-text-${{key}}-${{idx}}`);
      if (targetTextEl) {{
        const lineBlanks = (q.line_blanks && q.line_blanks[idx] && q.line_blanks[idx].length > 0)
          ? q.line_blanks[idx]
          : kwList;
        targetTextEl.innerHTML = formatTextWithBlanks(modelLines[idx], lineBlanks, l);
      }}
    }}
  }}
  chipBox.innerHTML = chipsHtml;
  ta.classList.toggle('error-overflow', hasOverflow);

  let hitCount = 0;
  const missedKws = [];
  if (q) {{
    kwList.forEach((kw, idx) => {{
      const el = document.getElementById(`kw-${{key}}-${{idx}}`);
      const isDetected = isKeywordSolvedInText(kw, text);
      if (isDetected) hitCount++;
      else missedKws.push(kw);
      if (el) {{
        el.classList.toggle('detected', isDetected);
        el.innerHTML = formatTextWithBlanks(kw, [kw], isDetected ? kw : text);
      }}
    }});
  }}

  const kalBar = document.getElementById('kal-rubric-' + key);
  if (kalBar) {{
    if (text.trim().length === 0) {{
      kalBar.innerHTML = '<span>🎯 [KICE 4점 만점 실시간 칼채점] 답안을 입력하면 필수 채점 키워드 적중 점수와 누락 키워드를 즉시 알려줍니다.</span>';
    }} else {{
      const totalKw = kwList.length || 1;
      const estScore = ((hitCount / totalKw) * 4.0).toFixed(1);
      if (hitCount === totalKw) {{
        kalBar.innerHTML = `<span style="color:#34d399;">🏆 [KICE 칼채점: 4.0 / 4.0점] 필수 채점 키워드 ${{hitCount}}/${{totalKw}}개 100% 완벽 적중!</span>`;
      }} else {{
        kalBar.innerHTML = `<span>🎯 [KICE 칼채점: <strong style="color:#fde047;">${{estScore}} / 4.0점</strong>] 적중 ${{hitCount}}/${{totalKw}}개</span><span style="color:#fda4af;">❌ 누락 키워드: ${{escapeHtml(missedKws.join(', '))}}</span>`;
      }}
    }}
  }}

  if (text.trim().length >= 20 && (validLineCount === targetLines || hitCount >= Math.ceil((kwList.length || 1) * 0.5))) {{
    recordDailyDone(key);
  }}

  if (q && text.trim().length >= 10) {{
    const weakLog = JSON.parse(localStorage.getItem('kice_weak_keywords') || '{{}}');
    if (missedKws.length > 0) {{
      weakLog[key] = {{ title: q.title, missed: missedKws }};
    }} else {{
      delete weakLog[key];
    }}
    localStorage.setItem('kice_weak_keywords', JSON.stringify(weakLog));
  }}
  updateMiniMockScoreBanner();

  const wasPerfect = evalScore.getAttribute('data-perfect') === 'true';
  if (text.trim().length === 0) {{
    evalScore.textContent = '판정 대기';
    evalScore.style.color = 'var(--accent-gold)';
    evalScore.setAttribute('data-perfect', 'false');
  }} else if (hasOverflow) {{
    evalScore.textContent = `경고: 한 줄에 ${{maxChars}}자를 초과하여 실제 시험지 칸을 벗어납니다!`;
    evalScore.style.color = 'var(--accent-rose)';
    evalScore.setAttribute('data-perfect', 'false');
  }} else if (validLineCount === targetLines) {{
    evalScore.textContent = `★ ${{targetLines}}줄 B4 규격 100% 만점 일치! (4.0 / 4.0)`;
    evalScore.style.color = 'var(--accent-emerald)';
    evalScore.setAttribute('data-perfect', 'true');
    if (!wasPerfect) playSuccessChime();
  }} else {{
    evalScore.textContent = `현재 작성 중 (규격 일치 ${{validLineCount}}줄 / 목표 ${{targetLines}}줄)`;
    evalScore.style.color = 'var(--accent-blue)';
    evalScore.setAttribute('data-perfect', 'false');
  }}

  localStorage.setItem(getRoundKeyPrefix() + key, text);
  const pill = document.getElementById('nav-pill-' + key);
  if (pill) pill.classList.toggle('done', text.trim().length >= 20);
  updateProgress();
}}

function minC_str(minC, maxC) {{
  return `${{minC}}~${{maxC}}자`;
}}

function updateProgress() {{
  const items = getList();
  let done = 0;
  items.forEach(q => {{
    const saved = localStorage.getItem(getRoundKeyPrefix() + currentPeriod + q.num);
    if (saved && saved.trim().length >= 20) done++;
  }});
  document.getElementById('progress-count').textContent = `${{done}} / ${{items.length}} 완료`;
}}

function loadSavedAnswers() {{
  const items = getList();
  const prefix = getRoundKeyPrefix();
  items.forEach(q => {{
    const key = currentPeriod + q.num;
    const saved = localStorage.getItem(prefix + key);
    if (saved) {{
      const ta = document.getElementById('ta-' + key);
      if (ta) {{
        ta.value = saved;
        const lines = saved.split('\\n');
        lines.forEach((ln, idx) => {{
          const inp = document.getElementById(`lbl-in-${{key}}-${{idx}}`);
          if (inp) inp.value = ln;
        }});
        evaluateCard(currentPeriod, q.num);
      }}
    }}
    if (q.cases8 && q.cases8.length > 0) {{
      q.cases8.forEach((c, cIdx) => {{
        const savedC = localStorage.getItem(prefix + key + '_C' + cIdx);
        if (savedC !== null) {{
          const cInp = document.getElementById(`case8-in-${{key}}-${{cIdx}}`);
          if (cInp) {{
            cInp.value = savedC;
            handleCase8Input(currentPeriod, q.num, cIdx, true);
          }}
        }}
      }});
    }}
    if (q.ped_platform && q.ped_platform.length > 0) {{
      q.ped_platform.forEach((pItem, pIdx) => {{
        const savedP = localStorage.getItem(prefix + key + '_P' + pIdx);
        if (savedP !== null) {{
          const pInp = document.getElementById(`ped-plat-in-${{key}}-${{pIdx}}`);
          if (pInp) {{
            pInp.value = savedP;
            handlePedPlatInput(currentPeriod, q.num, pIdx, true);
          }}
        }}
      }});
    }}
    const savedQuiz = localStorage.getItem(prefix + key + '_quiz');
    if (savedQuiz && q.quiz_a) {{
      const qEl = document.getElementById('quiz-in-' + key);
      if (qEl) {{
        qEl.value = savedQuiz;
        handleQuizInput(key, q.quiz_a);
      }}
    }}
  }});
}}

function toggleMask(period, num) {{
  const el = document.getElementById('ans-' + period + num);
  if (el) el.classList.toggle('masked');
}}

function toggleAllMasks() {{
  allMasked = !allMasked;
  const items = getList();
  items.forEach(q => {{
    const el = document.getElementById('ans-' + currentPeriod + q.num);
    if (el) el.classList.toggle('masked', allMasked);
  }});
  document.querySelectorAll('.lbl-target-line').forEach(el => {{
    el.classList.toggle('masked-hint', allMasked);
  }});
  document.getElementById('btn-toggle-all').textContent = allMasked ? '전체 정답 보기' : '백지연습(정답 가리기)';
}}

function copyModelAnswer(period, num) {{
  const items = getList();
  const q = items.find(x => x.num === num);
  if (q && q.answer) {{
    navigator.clipboard.writeText(q.answer).then(() => showToast('4줄 만점 정답이 복사되었습니다!'));
  }}
}}

function openReportModal() {{
  const modal = document.getElementById('report-modal');
  const container = document.getElementById('report-content');
  const periods = [
    {{ id: 'KICE55', name: '🔥 11.28 결전 55개 KICE 키워드 4줄 정답', total: dataKICE55.length }},
    {{ id: 'TEMPLATE', name: '🎯 임용 만점 4줄 만능 템플릿', total: dataTEMPLATE.length }},
    {{ id: 'PED', name: '1교시 교육학 논술 (16제)', total: dataPED.length }},
    {{ id: 'A', name: '2교시 전공 A형 (12제)', total: dataA.length }},
    {{ id: 'B', name: '3교시 전공 B형 (11제)', total: dataB.length }}
  ];

  let html = '';
  let grandTotal = 0;
  let grandDone = 0;

  periods.forEach(p => {{
    let done = 0;
    for (let i = 1; i <= p.total; i++) {{
      const val = localStorage.getItem(getRoundKeyPrefix() + p.id + i) || '';
      if (val.trim().length >= 20) done++;
    }}
    grandTotal += p.total;
    grandDone += done;
    const rate = Math.round((done / p.total) * 100);

    html += `
      <div class="report-row">
        <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.9rem;">
          <span>${{p.name}}</span>
          <span style="color:#38bdf8;">${{done}} / ${{p.total}} 완료 (${{rate}}%)</span>
        </div>
        <div class="report-bar-wrap">
          <div class="report-bar-fill" style="width: ${{rate}}%"></div>
        </div>
      </div>
    `;
  }});

  const totalRate = Math.round((grandDone / grandTotal) * 100);
  html = `
    <div style="background:#0b1220; padding:16px; border-radius:8px; margin-bottom:16px; text-align:center;">
      <div style="font-size:0.9rem; color:#94a3b8;">전과목 종합 타이핑 달성도</div>
      <div style="font-size:2rem; font-weight:900; color:#fbbf24; margin:4px 0;">${{totalRate}}점 / 100점</div>
      <div style="font-size:0.85rem; color:#34d399;">총 ${{grandTotal}}문항 중 ${{grandDone}}문항 인출 달성!</div>
    </div>
  ` + html;

  container.innerHTML = html;
  modal.style.display = 'flex';
}}

function closeReportModal() {{
  document.getElementById('report-modal').style.display = 'none';
}}

function exportWrongNotes() {{
  const items = getList();
  let txt = `=======================================================================\\n`;
  txt += `[2027학년도 11.28 임용 변귀섭 대표님 55개 KICE 핵심키워드 4줄 정답 요약노트]\\n`;
  txt += `생성일시: ${{new Date().toLocaleString()}}\\n`;
  txt += `=======================================================================\\n\\n`;

  items.forEach(q => {{
    txt += `[#${{String(q.num).padStart(2, '0')}} ${{q.type}}] ${{q.title}}\\n`;
    if (q.keywords) txt += `🔑 핵심 키워드: ${{q.keywords.join(', ')}}\\n`;
    txt += `[KICE 공인 4줄 만점 정답]\\n${{q.answer}}\\n\\n`;
    txt += `-----------------------------------------------------------------------\\n\\n`;
  }});

  const blob = new Blob([txt], {{ type: 'text/plain;charset=utf-8' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `2027_임용_${{currentPeriod}}_4줄만점정답_단권화노트.txt`;
  a.click();
  URL.revokeObjectURL(url);
  showToast('4줄 만점 정답 단권화 노트가 다운로드되었습니다!');
}}

function exportAnswers() {{
  const items = getList();
  let txt = `=======================================================================\\n`;
  txt += `[2027학년도 공립 중등임용시험 ${{currentPeriod}} 답안지]\\n`;
  txt += `수험자: 변귀섭 대표님 | 제출일시: ${{new Date().toLocaleString()}}\\n`;
  txt += `=======================================================================\\n\\n`;

  items.forEach(q => {{
    const key = currentPeriod + q.num;
    const ans = localStorage.getItem(getRoundKeyPrefix() + key) || '(미작성)';
    txt += `[#${{q.num}} - ${{q.type}} (${{q.score}}점)] ${{q.title}}\\n`;
    txt += `작성 답안:\\n${{ans}}\\n\\n`;
    txt += `-----------------------------------------------------------------------\\n\\n`;
  }});

  const blob = new Blob([txt], {{ type: 'text/plain;charset=utf-8' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `2027_임용_${{currentPeriod}}_변귀섭대표님_답안지.txt`;
  a.click();
  URL.revokeObjectURL(url);
  showToast('실전 답안지가 다운로드되었습니다!');
}}

function showToast(msg) {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}}

function escapeHtml(str) {{
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}}

function applyTabletInputAttrs() {{
  document.querySelectorAll('input[type="text"], textarea').forEach(el => {{
    el.setAttribute('autocapitalize', 'off');
    el.setAttribute('autocorrect', 'off');
    el.setAttribute('autocomplete', 'off');
    el.setAttribute('spellcheck', 'false');
    if (el.tagName === 'INPUT') el.setAttribute('enterkeyhint', 'next');
  }});
}}

function init() {{
  updateDDayBadge();
  updateDailyMissionUI();
  renderNav();
  renderCards();
  applyTabletInputAttrs();
  loadSavedAnswers();
  updateProgress();
  startTimer();
  for (let r = 1; r <= 3; r++) {{
    const el = document.getElementById('round-btn-' + r);
    if (el) el.classList.toggle('active', r === currentRound);
  }}
  // 태블릿(iOS/Android) 첫 터치 시 오디오 컨텍스트 자동 활성화
  const unlockAudioOnce = () => {{
    try {{ ensureAudioCtx(); }} catch(e) {{}}
    window.removeEventListener('touchstart', unlockAudioOnce);
  }};
  window.addEventListener('touchstart', unlockAudioOnce, {{ passive: true }});
}}

window.addEventListener('keydown', (e) => {{
  if (e.altKey && e.key === 'ArrowLeft' && isSingleFocusMode) {{
    e.preventDefault();
    stepSingleCard(-1);
  }} else if (e.altKey && e.key === 'ArrowRight' && isSingleFocusMode) {{
    e.preventDefault();
    stepSingleCard(1);
  }}
}});

window.addEventListener('DOMContentLoaded', init);
</script>
</body>
</html>
"""

# Write to all target HTML files in both root and 교육학 folder
target_paths = [
    "2027_전문상담_AB형_타이핑_마스터_웹앱.html",
    "index.html",
    "exam_master_2027.html",
    "2027_KICE_전문상담_핵심키워드_55제_다크모드.html",
    "pedagogy_16_topics.html",
    "counseling_55_topics.html",
    "exam_2027_kice_ab.html",
    os.path.join("..", "index.html"),
    os.path.join("..", "typing_master.html"),
    os.path.join("..", "exam_master_2027.html"),
    os.path.join("..", "2027_dark_55_keywords.html"),
    os.path.join("..", "edu.html"),
    os.path.join("..", "2027_exam_keywords.html"),
]

for p in target_paths:
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Written: {p} ({len(html_content)} bytes)")
