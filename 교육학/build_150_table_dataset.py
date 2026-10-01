import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]
all_data = json.loads(data_str)

def clean_stars(s):
    if not s:
        return ''
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    s = s.replace('*', '')
    return s.strip()

# Partition data
ped_items = [it for it in all_data if '1교시' in it['period']]
career_items = [it for it in all_data if it['domain'] == '진로상담']
test_items = [it for it in all_data if it['domain'] == '심리검사']
pers_group_items = [it for it in all_data if it['domain'] in ['성격심리', '집단상담', '대인관계']]
theory_items = [it for it in all_data if it['domain'] in ['상담이론', '상담기법']]
family_items = [it for it in all_data if it['domain'] == '가족치료']
psychopath_items = [it for it in all_data if it['domain'] == '정신병리']
crisis_behav_play_items = [it for it in all_data if it['domain'] in ['행동치료', '위기상담', '놀이치료']]
law_ethics_super_items = [it for it in all_data if it['domain'] in ['학교폭력법령', '상담윤리', '상담수퍼비전']]

# Build 10 pages of 15 items = 150 items
pages = []

# Page 1: 1교시 교육학 핵심 15선
pages.append({
    'pageNum': 1,
    'pageTitle': '1교시 교육학 핵심 15선 (교육과정·교육방법·교육평가)',
    'items': ped_items[:15]
})

# Page 2: 2교시 진로상담 핵심 15선
pages.append({
    'pageNum': 2,
    'pageTitle': '2교시 전공 A형 [진로상담 핵심 15선] (로, 수퍼, 홀랜드, 갓프레드슨, 사비카스, SCCT)',
    'items': career_items[:15]
})

# Page 3: 2교시 심리검사 핵심 15선
pages.append({
    'pageNum': 3,
    'pageTitle': '2교시 전공 A형 [심리검사 핵심 15선] (MMPI-2-RF 타당도/재구성/특수척도, K-WISC-V)',
    'items': test_items[:15]
})

# Page 4: 2교시 성격심리 & 집단상담 핵심 15선
pages.append({
    'pageNum': 4,
    'pageTitle': '2교시 전공 A형 [성격심리 & 집단상담 핵심 15선] (아들러, 에릭슨, 융, 얄롬 집단상담)',
    'items': pers_group_items[:15]
})

# Page 5: 3교시 상담이론 핵심 15선
pages.append({
    'pageNum': 5,
    'pageTitle': '3교시 전공 B형 [상담이론 핵심 15선] (로저스, 벡, 엘리스, 번 교류분석, 게슈탈트, 의미치료)',
    'items': theory_items[:15]
})

# Page 6: 3교시 가족치료 핵심 15선
pages.append({
    'pageNum': 6,
    'pageTitle': '3교시 전공 B형 [가족치료 핵심 15선] (보웬 다세대/탈삼각화, 미누친 구조적 경계선/부모화, 사티어)',
    'items': family_items[:15]
})

# Page 7: 3교시 정신병리 DSM-5-TR 핵심 15선 (1편)
pages.append({
    'pageNum': 7,
    'pageTitle': '3교시 전공 B형 [정신병리 DSM-5-TR 1편] (강박장애, 조현병 스펙트럼, 양극성 장애, 공황장애)',
    'items': psychopath_items[:15]
})

# Page 8: 3교시 정신병리 DSM-5-TR 핵심 15선 (2편)
pages.append({
    'pageNum': 8,
    'pageTitle': '3교시 전공 B형 [정신병리 DSM-5-TR 2편] (신체증상장애, PTSD, 애착장애, 성격장애 감별)',
    'items': psychopath_items[15:30]
})

# Page 9: 3교시 행동치료 & 위기상담 & 놀이치료 핵심 15선
# If crisis_behav_play_items is 12, fill 3 from remaining family/pers
fill_behav = crisis_behav_play_items[:]
if len(fill_behav) < 15:
    extra = [it for it in family_items[15:] if it not in fill_behav]
    fill_behav.extend(extra[:15 - len(fill_behav)])

pages.append({
    'pageNum': 9,
    'pageTitle': '3교시 전공 B형 [행동치료·위기상담·놀이치료 핵심 15선] (ERP, 숀 셰이 CASE, 안전계획, 랜드레스)',
    'items': fill_behav[:15]
})

# Page 10: 3교시 학교폭력법령 & 상담윤리 & 수퍼비전 핵심 15선
pages.append({
    'pageNum': 10,
    'pageTitle': '3교시 전공 B형 [학교폭력법령·상담윤리·수퍼비전 핵심 15선] (학폭법 16조/17조, 비밀보장, 수퍼비전)',
    'items': law_ethics_super_items[:15]
})

print(f'Total pages created: {len(pages)}')
total_q = sum(len(p['items']) for p in pages)
print(f'Total questions across 10 pages: {total_q}')
assert total_q == 150, f'Expected 150, got {total_q}'
print('Verified: Exactly 150 questions across 10 pages!')

# Save pages to json for generator script
with open('scratch_150_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)
print('Saved scratch_150_pages.json')
