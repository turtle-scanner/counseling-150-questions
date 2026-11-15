# -*- coding: utf-8 -*-
import json

with open("kice_55_4lines_master.json", "r", encoding="utf-8") as f:
    kice55 = {item["id"]: item for item in json.load(f)}

with open("all_exam_master_data.json", "r", encoding="utf-8") as f:
    exam_master = json.load(f)

ped_to_k55 = {
    1: 2,
    2: 5,
    3: 6,
    4: 7,
    5: 8,
    6: 12,
    7: 10,
    8: 11,
    9: 13,
    10: 15,
    11: 14,
    12: 16,
    13: 17,
    14: 18,
    15: 20,
    16: 19,
}

for p in exam_master["pedagogy"]:
    num = p["num"]
    ref = kice55[ped_to_k55[num]]
    p["cases8"] = ref.get("cases8", [])
    p["ped_platform"] = ref.get("ped_platform", [])
    p["quiz_q"] = ref.get("quiz_q", f"{p['title']}의 핵심 채점 키워드는?")
    p["quiz_a"] = ref.get("quiz_a", ", ".join(p.get("keywords", [])[:2]))
    # Build line_blanks for each of the 6 model_answer lines
    lines = p.get("model_answer", [])
    kws = p.get("keywords", []) + ref.get("keywords", [])
    line_blanks = []
    for ln in lines:
        matched = []
        for kw in kws:
            clean_kw = kw.split("(")[0].strip()
            for part in clean_kw.replace("·", ",").split(","):
                part = part.strip()
                if len(part) >= 2 and part in ln and part not in matched:
                    matched.append(part)
        if not matched:
            # pick key noun phrase from line
            words = [w.strip(".,()") for w in ln.split() if len(w.strip(".,()")) >= 3]
            matched = words[1:3] if len(words) >= 3 else words[:1]
        line_blanks.append(matched)
    p["line_blanks"] = line_blanks

# Upgrade A (1~12)
a_to_k55 = {
    1: 48,
    2: 47,
    3: 54,
    4: 50,
    5: 21,
    6: 32,
    7: 36,
    8: 41,
    9: 52,
    10: 55,
    11: 55,
    12: 22,
}

# Custom 4-line (38~45 chars) for fill-in items A1~A4 so they also have 4-line typing practice
a_fillin_lines = {
    1: [
        "기입형 ㉠의 정답은 머레이의 욕구이며 ㉡의 정답은 환경적 압력(압착)이다.",
        "욕구는 행동을 일으키는 내적 힘이며 압력은 외부 환경의 영향력이다.",
        "객관적 실제 환경을 알파 압력이라 하고 주관적 지각을 베타 압력이라 한다.",
        "내담자의 심리적 부적응은 객관적 현실보다 주관적인 베타 압력에 좌우된다."
    ],
    2: [
        "기입형 ㉠의 정답은 나 아닌 나(Not-Me)이며 ㉡은 참여적 관찰자이다.",
        "극심한 불안과 공포로 인해 해리된 무의식적 자아상을 나 아닌 나라 한다.",
        "과거 중요 타인과의 관계 패턴을 현재에 투사하는 현상은 병렬적 왜곡이다.",
        "상담자는 객관적 거리와 대인관계 개입을 병행하는 참여적 관찰자가 된다."
    ],
    3: [
        "기입형 ㉠의 정답은 개방 영역이며 ㉡의 정답은 맹목 영역(Blind Spot)이다.",
        "자신과 타인이 모두 알고 있는 조하리의 창 영역을 개방 영역이라 부른다.",
        "자신은 모르지만 타인은 알고 있는 영역을 맹목 영역이라 하여 피드백을 준다.",
        "자기개방과 피드백 주고받기를 통해 개방 영역을 넓혀 대인관계를 증진한다."
    ],
    4: [
        "기입형 ㉠은 자기긍정-타인긍정이며 ㉡은 자기부정-타인긍정 생활자세이다.",
        "자신과 타인의 가치를 모두 신뢰하는 건강한 태도는 자기긍정-타인긍정이다.",
        "타인에 비해 자신이 무가치하다고 느껴 위축되는 태도는 자기부정-타인긍정이다.",
        "교류분석 상담을 통해 지금-여기의 합리적 판단 기능인 어른 자아를 활성화한다."
    ]
}

for a in exam_master["counselingA"]:
    num = a["num"]
    ref = kice55[a_to_k55[num]]
    a["cases8"] = ref.get("cases8", [])
    a["keywords"] = ref.get("keywords", [])
    a["quiz_q"] = ref.get("quiz_q", "")
    a["quiz_a"] = ref.get("quiz_a", "")
    if num in a_fillin_lines:
        a["lines"] = a_fillin_lines[num]
        a["answer"] = "\n".join(a["lines"])
    else:
        a["lines"] = [ln.strip() for ln in a["answer"].split("\n") if ln.strip()]

    # Build exact line_blanks for each line in a["lines"]
    custom_blanks_a = {
        1: [["욕구", "압력(압착)"], ["욕구", "압력"], ["알파 압력", "베타 압력"], ["베타 압력"]],
        2: [["나 아닌 나(Not-Me)", "참여적 관찰자"], ["나 아닌 나"], ["병렬적 왜곡"], ["참여적 관찰자"]],
        3: [["개방 영역", "맹목 영역"], ["개방 영역"], ["맹목 영역", "피드백"], ["자기개방", "개방 영역"]],
        4: [["자기긍정-타인긍정", "자기부정-타인긍정"], ["자기긍정-타인긍정"], ["자기부정-타인긍정"], ["어른 자아"]],
        5: [["강박장애", "강박성 성격장애"], ["자아 이질적", "자아 동질적"], ["노출 및 반응방지"], ["강박행동을 차단", "자연 소거"]],
        6: [["자살 죽음사고 척도"], ["자살 사고", "실행 위험성"], ["비밀보장의 예외", "보호자"], ["위기관리위원회", "전문 의료기관"]],
        7: [["삼각관계"], ["불안을 흡수", "신체화 증상"], ["정서적 중립성"], ["탈삼각화"]],
        8: [["이분법적 사고", "재앙화"], ["하향 화살표 기법"], ["역기능적 신념"], ["무엇을 의미하는지 질문"]],
        9: [["제한", "성역할 지향 단계"], ["타협"], ["흥미", "사회적 지위"], ["성역할"]],
        10: [["숀 셰이 CASE 모델"], ["제시 사건 최근 사건 과거 사건 즉각 사건"], ["즉각 사건", "자살 계획"], ["지금 여기", "자살 충동"]],
        11: [["제6호 조치"], ["가중 조치"], ["심리치료", "일시보호"], ["출석인정 결석"]],
        12: [["파국적 오해석"], ["생리적 각성", "악순환 증폭"], ["내수용성 노출"], ["안전행동을 차단"]]
    }
    a["line_blanks"] = custom_blanks_a.get(num, ref.get("line_blanks", []))

# Upgrade B (1~11)
b_to_k55 = {
    1: 53,
    2: 49,
    3: 23,
    4: 24,
    5: 34,
    6: 35,
    7: 40,
    8: 37,
    9: 44,
    10: 53,
    11: 55,
}

b_fillin_lines = {
    1: [
        "기입형 ㉠의 정답은 계측성(Calculus)이며 ㉡의 정답은 일관성이다.",
        "육각형 모델에서 흥미 유형 간 심리적 거리가 반비례한다는 개념은 계측성이다.",
        "인접한 유형일수록 심리적 유사성이 높다는 개념을 일관성이라 부른다.",
        "개인의 흥미와 직업 환경의 부합 정도를 나타내는 개념은 일치성이다."
    ],
    2: [
        "기입형 ㉠의 정답은 페르소나(Persona)이며 ㉡의 정답은 동일시이다.",
        "사회적 요구에 부응하기 위해 개인이 쓰는 공적 얼굴을 페르소나라 한다.",
        "사회적 역할을 진정한 자신으로 착각하는 부작용을 페르소나 동일시라 한다.",
        "무의식 속 억압된 그림자를 수용하고 통합하여 온전한 개성화를 이룬다."
    ]
}

for b in exam_master["counselingB"]:
    num = b["num"]
    ref = kice55[b_to_k55[num]]
    b["cases8"] = ref.get("cases8", [])
    b["keywords"] = ref.get("keywords", [])
    b["quiz_q"] = ref.get("quiz_q", "")
    b["quiz_a"] = ref.get("quiz_a", "")
    if num in b_fillin_lines:
        b["lines"] = b_fillin_lines[num]
        b["answer"] = "\n".join(b["lines"])
    else:
        b["lines"] = [ln.strip() for ln in b["answer"].split("\n") if ln.strip()]

    custom_blanks_b = {
        1: [["계측성(Calculus)", "일관성"], ["심리적 거리", "계측성"], ["심리적 유사성", "일관성"], ["일치성"]],
        2: [["페르소나(Persona)", "동일시"], ["공적 얼굴", "페르소나"], ["페르소나 동일시"], ["그림자", "개성화"]],
        3: [["신체증상장애", "질병불안장애"], ["신체 통증 증상"], ["뚜렷한 신체 증상이 없음", "불치병"], ["확인 행동"]],
        4: [["사회적 실용적 의사소통장애", "자폐스펙트럼장애"], ["제한적이고 반복적인 행동 패턴"], ["상동 행동과 집착"], ["화용론적 언어 사용"]],
        5: [["외향형"], ["정서적 자극", "행동 중심"], ["D점수가 음수", "과부하 상태"], ["정서적 통제력 상실"]],
        6: [["자극추구", "위험회피", "충동성"], ["조심성이 결여", "규칙 위반"], ["자율성과 연대감"], ["자율성", "연대감"]],
        7: [["탈숙고(Dereflection)"], ["불안 악순환을 차단", "자발성"], ["역설적 의도"], ["증상을 직면", "스스로 통제"]],
        8: [["밀착된 경계선", "유리된 경계선"], ["실연화"], ["상호작용 패턴", "직접 관찰"], ["명확한 경계선"]],
        9: [["반전"], ["빈의자 기법"], ["승리자", "패배자"], ["자기 통합"]],
        10: [["생애 주제"], ["관심 통제 호기심 자신감"], ["통제"], ["적응 역량"]],
        11: [["지지 제공 단계"], ["참여 유도 단계"], ["비상 연락망"], ["안전계획서"]]
    }
    b["line_blanks"] = custom_blanks_b.get(num, ref.get("line_blanks", []))

with open("all_exam_master_data.json", "w", encoding="utf-8") as f:
    json.dump(exam_master, f, ensure_ascii=False, indent=2)

print("Successfully upgraded all_exam_master_data.json (PED 16, A 12, B 11)!")
