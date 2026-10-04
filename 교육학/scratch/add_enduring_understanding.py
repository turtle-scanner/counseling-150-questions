import json
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('let items = [') + len('let items = ')
end = html.find('];', start) + 1
items = json.loads(html[start:end])

# 1. Upgrade Item 1 (백워드 설계 모형 - 영속적 이해)
items[0] = {
    "num": 1,
    "badge": "교육과정",
    "kw": "백워드 설계 모형 (영속적 이해)",
    "q": "학습자가 세부 사실을 잊어버린 후에도 장기적으로 파지되는 '빅 아이디어(Big Idea)'를 중심으로, 1단계(바라는 결과 확인) --> 2단계(수락할 만한 평가 증거 결정) --> 3단계(학습 경험 및 교수 계획) 순서로 교육과정을 설계하는 위긴스와 맥타이(Wiggins & McTighe) 모형의 명칭과 핵심 목표 개념을 쓸 것.",
    "ans": "학습 내용의 세부 사실을 잊은 뒤에도 유지되는 핵심 개념과 원리를 습득하는 '영속적 이해(Enduring Understanding)'를 도모하며, 목표 설정 후 평가 계획을 수업 설계보다 먼저 수립하여 일관성을 극대화하는 '백워드 설계 모형'이다."
}

# 2. Add New Dedicated Card: 영속적 이해의 6개 측면
new_item = {
    "num": 2,
    "badge": "교육과정",
    "kw": "영속적 이해 6대 측면 (설명·해석·적용·관점·감정이입·자기인식)",
    "q": "위긴스와 맥타이(Wiggins & McTighe)의 백워드 설계에서 '영속적 이해(Enduring Understanding)'의 성취 여부를 평가하는 6가지 세부 이해의 측면 중, '지식을 새로운 상황이나 맥락에 효과적으로 사용하는 능력'과 '타인의 입장과 감정을 직관적으로 수용하고 이해하는 능력'에 해당하는 측면의 공식 명칭을 쓸 것.",
    "ans": "지식을 다양한 실제 맥락에 실천적으로 활용하는 '적용(Application)'과 타인의 가치관과 세계관을 깊이 공감하고 수용하는 '감정이입(Empathy)'이다. (영속적 이해 6대 측면: 설명, 해석, 적용, 관점, 감정이입, 자기인식)"
}

# Insert as second item and renumber subsequent items
new_items = [items[0], new_item]
for idx, it in enumerate(items[1:], start=3):
    it_copy = dict(it)
    it_copy["num"] = idx
    new_items.append(it_copy)

print(f'Total items updated: {len(new_items)}')

# Serialize back to HTML
new_items_json = json.dumps(new_items, ensure_ascii=False)
html = html[:start] + new_items_json + html[end-1:]

# Update title and energy bar
html = html.replace('2027 KICE 핵심 단어장 (200선)', f'2027 KICE 핵심 단어장 ({len(new_items)}선)')
html = html.replace('1 / 200', f'1 / {len(new_items)}')
html = html.replace('총 200개', f'총 {len(new_items)}개')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully injected 영속적 이해 cards!')
